#!/usr/bin/env python3
"""Convert and upload carousel images for Rank 199."""
import os
import sys
import json
import base64
import urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

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
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"

CAROUSEL_PRODUCTS = [
    {
        "sku": "BVEM0663C65",
        "name": "The Chevalier Gold Chain",
        "slug": "the-chevalier-gold-chain",
        "png": ROOT / "ProductImages/seo images/Chains/The Chevalier Gold Chain.png",
        "url": "https://www.bluestone.com/chains/the-chevalier-gold-chain~124914.html",
        "alt": "gold kanthi chain design 2026 gift idea: The Chevalier Gold Chain",
        "title": "The Chevalier Gold Chain - Classic 22K Gold Chain Design"
    },
    {
        "sku": "BVEM0663C88",
        "name": "The Tetyana Gold Chain",
        "slug": "the-tetyana-gold-chain",
        "png": ROOT / "ProductImages/seo images/Chains/The Tetyana Gold Chain.png",
        "url": "https://www.bluestone.com/chains/the-tetyana-gold-chain~124927.html",
        "alt": "gold kanthi chain design 2026 gift idea: The Tetyana Gold Chain",
        "title": "The Tetyana Gold Chain - Traditional Fine Gold Chain Design"
    },
    {
        "sku": "BIAV1037C17",
        "name": "The Ruan Cuban Diamond Chain",
        "slug": "the-ruan-cuban-diamond-chain",
        "png": ROOT / "ProductImages/seo images/Chains/The Ruan Cuban Diamond Chain.png",
        "url": "https://www.bluestone.com/chains/the-ruan-cuban-diamond-chain~165221.html",
        "alt": "gold kanthi chain design 2026 gift idea: The Ruan Cuban Diamond Chain",
        "title": "The Ruan Cuban Diamond Chain - Modern Diamond Cuban Link Chain"
    },
    {
        "sku": "BIAV0987N78",
        "name": "The Ailia Evil Eye Layered Necklace",
        "slug": "the-ailia-evil-eye-layered-necklace",
        "png": ROOT / "ProductImages/seo images/Necklaces/The Ailia Evil Eye Layered Necklace.png",
        "url": "https://www.bluestone.com/necklaces/the-ailia-evil-eye-layered-necklace~116379.html",
        "alt": "gold kanthi chain design 2026 gift idea: The Ailia Evil Eye Layered Necklace",
        "title": "The Ailia Evil Eye Layered Necklace - Multi-tier Gold Collar Necklace"
    },
    {
        "sku": "BIPN0987N07",
        "name": "The Rapett Evil Eye Charm Necklace",
        "slug": "the-rapett-evil-eye-charm-necklace",
        "png": ROOT / "ProductImages/seo images/Necklaces/The Rapett Evil Eye Charm Necklace.png",
        "url": "https://www.bluestone.com/necklaces/the-rapett-evil-eye-charm-necklace~114824.html",
        "alt": "gold kanthi chain design 2026 gift idea: The Rapett Evil Eye Charm Necklace",
        "title": "The Rapett Evil Eye Charm Necklace - Dainty Gold Collar Charm Necklace"
    },
    {
        "sku": "BISL0819N09",
        "name": "The Yfel Evil Eye Pendant Necklace",
        "slug": "the-yfel-evil-eye-pendant-necklace",
        "png": ROOT / "ProductImages/seo images/Necklaces/The Yfel Evil Eye Pendant Necklace.png",
        "url": "https://www.bluestone.com/necklaces/the-yfel-evil-eye-pendant-necklace~89724.html",
        "alt": "gold kanthi chain design 2026 gift idea: The Yfel Evil Eye Pendant Necklace",
        "title": "The Yfel Evil Eye Pendant Necklace - Refined Yellow Gold Collar Necklace"
    }
]

def to_carousel_webp(src: Path, dest: Path):
    image = Image.open(src).convert("RGB")
    target_w, target_h = 960, 535
    image.thumbnail((target_w, target_h), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (target_w, target_h), (245, 243, 240))
    canvas.paste(image, ((target_w - image.width) // 2, (target_h - image.height) // 2))
    dest.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dest, "WEBP", quality=82, method=6)

def upload_webp(path: Path, alt: str, title: str):
    headers = {
        "Authorization": f"Basic {TOKEN}",
        "User-Agent": "BluestoneSEO/1.0",
        "Content-Disposition": f'attachment; filename="{path.name}"',
        "Content-Type": "image/webp"
    }
    req = urllib.request.Request(f"{WP_API}/media", data=path.read_bytes(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=60) as resp:
        media = json.loads(resp.read().decode())
    
    # Update title and alt
    update_headers = {
        "Authorization": f"Basic {TOKEN}",
        "User-Agent": "BluestoneSEO/1.0",
        "Content-Type": "application/json"
    }
    update_data = json.dumps({"alt_text": alt, "title": title}).encode()
    req2 = urllib.request.Request(f"{WP_API}/media/{media['id']}", data=update_data, headers=update_headers, method="POST")
    with urllib.request.urlopen(req2, timeout=60) as resp2:
        media = json.loads(resp2.read().decode())
    return media

def main():
    dest_dir = ROOT / "output/carousel_webp/rank199"
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    media_json_path = dest_dir / "media_ids.json"
    if media_json_path.exists():
        print(f"media_ids.json already exists at {media_json_path}")
        with open(media_json_path) as f:
            print(f.read())
        return

    media_results = []
    for prod in CAROUSEL_PRODUCTS:
        webp_path = dest_dir / f"{prod['slug']}-carousel.webp"
        print(f"Processing {prod['name']} -> {webp_path}")
        to_carousel_webp(prod["png"], webp_path)
        
        print(f"Uploading to WordPress: {prod['name']}")
        media = upload_webp(webp_path, prod["alt"], prod["title"])
        print(f"  Uploaded media ID: {media['id']} -> {media['source_url']}")
        media_results.append({
            "name": prod["name"],
            "sku": prod["sku"],
            "id": media["id"],
            "src": media["source_url"],
            "alt": prod["alt"]
        })
        
    with open(media_json_path, "w") as f:
        json.dump(media_results, f, indent=2)
    print(f"Saved media records to {media_json_path}")

if __name__ == "__main__":
    main()
