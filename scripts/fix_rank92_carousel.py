#!/usr/bin/env python3
"""Fix and upgrade 3D Coverflow Carousel for WordPress post 38061 (Rank 92: 24K Gold Chain for Men Buying Guide 2026)."""
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

POST_ID = 38061
CAROUSEL_ID = "bs-cf-24k-gold-chain-mens"
LABEL = "BlueStone Men's Gold Chain Collection"

ITEMS = [
    {
        "name": "The Chevalier Gold Chain",
        "url": "https://www.bluestone.com/chains/the-chevalier-gold-chain~124914.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-chevalier-gold-chain-carousel-9.webp",
        "alt": "24k gold chain mens 2026 gift idea: The Chevalier Gold Chain",
        "desc": "A heavy curb-link chain crafted in solid gold, featuring diamond-cut beveled facets that rest smoothly against the collarbone."
    },
    {
        "name": "The Tetyana Gold Chain",
        "url": "https://www.bluestone.com/chains/the-tetyana-gold-chain~124927.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-tetyana-gold-chain-carousel-10.webp",
        "alt": "24k gold chain mens 2026 gift idea: The Tetyana Gold Chain",
        "desc": "A supple wheat-weave link chain providing superior flexibility and tensile strength for everyday active wear."
    },
    {
        "name": "The Ruan Cuban Diamond Chain",
        "url": "https://www.bluestone.com/chains/the-ruan-cuban-diamond-chain~165221.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-ruan-cuban-diamond-chain-carousel-7.webp",
        "alt": "24k gold chain mens 2026 gift idea: The Ruan Cuban Diamond Chain",
        "desc": "An iconic Cuban curb chain pavé-set with natural brilliant diamonds, delivering masculine luxury and bold neckline presence."
    },
    {
        "name": "The Talisman Evil Eye Pendant For Him",
        "url": "https://www.bluestone.com/pendants/the-talisman-evil-eye-pendant-for-him~115385.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-talisman-evil-eye-pendant-for-him-carousel-3.webp",
        "alt": "24k gold chain mens 2026 gift idea: The Talisman Evil Eye Pendant For Him",
        "desc": "A sculptural protective talisman in 18K solid gold designed with a wide bail to slide effortlessly over heavy gold chains."
    },
    {
        "name": "The Serenity Evil Eye Pendant For Him",
        "url": "https://www.bluestone.com/pendants/the-serenity-evil-eye-pendant-for-him~115382.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-serenity-evil-eye-pendant-for-him-carousel-2.webp",
        "alt": "24k gold chain mens 2026 gift idea: The Serenity Evil Eye Pendant For Him",
        "desc": "Geometric protective medallion combining high-polish gold surfaces with matte textures for an understated modern finish."
    },
    {
        "name": "The Kilxer Link Bracelet For Him",
        "url": "https://www.bluestone.com/bracelets/the-kilxer-link-bracelet-for-him~163433.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-kilxer-link-bracelet-for-him-carousel-6.webp",
        "alt": "24k gold chain mens 2026 gift idea: The Kilxer Link Bracelet For Him",
        "desc": "Engineered with interlocking architectural links, creating a cohesive luxury wrist companion to match men's gold chains."
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
    print(f"\n--- Fixing & Upgrading Post {POST_ID} (24K Gold Chain for Men 2026) ---")
    verify_images()
    
    post = fetch_post(POST_ID)
    raw = post.get("content", {}).get("raw", "")
    print(f"Original content length: {len(raw)}")
    
    carousel_3d = build_3d_coverflow_carousel(
        CAROUSEL_ID,
        LABEL,
        ITEMS
    )
    highlights = build_highlights_list(ITEMS)
    replacement = f"{carousel_3d}\n\n{highlights}"
    
    # Locate existing carousel block (whether wrapped in wp:html or raw style/div/script)
    pattern = r"(?:<!-- wp:html -->\s*)?<style>[\s\S]*?id=\"bs-cf-24k-gold-chain-mens\"[\s\S]*?</script>(?:\s*<!-- /wp:html -->)?(\s*<!-- wp:paragraph -->\s*<p><strong>Curated Design Highlights:</strong></p>\s*<!-- /wp:paragraph -->\s*<!-- wp:list -->\s*<ul>[\s\S]*?</ul>\s*<!-- /wp:list -->)?"
    m = re.search(pattern, raw)
    if not m:
        # Fallback to broad search around bs-cf-24k-gold-chain-mens
        pattern2 = r"<style>[\s\S]*?bs-cf-24k-gold-chain-mens[\s\S]*?</script>"
        m = re.search(pattern2, raw)
        if not m:
            print("ERROR: Carousel block pattern not found in post 38061!")
            return False
            
    new_raw = raw[:m.start()] + replacement + raw[m.end():]
    print(f"New content length: {len(new_raw)}")
    
    updated = update_post(POST_ID, new_raw)
    print(f"SUCCESS: Post {POST_ID} updated with spacious 3D Coverflow: {updated.get('link')}")
    return True

if __name__ == "__main__":
    main()
