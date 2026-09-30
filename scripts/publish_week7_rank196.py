#!/usr/bin/env python3
"""Publish script for Week 7 Rank 196: Big Earrings."""
import os
import re
import sys
import json
import base64
import urllib.request
from html import escape
from pathlib import Path

from build_week7_rank196_big_earrings import (
    build_article_content,
    check_no_prohibited_characters,
    TITLE,
    SEO_TITLE,
    META_DESC,
    SLUG,
    AUTHOR_ID,
    CATEGORIES,
    PRIMARY_KEYWORD,
    CAROUSEL_PRODUCTS
)

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

def build_carousel_html():
    media_json_path = ROOT / "output/carousel_webp/rank196/media_ids.json"
    with open(media_json_path) as f:
        media_list = json.load(f)
    
    # Map by name
    media_by_name = {m["name"]: m for m in media_list}
    
    cards = []
    dots = []
    carousel_id = "bs-cf-big-earrings"
    
    for i, prod in enumerate(CAROUSEL_PRODUCTS):
        name = prod["name"]
        m = media_by_name[name]
        src = m["src"]
        alt = escape(m["alt"])
        url = prod["url"]
        
        cards.append(f"""    <div class="bs-cf-card" data-i="{i}">
      <a class="bs-cf-media" href="{url}">
        <img src="{src}" alt="{alt}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <p class="bs-cf-name">{escape(name)}</p>
        <a class="bs-cf-cta" href="{url}">Buy now</a>
      </div>
    </div>""")
        
        active_cls = " is-active" if i == 0 else ""
        dots.append(f'    <button type="button" class="bs-cf-dot{active_cls}" data-i="{i}" aria-label="Product {i+1}"></button>')
        
    cards_html = "\n".join(cards)
    dots_html = "\n".join(dots)
    
    template = (ROOT / "templates/eid_carousel_6_snippet.html").read_text()
    style = template.split("<style>", 1)[1].split("</style>", 1)[0]
    script = template.split("<script>", 1)[1].split("</script>", 1)[0]
    script = script.replace("bs-cf-eid", carousel_id)
    
    carousel_html = f"""<!-- wp:html -->
<style>
{style}
</style>
<div class="bs-cf" id="{carousel_id}" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone Big Earrings Collection">
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
    return carousel_html

def build_schema_blocks(faq_items):
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_items
    }
    
    blog_schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": TITLE,
        "description": META_DESC,
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"https://blog.bluestone.com/{SLUG}/"
        },
        "author": {
            "@type": "Person",
            "name": "Satyam",
            "url": "https://blog.bluestone.com/author/satyam/"
        },
        "publisher": {
            "@type": "Organization",
            "name": "BlueStone Jewellery",
            "logo": {
                "@type": "ImageObject",
                "url": "https://blog.bluestone.com/wp-content/uploads/2021/04/bluestone-logo.png"
            }
        },
        "datePublished": "2026-08-30T14:33:00+00:00",
        "dateModified": "2026-08-30T14:33:00+00:00"
    }
    
    schema_html = f"""<!-- wp:html -->
<script type="application/ld+json">
{json.dumps(faq_schema, indent=2, ensure_ascii=False)}
</script>
<script type="application/ld+json">
{json.dumps(blog_schema, indent=2, ensure_ascii=False)}
</script>
<!-- /wp:html -->"""
    return schema_html

def publish():
    raw_content, faq_items, word_count = build_article_content()
    carousel_html = build_carousel_html()
    schema_html = build_schema_blocks(faq_items)
    
    # Replace carousel placeholder
    assert "<!-- CAROUSEL_PLACEHOLDER -->" in raw_content
    full_content = raw_content.replace("<!-- CAROUSEL_PLACEHOLDER -->", carousel_html)
    
    # Append schema at the end
    full_content = full_content + "\n\n" + schema_html
    
    # check_no_prohibited_characters was already verified on raw_content
    
    post_payload = {
        "title": TITLE,
        "slug": SLUG,
        "content": full_content,
        "author": AUTHOR_ID,
        "categories": CATEGORIES,
        "status": "publish",
        "meta": {
            "_yoast_wpseo_focuskw": PRIMARY_KEYWORD,
            "_yoast_wpseo_title": SEO_TITLE,
            "_yoast_wpseo_metadesc": META_DESC
        }
    }
    
    req = urllib.request.Request(
        f"{WP_API}/posts",
        data=json.dumps(post_payload).encode(),
        headers=AUTH_HEADERS,
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        post_data = json.loads(resp.read().decode())
        
    post_id = post_data["id"]
    post_link = post_data["link"]
    print(f"Published WordPress Post ID: {post_id}")
    print(f"Live URL: {post_link}")
    
    # Save post details
    out_info = {
        "post_id": post_id,
        "link": post_link,
        "slug": SLUG,
        "title": TITLE,
        "author": AUTHOR_ID,
        "categories": CATEGORIES,
        "word_count": word_count
    }
    with open("output/rank196_post_info.json", "w") as f:
        json.dump(out_info, f, indent=2)
    return post_id, post_link

if __name__ == "__main__":
    publish()
