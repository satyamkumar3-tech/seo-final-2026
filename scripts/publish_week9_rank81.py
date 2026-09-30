#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish Week 9 Rank 81 post to WordPress."""
import json
import os
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

with open(ROOT / 'output/Week9_Rank81_draft.json', encoding='utf-8') as f:
    draft = json.load(f)

with open(ROOT / 'output/week9_rank81_carousel_media.json', encoding='utf-8') as f:
    carousel_items = json.load(f)

slug = draft['slug']

# 1. Exact slug check before creating
req_check = urllib.request.Request(f'{api_base}/posts?slug={slug}', headers=headers)
with urllib.request.urlopen(req_check) as resp:
    existing = json.loads(resp.read().decode())
    if existing:
        print(f"Post with slug {slug} already exists! ID: {existing[0]['id']}")
        with open(ROOT / 'output/week9_rank81_published_post.json', 'w') as out_f:
            json.dump(existing[0], out_f, indent=2)
        exit(0)

# Build Carousel HTML
carousel_cards_html = []
for i, item in enumerate(carousel_items):
    pos_class = "is-pos-0" if i == 0 else f"is-pos-{i}" if i <= 3 else "is-pos--2" if i == 4 else "is-pos--1"
    card = f"""    <div class="bs-cf-card {pos_class}" data-index="{i}">
      <a class="bs-cf-media" href="{item['url']}">
        <img src="{item['src']}" alt="{item['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{item['name']}</div>
        <a class="bs-cf-cta" href="{item['url']}">Buy now</a>
      </div>
    </div>"""
    carousel_cards_html.append(card)

cards_block = "\n".join(carousel_cards_html)

carousel_html = f"""<!-- wp:html -->
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
<div class="bs-cf" id="bs-cf-{slug}" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone kids necklace and jewellery collection">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
{cards_block}
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
  var root=document.getElementById('bs-cf-{slug}');
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

content = draft['content'].replace('<!-- CAROUSEL_PLACEHOLDER -->', carousel_html)

# Add Trailing JSON-LD Schema
schema_json = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "FAQPage",
            "@id": f"https://blog.bluestone.com/{slug}/#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "What is the safest material for a kids necklace?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "The safest and most reliable material for a kids necklace is 14K or 18K solid gold certified with a BIS hallmark. High-purity gold alloys from reputable fine jewellers are strictly nickel-free, hypoallergenic, and resistant to tarnishing or corrosion from skin perspiration. Unlike cheap costume fashion jewellery that often contains toxic trace metals like lead or nickel, solid gold does not irritate sensitive young skin or cause allergic contact dermatitis."
                    }
                },
                {
                    "@type": "Question",
                    "name": "What necklace length is recommended for children of different ages?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "For toddlers and young children aged 3 to 6 years, a 12 to 14-inch chain sits comfortably above the collarbone without hanging low. For growing children aged 7 to 11 years, a 14 to 16-inch chain is ideal, offering a classic princess fit over festive lehengas or casual wear. For pre-teens aged 12 and above, 16 to 18-inch chains become suitable. Always choose chains equipped with extra jump rings so the necklace length can adjust as the child grows."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Can a child wear a gold necklace every day?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Yes, children can wear a gold necklace daily provided the piece is specifically engineered for kids. Look for lightweight designs weighing under 6 grams, smooth bezel or flush stone settings without protruding prongs, rounded edges, and sturdy weaves like cable or curb links. However, parents should always remove necklaces before bedtime, swimming, playground tumbling, or vigorous contact sports to prevent accidental snagging or damage."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Why are 14K and 18K gold preferred over 22K gold for kids jewellery?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "While 22K gold contains 91.6 percent pure gold, its high purity makes it naturally soft, malleable, and prone to stretching or bending under sudden physical stress. For an active child, a 22K chain link or pendant bail can warp and snap easily during play. By comparison, 14K and 18K gold are alloyed with stronger metals, providing the structural hardness and tensile strength necessary to resist active wear while maintaining glorious golden beauty."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How do stone necklaces for women differ from kids necklaces?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Stone necklaces for women are designed for adult frames, typically weighing between 15 and 50 grams or more, which causes significant neck strain and discomfort on young children. Furthermore, adult stone necklaces commonly feature elevated prong settings that easily catch on clothing or scratch skin. In contrast, kids necklaces feature featherlight weights (2 to 6 grams), smooth protective bezel surrounds, and calibrated safety chain lengths."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How can I verify the authenticity of a kids gold necklace in India?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Always check for the mandatory Bureau of Indian Standards (BIS) hallmark laser-engraved on the chain tag or pendant bail. It must include the triangular BIS logo, the gold fineness mark (such as 18K750 or 14K585), and a 6-digit alphanumeric Hallmark Unique Identification (HUID) code. You can verify this 6-digit HUID code instantly using the official BIS Care mobile app to view the hallmarking centre, jeweller details, and verified purity."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How should I clean and store my child gold necklace at home?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Clean your child gold necklace by soaking it in lukewarm water mixed with a few drops of mild, pH-neutral baby shampoo for 10 minutes. Gently brush around links and charm crevices using an ultra-soft baby toothbrush, rinse thoroughly under clean lukewarm water, and pat completely dry with a soft microfiber cloth. Store the necklace flat with its clasp fastened inside a separate soft velvet pouch to prevent scratches and knots."
                    }
                }
            ]
        },
        {
            "@type": "BlogPosting",
            "@id": f"https://blog.bluestone.com/{slug}/#article",
            "headline": draft['title'],
            "description": draft['meta_desc'],
            "datePublished": "2026-09-27T14:40:00+05:30",
            "dateModified": "2026-09-27T14:40:00+05:30",
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": f"https://blog.bluestone.com/{slug}/"
            },
            "author": {
                "@type": "Person",
                "name": "Satyam",
                "url": "https://blog.bluestone.com/author/satyam/"
            },
            "publisher": {
                "@type": "Organization",
                "name": "BlueStone",
                "url": "https://www.bluestone.com",
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://www.bluestone.com/skin/frontend/default/bluestone/images/logo.png"
                }
            },
            "keywords": "kids necklace, gold necklace for kid girl, kids gold necklace, baby necklace, child safety necklace",
            "image": [
                carousel_items[0]['src']
            ]
        }
    ]
}

schema_block = f"""<!-- wp:html -->
<script type="application/ld+json">
{json.dumps(schema_json, indent=2, ensure_ascii=False)}
</script>
<!-- /wp:html -->"""

content = content + "\n\n" + schema_block

# Create WordPress post
post_payload = {
    'title': draft['title'],
    'slug': slug,
    'status': 'publish',
    'author': draft['author_id'],
    'categories': draft['categories'],
    'excerpt': draft['meta_desc'],
    'content': content,
    'featured_media': carousel_items[0]['media_id'],
    'meta': {
        '_yoast_wpseo_focuskw': draft['primary_kw'],
        '_yoast_wpseo_title': f"{draft['meta_title']} | BlueStone",
        '_yoast_wpseo_metadesc': draft['meta_desc']
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
    print(f"SUCCESS: Post created with ID {post_id} at {post_url}")
    with open(ROOT / 'output/week9_rank81_published_post.json', 'w') as out_f:
        json.dump(post_res, out_f, indent=2)
