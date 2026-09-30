#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate official 3D Coverflow carousel HTML snippet for Week 9 Rank 90."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

with open(ROOT / "output/week9_rank90_carousel_media.json", encoding="utf-8") as f:
    items = json.load(f)

slug = "earring-styles-for-guys-2026"
carousel_id = "bs-cf-earring-styles-guys"

# Strict 3D Coverflow CSS
css = """<!-- wp:html -->
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
</style>"""

pos_classes = ["is-pos-0", "is-pos-1", "is-pos-2", "is-pos-3", "is-pos--2", "is-pos--1"]

cards_html = []
dots_html = []

for i, it in enumerate(items):
    pos_cls = pos_classes[i]
    active_cls = " is-active" if i == 0 else ""
    c_html = f"""    <div class="bs-cf-card {pos_cls}" data-index="{i}">
      <a class="bs-cf-media" href="{it['url']}">
        <img src="{it['image_url']}" alt="{it['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{it['name']}</div>
        <a class="bs-cf-cta" href="{it['url']}">Buy now</a>
      </div>
    </div>"""
    cards_html.append(c_html)
    dots_html.append(f"""    <button type="button" class="bs-cf-dot{active_cls}" data-i="{i}" aria-label="Product {i+1}"></button>""")

cards_str = "\n".join(cards_html)
dots_str = "\n".join(dots_html)

container_html = f"""<div class="bs-cf" id="{carousel_id}" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone Men's Earring Styles">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
{cards_str}
  </div>
  <div class="bs-cf-dots" role="tablist">
{dots_str}
  </div>
</div>"""

script = """<script>
(function(){
  var root=document.getElementById('""" + carousel_id + """');
  if(!root||root.dataset.ready==='1')return;
  root.dataset.ready='1';
  var cards=Array.prototype.slice.call(root.querySelectorAll('.bs-cf-card'));
  var dots=Array.prototype.slice.call(root.querySelectorAll('.bs-cf-dot'));
  var prevBtn=root.querySelector('.bs-cf-prev');
  var nextBtn=root.querySelector('.bs-cf-next');
  var n=cards.length;
  var cur=0;
  var timer=null;
  var interval=parseInt(root.getAttribute('data-interval')||'3200',10);

  function rel(i,c){return((i-c)%n+n)%n;}

  function paint(){
    cards.forEach(function(card,i){
      card.className=card.className.replace(/\\bis-pos-[^\\s]+\\b/g,'').trim();
      var r=rel(i,cur);
      var pos='is-pos-3';
      if(r===0)pos='is-pos-0';
      else if(r===1)pos='is-pos-1';
      else if(r===2)pos='is-pos-2';
      else if(r===n-1)pos='is-pos--1';
      else if(r===n-2)pos='is-pos--2';
      card.classList.add(pos);
    });
    dots.forEach(function(d,i){d.classList.toggle('is-active',i===cur);});
  }

  function go(t){cur=((t%n)+n)%n;paint();}
  function next(){go(cur+1);}
  function prev(){go(cur-1);}

  if(prevBtn)prevBtn.addEventListener('click',function(e){e.preventDefault();prev();restart();});
  if(nextBtn)nextBtn.addEventListener('click',function(e){e.preventDefault();next();restart();});
  dots.forEach(function(d){d.addEventListener('click',function(e){e.preventDefault();var i=parseInt(d.getAttribute('data-i'),10);if(!isNaN(i)){go(i);restart();}});});
  cards.forEach(function(card){card.addEventListener('click',function(e){var idx=parseInt(card.getAttribute('data-index'),10);if(idx!==cur){e.preventDefault();go(idx);restart();}});});

  function start(){if(!timer&&interval>0){timer=setInterval(next,interval);}}
  function stop(){if(timer){clearInterval(timer);timer=null;}}
  function restart(){stop();start();}

  root.addEventListener('mouseenter',stop);
  root.addEventListener('mouseleave',start);
  paint();
  start();
})();
</script>
<!-- /wp:html -->"""

full_snippet = f"{css}\n{container_html}\n{script}"

out_file = ROOT / "output/week9_rank90_carousel_snippet.html"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(full_snippet)

print(f"Generated 3D coverflow carousel snippet at {out_file} ({len(full_snippet)} bytes)")
