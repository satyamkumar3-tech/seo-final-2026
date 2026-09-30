#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate comprehensive draft content and metadata for Week 9 Rank 62."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

slug = "gold-stud-earrings-designs-for-daily-use-2026"
primary_kw = "gold stud earrings designs for daily use"
supporting_kw = "light weight gold earrings designs for daily use"
title = "Gold Stud Earrings Designs for Daily Use 2026: Light Weight Styles, 18K vs 22K Purity, Earring Backs & Earlobe Comfort"
meta_title = "Gold Stud Earrings Designs for Daily Use (2026 Guide) | BlueStone"
meta_desc = "Explore gold stud earrings designs for daily use in 2026. Compare light weight gold styles, 18K vs 22K purity, secure screw backs, earlobe comfort, and BIS signs."

# Gutenberg helper
def p(text):
    return f"<!-- wp:paragraph -->\n<p>{text.strip()}</p>\n<!-- /wp:paragraph -->"

def h2(text):
    return f'<!-- wp:heading {{"level":2}} -->\n<h2>{text.strip()}</h2>\n<!-- /wp:heading -->'

def h3(text):
    return f'<!-- wp:heading {{"level":3}} -->\n<h3>{text.strip()}</h3>\n<!-- /wp:heading -->'

def ul(items):
    lis = "\n".join([f"<li>{it.strip()}</li>" for it in items])
    return f"<!-- wp:list -->\n<ul>\n{lis}\n</ul>\n<!-- /wp:list -->"

# Carousel snippet generator with 3D coverflow
def generate_carousel_block(slug_id, products):
    cards_html = []
    dots_html = []
    
    # Position classes for initial render: 0, 1, 2, 3, -2, -1
    pos_classes = ["is-pos-0", "is-pos-1", "is-pos-2", "is-pos-3", "is-pos--2", "is-pos--1"]
    
    for idx, prod in enumerate(products):
        pos_cls = pos_classes[idx]
        card = f'''    <div class="bs-cf-card {pos_cls}" data-index="{idx}">
      <a class="bs-cf-media" href="{prod['url']}">
        <img src="{prod['img_url']}" alt="{prod['alt']}" width="960" height="535" loading="lazy" />
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{prod['name']}</div>
        <a class="bs-cf-cta" href="{prod['url']}">Buy now</a>
      </div>
    </div>'''
        cards_html.append(card)
        active_cls = " is-active" if idx == 0 else ""
        dots_html.append(f'    <button type="button" class="bs-cf-dot{active_cls}" data-i="{idx}" aria-label="Product {idx+1}"></button>')

    cards_joined = "\n".join(cards_html)
    dots_joined = "\n".join(dots_html)

    style = '''<style>
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
</style>'''

    html_container = f'''<div class="bs-cf" id="bs-cf-{slug_id}" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone daily gold stud earrings collection">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
{cards_joined}
  </div>
  <div class="bs-cf-dots" role="tablist">
{dots_joined}
  </div>
</div>'''

    script = f'''<script>
(function(){{
  var root=document.getElementById('bs-cf-{slug_id}');
  if(!root||root.dataset.ready==='1')return;
  root.dataset.ready='1';
  var cards=[].slice.call(root.querySelectorAll('.bs-cf-card'));
  var dots=[].slice.call(root.querySelectorAll('.bs-cf-dot'));
  var total=cards.length;
  if(total<2)return;
  var idx=0,timer=null,interval=parseInt(root.getAttribute('data-interval')||'3200',10);
  function rel(i,c){{var d=(i-c)%total;if(d>total/2)d-=total;if(d<-total/2)d+=total;return d;}}
  function paint(){{
    cards.forEach(function(c,i){{
      var r=rel(i,idx);
      c.className='bs-cf-card';
      if(r===0)c.classList.add('is-pos-0');
      else if(r===1)c.classList.add('is-pos-1');
      else if(r===-1)c.classList.add('is-pos-2');
      else if(r===2)c.classList.add('is-pos-3');
      else if(r===-2)c.classList.add('is-pos--1');
      else c.classList.add('is-pos--3');
    }});
    dots.forEach(function(d,i){{
      if(i===idx)d.classList.add('is-active');
      else d.classList.remove('is-active');
    }});
  }}
  function go(n){{idx=(n+total)%total;paint();}}
  function next(){{go(idx+1);}}
  function prev(){{go(idx-1);}}
  function start(){{stop();timer=setInterval(next,interval);}}
  function stop(){{if(timer){{clearInterval(timer);timer=null;}}}}
  root.querySelector('.bs-cf-next').addEventListener('click',function(){{next();start();}});
  root.querySelector('.bs-cf-prev').addEventListener('click',function(){{prev();start();}});
  dots.forEach(function(d){{
    d.addEventListener('click',function(){{
      var target=parseInt(d.getAttribute('data-i')||'0',10);
      go(target);
      start();
    }});
  }});
  root.addEventListener('mouseenter',stop);
  root.addEventListener('mouseleave',start);
  root.addEventListener('touchstart',stop,{{passive:true}});
  root.addEventListener('touchend',start,{{passive:true}});
  paint();
  start();
}})();
</script>'''

    return f"<!-- wp:html -->\n{style}\n{html_container}\n{script}\n<!-- /wp:html -->"

print("Helper definitions complete")
