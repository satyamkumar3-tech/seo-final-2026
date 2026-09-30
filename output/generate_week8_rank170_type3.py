#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Type 3 images for Week 8 Rank 170: Real Diamond Rings Buying Guide 2026."""
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

MANIFEST_PATH = ROOT / "output/Week8_Rank170_RealDiamondRings_type3_prompts.json"

def get_account_status():
    cmd = [str(HIGGSFIELD_BIN), "account", "status", "--json"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode == 0:
        try:
            return json.loads(proc.stdout)
        except Exception:
            pass
    return {}

def run_higgsfield_generation(manifest_data, slot_key: str):
    slot_info = manifest_data["slots"][slot_key]
    out_rel = manifest_data["output"][slot_key]
    dest_path = ROOT / out_rel
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
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
    
    print(f"\n--- Starting Higgsfield CLI generation for slot '{slot_key}' ---")
    start_t = time.time()
    
    proc = None
    retries = 0
    for attempt in range(2):
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode == 0:
            break
        retries += 1
        print(f"Attempt {attempt+1} failed for {slot_key}: {proc.stderr or proc.stdout}")
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
    print(f"Downloading from {result_url}...")
    
    raw_path = dest_path.with_suffix(".raw.png")
    req = urllib.request.Request(result_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        raw_path.write_bytes(resp.read())
        
    img = Image.open(raw_path).convert("RGB")
    if img.width > 1400:
        target_h = round(img.height * 1400 / img.width)
        img = img.resize((1400, target_h), Image.Resampling.LANCZOS)
    img.save(dest_path, "WEBP", quality=82, method=6)
    print(f"Saved optimized WebP to {dest_path} ({img.width}x{img.height}, {os.path.getsize(dest_path)} bytes)")
    
    return {
        "slot": slot_key,
        "job_id": job_id,
        "result_url": result_url,
        "local_path": str(dest_path),
        "retries": retries,
        "duration": round(time.time() - start_t, 1)
    }

def main():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)
        
    initial_status = get_account_status()
    print(f"Starting Higgsfield balance: {initial_status.get('credits')} credits (plan: {initial_status.get('subscription_plan_type')})")
    
    results = {}
    slots_to_generate = ["hero", "flatlay", "lifestyle"]
    
    for slot in slots_to_generate:
        res = run_higgsfield_generation(manifest_data, slot)
        results[slot] = res
        time.sleep(5)
        
    ending_status = get_account_status()
    print(f"\nEnding Higgsfield balance: {ending_status.get('credits')} credits")
    
    summary = {
        "initial_status": initial_status,
        "ending_status": ending_status,
        "results": results
    }
    
    summary_path = ROOT / "output/Week8_Rank170_type3_generation_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSUCCESS: All 3 Type 3 images generated and saved to {summary_path}")

if __name__ == "__main__":
    main()
