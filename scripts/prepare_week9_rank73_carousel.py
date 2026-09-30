#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare, convert to WebP, upload and verify 6 carousel media assets for Week 9 Rank 73."""
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
        "code": "BISL0851R28",
        "name": "The Jasper Band For Him",
        "slug": "the-jasper-band-for-him",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Jasper Band For Him.png",
        "url": "https://www.bluestone.com/rings/the-jasper-band-for-him~93964.html"
    },
    {
        "code": "BISE0932R181",
        "name": "The Le Sommet Ring",
        "slug": "the-le-sommet-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Le Sommet Ring.png",
        "url": "https://www.bluestone.com/rings/the-le-sommet-ring~105031.html"
    },
    {
        "code": "BISV0910R24",
        "name": "The Interlink Band Ring",
        "slug": "the-interlink-band-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Interlink Band Ring.png",
        "url": "https://www.bluestone.com/rings/the-interlink-band-ring~108785.html"
    },
    {
        "code": "BIAR0097R16",
        "name": "The Quinn Ring",
        "slug": "the-quinn-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Quinn Ring.png",
        "url": "https://www.bluestone.com/rings/the-quinn-ring~57845.html"
    },
    {
        "code": "BINS0639R18",
        "name": "The Gigi Ring",
        "slug": "the-gigi-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Gigi Ring.png",
        "url": "https://www.bluestone.com/rings/the-gigi-ring~64382.html"
    },
    {
        "code": "BIAR0097R07",
        "name": "The Liza ring",
        "slug": "the-liza-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Liza ring.png",
        "url": "https://www.bluestone.com/rings/the-liza-ring~7623.html"
    }
]

def convert_png_to_webp(src_png: Path, dst_webp: Path, target_size=(960, 535), quality=82):
    dst_webp.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src_png) as img:
        img = img.convert("RGBA")
        img_w, img_h = img.size
        target_w, target_h = target_size
        scale = min(target_w / img_w, target_h / img_h)
        new_w = int(img_w * scale)
        new_h = int(img_h * scale)
        resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", target_size, (248, 246, 243, 255))
        paste_x = (target_w - new_w) // 2
        paste_y = (target_h - new_h) // 2
        canvas.paste(resized, (paste_x, paste_y), resized)
        rgb_canvas = canvas.convert("RGB")
        rgb_canvas.save(dst_webp, "WEBP", quality=quality, method=6)
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
                print(f"HTTP error {e.code}: {e.reason}")
                raise e
    raise Exception("Max retries exceeded for request")

def upload_webp_to_wp(webp_path: Path, title: str, alt: str):
    filename = webp_path.name
    with open(webp_path, "rb") as f:
        file_data = f.read()

    headers = {
        **AUTH_HEADERS,
        "Content-Disposition": f'attachment; filename="{filename}"',
        "Content-Type": "image/webp"
    }

    url = f"{WP_API}/media"
    req = urllib.request.Request(url, data=file_data, headers=headers, method="POST")
    print(f"Uploading {filename} to WordPress...")
    status, body = req_with_retry(req)
    media = json.loads(body.decode())
    media_id = media["id"]
    source_url = media["source_url"]

    # Update metadata
    meta_url = f"{WP_API}/media/{media_id}"
    update_data = {
        "title": title,
        "alt_text": alt,
        "caption": alt
    }
    meta_req = urllib.request.Request(
        meta_url,
        data=json.dumps(update_data).encode(),
        headers={**AUTH_HEADERS, "Content-Type": "application/json"},
        method="POST"
    )
    req_with_retry(meta_req)
    print(f"Uploaded Media ID: {media_id} -> {source_url}")
    return media_id, source_url

def verify_url(url: str):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "BluestoneSEO/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"Verification error for {url}: {e}")
        return False

def main():
    webp_dir = ROOT / "output" / "carousel_webp_rank73"
    webp_dir.mkdir(parents=True, exist_ok=True)

    verified_products = []

    for item in PRODUCTS:
        webp_filename = f"{item['slug']}-marriage-ring-carousel-2026.webp"
        webp_path = webp_dir / webp_filename

        if not item["src_png"].exists():
            raise FileNotFoundError(f"Missing source PNG at {item['src_png']}")

        convert_png_to_webp(item["src_png"], webp_path)

        alt = f"Marriage ring finger gift idea 2026: {item['name']} from BlueStone"
        title = f"{item['name']} Marriage Ring Finger Gift 2026"

        media_id, src_url = upload_webp_to_wp(webp_path, title, alt)

        # Verify live HTTP 200
        is_live = verify_url(src_url)
        if not is_live:
            raise RuntimeError(f"Uploaded media failed verification: {src_url}")
        print(f"Verified live HTTP 200 for: {src_url}")

        verified_products.append({
            "code": item["code"],
            "name": item["name"],
            "slug": item["slug"],
            "url": item["url"],
            "media_id": media_id,
            "src": src_url,
            "alt": alt
        })

    media_json_path = ROOT / "output" / "week9_rank73_carousel_media.json"
    with open(media_json_path, "w", encoding="utf-8") as f:
        json.dump(verified_products, f, indent=2)

    print(f"\nAll 6 carousel media assets successfully uploaded and verified!")
    print(f"Saved media details to {media_json_path}")
    return verified_products

if __name__ == "__main__":
    main()
