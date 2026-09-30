#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare, convert, upload (or reuse verified), and verify carousel media for Week 9 Rank 61."""

import os
import sys
import json
import base64
import urllib.request
import urllib.parse
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

# Load .env
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

HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0"
}

CAROUSEL_PRODUCTS = [
    {
        "sku": "BVEM0663C65",
        "name": "The Chevalier Gold Chain",
        "slug": "the-chevalier-gold-chain",
        "png": ROOT / "ProductImages/seo images/Chains/The Chevalier Gold Chain.png",
        "url": "https://www.bluestone.com/chains/the-chevalier-gold-chain~124914.html",
        "alt": "Women chain buying guide 2026 gift idea: The Chevalier Gold Chain",
        "title": "The Chevalier Gold Chain - Classic 22K Solid Gold Chain"
    },
    {
        "sku": "BVEM0663C88",
        "name": "The Tetyana Gold Chain",
        "slug": "the-tetyana-gold-chain",
        "png": ROOT / "ProductImages/seo images/Chains/The Tetyana Gold Chain.png",
        "url": "https://www.bluestone.com/chains/the-tetyana-gold-chain~124927.html",
        "alt": "Women chain buying guide 2026 gift idea: The Tetyana Gold Chain",
        "title": "The Tetyana Gold Chain - Traditional Yellow Gold Chain"
    },
    {
        "sku": "BIAV0987N78",
        "name": "The Ailia Evil Eye Layered Necklace",
        "slug": "the-ailia-evil-eye-layered-necklace",
        "png": ROOT / "ProductImages/seo images/Necklaces/The Ailia Evil Eye Layered Necklace.png",
        "url": "https://www.bluestone.com/necklaces/the-ailia-evil-eye-layered-necklace~116379.html",
        "alt": "Women chain buying guide 2026 gift idea: The Ailia Evil Eye Layered Necklace",
        "title": "The Ailia Evil Eye Layered Necklace - Multi-tier Gold Collar Chain"
    },
    {
        "sku": "BIPN0987N07",
        "name": "The Rapett Evil Eye Charm Necklace",
        "slug": "the-rapett-evil-eye-charm-necklace",
        "png": ROOT / "ProductImages/seo images/Necklaces/The Rapett Evil Eye Charm Necklace.png",
        "url": "https://www.bluestone.com/necklaces/the-rapett-evil-eye-charm-necklace~114824.html",
        "alt": "Women chain buying guide 2026 gift idea: The Rapett Evil Eye Charm Necklace",
        "title": "The Rapett Evil Eye Charm Necklace - Dainty Gold Link Necklace"
    },
    {
        "sku": "BISL0819N09",
        "name": "The Yfel Evil Eye Pendant Necklace",
        "slug": "the-yfel-evil-eye-pendant-necklace",
        "png": ROOT / "ProductImages/seo images/Necklaces/The Yfel Evil Eye Pendant Necklace.png",
        "url": "https://www.bluestone.com/necklaces/the-yfel-evil-eye-pendant-necklace~89724.html",
        "alt": "Women chain buying guide 2026 gift idea: The Yfel Evil Eye Pendant Necklace",
        "title": "The Yfel Evil Eye Pendant Necklace - Gold Chain with Delicate Pendant"
    },
    {
        "sku": "BVPJ0935C06",
        "name": "The Shubhlatika Mangalsutra Necklace",
        "slug": "the-shubhlatika-mangalsutra-necklace",
        "png": ROOT / "ProductImages/seo images/Mangalsutra Chains/The Shubhlatika Mangalsutra Necklace.png",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-shubhlatika-mangalsutra-necklace~146084.html",
        "alt": "Women chain buying guide 2026 gift idea: The Shubhlatika Mangalsutra Necklace",
        "title": "The Shubhlatika Mangalsutra Necklace - Fine Gold Chain Neckwear"
    }
]

def check_http_200(url: str) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "BluestoneSEO/1.0"}, method="HEAD")
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"HEAD failed for {url}: {e}")
        return False

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

def find_existing_wp_media(slug: str):
    search_q = urllib.parse.quote(f"{slug}-carousel")
    req = urllib.request.Request(f"{WP_API}/media?search={search_q}&per_page=5", headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            items = json.loads(resp.read().decode("utf-8"))
            for item in items:
                src = item.get("source_url", "")
                if src and check_http_200(src):
                    return item
    except Exception as e:
        print(f"Search media error for {slug}: {e}")
    return None

def main():
    dest_dir = ROOT / "output/carousel_webp/rank61"
    dest_dir.mkdir(parents=True, exist_ok=True)
    media_json_path = ROOT / "output/week9_rank61_carousel_media.json"
    
    media_results = []
    for prod in CAROUSEL_PRODUCTS:
        print(f"\n--- Checking media for: {prod['name']} ---")
        existing_media = find_existing_wp_media(prod["slug"])
        if existing_media:
            src_url = existing_media["source_url"]
            print(f"Found existing live media ID {existing_media['id']}: {src_url}")
            media_results.append({
                "sku": prod["sku"],
                "name": prod["name"],
                "slug": prod["slug"],
                "id": existing_media["id"],
                "src": src_url,
                "alt": prod["alt"],
                "url": prod["url"]
            })
        else:
            webp_path = dest_dir / f"{prod['slug']}-carousel-2026.webp"
            print(f"Generating WebP: {webp_path}")
            to_carousel_webp(prod["png"], webp_path)
            print(f"Uploading fresh media to WordPress: {webp_path.name}")
            media = upload_webp(webp_path, prod["alt"], prod["title"])
            src_url = media["source_url"]
            assert check_http_200(src_url), f"Uploaded URL not returning 200: {src_url}"
            print(f"Uploaded successfully ID {media['id']}: {src_url}")
            media_results.append({
                "sku": prod["sku"],
                "name": prod["name"],
                "slug": prod["slug"],
                "id": media["id"],
                "src": src_url,
                "alt": prod["alt"],
                "url": prod["url"]
            })

    # Save media results
    media_json_path.write_text(json.dumps(media_results, indent=2), encoding="utf-8")
    print(f"\nSaved all 6 verified media records to {media_json_path}")
    
    # Verify all 6 are HTTP 200
    for m in media_results:
        ok = check_http_200(m["src"])
        print(f"Pre-flight check: {m['name']} -> {m['src']} -> HTTP 200: {ok}")
        assert ok, f"Media URL failed pre-flight 200 check: {m['src']}"

    # Build Coverflow HTML snippet
    template_path = ROOT / "templates/eid_carousel_6_snippet.html"
    snippet_tpl = template_path.read_text(encoding="utf-8")
    
    cards_html = []
    positions = ["is-pos-0", "is-pos-1", "is-pos-2", "is-pos-3", "is-pos--2", "is-pos--1"]
    for i, p in enumerate(media_results):
        pos = positions[i]
        card = f"""    <div class="bs-cf-card {pos}" data-index="{i}">
      <a class="bs-cf-media" href="{p['url']}">
        <img src="{p['src']}" alt="{p['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{p['name']}</div>
        <a class="bs-cf-cta" href="{p['url']}">Buy now</a>
      </div>
    </div>"""
        cards_html.append(card)

    cards_block = "\n".join(cards_html)
    
    # Replace container ID and cards in the template
    slug_id = "women-chain-2026"
    custom_snippet = snippet_tpl
    custom_snippet = custom_snippet.replace("id=\"bs-cf-eid\"", f"id=\"bs-cf-{slug_id}\"")
    custom_snippet = custom_snippet.replace("aria-label=\"BlueStone Eid gift ideas\"", "aria-label=\"BlueStone women chain collection\"")
    custom_snippet = custom_snippet.replace("document.getElementById('bs-cf-eid')", f"document.getElementById('bs-cf-{slug_id}')")
    
    # Replace the stage contents
    start_marker = '<div class="bs-cf-stage">'
    end_marker = '  </div>\n  <div class="bs-cf-dots"'
    
    s_idx = custom_snippet.find(start_marker)
    e_idx = custom_snippet.find(end_marker)
    
    custom_snippet = custom_snippet[:s_idx + len(start_marker)] + "\n" + cards_block + "\n" + custom_snippet[e_idx:]
    
    # Inject into draft HTML
    draft_file = ROOT / "output/week9_rank61_draft.html"
    draft_content = draft_file.read_text(encoding="utf-8")
    assert "<!-- CAROUSEL_PLACEHOLDER -->" in draft_content, "Missing CAROUSEL_PLACEHOLDER in draft"
    
    draft_content = draft_content.replace("<!-- CAROUSEL_PLACEHOLDER -->", custom_snippet.strip())
    draft_file.write_text(draft_content, encoding="utf-8")
    print(f"\nInjected 3D Coverflow carousel into {draft_file} successfully!")

if __name__ == "__main__":
    main()
