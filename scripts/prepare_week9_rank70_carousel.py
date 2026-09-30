#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare, convert to WebP, upload and verify 6 carousel media assets for Week 9 Rank 70."""
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
        "code": "BISL0987V71",
        "name": "The Elize Evil Eye Bracelet",
        "slug": "the-elize-evil-eye-bracelet",
        "src_png": ROOT / "ProductImages/seo images/Bracelet/The Elize Evil Eye Bracelet.png",
        "url": "https://www.bluestone.com/bracelets/the-elize-evil-eye-bracelet~121012.html"
    },
    {
        "code": "BIPO0987V31",
        "name": "The Tapia Chain Bracelet",
        "slug": "the-tapia-chain-bracelet",
        "src_png": ROOT / "ProductImages/seo images/Bracelet/The Tapia Chain Bracelet.png",
        "url": "https://www.bluestone.com/bracelets/the-tapia-chain-bracelet~115379.html"
    },
    {
        "code": "BIPO0730V39",
        "name": "The Kricia Charm Bracelet",
        "slug": "the-kricia-charm-bracelet",
        "src_png": ROOT / "ProductImages/seo images/Bracelet/The Kricia Charm Bracelet.png",
        "url": "https://www.bluestone.com/bracelets/the-kricia-charm-bracelet~75605.html"
    },
    {
        "code": "BIMG0635V45",
        "name": "The Shining Star Bracelet",
        "slug": "the-shining-star-bracelet",
        "src_png": ROOT / "ProductImages/seo images/Bracelet/The Shining Star Bracelet.png",
        "url": "https://www.bluestone.com/bracelets/the-shining-star-bracelet~63731.html"
    },
    {
        "code": "BIAV0865V24",
        "name": "The Pervinca Charm Holder Bracelet",
        "slug": "the-pervinca-charm-holder-bracelet",
        "src_png": ROOT / "ProductImages/seo images/Bracelet/The Pervinca Charm Holder Bracelet.png",
        "url": "https://www.bluestone.com/bracelets/the-pervinca-charm-holder-bracelet~103133.html"
    },
    {
        "code": "BIAV0865V25",
        "name": "The Malocchio Charm Holder Bracelet",
        "slug": "the-malocchio-charm-holder-bracelet",
        "slug_img": "the-malocchio-charm-holder-bracelet",
        "src_png": ROOT / "ProductImages/seo images/Bracelet/The Malocchio Charm Holder Bracelet.png",
        "url": "https://www.bluestone.com/bracelets/the-malocchio-charm-holder-bracelet~95653.html"
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
    assets_dir = ROOT / "output" / "Week9_Rank70_assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    data_file = ROOT / "output" / "Week9_Rank70_carousel_data.json"
    if data_file.exists():
        with open(data_file, "r") as f:
            existing = json.load(f)
        if len(existing) == 6:
            print("Existing verified carousel data found:")
            all_valid = True
            for item in existing:
                if not verify_http_200(item["src"]):
                    all_valid = False
                    break
            if all_valid:
                print("All 6 existing media URLs return HTTP 200 OK. Reusing.")
                return existing

    uploaded_products = []
    
    for p in PRODUCTS:
        webp_path = assets_dir / f"{p['slug']}-citrine-bracelet-carousel-2026.webp"
        convert_png_to_webp(p["src_png"], webp_path)
        
        alt_text = f"Citrine bracelet benefits 2026 design idea: {p['name']} from BlueStone"
        media_title = f"{p['name']} carousel: Citrine Bracelet Benefits 2026"
        
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
        
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(uploaded_products, f, indent=2)
        
    print(f"\nSaved all 6 carousel records to {data_file}")
    return uploaded_products

if __name__ == "__main__":
    main()
