#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch Type 3 images, run Live QA, and update status for Week 8 Rank 170: Real Diamond Rings 2026."""

import base64
import csv
import json
import os
import re
import urllib.request
from pathlib import Path

ROOT = Path("/Users/satyamkumar/Downloads/seo final 2026")
POST_ID = 38975
SLUG = "real-diamond-rings-2026"
URL = "https://blog.bluestone.com/real-diamond-rings-2026/"
PRIMARY = "real diamond rings"
RANK = 170

# Load environment
env_path = ROOT / ".env"
if not env_path.exists():
    env_path = Path("/Users/satyamkumar/Downloads/final seo generation context/.env")
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

USER = os.environ.get("WP_USER", "blogbluestone")
PWD = os.environ.get("WP_APP_PASSWORD") or os.environ.get("WP_APP_PASS") or os.environ.get("WP_PASSWORD", "")
token = base64.b64encode(f"{USER}:{PWD}".encode()).decode()
headers = {"Authorization": f"Basic {token}", "User-Agent": "BluestoneSEO/1.0"}

def upload_media(file_path: Path, title: str, alt: str):
    filename = file_path.name
    search_url = f"https://blog.bluestone.com/wp-json/wp/v2/media?search={filename}"
    req_search = urllib.request.Request(search_url, headers=headers)
    try:
        with urllib.request.urlopen(req_search, timeout=30) as resp:
            results = json.loads(resp.read().decode())
            for item in results:
                if filename in item.get("source_url", ""):
                    print(f"Found existing media for {filename}: ID {item['id']}")
                    return item["id"], item["source_url"]
    except Exception as e:
        print(f"Media search error for {filename}: {e}")

    with open(file_path, "rb") as f:
        file_data = f.read()

    h = dict(headers)
    h["Content-Type"] = "image/webp"
    h["Content-Disposition"] = f'attachment; filename="{filename}"'

    req_upload = urllib.request.Request(
        "https://blog.bluestone.com/wp-json/wp/v2/media",
        data=file_data,
        headers=h,
        method="POST"
    )
    with urllib.request.urlopen(req_upload, timeout=60) as resp:
        res = json.loads(resp.read().decode())
        media_id = res["id"]
        source_url = res["source_url"]
        print(f"Uploaded {filename} -> ID {media_id}")

    # Remove any em dashes from title/alt
    clean_title = title.replace("—", "-").replace("–", "-")
    clean_alt = alt.replace("—", "-").replace("–", "-")
    update_data = json.dumps({"title": clean_title, "alt_text": clean_alt}).encode("utf-8")
    h_update = dict(headers)
    h_update["Content-Type"] = "application/json"
    req_update = urllib.request.Request(
        f"https://blog.bluestone.com/wp-json/wp/v2/media/{media_id}",
        data=update_data,
        headers=h_update,
        method="POST"
    )
    try:
        with urllib.request.urlopen(req_update, timeout=30) as resp_up:
            pass
    except Exception as e:
        print(f"Failed to update metadata for ID {media_id}: {e}")

    return media_id, source_url

def patch_and_publish():
    hero_webp = ROOT / "output/magnific_generated/real-diamond-rings-hero-2026.webp"
    flatlay_webp = ROOT / "output/magnific_generated/real-diamond-rings-flatlay-2026.webp"
    lifestyle_webp = ROOT / "output/magnific_generated/real-diamond-rings-lifestyle-2026.webp"

    for p in [hero_webp, flatlay_webp, lifestyle_webp]:
        if not p.exists():
            raise FileNotFoundError(f"Missing image file: {p}")

    print("Uploading Type 3 images to WordPress...")
    hero_id, hero_url = upload_media(
        hero_webp,
        "The Anya Ring - Real Diamond Rings 2026",
        "real diamond rings 2026: The Anya Ring in hallmarked gold worn by a fair-skinned Indian woman"
    )
    flatlay_id, flatlay_url = upload_media(
        flatlay_webp,
        "The Luvee Highway Ring Flatlay - Real Diamond Rings 2026",
        "real diamond rings 2026: The Luvee Highway Ring on an organized study desk with jeweller tools"
    )
    lifestyle_id, lifestyle_url = upload_media(
        lifestyle_webp,
        "The Interlink Band Ring for Men - Real Diamond Rings 2026",
        "real diamond rings for men 2026: The Interlink Band Ring in gold worn on an Indian man's hand"
    )

    # Load article content
    content = (ROOT / "output/week8_rank170_article_content.html").read_text(encoding="utf-8")

    # Format Gutenberg image blocks with custom PDP link & caption
    flatlay_pdp = "https://www.bluestone.com/rings/the-luvee-highway-ring~123242.html"
    flatlay_block = f"""<!-- wp:image {{"id":{flatlay_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{flatlay_pdp}"><img src="{flatlay_url}" alt="real diamond rings 2026: The Luvee Highway Ring on an organized study desk with jeweller tools" class="wp-image-{flatlay_id}"/></a><figcaption>The Luvee Highway Ring showcasing multi-row diamond craftsmanship: <a href="{flatlay_pdp}">The Luvee Highway Ring</a> in hallmarked gold</figcaption></figure>
<!-- /wp:image -->"""

    lifestyle_pdp = "https://www.bluestone.com/rings/the-interlink-band-ring~108785.html"
    lifestyle_block = f"""<!-- wp:image {{"id":{lifestyle_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{lifestyle_pdp}"><img src="{lifestyle_url}" alt="real diamond rings for men 2026: The Interlink Band Ring in gold worn on an Indian man's hand" class="wp-image-{lifestyle_id}"/></a><figcaption>The Interlink Band Ring for men: <a href="{lifestyle_pdp}">The Interlink Band Ring</a> in solid gold with diamond accents</figcaption></figure>
<!-- /wp:image -->"""

    content = content.replace("<!-- TYPE3_FLATLAY_PLACEHOLDER -->", flatlay_block)
    content = content.replace("<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->", lifestyle_block)

    # Update BlogPosting schema images
    content = re.sub(
        r'"image":\s*\[\s*"[^"]*",\s*"[^"]*",\s*"[^"]*"\s*\]',
        f'"image": [\n        "{hero_url}",\n        "{flatlay_url}",\n        "{lifestyle_url}"\n      ]',
        content
    )

    # Ensure no prohibited dashes in content
    content = content.replace("—", "-").replace("–", "-")

    final_html_path = ROOT / "output/Week8_Rank170_RealDiamondRings_article_final.html"
    final_html_path.write_text(content, encoding="utf-8")
    print(f"Saved final article HTML to {final_html_path}")

    # Patch WordPress Post
    patch_payload = {
        "featured_media": hero_id,
        "content": content,
        "meta": {
            "_yoast_wpseo_focuskw": PRIMARY,
            "_yoast_wpseo_title": f"Real Diamond Rings Buying Guide 2026: Authentication & 4Cs %%page%% %%sep%% %%sitename%%",
            "_yoast_wpseo_metadesc": (
                "Comprehensive 2026 buying guide to real diamond rings. "
                "Discover natural diamond authentication, 4Cs grading, 18Kt vs 14Kt gold security, SGL/IGI certificates & care."
            ),
            "_yoast_wpseo_canonical": URL,
            "_yoast_wpseo_opengraph-image": hero_url,
            "_yoast_wpseo_opengraph-image-id": str(hero_id),
            "_yoast_wpseo_twitter-image": hero_url,
            "_yoast_wpseo_twitter-image-id": str(hero_id)
        }
    }

    h_patch = dict(headers)
    h_patch["Content-Type"] = "application/json"
    req_patch = urllib.request.Request(
        f"https://blog.bluestone.com/wp-json/wp/v2/posts/{POST_ID}",
        data=json.dumps(patch_payload).encode("utf-8"),
        headers=h_patch,
        method="POST"
    )

    with urllib.request.urlopen(req_patch, timeout=60) as resp:
        res_post = json.loads(resp.read().decode())
        print(f"Successfully updated post ID {res_post['id']} at {res_post.get('link')}")

    return hero_id, flatlay_id, lifestyle_id

def run_qa():
    print(f"\n--- Running Live QA on {URL} ---")
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
    assert "real-diamond-rings-hero-2026" in og_image, "og:image hero missing"

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

def update_status(words, type3_ids):
    status_file = ROOT / "output/Week8_Blog_Queue_status.csv"
    existing_rows = []
    if status_file.exists():
        with open(status_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            existing_rows = list(reader)

    carousel_ids = "38969-38974"
    type3_str = f"hero {type3_ids[0]}; flatlay {type3_ids[1]}; lifestyle {type3_ids[2]}"
    notes = "Published 2026-09-15 via buying_guide engine. Comprehensive guide to real diamond rings, natural vs lab/simulants, 4Cs framework, 18Kt/14Kt gold security, SGL/IGI verification, 6-card 3D coverflow carousel (38969-38974), 3 Type 3 images (The Anya Ring, The Luvee Highway Ring, The Interlink Band Ring), flatlay setting study-desk, author Satyam (270271337), passed live QA."

    record = {
        "rank": str(RANK),
        "primary": PRIMARY,
        "slug": SLUG,
        "blog_url": URL,
        "wp_post_id": str(POST_ID),
        "status": "published",
        "carousel_media": carousel_ids,
        "type3_media": type3_str,
        "lines": "522",
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
    cp_file = ROOT / "output/checkpoints/week8_rank170.json"
    cp = {
        "pipeline": "week8",
        "rank": RANK,
        "slug": SLUG,
        "primary": PRIMARY,
        "created_at": "2026-09-15T12:44:27Z",
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
            "carousel_media_ids": [38969, 38970, 38971, 38972, 38973, 38974],
            "type3_media_ids": list(type3_ids),
            "status": "published"
        },
        "updated_at": "2026-09-15T13:35:00Z"
    }
    cp_file.write_text(json.dumps(cp, indent=2), encoding="utf-8")
    print(f"Updated checkpoint file {cp_file}")

if __name__ == "__main__":
    t3 = patch_and_publish()
    words = run_qa()
    update_status(words, t3)
