#!/usr/bin/env python3
"""Regenerate selected Week 3-4 Rank 11-15 Type 3 slots with stricter prompts."""
from __future__ import annotations

import json
import subprocess
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TARGETS = [
    (
        "output/Week34_Rank11_FriendshipDayMsg_type3_prompts.json",
        "flatlay",
        "regen_no_rectangle",
        (
            "\n\nSTRICT REGENERATION CORRECTION: remove every notebook, book, loose paper, greeting card, flat blank rectangle, "
            "white rectangle, screen-like object, and large empty prop. Use only the wooden table, small wrapped gift box, soft ribbon, "
            "dried flowers, ceramic cup, and brass bowl. The jewellery is the only jewellery object. Keep the full ring exact and true scale."
        ),
    ),
    (
        "output/Week34_Rank15_NationalBestFriendsDay_type3_prompts.json",
        "flatlay",
        "regen_no_extra_gold",
        (
            "\n\nSTRICT REGENERATION CORRECTION: remove every book, notebook, paper, card, blank rectangle, gold cord, gold bow, "
            "metallic string, jewellery-like decoration, and extra jewellery object. Use only cream fabric surface, silk ribbon spool, "
            "dried flowers, ceramic cup, and a plain wrapped gift box with fabric ribbon. The ring is the single jewellery object, exact design, true scale."
        ),
    ),
]


def output_raw_for(manifest: dict[str, object], suffix: str, slot: str) -> Path:
    final_path = ROOT / manifest["output"][slot]
    return final_path.with_name(final_path.stem + f".{suffix}.raw.png")


def run_one(manifest_path: Path, slot: str, suffix: str, correction: str) -> None:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    cfg = manifest["slots"][slot]
    output_raw = output_raw_for(manifest, suffix, slot)
    output_raw.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "higgsfield",
        "generate",
        "create",
        manifest.get("higgsfield", {}).get("model", "nano_banana_pro"),
        "--prompt",
        cfg["prompt"] + correction,
        "--aspect_ratio",
        manifest.get("higgsfield", {}).get("aspect_ratio", "16:9"),
        "--resolution",
        manifest.get("higgsfield", {}).get("resolution", "2k"),
    ]
    for image in cfg["local_reference_images"]:
        cmd += ["--image", str(ROOT / image)]
    cmd += ["--wait", "--wait-timeout", "20m", "--wait-interval", "5s", "--json"]
    last_error = ""
    for attempt in range(2):
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode == 0:
            data = json.loads(proc.stdout)
            job = data[0] if isinstance(data, list) else data
            with urllib.request.urlopen(job["result_url"], timeout=180) as response:
                output_raw.write_bytes(response.read())
            jobs = manifest.setdefault("higgsfield_jobs", {})
            jobs[f"{slot}_rejected"] = {
                "reason": "visual QA failed: blank rectangle or extra jewellery-like prop",
                "local_raw": str((ROOT / manifest["output"][slot]).with_suffix(".raw.png").relative_to(ROOT)),
            }
            jobs[f"{slot}_accepted"] = {
                "job_id": job.get("id"),
                "result_url": job.get("result_url"),
                "local_raw": str(output_raw.relative_to(ROOT)),
            }
            cfg["prompt"] = cfg["prompt"] + correction
            manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print("REGEN_DONE", manifest_path.relative_to(ROOT), slot, job.get("id"), output_raw.relative_to(ROOT), flush=True)
            return
        last_error = (proc.stderr or proc.stdout or "").strip()
        if attempt == 0:
            time.sleep(45)
    raise SystemExit(f"Regeneration failed for {manifest_path}:{slot}: {last_error}")


def main() -> None:
    for manifest_rel, slot, suffix, correction in TARGETS:
        run_one(ROOT / manifest_rel, slot, suffix, correction)


if __name__ == "__main__":
    main()
