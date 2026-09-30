#!/usr/bin/env python3
"""Generate Type 3 images for Week 8 Rank 178: Finger Rings for Girls 2026."""
import os
import sys
import json
import time
import subprocess
import urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path("/Users/satyamkumar/Downloads/seo final 2026")
HIGGSFIELD_BIN = Path("/Users/satyamkumar/.local/bin/higgsfield")
if not HIGGSFIELD_BIN.exists():
    HIGGSFIELD_BIN = Path.home() / ".local" / "bin" / "higgsfield"

MANIFEST_PATH = ROOT / "output/Week8_Rank178_FingerRingsForGirls_type3_prompts.json"


def download_and_convert_webp(img_url: str, out_webp: Path, target_width=1400, quality=82):
    out_webp.parent.mkdir(parents=True, exist_ok=True)
    temp_download = out_webp.with_suffix(".tmp")
    req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp, open(temp_download, "wb") as f:
        f.write(resp.read())

    with Image.open(temp_download) as im:
        im = im.convert("RGB")
        w, h = im.size
        if w > target_width:
            new_h = int(h * (target_width / w))
            im = im.resize((target_width, new_h), Image.Resampling.LANCZOS)
        im.save(out_webp, "WEBP", quality=quality)

    if temp_download.exists():
        temp_download.unlink()
    print(f"  Saved converted WebP: {out_webp} ({out_webp.stat().st_size} bytes)")


def run_single_generation(manifest_data, slot_key: str):
    slot_info = manifest_data["slots"][slot_key]
    out_rel = manifest_data["output"][slot_key]
    dest_path = ROOT / out_rel
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Check if hero is already completed from earlier attempt
    if slot_key == "hero":
        known_job_id = "a600f665-db74-4b2d-a7b5-3f68f868f366"
        known_url = "https://d8j0ntlcm91z4.cloudfront.net/user_30dprT6AStriTdilMnAVIyL1c0u/hf_20260916_071839_a600f665-db74-4b2d-a7b5-3f68f868f366.png"
        print(f"Reusing recorded completed Higgsfield job for hero: {known_job_id}")
        download_and_convert_webp(known_url, dest_path)
        return {
            "slot": "hero",
            "job_id": known_job_id,
            "result_url": known_url,
            "local_webp": str(out_rel),
            "duration_seconds": 0,
            "attempt": 1,
            "status": "success"
        }

    prompt = slot_info["prompt"]
    ref_paths = [ROOT / r for r in slot_info["local_reference_images"]]

    cmd = [
        str(HIGGSFIELD_BIN),
        "generate",
        "create",
        "nano_banana_pro",
        "--prompt", prompt,
        "--aspect_ratio", "16:9",
        "--resolution", "2k",
    ]
    for r in ref_paths:
        if r.exists():
            cmd += ["--image", str(r)]

    cmd += ["--wait", "--wait-timeout", "10m", "--wait-interval", "5s", "--json"]

    print(f"Starting Higgsfield CLI generation for slot '{slot_key}'...")
    start_t = time.time()
    for attempt in range(1, 3):
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, check=True)
            output_str = res.stdout.strip()
            data = json.loads(output_str)
            job = data[0] if isinstance(data, list) else data

            result_url = job.get("result_url")
            job_id = job.get("id") or "unknown"
            elapsed = time.time() - start_t
            print(f"  Slot '{slot_key}' completed in {elapsed:.1f}s | Job ID: {job_id}")
            print(f"  Result URL: {result_url}")

            if not result_url:
                raise ValueError(f"No result_url in job output: {output_str}")

            download_and_convert_webp(result_url, dest_path)
            return {
                "slot": slot_key,
                "job_id": job_id,
                "result_url": result_url,
                "local_webp": str(out_rel),
                "duration_seconds": elapsed,
                "attempt": attempt,
                "status": "success"
            }
        except Exception as e:
            print(f"  Attempt {attempt} failed for slot '{slot_key}': {e}")
            if attempt < 2:
                print("  Waiting 45 seconds before retry...")
                time.sleep(45)
            else:
                raise e


def main():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)

    results = {}
    for slot in ["hero", "flatlay", "lifestyle"]:
        res = run_single_generation(manifest_data, slot)
        results[slot] = res
        time.sleep(2)

    out_results_path = ROOT / "output/week8_rank178_type3_results.json"
    with open(out_results_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"\nAll 3 Type 3 images generated and saved! Ledger written to {out_results_path}")


if __name__ == "__main__":
    main()
