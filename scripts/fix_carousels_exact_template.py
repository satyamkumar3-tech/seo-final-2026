#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix carousels on Rank 8, Rank 9, and Rank 10 to match the exact working canonical 3D Coverflow template from Rank 5 (ear-piercing-jewelry-2026)."""

import urllib.request, json, base64, re, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
env_paths = [ROOT / '.env', Path('/Users/satyamkumar/Downloads/seo final 2026/.env')]
for ep in env_paths:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

WP_USER = os.environ.get('WP_USER', 'blogbluestone')
WP_PASS = os.environ.get('WP_APP_PASSWORD') or os.environ.get('WP_APP_PASS') or os.environ.get('WP_PASSWORD', '')
WP_URL = os.environ.get('WP_URL', 'https://blog.bluestone.com')
TOKEN = base64.b64encode(f"{WP_USER}:{WP_PASS}".encode()).decode()
HEADERS = {"Authorization": f"Basic {TOKEN}", "Content-Type": "application/json"}

def render_canonical_carousel(slug, aria_label, products):
    cards_html = ""
    initial_classes = ["is-pos-0", "is-pos-1", "is-pos-2", "is-pos-3", "is-pos--2", "is-pos--1"]
    for i, p in enumerate(products):
        cls = initial_classes[i] if i < len(initial_classes) else "is-pos-3"
        cards_html += f"""    <div class="bs-cf-card {cls}" data-index="{i}">
      <a class="bs-cf-media" href="{p['url']}">
        <img src="{p['img_url']}" alt="{p['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{p['name']}</div>
        <a class="bs-cf-cta" href="{p['url']}">Buy now</a>
      </div>
    </div>\n"""

    dots_html = ""
    for i in range(len(products)):
        active_cls = " is-active" if i == 0 else ""
        dots_html += f"""    <button type="button" class="bs-cf-dot{active_cls}" data-i="{i}" aria-label="Product {i+1}"></button>\n"""

    snippet = f"""<!-- wp:html -->
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
<div class="bs-cf" id="bs-cf-{slug}" data-interval="3200" aria-roledescription="carousel" aria-label="{aria_label}">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
{cards_html}  </div>
  <div class="bs-cf-dots" role="tablist">
{dots_html}  </div>
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
    return snippet

def fix_post(pid, slug, aria_label, products, highlights_p):
    print(f"\nProcessing Post ID {pid} ({slug})...")
    req = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/posts/{pid}?context=edit", headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        post = json.loads(resp.read().decode('utf-8'))
        raw = post['content']['raw']

    # 1. Clean out all previous carousels and highlight paragraphs
    raw = re.sub(r'<!-- wp:html -->\s*<style>[\s\S]*?<!-- /wp:html -->', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<style>[\s\S]*?\.bs-cf[\s\S]*?</style>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<div class=[\"\']bs-cf[\"\'][\s\S]*?</div>\s*<script>[\s\S]*?</script>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<script>[\s\S]*?bs-cf[\s\S]*?</script>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<div class=[\"\']bs-cf[\"\'][\s\S]*?</div>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<!-- wp:paragraph -->\s*<p[^>]*>\s*<strong>Curated Design Highlights:</strong>[\s\S]*?<!-- /wp:paragraph -->', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<p[^>]*>\s*<strong>Curated Design Highlights:</strong>[\s\S]*?</p>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'\n{3,}', '\n\n', raw).strip()

    carousel_block = render_canonical_carousel(slug, aria_label, products)
    full_carousel_section = carousel_block + "\n\n" + highlights_p

    # 2. Insert carousel after the first H2 section
    h2_positions = []
    for m in re.finditer(r'(<!-- wp:heading {"level":2} -->|<h2[^>]*>)', raw, flags=re.IGNORECASE):
        h2_positions.append(m.start())
        
    if len(h2_positions) >= 2:
        idx = h2_positions[1]
        final_content = raw[:idx] + full_carousel_section + "\n\n" + raw[idx:]
    else:
        final_content = full_carousel_section + "\n\n" + raw

    # 3. Patch Post
    patch_payload = {
        "content": final_content
    }
    patch_req = urllib.request.Request(
        f"{WP_URL}/wp-json/wp/v2/posts/{pid}",
        data=json.dumps(patch_payload).encode('utf-8'),
        headers=HEADERS,
        method="POST"
    )
    with urllib.request.urlopen(patch_req, timeout=45) as resp:
        print(f"Successfully updated carousel in Post {pid} ({slug})!")

if __name__ == "__main__":
    # 1. RANK 8 (Post 39414)
    r8_products = [
        {"name": "The Estrella Oval Bangle", "url": "https://www.bluestone.com/bangles/the-estrella-oval-bangle~34771.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-estrella-oval-bangle-carousel-2026-1.webp", "alt": "Casual daily wear gold bangle 2026: The Estrella Oval Bangle from BlueStone"},
        {"name": "The Channing Bangle", "url": "https://www.bluestone.com/bangles/the-channing-bangle~975.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-channing-bangle-carousel-2026-1.webp", "alt": "Casual daily wear gold bangle 2026: The Channing Bangle from BlueStone"},
        {"name": "The Muricelle Bangle", "url": "https://www.bluestone.com/bangles/the-muricelle-bangle~1001.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-muricelle-bangle-carousel-2026-1.webp", "alt": "Casual daily wear gold bangle 2026: The Muricelle Bangle from BlueStone"},
        {"name": "The Skein Bangle", "url": "https://www.bluestone.com/bangles/the-skein-bangle~27491.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-skein-bangle-carousel-2026-1.webp", "alt": "Casual daily wear gold bangle 2026: The Skein Bangle from BlueStone"},
        {"name": "The Pear Evil Eye Toggle Bangle", "url": "https://www.bluestone.com/bangles/the-pear-evil-eye-toggle-bangle~87037.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-pear-evil-eye-toggle-bangle-carousel-2026-1.webp", "alt": "Casual daily wear gold bangle 2026: The Pear Evil Eye Toggle Bangle from BlueStone"},
        {"name": "The Tarentella Oval Bangle", "url": "https://www.bluestone.com/bangles/the-tarentella-oval-bangle~31547.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-tarentella-oval-bangle-carousel-2026-1.webp", "alt": "Casual daily wear gold bangle 2026: The Tarentella Oval Bangle from BlueStone"}
    ]
    r8_highlights = """<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong> Explore signature everyday gold bangle designs crafted for fine elegance and daily comfort: <a href="https://www.bluestone.com/bangles/the-estrella-oval-bangle~34771.html">The Estrella Oval Bangle</a> with understated brilliance, <a href="https://www.bluestone.com/bangles/the-channing-bangle~975.html">The Channing Bangle</a> for modern minimalism, <a href="https://www.bluestone.com/bangles/the-muricelle-bangle~1001.html">The Muricelle Bangle</a> featuring high-polish contouring, <a href="https://www.bluestone.com/bangles/the-skein-bangle~27491.html">The Skein Bangle</a> engineered with seamless comfort curves, <a href="https://www.bluestone.com/bangles/the-pear-evil-eye-toggle-bangle~87037.html">The Pear Evil Eye Toggle Bangle</a> for delicate talismanic charm, and <a href="https://www.bluestone.com/bangles/the-tarentella-oval-bangle~31547.html">The Tarentella Oval Bangle</a> for timeless wrist styling.</p>
<!-- /wp:paragraph -->"""
    fix_post(39414, "casual-daily-wear-gold-bangle-2026", "BlueStone Daily Wear Gold Bangle Collection", r8_products, r8_highlights)

    # 2. RANK 9 (Post 39421)
    r9_products = [
        {"name": "The Aleena Huggie Earrings", "url": "https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-aleena-huggie-earrings-carousel-2026-3.webp", "alt": "Daily wear earrings 2026: The Aleena Huggie Earrings from BlueStone"},
        {"name": "The Vicky Hoop Earrings", "url": "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-vicky-hoop-earrings-carousel-2026-2.webp", "alt": "Daily wear earrings 2026: The Vicky Hoop Earrings from BlueStone"},
        {"name": "The Ursa Hoop Earrings", "url": "https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-ursa-hoop-earrings-carousel-2026-2.webp", "alt": "Daily wear earrings 2026: The Ursa Hoop Earrings from BlueStone"},
        {"name": "The Rohal Huggie Earrings", "url": "https://www.bluestone.com/earrings/the-rohal-huggie-earrings~21864.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-rohal-huggie-earrings-carousel-2026-2.webp", "alt": "Daily wear earrings 2026: The Rohal Huggie Earrings from BlueStone"},
        {"name": "The Asya Huggie Earrings", "url": "https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-asya-huggie-earrings-carousel-2026-2.webp", "alt": "Daily wear earrings 2026: The Asya Huggie Earrings from BlueStone"},
        {"name": "The Skein Hoop Earrings", "url": "https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-skein-hoop-earrings-carousel-2026-3.webp", "alt": "Daily wear earrings 2026: The Skein Hoop Earrings from BlueStone"}
    ]
    r9_highlights = """<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong> Explore signature everyday earring designs engineered for 24/7 comfort: <a href="https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html">The Aleena Huggie Earrings</a> with snag-free huggie ergonomics, <a href="https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html">The Vicky Hoop Earrings</a> offering featherlight hoop silhouettes, <a href="https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html">The Ursa Hoop Earrings</a> with contemporary rounded contours, <a href="https://www.bluestone.com/earrings/the-rohal-huggie-earrings~21864.html">The Rohal Huggie Earrings</a> featuring secure latch-backs, <a href="https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html">The Asya Huggie Earrings</a> crafted with diamond-accented grace, and <a href="https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html">The Skein Hoop Earrings</a> for textured modern minimalism.</p>
<!-- /wp:paragraph -->"""
    fix_post(39421, "daily-wear-earrings-2026", "BlueStone Daily Wear Earrings Collection", r9_products, r9_highlights)

    # 3. RANK 10 (Post 39440)
    r10_products = [
        {"name": "The Thaloria Pendant", "url": "https://www.bluestone.com/pendants/the-thaloria-pendant~165041.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-thaloria-pendant-carousel-2026-2.webp", "alt": "White stone necklace 2026: The Thaloria Pendant from BlueStone"},
        {"name": "The Lumeelle Cluster Pendant", "url": "https://www.bluestone.com/pendants/the-lumeelle-cluster-pendant~162509.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-lumeelle-cluster-pendant-carousel-2026-4.webp", "alt": "White stone necklace 2026: The Lumeelle Cluster Pendant from BlueStone"},
        {"name": "The Thyvarne Pendant", "url": "https://www.bluestone.com/pendants/the-thyvarne-pendant~173761.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-thyvarne-pendant-carousel-2026.webp", "alt": "White stone necklace 2026: The Thyvarne Pendant from BlueStone"},
        {"name": "The Aagarna Pendant", "url": "https://www.bluestone.com/pendants/the-aagarna-pendant~54965.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-aagarna-pendant-carousel-2026.webp", "alt": "White stone necklace 2026: The Aagarna Pendant from BlueStone"},
        {"name": "The Sarvanya Pendant", "url": "https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-sarvanya-pendant-carousel-2026-3.webp", "alt": "White stone necklace 2026: The Sarvanya Pendant from BlueStone"},
        {"name": "The Teshvarya Pendant", "url": "https://www.bluestone.com/pendants/the-teshvarya-pendant~173771.html", "img_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-teshvarya-pendant-carousel-2026-1.webp", "alt": "White stone necklace 2026: The Teshvarya Pendant from BlueStone"}
    ]
    r10_highlights = """<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong> Discover handcrafted white stone neckwear silhouettes engineered for radiant light refraction: <a href="https://www.bluestone.com/pendants/the-thaloria-pendant~165041.html">The Thaloria Pendant</a> set in 18k solid gold, <a href="https://www.bluestone.com/pendants/the-lumeelle-cluster-pendant~162509.html">The Lumeelle Cluster Pendant</a> featuring high-clarity cluster geometry, <a href="https://www.bluestone.com/pendants/the-thyvarne-pendant~173761.html">The Thyvarne Pendant</a> with contemporary bezel settings, <a href="https://www.bluestone.com/pendants/the-aagarna-pendant~54965.html">The Aagarna Pendant</a> for delicate floral motifs, <a href="https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html">The Sarvanya Pendant</a> with symmetrical drop elegance, and <a href="https://www.bluestone.com/pendants/the-teshvarya-pendant~173771.html">The Teshvarya Pendant</a> for statement evening sparkle.</p>
<!-- /wp:paragraph -->"""
    fix_post(39440, "white-stone-necklace-2026", "BlueStone White Stone Necklace & Pendant Collection", r10_products, r10_highlights)

    print("\nALL CAROUSELS ON POSTS 8, 9, 10 PERFECTLY STANDARDIZED!")
