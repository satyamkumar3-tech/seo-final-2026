#!/usr/bin/env python3
"""Week 7 SEO article pipeline wrapper.

Examples:

  python3 -B scripts/week7_pipeline.py produce --next --manifest output/week7_next.json --timers --approve-for-me
  python3 -B scripts/week7_pipeline.py produce --ranks 8-10 --manifest output/week7_8_10.json --timers --approve-for-me

The wrapper reads the full Week 7 workbook row, creates a per-rank checkpoint,
writes a precise Codex prompt, launches Codex, keeps the terminal concise, and
upserts terminal status by rank. It never reads Week 6 queue rows.
"""
from __future__ import annotations

import argparse
import csv
import fcntl
import json
import os
import queue
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import zipfile
import xml.etree.ElementTree as ET
from collections import deque
from contextlib import contextmanager
from pathlib import Path, PurePosixPath
from typing import Any

import week6_pipeline as common
import week7_checkpoint


ROOT = Path(__file__).resolve().parents[1]
WORKBOOK = ROOT / "SEO Strategy 2026.xlsx"
WEEK7_CSV = ROOT / "output" / "Week7_Gift_Guides_PostRank10.csv"
OUTPUT_DIR = ROOT / "output"
CHECKPOINT_DIR = OUTPUT_DIR / "checkpoints"
LOCK_DIR = OUTPUT_DIR / ".locks"
STATUS_CSV = OUTPUT_DIR / "Week7_Gift_Guides_PostRank10_status.csv"
DEFAULT_CODEX_BIN = Path.home() / ".local" / "bin" / "codex"
DEFAULT_AGY_BIN = Path.home() / ".local" / "bin" / "agy"

MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
DOC_REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"


def utc_now() -> str:
    return common.utc_now()


def local_stamp() -> str:
    return common.local_stamp()


def rel(path: Path) -> str:
    return common.rel(path)


def _column_index(cell_ref: str) -> int:
    match = re.match(r"[A-Z]+", cell_ref)
    if not match:
        raise ValueError(f"Invalid Excel cell reference: {cell_ref}")
    value = 0
    for char in match.group(0):
        value = value * 26 + ord(char) - 64
    return value - 1


def _shared_strings(archive: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in archive.namelist():
        return []
    namespace = {"x": MAIN_NS}
    root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    strings: list[str] = []
    for item in root.findall("x:si", namespace):
        strings.append("".join(node.text or "" for node in item.iterfind(".//x:t", namespace)))
    return strings


def _week7_sheet_path(archive: zipfile.ZipFile) -> str:
    namespace = {"x": MAIN_NS, "r": DOC_REL_NS}
    workbook = ET.fromstring(archive.read("xl/workbook.xml"))
    relation_id: str | None = None
    for sheet in workbook.findall(".//x:sheets/x:sheet", namespace):
        if sheet.attrib.get("name") == "Week 7":
            relation_id = sheet.attrib.get(f"{{{DOC_REL_NS}}}id")
            break
    if not relation_id:
        raise SystemExit("Sheet 'Week 7' was not found in SEO Strategy 2026.xlsx")

    relationships = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    target: str | None = None
    for relation in relationships.findall(f"{{{PKG_REL_NS}}}Relationship"):
        if relation.attrib.get("Id") == relation_id:
            target = relation.attrib.get("Target")
            break
    if not target:
        raise SystemExit("The Week 7 worksheet relationship could not be resolved")
    if target.startswith("/"):
        return target.lstrip("/")
    return str(PurePosixPath("xl") / target)


def _cell_value(cell: ET.Element, shared: list[str]) -> str:
    namespace = {"x": MAIN_NS}
    cell_type = cell.attrib.get("t")
    if cell_type == "inlineStr":
        return "".join(node.text or "" for node in cell.iterfind(".//x:t", namespace))
    value_node = cell.find("x:v", namespace)
    if value_node is None or value_node.text is None:
        return ""
    if cell_type == "s":
        index = int(value_node.text)
        return shared[index] if 0 <= index < len(shared) else ""
    return value_node.text


def _rows_from_workbook() -> list[dict[str, str]]:
    if not WORKBOOK.exists():
        raise FileNotFoundError(WORKBOOK)
    namespace = {"x": MAIN_NS}
    with zipfile.ZipFile(WORKBOOK) as archive:
        shared = _shared_strings(archive)
        sheet_path = _week7_sheet_path(archive)
        sheet = ET.fromstring(archive.read(sheet_path))
        raw_rows: list[list[str]] = []
        for row in sheet.findall(".//x:sheetData/x:row", namespace):
            values: list[str] = []
            for cell in row.findall("x:c", namespace):
                index = _column_index(cell.attrib["r"])
                if index >= len(values):
                    values.extend([""] * (index + 1 - len(values)))
                values[index] = _cell_value(cell, shared).strip()
            raw_rows.append(values)
    if not raw_rows:
        raise SystemExit("The Week 7 sheet is empty")
    headers = raw_rows[0]
    return [
        {header: row[index] if index < len(row) else "" for index, header in enumerate(headers) if header}
        for row in raw_rows[1:]
        if row and any(value for value in row)
    ]


def _minimal_csv_rows() -> list[dict[str, str]]:
    if not WEEK7_CSV.exists():
        raise SystemExit(f"Week 7 CSV not found: {WEEK7_CSV}")
    with WEEK7_CSV.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def _normalise_workbook_row(row: dict[str, str]) -> dict[str, str]:
    return {
        "rank": row.get("Priority Rank", ""),
        "action": row.get("Action", ""),
        "primary": row.get("Primary Keyword", ""),
        "volume": row.get("Volume", ""),
        "kd": row.get("KD", ""),
        "score": row.get("Priority Score", ""),
        "theme": row.get("Theme", ""),
        "category_fit": row.get("Category Fit", ""),
        "slug": row.get("Suggested URL Slug", ""),
        "supporting_keywords": row.get("Supporting Keywords", ""),
        "competitor_url": row.get("CaratLane URL", ""),
        "semrush_page": row.get("Semrush Page", ""),
        "execution_note": row.get("Execution Note", ""),
        "bluestone_blog_url": row.get("Bluestone Blog URL", ""),
        "source": row.get("Source", ""),
        "type": row.get("Type", ""),
    }


def _normalise_csv_row(row: dict[str, str]) -> dict[str, str]:
    return {
        "rank": row.get("rank", ""),
        "action": row.get("action", ""),
        "primary": row.get("primary", ""),
        "volume": row.get("volume", ""),
        "kd": row.get("kd", ""),
        "score": row.get("score", ""),
        "theme": row.get("theme", ""),
        "category_fit": row.get("category_fit", ""),
        "slug": row.get("slug", ""),
        "supporting_keywords": row.get("supporting_keywords", ""),
        "competitor_url": row.get("competitor_url", ""),
        "semrush_page": row.get("semrush_page", ""),
        "execution_note": row.get("execution_note", ""),
        "bluestone_blog_url": row.get("bluestone_blog_url", ""),
        "source": row.get("source", ""),
        "type": row.get("type", ""),
    }


def load_week7_rows() -> dict[int, dict[str, str]]:
    try:
        source_rows = [_normalise_workbook_row(row) for row in _rows_from_workbook()]
        source_name = "workbook"
    except (FileNotFoundError, KeyError, ValueError, zipfile.BadZipFile, ET.ParseError) as error:
        source_rows = [_normalise_csv_row(row) for row in _minimal_csv_rows()]
        source_name = f"csv_fallback:{type(error).__name__}"
    output: dict[int, dict[str, str]] = {}
    for row in source_rows:
        if not row["rank"]:
            continue
        rank = int(float(row["rank"]))
        if rank in output:
            raise SystemExit(f"Duplicate Week 7 rank: {rank}")
        if not row["primary"] or not row["slug"]:
            raise SystemExit(f"Week 7 Rank {rank} is missing primary keyword or slug")
        row["rank"] = str(rank)
        row["row_source"] = source_name
        output[rank] = row
    if not output:
        raise SystemExit("No Week 7 rows were loaded")
    return output


def engine_for(row: dict[str, str]) -> str:
    engine = common.engine_for(row)
    return "week7_general" if engine == "week6_general" else engine


def category_hint_for(row: dict[str, str], engine: str) -> str:
    return common.category_hint_for(row, engine)


def checkpoint_path_for(rank: int) -> Path:
    return CHECKPOINT_DIR / f"week7_rank{rank}.json"


def archive_checkpoint_for_restart(path: Path) -> Path | None:
    """Move an existing checkpoint into an audit archive before a clean rerun."""
    if not path.exists():
        return None
    archive_dir = CHECKPOINT_DIR / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    stamp = local_stamp()
    destination = archive_dir / f"{path.stem}_{stamp}{path.suffix}"
    counter = 1
    while destination.exists():
        destination = archive_dir / f"{path.stem}_{stamp}_{counter}{path.suffix}"
        counter += 1
    path.replace(destination)
    return destination


def initialize_checkpoint(path: Path, row: dict[str, str]) -> dict[str, Any]:
    def update(data: dict[str, Any]) -> None:
        data.setdefault("pipeline", "week7")
        data.setdefault("rank", int(row["rank"]))
        data.setdefault("slug", row["slug"])
        data.setdefault("primary", row["primary"])
        data.setdefault("created_at", utc_now())
        data.setdefault("status", "pending")
        steps = data.setdefault("steps", {})
        for step in week7_checkpoint.STEPS:
            steps.setdefault(step, {"status": "pending"})

    return week7_checkpoint.mutate(path, update)


def terminal_status_row(rank: int) -> dict[str, str] | None:
    if not STATUS_CSV.exists():
        return None
    with STATUS_CSV.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            if row.get("rank") == str(rank) and row.get("status", "").lower() in {
                "published",
                "skipped_existing_intent",
            }:
                return row
    return None


def completed_rank(rank: int) -> dict[str, Any] | None:
    path = checkpoint_path_for(rank)
    checkpoint = week7_checkpoint.load(path)
    if checkpoint.get("status") == "complete":
        return {
            "source": rel(path),
            "status": checkpoint.get("status"),
            "outcome": checkpoint.get("outcome"),
            "live_url": checkpoint.get("live_url") or checkpoint.get("conflicting_url"),
            "wp_post_id": checkpoint.get("wp_post_id") or checkpoint.get("conflicting_post_id"),
        }
    row = terminal_status_row(rank)
    if row:
        return {
            "source": rel(STATUS_CSV),
            "status": row.get("status"),
            "live_url": row.get("blog_url"),
            "wp_post_id": row.get("wp_post_id"),
        }
    return None


def _new_action(row: dict[str, str]) -> bool:
    return row.get("action", "").strip().lower() == "new"


def select_ranks(args: argparse.Namespace, rows: dict[int, dict[str, str]]) -> list[int]:
    if args.ranks:
        ranks = common.parse_ranks(args.ranks)
    else:
        count = int(args.next or 1)
        ranks = []
        for rank in sorted(rows):
            row = rows[rank]
            if _new_action(row) and not completed_rank(rank):
                ranks.append(rank)
                if len(ranks) >= count:
                    break
        if len(ranks) < count:
            raise SystemExit(f"Only {len(ranks)} unfinished Week 7 New rank(s) remain; requested {count}")
    missing = [rank for rank in ranks if rank not in rows]
    if missing:
        raise SystemExit(f"Ranks not found in Week 7: {missing}")
    return ranks


def load_manifest(path: Path) -> dict[str, Any]:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {
        "pipeline": "week7_pipeline",
        "created_at": utc_now(),
        "workspace": str(ROOT),
        "week7_workbook": rel(WORKBOOK),
        "week7_csv": rel(WEEK7_CSV),
        "runs": [],
    }


def save_manifest(path: Path, data: dict[str, Any]) -> None:
    data["updated_at"] = utc_now()
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def append_run(manifest: dict[str, Any], run: dict[str, Any]) -> None:
    manifest.setdefault("runs", []).append(run)


def upsert_status_record(
    row: dict[str, str],
    checkpoint: dict[str, Any],
    *,
    status: str,
    notes: str,
) -> None:
    STATUS_CSV.parent.mkdir(parents=True, exist_ok=True)
    lock_path = STATUS_CSV.with_suffix(STATUS_CSV.suffix + ".lock")
    with lock_path.open("a+", encoding="utf-8") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        existing: list[dict[str, str]] = []
        if STATUS_CSV.exists():
            with STATUS_CSV.open(newline="", encoding="utf-8-sig") as handle:
                existing = list(csv.DictReader(handle))
        fieldnames = [
            "rank",
            "primary",
            "slug",
            "blog_url",
            "wp_post_id",
            "status",
            "carousel_media",
            "type3_media",
            "lines",
            "visible_words",
            "notes",
        ]
        steps = checkpoint.get("steps", {})
        publish = steps.get("publish_wordpress", {})
        duplicate = steps.get("duplicate_check", {})
        patch = steps.get("patch_type3", {})
        draft = steps.get("draft", {})
        qa = steps.get("live_qa", {})
        record = {
            "rank": row["rank"],
            "primary": row["primary"],
            "slug": row["slug"],
            "blog_url": str(
                publish.get("live_url")
                or checkpoint.get("live_url")
                or duplicate.get("conflicting_url")
                or checkpoint.get("conflicting_url")
                or ""
            ),
            "wp_post_id": str(
                publish.get("wp_post_id")
                or checkpoint.get("wp_post_id")
                or duplicate.get("conflicting_post_id")
                or checkpoint.get("conflicting_post_id")
                or ""
            ),
            "status": status,
            "carousel_media": str(publish.get("carousel_media_ids") or ""),
            "type3_media": str(patch.get("type3_media_ids") or ""),
            "lines": str(draft.get("section_lines") or draft.get("section_source_lines") or ""),
            "visible_words": str(qa.get("visible_words") or ""),
            "notes": notes,
        }
        by_rank = {item.get("rank"): item for item in existing}
        by_rank[row["rank"]] = record
        ordered = sorted(by_rank.values(), key=lambda item: int(item.get("rank") or 0))
        descriptor, temp_name = tempfile.mkstemp(prefix=f".{STATUS_CSV.name}.", dir=STATUS_CSV.parent)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(ordered)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temp_name, STATUS_CSV)
        finally:
            if os.path.exists(temp_name):
                os.unlink(temp_name)


def _url_and_post(final_text: str) -> tuple[str | None, int | None]:
    url_match = re.search(r"https://blog\.bluestone\.com/[^\s|)>]+/?", final_text)
    post_match = re.search(
        r"(?:WP post ID|WordPress post ID)\s*\|?\s*:?\s*[`*]*(\d+)",
        final_text,
        re.I,
    )
    url = url_match.group(0).rstrip(".,") if url_match else None
    post_id = int(post_match.group(1)) if post_match else None
    return url, post_id


def finalize_checkpoint(
    path: Path,
    *,
    success: bool,
    final_text: str,
    exit_code: int,
) -> dict[str, Any]:
    url, post_id = _url_and_post(final_text)

    def update(data: dict[str, Any]) -> None:
        data["last_exit_code"] = exit_code
        steps = data.setdefault("steps", {})
        final_report = steps.get("final_report", {})
        reported_outcome = str(final_report.get("outcome") or "")
        duplicate_skip = (
            reported_outcome in {"skipped_existing_intent", "blocked_duplicate_intent"}
            or bool(re.search(r"stopped safely at the duplicate intent gate|stopped at the duplicate gate", final_text, re.I))
            or bool(re.search(r"no new post or media was created", final_text, re.I))
        )
        publish = steps.get("publish_wordpress", {})
        qa = steps.get("live_qa", {})
        published_and_verified = (
            publish.get("status") == "done"
            and bool(publish.get("wp_post_id"))
            and qa.get("status") == "done"
            and str(qa.get("result", "")).lower() == "passed"
        )
        if success and duplicate_skip:
            duplicate = steps.get("duplicate_check", {})
            data["status"] = "status_update_pending"
            data["outcome"] = "skipped_existing_intent"
            data["conflicting_url"] = duplicate.get("conflicting_url") or url
            data["conflicting_post_id"] = duplicate.get("conflicting_post_id") or post_id
            data.pop("live_url", None)
            data.pop("wp_post_id", None)
        elif success and published_and_verified:
            data["status"] = "status_update_pending"
            data["outcome"] = "published"
            data["live_url"] = publish.get("live_url") or url
            data["wp_post_id"] = int(publish.get("wp_post_id") or post_id or 0)
        elif success:
            data["status"] = "incomplete"
            data["outcome"] = reported_outcome or "successful_exit_without_published_live_qa"
        else:
            data["status"] = "failed"
            data["failed_at"] = utc_now()

    return week7_checkpoint.mutate(path, update)


def complete_checkpoint_after_status(path: Path, *, outcome: str) -> dict[str, Any]:
    def update(data: dict[str, Any]) -> None:
        entry = data.setdefault("steps", {}).setdefault("update_status", {})
        entry["status"] = "done"
        entry["finished_at"] = utc_now()
        entry["confirmed_by"] = "week7_pipeline_atomic_upsert"
        entry["status_csv"] = "upserted"
        data["status"] = "complete"
        data["outcome"] = outcome
        data["completed_at"] = utc_now()

    return week7_checkpoint.mutate(path, update)


@contextmanager
def pipeline_lock():
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    path = LOCK_DIR / "week7_pipeline.lock"
    with path.open("a+", encoding="utf-8") as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise SystemExit(
                "Another Week 7 pipeline is already running in this workspace. "
                "Wait for it to finish before starting another Week 7 terminal."
            ) from error
        yield


def prompt_for_rank(
    row: dict[str, str],
    engine: str,
    category_hint: str,
    timers: bool,
    checkpoint_path: Path,
    checkpoint: dict[str, Any],
    allow_existing_intent: bool,
) -> str:
    checkpoint_rel = rel(checkpoint_path)
    checkpoint_steps = {
        name: details.get("status", "pending")
        for name, details in checkpoint.get("steps", {}).items()
    }
    competitor_status = row["competitor_url"] or "blank in source row"
    supporting_status = row["supporting_keywords"] or "blank in source row"
    duplicate_override_block = """
Duplicate-intent handling:
- The normal duplicate-intent gate is active. If an existing live page already satisfies the same intent, stop safely without creating a new post.
"""
    if allow_existing_intent:
        duplicate_override_block = f"""
Explicit duplicate-intent override for this rerun:
- The user explicitly authorized a new Rank {row['rank']} post even if a differently slugged BlueStone article has overlapping search intent.
- Still run and record the complete duplicate check before drafting.
- This override applies only to a semantic-intent conflict with a different slug. It does not permit two posts at the exact target slug.
- If the exact target slug already exists, reuse a trusted post created by this rerun or stop safely. Never create a second exact-slug post.
- Do not modify, redirect, unpublish, or delete the older conflicting article.
- Continue through research, full drafting, WordPress publishing, Type 3 generation, patching, and live QA after documenting the semantic conflict and this approval.
- Differentiate the new article through current official sourcing, clearer calculations, stronger buyer examples, and the supplied Week 7 keyword map. Do not copy the older page.
"""
    timer_block = ""
    if timers:
        timer_block = """
Progress display requirement:
Before each major step, print:
STEP START: <step name> | time: <current time> | elapsed: <elapsed since run start>

After each major step, print:
STEP DONE: <step name> | time: <current time> | step duration: <duration> | total elapsed: <elapsed>

Use these steps:
1. Read required docs
2. Verify Higgsfield status and report credits/plan
3. Inspect the Week 7 target row
4. Check duplicate slug and search intent
5. Analyze the supplied competitor URL and fact-check current sources
6. Filter and map supporting keywords
7. Build the H2 keyword map
8. Select article structure and visual concept
9. Draft the complete article
10. Select products and carousel media
11. Publish the WordPress post
12. Generate Type 3 images through the Higgsfield CLI
13. Patch images and social metadata into WordPress
14. Run live QA
15. Update status files and write the final report
"""

    return f"""Workspace root: final seo generation context

Read these fully before doing task work:
- HANDOFF.md
- docs/SOP_ARTICLE_GENERATION.md
- docs/ARTICLE_WORKFLOW.md
- docs/WEEK6_CLUSTER_PLAYBOOK.md
- docs/HIGGSFIELD_IMAGE_GENERATION.md
- docs/Blog-SEO-AEO-GEO-Checklist-v2.md
- cursor-rules/new-blogs-only.mdc
- cursor-rules/carousel-seo-images.mdc
- cursor-rules/type3-fair-skinned-indians.mdc
- cursor-rules/image-seo.mdc
- cursor-rules/product-rotation-captions-education.mdc

Generate Week 7 Rank {row['rank']} end-to-end.

Source authority:
- Use SEO Strategy 2026.xlsx sheet Week 7 and output/Week7_Gift_Guides_PostRank10.csv.
- Ignore the Week 6 sheet, Week 6 CSV, Week 6 status file, and Week 6 checkpoints completely.
- HANDOFF.md may contain historical Week 6 notes. This Week 7 target block overrides those notes.

Target row:
- Rank: {row['rank']}
- Action: {row['action']}
- Primary keyword: {row['primary']}
- Volume: {row['volume']}
- KD: {row['kd']}
- Priority score: {row['score']}
- Theme: {row['theme']}
- Category fit: {row['category_fit']}
- Suggested slug: {row['slug']}
- Article engine: {engine}
- Category hint: {category_hint}
- Supplied supporting keywords: {supporting_status}
- Supplied competitor URL: {competitor_status}
- Semrush page: {row['semrush_page'] or 'blank'}
- Source execution note: {row['execution_note'] or 'blank'}

{duplicate_override_block}

Checkpoint and idempotency:
- Checkpoint file: {checkpoint_rel}
- Existing step state: {json.dumps(checkpoint_steps, ensure_ascii=False)}
- Before each major step, read the checkpoint. If a step is already done, verify its artifact or external ID and skip its side effect.
- Mark each step running, then done or failed with:
  python3 -B scripts/week7_checkpoint.py mark --path {checkpoint_rel} --step <step_name> --status <status> --detail key=value
- Step names in order: {', '.join(week7_checkpoint.STEPS)}.
- WordPress creation is exactly once. Reuse a trusted matching post ID. If an untracked matching slug exists, stop instead of creating a duplicate.
- Reuse recorded Higgsfield jobs, local images, carousel media IDs, and Type 3 media IDs. Never regenerate or re-upload a completed slot without explicit user approval.
- Update the Week 7 status CSV by rank and product rotation by rank or SKU as upserts, never blind appends.
- Do not modify shared helper scripts during an article production run.

Mandatory content gates:
- CRITICAL RUNTIME EXECUTION GATE — STRICTLY SYNCHRONOUS ONLY:
  * DO NOT spawn background tasks or execute commands with asynchronous delays.
  * Execute ALL python scripts, curl/API calls, Higgsfield generations, and WordPress uploads SYNCHRONOUSLY in the foreground (blocking until full completion).
  * Wait for each command and script to fully complete before calling the next tool or emitting text.
  * NEVER end your turn or output messages like "waiting for background task to finish" while a task is running, as this triggers watchdog idle termination. Run all scripts synchronously from start to finish.
- Confirm this row is Action New. If it is Done or Skip-Existing, stop without publishing.
- Run the duplicate slug and search-intent check before research or drafting. Follow the duplicate-intent handling block above.
- Analyze the supplied competitor URL when present. Use it for intent, structure, omissions, and differentiation. Do not copy wording. If blank, do not invent a competitor URL.
- Audit every supplied supporting keyword for topical relevance. Map relevant phrases naturally into H2s, body, FAQs, and schema. Explicitly reject unrelated or polluted phrases instead of forcing them into the article.
- Build an H2 map and label every major H2 primary-backed, supporting-keyword-backed, competitor-structure-backed, or intent-inferred. Only claim metrics supplied by the Week 7 row.
- Use the appropriate Gift Guide, Buying Guide / Education, or Design Listicle engine from docs/WEEK6_CLUSTER_PLAYBOOK.md. The engine rules are reusable; Week 6 queue data is not.
- Preserve full article depth. Parallel image work never permits shorter content.
- For gift guides, include 5 to 6 useful named BlueStone recommendations with distinct reasons and no prices.
- For buying guides and factual topics, explain calculations and buyer implications clearly. If the topic touches GST, tax, hallmarking, purity, measurements, or regulations, browse current authoritative sources and cite them.
- No prices, fake statistics, unsupported legal or tax claims, or competitor criticism.
- No em dashes, en dashes, or spaced hyphens.
- Author: Always set author to Satyam (ID 270271337) with on-page byline `By Satyam, BlueStone Editorial` and BlogPosting schema author `Satyam`.
- NO HTML TABLES: Never insert raw HTML `<table>` or `<!-- wp:table -->` blocks into the article body. Convert comparison tables to clean structured bullet lists/cards or generate styled PNG graphics and embed as `wp:image`.
- Jewellery Material Truth: BlueStone is a fine gold and diamond jeweller (does not sell silver). Never recolor BlueStone SKUs or describe authentic gold/diamond jewellery as silver in image prompts.
- EXACTLY ONCE CONTENT & NO DUPLICATE SECTIONS: When inserting in-body Type 3 images and schemas during the patch phase, replace image placeholder targets precisely. Never prepend, concatenate, or duplicate the first half of the article. Verify that every H2 heading and section appears exactly once from intro to conclusion.
- STRICT GUTENBERG BLOCK SYNTAX: Every WordPress block comment MUST be strictly formatted with opening and closing hyphens (e.g., `<!-- /wp:paragraph -->`, `<!-- /wp:list -->`, `<!-- /wp:heading -->`, `<!-- /wp:image -->`). Never emit malformed comments like `<!-- /wp:paragraph>` without `--` or typos like `<!-- /wp:paragraph)` with a parenthesis. Verify that no unclosed `<!--` comments exist in the article body before publishing. Every paragraph block MUST explicitly enclose its text in `<p>...</p>` tags (e.g., `<!-- wp:paragraph -->\n<p>Paragraph text...</p>\n<!-- /wp:paragraph -->`). Never leave raw unwrapped text inside paragraph blocks, which causes distinct paragraphs and numbered items to concatenate into a single wall of text in the browser.
- SECTION ORDERING: The "Final Thoughts" / "Conclusion" section MUST ALWAYS BE PLACED BEFORE the "Frequently Asked Questions" section. The Frequently Asked Questions section (with 5 to 7 visible Q&As) must be the final content section directly preceding the trailing JSON-LD schema.
- COMPLETE FAQ & SECTION RENDERING: Every article must include 5 to 7 full FAQ question-and-answer pairs in the visible HTML body directly under the FAQ H2 heading. Live QA must verify that every FAQ question and heading renders in the live browser DOM.
- CLEAN IMAGE CAPTIONS: Use standard `<figcaption>editorial caption</figcaption>` without extra classes to prevent Gutenberg editor recovery warnings.
- MANDATORY 3D COVERFLOW CAROUSEL SYNTAX & STUDIO IMAGERY: The mid-article 6-product carousel MUST strictly use the official 3D Coverflow snippet from `templates/eid_carousel_6_snippet.html` (matching `rudraksh-gold-bracelet-2026` and `mens-black-bracelet-2026`). All 6 carousel images MUST be high-definition studio-styled visuals sourced from `ProductImages/seo images/<Category>/<Product Name>.png` (converted to 960x535 WebP on stone plinths/draped fabric with warm lighting, NEVER plain white packshots). It MUST be inserted as a SINGLE unified `<!-- wp:html -->` block containing: (1) the full `<style>...</style>` (with `.bs-cf-stage {{ height: 360px }}`, `margin: 1.75rem auto 1.25rem`, `.bs-cf-card {{ width: min(420px, 78vw) }}`, `.bs-cf-name {{ white-space: nowrap; overflow: hidden; text-overflow: ellipsis }}`, `.bs-cf-cta {{ background: #111; color: #fff; }}`, `.bs-cf-card.is-pos-0`, `.bs-cf-dots`, etc. with NO `<p>` tags inside), (2) the `<div class="bs-cf" id="bs-cf-<slug>" data-interval="3200" ...>` container with both nav buttons (`.bs-cf-prev`, `.bs-cf-next`), all 6 product cards with initial position classes (`.bs-cf-card is-pos-0 data-index="0"` ... `is-pos--1 data-index="5"`) and dots, and (3) the vanilla JS `<script>(function(){{...}})();</script>` with the `paint()` and `rel()` rotation functions (with NO `<p>` wrappers). Follow immediately ONLY with a single `<!-- wp:paragraph -->\n<p><strong>Curated Design Highlights:</strong> Explore signature ... <a href="<product_url>">Product Name</a> ...</p>\n<!-- /wp:paragraph -->`. NEVER insert a repetitive product bullet list after the carousel. NEVER emit custom unstyled wrappers like `bs-cf-wrap` or `bs-cf-track`, NEVER omit the `<style>` or `<script>` tags, NEVER split style/div/script into multiple separate blocks, and NEVER prepend or wrap lines with single quotes.
- CAROUSEL MEDIA PRE-FLIGHT VERIFICATION: Every single product image URL in the carousel MUST be verified to return HTTP 200 before inserting into WordPress. Never hallucinate, guess, or manually increment upload filenames without checking WordPress media library. Every card MUST display a valid, working image without any broken image icons or fallback alt text.
- MANDATORY RELATED GUIDES SECTION (INTERNAL BLOG CLUSTER): Directly between the "Final Thoughts" / "Conclusion" section and the "Frequently Asked Questions" section, you MUST include a dedicated H2 heading (e.g., `More Gold Buying Guides` or `More Jewellery & Buying Guides`) followed by a paragraph containing 4 to 5 natural, contextual hyperlinks pointing to live, related BlueStone blog articles (e.g., `https://blog.bluestone.com/how-to-check-gold-purity-2026/`, `https://blog.bluestone.com/gst-on-gold-jewellery-in-india-what-youre-actually-paying-in-tax/`, `https://blog.bluestone.com/is-buying-gold-jewellery-online-safe-in-india-the-honest-answer/`, or other published cluster blogs) to establish strong topical authority and connect readers to other blog guides.

Mandatory image gates:
- Verify Higgsfield status first using MCP balance when available or higgsfield account status --json. Report plan and credits. Do not start Type 3 generation until it succeeds.
- Use Higgsfield CLI nano_banana_pro, 16:9, 2k, count 1 per slot.
- Run no more than two Higgsfield generations simultaneously.
- On a queue or generation error, wait 45 seconds and retry once.
- Higgsfield CLI Result URL Rule: When polling or reading Higgsfield job JSON output, extract the image URL directly from `result_url` (e.g., job['result_url'] or job.get('result_url')), not 'results' or 'output'.
- Hero and lifestyle require image reference 1 as BP-PICS body_image and image reference 2 as the design. If a SKU lacks body_image, select another SKU. Never create people shots from packshots alone.
- Product dimensions are product_height_mm and product_width_mm only, explicitly described as jewellery dimensions, not face or body measurements.
- Use analog grain, Kodak Portra color science, highlight halation, creamy bokeh, filmic tonal response, editorial color grading, natural dynamic range, and filmic contrast.
- No empty phones, screens, cards, boards, placards, readable text, logos, or product overlays. Use physical props.
- Use WebP, unique keyword-led alt text, editorial product-specific captions, and no duplicate hero in the body.
- Product Links on Images: Every product image in the article must be wrapped in a direct hyperlink to its BlueStone product page (PDP URL) from `Seo Products - consolidated.csv`. For in-body Type 3 images (flatlay and lifestyle), wrap `<img .../>` in `<a href="<product_url>">` and set Gutenberg block attribute `\"linkDestination\":\"custom\"`. Also link the product name in `<figcaption>` to `<product_url>`. For carousels, ensure every card has `<a class="bs-cf-media" href="<product_url>"><img .../></a>` and `<a class="bs-cf-cta" href="<product_url>">Buy now</a>`.

WordPress and live QA:
- Publish through the existing WordPress API helpers as a new post only after duplicate checks pass.
- Set the accepted hero as featured media and Yoast social image. Prefer the API. If this site's Yoast social-image field is not exposed through REST, use the authenticated editor UI only for that field.
- LIVE QA CAROUSEL GATE: Verify that the published post DOM contains `.bs-cf`, `.bs-cf-stage`, `.bs-cf-card`, and `.bs-cf-dots` (the official 3D Coverflow snippet), and verify via HTTP HEAD that all 6 carousel card image URLs return HTTP 200. If an unstyled `bs-cf-wrap` format or broken/404 image is detected, immediately replace it with the 3D Coverflow template from `templates/eid_carousel_6_snippet.html` and verify before completing.
- Verify the public og:image, canonical URL, visible word count, heading counts, carousel cards, buy links, FAQ schema, BlogPosting schema images, internal links, image formats, unique alt text, captions, author, categories, and prohibited dash or price patterns.
- Update output/Week7_Gift_Guides_PostRank10_status.csv, output/product_rotation.json, the Week 7 workbook row when safely supported, and the checkpoint exactly once.

{timer_block}
Final report must include:
- live URL and WordPress post ID
- article engine, author, and categories
- visible article word count
- primary keyword and supplied metrics
- supporting keywords used and rejected, with reasons
- H2 keyword map
- competitor URL and analysis summary
- factual sources used
- carousel and Type 3 media IDs
- product SKUs and product rotation
- Higgsfield plan, starting balance, jobs, retries, and ending balance when available
- duplicate and cannibalization result
- live og:image verification
"""


def runner_command(args: argparse.Namespace, prompt: str, final_path: Path) -> list[str]:
    if getattr(args, "runner", "agy") == "agy":
        cmd = [
            args.agy_bin,
            "--dangerously-skip-permissions",
            "--print-timeout",
            "45m",
            "--output-format",
            "text",
        ]
        if getattr(args, "model", None):
            cmd.extend(["--model", args.model])
        cmd.extend(["-p", prompt])
        return cmd
    return common.codex_command(args, prompt, final_path)


def codex_command(args: argparse.Namespace, prompt: str, final_path: Path) -> list[str]:
    return runner_command(args, prompt, final_path)


STEP_ORDER = [
    "read_docs",
    "verify_higgsfield",
    "inspect_row",
    "duplicate_check",
    "fact_check",
    "keyword_map",
    "structure_visuals",
    "draft",
    "product_media",
    "publish_wordpress",
    "generate_type3",
    "patch_type3",
    "live_qa",
    "update_status",
    "final_report",
]


def stream_command(
    command: list[str],
    log_path: Path,
    *,
    rank: int,
    verbose: bool,
    heartbeat_seconds: int,
) -> int:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w", encoding="utf-8") as log:
        log.write("COMMAND:\n")
        log.write(json.dumps(command, indent=2) + "\n\nOUTPUT:\n")
        log.flush()
        process = subprocess.Popen(
            command,
            cwd=str(ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        assert process.stdout is not None
        output_queue: queue.Queue[str | None] = queue.Queue()
        recent: deque[str] = deque(maxlen=80)

        def read_output() -> None:
            for output_line in process.stdout:
                output_queue.put(output_line)
            output_queue.put(None)

        reader = threading.Thread(target=read_output, daemon=True)
        reader.start()

        started = time.monotonic()
        current_step_num = 0
        current_step_name = "initializing"
        current_step_started = started
        last_timer_update = 0.0
        line_active = False

        while True:
            try:
                line = output_queue.get(timeout=0.2)
            except queue.Empty:
                line = ""

            if line is None:
                if line_active and not verbose:
                    sys.stdout.write("\n")
                    sys.stdout.flush()
                    line_active = False
                break

            if line:
                log.write(line)
                log.flush()
                cleaned = common.clean_terminal_line(line)
                if cleaned:
                    recent.append(cleaned)
                    if verbose:
                        print(line, end="", flush=True)
                    else:
                        start_match = re.search(r"STEP START:\s*([a-zA-Z0-9_]+)", cleaned, re.I)
                        done_match = re.search(r"STEP DONE:\s*([a-zA-Z0-9_]+)", cleaned, re.I)
                        if start_match:
                            step_raw = start_match.group(1).lower()
                            if step_raw in STEP_ORDER:
                                current_step_num = STEP_ORDER.index(step_raw) + 1
                            else:
                                current_step_num += 1
                            current_step_name = step_raw
                            current_step_started = time.monotonic()
                        elif done_match:
                            step_raw = done_match.group(1).lower()
                            step_dur = time.monotonic() - current_step_started
                            if line_active:
                                sys.stdout.write(f"\r\033[Kstep {current_step_num}: {current_step_name} | completed in {common.format_duration(step_dur)}\n")
                                sys.stdout.flush()
                                line_active = False
                            else:
                                print(f"step {current_step_num}: {current_step_name} | completed in {common.format_duration(step_dur)}", flush=True)
                        elif re.search(r"(?:published new post|Post updated!|LIVE_QA_PASSED|FINAL RESULT)", cleaned, re.I):
                            if line_active:
                                sys.stdout.write("\n")
                                sys.stdout.flush()
                                line_active = False
                            print(cleaned, flush=True)

            now = time.monotonic()
            if not verbose and current_step_num > 0 and (now - last_timer_update >= 0.5):
                step_elapsed = now - current_step_started
                timer_str = f"step {current_step_num}: {current_step_name} | {common.format_duration(step_elapsed)}..."
                sys.stdout.write(f"\r\033[K{timer_str}")
                sys.stdout.flush()
                line_active = True
                last_timer_update = now

        code = process.wait()
        if code != 0 and not verbose:
            useful = [
                line
                for line in recent
                if re.search(r"error|failed|exception|traceback|not permitted|not found", line, re.I)
            ]
            if useful:
                print("ERROR SUMMARY:", flush=True)
                for line in useful[-8:]:
                    print(f"  {line[:500]}", flush=True)
            print(f"Full diagnostic log: {rel(log_path)}", flush=True)
        return code


def cmd_produce(args: argparse.Namespace) -> None:
    with pipeline_lock():
        cmd_produce_locked(args)


def cmd_produce_locked(args: argparse.Namespace) -> None:
    if args.restart and not args.ranks:
        raise SystemExit("--restart requires explicit --ranks so a completed rank cannot be reset accidentally")
    if args.allow_existing_intent and not args.restart:
        raise SystemExit("--allow-existing-intent requires --restart for a clean, auditable rerun")

    timer = common.StepTimer(enabled=args.timers)
    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = ROOT / manifest_path

    timer.start("load Week 7 rows")
    rows = load_week7_rows()
    ranks = select_ranks(args, rows)
    timer.done()

    timer.start("prepare manifest")
    manifest = load_manifest(manifest_path)
    manifest["requested_ranks"] = ranks
    manifest["codex_bin"] = args.codex_bin
    manifest["skip_git_repo_check"] = True
    manifest["sandbox_requested"] = args.sandbox
    manifest["sandbox_effective"] = (
        "workspace-write (managed by --approve-for-me)" if args.approve_for_me else args.sandbox
    )
    manifest["approve_for_me"] = args.approve_for_me
    manifest["search_requested_in_prompt"] = args.search
    manifest["restart_requested"] = args.restart
    manifest["allow_existing_intent"] = args.allow_existing_intent
    save_manifest(manifest_path, manifest)
    timer.done()

    if args.max_parallel != 1:
        print(
            "NOTE: Article jobs run sequentially to protect shared WordPress and status state. "
            "Each article prompt allows up to two concurrent Higgsfield image generations.",
            flush=True,
        )

    if not args.dry_run:
        codex_path = shutil.which(args.codex_bin) if os.sep not in args.codex_bin else args.codex_bin
        if not codex_path:
            raise SystemExit(f"Codex CLI not found: {args.codex_bin}")

    for rank in ranks:
        row = rows[rank]
        if not _new_action(row) and not args.force:
            print(
                f"SKIP: Week 7 Rank {rank} has Action={row['action']}. "
                "Only Action=New rows are generated.",
                flush=True,
            )
            if row.get("bluestone_blog_url"):
                print(f"  Existing blog: {row['bluestone_blog_url']}", flush=True)
            continue
        checkpoint_path = checkpoint_path_for(rank)
        archived_checkpoint: Path | None = None
        if args.restart and not args.dry_run:
            archived_checkpoint = archive_checkpoint_for_restart(checkpoint_path)
            if archived_checkpoint:
                print(
                    f"RESTART: archived the previous Rank {rank} checkpoint at "
                    f"{rel(archived_checkpoint)}",
                    flush=True,
                )

        if not args.force and not args.restart:
            existing = completed_rank(rank)
            if existing:
                print(f"SKIP: Week 7 Rank {rank} is already terminal according to {existing['source']}", flush=True)
                if existing.get("live_url"):
                    print(f"  Blog: {existing['live_url']}", flush=True)
                if existing.get("wp_post_id"):
                    print(f"  WordPress post ID: {existing['wp_post_id']}", flush=True)
                print("  Use --force only for an intentional controlled rerun.", flush=True)
                continue

        engine = engine_for(row)
        category_hint = category_hint_for(row, engine)
        checkpoint = initialize_checkpoint(checkpoint_path, row)
        stamp = local_stamp()
        safe_slug = row["slug"].replace("/", "-")
        prompt_path = OUTPUT_DIR / f"week7_rank{rank}_{safe_slug}_{stamp}.prompt.txt"
        log_path = OUTPUT_DIR / f"week7_rank{rank}_{safe_slug}_{stamp}.log"
        final_path = OUTPUT_DIR / f"week7_rank{rank}_{safe_slug}_{stamp}.final.txt"

        timer.start(f"rank {rank}: write prompt")
        prompt = prompt_for_rank(
            row,
            engine,
            category_hint,
            args.timers,
            checkpoint_path,
            checkpoint,
            args.allow_existing_intent,
        )
        prompt_path.write_text(prompt, encoding="utf-8")
        runner_name = getattr(args, "runner", "agy")
        command = runner_command(args, prompt, final_path)
        run: dict[str, Any] = {
            "rank": rank,
            "action": row["action"],
            "primary": row["primary"],
            "slug": row["slug"],
            "theme": row["theme"],
            "category_fit": row["category_fit"],
            "engine": engine,
            "category_hint": category_hint,
            "status": "dry_run" if args.dry_run else "running",
            "started_at": utc_now(),
            "prompt_path": rel(prompt_path),
            "log_path": rel(log_path),
            "final_path": rel(final_path),
            "checkpoint_path": rel(checkpoint_path),
            "archived_checkpoint_path": rel(archived_checkpoint) if archived_checkpoint else None,
            "allow_existing_intent": args.allow_existing_intent,
            "runner": runner_name,
            "command": command[:-1] + [f"<prompt stored in {rel(prompt_path)}>"],
            "max_parallel_requested": args.max_parallel,
        }
        append_run(manifest, run)
        save_manifest(manifest_path, manifest)
        timer.done()

        print()
        print("=" * 80)
        print(f"Week 7 Rank {rank}: {row['primary']} (Runner: {runner_name})")
        print(f"Engine: {engine}")
        print(f"Prompt: {rel(prompt_path)}")
        print(f"Log: {rel(log_path)}")
        print(f"Final: {rel(final_path)}")
        print("=" * 80)
        print()

        if args.dry_run:
            print(f"DRY RUN: {runner_name.upper()} runner was not launched.", flush=True)
            continue

        timer.start(f"rank {rank}: {runner_name} exec")
        started = time.monotonic()
        code = stream_command(
            command,
            log_path,
            rank=rank,
            verbose=args.verbose,
            heartbeat_seconds=args.heartbeat_seconds,
        )
        duration = time.monotonic() - started
        timer.done()

        if not final_path.exists() and log_path.exists():
            final_path.write_text(log_path.read_text(encoding="utf-8", errors="replace"), encoding="utf-8")

        final_text = final_path.read_text(encoding="utf-8", errors="replace") if final_path.exists() else ""
        checkpoint = finalize_checkpoint(
            checkpoint_path,
            success=code == 0,
            final_text=final_text,
            exit_code=code,
        )
        if checkpoint.get("status") == "status_update_pending":
            outcome = str(checkpoint.get("outcome") or "")
            if outcome == "published":
                status = "published"
                notes = (
                    f"Completed by {engine} with checkpointed WordPress, media, Type 3 generation, "
                    "social metadata verification, and passed live QA."
                )
            else:
                status = "skipped_existing_intent"
                notes = "No new post or media created because an existing live article satisfies the intent."
            upsert_status_record(row, checkpoint, status=status, notes=notes)
            checkpoint = complete_checkpoint_after_status(checkpoint_path, outcome=outcome)

        run["finished_at"] = utc_now()
        run["duration_seconds"] = round(duration, 2)
        run["exit_code"] = code
        run["status"] = str(checkpoint.get("status") or ("done" if code == 0 else "failed"))
        run["checkpoint_status"] = checkpoint.get("status")
        run["outcome"] = checkpoint.get("outcome")
        save_manifest(manifest_path, manifest)
        if code == 0:
            common.print_final_summary(final_path, duration)
        if code != 0 and not args.continue_on_error:
            raise SystemExit(code)

    print()
    print(f"Manifest updated: {rel(manifest_path)}")


def cmd_status(args: argparse.Namespace) -> None:
    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = ROOT / manifest_path
    data = load_manifest(manifest_path)
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    print(f"Manifest: {rel(manifest_path)}")
    runs = data.get("runs", [])
    if not runs:
        print("No runs recorded.")
        return
    for run in runs:
        print(
            f"Rank {run.get('rank')}: {run.get('status')} | {run.get('primary')} | "
            f"duration {common.format_duration(float(run.get('duration_seconds') or 0))}"
        )
        if run.get("final_path"):
            print(f"  Final: {run['final_path']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Week 7 SEO article pipeline wrapper")
    sub = parser.add_subparsers(dest="command", required=True)

    produce = sub.add_parser("produce", help="Run Codex CLI for Week 7 ranks")
    selection = produce.add_mutually_exclusive_group(required=True)
    selection.add_argument("--ranks", help="Rank list/range, for example 8 or 8-12 or 8,10,13")
    selection.add_argument(
        "--next",
        nargs="?",
        const=1,
        type=int,
        metavar="COUNT",
        help="Select the next unfinished Action=New rank, or the next COUNT ranks",
    )
    produce.add_argument("--manifest", required=True, help="Manifest JSON path")
    produce.add_argument("--timers", action="store_true", help="Show wrapper and agent step timers")
    produce.add_argument("--dry-run", action="store_true", help="Write manifest and prompt without launching Codex")
    produce.add_argument(
        "--force",
        action="store_true",
        help="Allow an intentional rerun of a non-New or already terminal rank",
    )
    produce.add_argument(
        "--restart",
        action="store_true",
        help="Archive the existing checkpoint and restart explicitly selected ranks from step one",
    )
    produce.add_argument(
        "--allow-existing-intent",
        action="store_true",
        help="After documenting a differently slugged semantic duplicate, continue this approved rerun",
    )
    produce.add_argument(
        "--verbose",
        action="store_true",
        help="Show raw Codex output; the full output is always saved in the log",
    )
    produce.add_argument(
        "--heartbeat-seconds",
        type=int,
        default=30,
        help="Seconds between concise progress updates, with a minimum effective value of 10",
    )
    produce.add_argument("--continue-on-error", action="store_true")
    produce.add_argument(
        "--max-parallel",
        type=int,
        default=1,
        help="Article jobs remain sequential; prompts allow two concurrent Higgsfield generations",
    )
    produce.add_argument(
        "--runner",
        default="agy",
        choices=["agy", "codex"],
        help="Agent runner to orchestrate: agy (Antigravity) or codex (default: agy)",
    )
    produce.add_argument(
        "--agy-bin",
        default=str(DEFAULT_AGY_BIN) if DEFAULT_AGY_BIN.exists() else "agy",
        help="Antigravity executable name or path",
    )
    produce.add_argument(
        "--codex-bin",
        default=str(DEFAULT_CODEX_BIN) if DEFAULT_CODEX_BIN.exists() else "codex",
        help="Codex executable name or path",
    )
    produce.add_argument(
        "--sandbox",
        default="workspace-write",
        choices=["read-only", "workspace-write", "danger-full-access"],
    )
    produce.add_argument(
        "--approve-for-me",
        action="store_true",
        help="Let Codex CLI route approval prompts through automatic review when supported",
    )
    produce.add_argument("--search", dest="search", action="store_true", default=True)
    produce.add_argument("--no-search", dest="search", action="store_false")
    produce.add_argument("--model", default=None)
    produce.set_defaults(func=cmd_produce)

    status = sub.add_parser("status", help="Print a Week 7 manifest")
    status.add_argument("--manifest", required=True)
    status.add_argument("--json", action="store_true")
    status.set_defaults(func=cmd_status)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
