#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run fixes sequentially for Rank 8, Rank 9, and Rank 10."""

import subprocess, sys

def run_script(script_path):
    print(f"\n========================================================")
    print(f"RUNNING: {script_path}")
    print(f"========================================================")
    res = subprocess.run([sys.executable, "-B", script_path])
    if res.returncode != 0:
        print(f"ERROR: {script_path} failed with exit code {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    run_script("scripts/build_week9_rank8_casual_daily_wear_gold_bangle.py")
    run_script("scripts/build_week9_rank9_daily_wear_earrings.py")
    run_script("scripts/build_week9_rank10_white_stone_necklace.py")
    print("\nALL RANKS 8, 9, 10 SUCCESSFULLY COMPLETED AND VERIFIED!")
