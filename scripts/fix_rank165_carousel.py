#!/usr/bin/env python3
"""Fix and upgrade 3D Coverflow Carousel for Rank 165 post:
- Post 38938 (Week 8 Rank 165: Black Bead Bracelet Buying Guide 2026)
Matches the exact dimensions, stage height (360px), card width (min(420px, 78vw)),
initial position classes (zero layout shift), and smooth 3D coverflow of mens-black-bracelet-2026.
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

POST_ID = 38938
CAROUSEL_ID = "bs-cf-black-bead-bracelet-2026"
LABEL = "Curated BlueStone fine gold black bead bracelets and link bracelets"

ITEMS = [
    {
        "name": "The Elize Evil Eye Bracelet",
        "url": "https://www.bluestone.com/bracelets/the-elize-evil-eye-bracelet~121012.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-elize-evil-eye-bracelet-black-bead-bracelet-carousel.webp",
        "alt": "Black bead bracelet 2026 buying guide: The Elize Evil Eye Bracelet in 18k yellow gold from BlueStone",
        "initial_class": "is-pos-0",
        "index": 0
    },
    {
        "name": "The Malocchio Charm Holder Bracelet",
        "url": "https://www.bluestone.com/bracelets/the-malocchio-charm-holder-bracelet~95653.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-malocchio-charm-holder-bracelet-black-bead-bracelet-carousel.webp",
        "alt": "Black bead bracelet 2026 buying guide: The Malocchio Charm Holder Bracelet in 18k yellow gold from BlueStone",
        "initial_class": "is-pos-1",
        "index": 1
    },
    {
        "name": "The Pervinca Charm Holder Bracelet",
        "url": "https://www.bluestone.com/bracelets/the-pervinca-charm-holder-bracelet~103133.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-pervinca-charm-holder-bracelet-black-bead-bracelet-carousel.webp",
        "alt": "Black bead bracelet 2026 buying guide: The Pervinca Charm Holder Bracelet in 18k yellow gold from BlueStone",
        "initial_class": "is-pos-3",
        "index": 2
    },
    {
        "name": "The Kricia Charm Bracelet",
        "url": "https://www.bluestone.com/bracelets/the-kricia-charm-bracelet~75605.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-kricia-charm-bracelet-black-bead-bracelet-carousel.webp",
        "alt": "Black bead bracelet 2026 buying guide: The Kricia Charm Bracelet in 18k yellow gold from BlueStone",
        "initial_class": "is-pos-3",
        "index": 3
    },
    {
        "name": "The Shining Star Bracelet",
        "url": "https://www.bluestone.com/bracelets/the-shining-star-bracelet~63731.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-shining-star-bracelet-black-bead-bracelet-carousel.webp",
        "alt": "Black bead bracelet 2026 buying guide: The Shining Star Bracelet in 18k yellow gold from BlueStone",
        "initial_class": "is-pos--1",
        "index": 4
    },
    {
        "name": "The Tapia Chain Bracelet",
        "url": "https://www.bluestone.com/bracelets/the-tapia-chain-bracelet~115379.html",
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-tapia-chain-bracelet-black-bead-bracelet-carousel.webp",
        "alt": "Black bead bracelet 2026 buying guide: The Tapia Chain Bracelet in 18k yellow gold from BlueStone",
        "initial_class": "is-pos-2",
        "index": 5
    }
]

def build_carousel_html():
    cards_html = []
    for item in ITEMS:
        cards_html.append(f"""    <div class="bs-cf-card {item['initial_class']}" data-index="{item['index']}">
      <a class="bs-cf-media" href="{item['url']}">
        <img src="{item['src']}" alt="{item['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{item['name']}</div>
        <a class="bs-cf-cta" href="{item['url']}">Buy now</a>
      </div>
    </div>""")
    
    dots_html = []
    for i in range(len(ITEMS)):
        active_cls = " is-active" if i == 0 else ""
        dots_html.append(f'    <button type="button" class="bs-cf-dot{active_cls}" data-i="{i}" aria-label="Product {i+1}"></button>')
    
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
<div class="bs-cf" id="{CAROUSEL_ID}" data-interval="3200" aria-roledescription="carousel" aria-label="{LABEL}">
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
  var root=document.getElementById('{CAROUSEL_ID}');
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
    print(f"Fetching post {POST_ID}...")
    req = urllib.request.Request(f"{WP_API}/posts/{POST_ID}?context=edit", headers=AUTH_HEADERS)
    with urllib.request.urlopen(req) as resp:
        post = json.loads(resp.read().decode())
    
    content = post["content"]["raw"]
    new_carousel = build_carousel_html()
    
    # Replace existing carousel block
    # Check for <!-- wp:html -->.*?(bs-cf-black-bead-bracelet-2026).*?<!-- /wp:html -->
    # or fallback to regex matching <style>.*?</script> with bs-cf
    pattern = r"<!-- wp:html -->\s*<style>.*?\.bs-cf.*?<\/script>\s*<!-- \/wp:html -->"
    if re.search(pattern, content, re.S):
        updated_content = re.sub(pattern, new_carousel, content, count=1, flags=re.S)
        print("Replaced <!-- wp:html --> block successfully.")
    else:
        alt_pattern = r"<style>.*?\.bs-cf.*?<\/script>"
        if re.search(alt_pattern, content, re.S):
            updated_content = re.sub(alt_pattern, new_carousel, content, count=1, flags=re.S)
            print("Replaced bare <style>...</script> block successfully.")
        else:
            print("Could not find carousel pattern in content!")
            return
    
    # Update post
    payload = json.dumps({"content": updated_content}).encode("utf-8")
    update_req = urllib.request.Request(
        f"{WP_API}/posts/{POST_ID}",
        data=payload,
        headers=AUTH_HEADERS,
        method="POST"
    )
    with urllib.request.urlopen(update_req) as resp:
        res = json.loads(resp.read().decode())
        print(f"Successfully updated post {POST_ID} ({res['slug']})!")

if __name__ == "__main__":
    main()
