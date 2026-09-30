#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare, convert to WebP, upload and verify 6 carousel media assets for Week 9 Rank 60."""
import os, sys, json, time, re, urllib.request, base64
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

# Load environment
env_paths = [ROOT / '.env', Path('/Users/satyamkumar/Downloads/seo final 2026/.env')]
for ep in env_paths:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

WP_USER = os.environ.get('WP_USER', 'blogbluestone')
WP_PASS = os.environ.get('WP_APP_PASSWORD') or os.environ.get('WP_APP_PASS') or os.environ.get('WP_PASSWORD', '')
WP_URL = os.environ.get('WP_URL', 'https://blog.bluestone.com')
TOKEN = base64.b64encode(f"{WP_USER}:{WP_PASS}".encode()).decode()
HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0",
    "Content-Type": "application/json"
}

OUTPUT_DIR = ROOT / "output" / "week9_rank60_carousel_webp"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CAROUSEL_PRODUCTS = [
    {
        "sku": "BIPM0001H28",
        "name": "The Rohal Huggie Earrings",
        "category": "Earrings",
        "pdp": "https://www.bluestone.com/earrings/the-rohal-huggie-earrings~21864.html",
        "png": ROOT / "ProductImages/seo images/Earrings/The Rohal Huggie Earrings.png",
        "slug": "the-rohal-huggie-earrings"
    },
    {
        "sku": "BIHS1145P21",
        "name": "The Valeria Rose Pendant",
        "category": "Pendants",
        "pdp": "https://www.bluestone.com/pendants/the-valeria-rose-pendant~181266.html",
        "png": ROOT / "ProductImages/seo images/Pendants/The Valeria Rose Pendant.png",
        "slug": "the-valeria-rose-pendant"
    },
    {
        "sku": "BIMG0635V45",
        "name": "The Shining Star Bracelet",
        "category": "Bracelets",
        "pdp": "https://www.bluestone.com/bracelets/the-shining-star-bracelet~63731.html",
        "png": ROOT / "ProductImages/seo images/Bracelet/The Shining Star Bracelet.png",
        "slug": "the-shining-star-bracelet"
    },
    {
        "sku": "BIAR0097R07",
        "name": "The Liza Ring",
        "category": "Rings",
        "pdp": "https://www.bluestone.com/rings/the-liza-ring~7623.html",
        "png": ROOT / "ProductImages/seo images/Rings/The Liza Ring.png",
        "slug": "the-liza-ring"
    },
    {
        "sku": "BINS0639R18",
        "name": "The Gigi Ring",
        "category": "Rings",
        "pdp": "https://www.bluestone.com/rings/the-gigi-ring~64382.html",
        "png": ROOT / "ProductImages/seo images/Rings/The Gigi Ring.png",
        "slug": "the-gigi-ring"
    },
    {
        "sku": "BISA0255D05",
        "name": "The Asya Huggie Earrings",
        "category": "Earrings",
        "pdp": "https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html",
        "png": ROOT / "ProductImages/seo images/Earrings/The Asya Huggie Earrings.png",
        "slug": "the-asya-huggie-earrings"
    }
]

def convert_to_960x535_webp(png_path: Path, output_webp: Path, quality=90) -> Path:
    img = Image.open(png_path).convert("RGB")
    target_w, target_h = 960, 535
    img_ratio = img.width / img.height
    target_ratio = target_w / target_h

    if img_ratio > target_ratio:
        new_h = target_h
        new_w = round(target_h * img_ratio)
        resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        left = (new_w - target_w) // 2
        cropped = resized.crop((left, 0, left + target_w, target_h))
    else:
        new_w = target_w
        new_h = round(target_w / img_ratio)
        resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        top = (new_h - target_h) // 2
        cropped = resized.crop((0, top, target_w, top + target_h))

    cropped.save(output_webp, "WEBP", quality=quality, method=6)
    return output_webp

def verify_http_url(url: str) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"HEAD verification failed for {url}: {e}")
        return False

def upload_or_reuse(product: dict) -> dict:
    filename = f"{product['slug']}-916-gold-carousel-2026.webp"
    webp_path = OUTPUT_DIR / filename
    
    convert_to_960x535_webp(product['png'], webp_path)
    print(f"Prepared local WebP: {webp_path.name} ({os.path.getsize(webp_path)} bytes)")

    # Check if media with this filename already exists
    search_url = f"{WP_URL}/wp-json/wp/v2/media?search={filename}&per_page=10"
    req = urllib.request.Request(search_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            existing = json.loads(resp.read().decode())
            for item in existing:
                src = item.get("source_url", "")
                if filename in src and verify_http_url(src):
                    print(f"Reusing existing valid media ID {item['id']}: {src}")
                    return {
                        "sku": product["sku"],
                        "name": product["name"],
                        "category": product["category"],
                        "pdp": product["pdp"],
                        "media_id": item["id"],
                        "source_url": src,
                        "alt": f"916 hallmark gold jewellery design: {product['name']}",
                        "title": f"{product['name']} carousel - 916 Hallmark Gold 2026"
                    }
    except Exception as e:
        print(f"Search warning for {filename}: {e}")

    # Upload new media
    print(f"Uploading new media for {product['name']} ({filename})...")
    with open(webp_path, "rb") as f:
        img_bytes = f.read()

    upload_url = f"{WP_URL}/wp-json/wp/v2/media"
    upload_headers = {
        "Authorization": f"Basic {TOKEN}",
        "User-Agent": "BluestoneSEO/1.0",
        "Content-Disposition": f'attachment; filename="{filename}"',
        "Content-Type": "image/webp"
    }
    upload_req = urllib.request.Request(upload_url, data=img_bytes, headers=upload_headers, method="POST")
    with urllib.request.urlopen(upload_req, timeout=60) as resp:
        media_obj = json.loads(resp.read().decode())
        media_id = media_obj["id"]
        source_url = media_obj["source_url"]

    alt_text = f"916 hallmark gold jewellery design: {product['name']}"
    media_title = f"{product['name']} carousel - 916 Hallmark Gold 2026"
    
    # Patch metadata
    patch_url = f"{WP_URL}/wp-json/wp/v2/media/{media_id}"
    pdp_url = product["pdp"]
    prod_name = product["name"]
    patch_body = json.dumps({
        "title": media_title,
        "alt_text": alt_text,
        "caption": f'<a href="{pdp_url}">{prod_name}</a>',
        "description": alt_text
    }).encode("utf-8")
    patch_req = urllib.request.Request(patch_url, data=patch_body, headers=HEADERS, method="POST")
    with urllib.request.urlopen(patch_req, timeout=30) as resp:
        print(f"Uploaded and patched media ID {media_id}: {source_url}")

    # Verify HTTP 200
    if not verify_http_url(source_url):
        raise RuntimeError(f"Uploaded image URL did not return HTTP 200: {source_url}")

    return {
        "sku": product["sku"],
        "name": product["name"],
        "category": product["category"],
        "pdp": product["pdp"],
        "media_id": media_id,
        "source_url": source_url,
        "alt": alt_text,
        "title": media_title
    }

def main():
    results = []
    for prod in CAROUSEL_PRODUCTS:
        res = upload_or_reuse(prod)
        results.append(res)

    out_file = ROOT / "output" / "Week9_Rank60_916HallmarkGold_product_media.json"
    out_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nAll 6 carousel images verified and saved to {out_file}")
    for r in results:
        print(f" - [{r['sku']}] {r['name']} -> {r['source_url']}")

if __name__ == "__main__":
    main()
