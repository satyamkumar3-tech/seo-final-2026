#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare, convert to WebP, upload and verify 6 carousel media assets for Week 9 Rank 82."""
import os
import sys
import time
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

# Load environment
for ep in [ROOT / ".env", Path("/Users/satyamkumar/Downloads/seo final 2026/.env")]:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

WP_USER = os.environ.get("WP_USER", "blogbluestone")
WP_PASS = os.environ.get("WP_APP_PASSWORD") or os.environ.get("WP_APP_PASS") or os.environ.get("WP_PASSWORD", "")
WP_URL = os.environ.get("WP_URL", "https://blog.bluestone.com")
TOKEN = base64.b64encode(f"{WP_USER}:{WP_PASS}".encode()).decode()
WP_API = f"{WP_URL}/wp-json/wp/v2"

AUTH_HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0"
}

PRODUCTS = [
    {
        "code": "BENS0325O09",
        "name": "The Tarentella Oval Bangle",
        "slug": "the-tarentella-oval-bangle",
        "src_png": ROOT / "ProductImages/seo images/Bangles/The Tarentella Oval Bangle.png",
        "url": "https://www.bluestone.com/bangles/the-tarentella-oval-bangle~31547.html"
    },
    {
        "code": "BIDG0393O37",
        "name": "The Estrella Oval Bangle",
        "slug": "the-estrella-oval-bangle",
        "src_png": ROOT / "ProductImages/seo images/Bangles/The Estrella Oval Bangle.png",
        "url": "https://www.bluestone.com/bangles/the-estrella-oval-bangle~34771.html"
    },
    {
        "code": "BINK0363B03",
        "name": "The Skein Bangle",
        "slug": "the-skein-bangle",
        "src_png": ROOT / "ProductImages/seo images/Bangles/The Skein Bangle.png",
        "url": "https://www.bluestone.com/bangles/the-skein-bangle~27491.html"
    },
    {
        "code": "BISM0003O14",
        "name": "The Muricelle Bangle",
        "slug": "the-muricelle-bangle",
        "src_png": ROOT / "ProductImages/seo images/Bangles/The Muricelle Bangle.png",
        "url": "https://www.bluestone.com/bangles/the-muricelle-bangle~1001.html"
    },
    {
        "code": "BIPS0003O06",
        "name": "The Channing Bangle",
        "slug": "the-channing-bangle",
        "src_png": ROOT / "ProductImages/seo images/Bangles/The Channing Bangle.png",
        "url": "https://www.bluestone.com/bangles/the-channing-bangle~975.html"
    },
    {
        "code": "BISL0804O13",
        "name": "The Pear Evil Eye Toggle Bangle",
        "slug": "the-pear-evil-eye-toggle-bangle",
        "src_png": ROOT / "ProductImages/seo images/Bangles/The Pear Evil Eye Toggle Bangle.png",
        "url": "https://www.bluestone.com/bangles/the-pear-evil-eye-toggle-bangle~87037.html"
    }
]

def convert_png_to_webp(src_png: Path, dst_webp: Path, target_size=(960, 535), quality=82):
    dst_webp.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src_png) as img:
        img = img.convert("RGBA")
        resized = img.resize(target_size, Image.Resampling.LANCZOS)
        rgb_img = resized.convert("RGB")
        rgb_img.save(dst_webp, "WEBP", quality=quality, method=6)
    print(f"Converted {src_png.name} -> {dst_webp.name} ({dst_webp.stat().st_size} bytes)")

def req_with_retry(req, max_retries=5, initial_delay=3):
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return resp.status, resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"HTTP 429 received. Waiting {delay}s before retry (attempt {attempt+1}/{max_retries})...")
                time.sleep(delay)
                delay *= 2
            else:
                raise
    raise RuntimeError(f"Request failed after {max_retries} retries.")

def upload_webp_to_wp(webp_path: Path, title: str, alt_text: str):
    filename = webp_path.name
    with open(webp_path, "rb") as f:
        file_bytes = f.read()

    upload_headers = {
        "Authorization": f"Basic {TOKEN}",
        "Content-Disposition": f'attachment; filename="{filename}"',
        "Content-Type": "image/webp",
        "User-Agent": "BluestoneSEO/1.0"
    }

    req = urllib.request.Request(f"{WP_API}/media", data=file_bytes, headers=upload_headers, method="POST")
    status, body = req_with_retry(req)
    media = json.loads(body.decode("utf-8"))
    media_id = media["id"]
    source_url = media["source_url"]
    print(f"Uploaded {filename} -> Media ID {media_id}, URL: {source_url}")

    # Update metadata
    update_data = json.dumps({
        "title": title,
        "alt_text": alt_text,
        "description": f"{title}. Fine gold and diamond jewellery by BlueStone."
    }).encode("utf-8")

    update_headers = {
        "Authorization": f"Basic {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "BluestoneSEO/1.0"
    }

    req_update = urllib.request.Request(f"{WP_API}/media/{media_id}", data=update_data, headers=update_headers, method="POST")
    req_with_retry(req_update)
    print(f"Updated metadata for Media ID {media_id}: alt='{alt_text}'")

    return media_id, source_url

def verify_url_200(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status == 200:
                print(f"HTTP 200 Verified: {url}")
                return True
    except Exception as e:
        print(f"Verification FAILED for {url}: {e}")
        return False
    return False

def main():
    carousel_dir = ROOT / "output/carousel_week9_rank82"
    carousel_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for item in PRODUCTS:
        webp_name = f"{item['slug']}-rose-gold-bangle-carousel-2026.webp"
        dst_webp = carousel_dir / webp_name
        convert_png_to_webp(item["src_png"], dst_webp)

        alt = f"rose gold bangle 2026 design: {item['name']}"
        title = f"{item['name']} rose gold bangle design 2026"

        media_id, source_url = upload_webp_to_wp(dst_webp, title=title, alt_text=alt)

        # Pre-flight HTTP 200 verification
        if not verify_url_200(source_url):
            raise RuntimeError(f"Pre-flight verification failed for uploaded media: {source_url}")

        results.append({
            "code": item["code"],
            "name": item["name"],
            "url": item["url"],
            "id": media_id,
            "src": source_url,
            "alt": alt,
            "title": title
        })
        time.sleep(1)

    out_file = ROOT / "output/week9_rank82_carousel_media.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"\nAll 6 carousel media verified and written to {out_file}")

if __name__ == "__main__":
    main()
