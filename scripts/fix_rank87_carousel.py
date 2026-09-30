#!/usr/bin/env python3
"""Convert carousel of post 37986 (Rank 87: Marathi Mangalsutra Buying Guide 2026) to 3D Coverflow + Curated Design Highlights."""
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

POST_ID = 37986
CAROUSEL_ID = "bs-cf-marathi-mangalsutra"
LABEL = "BlueStone Marathi Mangalsutra Collection"

ITEMS = [
    {
        "name": "The Casma Mangalsutra",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-casma-mangalsutra~93030.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-casma-mangalsutra-carousel-8.webp",
        "alt": "marathi mangalsutra 2026 gift idea: The Casma Mangalsutra",
        "desc": "Traditional double hollow-cup vatimani motifs linked by auspicious black bead and fine 22K gold chain strands."
    },
    {
        "name": "The Aarabhi Mangalsutra",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-aarabhi-mangalsutra~46940.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-aarabhi-mangalsutra-carousel-6.webp",
        "alt": "marathi mangalsutra 2026 gift idea: The Aarabhi Mangalsutra",
        "desc": "A refined dual-vati pendant accented with delicate floral wirework, balancing Maharashtrian heritage with daily wear comfort."
    },
    {
        "name": "The Eirini Mangalsutra",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-eirini-mangalsutra~53179.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-eirini-mangalsutra-carousel-6.webp",
        "alt": "marathi mangalsutra 2026 gift idea: The Eirini Mangalsutra",
        "desc": "Contemporary semi-spherical vatis with diamond-accented connector cups, ideal for modern festive and workplace styling."
    },
    {
        "name": "The Shubhlatika Mangalsutra Necklace",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-shubhlatika-mangalsutra-necklace~146084.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-shubhlatika-mangalsutra-necklace-carousel-6.webp",
        "alt": "marathi mangalsutra 2026 gift idea: The Shubhlatika Mangalsutra Necklace",
        "desc": "An ornate creepers-and-leaves motif joining the sacred vatis, celebrating prosperity, family bond, and auspicious beginnings."
    },
    {
        "name": "The Yeijah Mangaslsutra Necklace",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-yeijah-mangaslsutra-necklace~163411.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-yeijah-mangaslsutra-necklace-carousel-8.webp",
        "alt": "marathi mangalsutra 2026 gift idea: The Yeijah Mangaslsutra Necklace",
        "desc": "An architectural gold pendant head flanked by high-polish cylindrical barrels and hand-woven black onyx bead links."
    },
    {
        "name": "The Yosni Mangalsutra",
        "url": "https://www.bluestone.com/mangalsutra+chains/the-yosni-mangalsutra~81520.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-yosni-mangalsutra-carousel-4.webp",
        "alt": "marathi mangalsutra 2026 gift idea: The Yosni Mangalsutra",
        "desc": "Sleek minimalist vatis on an ergonomic short chain, delivering classic symbolic protection with lightweight all-day elegance."
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
    print(f"\n--- Upgrading Post {POST_ID} (Marathi Mangalsutra 2026) Carousel ---")
    verify_images()
    
    post = fetch_post(POST_ID)
    raw = post.get("content", {}).get("raw", "")
    print(f"Original content length: {len(raw)}")
    
    # Match any carousel block in the post
    pattern = r"<!-- wp:html -->[\s\S]*?id=\"bs-cf-marathi-mangalsutra\"[\s\S]*?<!-- /wp:html -->(\s*<!-- wp:paragraph -->\s*<p><strong>Curated Design Highlights:</strong></p>\s*<!-- /wp:paragraph -->\s*<!-- wp:list -->\s*<ul>[\s\S]*?</ul>\s*<!-- /wp:list -->)?"
    m = re.search(pattern, raw)
    if not m:
        # Check if there is an unclosed or alternative pattern
        pattern2 = r"<!-- wp:html -->[\s\S]*?bs-cf-marathi-mangalsutra[\s\S]*?<!-- /wp:html -->"
        m = re.search(pattern2, raw)
        if not m:
            print("ERROR: Carousel block pattern not found in post 37986!")
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
