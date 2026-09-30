#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix and verify 3D Coverflow Carousel with dedicated gold pendant designs for Week 8 Rank 188 (Post ID: 39196)."""

import os, base64, json, urllib.request, re
from pathlib import Path

env_paths = [
    Path('.env'),
    Path('/Users/satyamkumar/Downloads/seo final 2026/.env'),
    Path('/Users/satyamkumar/Downloads/final seo generation context/.env'),
]
for ep in env_paths:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

USER = os.environ.get('WP_USER', 'blogbluestone')
PWD = os.environ.get('WP_APP_PASSWORD') or os.environ.get('WP_APP_PASS') or os.environ.get('WP_PASSWORD', '')
token = base64.b64encode(f'{USER}:{PWD}'.encode()).decode()
headers = {
    'Authorization': f'Basic {token}',
    'User-Agent': 'BluestoneSEO/1.0',
    'Content-Type': 'application/json',
}

post_id = 39196
url = f'https://blog.bluestone.com/wp-json/wp/v2/posts/{post_id}?context=edit'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=30) as resp:
    post = json.loads(resp.read().decode())
    raw = post.get('content', {}).get('raw', '')

print('Original raw content length:', len(raw))

# Target carousel block
pattern = re.compile(r'<!-- wp:html -->\s*<style>\s*\.bs-cf.*?<!-- /wp:html -->', re.DOTALL)
match = pattern.search(raw)
if not match:
    pattern = re.compile(r'<style>\s*\.bs-cf.*?</script>', re.DOTALL)
    match = pattern.search(raw)

if not match:
    print('ERROR: Could not find carousel block!')
    exit(1)

print(f'Matched carousel span: {match.start()} to {match.end()}')

NEW_CAROUSEL = """<!-- wp:html -->
<style>
.bs-cf{max-width:900px;margin:1.75rem auto 1.25rem;position:relative;perspective:1200px}
.bs-cf-stage{position:relative;height:360px;margin:0 auto;overflow:visible}
.bs-cf-card{position:absolute;top:0;left:50%;width:min(420px,78vw);transform-origin:center center;transition:transform .65s cubic-bezier(.22,.61,.36,1),opacity .65s ease,filter .65s ease;border-radius:16px;background:#fff;box-shadow:0 12px 30px rgba(0,0,0,.12);overflow:hidden;border:1px solid #ececec}
.bs-cf-media{display:block;line-height:0;background:#f4f4f4}
.bs-cf-media img{display:block;width:100%;aspect-ratio:16/9;height:auto;object-fit:cover;object-position:center}
.bs-cf-meta{padding:14px 16px 16px;text-align:center;background:#fff}
.bs-cf-name{margin:0 0 10px;font-size:1rem;font-weight:600;color:#1a1a1a;text-decoration:none;line-height:1.35;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bs-cf-cta{display:inline-block;padding:8px 18px;border-radius:2px;background:#111;color:#fff!important;font-size:.875rem;font-weight:600;text-decoration:none!important;letter-spacing:.02em}
.bs-cf-cta:hover{background:#333;color:#fff!important}
.bs-cf-card.is-pos-0{z-index:5;opacity:1;filter:none;transform:translate3d(-50%,8px,0) scale(1.02)}
.bs-cf-card.is-pos-1{z-index:3;opacity:.95;filter:brightness(.97);transform:translate3d(calc(-50% + 210px),34px,-110px) rotateY(-26deg) scale(.78)}
.bs-cf-card.is-pos-2{z-index:3;opacity:.95;filter:brightness(.97);transform:translate3d(calc(-50% - 210px),34px,-110px) rotateY(26deg) scale(.78)}
.bs-cf-card.is-pos-3,.bs-cf-card.is-pos--3{z-index:1;opacity:.3;pointer-events:none;transform:translate3d(calc(-50% + 340px),54px,-200px) rotateY(-36deg) scale(.58)}
.bs-cf-card.is-pos--1{z-index:1;opacity:.3;pointer-events:none;transform:translate3d(calc(-50% - 340px),54px,-200px) rotateY(36deg) scale(.58)}
.bs-cf-dots{display:flex;justify-content:center;gap:8px;margin-top:14px}
.bs-cf-dot{width:8px;height:8px;border-radius:50%;border:0;padding:0;background:#c8c8c8;cursor:pointer}
.bs-cf-dot.is-active{background:#111;transform:scale(1.2)}
.bs-cf-nav{position:absolute;top:38%;z-index:8;width:38px;height:38px;border:0;border-radius:50%;background:rgba(255,255,255,.96);box-shadow:0 2px 8px rgba(0,0,0,.14);cursor:pointer;font-size:20px;color:#222;transform:translateY(-50%)}
.bs-cf-prev{left:0}.bs-cf-next{right:0}
@media (max-width:700px){
  .bs-cf-stage{height:300px}
  .bs-cf-card{width:min(300px,84vw)}
  .bs-cf-card.is-pos-1{transform:translate3d(calc(-50% + 130px),36px,-80px) rotateY(-24deg) scale(.72)}
  .bs-cf-card.is-pos-2{transform:translate3d(calc(-50% - 130px),36px,-80px) rotateY(24deg) scale(.72)}
  .bs-cf-card.is-pos-3,.bs-cf-card.is-pos--3,.bs-cf-card.is-pos--1{opacity:0}
}
@media (prefers-reduced-motion:reduce){.bs-cf-card{transition:none}}
</style>
<div class="bs-cf" id="bs-cf-om-pendant-gold" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone Gold Om Pendant Designs">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
    <div class="bs-cf-card is-pos-0" data-index="0">
      <a class="bs-cf-media" href="https://www.bluestone.com/pendants/the-aagarna-pendant~54965.html">
        <img src="https://blog.bluestone.com/wp-content/uploads/2026/09/the-aagarna-pendant-carousel-13.webp" alt="Om Pendant Gold 2026: The Aagarna Pendant from BlueStone" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">The Aagarna Pendant</div>
        <a class="bs-cf-cta" href="https://www.bluestone.com/pendants/the-aagarna-pendant~54965.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-1" data-index="1">
      <a class="bs-cf-media" href="https://www.bluestone.com/pendants/the-thaloria-pendant~165041.html">
        <img src="https://blog.bluestone.com/wp-content/uploads/2026/09/the-thaloria-pendant-carousel-15.webp" alt="Om Pendant Gold 2026: The Thaloria Pendant from BlueStone" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">The Thaloria Pendant</div>
        <a class="bs-cf-cta" href="https://www.bluestone.com/pendants/the-thaloria-pendant~165041.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-2" data-index="2">
      <a class="bs-cf-media" href="https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html">
        <img src="https://blog.bluestone.com/wp-content/uploads/2026/09/the-sarvanya-pendant-carousel-15.webp" alt="Om Pendant Gold 2026: The Sarvanya Pendant from BlueStone" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">The Sarvanya Pendant</div>
        <a class="bs-cf-cta" href="https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-3" data-index="3">
      <a class="bs-cf-media" href="https://www.bluestone.com/pendants/the-valeria-rose-pendant~181266.html">
        <img src="https://blog.bluestone.com/wp-content/uploads/2026/09/the-valeria-rose-pendant-carousel-7.webp" alt="Om Pendant Gold 2026: The Valeria Rose Pendant from BlueStone" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">The Valeria Rose Pendant</div>
        <a class="bs-cf-cta" href="https://www.bluestone.com/pendants/the-valeria-rose-pendant~181266.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos--2" data-index="4">
      <a class="bs-cf-media" href="https://www.bluestone.com/pendants/the-thyvarne-pendant~173761.html">
        <img src="https://blog.bluestone.com/wp-content/uploads/2026/09/the-thyvarne-pendant-carousel-6.webp" alt="Om Pendant Gold 2026: The Thyvarne Pendant from BlueStone" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">The Thyvarne Pendant</div>
        <a class="bs-cf-cta" href="https://www.bluestone.com/pendants/the-thyvarne-pendant~173761.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos--1" data-index="5">
      <a class="bs-cf-media" href="https://www.bluestone.com/pendants/the-xarvithis-pendant~156920.html">
        <img src="https://blog.bluestone.com/wp-content/uploads/2026/08/the-xarvithis-pendant-carousel-12.webp" alt="Om Pendant Gold 2026: The Xarvithis Pendant from BlueStone" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">The Xarvithis Pendant</div>
        <a class="bs-cf-cta" href="https://www.bluestone.com/pendants/the-xarvithis-pendant~156920.html">Buy now</a>
      </div>
    </div>
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
(function(){
  var root=document.getElementById('bs-cf-om-pendant-gold');
  if(!root||root.dataset.ready)return;
  root.dataset.ready='1';
  var cards=[].slice.call(root.querySelectorAll('.bs-cf-card'));
  var dots=[].slice.call(root.querySelectorAll('.bs-cf-dot'));
  var n=cards.length, active=0, timer=null;
  var ms=parseInt(root.getAttribute('data-interval'),10)||3200;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function rel(i){ var d=((i-active)%n+n)%n; if(d>n/2)d=d-n; return d; }
  function paint(){
    cards.forEach(function(c,i){
      c.className='bs-cf-card';
      var d=rel(i), cls='is-pos-'+d;
      if(d===-1)cls='is-pos-2'; if(d===1)cls='is-pos-1'; if(d===0)cls='is-pos-0';
      if(d===-2||d===2)cls=d===2?'is-pos-3':'is-pos--1';
      c.classList.add(cls);
    });
    dots.forEach(function(d,i){d.classList.toggle('is-active',i===active)});
  }
  function go(to){active=((to%n)+n)%n;paint()}
  function next(){go(active+1)}
  function prev(){go(active-1)}
  function stop(){if(timer){clearInterval(timer);timer=null}}
  function start(){if(reduce)return;stop();timer=setInterval(next,ms)}
  root.querySelector('.bs-cf-next').addEventListener('click',function(){next();start()});
  root.querySelector('.bs-cf-prev').addEventListener('click',function(){prev();start()});
  dots.forEach(function(d){d.addEventListener('click',function(){go(+d.getAttribute('data-i'));start()})});
  root.addEventListener('mouseenter',stop);
  root.addEventListener('mouseleave',start);
  paint(); start();
})();
</script>
<!-- /wp:html -->"""

# Also update the curated highlights list right below the carousel
curated_highlights = """<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li><a href="https://www.bluestone.com/pendants/the-aagarna-pendant~54965.html">The Aagarna Pendant</a> &ndash; An elegant solid gold pendant featuring sacred openwork geometry.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://www.bluestone.com/pendants/the-thaloria-pendant~165041.html">The Thaloria Pendant</a> &ndash; A refined contemporary gold pendant crafted in hallmarked 18K gold.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html">The Sarvanya Pendant</a> &ndash; A timeless sacred gold medallion with fine craftsmanship.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://www.bluestone.com/pendants/the-valeria-rose-pendant~181266.html">The Valeria Rose Pendant</a> &ndash; A warm rose gold devotional pendant with intricate filigree details.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://www.bluestone.com/pendants/the-thyvarne-pendant~173761.html">The Thyvarne Pendant</a> &ndash; A classic fine jewellery gold pendant designed for daily wear and spiritual grace.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://www.bluestone.com/pendants/the-xarvithis-pendant~156920.html">The Xarvithis Pendant</a> &ndash; A modern geometric gold pendant with balanced proportions.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->"""

# Find the curated highlights block in raw content
hl_pattern = re.compile(r'<!-- wp:paragraph -->\s*<p><strong>Curated Design Highlights:</strong></p>\s*<!-- /wp:paragraph -->\s*<!-- wp:list -->.*?<!-- /wp:list -->', re.DOTALL)
hl_match = hl_pattern.search(raw)

if hl_match:
    updated_raw = raw[:match.start()] + NEW_CAROUSEL + raw[match.end():hl_match.start()] + curated_highlights + raw[hl_match.end():]
else:
    updated_raw = raw[:match.start()] + NEW_CAROUSEL + raw[match.end():]

print('Updated raw content length:', len(updated_raw))

# Send update to WordPress
update_url = f'https://blog.bluestone.com/wp-json/wp/v2/posts/{post_id}'
payload = json.dumps({'content': updated_raw}).encode('utf-8')
update_req = urllib.request.Request(update_url, data=payload, headers=headers, method='POST')

with urllib.request.urlopen(update_req, timeout=30) as resp:
    res = json.loads(resp.read().decode())
    print('WordPress Post 39196 updated successfully! HTTP status:', resp.status)
