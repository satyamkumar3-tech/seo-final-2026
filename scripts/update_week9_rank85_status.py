#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update Week9_Blog_Queue_status.csv, product_rotation.json, and SEO Strategy 2026.xlsx for Rank 85."""
import csv
import json
from pathlib import Path
import openpyxl

ROOT = Path(__file__).resolve().parents[1]

# 1. Update output/Week9_Blog_Queue_status.csv
status_csv = ROOT / "output/Week9_Blog_Queue_status.csv"
rows = []
fieldnames = ['rank', 'primary', 'slug', 'blog_url', 'wp_post_id', 'status', 'carousel_media', 'type3_media', 'lines', 'visible_words', 'notes']

if status_csv.exists():
    with open(status_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or fieldnames
        for r in reader:
            if str(r.get("rank")).strip() != "85":
                rows.append(r)

new_row = {
    "rank": "85",
    "primary": "stone necklace for women",
    "slug": "stone-necklace-for-women-2026",
    "blog_url": "https://blog.bluestone.com/stone-necklace-for-women-2026/",
    "wp_post_id": "40426",
    "status": "Done",
    "carousel_media": "40420,40421,40422,40423,40424,40425",
    "type3_media": "40427,40428,40429",
    "lines": "",
    "visible_words": "2875",
    "notes": "2026-09-28T10:49:00Z | SERP intelligence pipeline v1"
}
rows.append(new_row)

# Sort rows by numeric rank
rows.sort(key=lambda x: int(x["rank"]) if x["rank"].isdigit() else 999)

with open(status_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Updated output/Week9_Blog_Queue_status.csv successfully.")

# 2. Update output/product_rotation.json
rotation_path = ROOT / "output/product_rotation.json"
if rotation_path.exists():
    with open(rotation_path, "r", encoding="utf-8") as f:
        rotation = json.load(f)
else:
    rotation = {
        "recent_flatlay_settings": [],
        "recent_type3_trios": [],
        "recent_skus": []
    }

# Upsert flatlay setting
rotation.setdefault("recent_flatlay_settings", []).append({
    "rank": "Week9 Rank 85",
    "setting": "windowsill-daylight",
    "note": "stone necklace for women The Xarvithis Pendant on painted windowsill with sheer linen and ceramic pot in daylight"
})

# Upsert type3 trio
rotation.setdefault("recent_type3_trios", []).append({
    "rank": "Week9 Rank 85",
    "hero": "BISW1080P131 The Thaloria Pendant",
    "flatlay": "BISW1080P246 The Xarvithis Pendant",
    "lifestyle": "BIIP0550P16 The Aagarna Pendant"
})

# Upsert recent SKUs
rotation.setdefault("recent_skus", []).extend([
    {"rank": "Week9 Rank 85", "slot": "hero", "code": "BISW1080P131", "name": "The Thaloria Pendant"},
    {"rank": "Week9 Rank 85", "slot": "flatlay", "code": "BISW1080P246", "name": "The Xarvithis Pendant"},
    {"rank": "Week9 Rank 85", "slot": "lifestyle", "code": "BIIP0550P16", "name": "The Aagarna Pendant"}
])

with open(rotation_path, "w", encoding="utf-8") as f:
    json.dump(rotation, f, indent=2)

print("Updated output/product_rotation.json successfully.")

# 3. Update SEO Strategy 2026.xlsx
xlsx_path = ROOT / "SEO Strategy 2026.xlsx"
real_xlsx = xlsx_path.resolve()
wb = openpyxl.load_workbook(real_xlsx)
if "Week 9" in wb.sheetnames:
    ws = wb["Week 9"]
    rank_col = None
    action_col = None
    url_col = None
    note_col = None

    for col in range(1, ws.max_column + 1):
        val = str(ws.cell(row=1, column=col).value).strip()
        if val == "Priority Rank":
            rank_col = col
        elif val == "Action":
            action_col = col
        elif val == "Bluestone Blog URL":
            url_col = col
        elif val == "Execution Note":
            note_col = col

    updated_row = False
    for row in range(2, ws.max_row + 1):
        cell_val = str(ws.cell(row=row, column=rank_col).value).strip()
        if cell_val == "85":
            ws.cell(row=row, column=action_col, value="Done")
            ws.cell(row=row, column=url_col, value="https://blog.bluestone.com/stone-necklace-for-women-2026/")
            exec_note = "Published 2026-09-28. WP ID 40426. Engine: buying_guide. Author Satyam (270271337). 3D Coverflow + Type 3 trio verified. SERP intelligence v1."
            ws.cell(row=row, column=note_col, value=exec_note)
            updated_row = True
            print(f"Updated row {row} in sheet Week 9.")
            break

    if updated_row:
        wb.save(real_xlsx)
        print("Saved SEO Strategy 2026.xlsx successfully.")
    else:
        print("Warning: Rank 85 row not found in Week 9 sheet.")
else:
    print("Warning: Week 9 sheet not found in workbook.")
