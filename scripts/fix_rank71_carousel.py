#!/usr/bin/env python3
"""Fix carousel block and editorial highlights in WordPress post 37753 (Cocktail Rings Buying Guide 2026)."""
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
POST_ID = 37753

# 6 Carousel items with verified media URLs and PDP links
CAROUSEL_ITEMS = [
    {
        "name": "The Gigi Ring",
        "url": "https://www.bluestone.com/rings/the-gigi-ring~64382.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-gigi-ring-carousel-2.webp",
        "alt": "cocktail rings 2026 gift idea: The Gigi Ring",
        "desc": "A breathtaking masterpiece in high jewellery engineering, The Gigi Ring features an opulent floral cluster arrangement of brilliant-cut diamonds embraced by an openwork gold cage gallery. Spanning 23 mm in height and over 16 mm in width, this design delivers majestic presence without overwhelming the hand. Best for gala receptions, black-tie cocktail parties, and milestone anniversaries."
    },
    {
        "name": "The Ebony Ring",
        "url": "https://www.bluestone.com/rings/the-ebony-ring~9686.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-ebony-ring-carousel-6.webp",
        "alt": "cocktail rings 2026 gift idea: The Ebony Ring",
        "desc": "Radiating regal vintage charm, The Ebony Ring showcases an expansive diamond medallion surrounded by fine milgrain borders and warm 18K yellow gold contours. Its wide 18.35 mm face creates an enchanting tapestry of light across the finger, making it an exquisite companion for silk sarees and velvet evening capes. Best for festive family celebrations and heirloom trousseau investments."
    },
    {
        "name": "The Yuthika Highway Ring",
        "url": "https://www.bluestone.com/rings/the-yuthika-highway-ring~131078.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-yuthika-highway-ring-carousel-1.webp",
        "alt": "cocktail rings 2026 gift idea: The Yuthika Highway Ring",
        "desc": "Celebrating contemporary architectural geometry, The Yuthika Highway Ring features multi-tier overlapping gold bands studded with shimmering diamond pavé tracks. Its multi-row crossover framework creates sweeping diagonal lines that visually elongate the fingers while maintaining comfortable airflow. Best for modern cocktail soirées, corporate gala banquets, and fashion-forward evening wear."
    },
    {
        "name": "The Haily Ring",
        "url": "https://www.bluestone.com/rings/the-haily-ring~64366.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-haily-ring-carousel-1.webp",
        "alt": "cocktail rings 2026 gift idea: The Haily Ring",
        "desc": "For lovers of bold sculptural minimalism, The Haily Ring presents a polished bombe dome silhouette in solid radiant gold. Rising with fluid organic curves, this sculptural statement piece catches specular room reflections with mirror-like brilliance. Best for contemporary art gallery previews, upscale dinner dates, and minimalist luxury enthusiasts."
    },
    {
        "name": "The Viperine Twist Ring",
        "url": "https://www.bluestone.com/rings/the-viperine-twist-ring~124507.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-viperine-twist-ring-carousel-3.webp",
        "alt": "cocktail rings 2026 gift idea: The Viperine Twist Ring",
        "desc": "Inspired by serpentine elegance and fluid movement, The Viperine Twist Ring wraps the finger in a dynamic bypass silhouette of ribbed gold ribbons. The organic twist coils gracefully, offering an edgy yet refined silhouette that flatters the index or middle finger. Best for celebratory brunch gatherings, cocktail lounge parties, and expressive personal styling."
    },
    {
        "name": "The Malibu Ring",
        "url": "https://www.bluestone.com/rings/the-malibu-ring~2321.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-malibu-ring-carousel-6.webp",
        "alt": "cocktail rings 2026 gift idea: The Malibu Ring",
        "desc": "Evoking the radiant energy of a golden sunset, The Malibu Ring showcases a sunburst cluster of brilliant diamonds set atop an elevated golden halo. Its tapered shoulders focus all attention onto the sparkling celestial head, creating an illusion of boundless brilliance. Best for engagement anniversary dinners, festive cocktail receptions, and festive gifting."
    }
]

def build_clean_carousel_block(carousel_id="bs-cf-cocktail-rings"):
    cards = []
    dots = []
    
    for i, item in enumerate(CAROUSEL_ITEMS):
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
<div class="bs-cf" id="{carousel_id}" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone Cocktail Rings Collection">
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

def build_editorial_highlights_block():
    list_items = []
    for item in CAROUSEL_ITEMS:
        list_items.append(
            f'<li><strong><a href="{item["url"]}">{item["name"]}</a>:</strong> {item["desc"]}</li>'
        )
    items_html = "\n".join(list_items)
    
    return f"""<!-- wp:paragraph -->
<p><strong>Editorial Highlights from the Collection:</strong></p>
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
    post = fetch_post(POST_ID)
    title = post.get("title", {}).get("raw", "")
    content = post.get("content", {}).get("raw", "")
    print(f"Fetched post ID {POST_ID}: {title}")
    print(f"Current content length: {len(content)} chars")
    
    # Target the corrupted region between the intro paragraph and the next heading
    start_pattern = r'(<!-- wp:paragraph.*?-->\s*<p.*?>At BlueStone, our master artisans craft womens cocktail rings[\s\S]*?<!-- /wp:paragraph -->)'
    m_start = re.search(start_pattern, content)
    if not m_start:
        print("ERROR: Start pattern not found!")
        return False
    
    end_pattern = r'(<!-- wp:heading.*?-->\s*<h2.*?>Gemstone Settings and Prong Security: Protecting Heavy Statement Stones</h2>\s*<!-- /wp:heading -->)'
    m_end = re.search(end_pattern, content)
    if not m_end:
        print("ERROR: End pattern not found!")
        return False
    
    start_pos = m_start.end()
    end_pos = m_end.start()
    
    corrupted_segment = content[start_pos:end_pos]
    print(f"Corrupted segment length: {len(corrupted_segment)} chars")
    
    clean_carousel = build_clean_carousel_block("bs-cf-cocktail-rings")
    clean_highlights = build_editorial_highlights_block()
    
    replacement = f"\n\n{clean_carousel}\n\n{clean_highlights}\n\n"
    
    new_content = content[:start_pos] + replacement + content[end_pos:]
    print(f"New content length: {len(new_content)} chars")
    
    # Verify no prohibited characters or broken tags
    assert "<!-- wp:html -->" in new_content
    assert "<!-- /wp:html -->" in new_content
    assert "<p><script></p>" not in new_content
    assert "<p>.bs-cf" not in new_content
    
    updated = update_post(POST_ID, new_content)
    print(f"SUCCESS: Post {POST_ID} updated successfully!")
    print(f"Live URL: {updated.get('link')}")
    return True

if __name__ == "__main__":
    main()
