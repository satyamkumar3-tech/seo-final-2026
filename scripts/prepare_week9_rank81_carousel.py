#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare, convert to WebP, upload and verify 6 carousel media assets for Week 9 Rank 81."""
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
        "code": "BIPN0987N07",
        "name": "The Rapett Evil Eye Charm Necklace",
        "slug": "the-rapett-evil-eye-charm-necklace",
        "src_png": ROOT / "ProductImages/seo images/Necklaces/The Rapett Evil Eye Charm Necklace.png",
        "url": "https://www.bluestone.com/necklaces/the-rapett-evil-eye-charm-necklace~114824.html"
    },
    {
        "code": "BISL0819N09",
        "name": "The Yfel Evil Eye Pendant Necklace",
        "slug": "the-yfel-evil-eye-pendant-necklace",
        "src_png": ROOT / "ProductImages/seo images/Necklaces/The Yfel Evil Eye Pendant Necklace.png",
        "url": "https://www.bluestone.com/necklaces/the-yfel-evil-eye-pendant-necklace~89724.html"
    },
    {
        "code": "BIAV1005V201",
        "name": "The Novare Evil Eye Kids Nazariya Bracelet",
        "slug": "the-novare-evil-eye-kids-nazariya-bracelet",
        "src_png": ROOT / "ProductImages/seo images/Kids Bracelets/The Novare Evil Eye Kids Nazariya Bracelet.png",
        "url": "https://www.bluestone.com/kids+bracelets/the-novare-evil-eye-kids-nazariya-bracelet~173235.html"
    },
    {
        "code": "BIEK1005V227",
        "name": "The Winkoo Kids Evil Eye Bracelet",
        "slug": "the-winkoo-kids-evil-eye-bracelet",
        "src_png": ROOT / "ProductImages/seo images/Kids Bracelets/The Winkoo Kids Evil Eye Bracelet.png",
        "url": "https://www.bluestone.com/kids+bracelets/the-winkoo-kids-evil-eye-bracelet~181193.html"
    },
    {
        "code": "BIPO0783P12",
        "name": "The Melene Evil Eye Pendant",
        "slug": "the-melene-evil-eye-pendant",
        "src_png": ROOT / "ProductImages/seo images/Pendants/The Melene Evil Eye Pendant.png",
        "url": "https://www.bluestone.com/pendants/the-melene-evil-eye-pendant~82769.html"
    },
    {
        "code": "BIPO0783P11",
        "name": "The Ixea Evil Eye Pendant",
        "slug": "the-ixea-evil-eye-pendant",
        "src_png": ROOT / "ProductImages/seo images/Pendants/The Ixea Evil Eye Pendant.png",
        "url": "https://www.bluestone.com/pendants/the-ixea-evil-eye-pendant~82777.html"
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
                print(f"HTTP error {e.code}: {e.reason}")
                raise e
    raise Exception("Max retries exceeded for request")

def upload_media_to_wp(webp_path: Path, title: str, alt_text: str):
    url = f"{WP_API}/media"
    file_bytes = webp_path.read_bytes()
    headers = {
        "Authorization": AUTH_HEADERS["Authorization"],
        "Content-Type": "image/webp",
        "Content-Disposition": f'attachment; filename="{webp_path.name}"',
        "User-Agent": AUTH_HEADERS["User-Agent"]
    }
    req = urllib.request.Request(url, data=file_bytes, headers=headers, method="POST")
    status, body = req_with_retry(req)
    res = json.loads(body.decode())
    media_id = res["id"]
    source_url = res.get("source_url") or res.get("guid", {}).get("rendered", "")

    # Update metadata
    update_url = f"{WP_API}/media/{media_id}"
    update_data = json.dumps({"title": title, "alt_text": alt_text}).encode("utf-8")
    update_headers = {
        "Authorization": AUTH_HEADERS["Authorization"],
        "Content-Type": "application/json",
        "User-Agent": AUTH_HEADERS["User-Agent"]
    }
    update_req = urllib.request.Request(update_url, data=update_data, headers=update_headers, method="POST")
    req_with_retry(update_req)

    return media_id, source_url

def verify_url(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "BluestoneSEO/1.0"}, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"Verification error for {url}: {e}")
        return False

def main():
    carousel_dir = ROOT / "output" / "carousel_week9_rank81"
    carousel_dir.mkdir(parents=True, exist_ok=True)

    verified_items = []
    print(f"Processing {len(PRODUCTS)} products for Rank 81 carousel...")

    for prod in PRODUCTS:
        webp_name = f"{prod['slug']}-kids-necklace-carousel-2026.webp"
        webp_path = carousel_dir / webp_name
        convert_png_to_webp(prod["src_png"], webp_path)

        title = f"{prod['name']} carousel — Kids necklace 2026"
        alt = f"Kids necklace 2026 gift idea: {prod['name']}"

        print(f"Uploading {webp_name} to WordPress...")
        media_id, src_url = upload_media_to_wp(webp_path, title, alt)
        print(f"Uploaded: ID={media_id}, URL={src_url}")

        # Verify HTTP 200
        ok = verify_url(src_url)
        if not ok:
            raise RuntimeError(f"Pre-flight verification failed for {src_url}")
        print(f"Verified HTTP 200 for {src_url}")

        verified_items.append({
            "code": prod["code"],
            "name": prod["name"],
            "slug": prod["slug"],
            "url": prod["url"],
            "media_id": media_id,
            "src": src_url,
            "alt": alt
        })
        time.sleep(1)

    out_file = ROOT / "output" / "week9_rank81_carousel_media.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(verified_items, f, indent=2)

    print(f"\nAll {len(verified_items)} carousel items successfully verified and written to {out_file.name}")

if __name__ == "__main__":
    main()
