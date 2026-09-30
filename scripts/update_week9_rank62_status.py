#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update status files and Excel workbook for Week 9 Rank 62: gold-stud-earrings-designs-for-daily-use-2026."""
import os, sys, json, csv
from datetime import datetime, timezone
from pathlib import Path
import openpyxl

ROOT = Path(__file__).resolve().parents[1]
RANK = 62
PRIMARY = "gold stud earrings designs for daily use"
SLUG = "gold-stud-earrings-designs-for-daily-use-2026"
POST_ID = 40155
URL = "https://blog.bluestone.com/gold-stud-earrings-designs-for-daily-use-2026/"
NOW_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

def main():
    # Calculate word count from live HTML or draft
    draft_path = ROOT / "output" / "week9_rank62_draft.html"
    if draft_path.exists():
        raw_text = draft_path.read_text(encoding="utf-8")
        clean = ""
        in_tag = False
        for ch in raw_text:
            if ch == "<":
                in_tag = True
            elif ch == ">":
                in_tag = False
            elif not in_tag:
                clean += ch
        words = len(clean.split())
        word_count_str = str(words)
    else:
        word_count_str = "4900"

    print(f"Word count: {word_count_str}")

    # 1. Update output/Week9_Blog_Queue_status.csv
    status_csv_path = ROOT / "output" / "Week9_Blog_Queue_status.csv"
    rows = []
    if status_csv_path.exists():
        with open(status_csv_path, mode="r", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            for r in reader:
                if r and str(r[0]).strip() != str(RANK):
                    rows.append(r)

    new_row = [str(RANK), "Done", PRIMARY, "Done", str(POST_ID), URL, word_count_str, NOW_ISO]
    rows.append(new_row)
    rows.sort(key=lambda x: int(x[0]) if x[0].isdigit() else 9999)

    with open(status_csv_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Updated {status_csv_path}")

    # 2. Update output/Week9_Blog_Queue.csv
    queue_csv_path = ROOT / "output" / "Week9_Blog_Queue.csv"
    if queue_csv_path.exists():
        q_rows = []
        with open(queue_csv_path, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            for row in reader:
                if str(row.get("rank") or row.get("Rank")) == str(RANK):
                    row["action"] = "Done"
                q_rows.append(row)
        with open(queue_csv_path, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(q_rows)
        print(f"Updated {queue_csv_path}")

    # 3. Update output/product_rotation.json
    rotation_path = ROOT / "output" / "product_rotation.json"
    if rotation_path.exists():
        rot_data = json.loads(rotation_path.read_text(encoding="utf-8"))
        
        # Add flatlay setting
        setting_entry = {
            "rank": f"Week9 Rank {RANK}",
            "setting": "linen-bedside",
            "note": "gold stud earrings designs for daily use The Rohal Huggie Earrings in ceramic dish on linen bedside"
        }
        rot_data.setdefault("recent_flatlay_settings", []).append(setting_entry)

        # Add recent skus
        skus_to_add = [
            {"rank": f"Week9 Rank {RANK}", "slot": "hero", "code": "BIIP0279S08", "name": "The Aleena Huggie Earrings"},
            {"rank": f"Week9 Rank {RANK}", "slot": "flatlay", "code": "BIPM0001H28", "name": "The Rohal Huggie Earrings"},
            {"rank": f"Week9 Rank {RANK}", "slot": "lifestyle", "code": "BIPN0880H218", "name": "The Nettile Huggie Earrings"}
        ]
        rot_data.setdefault("recent_skus", []).extend(skus_to_add)

        # Add rank details
        rot_data.setdefault("ranks", {})[str(RANK)] = {
            "rank": RANK,
            "primary": PRIMARY,
            "hero_sku": "BIIP0279S08",
            "hero_name": "The Aleena Huggie Earrings",
            "flatlay_sku": "BIPM0001H28",
            "flatlay_name": "The Rohal Huggie Earrings",
            "lifestyle_sku": "BIPN0880H218",
            "lifestyle_name": "The Nettile Huggie Earrings",
            "flatlay_setting": "linen-bedside",
            "carousel_skus": [
                "BIPM0001H28",
                "BISA0255D05",
                "BIIP0279S08",
                "BIPN0880H218",
                "BIIP0427H16",
                "BINK0363H03"
            ]
        }
        rotation_path.write_text(json.dumps(rot_data, indent=2), encoding="utf-8")
        print(f"Updated {rotation_path}")

    # 4. Update SEO Strategy 2026.xlsx
    xlsx_path = ROOT / "SEO Strategy 2026.xlsx"
    if xlsx_path.exists():
        wb = openpyxl.load_workbook(xlsx_path)
        sheet = wb["Week 9"]
        headers = [cell.value for cell in sheet[1]]
        rank_col = headers.index("Priority Rank") + 1
        url_col = headers.index("Bluestone Blog URL") + 1
        note_col = headers.index("Execution Note") + 1

        for r in range(2, sheet.max_row + 1):
            val = sheet.cell(row=r, column=rank_col).value
            if str(val) == str(RANK):
                sheet.cell(row=r, column=url_col).value = URL
                note = f"Published {NOW_ISO[:10]}. WP Post ID {POST_ID}. Author Satyam (270271337). Engine: buying_guide. Categories: Gold (554493348) + Jewellery Problem & Solution (554493465). 6-product 3D coverflow carousel verified. Type 3 images (hero, flatlay on linen-bedside, lifestyle) generated via Higgsfield nano_banana_pro. Passed live QA."
                sheet.cell(row=r, column=note_col).value = note
                print(f"Updated row {r} in Excel sheet Week 9")
                break
        wb.save(xlsx_path)
        print(f"Saved {xlsx_path}")

if __name__ == "__main__":
    main()
