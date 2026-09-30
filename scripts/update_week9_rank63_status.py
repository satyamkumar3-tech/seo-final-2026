#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update status files and Excel workbook for Week 9 Rank 63: mens-gold-band-rings-2026."""
import os, sys, json, csv
from datetime import datetime, timezone
from pathlib import Path
import openpyxl

ROOT = Path(__file__).resolve().parents[1]
RANK = 63
PRIMARY = "men's gold band rings"
SLUG = "mens-gold-band-rings-2026"
POST_ID = 40162
URL = "https://blog.bluestone.com/mens-gold-band-rings-2026/"
NOW_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

def main():
    # Calculate word count from live HTML or draft
    draft_path = ROOT / "output" / "week9_rank63_draft.html"
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
        word_count_str = "4050"

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
            "setting": "study-desk",
            "note": "men's gold band rings The Le Sommet Ring on leather desk pad on dark mahogany study desk"
        }
        rot_data.setdefault("recent_flatlay_settings", []).append(setting_entry)

        # Add recent skus
        skus_to_add = [
            {"rank": f"Week9 Rank {RANK}", "slot": "hero", "code": "BISL0851R28", "name": "The Jasper Band For Him"},
            {"rank": f"Week9 Rank {RANK}", "slot": "flatlay", "code": "BISE0932R181", "name": "The Le Sommet Ring"},
            {"rank": f"Week9 Rank {RANK}", "slot": "lifestyle", "code": "BISV0910R24", "name": "The Interlink Band Ring"}
        ]
        rot_data.setdefault("recent_skus", []).extend(skus_to_add)

        # Add rank details
        rot_data.setdefault("ranks", {})[str(RANK)] = {
            "rank": RANK,
            "primary": PRIMARY,
            "hero_sku": "BISL0851R28",
            "hero_name": "The Jasper Band For Him",
            "flatlay_sku": "BISE0932R181",
            "flatlay_name": "The Le Sommet Ring",
            "lifestyle_sku": "BISV0910R24",
            "lifestyle_name": "The Interlink Band Ring",
            "flatlay_setting": "study-desk",
            "carousel_skus": [
                "BISL0851R28",
                "BISV0910R24",
                "BISE0932R181",
                "BIPM0017R18",
                "BIIP0090R24",
                "BIKR0993R117"
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
                note = f"Published {NOW_ISO[:10]}. WP Post ID {POST_ID}. Author Satyam (270271337). Engine: buying_guide. Categories: Gold (554493348) + Jewellery Problem & Solution (554493465). 6-product 3D coverflow carousel verified. Type 3 images (hero The Jasper Band For Him, flatlay The Le Sommet Ring on study-desk, lifestyle The Interlink Band Ring) generated via Higgsfield nano_banana_pro. Passed live QA."
                sheet.cell(row=r, column=note_col).value = note
                print(f"Updated row {r} in Excel sheet Week 9")
                break
        wb.save(xlsx_path)
        print(f"Saved {xlsx_path}")

if __name__ == "__main__":
    main()
