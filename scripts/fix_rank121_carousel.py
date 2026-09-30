#!/usr/bin/env python3
"""Fix and upgrade 3D Coverflow Carousel for WordPress post 38426 (Week 8 Rank 121: Men's Cross Pendant Buying Guide 2026)
to exactly match the dimensions, stage height (360px), card width (min(420px, 78vw)), initial position classes,
and smooth 3D coverflow animations of post 37432 (mens-black-bracelet-2026).
"""
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

POST_ID = 38426
CAROUSEL_ID = "bs-cf-mens-cross-pendant-2026"
CAROUSEL_LABEL = "Curated Men's Fine Jewellery Highlights"

ITEMS = [
    {
        "name": "The Serenity Evil Eye Pendant For Him",
        "url": "https://www.bluestone.com/pendants/the-serenity-evil-eye-pendant-for-him~115382.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-serenity-evil-eye-pendant-for-him-carousel-5.webp",
        "alt": "mens cross pendant 2026 gift idea: The Serenity Evil Eye Pendant For Him"
    },
    {
        "name": "The Talisman Evil Eye Pendant For Him",
        "url": "https://www.bluestone.com/pendants/the-talisman-evil-eye-pendant-for-him~115385.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-talisman-evil-eye-pendant-for-him-carousel-6.webp",
        "alt": "mens cross pendant 2026 gift idea: The Talisman Evil Eye Pendant For Him"
    },
    {
        "name": "The Chevalier Gold Chain",
        "url": "https://www.bluestone.com/chains/the-chevalier-gold-chain~124914.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-chevalier-gold-chain-carousel-14.webp",
        "alt": "mens cross pendant 2026 gift idea: The Chevalier Gold Chain"
    },
    {
        "name": "The Tetyana Gold Chain",
        "url": "https://www.bluestone.com/chains/the-tetyana-gold-chain~124927.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-tetyana-gold-chain-carousel-15.webp",
        "alt": "mens cross pendant 2026 gift idea: The Tetyana Gold Chain"
    },
    {
        "name": "The Jasper Band For Him",
        "url": "https://www.bluestone.com/rings/the-jasper-band-for-him~93964.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-jasper-band-for-him-carousel-15.webp",
        "alt": "mens cross pendant 2026 gift idea: The Jasper Band For Him"
    },
    {
        "name": "The Interlink Band Ring",
        "url": "https://www.bluestone.com/rings/the-interlink-band-ring~108785.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-interlink-band-ring-carousel-12.webp",
        "alt": "mens cross pendant 2026 gift idea: The Interlink Band Ring"
    }
]

def verify_images():
    print(f"Verifying images via HTTP HEAD...")
    for item in ITEMS:
        url = item["src"]
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
        with urllib.request.urlopen(req, timeout=10) as res:
            if res.status != 200:
                raise RuntimeError(f"Image {url} failed with HTTP status {res.status}")
            print(f"  [200 OK] {item['name']} -> {url}")

def build_perfect_carousel(carousel_id: str, label: str, items: list) -> str:
    cards = []
    dots = []
    
    for i, item in enumerate(items):
        name = item["name"]
        url = item["url"]
        src = item["src"]
        alt = item["alt"]
        
        # Initial position classes for zero layout shift
        if i == 0:
            pos_cls = "is-pos-0"
        elif i == 1:
            pos_cls = "is-pos-1"
        elif i == 2:
            pos_cls = "is-pos-2"
        elif i == 3:
            pos_cls = "is-pos-3"
        elif i == 4:
            pos_cls = "is-pos--2"
        else:
            pos_cls = "is-pos--1"
            
        cards.append(f"""    <div class="bs-cf-card {pos_cls}" data-index="{i}">
      <a class="bs-cf-media" href="{url}">
        <img src="{src}" alt="{alt}" width="960" height="535" loading="lazy" />
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{name}</div>
        <a class="bs-cf-cta" href="{url}">Buy now</a>
      </div>
    </div>""")
        
        active_cls = " is-active" if i == 0 else ""
        dots.append(f'    <button type="button" class="bs-cf-dot{active_cls}" data-i="{i}" aria-label="Product {i+1}"></button>')
        
    cards_html = "\n".join(cards)
    dots_html = "\n".join(dots)
    
    html_block = f"""<!-- wp:html -->
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
    return html_block

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
    print(f"\n--- Upgrading Carousel in Post {POST_ID} to match mens-black-bracelet-2026 ---")
    verify_images()
    
    post = fetch_post(POST_ID)
    raw = post.get("content", {}).get("raw", "")
    print(f"Original content length: {len(raw)}")
    
    new_carousel = build_perfect_carousel(CAROUSEL_ID, CAROUSEL_LABEL, ITEMS)
    
    # Locate existing carousel block
    pattern = r"<!-- wp:html -->\s*<style>[\s\S]*?</script>\s*<!-- /wp:html -->"
    m = re.search(pattern, raw)
    if not m:
        pattern2 = r"<style>[\s\S]*?" + re.escape(CAROUSEL_ID) + r"[\s\S]*?</script>"
        m = re.search(pattern2, raw)
        if not m:
            print("ERROR: Carousel block pattern not found in post 38426!")
            return False
            
    print(f"Matched carousel block from char {m.start()} to {m.end()} (length {len(m.group(0))})")
    new_raw = raw[:m.start()] + new_carousel + raw[m.end():]
    print(f"New content length: {len(new_raw)}")
    
    updated = update_post(POST_ID, new_raw)
    print(f"SUCCESS: Post {POST_ID} updated with reference-matched 3D Coverflow: {updated.get('link')}")
    return True

if __name__ == "__main__":
    main()
