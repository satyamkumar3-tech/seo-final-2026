#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare, convert to WebP, upload and verify 6 carousel media assets for Week 9 Rank 86 (modern vanki ring designs)."""
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
        "code": "BISE0932R181",
        "name": "The Le Sommet Ring",
        "slug": "the-le-sommet-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Le Sommet Ring.png",
        "url": "https://www.bluestone.com/rings/the-le-sommet-ring~105031.html"
    },
    {
        "code": "BIAR0097R07",
        "name": "The Liza Ring",
        "slug": "the-liza-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Liza ring.png",
        "url": "https://www.bluestone.com/rings/the-liza-ring~7623.html"
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
        "code": "BIKR0993R117",
        "name": "The Luvee Highway Ring",
        "slug": "the-luvee-highway-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Luvee Highway Ring.png",
        "url": "https://www.bluestone.com/rings/the-luvee-highway-ring~123242.html"
    },
    {
        "code": "BIPM0017R18",
        "name": "The Malibu Ring",
        "slug": "the-malibu-ring",
        "src_png": ROOT / "ProductImages/seo images/Rings/The Malibu Ring.png",
        "url": "https://www.bluestone.com/rings/the-malibu-ring~2321.html"
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

def find_existing_media(filename: str):
    slug_name = Path(filename).stem
    search_url = f"{WP_API}/media?search={slug_name}&per_page=10"
    req = urllib.request.Request(search_url, headers=AUTH_HEADERS)
    try:
        body, code = req_with_retry(req)
        items = json.loads(body.decode("utf-8"))
        for it in items:
            source_url = it.get("source_url", "")
            if filename in source_url or source_url.endswith(f"/{filename}"):
                return it["id"], source_url
    except Exception as e:
        print(f"Error checking existing media for {filename}: {e}")
    return None, None

def upload_webp_to_wp(webp_path: Path, title: str, alt_text: str):
    filename = webp_path.name
    existing_id, existing_url = find_existing_media(filename)
    if existing_id and existing_url:
        print(f"Reusing existing media for {filename} -> Media ID {existing_id}: {existing_url}")
        return existing_id, existing_url

    url = f"{WP_API}/media"
    data = webp_path.read_bytes()

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
        print(f"Failed HEAD on {url}: {e}")
        return False

def main():
    print("Preparing 6 carousel WebP assets for Week 9 Rank 86...")
    webp_dir = ROOT / "output/webp_carousel_rank86"
    webp_dir.mkdir(parents=True, exist_ok=True)

    results = []
    occasion_year = "Modern Vanki Ring Designs 2026"

    for p in PRODUCTS:
        assert p["src_png"].exists(), f"Source PNG does not exist: {p['src_png']}"
        dst_webp = webp_dir / f"{p['slug']}-carousel.webp"
        convert_png_to_webp(p["src_png"], dst_webp)

        title = f"{p['name']} carousel: {occasion_year}"
        alt = f"modern vanki ring designs 2026 gift idea: {p['name']}"

        media_id, src_url = upload_webp_to_wp(dst_webp, title, alt)

        # Verify HTTP 200
        ok = verify_url(src_url)
        print(f"Pre-flight verification for {src_url}: HTTP {'200 OK' if ok else 'FAILED'}")
        if not ok:
            print(f"CRITICAL: Media URL returned non-200: {src_url}")
            sys.exit(1)

        results.append({
            "code": p["code"],
            "name": p["name"],
            "slug": p["slug"],
            "url": p["url"],
            "media_id": media_id,
            "image_url": src_url,
            "alt": alt,
            "title": title
        })

    out_file = ROOT / "output/week9_rank86_carousel_media.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"\nAll 6 carousel items verified and saved to {out_file}")
    media_ids = [str(r["media_id"]) for r in results]
    print(f"Media IDs: {','.join(media_ids)}")

if __name__ == "__main__":
    main()
