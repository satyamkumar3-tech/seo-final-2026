#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run Live QA and update status for Week 8 Rank 168: Amethyst Rings 2026."""

import csv
import json
import re
import urllib.request
from pathlib import Path

URL = "https://blog.bluestone.com/amethyst-rings-2026/"
POST_ID = 38956
SLUG = "amethyst-rings-2026"
RANK = 168
PRIMARY = "amethyst rings"

ROOT = Path("/Users/satyamkumar/Downloads/final seo generation context")
WORKSPACE = Path("/Users/satyamkumar/Downloads/seo final 2026")

def run_qa():
    print(f"Fetching live URL: {URL}...")
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8")
        status_code = resp.status

    print(f"HTTP Status: {status_code}")
    assert status_code == 200, f"Expected 200, got {status_code}"

    # Check canonical
    assert f'rel="canonical" href="{URL}"' in html or f'rel="canonical" href="https://blog.bluestone.com/{SLUG}/"' in html, "Canonical mismatch"
    print("Canonical: verified")

    # Check og:image
    og_m = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    og_image = og_m.group(1) if og_m else ""
    print(f"og:image: {og_image}")
    assert "amethyst-rings-hero-2026" in og_image, "og:image hero missing"

    # Check carousel
    assert "bs-cf" in html, "Carousel .bs-cf missing"
    assert "bs-cf-stage" in html, "Carousel .bs-cf-stage missing"
    assert "bs-cf-dots" in html, "Carousel .bs-cf-dots missing"
    print("Carousel Coverflow DOM: verified")

    # Check carousel images
    img_urls = re.findall(r'<div class="bs-cf-card[^"]*"[^>]*>[\s\S]*?<img [^>]*src="([^"]+)"', html)
    print(f"Found {len(img_urls)} carousel card images:")
    for u in img_urls:
        req_img = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req_img, timeout=15) as r_img:
            print(f"  {u} -> HTTP {r_img.status}")
            assert r_img.status == 200

    # Calculate visible words
    # Strip script, style, tags
    cleaned = re.sub(r'<style[\s\S]*?</style>', ' ', html)
    cleaned = re.sub(r'<script[\s\S]*?</script>', ' ', cleaned)
    cleaned = re.sub(r'<[^>]+>', ' ', cleaned)
    words = len(cleaned.split())
    print(f"Estimated visible words: {words}")

    # Check dashes inside article body
    entry_m = re.search(r'<div class="entry-content[^"]*"[^>]*>([\s\S]*?)(?:<footer|<nav|</article|<!-- \.entry-content)', html)
    body_content = entry_m.group(1) if entry_m else ""
    assert len(body_content) > 1000, "Failed to extract article body content"
    assert "—" not in body_content, "Prohibited em dash found in body"
    assert "–" not in body_content, "Prohibited en dash found in body"
    print("Dashes check: passed (0 prohibited dashes in article body)")

    print("--- LIVE QA PASSED SUCCESSFULLY ---")
    return words

def update_status(words):
    # Update Status CSV in WORKSPACE
    status_file = WORKSPACE / "output/Week8_Blog_Queue_status.csv"
    existing_rows = []
    if status_file.exists():
        with open(status_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            existing_rows = list(reader)

    carousel_ids = "38950-38955"
    type3_ids = "hero 38957; flatlay 38958; lifestyle 38959"
    notes = "Published 2026-09-15 via buying_guide engine. Comprehensive guide to amethyst rings, purple gemstone quality, 18Kt/14Kt gold settings, Mohs hardness, 6-card 3D coverflow carousel (38950-38955), 3 Type 3 images (The Malibu Ring, The Le Sommet Ring, The Jasper Band For Him), flatlay setting desk-kraft, author Satyam (270271337), passed live QA."

    record = {
        "rank": str(RANK),
        "primary": PRIMARY,
        "slug": SLUG,
        "blog_url": URL,
        "wp_post_id": str(POST_ID),
        "status": "published",
        "carousel_media": carousel_ids,
        "type3_media": type3_ids,
        "lines": "415",
        "visible_words": str(words),
        "notes": notes
    }

    by_rank = {r.get("rank"): r for r in existing_rows}
    by_rank[str(RANK)] = record

    fieldnames = ["rank", "primary", "slug", "blog_url", "wp_post_id", "status", "carousel_media", "type3_media", "lines", "visible_words", "notes"]
    with open(status_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in sorted(by_rank.values(), key=lambda x: int(x.get("rank", 9999)) if x.get("rank", "").isdigit() else 9999):
            writer.writerow(r)
    print(f"Updated status file {status_file}")

    # Update checkpoint
    cp_file = WORKSPACE / "output/checkpoints/week8_rank168.json"
    cp = {
        "pipeline": "week8",
        "rank": 168,
        "slug": SLUG,
        "primary": PRIMARY,
        "created_at": "2026-09-15T11:14:06Z",
        "status": "completed",
        "steps": {
            "read_docs": {"status": "done"},
            "verify_higgsfield": {"status": "done"},
            "inspect_row": {"status": "done"},
            "duplicate_check": {"status": "done"},
            "fact_check": {"status": "done"},
            "keyword_map": {"status": "done"},
            "structure_visuals": {"status": "done"},
            "draft": {"status": "done"},
            "product_media": {"status": "done"},
            "publish_wordpress": {"status": "done"},
            "generate_type3": {"status": "done"},
            "patch_type3": {"status": "done"},
            "live_qa": {"status": "done"},
            "update_status": {"status": "done"},
            "final_report": {"status": "done"}
        },
        "details": {
            "wp_post_id": str(POST_ID),
            "live_url": URL,
            "visible_words": str(words),
            "carousel_media_ids": [38950, 38951, 38952, 38953, 38954, 38955],
            "type3_media_ids": [38957, 38958, 38959],
            "status": "published"
        },
        "updated_at": "2026-09-15T12:24:00Z"
    }
    cp_file.write_text(json.dumps(cp, indent=2), encoding="utf-8")
    print(f"Updated checkpoint file {cp_file}")

if __name__ == "__main__":
    words = run_qa()
    update_status(words)
