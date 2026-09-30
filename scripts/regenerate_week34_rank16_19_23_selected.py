#!/usr/bin/env python3
"""Regenerate selected Week 3-4 Rank 16-19 and 23 Type 3 slots."""
from __future__ import annotations

import json
import subprocess
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TARGETS = [
    (
        "output/Week34_Rank16_DiwaliPadwaWishes_type3_prompts.json",
        "hero",
        "regen_full_face_no_extra_jewellery",
        "\n\nSTRICT REGENERATION CORRECTION: full face and full head must be visible with safe top margin. Hands stay low and wrists out of frame. No earrings, no rings, no bracelets, no bangles, no watch, no extra jewellery anywhere. No upright rectangle, no frame, no book, no paper, no card, no screen-like object. The pendant is the only jewellery object and stays true small worn neck scale.",
    ),
    (
        "output/Week34_Rank17_DiwaliGreetingCard_type3_prompts.json",
        "hero",
        "regen_full_face_no_hand_jewellery",
        "\n\nSTRICT REGENERATION CORRECTION: full face and full head visible. Hands may touch flowers only, with wrists out of frame. No earrings, no rings, no bracelets, no bangles, no watch, no extra jewellery anywhere. No card, no book, no paper, no upright rectangle, no screen-like prop. The pendant is the only jewellery object and stays true small worn neck scale.",
    ),
    (
        "output/Week34_Rank19_MissingMotherQuotes_type3_prompts.json",
        "hero",
        "regen_no_frame_full_face",
        "\n\nSTRICT REGENERATION CORRECTION: remove every upright frame, blank rectangle, book, card, paper, photo, memorial prop, and screen-like object. Full face and full head visible with safe margins. No earrings, no rings, no bracelets, no bangles, no watch, no extra jewellery. The pendant is the only jewellery object and stays true small worn neck scale.",
    ),
    (
        "output/Week34_Rank23_DiwaliDesign_type3_prompts.json",
        "hero",
        "regen_full_face_single_wearer",
        "\n\nSTRICT REGENERATION CORRECTION: one solo woman only, full face and full head visible, no split composition, no cropped face, no cropped head, no second body part or second person. Hands and wrists out of frame. No earrings, no rings, no bracelets, no bangles, no watch, no extra jewellery. No card, no poster, no paper, no screen-like prop. The pendant is the only jewellery object and stays true small worn neck scale.",
    ),
]


def raw_out(manifest: dict[str, object], slot: str, suffix: str) -> Path:
    final = ROOT / manifest["output"][slot]
    return final.with_name(final.stem + f".{suffix}.raw.png")


def run_one(manifest_rel: str, slot: str, suffix: str, correction: str) -> None:
    path = ROOT / manifest_rel
    manifest = json.loads(path.read_text(encoding="utf-8"))
    cfg = manifest["slots"][slot]
    out = raw_out(manifest, slot, suffix)
    out.parent.mkdir(parents=True, exist_ok=True)
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
                out.write_bytes(response.read())
            jobs = manifest.setdefault("higgsfield_jobs", {})
            jobs[f"{slot}_rejected"] = {
                "reason": "visual QA failed: cropped face, extra jewellery, or blank rectangle prop",
                "local_raw": str((ROOT / manifest["output"][slot]).with_suffix(".raw.png").relative_to(ROOT)),
            }
            jobs[f"{slot}_accepted"] = {"job_id": job.get("id"), "result_url": job.get("result_url"), "local_raw": str(out.relative_to(ROOT))}
            cfg["prompt"] = cfg["prompt"] + correction
            path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print("REGEN_DONE", manifest_rel, slot, job.get("id"), out.relative_to(ROOT), flush=True)
            return
        last_error = (proc.stderr or proc.stdout or "").strip()
        if attempt == 0:
            time.sleep(45)
    raise SystemExit(f"Regeneration failed for {manifest_rel}:{slot}: {last_error}")


def main() -> None:
    for target in TARGETS:
        run_one(*target)


if __name__ == "__main__":
    main()
