#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ensure each post has:
- Exactly 1 3D Coverflow Carousel
- Exactly 2 In-Body Type 3 Figures (Flatlay + Lifestyle) with PDP links & captions
- Exactly 1 Featured Media (Hero)
Total images = 3 photorealistic visuals + 6-product carousel.
"""

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

def normalize_post(pid, slug, title_kw, hero_id, hero_url, flatlay_id, flatlay_url, flatlay_pdp, flatlay_alt, flatlay_caption, lifestyle_id, lifestyle_url, lifestyle_pdp, lifestyle_alt, lifestyle_caption, carousel_products):
    req = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/posts/{pid}?context=edit", headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        post = json.loads(resp.read().decode('utf-8'))
        raw = post['content']['raw']

    # 1. Clean all existing carousels, styles, scripts, figures
    raw = re.sub(r'<!-- wp:html -->\s*<style>[\s\S]*?<!-- /wp:html -->', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<style>[\s\S]*?\.bs-cf[\s\S]*?</style>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<div class=[\"\']bs-cf[\"\'][\s\S]*?</div>\s*<script>[\s\S]*?</script>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<script>[\s\S]*?bs-cf[\s\S]*?</script>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<div class=[\"\']bs-cf[\"\'][\s\S]*?</div>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<!-- wp:paragraph -->\s*<p[^>]*>\s*<strong>Curated Design Highlights:</strong>[\s\S]*?<!-- /wp:paragraph -->', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<p[^>]*>\s*<strong>Curated Design Highlights:</strong>[\s\S]*?</p>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<!-- wp:image[\s\S]*?<!-- /wp:image -->', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<figure class=[\"\']wp-block-image[\"\'][\s\S]*?</figure>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'\n{3,}', '\n\n', raw).strip()

    # 2. Build 3D Coverflow Carousel
    c = carousel_products
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
<div class="bs-cf" id="bs-cf-{slug}" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone {title_kw} Collection">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
    <div class="bs-cf-card is-pos-0" data-index="0">
      <a class="bs-cf-media" href="{c[0]['url']}">
        <img src="{c[0]['media_url']}" alt="{title_kw} 2026: {c[0]['name']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{c[0]['name']}</div>
        <a class="bs-cf-cta" href="{c[0]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-1" data-index="1">
      <a class="bs-cf-media" href="{c[1]['url']}">
        <img src="{c[1]['media_url']}" alt="{title_kw} 2026: {c[1]['name']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{c[1]['name']}</div>
        <a class="bs-cf-cta" href="{c[1]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-2" data-index="2">
      <a class="bs-cf-media" href="{c[2]['url']}">
        <img src="{c[2]['media_url']}" alt="{title_kw} 2026: {c[2]['name']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{c[2]['name']}</div>
        <a class="bs-cf-cta" href="{c[2]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-3" data-index="3">
      <a class="bs-cf-media" href="{c[3]['url']}">
        <img src="{c[3]['media_url']}" alt="{title_kw} 2026: {c[3]['name']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{c[3]['name']}</div>
        <a class="bs-cf-cta" href="{c[3]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos--2" data-index="4">
      <a class="bs-cf-media" href="{c[4]['url']}">
        <img src="{c[4]['media_url']}" alt="{title_kw} 2026: {c[4]['name']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{c[4]['name']}</div>
        <a class="bs-cf-cta" href="{c[4]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos--1" data-index="5">
      <a class="bs-cf-media" href="{c[5]['url']}">
        <img src="{c[5]['media_url']}" alt="{title_kw} 2026: {c[5]['name']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{c[5]['name']}</div>
        <a class="bs-cf-cta" href="{c[5]['url']}">Buy now</a>
      </div>
    </div>
  </div>
  <div class="bs-cf-dots">
    <button type="button" class="bs-cf-dot is-active" data-dot="0" aria-label="Go to slide 1"></button>
    <button type="button" class="bs-cf-dot" data-dot="1" aria-label="Go to slide 2"></button>
    <button type="button" class="bs-cf-dot" data-dot="2" aria-label="Go to slide 3"></button>
    <button type="button" class="bs-cf-dot" data-dot="3" aria-label="Go to slide 4"></button>
    <button type="button" class="bs-cf-dot" data-dot="4" aria-label="Go to slide 5"></button>
    <button type="button" class="bs-cf-dot" data-dot="5" aria-label="Go to slide 6"></button>
  </div>
</div>
<script>
(function(){{
  var root=document.getElementById("bs-cf-{slug}");
  if(!root)return;
  var cards=Array.prototype.slice.call(root.querySelectorAll(".bs-cf-card"));
  var dots=Array.prototype.slice.call(root.querySelectorAll(".bs-cf-dot"));
  var prevBtn=root.querySelector(".bs-cf-prev");
  var nextBtn=root.querySelector(".bs-cf-next");
  var total=cards.length;
  var current=0;
  var timer=null;
  var interval=parseInt(root.getAttribute("data-interval")||"3200",10);
  var classNames=["is-pos-0","is-pos-1","is-pos-2","is-pos-3","is-pos--2","is-pos--1"];
  function update(){{
    cards.forEach(function(card,i){{
      classNames.forEach(function(cls){{card.classList.remove(cls);}});
      var rel=(i-current+total)%total;
      if(rel===0)card.classList.add("is-pos-0");
      else if(rel===1)card.classList.add("is-pos-1");
      else if(rel===2)card.classList.add("is-pos-2");
      else if(rel===3)card.classList.add("is-pos-3");
      else if(rel===total-2)card.classList.add("is-pos--2");
      else if(rel===total-1)card.classList.add("is-pos--1");
    }});
    dots.forEach(function(dot,i){{
      dot.classList.toggle("is-active",i===current);
    }});
  }}
  function next(){{current=(current+1)%total;update();}}
  function prev(){{current=(current-1+total)%total;update();}}
  function start(){{stop();timer=setInterval(next,interval);}}
  function stop(){{if(timer){{clearInterval(timer);timer=null;}}}}
  if(nextBtn)nextBtn.addEventListener("click",function(){{next();start();}});
  if(prevBtn)prevBtn.addEventListener("click",function(){{prev();start();}});
  dots.forEach(function(dot,i){{
    dot.addEventListener("click",function(){{current=i;update();start();}});
  }});
  root.addEventListener("mouseenter",stop);
  root.addEventListener("mouseleave",start);
  update();
  start();
}})();
</script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong> Explore signature {title_kw.lower()} designs crafted for fine elegance and daily comfort: <a href="{c[0]['url']}">{c[0]['name']}</a> with understated brilliance, <a href="{c[1]['url']}">{c[1]['name']}</a> for modern minimalism, <a href="{c[2]['url']}">{c[2]['name']}</a> featuring high-polish contouring, <a href="{c[3]['url']}">{c[3]['name']}</a> engineered with seamless comfort, <a href="{c[4]['url']}">{c[4]['name']}</a> for delicate charm, and <a href="{c[5]['url']}">{c[5]['name']}</a> for timeless styling.</p>
<!-- /wp:paragraph -->"""

    # 3. Build In-Body Gutenberg Image Blocks
    flatlay_block = f"""<!-- wp:image {{"id":{flatlay_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{flatlay_pdp}"><img src="{flatlay_url}" alt="{flatlay_alt}" class="wp-image-{flatlay_id}"/></a><figcaption>{flatlay_caption}</figcaption></figure>
<!-- /wp:image -->"""

    lifestyle_block = f"""<!-- wp:image {{"id":{lifestyle_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{lifestyle_pdp}"><img src="{lifestyle_url}" alt="{lifestyle_alt}" class="wp-image-{lifestyle_id}"/></a><figcaption>{lifestyle_caption}</figcaption></figure>
<!-- /wp:image -->"""

    # 4. Split by H2 headers (either <!-- wp:heading {"level":2} --> or <h2)
    h2_positions = []
    for m in re.finditer(r'(<!-- wp:heading {"level":2} -->|<h2[^>]*>)', raw, flags=re.IGNORECASE):
        h2_positions.append(m.start())
        
    print(f"Post {pid}: Found {len(h2_positions)} H2 positions.")
    
    if len(h2_positions) >= 5:
        p1 = raw[:h2_positions[1]] + "\n\n" + carousel_html + "\n\n"
        p2 = raw[h2_positions[1]:h2_positions[2]] + "\n\n" + flatlay_block + "\n\n"
        p3 = raw[h2_positions[2]:h2_positions[4]] + "\n\n" + lifestyle_block + "\n\n"
        p4 = raw[h2_positions[4]:]
        final_content = p1 + p2 + p3 + p4
    elif len(h2_positions) >= 3:
        p1 = raw[:h2_positions[1]] + "\n\n" + carousel_html + "\n\n"
        p2 = raw[h2_positions[1]:h2_positions[2]] + "\n\n" + flatlay_block + "\n\n"
        p3 = raw[h2_positions[2]:] + "\n\n" + lifestyle_block + "\n\n"
        final_content = p1 + p2 + p3
    else:
        final_content = carousel_html + "\n\n" + flatlay_block + "\n\n" + raw + "\n\n" + lifestyle_block

    # 5. Send update
    patch_payload = {
        "featured_media": hero_id,
        "content": final_content,
        "meta": {
            "_yoast_wpseo_opengraph-image": hero_url,
            "_yoast_wpseo_twitter-image": hero_url
        }
    }
    patch_req = urllib.request.Request(
        f"{WP_URL}/wp-json/wp/v2/posts/{pid}",
        data=json.dumps(patch_payload).encode('utf-8'),
        headers=HEADERS,
        method="POST"
    )
    with urllib.request.urlopen(patch_req, timeout=45) as resp:
        print(f"Normalized Post {pid} successfully.")

if __name__ == "__main__":
    # RANK 8
    rank8_carousel = [
        {"name": "The Estrella Oval Bangle", "url": "https://www.bluestone.com/bangles/the-estrella-oval-bangle~34771.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-estrella-oval-bangle-carousel-2026-1.webp"},
        {"name": "The Channing Bangle", "url": "https://www.bluestone.com/bangles/the-channing-bangle~975.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-channing-bangle-carousel-2026-1.webp"},
        {"name": "The Muricelle Bangle", "url": "https://www.bluestone.com/bangles/the-muricelle-bangle~1001.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-muricelle-bangle-carousel-2026-1.webp"},
        {"name": "The Skein Bangle", "url": "https://www.bluestone.com/bangles/the-skein-bangle~27491.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-skein-bangle-carousel-2026-1.webp"},
        {"name": "The Pear Evil Eye Toggle Bangle", "url": "https://www.bluestone.com/bangles/the-pear-evil-eye-toggle-bangle~87037.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-pear-evil-eye-toggle-bangle-carousel-2026-1.webp"},
        {"name": "The Tarentella Oval Bangle", "url": "https://www.bluestone.com/bangles/the-tarentella-oval-bangle~31547.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-tarentella-oval-bangle-carousel-2026-1.webp"}
    ]
    normalize_post(
        pid=39414,
        slug="casual-daily-wear-gold-bangle-2026",
        title_kw="Casual Daily Wear Gold Bangle",
        hero_id=39441,
        hero_url="https://blog.bluestone.com/wp-content/uploads/2026/09/casual-daily-wear-gold-bangle-hero-2026.webp",
        flatlay_id=39442,
        flatlay_url="https://blog.bluestone.com/wp-content/uploads/2026/09/casual-daily-wear-gold-bangle-flatlay-2026.webp",
        flatlay_pdp="https://www.bluestone.com/bangles/the-channing-bangle~975.html",
        flatlay_alt="Casual daily wear gold bangle buying guide 2026 flatlay on Italian marble showing The Channing Bangle",
        flatlay_caption="Minimalist everyday design: <a href=\"https://www.bluestone.com/bangles/the-channing-bangle~975.html\">The Channing Bangle</a> in high-polish 18k yellow gold",
        lifestyle_id=39443,
        lifestyle_url="https://blog.bluestone.com/wp-content/uploads/2026/09/casual-daily-wear-gold-bangle-lifestyle-2026.webp",
        lifestyle_pdp="https://www.bluestone.com/bangles/the-muricelle-bangle~1001.html",
        lifestyle_alt="Casual daily wear gold bangle buying guide 2026 lifestyle: fair-skinned Indian professional wearing The Muricelle Bangle",
        lifestyle_caption="Desk-to-dinner elegance: <a href=\"https://www.bluestone.com/bangles/the-muricelle-bangle~1001.html\">The Muricelle Bangle</a> offering lightweight comfort and secure clasp closure",
        carousel_products=rank8_carousel
    )

    # RANK 9
    rank9_carousel = [
        {"name": "The Aleena Huggie Earrings", "url": "https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-aleena-huggie-earrings-carousel-2026-3.webp"},
        {"name": "The Vicky Hoop Earrings", "url": "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-vicky-hoop-earrings-carousel-2026-2.webp"},
        {"name": "The Ursa Hoop Earrings", "url": "https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-ursa-hoop-earrings-carousel-2026-2.webp"},
        {"name": "The Rohal Huggie Earrings", "url": "https://www.bluestone.com/earrings/the-rohal-huggie-earrings~21864.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-rohal-huggie-earrings-carousel-2026-2.webp"},
        {"name": "The Asya Huggie Earrings", "url": "https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-asya-huggie-earrings-carousel-2026-2.webp"},
        {"name": "The Skein Hoop Earrings", "url": "https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-skein-hoop-earrings-carousel-2026-3.webp"}
    ]
    normalize_post(
        pid=39421,
        slug="daily-wear-earrings-2026",
        title_kw="Daily Wear Earrings",
        hero_id=39456,
        hero_url="https://blog.bluestone.com/wp-content/uploads/2026/09/daily-wear-earrings-hero-2026.webp",
        flatlay_id=39457,
        flatlay_url="https://blog.bluestone.com/wp-content/uploads/2026/09/daily-wear-earrings-flatlay-2026.webp",
        flatlay_pdp="https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html",
        flatlay_alt="Daily wear earrings buying guide 2026 flatlay on travertine tray showing The Vicky Hoop Earrings",
        flatlay_caption="Effortless everyday loops: <a href=\"https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html\">The Vicky Hoop Earrings</a> featuring secure click-top closures",
        lifestyle_id=39458,
        lifestyle_url="https://blog.bluestone.com/wp-content/uploads/2026/09/daily-wear-earrings-lifestyle-2026.webp",
        lifestyle_pdp="https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html",
        lifestyle_alt="Daily wear earrings buying guide 2026 lifestyle: fair-skinned Indian woman styling The Ursa Hoop Earrings",
        lifestyle_caption="Contemporary hoops: <a href=\"https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html\">The Ursa Hoop Earrings</a> crafted for all-day earlobe comfort",
        carousel_products=rank9_carousel
    )

    # RANK 10
    rank10_carousel = [
        {"name": "The Thaloria Pendant", "url": "https://www.bluestone.com/pendants/the-thaloria-pendant~165041.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-thaloria-pendant-carousel-2026-2.webp"},
        {"name": "The Lumeelle Cluster Pendant", "url": "https://www.bluestone.com/pendants/the-lumeelle-cluster-pendant~162509.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-lumeelle-cluster-pendant-carousel-2026-4.webp"},
        {"name": "The Thyvarne Pendant", "url": "https://www.bluestone.com/pendants/the-thyvarne-pendant~173761.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-thyvarne-pendant-carousel-2026.webp"},
        {"name": "The Aagarna Pendant", "url": "https://www.bluestone.com/pendants/the-aagarna-pendant~54965.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-aagarna-pendant-carousel-2026.webp"},
        {"name": "The Sarvanya Pendant", "url": "https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-sarvanya-pendant-carousel-2026-3.webp"},
        {"name": "The Teshvarya Pendant", "url": "https://www.bluestone.com/pendants/the-teshvarya-pendant~173771.html", "media_url": "https://blog.bluestone.com/wp-content/uploads/2026/09/the-teshvarya-pendant-carousel-2026-1.webp"}
    ]
    normalize_post(
        pid=39440,
        slug="white-stone-necklace-2026",
        title_kw="White Stone Necklace",
        hero_id=39466,
        hero_url="https://blog.bluestone.com/wp-content/uploads/2026/09/white-stone-necklace-hero-2026.webp",
        flatlay_id=39467,
        flatlay_url="https://blog.bluestone.com/wp-content/uploads/2026/09/white-stone-necklace-flatlay-2026.webp",
        flatlay_pdp="https://www.bluestone.com/pendants/the-lumeelle-cluster-pendant~162509.html",
        flatlay_alt="White stone necklace buying guide 2026 flatlay on dark slate stone showing The Lumeelle Cluster Pendant",
        flatlay_caption="Precision cluster setting: <a href=\"https://www.bluestone.com/pendants/the-lumeelle-cluster-pendant~162509.html\">The Lumeelle Cluster Pendant</a> featuring brilliant white sapphire accents",
        lifestyle_id=39468,
        lifestyle_url="https://blog.bluestone.com/wp-content/uploads/2026/09/white-stone-necklace-lifestyle-2026.webp",
        lifestyle_pdp="https://www.bluestone.com/pendants/the-thyvarne-pendant~173761.html",
        lifestyle_alt="White stone necklace buying guide 2026 lifestyle: fair-skinned Indian woman styling The Thyvarne Pendant",
        lifestyle_caption="Evening sparkle: <a href=\"https://www.bluestone.com/pendants/the-thyvarne-pendant~173761.html\">The Thyvarne Pendant</a> offering radiant light reflection in solid 18k gold",
        carousel_products=rank10_carousel
    )
