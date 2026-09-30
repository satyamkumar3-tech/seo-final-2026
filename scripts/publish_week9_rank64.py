import os
import sys
import time
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Load env
env = {}
with open(ROOT / ".env") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            env[k.strip()] = v.strip().strip('\'\"')

user = env.get("WP_USER")
pwd = env.get("WP_APP_PASSWORD")
token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
AUTH_HEADERS = {
    "Authorization": f"Basic {token}",
    "User-Agent": "BluestoneSEO/1.0"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"

def req_with_retry(req, max_retries=5, initial_delay=3):
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return resp.status, resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"HTTP 429 received. Waiting {delay}s before retry (attempt {attempt+1}/{max_retries})...")
                time.sleep(delay)
                delay *= 2
            else:
                print(f"HTTP error {e.code}: {e.reason}")
                raise e
    raise Exception("Max retries exceeded for request")

def build_3d_coverflow(products, slug="yellow-stone-ring-2026"):
    # Official snippet strictly matching templates/eid_carousel_6_snippet.html
    css = """<style>
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
</style>"""

    pos_classes = ["is-pos-0", "is-pos-1", "is-pos-2", "is-pos-3", "is-pos--2", "is-pos--1"]
    card_htmls = []
    dot_htmls = []

    for i, p in enumerate(products):
        cls = pos_classes[i]
        card_htmls.append(f"""    <div class="bs-cf-card {cls}" data-index="{i}">
      <a class="bs-cf-media" href="{p['url']}">
        <img src="{p['src']}" alt="{p['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{p['name']}</div>
        <a class="bs-cf-cta" href="{p['url']}">Buy now</a>
      </div>
    </div>""")
        dot_cls = "is-active" if i == 0 else ""
        dot_htmls.append(f'    <button type="button" class="bs-cf-dot {dot_cls}" data-i="{i}" aria-label="Product {i+1}"></button>')

    cards_str = "\n".join(card_htmls)
    dots_str = "\n".join(dot_htmls)

    js = f"""<script>
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
</script>"""

    snippet = f"""<!-- wp:html -->
{css}
<div class="bs-cf" id="bs-cf-{slug}" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone Yellow Stone Ring designs">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
{cards_str}
  </div>
  <div class="bs-cf-dots" role="tablist">
{dots_str}
  </div>
</div>
{js}
<!-- /wp:html -->"""

    curated_highlights = f"""<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong> Explore signature fine jewellery ring silhouettes, from the sleek solitaire profile of <a href="{products[0]['url']}">{products[0]['name']}</a> and the intricate vintage halo architecture of <a href="{products[1]['url']}">{products[1]['name']}</a>, to the radiant multi-gemstone band of <a href="{products[2]['url']}">{products[2]['name']}</a>, the bold architectural rows of <a href="{products[3]['url']}">{products[3]['name']}</a>, the organic floral curves of <a href="{products[4]['url']}">{products[4]['name']}</a>, and the contemporary geometric lines of <a href="{products[5]['url']}">{products[5]['name']}</a>.</p>
<!-- /wp:paragraph -->"""

    return snippet + "\n\n" + curated_highlights

def main():
    # 1. Read Draft
    with open(ROOT / "output/Week9_Rank64_yellow_stone_ring_draft.json") as f:
        draft = json.load(f)

    # 2. Read Product Media
    with open(ROOT / "output/Week9_Rank64_product_media.json") as f:
        product_media = json.load(f)

    # 3. Build Carousel block
    carousel_block = build_3d_coverflow(product_media, draft["slug"])

    # 4. Splice Carousel into content
    content = draft["content"]
    if "<!-- CAROUSEL_PLACEHOLDER -->" in content:
        content = content.replace("<!-- CAROUSEL_PLACEHOLDER -->", carousel_block)
    else:
        raise Exception("Carousel placeholder not found in draft content")

    # 5. Check duplicate post ID or existing slug
    check_req = urllib.request.Request(f"{WP_API}/posts?slug={draft['slug']}", headers=AUTH_HEADERS)
    _, check_body = req_with_retry(check_req)
    existing_posts = json.loads(check_body.decode())
    
    post_payload = {
        "title": draft["title"],
        "slug": draft["slug"],
        "status": "publish",
        "author": 270271337,
        "categories": [554493326, 554493414, 554493465],
        "content": content,
        "excerpt": draft["meta_desc"],
        "meta": {
            "_yoast_wpseo_focuskw": draft["focus_kw"],
            "_yoast_wpseo_title": draft["meta_title"],
            "_yoast_wpseo_metadesc": draft["meta_desc"]
        }
    }

    if existing_posts:
        pid = existing_posts[0]["id"]
        print(f"Post with slug {draft['slug']} already exists (ID: {pid}). Updating post...")
        post_url = f"{WP_API}/posts/{pid}"
    else:
        print(f"Creating new post for slug {draft['slug']}...")
        post_url = f"{WP_API}/posts"

    post_req = urllib.request.Request(
        post_url,
        data=json.dumps(post_payload).encode(),
        headers={**AUTH_HEADERS, "Content-Type": "application/json"},
        method="POST"
    )
    time.sleep(2)
    _, resp_body = req_with_retry(post_req)
    post_res = json.loads(resp_body.decode())
    
    published_id = post_res["id"]
    published_url = post_res["link"]
    print(f"SUCCESS: Published post ID {published_id}")
    print(f"Live URL: {published_url}")

    # Save publish receipt
    receipt = {
        "post_id": published_id,
        "url": published_url,
        "slug": draft["slug"],
        "title": draft["title"],
        "author": 270271337,
        "categories": [554493326, 554493414, 554493465],
        "published_at": post_res.get("date"),
        "modified_at": post_res.get("modified")
    }
    receipt_path = ROOT / "output/Week9_Rank64_publish_receipt.json"
    with open(receipt_path, "w", encoding="utf-8") as f:
        json.dump(receipt, f, indent=2)
    print(f"Publish receipt saved to {receipt_path}")

if __name__ == "__main__":
    main()
