#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare, convert to WebP, upload and verify 6 carousel media assets for Week 9 Rank 65."""
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
        "code": "BISV0910R24",
        "name": "The Interlink Band Ring",
        "slug": "the-interlink-band-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Interlink Band Ring.png",
        "url": "https://www.bluestone.com/rings/the-interlink-band-ring~108785.html"
    },
    {
        "code": "BISE0932R181",
        "name": "The Le Sommet Ring",
        "slug": "the-le-sommet-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Le Sommet Ring.png",
        "url": "https://www.bluestone.com/rings/the-le-sommet-ring~105031.html"
    },
    {
        "code": "BIPM0017R18",
        "name": "The Malibu Ring",
        "slug": "the-malibu-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Malibu Ring.png",
        "url": "https://www.bluestone.com/rings/the-malibu-ring~2321.html"
    },
    {
        "code": "BIIP0090R24",
        "name": "The Ebony Ring",
        "slug": "the-ebony-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Ebony Ring.png",
        "url": "https://www.bluestone.com/rings/the-ebony-ring~9686.html"
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
                print(f"HTTP 429 received. Waiting {delay} seconds before retry (attempt {attempt+1}/{max_retries})...")
                time.sleep(delay)
                delay *= 2
            else:
                print(f"HTTP error {e.code}: {e.reason}")
                raise e
    raise Exception("Max retries exceeded for request")

def upload_media(path: Path, alt: str, title: str):
    headers = dict(AUTH_HEADERS)
    headers["Content-Disposition"] = f'attachment; filename="{path.name}"'
    headers["Content-Type"] = "image/webp"
    
    # Upload binary
    req = urllib.request.Request(f"{WP_API}/media", data=path.read_bytes(), headers=headers, method="POST")
    status, body = req_with_retry(req)
    media = json.loads(body.decode())
    mid = media["id"]
    src_url = media["source_url"]
    print(f"Uploaded {path.name} -> ID: {mid}, URL: {src_url}")
    
    # Update alt & title
    time.sleep(0.5)
    update_data = json.dumps({"alt_text": alt, "title": title}).encode()
    u_headers = dict(AUTH_HEADERS)
    u_headers["Content-Type"] = "application/json"
    u_req = urllib.request.Request(f"{WP_API}/media/{mid}", data=update_data, headers=u_headers, method="POST")
    req_with_retry(u_req)
    print(f"Updated metadata for media ID {mid}")
    return mid, src_url

def verify_http_200(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "BluestoneSEO/1.0"}, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"Verification failed for {url}: {e}")
        return False

def main():
    assets_dir = ROOT / "output" / "Week9_Rank65_assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    uploaded_products = []
    
    for p in PRODUCTS:
        webp_path = assets_dir / f"{p['slug']}-carousel.webp"
        convert_png_to_webp(p["src_png"], webp_path)
        
        alt_text = f"Blue stone ring for men 2026 design: {p['name']} from BlueStone"
        media_title = f"{p['name']} carousel — Blue Stone Ring for Men 2026"
        
        time.sleep(1)
        mid, src_url = upload_media(webp_path, alt=alt_text, title=media_title)
        
        # Verify HTTP 200
        time.sleep(0.5)
        ok = verify_http_200(src_url)
        print(f"Pre-flight verification for {src_url}: {'HTTP 200 OK' if ok else 'FAILED'}")
        if not ok:
            raise Exception(f"Pre-flight verification failed for {src_url}")
            
        p_record = {
            "code": p["code"],
            "name": p["name"],
            "slug": p["slug"],
            "url": p["url"],
            "alt": alt_text,
            "media_id": mid,
            "src": src_url
        }
        uploaded_products.append(p_record)

    # Save to product media json
    media_json_path = ROOT / "output" / "week9_rank65_carousel_media.json"
    with open(media_json_path, "w", encoding="utf-8") as f:
        json.dump(uploaded_products, f, indent=2)
    print(f"All 6 carousel media uploaded and saved to {media_json_path}")

if __name__ == "__main__":
    main()
