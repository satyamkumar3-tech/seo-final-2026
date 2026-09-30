#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Type 3 images for Week 9 Rank 83: White Stone Necklace Gold via Higgsfield CLI."""
import os
import sys
import json
import time
import subprocess
import urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
HIGGSFIELD_BIN = Path("/Users/satyamkumar/.local/bin/higgsfield")
if not HIGGSFIELD_BIN.exists():
    HIGGSFIELD_BIN = Path.home() / ".local" / "bin" / "higgsfield"

MANIFEST_PATH = ROOT / "output" / "Week9_Rank83_WhiteStoneNecklaceGold_type3_prompts.json"

def run_higgsfield_generation(manifest_data, slot_key: str):
    slot_info = manifest_data["slots"][slot_key]
    out_rel = manifest_data["output"][slot_key]
    dest_path = ROOT / out_rel
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Check if already generated
    if dest_path.exists() and dest_path.stat().st_size > 10000:
        print(f"Slot '{slot_key}' already exists at {dest_path}. Reusing existing image.")
        return {
            "slot": slot_key,
            "job_id": "cached_local",
            "result_url": "cached_local",
            "path": str(dest_path.relative_to(ROOT)),
            "alt": slot_info["alt"],
            "caption": slot_info.get("caption", ""),
            "product_name": slot_info["product_name"],
            "code": slot_info.get("code", ""),
            "pdp": slot_info.get("pdp", "")
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

    print(f"\n==========================================")
    print(f"Starting Higgsfield CLI generation for slot '{slot_key}'...")
    print(f"Product: {slot_info['product_name']} ({slot_info.get('code')})")
    print(f"References: {[str(r.relative_to(ROOT)) for r in ref_paths]}")
    start_t = time.time()

    proc = None
    for attempt in range(2):
        print(f"Submission attempt {attempt + 1}...")
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode == 0:
            break
        print(f"Attempt {attempt + 1} failed: {proc.stderr or proc.stdout}")
        if attempt == 0:
            print("Waiting 45 seconds before retry...")
            time.sleep(45)

    if proc.returncode != 0:
        raise RuntimeError(f"Higgsfield generation failed for slot {slot_key}: {proc.stderr or proc.stdout}")

    try:
        data = json.loads(proc.stdout)
    except Exception as e:
        raise RuntimeError(f"Failed to parse JSON output from Higgsfield: {proc.stdout}") from e

    job = data[0] if isinstance(data, list) else data
    result_url = job.get("result_url")
    job_id = job.get("id", "unknown")
    if not result_url:
        raise RuntimeError(f"No result_url returned in job: {job}")

    print(f"Slot '{slot_key}' finished in {time.time() - start_t:.1f}s, Job ID: {job_id}")
    print(f"Result URL: {result_url}")
    print(f"Downloading image from {result_url}...")

    raw_path = dest_path.with_suffix(".raw.png")
    req = urllib.request.Request(result_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        raw_path.write_bytes(resp.read())

    img = Image.open(raw_path).convert("RGB")
    if img.width > 1400:
        ratio = 1400 / img.width
        new_height = int(img.height * ratio)
        img = img.resize((1400, new_height), Image.Resampling.LANCZOS)

    img.save(dest_path, "WEBP", quality=82, method=6)
    print(f"Saved optimized WebP ({dest_path.stat().st_size} bytes) -> {dest_path}")

    return {
        "slot": slot_key,
        "job_id": job_id,
        "result_url": result_url,
        "path": str(dest_path.relative_to(ROOT)),
        "alt": slot_info["alt"],
        "caption": slot_info.get("caption", ""),
        "product_name": slot_info["product_name"],
        "code": slot_info.get("code", ""),
        "pdp": slot_info.get("pdp", "")
    }

def main():
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        manifest_data = json.load(f)

    results = {}
    slots = ["hero", "flatlay", "lifestyle"]
    for slot in slots:
        res = run_higgsfield_generation(manifest_data, slot)
        results[slot] = res
        time.sleep(2)

    out_file = ROOT / "output" / "Week9_Rank83_type3_results.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("\n==========================================")
    print(f"All 3 Type 3 images generated and saved to {out_file.name}")

if __name__ == "__main__":
    main()
