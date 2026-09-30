#!/usr/bin/env python3
"""Update status files and workbook for Week 8 Rank 149: Statement Earrings."""
import os
import csv
import json
import openpyxl
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RANK = 149
PRIMARY_KW = "statement earrings"
SLUG = "statement-earrings-2026"
BLOG_URL = "https://blog.bluestone.com/statement-earrings-2026/"
POST_ID = 38783
AUTHOR = "Satyam"

def update_status_csv():
    status_csv_path = ROOT / "output/Week8_Blog_Queue_status.csv"
    
    # Read product media and type 3 media
    with open(ROOT / "output/Week8_Rank149_StatementEarrings_product_media.json") as f:
        prod_media = json.load(f)
    carousel_range = f"{prod_media[0]['id']}-{prod_media[-1]['id']}"
    
    with open(ROOT / "output/Week8_Rank149_StatementEarrings_type3_media.json") as f:
        t3_media = json.load(f)
    t3_str = f"hero {t3_media['hero']['id']}; flatlay {t3_media['flatlay']['id']}; lifestyle {t3_media['lifestyle']['id']}"
    
    with open(ROOT / "output/Week8_Rank149_StatementEarrings_qa_results.json") as f:
        qa_data = json.load(f)
    word_count = qa_data.get("word_count", 3435)
    
    notes = (
        f"Published 2026-09-14 via buying_guide engine. Comprehensive guide to statement earrings, "
        f"18Kt/22K gold purities, weight engineering and earlobe support, face shape pairing, lock security, "
        f"6-card 3D coverflow carousel ({carousel_range}), 3 Type 3 images (The Ursa Hoop Earrings, "
        f"The Rohal Huggie Earrings, The Asya Huggie Earrings), flatlay setting desk-kraft, author Satyam (270271337), passed live QA."
    )
    
    rows = []
    header = ["rank", "primary", "slug", "blog_url", "wp_post_id", "status", "carousel_media", "type3_media", "lines", "visible_words", "notes"]
    updated = False
    
    if status_csv_path.exists():
        with open(status_csv_path, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for r in reader:
                if str(r.get("rank", "")).strip() == str(RANK):
                    rows.append({
                        "rank": str(RANK),
                        "primary": PRIMARY_KW,
                        "slug": SLUG,
                        "blog_url": BLOG_URL,
                        "wp_post_id": str(POST_ID),
                        "status": "published",
                        "carousel_media": carousel_range,
                        "type3_media": t3_str,
                        "lines": "415",
                        "visible_words": str(word_count),
                        "notes": notes
                    })
                    updated = True
                else:
                    rows.append(r)
                    
    if not updated:
        rows.append({
            "rank": str(RANK),
            "primary": PRIMARY_KW,
            "slug": SLUG,
            "blog_url": BLOG_URL,
            "wp_post_id": str(POST_ID),
            "status": "published",
            "carousel_media": carousel_range,
            "type3_media": t3_str,
            "lines": "415",
            "visible_words": str(word_count),
            "notes": notes
        })
        
    with open(status_csv_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Updated {status_csv_path} for rank {RANK}")

def update_product_rotation():
    rot_path = ROOT / "output/product_rotation.json"
    with open(rot_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    data.setdefault("recent_flatlay_settings", []).append({
        "rank": f"Week8 Rank {RANK}",
        "setting": "desk-kraft",
        "note": "statement earrings The Rohal Huggie Earrings"
    })
    
    data.setdefault("recent_skus", []).extend([
        {"rank": f"Week8 Rank {RANK}", "slot": "hero", "code": "BISP0427H21", "name": "The Ursa Hoop Earrings"},
        {"rank": f"Week8 Rank {RANK}", "slot": "flatlay", "code": "BIPM0001H28", "name": "The Rohal Huggie Earrings"},
        {"rank": f"Week8 Rank {RANK}", "slot": "lifestyle", "code": "BISA0255D05", "name": "The Asya Huggie Earrings"}
    ])
    
    data.setdefault("ranks", {})[str(RANK)] = {
        "rank": RANK,
        "primary": PRIMARY_KW,
        "hero_sku": "BISP0427H21",
        "hero_name": "The Ursa Hoop Earrings",
        "flatlay_sku": "BIPM0001H28",
        "flatlay_name": "The Rohal Huggie Earrings",
        "lifestyle_sku": "BISA0255D05",
        "lifestyle_name": "The Asya Huggie Earrings",
        "flatlay_setting": "desk-kraft",
        "carousel_skus": ["BIIP0279S08", "BIIP0427H16", "BIJP0686H03", "BINK0363H03", "BIPN0880H218", "BIPM0001H28"]
    }
    
    with open(rot_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Updated {rot_path} for rank {RANK}")

def update_excel_workbook():
    wb_path = ROOT / "SEO Strategy 2026.xlsx"
    wb = openpyxl.load_workbook(wb_path)
    if "Week 8" not in wb.sheetnames:
        print("Week 8 sheet not found in workbook, skipping Excel update.")
        return
        
    ws = wb["Week 8"]
    target_row_idx = None
    for row_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
        if str(row[0]).strip() in (str(RANK), f"{RANK}.0"):
            target_row_idx = row_idx
            break
            
    if target_row_idx:
        # Col 8 is Action (1-indexed: 8)
        # Col 11 is Bluestone Blog URL (1-indexed: 12)
        # Col 10 is Suggested URL Slug (1-indexed: 11)
        # Col 22 is Execution Note (1-indexed: 23)
        ws.cell(row=target_row_idx, column=8, value="Done")
        ws.cell(row=target_row_idx, column=11, value=SLUG)
        ws.cell(row=target_row_idx, column=12, value=BLOG_URL)
        exec_note = (
            f"Published 2026-09-14, WP post ID {POST_ID}, year 2026, author {AUTHOR}, "
            f"Yoast focus KW {PRIMARY_KW}, schema OK, carousel SKUs: BIIP0279S08, BIIP0427H16, BIJP0686H03, BINK0363H03, BIPN0880H218, BIPM0001H28; "
            f"Type 3 SKUs: BISP0427H21 (hero), BIPM0001H28 (flatlay), BISA0255D05 (lifestyle); flatlay setting: desk-kraft; passed live QA."
        )
        ws.cell(row=target_row_idx, column=23, value=exec_note)
        wb.save(wb_path)
        print(f"Successfully updated Excel workbook row {target_row_idx} for rank {RANK}")
    else:
        print(f"Row {RANK} not found in Week 8 sheet!")

def main():
    update_status_csv()
    update_product_rotation()
    update_excel_workbook()

if __name__ == "__main__":
    main()
