#!/usr/bin/env python3
"""Prepare, convert to WebP, upload and verify 6 carousel media assets for Week 8 Rank 178."""
import os
import sys
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path
from PIL import Image

ROOT = Path("/Users/satyamkumar/Downloads/seo final 2026")

# Load environment
env_path = ROOT / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

USER = os.environ.get("WP_USER", "blogbluestone")
PWD = os.environ.get("WP_APP_PASSWORD") or os.environ.get("WP_APP_PASS") or os.environ.get("WP_PASSWORD", "")
token = base64.b64encode(f"{USER}:{PWD}".encode()).decode()
headers = {"Authorization": f"Basic {token}", "User-Agent": "BluestoneSEO/1.0"}

CAROUSEL_SKUS = [
    {
        "sku": "BINS0639R18",
        "name": "The Gigi Ring",
        "url": "https://www.bluestone.com/rings/the-gigi-ring~64382.html",
        "png": ROOT / "ProductImages/seo images/Rings/The Gigi Ring.png",
        "slug": "the-gigi-ring"
    },
    {
        "sku": "BIPM0017R18",
        "name": "The Malibu Ring",
        "url": "https://www.bluestone.com/rings/the-malibu-ring~2321.html",
        "png": ROOT / "ProductImages/seo images/Rings/The Malibu Ring.png",
        "slug": "the-malibu-ring"
    },
    {
        "sku": "BIKR0993R117",
        "name": "The Luvee Highway Ring",
        "url": "https://www.bluestone.com/rings/the-luvee-highway-ring~123242.html",
        "png": ROOT / "ProductImages/seo images/Rings/The Luvee Highway Ring.png",
        "slug": "the-luvee-highway-ring"
    },
    {
        "sku": "BINS0639R11",
        "name": "The Haily Ring",
        "url": "https://www.bluestone.com/rings/the-haily-ring~64366.html",
        "png": ROOT / "ProductImages/seo images/Rings/The Haily Ring.png",
        "slug": "the-haily-ring"
    },
    {
        "sku": "BIAR0097R07",
        "name": "The Liza ring",
        "url": "https://www.bluestone.com/rings/the-liza-ring~7623.html",
        "png": ROOT / "ProductImages/seo images/Rings/The Liza ring.png",
        "slug": "the-liza-ring"
    },
    {
        "sku": "BIJP0993R123",
        "name": "The Viperine Twist Ring",
        "url": "https://www.bluestone.com/rings/the-viperine-twist-ring~124507.html",
        "png": ROOT / "ProductImages/seo images/Rings/The Viperine Twist Ring.png",
        "slug": "the-viperine-twist-ring"
    }
]


def convert_png_to_webp(png_path: Path, output_webp: Path, target_size=(960, 535), quality=82):
    output_webp.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(png_path) as im:
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        composed = Image.alpha_composite(bg, im).convert("RGB")
        # Aspect fit into 960x535 with white padding or resize
        # Calculate aspect ratio
        w, h = composed.size
        target_w, target_h = target_size
        scale = min(target_w / w, target_h / h)
        new_w = int(w * scale)
        new_h = int(h * scale)
        resized = composed.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        final_img = Image.new("RGB", (target_w, target_h), (255, 255, 255))
        paste_x = (target_w - new_w) // 2
        paste_y = (target_h - new_h) // 2
        final_img.paste(resized, (paste_x, paste_y))
        final_img.save(output_webp, "WEBP", quality=quality)
    return output_webp


def upload_media_to_wp(webp_path: Path, title: str, alt: str):
    filename = webp_path.name
    # Search existing media first
    search_url = f"https://blog.bluestone.com/wp-json/wp/v2/media?search={filename}&per_page=10"
    req = urllib.request.Request(search_url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode())
            for item in data:
                src_url = item.get("source_url", "")
                if filename in src_url:
                    print(f"  Found existing media for {filename}: ID {item['id']} -> {src_url}")
                    return item["id"], src_url
    except Exception as e:
        print(f"  Search error for {filename}: {e}")

    # Upload new media
    upload_url = "https://blog.bluestone.com/wp-json/wp/v2/media"
    upload_headers = dict(headers)
    upload_headers["Content-Disposition"] = f'attachment; filename="{filename}"'
    upload_headers["Content-Type"] = "image/webp"

    with open(webp_path, "rb") as f:
        media_bytes = f.read()

    req = urllib.request.Request(upload_url, data=media_bytes, headers=upload_headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=40) as resp:
            res = json.loads(resp.read().decode())
            mid = res.get("id")
            src_url = res.get("source_url")
            print(f"  Uploaded new media {filename}: ID {mid} -> {src_url}")

            # Update alt text and title
            update_url = f"https://blog.bluestone.com/wp-json/wp/v2/media/{mid}"
            up_headers = dict(headers)
            up_headers["Content-Type"] = "application/json"
            up_data = json.dumps({"title": title, "alt_text": alt}).encode()
            up_req = urllib.request.Request(update_url, data=up_data, headers=up_headers, method="POST")
            try:
                urllib.request.urlopen(up_req, timeout=20)
            except Exception as e_up:
                print(f"  Failed to update alt text: {e_up}")

            return mid, src_url
    except Exception as e:
        print(f"  Upload error for {filename}: {e}")
        raise e


def verify_http_200(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"  HTTP HEAD check failed for {url}: {e}")
        return False


def main():
    print("Preparing 6 Carousel Product Assets for Week 8 Rank 178...")
    out_dir = ROOT / "output" / "carousel_webp"
    out_dir.mkdir(parents=True, exist_ok=True)

    verified_cards = []

    for i, item in enumerate(CAROUSEL_SKUS):
        name = item["name"]
        slug = item["slug"]
        png_path = item["png"]
        # Use rank and slug in filename to prevent collisions while remaining semantic
        webp_name = f"{slug}-carousel-178.webp"
        webp_path = out_dir / webp_name
        alt_text = f"finger rings for girls 2026 gift idea: {name}"
        title = f"{name} carousel finger rings for girls 2026"

        print(f"Processing [{i+1}/6]: {name} ({webp_name})...")
        convert_png_to_webp(png_path, webp_path)

        mid, src_url = upload_media_to_wp(webp_path, title, alt_text)
        is_200 = verify_http_200(src_url)
        print(f"  Pre-flight verification HTTP 200: {is_200} for {src_url}")
        if not is_200:
            raise RuntimeError(f"Media URL {src_url} failed HTTP 200 verification!")

        verified_cards.append({
            "index": i,
            "sku": item["sku"],
            "name": name,
            "url": item["url"],
            "media_id": mid,
            "image_url": src_url,
            "alt": alt_text
        })

    # Save to json
    out_json = ROOT / "output" / "week8_rank178_product_media.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(verified_cards, f, indent=2)
    print(f"Saved verified carousel media to {out_json}")


if __name__ == "__main__":
    main()
