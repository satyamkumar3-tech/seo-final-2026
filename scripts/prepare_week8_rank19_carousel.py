#!/usr/bin/env python3
"""Prepare and upload carousel WebP assets for Week 8 Rank 19: Engagement Rings for Couples."""
import os
import sys
import json
import base64
import urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

# Load local environment
def load_env():
    env_file = ROOT / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

load_env()
USER = os.environ.get("WP_USER", "")
PWD = os.environ.get("WP_APP_PASSWORD", "")
TOKEN = base64.b64encode(f"{USER}:{PWD}".encode()).decode() if USER and PWD else ""
AUTH_HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"

from build_week8_rank19_couple_engagement_rings import CAROUSEL_PRODUCTS

PRODUCTS_WITH_PATHS = [
    {
        "sku": "BIAR0097R07",
        "name": "The Liza Ring",
        "png": ROOT / "ProductImages/seo images/Rings/The Liza ring.png",
        "alt": "engagement rings for couples 2026 idea: The Liza Ring",
        "title": "The Liza Ring carousel — engagement rings for couples 2026",
        "url": "https://www.bluestone.com/rings/the-liza-ring~7623.html"
    },
    {
        "sku": "BISL0851R28",
        "name": "The Jasper Band For Him",
        "png": ROOT / "ProductImages/seo images/Rings/The Jasper Band For Him.png",
        "alt": "engagement rings for couples 2026 idea: The Jasper Band For Him",
        "title": "The Jasper Band For Him carousel — engagement rings for couples 2026",
        "url": "https://www.bluestone.com/rings/the-jasper-band-for-him~93964.html"
    },
    {
        "sku": "BIAR0097R16",
        "name": "The Quinn Ring",
        "png": ROOT / "ProductImages/seo images/Rings/The Quinn Ring.png",
        "alt": "engagement rings for couples 2026 idea: The Quinn Ring",
        "title": "The Quinn Ring carousel — engagement rings for couples 2026",
        "url": "https://www.bluestone.com/rings/the-quinn-ring~57845.html"
    },
    {
        "sku": "BISV0910R24",
        "name": "The Interlink Band Ring",
        "png": ROOT / "ProductImages/seo images/Rings/The Interlink Band Ring.png",
        "alt": "engagement rings for couples 2026 idea: The Interlink Band Ring",
        "title": "The Interlink Band Ring carousel — engagement rings for couples 2026",
        "url": "https://www.bluestone.com/rings/the-interlink-band-ring~108785.html"
    },
    {
        "sku": "BIAR0097R04",
        "name": "The Anya Ring",
        "png": ROOT / "ProductImages/seo images/Rings/The Anya Ring.png",
        "alt": "engagement rings for couples 2026 idea: The Anya Ring",
        "title": "The Anya Ring carousel — engagement rings for couples 2026",
        "url": "https://www.bluestone.com/rings/the-anya-ring~7515.html"
    },
    {
        "sku": "BISE0932R181",
        "name": "The Le Sommet Ring",
        "png": ROOT / "ProductImages/seo images/Rings/The Le Sommet Ring.png",
        "alt": "engagement rings for couples 2026 idea: The Le Sommet Ring",
        "title": "The Le Sommet Ring carousel — engagement rings for couples 2026",
        "url": "https://www.bluestone.com/rings/the-le-sommet-ring~105031.html"
    }
]

def convert_png_to_webp(src_png: Path, dst_webp: Path, target_size=(960, 535), quality=82):
    dst_webp.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src_png) as img:
        img = img.convert("RGBA")
        img_w, img_h = img.size
        
        # Calculate aspect fitting
        target_w, target_h = target_size
        scale = min(target_w / img_w, target_h / img_h)
        new_w = int(img_w * scale)
        new_h = int(img_h * scale)
        
        resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        canvas = Image.new("RGBA", target_size, (255, 255, 255, 0))
        paste_x = (target_w - new_w) // 2
        paste_y = (target_h - new_h) // 2
        canvas.paste(resized, (paste_x, paste_y), resized)
        
        canvas.save(dst_webp, "WEBP", quality=quality)
    print(f"Converted {src_png.name} -> {dst_webp.name} ({dst_webp.stat().st_size} bytes)")

def upload_media(path: Path, alt: str, title: str):
    headers = dict(AUTH_HEADERS)
    headers["Content-Disposition"] = f'attachment; filename="{path.name}"'
    headers["Content-Type"] = "image/webp"
    
    req = urllib.request.Request(f"{WP_API}/media", data=path.read_bytes(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=120) as resp:
        media = json.loads(resp.read().decode())
    mid = media["id"]
    
    update_headers = dict(AUTH_HEADERS)
    update_headers["Content-Type"] = "application/json"
    update_data = json.dumps({"alt_text": alt, "title": title}).encode()
    req_u = urllib.request.Request(f"{WP_API}/media/{mid}", data=update_data, headers=update_headers, method="POST")
    with urllib.request.urlopen(req_u, timeout=120) as resp_u:
        media_u = json.loads(resp_u.read().decode())
    s_url = media_u.get("source_url")
    print(f"Uploaded {path.name} -> ID {mid} ({s_url})")
    return media_u

def main():
    out_dir = ROOT / "output/carousel_webp/rank19"
    out_dir.mkdir(parents=True, exist_ok=True)
    media_json_path = out_dir / "media_ids.json"
    
    # Check if already generated and uploaded
    if media_json_path.exists():
        with open(media_json_path) as f:
            existing = json.load(f)
        if len(existing) == 6 and all(m.get("id") for m in existing):
            print(f"Using existing carousel media ({len(existing)} items): {[m['id'] for m in existing]}")
            return existing
            
    results = []
    for prod in PRODUCTS_WITH_PATHS:
        slug_name = prod["name"].lower().replace(" ", "-").replace("'", "")
        webp_name = f"{slug_name}-carousel.webp"
        webp_path = out_dir / webp_name
        
        convert_png_to_webp(prod["png"], webp_path)
        
        print(f"Uploading {webp_name} to WP...")
        m = upload_media(webp_path, prod["alt"], prod["title"])
        results.append({
            "name": prod["name"],
            "sku": prod["sku"],
            "id": m["id"],
            "src": m["source_url"],
            "alt": prod["alt"],
            "title": prod["title"],
            "url": prod["url"]
        })
        
    with open(media_json_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved {len(results)} media items to {media_json_path}")
    
    with open(ROOT / "output/Week8_Rank19_EngagementRingsCouples_product_media.json", "w") as f:
        json.dump(results, f, indent=2)
    return results

if __name__ == "__main__":
    main()
