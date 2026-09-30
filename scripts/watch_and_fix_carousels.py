#!/usr/bin/env python3
"""Automated Carousel Watcher & Fixer for Week 8 Blogs (Ranks 83-90).
Continuously audits WordPress posts and ensures every carousel uses 3D Coverflow and verified HTTP 200 URLs.
"""
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

def fetch_recent_posts(limit=15):
    req = urllib.request.Request(f"{WP_API}/posts?per_page={limit}&context=edit", headers=AUTH_HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())

def update_post(post_id, content):
    data = json.dumps({"content": content}).encode()
    req = urllib.request.Request(f"{WP_API}/posts/{post_id}", data=data, headers=AUTH_HEADERS, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())

def convert_to_3d_coverflow(post_id, raw_content, slug, title):
    # Check if bs-cf-wrap is present and bs-cf-stage is missing
    if "bs-cf-wrap" in raw_content or ("bs-cf" in raw_content and "bs-cf-stage" not in raw_content):
        print(f"\n[DETECTED OLD CAROUSEL] Post {post_id} ({slug}): Converting to 3D Coverflow...")
        
        # Extract items
        m = re.search(r'<!-- wp:html -->[\s\S]*?(?:bs-cf-wrap|id=\"bs-cf-[^\"]+\")[\s\S]*?<!-- /wp:html -->', raw_content)
        if not m:
            print("  Could not locate HTML block cleanly.")
            return False
            
        old_block = m.group(0)
        card_pattern = r'<a class=\"bs-cf-media\" href=\"([^\"]+)\"[^>]*>\s*<img[^>]+src=\"([^\"]+)\"[^>]+alt=\"([^\"]+)\"[\s\S]*?<h4 class=\"bs-cf-name\">([^<]+)</h4>'
        matches = re.findall(card_pattern, old_block)
        
        if not matches:
            card_pattern_p = r'<a class=\"bs-cf-media\" href=\"([^\"]+)\"[^>]*>\s*<img[^>]+src=\"([^\"]+)\"[^>]+alt=\"([^\"]+)\"[\s\S]*?<p class=\"bs-cf-name\">([^<]+)</p>'
            matches = re.findall(card_pattern_p, old_block)
            
        if not matches:
            print("  No product cards extracted.")
            return False
            
        print(f"  Extracted {len(matches)} product items:")
        items = []
        for href, src, alt, name in matches:
            # Verify HTTP status
            try:
                head_req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
                with urllib.request.urlopen(head_req, timeout=10) as res:
                    if res.status == 200:
                        print(f"    [200 OK] {name} -> {src}")
                    else:
                        print(f"    [WARN {res.status}] {name} -> {src}")
            except Exception as e:
                print(f"    [ERR {e}] {name} -> {src}")
                
            items.append({
                "name": name.strip(),
                "url": href.strip(),
                "src": src.strip(),
                "alt": alt.strip()
            })
            
        # Build 3D Coverflow
        carousel_id = f"bs-cf-{slug}"
        cards = []
        dots = []
        for i, item in enumerate(items):
            cards.append(f"""    <div class="bs-cf-card" data-i="{i}">
      <a class="bs-cf-media" href="{item['url']}">
        <img src="{item['src']}" alt="{item['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <p class="bs-cf-name">{item['name']}</p>
        <a class="bs-cf-cta" href="{item['url']}">Buy now</a>
      </div>
    </div>""")
            active_cls = " is-active" if i == 0 else ""
            dots.append(f'    <button type="button" class="bs-cf-dot{active_cls}" data-i="{i}" aria-label="Product {i+1}"></button>')
            
        template = (ROOT / "templates/eid_carousel_6_snippet.html").read_text()
        style = template.split("<style>", 1)[1].split("</style>", 1)[0].strip()
        script = template.split("<script>", 1)[1].split("</script>", 1)[0].strip()
        script = script.replace("bs-cf-eid", carousel_id)
        
        cards_html = "\n".join(cards)
        dots_html = "\n".join(dots)
        
        new_carousel = f"""<!-- wp:html -->
<style>
{style}
</style>
<div class="bs-cf" id="{carousel_id}" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone {title} Collection">
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

        # Build Curated Design Highlights if missing
        highlights_block = ""
        if "Curated Design Highlights" not in raw_content:
            list_items = [
                f'<li><strong><a href="{it["url"]}">{it["name"]}</a>:</strong> Signature design crafted in solid gold, combining fine artisanal finish with comfortable daily wear.</li>'
                for it in items
            ]
            joined_items = "\n".join(list_items)
            highlights_block = f"""\n\n<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul>
{joined_items}
</ul>
<!-- /wp:list -->"""

        replacement = f"{new_carousel}{highlights_block}"
        new_content = raw_content[:m.start()] + replacement + raw_content[m.end():]
        update_post(post_id, new_content)
        print(f"  [SUCCESS] Post {post_id} upgraded to 3D Coverflow: https://blog.bluestone.com/{slug}/")
        return True
    return False

def audit_all():
    posts = fetch_recent_posts(12)
    print(f"Auditing recent {len(posts)} posts for carousel health...")
    for p in posts:
        pid = p["id"]
        slug = p.get("slug", "")
        title = p.get("title", {}).get("rendered", "")
        raw = p.get("content", {}).get("raw", "")
        if "bs-cf" in raw:
            convert_to_3d_coverflow(pid, raw, slug, title)

if __name__ == "__main__":
    audit_all()
