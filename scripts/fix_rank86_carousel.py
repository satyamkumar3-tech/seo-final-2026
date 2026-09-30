#!/usr/bin/env python3
"""Convert carousel of post 37972 (Rank 86: Antique Jewellery Set Buying Guide 2026) to 3D Coverflow + Curated Design Highlights."""
import os
import re
import json
import base64
import urllib.request
from pathlib import Path

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
    "User-Agent": "BluestoneSEO/1.0",
    "Content-Type": "application/json"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"

POST_ID = 37972
CAROUSEL_ID = "bs-cf-antique-jewellery-set"
LABEL = "BlueStone Antique Jewellery Set Collection"

ITEMS = [
    {
        "name": "The Ailia Evil Eye Layered Necklace",
        "url": "https://www.bluestone.com/necklaces/the-ailia-evil-eye-layered-necklace~116379.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-ailia-evil-eye-layered-necklace-carousel-10.webp",
        "alt": "antique jewellery set 2026 gift idea: The Ailia Evil Eye Layered Necklace",
        "desc": "A multi-strand textured gold necklace inspired by heritage protective motifs, pairing cascading layers with timeless craftsmanship."
    },
    {
        "name": "The Faliha Purse Hoop Earrings",
        "url": "https://www.bluestone.com/earrings/the-faliha-purse-hoop-earrings~125078.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-faliha-purse-hoop-earrings-carousel-5.webp",
        "alt": "antique jewellery set 2026 gift idea: The Faliha Purse Hoop Earrings",
        "desc": "Sculptural hollow-form hoops with antique-inspired filigree accents, delivering rich traditional presence with featherlight lobe comfort."
    },
    {
        "name": "The Skein Bangle",
        "url": "https://www.bluestone.com/bangles/the-skein-bangle~70857.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-skein-bangle-carousel-2.webp",
        "alt": "antique jewellery set 2026 gift idea: The Skein Bangle",
        "desc": "Intertwined gold strands crafted with deep antique texturing, perfect as a heritage standalone cuff or part of a regal bridal stack."
    },
    {
        "name": "The Gigi Ring",
        "url": "https://www.bluestone.com/rings/the-gigi-ring~64382.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-gigi-ring-carousel-3.webp",
        "alt": "antique jewellery set 2026 gift idea: The Gigi Ring",
        "desc": "A cluster statement ring featuring milgrain edging and vintage floral symmetry in radiant yellow gold."
    },
    {
        "name": "The Channing Bangle",
        "url": "https://www.bluestone.com/bangles/the-channing-bangle~12599.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-channing-bangle-carousel-2.webp",
        "alt": "antique jewellery set 2026 gift idea: The Channing Bangle",
        "desc": "Featuring raised antique geometric reliefs and hand-finished matte contours, evoking the grandeur of royal Indian jewellery."
    },
    {
        "name": "The Teshvarya Pendant",
        "url": "https://www.bluestone.com/pendants/the-teshvarya-pendant~140134.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-teshvarya-pendant-carousel-5.webp",
        "alt": "antique jewellery set 2026 gift idea: The Teshvarya Pendant",
        "desc": "A majestic temple-inspired medallion pendant showcasing intricate granulation work and ceremonial motifs."
    }
]

def verify_images():
    print("Verifying all carousel image URLs...")
    for item in ITEMS:
        url = item["src"]
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
        try:
            with urllib.request.urlopen(req, timeout=10) as res:
                if res.status != 200:
                    raise RuntimeError(f"Image {url} returned HTTP status {res.status}")
                print(f"  [200 OK] {item['name']} -> {url}")
        except Exception as e:
            raise RuntimeError(f"Failed to verify image {url}: {e}")

def build_3d_coverflow_carousel(carousel_id: str, label: str, items: list) -> str:
    cards = []
    dots = []
    
    for i, item in enumerate(items):
        name = item["name"]
        url = item["url"]
        src = item["src"]
        alt = item["alt"]
        
        cards.append(f"""    <div class="bs-cf-card" data-i="{i}">
      <a class="bs-cf-media" href="{url}">
        <img src="{src}" alt="{alt}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <p class="bs-cf-name">{name}</p>
        <a class="bs-cf-cta" href="{url}">Buy now</a>
      </div>
    </div>""")
        
        active_cls = " is-active" if i == 0 else ""
        dots.append(f'    <button type="button" class="bs-cf-dot{active_cls}" data-i="{i}" aria-label="Product {i+1}"></button>')
        
    cards_html = "\n".join(cards)
    dots_html = "\n".join(dots)
    
    template = (ROOT / "templates/eid_carousel_6_snippet.html").read_text()
    style = template.split("<style>", 1)[1].split("</style>", 1)[0].strip()
    script = template.split("<script>", 1)[1].split("</script>", 1)[0].strip()
    script = script.replace("bs-cf-eid", carousel_id)
    
    html_block = f"""<!-- wp:html -->
<style>
{style}
</style>
<div class="bs-cf" id="{carousel_id}" data-interval="3200" aria-roledescription="carousel" aria-label="{label}">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
{cards_html}
  </div>
  <div class="bs-cf-dots" role="tablist">
{dots_html}
  </div>
</div>
<script>
{script}
</script>
<!-- /wp:html -->"""
    return html_block

def build_highlights_list(items: list) -> str:
    list_items = []
    for item in items:
        list_items.append(
            f'<li><strong><a href="{item["url"]}">{item["name"]}</a>:</strong> {item["desc"]}</li>'
        )
    items_html = "\n".join(list_items)
    
    return f"""<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul>
{items_html}
</ul>
<!-- /wp:list -->"""

def fetch_post(post_id):
    req = urllib.request.Request(f"{WP_API}/posts/{post_id}?context=edit", headers=AUTH_HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())

def update_post(post_id, content):
    data = json.dumps({"content": content}).encode()
    req = urllib.request.Request(f"{WP_API}/posts/{post_id}", data=data, headers=AUTH_HEADERS, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())

def main():
    print(f"\n--- Upgrading Post {POST_ID} (Antique Jewellery Set 2026) Carousel ---")
    verify_images()
    
    post = fetch_post(POST_ID)
    raw = post.get("content", {}).get("raw", "")
    print(f"Original content length: {len(raw)}")
    
    # Match any carousel block in the post
    pattern = r"<!-- wp:html -->[\s\S]*?id=\"bs-cf-antique-jewellery-set\"[\s\S]*?<!-- /wp:html -->(\s*<!-- wp:paragraph -->\s*<p><strong>Curated Design Highlights:</strong></p>\s*<!-- /wp:paragraph -->\s*<!-- wp:list -->\s*<ul>[\s\S]*?</ul>\s*<!-- /wp:list -->)?"
    m = re.search(pattern, raw)
    if not m:
        print("ERROR: Carousel block pattern not found in post 37972!")
        return False
        
    carousel_3d = build_3d_coverflow_carousel(
        CAROUSEL_ID,
        LABEL,
        ITEMS
    )
    highlights = build_highlights_list(ITEMS)
    replacement = f"{carousel_3d}\n\n{highlights}"
    
    new_raw = raw[:m.start()] + replacement + raw[m.end():]
    print(f"New content length: {len(new_raw)}")
    
    updated = update_post(POST_ID, new_raw)
    print(f"SUCCESS: Post {POST_ID} updated with 3D Coverflow + Highlights: {updated.get('link')}")
    return True

if __name__ == "__main__":
    main()
