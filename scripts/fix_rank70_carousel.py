#!/usr/bin/env python3
"""Fix carousel block and editorial highlights in WordPress post 37742 (Dangler Earrings Buying Guide 2026)."""
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
POST_ID = 37742

# 6 Carousel cards with verified media URLs and PDP links
CAROUSEL_ITEMS = [
    {
        "name": "The Aleena Huggie Earrings",
        "url": "https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-aleena-huggie-earrings-carousel-10.webp",
        "alt": "dangler earrings 2026 gift idea: The Aleena Huggie Earrings",
        "desc": "Radiating classic charm, The Aleena Huggie pairs shimmering diamonds with a graceful dangling silhouette in 18K gold. The fluid suspension provides gentle kinetic sway that complements cocktail dresses and evening ensembles with equal sophistication. Best for formal wedding receptions, celebratory dinners, and festive family reunions."
    },
    {
        "name": "The Nettile Huggie Earrings",
        "url": "https://www.bluestone.com/earrings/the-nettile-huggie-earrings~108215.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-nettile-huggie-earrings-carousel-8.webp",
        "alt": "dangler earrings 2026 gift idea: The Nettile Huggie Earrings",
        "desc": "Featuring an intricate geometric openwork drop in glowing 18K gold and diamonds, The Nettile Huggie delivers modern artistic flair. Its balanced proportions provide visual presence while remaining remarkably lightweight for all-day comfort. Best for cocktail parties, festive celebrations, and anniversary gifting."
    },
    {
        "name": "The Skein Hoop Earrings",
        "url": "https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-skein-hoop-earrings-carousel-8.webp",
        "alt": "dangler earrings 2026 gift idea: The Skein Hoop Earrings",
        "desc": "Inspired by entwined threads of golden yarn, The Skein Hoop introduces rich visual texture and dimensional warmth. The articulated hoop drops fluidly below the lobe, catching light across its interwoven gold contours. Best for pairing with traditional silk sarees, festive kurtas, and artisanal handloom ensembles."
    },
    {
        "name": "The Vicky Hoop Earrings",
        "url": "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-vicky-hoop-earrings-carousel-9.webp",
        "alt": "dangler earrings 2026 gift idea: The Vicky Hoop Earrings",
        "desc": "For those who cherish understated, weightless elegance, The Vicky Hoop features an articulated miniature silhouette in glowing 18K gold with sparkling diamond highlights. Its compact dimensions ensure total safety around scarves and active routines. Best for everyday signature wear, college wear, and thoughtful first fine jewellery gifts."
    },
    {
        "name": "The Ursa Hoop Earrings",
        "url": "https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-ursa-hoop-earrings-carousel-6.webp",
        "alt": "dangler earrings 2026 gift idea: The Ursa Hoop Earrings",
        "desc": "Showcasing celestial-inspired sculptural contours in 18K yellow gold, The Ursa Hoop offers modern celestial sophistication with gentle drop mobility. Best for chic evening wear, gallery openings, and milestone celebrations."
    },
    {
        "name": "The Asya Huggie Earrings",
        "url": "https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-asya-huggie-earrings-carousel-7.webp",
        "alt": "dangler earrings 2026 gift idea: The Asya Huggie Earrings",
        "desc": "Featuring articulated drop elements suspended from a comfortable huggie hoop in 18K yellow gold with sparkling diamonds, this design is the ultimate versatile day-to-night showstopper. The secure huggie clasp sits flush against the lobe, while the dangling teardrop catches ambient light with every subtle gesture. Best for effortless desk-to-dinner transitions and milestone anniversary gifting."
    }
]

def build_clean_carousel_block(carousel_id="bs-cf-dangler-earrings"):
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
<div class="bs-cf" id="{carousel_id}" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone Dangler Earrings Collection">
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
    # Find start marker
    start_pattern = r'(<!-- wp:paragraph.*?-->\s*<p.*?>At BlueStone, our fine jewellery artisans combine exquisite craftsmanship[\s\S]*?<!-- /wp:paragraph -->)'
    m_start = re.search(start_pattern, content)
    if not m_start:
        print("ERROR: Start pattern not found!")
        return False
    
    # Find end marker (the next H2)
    end_pattern = r'(<!-- wp:heading.*?-->\s*<h2.*?>Earring Backs, Closures, and Lobe Safety for Dangler Earrings</h2>\s*<!-- /wp:heading -->)'
    m_end = re.search(end_pattern, content)
    if not m_end:
        print("ERROR: End pattern not found!")
        return False
    
    start_pos = m_start.end()
    end_pos = m_end.start()
    
    corrupted_segment = content[start_pos:end_pos]
    print(f"Corrupted segment length: {len(corrupted_segment)} chars")
    
    clean_carousel = build_clean_carousel_block("bs-cf-dangler-earrings")
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
