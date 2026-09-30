#!/usr/bin/env python3
"""Regenerate Week 3-4 Rank 17 hero with hands hidden."""
from __future__ import annotations

import json
import subprocess
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_REL = "output/Week34_Rank17_DiwaliGreetingCard_type3_prompts.json"


def main() -> None:
    path = ROOT / MANIFEST_REL
    manifest = json.loads(path.read_text(encoding="utf-8"))
    cfg = manifest["slots"]["hero"]
    correction = (
        "\n\nSTRICT FINAL REGENERATION CORRECTION: compose as upper-body portrait only, from mid chest upward, hands completely hidden and out of frame. "
        "Full face and full head visible with safe top margin. No earrings, no rings, no bracelets, no bangles, no watch, no extra jewellery anywhere. "
        "No card, no book, no paper, no upright rectangle, no screen-like prop. Background may include only blurred diyas, marigold flowers, cream fabric, and a wrapped gift. "
        "The pendant is the only jewellery object and stays true small worn neck scale."
    )
    out = (ROOT / manifest["output"]["hero"]).with_name((ROOT / manifest["output"]["hero"]).stem + ".regen_portrait_no_hands.raw.png")
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
            jobs["hero_rejected_second"] = {
                "reason": "visual QA failed: cropped face and hand jewellery",
                "local_raw": "output/magnific_generated/diwali-greeting-card-hero-2026.regen_full_face_no_hand_jewellery.raw.png",
            }
            jobs["hero_accepted"] = {"job_id": job.get("id"), "result_url": job.get("result_url"), "local_raw": str(out.relative_to(ROOT))}
            cfg["prompt"] = cfg["prompt"] + correction
            path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print("REGEN_DONE", MANIFEST_REL, "hero", job.get("id"), out.relative_to(ROOT), flush=True)
            return
        last_error = (proc.stderr or proc.stdout or "").strip()
        if attempt == 0:
            time.sleep(45)
    raise SystemExit(f"Rank 17 final hero regeneration failed: {last_error}")


if __name__ == "__main__":
    main()
