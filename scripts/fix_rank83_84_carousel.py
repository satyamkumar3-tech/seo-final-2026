#!/usr/bin/env python3
"""Fix 3D Coverflow Carousel for WordPress posts 37935 (Rank 83) and 37947 (Rank 84)."""
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

# ----------------- RANK 83: South Indian Mangalsutra -----------------
RANK83_ID = 37935
RANK83_ITEMS = [
    {
        "name": "The Aarabhi Mangalsutra",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-aarabhi-mangalsutra~46940.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-aarabhi-mangalsutra-carousel-5.webp",
        "alt": "south indian mangalsutra 2026 gift idea: The Aarabhi Mangalsutra",
        "desc": "Featuring a traditional auspicious pendant motif suspended from a durable dual-strand black bead chain in glowing gold, perfect for everyday sacred elegance."
    },
    {
        "name": "The Yeijah Mangaslsutra Necklace",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-yeijah-mangaslsutra-necklace~163411.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-yeijah-mangaslsutra-necklace-carousel-7.webp",
        "alt": "south indian mangalsutra 2026 gift idea: The Yeijah Mangaslsutra Necklace",
        "desc": "Designed with contemporary geometric balance and fine diamond accents, offering modern workwear elegance without sacrificing cultural symbolism."
    },
    {
        "name": "The Ninetta Mangalsutra Necklace",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-ninetta-mangalsutra-necklace~97026.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-ninetta-mangalsutra-necklace-carousel-3.webp",
        "alt": "south indian mangalsutra 2026 gift idea: The Ninetta Mangalsutra Necklace",
        "desc": "Showcasing intricate craftsmanship with sparkling brilliant-cut diamonds and secure gold linkages for effortless daily styling."
    },
    {
        "name": "The Eirini Mangalsutra",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-eirini-mangalsutra~53179.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-eirini-mangalsutra-carousel-5.webp",
        "alt": "south indian mangalsutra 2026 gift idea: The Eirini Mangalsutra",
        "desc": "A refined minimalist design balancing delicate gold cups with sacred black beads for versatile desk-to-dinner wear."
    },
    {
        "name": "The Casma Mangalsutra",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-casma-mangalsutra~93030.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-casma-mangalsutra-carousel-7.webp",
        "alt": "south indian mangalsutra 2026 gift idea: The Casma Mangalsutra",
        "desc": "Combining timeless Vedic symbolism with modern structural durability in hallmarked solid gold."
    },
    {
        "name": "The Ailia Evil Eye Layered Necklace",
        "url": "https://www.bluestone.com/necklaces/the-ailia-evil-eye-layered-necklace~116379.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-ailia-evil-eye-layered-necklace-carousel-9.webp",
        "alt": "south indian mangalsutra 2026 gift idea: The Ailia Evil Eye Layered Necklace",
        "desc": "A protective contemporary layering piece blending symbolic motifs with fine gold chain links."
    }
]

# ----------------- RANK 84: Butterfly Earrings -----------------
RANK84_ID = 37947
RANK84_ITEMS = [
    {
        "name": "The Ursa Hoop Earrings",
        "url": "https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-ursa-hoop-earrings-carousel-10.webp",
        "alt": "butterfly earrings 2026 gift idea: The Ursa Hoop Earrings",
        "desc": "Crafted in 18K fine gold, these radiant earrings showcase an elegant curved hoop silhouette highlighted with delicate diamond accents. Designed with balanced proportions (height 16.14 mm, width 10.07 mm), they hug the earlobe comfortably while offering luminous brilliance suitable for both boardroom meetings and evening celebrations."
    },
    {
        "name": "The Skein Hoop Earrings",
        "url": "https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-skein-hoop-earrings-carousel-11.webp",
        "alt": "butterfly earrings 2026 gift idea: The Skein Hoop Earrings",
        "desc": "Featuring an intricate interwoven ribbon texture inspired by organic botanical forms, this 18K gold hoop design (height 17.95 mm, width 6.16 mm) catches ambient light from every angle, delivering rich tactile depth without unnecessary weight."
    },
    {
        "name": "The Rohal Huggie Earrings",
        "url": "https://www.bluestone.com/earrings/the-rohal-huggie-earrings~21864.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-rohal-huggie-earrings-carousel-14.webp",
        "alt": "butterfly earrings 2026 gift idea: The Rohal Huggie Earrings",
        "desc": "A minimalist huggie staple featuring a sleek 18K gold profile with flush-set diamond brilliance (height 16.0 mm, width 4.8 mm). Its snug earlobe profile makes it an exceptional choice for continuous daily wear, effortless multi-piercing stacking, and active lifestyles."
    },
    {
        "name": "The Aleena Huggie Earrings",
        "url": "https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-aleena-huggie-earrings-carousel-14.webp",
        "alt": "butterfly earrings 2026 gift idea: The Aleena Huggie Earrings",
        "desc": "Showcasing soft organic curves and sparkling pavé diamonds (height 17.23 mm, width 9.5 mm), this huggie design offers a graceful, sculptural presence that elevates casual denim and crisp white shirts effortlessly."
    },
    {
        "name": "The Faliha Purse Hoop Earrings",
        "url": "https://www.bluestone.com/earrings/the-faliha-purse-hoop-earrings~73262.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-faliha-purse-hoop-earrings-carousel-4.webp",
        "alt": "butterfly earrings 2026 gift idea: The Faliha Purse Hoop Earrings",
        "desc": "An artistic sculptural statement crafted in rich 18K gold with dimensional purse hoop contours (height 13.86 mm, width 13.12 mm), blending playful charm with sophisticated fine jewellery craftsmanship."
    },
    {
        "name": "The Nettile Huggie Earrings",
        "url": "https://www.bluestone.com/earrings/the-nettile-huggie-earrings~108215.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-nettile-huggie-earrings-carousel-12.webp",
        "alt": "butterfly earrings 2026 gift idea: The Nettile Huggie Earrings",
        "desc": "A refined curved huggie design featuring diamond-studded accents along a delicate tapering silhouette (height 14.39 mm, width 7.8 mm), perfect for adding subtle sparkle to everyday professional attire."
    }
]

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
<p><strong>Curated Collection Highlights:</strong></p>
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

def fix_post_83():
    print(f"\n--- Fixing Post {RANK83_ID} (South Indian Mangalsutra) ---")
    post = fetch_post(RANK83_ID)
    content = post.get("content", {}).get("raw", "")
    print(f"Original content length: {len(content)}")
    
    # Replace the bs-cf-wrap block
    pattern = r"<!-- wp:html -->\s*<div class=\"bs-cf-wrap\" id=\"bs-cf-south-indian-mangalsutra\"[\s\S]*?<!-- /wp:html -->"
    m = re.search(pattern, content)
    if not m:
        print("ERROR: Carousel block pattern not found in post 83!")
        return False
        
    carousel_3d = build_3d_coverflow_carousel(
        "bs-cf-south-indian-mangalsutra",
        "BlueStone South Indian Mangalsutra Collection",
        RANK83_ITEMS
    )
    highlights = build_highlights_list(RANK83_ITEMS)
    replacement = f"{carousel_3d}\n\n{highlights}"
    
    new_content = content[:m.start()] + replacement + content[m.end():]
    print(f"New content length: {len(new_content)}")
    
    updated = update_post(RANK83_ID, new_content)
    print(f"SUCCESS: Post {RANK83_ID} updated: {updated.get('link')}")
    return True

def fix_post_84():
    print(f"\n--- Fixing Post {RANK84_ID} (Butterfly Earrings) ---")
    post = fetch_post(RANK84_ID)
    content = post.get("content", {}).get("raw", "")
    print(f"Original content length: {len(content)}")
    
    # Replace the bs-cf-wrap block
    pattern = r"<!-- wp:html -->\s*<div class=\"bs-cf-wrap\" id=\"bs-cf-butterfly-earrings\"[\s\S]*?<!-- /wp:html -->"
    m = re.search(pattern, content)
    if not m:
        print("ERROR: Carousel block pattern not found in post 84!")
        return False
        
    carousel_3d = build_3d_coverflow_carousel(
        "bs-cf-butterfly-earrings",
        "BlueStone Butterfly Earrings Collection",
        RANK84_ITEMS
    )
    
    new_content = content[:m.start()] + carousel_3d + content[m.end():]
    print(f"New content length: {len(new_content)}")
    
    updated = update_post(RANK84_ID, new_content)
    print(f"SUCCESS: Post {RANK84_ID} updated: {updated.get('link')}")
    return True

def main():
    s83 = fix_post_83()
    s84 = fix_post_84()
    if s83 and s84:
        print("\nALL POSTS (83 & 84) CAROUSELS SUCCESSFULLY FIXED!")

if __name__ == "__main__":
    main()
