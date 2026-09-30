#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish Week 9 Rank 86 post to WordPress (modern vanki ring designs)."""
import json
import os
import sys
import base64
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Load environment
for ep in [ROOT / ".env", Path("/Users/satyamkumar/Downloads/seo final 2026/.env")]:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

wp_user = os.environ.get("WP_USER", "blogbluestone")
wp_pass = os.environ.get("WP_APP_PASSWORD") or os.environ.get("WP_APP_PASS") or os.environ.get("WP_PASSWORD", "")
auth_header = 'Basic ' + base64.b64encode((wp_user + ':' + wp_pass).encode()).decode()

headers = {
    'Authorization': auth_header,
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
}
api_base = 'https://blog.bluestone.com/wp-json/wp/v2'

slug = 'modern-vanki-ring-designs-2026'
title = 'How to Choose and Style Modern Vanki Ring Designs: An Expert Buying Guide (2026)'
meta_desc = "Discover modern vanki ring designs in 2026. Explore traditional symbolism, lightweight daily gold engineering, 18K vs 14K gold, styling tips, and sizing advice."
author_id = 270271337
categories = [554493348, 554493465] # Gold (554493348), Jewellery Problem & Solution (554493465)

# 1. Exact slug check before creating
req_check = urllib.request.Request(f'{api_base}/posts?slug={slug}&status=any', headers=headers)
with urllib.request.urlopen(req_check) as resp:
    existing = json.loads(resp.read().decode())
    if existing:
        print(f"Post with slug {slug} already exists! ID: {existing[0]['id']}")
        with open(ROOT / 'output/week9_rank86_published_post.json', 'w') as out_f:
            json.dump(existing[0], out_f, indent=2)
        sys.exit(0)

with open(ROOT / 'output/week9_rank86_draft.html', encoding='utf-8') as f:
    body_content = f.read()

with open(ROOT / 'output/week9_rank86_carousel_media.json', encoding='utf-8') as f:
    carousel_items = json.load(f)

# Build 3D Coverflow carousel HTML block from template
pos_classes = ['is-pos-0', 'is-pos-1', 'is-pos-2', 'is-pos-3', 'is-pos--2', 'is-pos--1']
carousel_id = 'bs-cf-modern-vanki-ring-designs'

cards_html = []
dots_html = []

for idx, item in enumerate(carousel_items):
    pos_cls = pos_classes[idx]
    active_cls = ' is-active' if idx == 0 else ''
    card = f"""    <div class="bs-cf-card {pos_cls}" data-index="{idx}">
      <a class="bs-cf-media" href="{item['url']}">
        <img src="{item['image_url']}" alt="{item['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{item['name']}</div>
        <a class="bs-cf-cta" href="{item['url']}">Buy now</a>
      </div>
    </div>"""
    cards_html.append(card)
    dots_html.append(f'    <button type="button" class="bs-cf-dot{active_cls}" data-i="{idx}" aria-label="Product {idx+1}"></button>')

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
<div class="bs-cf" id="{carousel_id}" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone modern vanki ring designs">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
{chr(10).join(cards_html)}
  </div>
  <div class="bs-cf-dots" role="tablist">
{chr(10).join(dots_html)}
  </div>
</div>
<script>
(function(){{
  var root=document.getElementById('{carousel_id}');
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

# Splice carousel into content
body_content = body_content.replace('CAROUSEL_SNIPPET_PLACEHOLDER', carousel_block)

# Trailing JSON-LD Schema
schema_json = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "BlogPosting",
            "@id": f"https://blog.bluestone.com/{slug}/#blogposting",
            "mainEntityOfPage": f"https://blog.bluestone.com/{slug}/",
            "headline": title,
            "description": meta_desc,
            "author": {
                "@type": "Person",
                "name": "Satyam",
                "jobTitle": "BlueStone Editorial"
            },
            "publisher": {
                "@type": "Organization",
                "name": "BlueStone",
                "url": "https://blog.bluestone.com"
            },
            "datePublished": "2026-09-28T16:30:00+05:30",
            "dateModified": "2026-09-28T16:30:00+05:30"
        },
        {
            "@type": "FAQPage",
            "@id": f"https://blog.bluestone.com/{slug}/#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "Which finger is a modern vanki ring traditionally worn on?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Traditionally, a vanki ring is worn on the ring finger or index finger of the right hand. In modern styling, however, women wear vanki rings on any finger, including the middle finger or thumb, depending on personal comfort and stacking preferences."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Which direction should the V of a vanki ring point?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Traditionally, the pointed apex of the V faces outward toward your fingernail, symbolizing an auspicious shield of protection and gracefully elongating the fingers. Alternatively, wearing the point facing inward toward your wrist creates a crown-like aesthetic that complements modern western attire."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Can modern vanki rings be worn as daily wear jewellery?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Yes. Contemporary modern vanki ring designs are specifically engineered as lightweight rings (typically 2 to 5 grams) with blunted, comfort-curved V-tips and low-profile diamond settings that prevent snagging on clothes, making them ideal for daily office and casual wear."
                    }
                },
                {
                    "@type": "Question",
                    "name": "What is the difference between a traditional vanki and a modern vanki ring?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "A traditional vanki was an elaborate, heavy gold armlet worn on the upper arm during bridal ceremonies. A modern vanki ring is an adapted fine jewellery finger ring that retains the distinctive V-silhouette while utilizing lightweight gold casting, diamonds, and minimalist proportions for versatile styling."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Is 18Kt or 14Kt gold better for a modern vanki ring?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Both karats are excellent choices. 18Kt gold offers a rich, classic golden hue and is ideal for diamond settings and festive occasions. 14Kt gold provides greater structural hardness and scratch resistance at an attractive price point, making it exceptionally well-suited for active daily wear."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Can I stack a modern vanki ring with my solitaire diamond ring?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Yes, modern vanki rings make superb stacking companions. The contoured V-curve naturally wraps around the base of a round, oval, or pear-cut solitaire, framing the center stone like an elegant crown without causing abrasive metal friction."
                    }
                }
            ]
        }
    ]
}

schema_block = f"""<!-- wp:html -->
<script type="application/ld+json">
{json.dumps(schema_json, indent=2, ensure_ascii=False)}
</script>
<!-- /wp:html -->"""

full_content = body_content.strip() + "\n\n" + schema_block

# Create WordPress post
post_payload = {
    'title': title,
    'slug': slug,
    'status': 'publish',
    'author': author_id,
    'categories': categories,
    'excerpt': meta_desc,
    'content': full_content,
    'featured_media': carousel_items[0]['media_id'],
    'meta': {
        '_yoast_wpseo_focuskw': 'modern vanki ring designs',
        '_yoast_wpseo_title': "Modern Vanki Ring Designs: 2026 Buying & Styling Guide | BlueStone",
        '_yoast_wpseo_metadesc': meta_desc
    }
}

req_create = urllib.request.Request(
    f'{api_base}/posts',
    data=json.dumps(post_payload).encode('utf-8'),
    headers=headers,
    method='POST'
)

with urllib.request.urlopen(req_create) as resp:
    post_res = json.loads(resp.read().decode())
    post_id = post_res['id']
    post_url = post_res['link']
    print(f"Successfully published post! ID: {post_id}")
    print(f"Live URL: {post_url}")
    with open(ROOT / 'output/week9_rank86_published_post.json', 'w') as out_f:
        json.dump(post_res, out_f, indent=2)

