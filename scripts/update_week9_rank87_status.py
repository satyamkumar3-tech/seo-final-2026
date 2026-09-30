#!/usr/bin/env python3
"""Update status files and workbook for Week 9 Rank 87 (Skip-Existing via Duplicate-Intent Gate)."""
import csv
import json
import openpyxl
from pathlib import Path

ROOT = Path(".")

# 1. Update output/Week9_Blog_Queue_status.csv
status_file = ROOT / "output/Week9_Blog_Queue_status.csv"
existing_rows = []
fieldnames = [
    "rank", "primary", "slug", "blog_url", "wp_post_id", "status",
    "carousel_media", "type3_media", "lines", "visible_words", "notes"
]

if status_file.exists():
    with open(status_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            existing_rows.append(r)

by_rank = {int(r["rank"]): r for r in existing_rows if r.get("rank")}

by_rank[87] = {
    "rank": "87",
    "primary": "second stud",
    "slug": "second-stud-2026",
    "blog_url": "https://blog.bluestone.com/second-stud-gold-earrings-2026/",
    "wp_post_id": "39610",
    "status": "Skip-Existing",
    "carousel_media": "39604,39605,39606,39607,39608,39609",
    "type3_media": "39611,39612,39613",
    "lines": "",
    "visible_words": "4128",
    "notes": "Duplicate-intent gate: intent satisfied by live post 39610 (https://blog.bluestone.com/second-stud-gold-earrings-2026/). Skipped existing intent."
}

sorted_rows = [by_rank[k] for k in sorted(by_rank.keys())]

with open(status_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sorted_rows)

print("Updated output/Week9_Blog_Queue_status.csv successfully.")

# 2. Update output/product_rotation.json
rot_file = ROOT / "output/product_rotation.json"
if rot_file.exists():
    with open(rot_file, "r", encoding="utf-8") as f:
        rot_data = json.load(f)
    
    # Check if rank 87 is already recorded
    if "week9_rank87" not in rot_data:
        rot_data["week9_rank87"] = {
            "rank": 87,
            "slug": "second-stud-2026",
            "action": "Skip-Existing",
            "conflicting_post_id": 39610,
            "conflicting_slug": "second-stud-gold-earrings-2026",
            "reused_skus": ["BIPM0001H28", "BIIP0427H16", "BISA0255D05"],
            "note": "Skipped new media generation to avoid cannibalization."
        }
        with open(rot_file, "w", encoding="utf-8") as f:
            json.dump(rot_data, f, indent=2)
        print("Updated output/product_rotation.json successfully.")

# 3. Update SEO Strategy 2026.xlsx
excel_file = ROOT / "SEO Strategy 2026.xlsx"
wb = openpyxl.load_workbook(excel_file)
if "Week 9" in wb.sheetnames:
    ws = wb["Week 9"]
    target_row = None
    for r in range(2, ws.max_row + 1):
        if ws.cell(r, 1).value == 87:
            target_row = r
            break
    
    if target_row:
        # Col 8 is Action
        # Col 12 is Bluestone Blog URL
        # Col 23 is Execution Note
        ws.cell(target_row, 8).value = "Skip-Existing"
        ws.cell(target_row, 12).value = "https://blog.bluestone.com/second-stud-gold-earrings-2026/"
        ws.cell(target_row, 23).value = "Duplicate-intent gate: intent satisfied by live post 39610 (https://blog.bluestone.com/second-stud-gold-earrings-2026/). Action: Skip-Existing to protect topical authority against self-cannibalization. Verified live QA 2026-09-28."
        wb.save(excel_file)
        print(f"Updated SEO Strategy 2026.xlsx Week 9 Row {target_row} (Rank 87) successfully.")
