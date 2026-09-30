#!/usr/bin/env python3
"""Prepare and upload carousel WebP assets for Week 8 Rank 1: Diamond Rings."""
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

from build_week8_rank1_diamond_rings import CAROUSEL_PRODUCTS

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
        
        # Create canvas with background color or transparent
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
    out_dir = ROOT / "output/carousel_webp/rank1"
    out_dir.mkdir(parents=True, exist_ok=True)
    media_json_path = out_dir / "media_ids.json"
    
    results = []
    for prod in CAROUSEL_PRODUCTS:
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
    
    # Also save to output/Week8_Rank1_DiamondRings_product_media.json
    with open(ROOT / "output/Week8_Rank1_DiamondRings_product_media.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
