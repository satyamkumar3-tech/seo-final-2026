#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix Carousel for Week 9 Rank 17 (white-stone-earrings-2026, Post ID 39633)."""

import os, sys, json, re, base64, urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / 'scripts'))

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
HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0",
    "Content-Type": "application/json"
}

OUTPUT_DIR = ROOT / "output" / "studio_carousel_webp"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def process_and_upload(src_path: Path, output_filename: str, title: str, alt: str, caption: str, target_w=960, target_h=535) -> tuple[int, str]:
    webp_path = OUTPUT_DIR / output_filename
    img = Image.open(src_path).convert("RGB")
    img_ratio = img.width / img.height
    target_ratio = target_w / target_h
    
    if img_ratio > target_ratio:
        new_h = target_h
        new_w = round(target_h * img_ratio)
        resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        left = (new_w - target_w) // 2
        cropped = resized.crop((left, 0, left + target_w, target_h))
    else:
        new_w = target_w
        new_h = round(target_w / img_ratio)
        resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        top = (new_h - target_h) // 2
        cropped = resized.crop((0, top, target_w, top + target_h))
        
    cropped.save(webp_path, "WEBP", quality=90, method=6)
    print(f"Generated {webp_path.name} ({cropped.width}x{cropped.height}, {os.path.getsize(webp_path)} bytes)")

    with open(webp_path, "rb") as f:
        img_data = f.read()
        
    upload_url = f"{WP_URL}/wp-json/wp/v2/media"
    req = urllib.request.Request(upload_url, data=img_data, headers={
        "Authorization": f"Basic {TOKEN}",
        "User-Agent": "BluestoneSEO/1.0",
        "Content-Disposition": f'attachment; filename="{output_filename}"',
        "Content-Type": "image/webp"
    }, method="POST")
    
    with urllib.request.urlopen(req, timeout=45) as resp:
        media_item = json.loads(resp.read().decode())
        media_id = media_item["id"]
        source_url = media_item["source_url"]
        
    update_url = f"{WP_URL}/wp-json/wp/v2/media/{media_id}"
    patch_payload = json.dumps({
        "title": title,
        "alt_text": alt,
        "caption": caption,
        "description": alt
    }).encode("utf-8")
    
    update_req = urllib.request.Request(update_url, data=patch_payload, headers=HEADERS, method="POST")
    with urllib.request.urlopen(update_req, timeout=30) as resp:
        print(f"Uploaded Media ID {media_id} -> {source_url}")
        
    return media_id, source_url

def render_carousel_snippet(slug: str, aria_label: str, products: list) -> str:
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

def fix_rank17():
    pid = 39633
    slug = "white-stone-earrings-2026"
    kw_theme = "White Stone Earrings"
    
    raw_products = [
        {"name": "The Aleena Huggie Earrings", "url": "https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html", "png": ROOT / "ProductImages/seo images/Earrings/The Aleena Huggie Earrings.png"},
        {"name": "The Ursa Hoop Earrings", "url": "https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html", "png": ROOT / "ProductImages/seo images/Earrings/The Ursa Hoop Earrings.png"},
        {"name": "The Rohal Huggie Earrings", "url": "https://www.bluestone.com/earrings/the-rohal-huggie-earrings~21864.html", "png": ROOT / "ProductImages/seo images/Earrings/The Rohal Huggie Earrings.png"},
        {"name": "The Vicky Hoop Earrings", "url": "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html", "png": ROOT / "ProductImages/seo images/Earrings/The Vicky Hoop Earrings.png"},
        {"name": "The Asya Huggie Earrings", "url": "https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html", "png": ROOT / "ProductImages/seo images/Earrings/The Asya Huggie Earrings.png"},
        {"name": "The Skein Hoop Earrings", "url": "https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html", "png": ROOT / "ProductImages/seo images/Earrings/The Skein Hoop Earrings.png"}
    ]
    
    highlights_html = """<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong> Explore signature white gemstone and sparkling diamond earring designs handcrafted in fine gold for everyday radiance: <a href="https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html">The Aleena Huggie Earrings</a> with snug ergonomics, <a href="https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html">The Ursa Hoop Earrings</a> featuring smooth contouring, <a href="https://www.bluestone.com/earrings/the-rohal-huggie-earrings~21864.html">The Rohal Huggie Earrings</a> with rich emerald-cut styling, <a href="https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html">The Vicky Hoop Earrings</a> with airy geometric lightness, <a href="https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html">The Asya Huggie Earrings</a> with delicate pearl drops and diamond pavé, and <a href="https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html">The Skein Hoop Earrings</a> for modern textured elegance.</p>
<!-- /wp:paragraph -->"""

    products_with_urls = []
    for p in raw_products:
        p_filename = f"{re.sub(r'[^a-zA-Z0-9]+', '-', p['name'].lower()).strip('-')}-studio-carousel-2026.webp"
        mid, murl = process_and_upload(
            p["png"], p_filename, f"{p['name']} Studio Carousel 2026",
            f"{kw_theme} 2026: {p['name']} from BlueStone",
            f'<a href="{p["url"]}">{p["name"]}</a>'
        )
        products_with_urls.append({"name": p["name"], "url": p["url"], "img_url": murl, "alt": f"{kw_theme} 2026: {p['name']} from BlueStone"})
        
    carousel_block = render_carousel_snippet(slug, f"BlueStone {kw_theme} Collection", products_with_urls)
    full_carousel_section = carousel_block + "\n\n" + highlights_html
    
    # Fetch Post Content
    req = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/posts/{pid}?context=edit", headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        post = json.loads(resp.read().decode('utf-8'))
        raw = post['content']['raw']
        
    # Thoroughly clean any existing/broken carousel artifacts
    raw = re.sub(r'<!-- wp:html -->[\s\S]*?<!-- /wp:html -->', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<style>[\s\S]*?\.bs-cf[\s\S]*?</style>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<div class=[\"\']bs-cf[\"\'][\s\S]*?</div>\s*<script>[\s\S]*?</script>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<script>[\s\S]*?bs-cf[\s\S]*?</script>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<div class=[\"\']bs-cf[\"\'][\s\S]*?</div>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<!-- wp:paragraph -->\s*<p[^>]*>\s*<strong>Curated Design Highlights:</strong>[\s\S]*?<!-- /wp:paragraph -->', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<p[^>]*>\s*<strong>Curated Design Highlights:</strong>[\s\S]*?</p>', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r'\n{3,}', '\n\n', raw).strip()
    
    # Place carousel right after the 2nd H2 (Popular White Stone Earrings Designs section)
    h2_matches = list(re.finditer(r'(<!-- wp:heading [^>]*-->\s*<h2[^>]*>.*?Popular White Stone.*?</h2>\s*<!-- /wp:heading -->|<h2[^>]*>.*?Popular White Stone.*?</h2>)', raw, flags=re.IGNORECASE))
    if h2_matches:
        idx_c = h2_matches[0].end()
        # Find next paragraph after this heading if any
        next_p = re.search(r'(<!-- wp:paragraph -->[\s\S]*?<!-- /wp:paragraph -->|<p>[\s\S]*?</p>)', raw[idx_c:])
        if next_p:
            ins_point = idx_c + next_p.end()
        else:
            ins_point = idx_c
        final_content = raw[:ins_point] + "\n\n" + full_carousel_section + "\n\n" + raw[ins_point:]
    else:
        all_h2s = list(re.finditer(r'(<!-- wp:heading {\"level\":2} -->|<h2[^>]*>)', raw, flags=re.IGNORECASE))
        if len(all_h2s) >= 2:
            idx_c = all_h2s[1].start()
            final_content = raw[:idx_c] + full_carousel_section + "\n\n" + raw[idx_c:]
        else:
            final_content = full_carousel_section + "\n\n" + raw

    # Patch post
    patch_payload = {"content": final_content}
    patch_req = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/posts/{pid}", data=json.dumps(patch_payload).encode('utf-8'), headers=HEADERS, method='POST')
    with urllib.request.urlopen(patch_req, timeout=45) as resp:
        print(f"Successfully patched carousel for Post {pid} ({slug})!")

if __name__ == "__main__":
    fix_rank17()
