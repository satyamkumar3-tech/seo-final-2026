#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update Week9_Blog_Queue_status.csv, product_rotation.json, and SEO Strategy 2026.xlsx for Rank 86."""
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
            if str(r.get("rank")).strip() != "86":
                rows.append(r)

new_row = {
    "rank": "86",
    "primary": "modern vanki ring designs",
    "slug": "modern-vanki-ring-designs-2026",
    "blog_url": "https://blog.bluestone.com/modern-vanki-ring-designs-2026/",
    "wp_post_id": "40437",
    "status": "Done",
    "carousel_media": "40432,40433,40434,40435,37070,40436",
    "type3_media": "40438,40439,40440",
    "lines": "",
    "visible_words": "2761",
    "notes": "2026-09-28T16:41:00Z | SERP intelligence pipeline v1"
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
    "rank": "Week9 Rank 86",
    "setting": "desk-kraft",
    "note": "modern vanki ring designs The Viperine Twist Ring on warm wooden desk with kraft box and linen"
})

# Upsert type3 trio
rotation.setdefault("recent_type3_trios", []).append({
    "rank": "Week9 Rank 86",
    "hero": "BISE0932R181 The Le Sommet Ring",
    "flatlay": "BIJP0993R123 The Viperine Twist Ring",
    "lifestyle": "BIAR0097R04 The Anya Ring"
})

# Upsert recent SKUs
rotation.setdefault("recent_skus", []).extend([
    {"rank": "Week9 Rank 86", "slot": "hero", "code": "BISE0932R181", "name": "The Le Sommet Ring"},
    {"rank": "Week9 Rank 86", "slot": "flatlay", "code": "BIJP0993R123", "name": "The Viperine Twist Ring"},
    {"rank": "Week9 Rank 86", "slot": "lifestyle", "code": "BIAR0097R04", "name": "The Anya Ring"}
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
        if cell_val == "86":
            ws.cell(row=row, column=action_col, value="Done")
            ws.cell(row=row, column=url_col, value="https://blog.bluestone.com/modern-vanki-ring-designs-2026/")
            exec_note = "Published 2026-09-28. WP ID 40437. Engine: buying_guide. Author Satyam (270271337). 3D Coverflow + Type 3 trio verified. SERP intelligence v1."
            ws.cell(row=row, column=note_col, value=exec_note)
            updated_row = True
            print(f"Updated row {row} in sheet Week 9.")
            break

    if updated_row:
        wb.save(real_xlsx)
        print("Saved SEO Strategy 2026.xlsx successfully.")
    else:
        print("Warning: Rank 86 row not found in Week 9 sheet.")
else:
    print("Warning: Week 9 sheet not found in workbook.")
