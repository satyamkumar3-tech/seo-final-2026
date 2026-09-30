#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare, convert to WebP, upload and verify 6 carousel media assets for Week 9 Rank 84 (baby wearing earrings)."""
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
        "code": "BIIP0279S08",
        "name": "The Aleena Huggie Earrings",
        "slug": "the-aleena-huggie-earrings",
        "src_png": ROOT / "ProductImages/seo images/Earrings/The Aleena Huggie Earrings.png",
        "url": "https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html"
    },
    {
        "code": "BIIP0427H16",
        "name": "The Vicky Hoop Earrings",
        "slug": "the-vicky-hoop-earrings",
        "src_png": ROOT / "ProductImages/seo images/Earrings/The Vicky Hoop Earrings.png",
        "url": "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html"
    },
    {
        "code": "BIPM0001H28",
        "name": "The Rohal Huggie Earrings",
        "slug": "the-rohal-huggie-earrings",
        "src_png": ROOT / "ProductImages/seo images/Earrings/The Rohal Huggie Earrings.png",
        "url": "https://www.bluestone.com/earrings/the-rohal-huggie-earrings~21864.html"
    },
    {
        "code": "BIPN0880H218",
        "name": "The Nettile Huggie Earrings",
        "slug": "the-nettile-huggie-earrings",
        "src_png": ROOT / "ProductImages/seo images/Earrings/The Nettile Huggie Earrings.png",
        "url": "https://www.bluestone.com/earrings/the-nettile-huggie-earrings~108215.html"
    },
    {
        "code": "BISA0255D05",
        "name": "The Asya Huggie Earrings",
        "slug": "the-asya-huggie-earrings",
        "src_png": ROOT / "ProductImages/seo images/Earrings/The Asya Huggie Earrings.png",
        "url": "https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html"
    },
    {
        "code": "BINK0363H03",
        "name": "The Skein Hoop Earrings",
        "slug": "the-skein-hoop-earrings",
        "src_png": ROOT / "ProductImages/seo images/Earrings/The Skein Hoop Earrings.png",
        "url": "https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html"
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
    for attempt in range(1, max_retries + 1):
        try:
            with urllib.request.urlopen(req) as resp:
                return resp.read(), resp.getcode()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < max_retries:
                print(f"HTTP {e.code} on attempt {attempt}, retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                body = e.read().decode('utf-8', errors='ignore') if hasattr(e, 'read') else str(e)
                print(f"HTTPError {e.code}: {body}")
                raise
        except Exception as e:
            if attempt < max_retries:
                print(f"Exception on attempt {attempt}: {e}, retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                raise

def upload_webp_to_wp(webp_path: Path, title: str, alt_text: str):
    url = f"{WP_API}/media"
    data = webp_path.read_bytes()
    filename = webp_path.name

    headers = {
        **AUTH_HEADERS,
        "Content-Type": "image/webp",
        "Content-Disposition": f'attachment; filename="{filename}"'
    }

    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    body, code = req_with_retry(req)
    media_json = json.loads(body.decode("utf-8"))
    media_id = media_json["id"]
    source_url = media_json["source_url"]

    # Update title and alt
    update_data = json.dumps({
        "title": title,
        "alt_text": alt_text
    }).encode("utf-8")

    update_headers = {
        **AUTH_HEADERS,
        "Content-Type": "application/json"
    }

    update_req = urllib.request.Request(f"{WP_API}/media/{media_id}", data=update_data, headers=update_headers, method="POST")
    req_with_retry(update_req)

    print(f"Uploaded {filename} -> Media ID {media_id}: {source_url}")
    return media_id, source_url

def verify_url(url: str):
    headers = {"User-Agent": "BluestoneSEO/1.0"}
    req = urllib.request.Request(url, headers=headers, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.getcode() == 200
    except Exception as e:
        print(f"Verification failed for {url}: {e}")
        return False

def main():
    out_dir = ROOT / "output/carousel_prepared"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    results = []
    
    for prod in PRODUCTS:
        webp_name = f"{prod['slug']}-baby-wearing-earrings-carousel-2026.webp"
        webp_path = out_dir / webp_name
        convert_png_to_webp(prod["src_png"], webp_path)
        
        alt_text = f"baby wearing earrings 2026 gift idea: {prod['name']}"
        title = f"{prod['name']} - Baby Wearing Earrings 2026"
        
        media_id, source_url = upload_webp_to_wp(webp_path, title, alt_text)
        
        time.sleep(1) # brief pause
        is_ok = verify_url(source_url)
        print(f"Verified {source_url}: HTTP 200 = {is_ok}")
        if not is_ok:
            print(f"WARNING: Image URL did not return 200: {source_url}", file=sys.stderr)
            sys.exit(1)
            
        results.append({
            "name": prod["name"],
            "url": prod["url"],
            "src": source_url,
            "alt": alt_text,
            "media_id": media_id,
            "sku": prod["code"]
        })
        
    out_json = ROOT / "output/week9_rank84_carousel_media.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    print(f"\nSuccessfully prepared and verified all 6 carousel items -> {out_json}")

if __name__ == "__main__":
    main()
