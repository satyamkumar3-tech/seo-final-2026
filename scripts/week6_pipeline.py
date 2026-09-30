#!/usr/bin/env python3
"""Week 6 article pipeline wrapper.

This script gives Week 6 a stable command interface:

  python3 -B scripts/week6_pipeline.py produce --ranks 2 --manifest output/week6_rank2.json --timers

It does not hardcode article prose. Instead, it:
1. Reads the Week 6 CSV row(s)
2. Creates/updates a run manifest
3. Writes a precise Codex CLI prompt per rank
4. Launches `codex exec` non-interactively with the required research instructions
5. Stores full Codex output in a timestamped log while showing concise progress
6. Records per-step checkpoints plus success/failure and timings
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
from collections import deque
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import week6_checkpoint

ROOT = Path(__file__).resolve().parents[1]
WEEK6_CSV = ROOT / "output" / "Week6_Gift_Guides_100.csv"
DEFAULT_OUTPUT_DIR = ROOT / "output"
DEFAULT_CODEX_BIN = Path.home() / ".local" / "bin" / "codex"
CHECKPOINT_DIR = DEFAULT_OUTPUT_DIR / "checkpoints"
LOCK_DIR = DEFAULT_OUTPUT_DIR / ".locks"
STATUS_CSV = DEFAULT_OUTPUT_DIR / "Week6_Gift_Guides_100_status.csv"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def local_stamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


class StepTimer:
    def __init__(self, enabled: bool = True) -> None:
        self.enabled = enabled
        self.run_start = time.monotonic()
        self.current_name: str | None = None
        self.current_start: float | None = None

    def _elapsed(self, seconds: float) -> str:
        seconds = max(0, int(seconds))
        minutes, sec = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        if hours:
            return f"{hours}h {minutes}m {sec}s"
        if minutes:
            return f"{minutes}m {sec}s"
        return f"{sec}s"

    def start(self, name: str) -> None:
        self.current_name = name
        self.current_start = time.monotonic()
        if self.enabled:
            print(
                f"STEP START: {name} | time: {datetime.now().strftime('%H:%M:%S')} | "
                f"elapsed: {self._elapsed(self.current_start - self.run_start)}",
                flush=True,
            )

    def done(self, name: str | None = None) -> None:
        now = time.monotonic()
        label = name or self.current_name or "step"
        step_start = self.current_start or now
        if self.enabled:
            print(
                f"STEP DONE: {label} | time: {datetime.now().strftime('%H:%M:%S')} | "
                f"step duration: {self._elapsed(now - step_start)} | "
                f"total elapsed: {self._elapsed(now - self.run_start)}",
                flush=True,
            )
        self.current_name = None
        self.current_start = None


def load_week6_rows() -> dict[int, dict[str, str]]:
    if not WEEK6_CSV.exists():
        raise SystemExit(f"Week 6 CSV not found: {WEEK6_CSV}")
    with WEEK6_CSV.open(newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    out: dict[int, dict[str, str]] = {}
    for row in rows:
        out[int(row["rank"])] = row
    return out


def parse_ranks(value: str) -> list[int]:
    ranks: list[int] = []
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start, end = int(start_s), int(end_s)
            if end < start:
                raise SystemExit(f"Invalid rank range: {part}")
            ranks.extend(range(start, end + 1))
        else:
            ranks.append(int(part))
    seen: set[int] = set()
    unique: list[int] = []
    for rank in ranks:
        if rank not in seen:
            unique.append(rank)
            seen.add(rank)
    if not unique:
        raise SystemExit("No ranks supplied.")
    return unique


def engine_for(row: dict[str, str]) -> str:
    theme = row.get("theme", "").strip().lower()
    category = row.get("category_fit", "").strip().lower()
    if "how-to" in theme or "education" in theme or "buying" in category:
        return "buying_guide"
    if "design" in theme or "jewellery design" in category:
        return "design_listicle"
    if "gift" in theme or "gifting" in category:
        return "gift_guide"
    return "week6_general"


def category_hint_for(row: dict[str, str], engine: str) -> str:
    primary = row.get("primary", "").lower()
    category = row.get("category_fit", "").lower()
    if "gold" in primary or "purity" in primary or "karat" in primary or "carat" in primary:
        return "`Gold` 554493348 + `Jewellery Problem & Solution` 554493465"
    if "size" in primary or "measure" in primary:
        return "`Jewellery Problem & Solution` 554493465"
    if "wedding" in primary or "bride" in primary or "marriage" in primary:
        return "`Gift` 554493424 + `Wedding Jewellery` 554493443"
    if "kids" in primary or "teenage" in primary:
        return "`Kids Jewellery` 554493433 if product fit is kids-specific, otherwise `Jewellery Trends` 554493317"
    if "men" in primary or "father" in primary or "husband" in primary or "brother" in primary:
        return "`Men's Jewellery` 554493434 where product fit is men's jewellery; otherwise `Gift` 554493424"
    if engine == "design_listicle":
        return "`Jewellery Trends` 554493317 or `Jewellery & Lifestyle` 554493425"
    if "seasonal" in category:
        return "`Gift` 554493424 + `Festive Wishes` 554493477"
    if engine == "gift_guide":
        return "`Gift` 554493424"
    return "Use `docs/WEEK6_CLUSTER_PLAYBOOK.md` category mapping"


def load_manifest(path: Path) -> dict[str, Any]:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {
        "pipeline": "week6_pipeline",
        "created_at": utc_now(),
        "workspace": str(ROOT),
        "week6_csv": rel(WEEK6_CSV),
        "runs": [],
    }


def save_manifest(path: Path, data: dict[str, Any]) -> None:
    data["updated_at"] = utc_now()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_run(manifest: dict[str, Any], run: dict[str, Any]) -> None:
    manifest.setdefault("runs", []).append(run)


def checkpoint_path_for(rank: int) -> Path:
    return CHECKPOINT_DIR / f"week6_rank{rank}.json"


def published_status_row(rank: int) -> dict[str, str] | None:
    if not STATUS_CSV.exists():
        return None
    with STATUS_CSV.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            if row.get("rank") == str(rank) and row.get("status", "").lower() == "published":
                return row
    return None


def completed_rank(rank: int) -> dict[str, Any] | None:
    checkpoint_path = checkpoint_path_for(rank)
    checkpoint = week6_checkpoint.load(checkpoint_path)
    if checkpoint.get("status") in {"complete", "skipped"}:
        return {
            "source": rel(checkpoint_path),
            "status": checkpoint.get("status"),
            "outcome": checkpoint.get("outcome"),
            "live_url": checkpoint.get("live_url") or checkpoint.get("conflicting_url"),
            "wp_post_id": checkpoint.get("wp_post_id") or checkpoint.get("conflicting_post_id"),
        }
    status_row = published_status_row(rank)
    if status_row:
        return {
            "source": rel(STATUS_CSV),
            "live_url": status_row.get("blog_url"),
            "wp_post_id": status_row.get("wp_post_id"),
        }
    return None


def initialize_checkpoint(path: Path, row: dict[str, str]) -> dict[str, Any]:
    def update(data: dict[str, Any]) -> None:
        data.setdefault("pipeline", "week6")
        data.setdefault("rank", int(row["rank"]))
        data.setdefault("slug", row["slug"])
        data.setdefault("primary", row["primary"])
        data.setdefault("created_at", utc_now())
        data.setdefault("status", "pending")
        steps = data.setdefault("steps", {})
        for step in week6_checkpoint.STEPS:
            steps.setdefault(step, {"status": "pending"})

    return week6_checkpoint.mutate(path, update)


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
                or checkpoint.get("conflicting_url")
                or ""
            ),
            "wp_post_id": str(
                publish.get("wp_post_id")
                or checkpoint.get("wp_post_id")
                or checkpoint.get("conflicting_post_id")
                or ""
            ),
            "status": status,
            "carousel_media": str(publish.get("carousel_media_ids") or ""),
            "type3_media": str(patch.get("type3_media_ids") or ""),
            "lines": str(draft.get("section_lines") or ""),
            "visible_words": str(qa.get("visible_words") or ""),
            "notes": notes,
        }
        by_rank = {item.get("rank"): item for item in existing}
        by_rank[row["rank"]] = record
        ordered = sorted(by_rank.values(), key=lambda item: int(item.get("rank") or 0))
        fd, temp_name = tempfile.mkstemp(prefix=f".{STATUS_CSV.name}.", dir=STATUS_CSV.parent)
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(ordered)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temp_name, STATUS_CSV)
        finally:
            if os.path.exists(temp_name):
                os.unlink(temp_name)


def finalize_checkpoint(
    path: Path,
    *,
    success: bool,
    final_text: str,
    exit_code: int,
) -> dict[str, Any]:
    url_match = re.search(r"https://blog\.bluestone\.com/[^\s|)>]+/?", final_text)
    post_match = re.search(r"(?:WP post ID|WordPress post ID)\s*\|?\s*:?[\s*`]*(\d+)", final_text, re.I)

    def update(data: dict[str, Any]) -> None:
        data["last_exit_code"] = exit_code
        steps = data.setdefault("steps", {})
        reported_outcome = str(steps.get("final_report", {}).get("outcome") or "")
        duplicate_block = reported_outcome.startswith("blocked_") or bool(
            re.search(r"safely stopped at the duplicate gate|new article[^\n]*not created", final_text, re.I)
        )
        publish = steps.get("publish_wordpress", {})
        qa = steps.get("live_qa", {})
        published_and_verified = (
            publish.get("status") == "done"
            and bool(publish.get("wp_post_id"))
            and qa.get("status") == "done"
            and str(qa.get("result", "")).lower() == "passed"
        )
        if success and duplicate_block:
            duplicate = steps.get("duplicate_check", {})
            data["status"] = "blocked"
            data["outcome"] = reported_outcome or "blocked_duplicate_intent"
            data["blocked_at"] = utc_now()
            data["conflicting_url"] = duplicate.get("conflicting_url") or (
                url_match.group(0).rstrip(".,") if url_match else None
            )
            data["conflicting_post_id"] = duplicate.get("conflicting_post_id") or (
                int(post_match.group(1)) if post_match else None
            )
            data.pop("live_url", None)
            data.pop("wp_post_id", None)
        elif success and published_and_verified:
            data["status"] = "published_pending_status"
            data["live_url"] = publish.get("live_url") or (
                url_match.group(0).rstrip(".,") if url_match else None
            )
            data["wp_post_id"] = int(publish.get("wp_post_id") or post_match.group(1))
        elif success:
            data["status"] = "incomplete"
            data["outcome"] = reported_outcome or "successful_exit_without_published_live_qa"
        else:
            data["status"] = "failed"
            data["failed_at"] = utc_now()

    return week6_checkpoint.mutate(path, update)


def complete_checkpoint_after_status(path: Path) -> dict[str, Any]:
    def update(data: dict[str, Any]) -> None:
        entry = data.setdefault("steps", {}).setdefault("update_status", {})
        entry["status"] = "done"
        entry["finished_at"] = utc_now()
        entry["confirmed_by"] = "atomic_pipeline_upsert"
        entry["status_csv"] = "upserted"
        entry.pop("blocker", None)
        data["status"] = "complete"
        data["completed_at"] = utc_now()

    return week6_checkpoint.mutate(path, update)


@contextmanager
def pipeline_lock():
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    path = LOCK_DIR / "week6_pipeline.lock"
    with path.open("a+", encoding="utf-8") as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise SystemExit(
                "Another Week 6 pipeline is already running in this workspace. "
                "Wait for it to finish before starting another terminal."
            ) from exc
        yield


def prompt_for_rank(
    row: dict[str, str],
    engine: str,
    category_hint: str,
    timers: bool,
    checkpoint_path: Path,
    checkpoint: dict[str, Any],
) -> str:
    rank = row["rank"]
    primary = row["primary"]
    slug = row["slug"]
    theme = row["theme"]
    category_fit = row["category_fit"]
    volume = row["volume"]
    kd = row["kd"]
    score = row["score"]
    checkpoint_rel = rel(checkpoint_path)
    checkpoint_steps = {
        name: details.get("status", "pending")
        for name, details in checkpoint.get("steps", {}).items()
    }

    timer_block = ""
    if timers:
        timer_block = """
Progress display requirement:
Before starting each major step, print:
STEP START: <step name> | time: <current time> | elapsed: <elapsed since run start>

After finishing each major step, print:
STEP DONE: <step name> | time: <current time> | step duration: <duration> | total elapsed: <elapsed>

Use these steps:
1. Read required docs
2. Verify Higgsfield status and report credits/plan
3. Inspect Week 6 target row
4. Check duplicate slug
5. Fact-check current sources if the topic is factual/current
6. Build H2 keyword map
7. Select article structure and visual concept
8. Draft full article
9. Select products/media only where useful for intent
10. Publish WordPress post
11. Generate Type 3 images through Higgsfield CLI
12. Patch images into WordPress
13. Run live QA
14. Update status files
15. Final report
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

Generate Week 6 Rank {rank} end-to-end.

Target row:
- Rank: {rank}
- Primary keyword: {primary}
- Volume: {volume}
- KD: {kd}
- Score: {score}
- Theme: {theme}
- Category fit: {category_fit}
- Suggested slug: {slug}
- Article engine: {engine}
- Category hint: {category_hint}

Checkpoint and idempotency:
- Checkpoint file: `{checkpoint_rel}`
- Existing step state: {json.dumps(checkpoint_steps, ensure_ascii=False)}
- Before each major step, read the checkpoint. If that step is already `done`, verify its recorded artifact or external ID and SKIP the side effect.
- Mark each step `running`, then `done` or `failed` with:
  `python3 -B scripts/week6_checkpoint.py mark --path {checkpoint_rel} --step <step_name> --status <status> [--detail key=value]`
- Step names in order: {', '.join(week6_checkpoint.STEPS)}.
- WordPress create is exactly-once: reuse a tracked matching post ID; if the slug already exists without a trusted matching ID, stop instead of creating another post.
- Reuse recorded Higgsfield jobs, downloaded image files, carousel media IDs, and Type 3 media IDs. Do not regenerate or re-upload a completed slot unless the user explicitly requested a replacement.
- Update the status CSV by rank and product rotation by SKU as upserts, never blind append operations.
- Do not modify shared helper scripts during an article production run. If a required capability is missing, mark the relevant checkpoint failed and report the blocker.

Mandatory gates:
- Verify Higgsfield status/balance first using the active working path, MCP balance if available or CLI `higgsfield account status --json`.
- Do not generate Type 3 images until Higgsfield status succeeds.
- New WordPress post only. Check duplicate slug before publishing.
- Week 6 CSV has no supporting keyword or competitor URL column. Do not invent a competitor URL. Use natural supporting phrases and report them as inferred unless backed by supplied data.
- Build an H2 keyword map. Label every major H2 as primary-backed, supporting-keyword-backed, competitor-structure-backed, or intent-inferred. Do not claim volume/KD for inferred H2s.
- Use the Week 6 engine rules from docs/WEEK6_CLUSTER_PLAYBOOK.md.
- If the topic touches GST, hallmarking, purity standards, gold buying dates, measurement charts, BIS rules, or other current facts, use live web search and cite reliable factual sources.
- Use editorial Type 3 captions that name the product and reflect intent. Do not use robotic captions like `detail: Product`, `look: Product`, or `vibe: Product`.
- Type 3 hero + lifestyle must obey body_image hard gate. Never generate people shots from packshots alone.
- If Higgsfield generation or queue errors happen, wait 40 to 50 seconds before retrying once.
- No prices, no fake stats, no competitor digs.
- No em dashes, en dashes, or spaced hyphens.
- Update output/Week6_Gift_Guides_100_status.csv and product_rotation.json when done.

{timer_block}
Final report must include:
- live URL
- WP post ID
- article engine used
- categories used
- article length in visible words
- H2 keyword map
- supporting phrases used and whether inferred or backed
- competitor URL status
- factual sources used, if applicable
- carousel media IDs
- Type 3 media IDs
- product SKUs used
- duplicate/cannibalization note
"""


def codex_command(args: argparse.Namespace, prompt: str, final_path: Path) -> list[str]:
    cmd = [
        args.codex_bin,
        "exec",
        "--cd",
        str(ROOT),
        "--skip-git-repo-check",
        "--output-last-message",
        str(final_path),
    ]
    if args.approve_for_me:
        # Current Codex CLI versions make this flag mutually exclusive with
        # --sandbox because approval routing already uses workspace-write.
        cmd.append("--approve-for-me")
    else:
        cmd.extend(["--sandbox", args.sandbox])
    if args.model:
        cmd.extend(["--model", args.model])
    cmd.append(prompt)
    return cmd


ANSI_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
IMPORTANT_LINE_RE = re.compile(
    r"^(?:STEP (?:START|DONE):|PROGRESS:|published new post\b|updated existing tracked post\b|"
    r"Post updated! URL:|LIVE_QA_(?:PASSED|FAILED)|DONE\s+output/|FAILED\s+|ERROR\b|Error\b|"
    r"Traceback \(most recent call last\):|Higgsfield account:|Higgsfield balance:)",
    re.I,
)


def clean_terminal_line(line: str) -> str:
    return ANSI_RE.sub("", line).strip()


def format_duration(seconds: float) -> str:
    seconds_i = max(0, int(seconds))
    minutes, sec = divmod(seconds_i, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}h {minutes}m {sec}s"
    if minutes:
        return f"{minutes}m {sec}s"
    return f"{sec}s"


def stream_command(
    cmd: list[str],
    log_path: Path,
    *,
    rank: int,
    verbose: bool,
    heartbeat_seconds: int,
) -> int:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w", encoding="utf-8") as log:
        log.write("COMMAND:\n")
        log.write(json.dumps(cmd, indent=2) + "\n\n")
        log.write("OUTPUT:\n")
        log.flush()
        proc = subprocess.Popen(
            cmd,
            cwd=str(ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        assert proc.stdout is not None

        output_queue: queue.Queue[str | None] = queue.Queue()
        recent: deque[str] = deque(maxlen=80)

        def read_output() -> None:
            for output_line in proc.stdout:
                output_queue.put(output_line)
            output_queue.put(None)

        reader = threading.Thread(target=read_output, daemon=True)
        reader.start()
        started = time.monotonic()
        next_heartbeat = started + max(10, heartbeat_seconds)

        while True:
            try:
                line = output_queue.get(timeout=1)
            except queue.Empty:
                line = ""

            if line is None:
                break
            if line:
                log.write(line)
                log.flush()
                clean = clean_terminal_line(line)
                if clean:
                    recent.append(clean)
                    if verbose:
                        print(line, end="", flush=True)
                    elif IMPORTANT_LINE_RE.search(clean):
                        print(clean, flush=True)

            now = time.monotonic()
            if not verbose and now >= next_heartbeat:
                print(
                    f"PROGRESS: Week 6 Rank {rank} agent is running | "
                    f"elapsed: {format_duration(now - started)} | full log: {rel(log_path)}",
                    flush=True,
                )
                next_heartbeat = now + max(10, heartbeat_seconds)

        code = proc.wait()
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


def print_final_summary(final_path: Path, duration: float) -> None:
    if not final_path.exists():
        print(f"Final report was not created: {rel(final_path)}", flush=True)
        return
    text = final_path.read_text(encoding="utf-8", errors="replace")
    urls = re.findall(r"https://blog\.bluestone\.com/[^\s|)>]+/?", text)
    url = urls[0].rstrip(".,") if urls else None
    post = re.search(r"(?:WP post ID|WordPress post ID)\s*\|?\s*:?[\s*`]*(\d+)", text, re.I)
    words = re.search(r"(?:Visible words|Article length)[^\d]*(\d[\d,]*)", text, re.I)
    qa = "passed" if re.search(r"Live QA[^\n]*(?:Passed|PASS)", text, re.I) else "reported"
    stopped = bool(
        re.search(
            r"(?:safely stopped|stopped safely) at the duplicate(?: intent)? gate|"
            r"(?:new article|no new post)[^\n]*(?:not created|was created)",
            text,
            re.I,
        )
    )
    if stopped:
        print("FINAL OUTCOME: STOPPED AT DUPLICATE GATE", flush=True)
        if url:
            print(f"  Conflicting existing blog: {url}", flush=True)
        if post:
            print(f"  Existing WordPress post ID: {post.group(1)}", flush=True)
        print("  New article created: no", flush=True)
        print(f"  Total runtime: {format_duration(duration)}", flush=True)
        print(f"  Full report: {rel(final_path)}", flush=True)
        return
    print("FINAL RESULT", flush=True)
    if url:
        print(f"  Blog: {url}", flush=True)
    if post:
        print(f"  WordPress post ID: {post.group(1)}", flush=True)
    if words:
        print(f"  Article length: {words.group(1)} words", flush=True)
    print(f"  Live QA: {qa}", flush=True)
    print(f"  Total runtime: {format_duration(duration)}", flush=True)
    print(f"  Full report: {rel(final_path)}", flush=True)


def cmd_produce(args: argparse.Namespace) -> None:
    with pipeline_lock():
        cmd_produce_locked(args)


def cmd_produce_locked(args: argparse.Namespace) -> None:
    timer = StepTimer(enabled=args.timers)
    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = ROOT / manifest_path

    timer.start("load Week 6 rows")
    rows = load_week6_rows()
    ranks = parse_ranks(args.ranks)
    missing = [rank for rank in ranks if rank not in rows]
    if missing:
        raise SystemExit(f"Ranks not found in Week 6 CSV: {missing}")
    timer.done()

    timer.start("prepare manifest")
    manifest = load_manifest(manifest_path)
    manifest["requested_ranks"] = ranks
    manifest["codex_bin"] = args.codex_bin
    manifest["skip_git_repo_check"] = True
    manifest["sandbox_requested"] = args.sandbox
    manifest["sandbox_effective"] = "workspace-write (managed by --approve-for-me)" if args.approve_for_me else args.sandbox
    manifest["approve_for_me"] = args.approve_for_me
    manifest["search_requested_in_prompt"] = args.search
    save_manifest(manifest_path, manifest)
    timer.done()

    if args.max_parallel != 1:
        print(
            "NOTE: This pipeline currently runs Codex article jobs sequentially. "
            "The --max-parallel value is recorded for planning, but not used to run multiple Codex agents.",
            flush=True,
        )

    codex_path = shutil.which(args.codex_bin) if os.sep not in args.codex_bin else args.codex_bin
    if not codex_path:
        raise SystemExit(f"Codex CLI not found: {args.codex_bin}")

    for rank in ranks:
        row = rows[rank]
        if not args.force:
            existing = completed_rank(rank)
            if existing:
                disposition = (
                    "was skipped because an existing article satisfies the intent"
                    if existing.get("status") == "skipped"
                    else "is already published"
                )
                print(
                    f"SKIP: Week 6 Rank {rank} {disposition} according to {existing['source']}",
                    flush=True,
                )
                if existing.get("live_url"):
                    print(f"  Blog: {existing['live_url']}", flush=True)
                if existing.get("wp_post_id"):
                    print(f"  WordPress post ID: {existing['wp_post_id']}", flush=True)
                print("  Use --force only for an intentional controlled rerun.", flush=True)
                continue

        engine = engine_for(row)
        category_hint = category_hint_for(row, engine)
        checkpoint_path = checkpoint_path_for(rank)
        checkpoint = initialize_checkpoint(checkpoint_path, row)
        stamp = local_stamp()
        safe_slug = row["slug"].replace("/", "-")
        prompt_path = DEFAULT_OUTPUT_DIR / f"week6_rank{rank}_{safe_slug}_{stamp}.prompt.txt"
        log_path = DEFAULT_OUTPUT_DIR / f"week6_rank{rank}_{safe_slug}_{stamp}.log"
        final_path = DEFAULT_OUTPUT_DIR / f"week6_rank{rank}_{safe_slug}_{stamp}.final.txt"

        timer.start(f"rank {rank}: write prompt")
        prompt = prompt_for_rank(
            row,
            engine,
            category_hint,
            args.timers,
            checkpoint_path,
            checkpoint,
        )
        prompt_path.write_text(prompt, encoding="utf-8")
        cmd = codex_command(args, prompt, final_path)
        run: dict[str, Any] = {
            "rank": rank,
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
            "codex_command": cmd[:-1] + [f"<prompt stored in {rel(prompt_path)}>"],
            "max_parallel_requested": args.max_parallel,
        }
        append_run(manifest, run)
        save_manifest(manifest_path, manifest)
        timer.done()

        print()
        print("=" * 80)
        print(f"Week 6 Rank {rank}: {row['primary']}")
        print(f"Engine: {engine}")
        print(f"Prompt: {rel(prompt_path)}")
        print(f"Log: {rel(log_path)}")
        print(f"Final: {rel(final_path)}")
        print("=" * 80)
        print()

        if args.dry_run:
            print("DRY RUN: not launching Codex CLI.")
            continue

        timer.start(f"rank {rank}: codex exec")
        started = time.monotonic()
        code = stream_command(
            cmd,
            log_path,
            rank=rank,
            verbose=args.verbose,
            heartbeat_seconds=args.heartbeat_seconds,
        )
        duration = time.monotonic() - started
        timer.done()

        final_text = final_path.read_text(encoding="utf-8", errors="replace") if final_path.exists() else ""
        checkpoint = finalize_checkpoint(
            checkpoint_path,
            success=code == 0,
            final_text=final_text,
            exit_code=code,
        )
        if checkpoint.get("status") == "published_pending_status":
            upsert_status_record(
                row,
                checkpoint,
                status="published",
                notes=(
                    f"Completed by {engine} pipeline with checkpointed WordPress, media, "
                    "Type 3 generation, image patching, and passed live QA."
                ),
            )
            checkpoint = complete_checkpoint_after_status(checkpoint_path)

        run["finished_at"] = utc_now()
        run["duration_seconds"] = round(duration, 2)
        run["exit_code"] = code
        run["status"] = str(checkpoint.get("status") or ("done" if code == 0 else "failed"))
        run["checkpoint_status"] = checkpoint.get("status")
        save_manifest(manifest_path, manifest)
        if code == 0:
            print_final_summary(final_path, duration)
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
    runs = data.get("runs", [])
    print(f"Manifest: {rel(manifest_path)}")
    if not runs:
        print("No runs recorded.")
        return
    for run in runs:
        print(
            f"Rank {run.get('rank')}: {run.get('status')} | "
            f"{run.get('primary')} | started {run.get('started_at')} | "
            f"duration {format_duration(float(run.get('duration_seconds') or 0))}"
        )
        if run.get("final_path"):
            print(f"  Final: {run['final_path']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Week 6 SEO article pipeline wrapper")
    sub = parser.add_subparsers(dest="command", required=True)

    produce = sub.add_parser("produce", help="Run Codex CLI for one or more Week 6 ranks")
    produce.add_argument("--ranks", required=True, help="Rank list/range, e.g. 2 or 2-6 or 2,4,7")
    produce.add_argument("--manifest", required=True, help="Manifest JSON path")
    produce.add_argument("--timers", action="store_true", help="Print pipeline timers and ask Codex to print step timers")
    produce.add_argument("--dry-run", action="store_true", help="Write manifest and prompt only; do not run Codex")
    produce.add_argument(
        "--force",
        action="store_true",
        help="Allow an intentional rerun even when the rank is already marked published/complete",
    )
    produce.add_argument(
        "--verbose",
        action="store_true",
        help="Show raw Codex output in the terminal; full raw output is always saved to the log",
    )
    produce.add_argument(
        "--heartbeat-seconds",
        type=int,
        default=30,
        help="Seconds between concise running updates (minimum effective value: 10)",
    )
    produce.add_argument("--continue-on-error", action="store_true", help="Continue to next rank if Codex exits non-zero")
    produce.add_argument("--max-parallel", type=int, default=1, help="Recorded for planning; current wrapper runs sequential Codex jobs")
    produce.add_argument(
        "--codex-bin",
        default=str(DEFAULT_CODEX_BIN) if DEFAULT_CODEX_BIN.exists() else "codex",
        help="Codex executable name/path",
    )
    produce.add_argument("--sandbox", default="workspace-write", choices=["read-only", "workspace-write", "danger-full-access"])
    produce.add_argument(
        "--approve-for-me",
        action="store_true",
        help="Let Codex CLI route approval prompts through automatic review when supported",
    )
    produce.add_argument(
        "--search",
        dest="search",
        action="store_true",
        default=True,
        help="Keep live-source fact-checking instructions in the generated prompt",
    )
    produce.add_argument(
        "--no-search",
        dest="search",
        action="store_false",
        help="Do not ask the article agent to use live-source fact-checking",
    )
    produce.add_argument("--model", default=None, help="Optional Codex model override")
    produce.set_defaults(func=cmd_produce)

    status = sub.add_parser("status", help="Print a manifest")
    status.add_argument("--manifest", required=True)
    status.add_argument("--json", action="store_true", help="Print the complete raw manifest")
    status.set_defaults(func=cmd_status)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
