#!/usr/bin/env python3
"""
Patch Rank 95 (post 38094) carousel to the premium 3D Coverflow snippet:
- Stage height 400px (eliminates collision with headings)
- Nav prev/next buttons + dots
- Single line ellipsis on card title
- Curated Design Highlights list with PDP links
- Clean single <!-- wp:html --> block
"""

import os
import json
import base64
import urllib.request

def main():
    env = {}
    with open('.env') as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                k, v = line.strip().split('=', 1)
                env[k] = v

    base_url = env.get('WP_BASE_URL', 'https://blog.bluestone.com/wp-json/wp/v2').rstrip('/')
    user = env.get('WP_USER')
    pwd = env.get('WP_APP_PASSWORD')
    auth = base64.b64encode(f'{user}:{pwd}'.encode()).decode()
    headers = {
        'Authorization': f'Basic {auth}',
        'Content-Type': 'application/json'
    }

    post_id = 38094
    req = urllib.request.Request(f'{base_url}/posts/{post_id}', headers={'Authorization': f'Basic {auth}'})
    with urllib.request.urlopen(req) as resp:
        post = json.loads(resp.read().decode())

    content = post['content']['raw'] if 'raw' in post['content'] else post['content']['rendered']

    start_marker = '<style>\n.bs-cf'
    if start_marker not in content:
        start_marker = '<style>'
    
    end_marker = '<h2 class="wp-block-heading">Ring Sizing, Comfort Fit Shanks'
    
    idx_start = content.find(start_marker)
    idx_end = content.find(end_marker)

    if idx_start == -1 or idx_end == -1:
        print(f"Error finding markers: start={idx_start}, end={idx_end}")
        return

    prefix = content[:idx_start].rstrip()
    suffix = content[idx_end:]

    carousel_html = """<!-- wp:html -->
<style>
.bs-cf{max-width:920px;margin:2rem auto 2.75rem;position:relative;perspective:1200px}
.bs-cf-stage{position:relative;height:400px;margin:0 auto 1rem;overflow:visible}
.bs-cf-card{position:absolute;top:0;left:50%;width:min(380px,75vw);transform-origin:center center;transition:transform .65s cubic-bezier(.22,.61,.36,1),opacity .65s ease,filter .65s ease;border-radius:14px;background:#fff;box-shadow:0 10px 28px rgba(0,0,0,.12);overflow:hidden;border:1px solid #e8e8e8}
.bs-cf-media{display:block;line-height:0;background:#f4f4f4}
.bs-cf-media img{display:block;width:100%;aspect-ratio:16/9;height:auto;object-fit:cover;object-position:center}
.bs-cf-meta{padding:12px 14px 14px;text-align:center;background:#fff}
.bs-cf-name{margin:0 0 8px;font-size:0.95rem;font-weight:600;color:#1a1a1a;text-decoration:none;line-height:1.3;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bs-cf-cta{display:inline-block;padding:7px 18px;border-radius:4px;background:#111;color:#fff!important;font-size:.82rem;font-weight:600;text-decoration:none!important;letter-spacing:.02em}
.bs-cf-cta:hover{background:#333;color:#fff!important}
.bs-cf-card.is-pos-0{z-index:5;opacity:1;filter:none;transform:translate3d(-50%,4px,0) scale(1)}
.bs-cf-card.is-pos-1{z-index:3;opacity:.92;filter:brightness(.95);transform:translate3d(calc(-50% + 185px),24px,-90px) rotateY(-22deg) scale(.8)}
.bs-cf-card.is-pos-2{z-index:3;opacity:.92;filter:brightness(.95);transform:translate3d(calc(-50% - 185px),24px,-90px) rotateY(22deg) scale(.8)}
.bs-cf-card.is-pos-3,.bs-cf-card.is-pos--3{z-index:1;opacity:.25;pointer-events:none;transform:translate3d(calc(-50% + 310px),44px,-170px) rotateY(-32deg) scale(.62)}
.bs-cf-card.is-pos--1{z-index:1;opacity:.25;pointer-events:none;transform:translate3d(calc(-50% - 310px),44px,-170px) rotateY(32deg) scale(.62)}
.bs-cf-dots{display:flex;justify-content:center;gap:8px;margin-top:16px;position:relative;z-index:6}
.bs-cf-dot{width:8px;height:8px;border-radius:50%;border:0;padding:0;background:#c8c8c8;cursor:pointer}
.bs-cf-dot.is-active{background:#111;transform:scale(1.2)}
.bs-cf-nav{position:absolute;top:40%;z-index:10;width:40px;height:40px;border:0;border-radius:50%;background:rgba(255,255,255,.96);box-shadow:0 3px 10px rgba(0,0,0,.15);cursor:pointer;font-size:22px;color:#111;display:flex;align-items:center;justify-content:center;transform:translateY(-50%)}
.bs-cf-prev{left:-10px}.bs-cf-next{right:-10px}
@media (max-width:700px){
  .bs-cf{margin:1.5rem auto 2rem}
  .bs-cf-stage{height:320px}
  .bs-cf-card{width:min(280px,80vw)}
  .bs-cf-card.is-pos-1{transform:translate3d(calc(-50% + 115px),24px,-60px) rotateY(-20deg) scale(.74)}
  .bs-cf-card.is-pos-2{transform:translate3d(calc(-50% - 115px),24px,-60px) rotateY(20deg) scale(.74)}
  .bs-cf-card.is-pos-3,.bs-cf-card.is-pos--3,.bs-cf-card.is-pos--1{opacity:0}
  .bs-cf-prev{left:2px}.bs-cf-next{right:2px}
}
@media (prefers-reduced-motion:reduce){.bs-cf-card{transition:none}}
</style>
<div class="bs-cf" id="bs-cf-platinum-diamond-ring" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone Platinum Diamond Ring Collection">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
    <div class="bs-cf-card" data-i="0">
      <a class="bs-cf-media" href="https://www.bluestone.com/rings/the-jasper-band-for-him~93964.html">
        <img data-recalc-dims="1" src="https://i0.wp.com/blog.bluestone.com/wp-content/uploads/2026/09/the-jasper-band-for-him-carousel-9.webp?resize=960%2C535&amp;ssl=1" alt="platinum diamond ring 2026 design: The Jasper Band For Him" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <p class="bs-cf-name">The Jasper Band For Him</p>
        <a class="bs-cf-cta" href="https://www.bluestone.com/rings/the-jasper-band-for-him~93964.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card" data-i="1">
      <a class="bs-cf-media" href="https://www.bluestone.com/rings/the-liza-ring~7623.html">
        <img data-recalc-dims="1" src="https://i0.wp.com/blog.bluestone.com/wp-content/uploads/2026/09/the-liza-ring-carousel-7.webp?resize=960%2C535&amp;ssl=1" alt="platinum diamond ring 2026 design: The Liza ring" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <p class="bs-cf-name">The Liza Ring</p>
        <a class="bs-cf-cta" href="https://www.bluestone.com/rings/the-liza-ring~7623.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card" data-i="2">
      <a class="bs-cf-media" href="https://www.bluestone.com/rings/the-gigi-ring~64382.html">
        <img data-recalc-dims="1" src="https://i0.wp.com/blog.bluestone.com/wp-content/uploads/2026/09/the-gigi-ring-carousel-4.webp?resize=960%2C535&amp;ssl=1" alt="platinum diamond ring 2026 design: The Gigi Ring" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <p class="bs-cf-name">The Gigi Ring</p>
        <a class="bs-cf-cta" href="https://www.bluestone.com/rings/the-gigi-ring~64382.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card" data-i="3">
      <a class="bs-cf-media" href="https://www.bluestone.com/rings/the-rafia-ring~53638.html">
        <img data-recalc-dims="1" src="https://i0.wp.com/blog.bluestone.com/wp-content/uploads/2026/09/the-rafia-ring-carousel-6.webp?resize=960%2C535&amp;ssl=1" alt="platinum diamond ring 2026 design: The Rafia Ring" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <p class="bs-cf-name">The Rafia Ring</p>
        <a class="bs-cf-cta" href="https://www.bluestone.com/rings/the-rafia-ring~53638.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card" data-i="4">
      <a class="bs-cf-media" href="https://www.bluestone.com/rings/the-malibu-ring~2321.html">
        <img data-recalc-dims="1" src="https://i0.wp.com/blog.bluestone.com/wp-content/uploads/2026/09/the-malibu-ring-carousel-7.webp?resize=960%2C535&amp;ssl=1" alt="platinum diamond ring 2026 design: The Malibu Ring" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <p class="bs-cf-name">The Malibu Ring</p>
        <a class="bs-cf-cta" href="https://www.bluestone.com/rings/the-malibu-ring~2321.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card" data-i="5">
      <a class="bs-cf-media" href="https://www.bluestone.com/rings/the-anya-ring~7515.html">
        <img data-recalc-dims="1" src="https://i0.wp.com/blog.bluestone.com/wp-content/uploads/2026/09/the-anya-ring-carousel-7.webp?resize=960%2C535&amp;ssl=1" alt="platinum diamond ring 2026 design: The Anya Ring" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <p class="bs-cf-name">The Anya Ring</p>
        <a class="bs-cf-cta" href="https://www.bluestone.com/rings/the-anya-ring~7515.html">Buy now</a>
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
  var root=document.getElementById('bs-cf-platinum-diamond-ring');
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
<!-- /wp:html -->

<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong><a href="https://www.bluestone.com/rings/the-jasper-band-for-him~93964.html">The Jasper Band For Him</a>:</strong> A bold platinum band with brushed satin finish accented by precision channel-set brilliant diamonds for sleek masculine refinement.</li>
<li><strong><a href="https://www.bluestone.com/rings/the-liza-ring~7623.html">The Liza Ring</a>:</strong> Elegant platinum solitaire ring featuring a high-brilliance prong-set diamond with refined tapered shoulders.</li>
<li><strong><a href="https://www.bluestone.com/rings/the-gigi-ring~64382.html">The Gigi Ring</a>:</strong> Modern multi-row diamond eternity styling engineered in high-polish Pt950 platinum.</li>
<li><strong><a href="https://www.bluestone.com/rings/the-rafia-ring~53638.html">The Rafia Ring</a>:</strong> Sculptural floral-inspired platinum diamond ring highlighting exceptional light performance.</li>
<li><strong><a href="https://www.bluestone.com/rings/the-malibu-ring~2321.html">The Malibu Ring</a>:</strong> Contemporary wave-profile band pairing tension-set diamonds with seamless comfort ergonomics.</li>
<li><strong><a href="https://www.bluestone.com/rings/the-anya-ring~7515.html">The Anya Ring</a>:</strong> Timeless vintage halo diamond engagement design set in enduring platinum.</li>
</ul>
<!-- /wp:list -->
"""

    new_content = f"{prefix}\n\n{carousel_html}\n\n{suffix}"

    print(f"Original content length: {len(content)}")
    print(f"New content length: {len(new_content)}")

    update_payload = json.dumps({'content': new_content}).encode()
    put_req = urllib.request.Request(
        f'{base_url}/posts/{post_id}',
        data=update_payload,
        headers=headers,
        method='POST'
    )
    with urllib.request.urlopen(put_req) as resp:
        res = json.loads(resp.read().decode())
        print("Updated successfully! Status:", res.get('status'), "Slug:", res.get('slug'))

if __name__ == '__main__':
    main()
