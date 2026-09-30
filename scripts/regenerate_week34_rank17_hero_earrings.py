#!/usr/bin/env python3
"""Regenerate Week 3-4 Rank 17 hero using an earrings SKU for cleaner compliance."""
from __future__ import annotations

import json
import subprocess
import time
import urllib.request
from pathlib import Path

import sys

sys.path.append(str(Path(__file__).resolve().parent))

from build_week34_rank9_10_batch import consolidated, load_csv, prompt_people, raw_image  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_REL = "output/Week34_Rank17_DiwaliGreetingCard_type3_prompts.json"


def main() -> None:
    rows = load_csv("docs/product/Seo Products - consolidated.csv")
    product = consolidated(rows, "The Rohal Huggie Earrings")
    path = ROOT / MANIFEST_REL
    manifest = json.loads(path.read_text(encoding="utf-8"))
    prompt = prompt_people(
        occasion="Diwali greeting card 2026 hero",
        scene=(
            "solo fair-skinned Indian adult woman in an ivory festive blouse standing beside a blurred festive table "
            "with diyas, marigold flowers, cream fabric, and a wrapped gift, upper body portrait, full face and full head visible, "
            "both ears clearly visible, hands completely out of frame, no card facing camera"
        ),
        product_name="The Rohal Huggie Earrings",
        product=product,
        body_part="ear",
        extra_negatives="necklace, pendant, bracelet, bangle, ring, watch, nose ring, hands, cropped face, cropped head, readable card, blank card, phone",
    )
    cfg = {
        **product,
        "alt": "diwali greeting card 2026 hero with The Rohal Huggie Earrings",
        "caption": "Diwali greeting card 2026 mood: The Rohal Huggie Earrings",
        "product": {"code": product["code"], "name": product["name"], "pdp": product["pdp"]},
        "local_reference_images": [
            raw_image("Earrings", "The Rohal Huggie Earrings", "1_body_portrait.png"),
            raw_image("Earrings", "The Rohal Huggie Earrings", "0_primary.png"),
        ],
        "ref_roles": ["body_image", "front_primary"],
        "prompt": prompt,
    }
    out = (ROOT / manifest["output"]["hero"]).with_name((ROOT / manifest["output"]["hero"]).stem + ".regen_earrings_clean.raw.png")
    cmd = [
        "higgsfield",
        "generate",
        "create",
        manifest.get("higgsfield", {}).get("model", "nano_banana_pro"),
        "--prompt",
        cfg["prompt"],
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
            manifest["slots"]["hero"] = cfg
            jobs = manifest.setdefault("higgsfield_jobs", {})
            jobs["hero_rejected_third"] = {
                "reason": "visual QA failed: pendant attempts introduced extra jewellery or cropped face",
                "local_raw": "output/magnific_generated/diwali-greeting-card-hero-2026.regen_portrait_no_hands.raw.png",
            }
            jobs["hero_accepted"] = {"job_id": job.get("id"), "result_url": job.get("result_url"), "local_raw": str(out.relative_to(ROOT))}
            manifest["media_titles"]["hero"] = "diwali greeting card 2026 Hero"
            path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print("REGEN_DONE", MANIFEST_REL, "hero", job.get("id"), out.relative_to(ROOT), flush=True)
            return
        last_error = (proc.stderr or proc.stdout or "").strip()
        if attempt == 0:
            time.sleep(45)
    raise SystemExit(f"Rank 17 earrings hero regeneration failed: {last_error}")


if __name__ == "__main__":
    main()
