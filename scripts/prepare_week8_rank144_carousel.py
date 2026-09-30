#!/usr/bin/env python3
"""Prepare and upload carousel WebP assets for Week 8 Rank 144: Purple Earrings."""
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
AUTH_HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"

PRODUCTS_WITH_PATHS = [
    {
        "sku": "BIIP0279S08",
        "name": "The Aleena Huggie Earrings",
        "png": ROOT / "ProductImages/seo images/Earrings/The Aleena Huggie Earrings.png",
        "alt": "purple earrings 2026 idea: The Aleena Huggie Earrings",
        "title": "The Aleena Huggie Earrings carousel — purple earrings 2026",
        "url": "https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html"
    },
    {
        "sku": "BIIP0427H16",
        "name": "The Vicky Hoop Earrings",
        "png": ROOT / "ProductImages/seo images/Earrings/The Vicky Hoop Earrings.png",
        "alt": "purple earrings 2026 idea: The Vicky Hoop Earrings",
        "title": "The Vicky Hoop Earrings carousel — purple earrings 2026",
        "url": "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html"
    },
    {
        "sku": "BIPN0880H218",
        "name": "The Nettile Huggie Earrings",
        "png": ROOT / "ProductImages/seo images/Earrings/The Nettile Huggie Earrings.png",
        "alt": "purple earrings 2026 idea: The Nettile Huggie Earrings",
        "title": "The Nettile Huggie Earrings carousel — purple earrings 2026",
        "url": "https://www.bluestone.com/earrings/the-nettile-huggie-earrings~108215.html"
    },
    {
        "sku": "BISP0427H21",
        "name": "The Ursa Hoop Earrings",
        "png": ROOT / "ProductImages/seo images/Earrings/The Ursa Hoop Earrings.png",
        "alt": "purple earrings 2026 idea: The Ursa Hoop Earrings",
        "title": "The Ursa Hoop Earrings carousel — purple earrings 2026",
        "url": "https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html"
    },
    {
        "sku": "BISA0255D05",
        "name": "The Asya Huggie Earrings",
        "png": ROOT / "ProductImages/seo images/Earrings/The Asya Huggie Earrings.png",
        "alt": "purple earrings 2026 idea: The Asya Huggie Earrings",
        "title": "The Asya Huggie Earrings carousel — purple earrings 2026",
        "url": "https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html"
    },
    {
        "sku": "BIPM0001H28",
        "name": "The Rohal Huggie Earrings",
        "png": ROOT / "ProductImages/seo images/Earrings/The Rohal Huggie Earrings.png",
        "alt": "purple earrings 2026 idea: The Rohal Huggie Earrings",
        "title": "The Rohal Huggie Earrings carousel — purple earrings 2026",
        "url": "https://www.bluestone.com/earrings/the-rohal-huggie-earrings~21864.html"
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

def verify_url(url: str) -> bool:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "BluestoneSEO/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"URL check failed for {url}: {e}")
        return False

def main():
    out_dir = ROOT / "output/carousel_webp/rank144"
    out_dir.mkdir(parents=True, exist_ok=True)
    media_json_path = out_dir / "media_ids.json"
    
    if media_json_path.exists():
        with open(media_json_path) as f:
            existing = json.load(f)
        if len(existing) == 6 and all(m.get("id") and m.get("src") for m in existing):
            all_ok = True
            for m in existing:
                if not verify_url(m["src"]):
                    all_ok = False
                    break
            if all_ok:
                print(f"Using existing verified carousel media ({len(existing)} items): {[m['id'] for m in existing]}")
                return existing
            
    results = []
    for prod in PRODUCTS_WITH_PATHS:
        slug_name = prod["name"].lower().replace(" ", "-").replace("'", "")
        webp_name = f"{slug_name}-carousel.webp"
        webp_path = out_dir / webp_name
        
        convert_png_to_webp(prod["png"], webp_path)
        
        print(f"Uploading {webp_name} to WP...")
        m = upload_media(webp_path, prod["alt"], prod["title"])
        
        src_url = m.get("source_url")
        if not verify_url(src_url):
            raise RuntimeError(f"Uploaded media URL {src_url} failed HTTP 200 pre-flight check!")
            
        results.append({
            "name": prod["name"],
            "sku": prod["sku"],
            "id": m["id"],
            "src": src_url,
            "alt": prod["alt"],
            "title": prod["title"],
            "url": prod["url"]
        })
        
    with open(media_json_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved {len(results)} media items to {media_json_path}")
    
    with open(ROOT / "output/Week8_Rank144_PurpleEarrings_product_media.json", "w") as f:
        json.dump(results, f, indent=2)
    return results

if __name__ == "__main__":
    main()
