#!/usr/bin/env python3
"""Publish post for Week 8 Rank 178: Finger Rings for Girls 2026."""
import os
import sys
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path("/Users/satyamkumar/Downloads/seo final 2026")
sys.path.insert(0, str(ROOT / "scripts"))

from build_week8_rank178_finger_rings_for_girls import (
    build_draft_article,
    check_prohibitions,
    TITLE,
    SEO_TITLE,
    META_DESC,
    SLUG,
    AUTHOR_ID,
    CATEGORIES,
    PRIMARY_KEYWORD
)

# Load environment
env_path = ROOT / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

USER = os.environ.get("WP_USER", "blogbluestone")
PWD = os.environ.get("WP_APP_PASSWORD") or os.environ.get("WP_APP_PASS") or os.environ.get("WP_PASSWORD", "")
token = base64.b64encode(f"{USER}:{PWD}".encode()).decode()
headers = {
    "Authorization": f"Basic {token}",
    "User-Agent": "BluestoneSEO/1.0",
    "Content-Type": "application/json"
}


def build_3d_coverflow_html(carousel_items):
    """Builds the strict 3D Coverflow carousel block matching eid_carousel_6_snippet.html."""
    cards_html = []
    # Pos mapping: 0, 1, 2, 3, -2, -1
    pos_classes = ["is-pos-0", "is-pos-1", "is-pos-2", "is-pos-3", "is-pos--2", "is-pos--1"]
    for i, item in enumerate(carousel_items):
        cls = pos_classes[i]
        c = f"""    <div class="bs-cf-card {cls}" data-index="{i}">
      <a class="bs-cf-media" href="{item['url']}">
        <img src="{item['image_url']}" alt="{item['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{item['name']}</div>
        <a class="bs-cf-cta" href="{item['url']}">Buy now</a>
      </div>
    </div>"""
        cards_html.append(c)

    cards_joined = "\n".join(cards_html)

    carousel_block = f"""<!-- wp:html -->
<style>
.bs-cf{{max-width:900px;margin:1.75rem auto 1.25rem;position:relative;perspective:1200px}}
.bs-cf-stage{{position:relative;height:360px;margin:0 auto;overflow:visible}}
.bs-cf-card{{position:absolute;top:0;left:50%;width:min(420px,78vw);transform-origin:center center;transition:transform .65s cubic-bezier(.22,.61,.36,1),opacity .65s ease,filter .65s ease;border-radius:16px;background:#fff;box-shadow:0 12px 30px rgba(0,0,0,.12);overflow:hidden;border:1px solid #ececec}}
.bs-cf-media{{display:block;line-height:0;background:#f4f4f4}}
.bs-cf-media img{{display:block;width:100%;aspect-ratio:16/9;height:auto;object-fit:cover;object-position:center}}
.bs-cf-meta{{padding:14px 16px 16px;text-align:center;background:#fff}}
.bs-cf-name{{margin:0 0 10px;font-size:1rem;font-weight:600;color:#1a1a1a;text-decoration:none;line-height:1.35;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.bs-cf-cta{{display:inline-block;padding:8px 18px;border-radius:2px;background:#111;color:#fff!important;font-size:.875rem;font-weight:600;text-decoration:none!important;letter-spacing:.02em}}
.bs-cf-cta:hover{{background:#333;color:#fff!important}}
.bs-cf-card.is-pos-0{{z-index:5;opacity:1;filter:none;transform:translate3d(-50%,8px,0) scale(1.02)}}
.bs-cf-card.is-pos-1{{z-index:3;opacity:.95;filter:brightness(.97);transform:translate3d(calc(-50% + 210px),34px,-110px) rotateY(-26deg) scale(.78)}}
.bs-cf-card.is-pos-2{{z-index:3;opacity:.95;filter:brightness(.97);transform:translate3d(calc(-50% - 210px),34px,-110px) rotateY(26deg) scale(.78)}}
.bs-cf-card.is-pos-3,.bs-cf-card.is-pos--3{{z-index:1;opacity:.3;pointer-events:none;transform:translate3d(calc(-50% + 340px),54px,-200px) rotateY(-36deg) scale(.58)}}
.bs-cf-card.is-pos--1{{z-index:1;opacity:.3;pointer-events:none;transform:translate3d(calc(-50% - 340px),54px,-200px) rotateY(36deg) scale(.58)}}
.bs-cf-dots{{display:flex;justify-content:center;gap:8px;margin-top:14px}}
.bs-cf-dot{{width:8px;height:8px;border-radius:50%;border:0;padding:0;background:#c8c8c8;cursor:pointer}}
.bs-cf-dot.is-active{{background:#111;transform:scale(1.2)}}
.bs-cf-nav{{position:absolute;top:38%;z-index:8;width:38px;height:38px;border:0;border-radius:50%;background:rgba(255,255,255,.96);box-shadow:0 2px 8px rgba(0,0,0,.14);cursor:pointer;font-size:20px;color:#222;transform:translateY(-50%)}}
.bs-cf-prev{{left:0}}.bs-cf-next{{right:0}}
@media (max-width:700px){{
  .bs-cf-stage{{height:300px}}
  .bs-cf-card{{width:min(300px,84vw)}}
  .bs-cf-card.is-pos-1{{transform:translate3d(calc(-50% + 130px),36px,-80px) rotateY(-24deg) scale(.72)}}
  .bs-cf-card.is-pos-2{{transform:translate3d(calc(-50% - 130px),36px,-80px) rotateY(24deg) scale(.72)}}
  .bs-cf-card.is-pos-3,.bs-cf-card.is-pos--3,.bs-cf-card.is-pos--1{{opacity:0}}
}}
@media (prefers-reduced-motion:reduce){{.bs-cf-card{{transition:none}}}}
</style>
<div class="bs-cf" id="bs-cf-{SLUG}" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone finger rings for girls gift ideas">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
{cards_joined}
  </div>
  <div class="bs-cf-dots" role="tablist">
    <button type="button" class="bs-cf-dot is-active" data-i="0" aria-label="Product 1"></button>
    <button type="button" class="bs-cf-dot" data-i="1" aria-label="Product 2"></button>
    <button type="button" class="bs-cf-dot" data-i="2" aria-label="Product 3"></button>
    <button type="button" class="bs-cf-dot" data-i="3" aria-label="Product 4"></button>
    <button type="button" class="bs-cf-dot" data-i="4" aria-label="Product 5"></button>
    <button type="button" class="bs-cf-dot" data-i="5" aria-label="Product 6"></button>
  </div>
</div>
<script>
(function(){{
  var root=document.getElementById('bs-cf-{SLUG}');
  if(!root||root.dataset.ready)return;
  root.dataset.ready='1';
  var cards=[].slice.call(root.querySelectorAll('.bs-cf-card'));
  var dots=[].slice.call(root.querySelectorAll('.bs-cf-dot'));
  var n=cards.length, active=0, timer=null;
  var ms=parseInt(root.getAttribute('data-interval'),10)||3200;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function rel(i){{ var d=((i-active)%n+n)%n; if(d>n/2)d=d-n; return d; }}
  function paint(){{
    cards.forEach(function(c,i){{
      c.className='bs-cf-card';
      var d=rel(i), cls='is-pos-'+d;
      if(d===-1)cls='is-pos-2'; if(d===1)cls='is-pos-1'; if(d===0)cls='is-pos-0';
      if(d===-2||d===2)cls=d===2?'is-pos-3':'is-pos--1';
      c.classList.add(cls);
    }});
    dots.forEach(function(d,i){{d.classList.toggle('is-active',i===active)}});
  }}
  function go(to){{active=((to%n)+n)%n;paint()}}
  function next(){{go(active+1)}}
  function prev(){{go(active-1)}}
  function stop(){{if(timer){{clearInterval(timer);timer=null}}}}
  function start(){{if(reduce)return;stop();timer=setInterval(next,ms)}}
  root.querySelector('.bs-cf-next').addEventListener('click',function(){{next();start()}});
  root.querySelector('.bs-cf-prev').addEventListener('click',function(){{prev();start()}});
  dots.forEach(function(d){{d.addEventListener('click',function(){{go(+d.getAttribute('data-i'));start()}})}});
  root.addEventListener('mouseenter',stop);
  root.addEventListener('mouseleave',start);
  paint(); start();
}})();
</script>
<!-- /wp:html -->"""
    return carousel_block


def main():
    print(f"Preparing to publish Week 8 Rank 178: {SLUG}...")
    
    # 1. Load draft
    content = build_draft_article()
    
    # 2. Load verified carousel items
    media_json = ROOT / "output/week8_rank178_product_media.json"
    if not media_json.exists():
        raise FileNotFoundError(f"Missing {media_json}! Run prepare_week8_rank178_carousel.py first.")
    
    carousel_items = json.loads(media_json.read_text(encoding="utf-8"))
    if len(carousel_items) != 6:
        raise ValueError(f"Expected 6 carousel items, got {len(carousel_items)}")

    # 3. Replace carousel placeholder
    carousel_block = build_3d_coverflow_html(carousel_items)
    content = content.replace("<!-- CAROUSEL_PLACEHOLDER -->", carousel_block)

    # 4. Check prohibitions
    errs = check_prohibitions(content)
    if errs:
        print("Validation errors:")
        for e in errs:
            print("  -", e)
        raise ValueError("Article failed validation rules!")

    # Save full article before patch
    article_html_path = ROOT / "output/week8_rank178_article_content.html"
    with open(article_html_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved initial full article content to {article_html_path}")

    # Check if post already exists
    post_id = None
    search_url = f"https://blog.bluestone.com/wp-json/wp/v2/posts?slug={SLUG}&status=any"
    req = urllib.request.Request(search_url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            posts = json.loads(resp.read().decode())
            if posts:
                post_id = posts[0]["id"]
                print(f"Found existing post ID {post_id} for slug {SLUG}")
    except Exception as e:
        print(f"Error checking existing post: {e}")

    payload = {
        "title": TITLE,
        "slug": SLUG,
        "status": "publish",
        "author": AUTHOR_ID,
        "categories": CATEGORIES,
        "content": content,
        "meta": {
            "_yoast_wpseo_title": SEO_TITLE,
            "_yoast_wpseo_metadesc": META_DESC,
            "_yoast_wpseo_focuskw": PRIMARY_KEYWORD
        }
    }

    if post_id:
        url = f"https://blog.bluestone.com/wp-json/wp/v2/posts/{post_id}"
        method = "POST"
        print(f"Updating post ID {post_id}...")
    else:
        url = "https://blog.bluestone.com/wp-json/wp/v2/posts"
        method = "POST"
        print(f"Creating new post for slug {SLUG}...")

    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data_bytes, headers=headers, method=method)
    
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode())
        post_id = result["id"]
        post_link = result.get("link", f"https://blog.bluestone.com/{SLUG}/")
        print(f"Successfully published post! ID: {post_id} | Link: {post_link}")

    # Save wp post info
    wp_info = {
        "id": post_id,
        "slug": SLUG,
        "link": post_link,
        "title": TITLE,
        "author": AUTHOR_ID,
        "categories": CATEGORIES,
        "status": "publish"
    }
    wp_json_path = ROOT / "output/week8_rank178_wp_post.json"
    with open(wp_json_path, "w", encoding="utf-8") as f:
        json.dump(wp_info, f, indent=2)
    print(f"Saved post details to {wp_json_path}")
    return post_id


if __name__ == "__main__":
    main()
