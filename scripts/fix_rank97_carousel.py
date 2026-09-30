#!/usr/bin/env python3
"""Fix and upgrade 3D Coverflow Carousel for WordPress posts:
- Post 38120 (Rank 97: Evil Eye Pendant 2026)
- Post 38109 (Rank 96: Kundan Set 2026)
"""
import os
import re
import json
import base64
import urllib.request
from pathlib import Path

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
    "User-Agent": "BluestoneSEO/1.0",
    "Content-Type": "application/json"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"

# ----------------- POST 38120: Evil Eye Pendant -----------------
POST38120_ID = 38120
POST38120_CAROUSEL_ID = "bs-cf-evil-eye-pendant"
POST38120_LABEL = "BlueStone Evil Eye Pendant Collection"
POST38120_ITEMS = [
    {
        "name": "The Protecteur Evil Eye Pendant",
        "url": "https://www.bluestone.com/pendants/the-protecteur-evil-eye-pendant~114379.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-protecteur-evil-eye-pendant-carousel.webp",
        "alt": "evil eye pendant 2026 gift idea: The Protecteur Evil Eye Pendant",
        "desc": "An iconic medallion silhouette in glowing hallmarked gold, featuring concentric enamel accents and a central brilliant stone."
    },
    {
        "name": "The Serenity Evil Eye Pendant For Him",
        "url": "https://www.bluestone.com/pendants/the-serenity-evil-eye-pendant-for-him~115382.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-serenity-evil-eye-pendant-for-him-carousel-3.webp",
        "alt": "evil eye pendant 2026 gift idea: The Serenity Evil Eye Pendant For Him",
        "desc": "Geometric protective medallion combining brushed gold surfaces with deep cobalt enamel for an understated masculine finish."
    },
    {
        "name": "The Talisman Evil Eye Pendant For Him",
        "url": "https://www.bluestone.com/pendants/the-talisman-evil-eye-pendant-for-him~115385.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-talisman-evil-eye-pendant-for-him-carousel-4.webp",
        "alt": "evil eye pendant 2026 gift idea: The Talisman Evil Eye Pendant For Him",
        "desc": "Substantial 18K solid gold shield talisman designed with a wide bail to slide effortlessly over heavy gold chains."
    },
    {
        "name": "The Yfel Evil Eye Pendant Necklace",
        "url": "https://www.bluestone.com/necklaces/the-yfel-evil-eye-pendant-necklace~89724.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-yfel-evil-eye-pendant-necklace-carousel-4.webp",
        "alt": "evil eye pendant 2026 gift idea: The Yfel Evil Eye Pendant Necklace",
        "desc": "Integrated 18K gold chain and diamond evil eye pendant delivering an effortless everyday neckline statement."
    },
    {
        "name": "The Rapett Evil Eye Charm Necklace",
        "url": "https://www.bluestone.com/necklaces/the-rapett-evil-eye-charm-necklace~114824.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-rapett-evil-eye-charm-necklace-carousel-6.webp",
        "alt": "evil eye pendant 2026 gift idea: The Rapett Evil Eye Charm Necklace",
        "desc": "Playful and opulent multi-charm necklace combining protective eye charms with dangling gold elements."
    },
    {
        "name": "The Ailia Evil Eye Layered Necklace",
        "url": "https://www.bluestone.com/necklaces/the-ailia-evil-eye-layered-necklace~116379.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-ailia-evil-eye-layered-necklace-carousel-12.webp",
        "alt": "evil eye pendant 2026 gift idea: The Ailia Evil Eye Layered Necklace",
        "desc": "Pre-styled double-layer necklace delivering curated collarbone chic with shimmering diamond eye detailing."
    }
]

# ----------------- POST 38109: Kundan Set -----------------
POST38109_ID = 38109
POST38109_CAROUSEL_ID = "bs-cf-kundan-set"
POST38109_LABEL = "BlueStone Kundan & Heritage Fine Jewellery Collection"
POST38109_ITEMS = [
    {
        "name": "The Ailia Evil Eye Layered Necklace",
        "url": "https://www.bluestone.com/necklaces/the-ailia-evil-eye-layered-necklace~116379.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-ailia-evil-eye-layered-necklace-carousel-11.webp",
        "alt": "kundan set 2026 design: The Ailia Evil Eye Layered Necklace",
        "desc": "Crafted in luminous 18K yellow gold with protective evil-eye symbolism, ideal for modern festive layering."
    },
    {
        "name": "The Estrella Oval Bangle",
        "url": "https://www.bluestone.com/bangles/the-estrella-oval-bangle~34771.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-estrella-oval-bangle-carousel-3.webp",
        "alt": "kundan set 2026 design: The Estrella Oval Bangle",
        "desc": "An elegant diamond-studded gold oval bangle that adds sophisticated brilliance alongside traditional bridal kadas."
    },
    {
        "name": "The Faliha Purse Hoop Earrings",
        "url": "https://www.bluestone.com/earrings/the-faliha-purse-hoop-earrings~73262.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-faliha-purse-hoop-earrings-carousel-7.webp",
        "alt": "kundan set 2026 design: The Faliha Purse Hoop Earrings",
        "desc": "Distinctive architectural gold hoop earrings crafted in 18K yellow gold, perfect for reception and sangeet celebrations."
    },
    {
        "name": "The Shubhlatika Mangalsutra Necklace",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-shubhlatika-mangalsutra-necklace~146084.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-shubhlatika-mangalsutra-necklace-carousel-7.webp",
        "alt": "kundan set 2026 design: The Shubhlatika Mangalsutra Necklace",
        "desc": "Auspicious traditional fine gold craftsmanship celebrating marital harmony with intricate floral accents."
    },
    {
        "name": "The Tarentella Oval Bangle",
        "url": "https://www.bluestone.com/bangles/the-tarentella-oval-bangle~31547.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-tarentella-oval-bangle-carousel-3.webp",
        "alt": "kundan set 2026 design: The Tarentella Oval Bangle",
        "desc": "A luxurious diamond-accented solid gold bangle designed to provide regal wrist architecture for traditional weddings."
    },
    {
        "name": "The Sarvanya Pendant",
        "url": "https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-sarvanya-pendant-carousel-9.webp",
        "alt": "kundan set 2026 design: The Sarvanya Pendant",
        "desc": "An intricate statement pendant in hallmarked gold evoking royal heritage silhouettes and timeless elegance."
    }
]

def verify_images(items, label):
    print(f"Verifying {label} carousel image URLs...")
    for item in items:
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

def fix_post(post_id: int, carousel_id: str, label: str, items: list, title: str):
    print(f"\n=======================================================")
    print(f"--- Fixing Post {post_id} ({title}) ---")
    verify_images(items, title)
    
    post = fetch_post(post_id)
    raw = post.get("content", {}).get("raw", "")
    print(f"Original content length: {len(raw)}")
    
    carousel_3d = build_3d_coverflow_carousel(carousel_id, label, items)
    highlights = build_highlights_list(items)
    replacement = f"{carousel_3d}\n\n{highlights}"
    
    # Locate existing carousel and optional adjacent highlights block
    patterns = [
        r"(?:<!-- wp:paragraph -->\s*<p><strong>Curated Design Highlights:</strong></p>\s*<!-- /wp:paragraph -->\s*<!-- wp:list -->\s*<ul>[\s\S]*?</ul>\s*<!-- /wp:list -->\s*)?(?:<p><strong>Curated Design Highlights:</strong></p>\s*<ul[\s\S]*?</ul>\s*)?(?:<!-- wp:html -->\s*)?<style>[\s\S]*?" + re.escape(carousel_id) + r"[\s\S]*?</script>(?:\s*<!-- /wp:html -->)?(?:\s*<!-- wp:paragraph -->\s*<p><strong>Curated Design Highlights:</strong></p>\s*<!-- /wp:paragraph -->\s*<!-- wp:list -->\s*<ul>[\s\S]*?</ul>\s*<!-- /wp:list -->)?",
        r"(?:<!-- wp:html -->\s*)?<style>[\s\S]*?" + re.escape(carousel_id) + r"[\s\S]*?</script>(?:\s*<!-- /wp:html -->)?",
        r"<style>[\s\S]*?\.bs-cf[\s\S]*?</script>"
    ]
    
    m = None
    for pat in patterns:
        m = re.search(pat, raw)
        if m:
            break
            
    if not m:
        print(f"ERROR: Carousel block pattern not found in post {post_id}!")
        return False
        
    print(f"Found carousel match from index {m.start()} to {m.end()} (length {len(m.group(0))})")
    new_raw = raw[:m.start()] + replacement + raw[m.end():]
    print(f"New content length: {len(new_raw)}")
    
    updated = update_post(post_id, new_raw)
    print(f"SUCCESS: Post {post_id} updated: {updated.get('link')}")
    return True

def main():
    ok1 = fix_post(POST38120_ID, POST38120_CAROUSEL_ID, POST38120_LABEL, POST38120_ITEMS, "Rank 97: Evil Eye Pendant")
    ok2 = fix_post(POST38109_ID, POST38109_CAROUSEL_ID, POST38109_LABEL, POST38109_ITEMS, "Rank 96: Kundan Set")
    
    if ok1 and ok2:
        print("\nAll carousels updated successfully with clean 3D coverflow & active buttons!")

if __name__ == "__main__":
    main()
