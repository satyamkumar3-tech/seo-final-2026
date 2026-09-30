#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the complete article draft JSON for Week 9 Rank 80 - Multicolor Earrings."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Load verified carousel media
with open(ROOT / "output/week9_rank80_carousel_media.json", encoding="utf-8") as f:
    carousel_items = json.load(f)

# 3D Coverflow template
carousel_html = f"""<!-- wp:html -->
<style>
.bs-cf {{
  max-width: 900px;
  margin: 1.75rem auto 1.25rem;
  padding: 0 10px;
  box-sizing: border-box;
  font-family: inherit;
  position: relative;
  perspective: 1200px;
}}
.bs-cf-stage {{
  position: relative;
  width: 100%;
  height: 360px;
  margin: 0 auto;
  transform-style: preserve-3d;
  overflow: visible;
}}
.bs-cf-card {{
  position: absolute;
  top: 0;
  left: 50%;
  width: min(420px, 78vw);
  margin-left: calc(min(420px, 78vw) / -2);
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid #ececec;
  box-shadow: 0 12px 30px rgba(0,0,0,.12);
  overflow: hidden;
  box-sizing: border-box;
  transition: transform .45s cubic-bezier(.25,1,.35,1), opacity .45s ease, z-index .45s step-end;
  cursor: pointer;
  display: flex;
  flex-direction: column;
}}
.bs-cf-card.is-pos-0 {{
  transform: translate3d(0, 0, 0) scale(1);
  z-index: 10;
  opacity: 1;
}}
.bs-cf-card.is-pos-1 {{
  transform: translate3d(55%, 0, -120px) scale(0.88);
  z-index: 7;
  opacity: 0.85;
}}
.bs-cf-card.is-pos-2 {{
  transform: translate3d(95%, 0, -220px) scale(0.76);
  z-index: 4;
  opacity: 0.55;
}}
.bs-cf-card.is-pos-3 {{
  transform: translate3d(0, 0, -320px) scale(0.65);
  z-index: 1;
  opacity: 0;
  pointer-events: none;
}}
.bs-cf-card.is-pos--2 {{
  transform: translate3d(-95%, 0, -220px) scale(0.76);
  z-index: 4;
  opacity: 0.55;
}}
.bs-cf-card.is-pos--1 {{
  transform: translate3d(-55%, 0, -120px) scale(0.88);
  z-index: 7;
  opacity: 0.85;
}}
.bs-cf-media {{
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  background: #f6f6f6;
  overflow: hidden;
  display: block;
}}
.bs-cf-media img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform .4s ease;
}}
.bs-cf-card:hover .bs-cf-media img {{
  transform: scale(1.04);
}}
.bs-cf-body {{
  padding: 14px 16px 16px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  justify-content: space-between;
  background: #ffffff;
}}
.bs-cf-name {{
  margin: 0 0 10px;
  font-size: 1rem;
  font-weight: 600;
  color: #1a1a1a;
  line-height: 1.35;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}
.bs-cf-cta {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 8px 16px;
  background: #111111;
  color: #ffffff !important;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 0.3px;
  text-decoration: none !important;
  border-radius: 999px;
  transition: background .2s ease, transform .15s ease;
  width: fit-content;
}}
.bs-cf-cta:hover {{
  background: #333333;
  transform: translateY(-1px);
}}
.bs-cf-nav {{
  position: absolute;
  top: 45%;
  transform: translateY(-50%);
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: rgba(255,255,255,0.92);
  border: 1px solid #ddd;
  box-shadow: 0 4px 12px rgba(0,0,0,0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 20;
  font-size: 18px;
  color: #222;
  transition: background .2s, transform .15s;
}}
.bs-cf-nav:hover {{
  background: #ffffff;
  transform: translateY(-50%) scale(1.06);
}}
.bs-cf-prev {{ left: -6px; }}
.bs-cf-next {{ right: -6px; }}
.bs-cf-dots {{
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 14px;
}}
.bs-cf-dot {{
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #d4d4d4;
  cursor: pointer;
  transition: background .25s ease, transform .25s ease;
}}
.bs-cf-dot.is-active {{
  background: #111111;
  transform: scale(1.25);
}}
@media (max-width: 700px) {{
  .bs-cf-stage {{ height: 300px; }}
  .bs-cf-card {{ width: min(340px, 82vw); margin-left: calc(min(340px, 82vw) / -2); }}
  .bs-cf-card.is-pos-1 {{ transform: translate3d(42%, 0, -100px) scale(0.86); }}
  .bs-cf-card.is-pos--1 {{ transform: translate3d(-42%, 0, -100px) scale(0.86); }}
}}
</style>
<div class="bs-cf" id="bs-cf-multicolor-earrings-2026" data-interval="3200">
  <div class="bs-cf-stage">
    <div class="bs-cf-card is-pos-0" data-index="0">
      <a class="bs-cf-media" href="{carousel_items[0]['url']}">
        <img src="{carousel_items[0]['src']}" alt="{carousel_items[0]['alt']}" loading="eager" />
      </a>
      <div class="bs-cf-body">
        <h4 class="bs-cf-name">{carousel_items[0]['name']}</h4>
        <a class="bs-cf-cta" href="{carousel_items[0]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-1" data-index="1">
      <a class="bs-cf-media" href="{carousel_items[1]['url']}">
        <img src="{carousel_items[1]['src']}" alt="{carousel_items[1]['alt']}" loading="lazy" />
      </a>
      <div class="bs-cf-body">
        <h4 class="bs-cf-name">{carousel_items[1]['name']}</h4>
        <a class="bs-cf-cta" href="{carousel_items[1]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-2" data-index="2">
      <a class="bs-cf-media" href="{carousel_items[2]['url']}">
        <img src="{carousel_items[2]['src']}" alt="{carousel_items[2]['alt']}" loading="lazy" />
      </a>
      <div class="bs-cf-body">
        <h4 class="bs-cf-name">{carousel_items[2]['name']}</h4>
        <a class="bs-cf-cta" href="{carousel_items[2]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-3" data-index="3">
      <a class="bs-cf-media" href="{carousel_items[3]['url']}">
        <img src="{carousel_items[3]['src']}" alt="{carousel_items[3]['alt']}" loading="lazy" />
      </a>
      <div class="bs-cf-body">
        <h4 class="bs-cf-name">{carousel_items[3]['name']}</h4>
        <a class="bs-cf-cta" href="{carousel_items[3]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos--2" data-index="4">
      <a class="bs-cf-media" href="{carousel_items[4]['url']}">
        <img src="{carousel_items[4]['src']}" alt="{carousel_items[4]['alt']}" loading="lazy" />
      </a>
      <div class="bs-cf-body">
        <h4 class="bs-cf-name">{carousel_items[4]['name']}</h4>
        <a class="bs-cf-cta" href="{carousel_items[4]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos--1" data-index="5">
      <a class="bs-cf-media" href="{carousel_items[5]['url']}">
        <img src="{carousel_items[5]['src']}" alt="{carousel_items[5]['alt']}" loading="lazy" />
      </a>
      <div class="bs-cf-body">
        <h4 class="bs-cf-name">{carousel_items[5]['name']}</h4>
        <a class="bs-cf-cta" href="{carousel_items[5]['url']}">Buy now</a>
      </div>
    </div>
  </div>
  <button class="bs-cf-nav bs-cf-prev" aria-label="Previous card">&#10094;</button>
  <button class="bs-cf-nav bs-cf-next" aria-label="Next card">&#10095;</button>
  <div class="bs-cf-dots">
    <span class="bs-cf-dot is-active" data-index="0"></span>
    <span class="bs-cf-dot" data-index="1"></span>
    <span class="bs-cf-dot" data-index="2"></span>
    <span class="bs-cf-dot" data-index="3"></span>
    <span class="bs-cf-dot" data-index="4"></span>
    <span class="bs-cf-dot" data-index="5"></span>
  </div>
</div>
<script>
(function(){{
  var root = document.getElementById('bs-cf-multicolor-earrings-2026');
  if (!root || root.dataset.ready === '1') return;
  root.dataset.ready = '1';
  var cards = Array.prototype.slice.call(root.querySelectorAll('.bs-cf-card'));
  var dots = Array.prototype.slice.call(root.querySelectorAll('.bs-cf-dot'));
  var total = cards.length;
  var current = 0;
  var timer = null;
  var interval = parseInt(root.getAttribute('data-interval') || '3200', 10);
  var classOrder = ['is-pos-0', 'is-pos-1', 'is-pos-2', 'is-pos-3', 'is-pos--2', 'is-pos--1'];
  function rel(i, c) {{ return (i-c + total) % total; }}
  function paint() {{
    for (var i = 0; i < total; i++) {{
      var r = rel(i, current);
      var el = cards[i];
      for (var k = 0; k < classOrder.length; k++) {{
        el.classList.remove(classOrder[k]);
      }}
      el.classList.add(classOrder[r]);
    }}
    for (var d = 0; d < dots.length; d++) {{
      if (d === current) {{
        dots[d].classList.add('is-active');
      }} else {{
        dots[d].classList.remove('is-active');
      }}
    }}
  }}
  function go(dir) {{
    current = (current + dir + total) % total;
    paint();
  }}
  function start() {{
    stop();
    timer = setInterval(function(){{ go(1); }}, interval);
  }}
  function stop() {{
    if (timer) {{ clearInterval(timer); timer = null; }}
  }}
  var prevBtn = root.querySelector('.bs-cf-prev');
  var nextBtn = root.querySelector('.bs-cf-next');
  if (prevBtn) prevBtn.addEventListener('click', function(e){{ e.preventDefault(); go(-1); start(); }});
  if (nextBtn) nextBtn.addEventListener('click', function(e){{ e.preventDefault(); go(1); start(); }});
  dots.forEach(function(dot){{
    dot.addEventListener('click', function(){{
      var idx = parseInt(this.getAttribute('data-index'), 10);
      if (!isNaN(idx)) {{ current = idx; paint(); start(); }}
    }});
  }});
  root.addEventListener('mouseenter', stop);
  root.addEventListener('mouseleave', start);
  root.addEventListener('touchstart', stop, {{ passive: true }});
  root.addEventListener('touchend', start, {{ passive: true }});
  paint();
  start();
}})();
</script>
<!-- /wp:html -->"""

curated_paragraph = f"""<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong> Explore signature multi-gemstone silhouettes from BlueStone, including <a href="{carousel_items[0]['url']}">{carousel_items[0]['name']}</a> in warm 18Kt gold with ruby accents, <a href="{carousel_items[1]['url']}">{carousel_items[1]['name']}</a> with sparkling prong settings, <a href="{carousel_items[2]['url']}">{carousel_items[2]['name']}</a> with artisanal sculpted contours, <a href="{carousel_items[3]['url']}">{carousel_items[3]['name']}</a> for subtle fluid movement, <a href="{carousel_items[4]['url']}">{carousel_items[4]['name']}</a> for vibrant geometric balance, and <a href="{carousel_items[5]['url']}">{carousel_items[5]['name']}</a> for delicate everyday earlobe comfort.</p>
<!-- /wp:paragraph -->"""

# Schema JSON-LD
schema_json = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "BlogPosting",
            "@id": "https://blog.bluestone.com/multicolor-earrings-2026/#article",
            "isPartOf": {
                "@type": "WebSite",
                "@id": "https://blog.bluestone.com/#website",
                "name": "BlueStone Jewellery Blog",
                "url": "https://blog.bluestone.com"
            },
            "headline": "How to Choose and Style Multicolor Earrings: An Informative Jewellery Guide (2026)",
            "description": "Explore how to choose and style multicolor earrings in fine gold. Learn about multi-gemstone pairings, lightweight comfort, BIS hallmarking, and care in 2026.",
            "url": "https://blog.bluestone.com/multicolor-earrings-2026/",
            "datePublished": "2026-09-26T23:25:00+05:30",
            "dateModified": "2026-09-26T23:25:00+05:30",
            "author": {
                "@type": "Person",
                "name": "Satyam",
                "jobTitle": "BlueStone Editorial"
            },
            "publisher": {
                "@type": "Organization",
                "name": "BlueStone Jewellery and Lifestyle Limited",
                "url": "https://www.bluestone.com",
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://cdn.bluestone.com/media/static/images/logo.png"
                }
            },
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": "https://blog.bluestone.com/multicolor-earrings-2026/"
            }
        },
        {
            "@type": "FAQPage",
            "@id": "https://blog.bluestone.com/multicolor-earrings-2026/#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "What are multicolor earrings in fine jewellery?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Multicolor earrings in fine jewellery are pieces crafted from authentic 18Kt or 14Kt gold that showcase two or more distinct colored gemstones, such as rubies, emeralds, sapphires, amethysts, tourmalines, citrines, or pearls. Unlike fashion costume jewellery made from plated base metals and synthetic resin, fine gold multicolor earrings offer lasting metallurgical integrity, secure gemstone prongs, and certified purity verified by BIS hallmarking."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How do I match multicolor earrings with my outfits?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "The most effective styling approach is the Hero Color Accent rule: identify one prominent gemstone color in your earrings and match it directly with a primary shade in your clothing or dupatta. Alternatively, treat multicolor earrings as your sole statement piece by styling them against neutral canvases like ivory raw silk, crisp white linen, charcoal grey, or black, which allows the natural gemstone colors to shine without competing patterns."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Are multicolor gold earrings suitable for everyday office wear?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Yes, multicolor gold earrings are exceptionally well suited for daily office wear when designed in compact silhouettes like huggies, small hoops, or cluster studs. Selecting light weight earrings with flush or bezel stone settings prevents snagging on winter knits or scarves while providing an elegant, professional touch of color to formal workwear."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How do I choose light weight earrings with multiple gemstones?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "To find comfortable light weight earrings featuring multiple stones, check the gross gold weight and silhouette architecture. Seek designs utilizing open back bezel galleries or precision CAD laser settings, which reduce unnecessary metal mass while maximizing gemstone light refraction. For all-day comfort, look for pairs weighing between 2.0 and 4.5 grams with secure screw back or Bombay screw closures."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Can I clean multi-gemstone gold earrings in an ultrasonic jewellery cleaner?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "No, you should never place multi-gemstone earrings into an ultrasonic cleaner. Different gemstones exhibit widely varying hardness and structural tolerances. While corundum stones like sapphires and rubies can tolerate ultrasonic vibrations, stones like emeralds, tourmalines, and organic pearls can fracture, cloud, or suffer dislodgement from high-frequency sound waves. Clean them safely by soaking in lukewarm water with mild liquid soap and gently scrubbing with a baby-soft brush."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How do I verify the authenticity of gold multicolor earrings in India?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Verify authenticity by checking for mandatory BIS hallmarking laser-engraved onto the earring stem or clasp. A genuine hallmark comprises the triangular BIS logo, the gold purity mark (such as 750 for 18Kt or 585 for 14Kt), and a unique 6-digit alphanumeric HUID code that can be verified through the BIS Care mobile application. Additionally, request authentic gemstone and diamond authenticity certification upon purchase."
                    }
                }
            ]
        }
    ]
}

schema_html = f"""<!-- wp:html -->
<script type="application/ld+json">
{json.dumps(schema_json, indent=2)}
</script>
<!-- /wp:html -->"""

# Content assembly
content_parts = [
    # Byline and Intro
    """<!-- wp:paragraph -->
<p><em>By Satyam, BlueStone Editorial</em></p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>Multicolor earrings crafted in fine gold represent one of the most versatile and expressive jewellery categories in modern fashion. By bringing together vibrant precious gemstones such as deep blue sapphires, lush green emeralds, fiery rubies, violet amethysts, and sunny citrines within durable 18Kt or 14Kt gold frameworks, these pieces bridge the gap between heirloom Indian heritage and contemporary minimalist styling. Whether you are searching for everyday light weight earrings to wear to the office or a magnificent statement pair for festive celebrations, understanding how multi-stone jewellery is engineered, evaluated, and harmonized will ensure your investment remains radiant for generations.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p><strong>Quick Buying Takeaway (TL;DR):</strong> When selecting multicolor earrings, prioritize fine gold alloy strength (18Kt or 14Kt) that holds multiple gemstones securely, look for BIS hallmarking with a verified 6-digit HUID code, and choose lightweight ergonomic silhouettes (under 4.5 grams per pair) for seamless daily comfort. For effortless styling, anchor the look with the Hero Color Accent rule or pair multi-hued jewels against crisp neutral monochrome ensembles.</p>
<!-- /wp:paragraph -->""",

    # Section 1
    """<!-- wp:heading -->
<h2 class="wp-block-heading">Understanding Multicolor Earrings: The Fusion of Gemstone Artistry and Fine Gold</h2>
<!-- /wp:heading -->""",

    """<!-- wp:paragraph -->
<p>In the landscape of fine jewellery, multicolor earrings occupy a distinctive artistic space. Unlike single-stone solitaires or monochrome diamond bands, multi-gemstone designs demand exceptional metallurgical precision and gemological balance. Each earring must balance contrasting mineral hues, refractive indexes, and gemstone cuts to create a cohesive visual symphony rather than an unstructured clash of colors.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>In Indian jewellery traditions, the appreciation for multi-hued adornment is deeply rooted in the Navratna arrangement, an auspicious cosmic setting combining nine sacred gemstones. Contemporary 2026 designs take inspiration from this timeless heritage while embracing modern European aesthetics, including pastel ombré fades, geometric gemstone baguettes, and organic asymmetrical clusters. When set in luminous yellow gold, romantic rose gold, or sleek white gold, these stones catch ambient light from multiple angles, creating a lively illumination around the wearer's face.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>It is equally important to distinguish fine gold multicolor earrings from fashion costume alternatives. While imitation jewellery often relies on resin pastes, synthetic acrylics, and brass platings that deteriorate quickly, fine jewellery utilizes natural or lab-certified precious gemstones set into solid gold mounts. This ensures that the stones retain their internal clarity and color saturation without clouding or peeling over time.</p>
<!-- /wp:paragraph -->""",

    # Section 2
    """<!-- wp:heading -->
<h2 class="wp-block-heading">Popular Silhouettes and Styles: From Daily Studs to Festive Chandeliers</h2>
<!-- /wp:heading -->""",

    """<!-- wp:paragraph -->
<p>Finding the right multicolor earrings begins with choosing a silhouette that complements your facial contours, lifestyle habits, and wardrobe preferences. Designers craft multi-gemstone pieces across five primary architectural formats, each serving a distinct aesthetic purpose:</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Petite Gemstone Studs and Floral Clusters:</strong> Compact button-style studs that sit flush against the earlobe. These designs often feature a central brilliant diamond or pearl encircled by a halo of multi-colored sapphire petals or alternating ruby and emerald points, offering a refined pop of color suitable for professional and daily routines.</li>
<li><strong>Huggie Hoops with Channel-Set Stones:</strong> Small-diameter hoops that closely hug the curve of the earlobe. By setting alternating gemstone baguettes directly into the channel or pave track, huggies provide radiant 360-degree color without protruding edges that could catch on clothing.</li>
<li><strong>Articulated Drop and Dangle Earrings:</strong> Multi-tiered drop designs featuring flexible jump rings between stone segments. As you move, each gemstone reflects light independently, creating fluid kinetic energy that flatters oval and heart-shaped faces.</li>
<li><strong>Modern Geometric Hoops:</strong> Medium-to-large hoops adorned with scattered or bezel-set gemstones along the outer or inner circumference, blending clean contemporary lines with playful vibrancy.</li>
<li><strong>Heritage Jhumkas and Chandelier Showpieces:</strong> Elaborate multi-stone festive earrings featuring tiered canopies, delicate seed pearls, and cascading gem briolettes, designed to pair with traditional Kanjeevarams, lehengas, and bridal attire.</li>
</ul>
<!-- /wp:list -->""",

    """<!-- wp:paragraph -->
<p>Selecting among these silhouettes depends largely on how often you plan to wear the piece. While ornate chandeliers make unforgettable statements during wedding celebrations, versatile huggies and drop earrings transition seamlessly from daytime meetings to intimate dinner gatherings.</p>
<!-- /wp:paragraph -->""",

    # Section 3
    """<!-- wp:heading -->
<h2 class="wp-block-heading">The Lightweight Advantage: Choosing Light Weight Earrings for All-Day Wear</h2>
<!-- /wp:heading -->""",

    """<!-- wp:paragraph -->
<p>One common concern among buyers considering multi-stone jewellery is physical weight. Because multi-gemstone earrings incorporate multiple stones, bezel cups, and gold prongs, poorly engineered pieces can feel heavy, pulling down earlobes and causing discomfort after just a few hours. Fortunately, modern precision casting has made <a href="https://www.bluestone.com/earrings.html">light weight earrings</a> with vibrant multi-stone configurations an accessible reality.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>Modern jewellery artisans achieve featherlight comfort through specialized structural techniques:</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Open-Back Bezel Galleries:</strong> By hollowing out the underlying gold mount behind each stone, craftsmen reduce unnecessary metal bulk while allowing light to enter from behind, enhancing the natural sparkle of each gemstone.</li>
<li><strong>Precision Laser Micro-Prongs:</strong> Replacing heavy metal walls with slender, cold-drawn gold prongs maintains absolute gemstone security while shedding significant gram weight.</li>
<li><strong>Balanced Weight Distribution:</strong> Engineering the center of gravity to align directly with the ear post prevents forward tilting, ensuring the earring sits upright on the earlobe without pulling.</li>
<li><strong>Comfort Weight Benchmarks:</strong> For continuous daily wear, look for total gross earring weights between 2.0 grams and 4.5 grams per pair. Occasional evening drops can comfortably range between 5.0 and 8.0 grams when fitted with wider stabilizing backings.</li>
</ul>
<!-- /wp:list -->""",

    """<!-- wp:paragraph -->
<p>The closure mechanism also plays a crucial role in wearer comfort. While push-back friction nuts provide rapid convenience for petite studs, traditional screw backs and South Indian Bombay screws (Thirupu) offer exceptional security for valuable fine gold pieces, distributing pressure evenly across the lobe tissue.</p>
<!-- /wp:paragraph -->""",

    # IN-BODY IMAGE PLACEHOLDER 1: FLATLAY
    """<!-- IN_BODY_IMAGE_FLATLAY_PLACEHOLDER -->""",

    # Section 4
    """<!-- wp:heading -->
<h2 class="wp-block-heading">Mastering Color Harmony: Practical Styling Rules for Ethnic and Western Outfits</h2>
<!-- /wp:heading -->""",

    """<!-- wp:paragraph -->
<p>Many jewellery lovers hesitate to invest in multicolor earrings because they worry about matching them with diverse wardrobe pieces. However, multicolor jewellery is actually easier to style than monochrome pieces because its varied palette offers multiple anchor points. By applying straightforward color theory principles, you can effortlessly incorporate multicolor earrings into everyday and festive looks.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>Here are four proven styling guidelines recommended by jewellery stylists:</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>The Hero Color Accent Strategy:</strong> Examine your multicolor earrings and identify one dominant gemstone hue (such as the emerald green or ruby red). Match that specific color to a key component of your ensemble, such as your blouse, dupatta border, footwear, or handbag. This creates visual harmony without needing every color to match identically.</li>
<li><strong>The Clean Neutral Canvas:</strong> Allow your earrings to serve as the undisputed focal point by pairing them against monochromatic neutral fabrics. Crisp white linen shirts, charcoal work blazers, ivory raw silk anarkalis, and classic little black dresses provide a pristine backdrop that lets multi-gemstone brilliance take center stage.</li>
<li><strong>Metal Undertone Synergy:</strong> Select the gold base that best complements your skin undertone and clothing palette. Classic 18Kt yellow gold enhances warm earth tones, mustard yellows, and rich maroon ethnic wear. Modern 18Kt rose gold flatters wheatish skin and pastel floral prints, while cool white gold accentuates jewel tones like royal blue, magenta, and emerald.</li>
<li><strong>Curated Ear Stacking Etiquette:</strong> If you have multiple lobe or cartilage piercings, treat your multicolor earring as the anchor piece in the primary lobe piercing. Keep secondary piercings understated by pairing them with delicate plain gold studs, tiny diamond huggies, or simple gold balls to avoid visual clutter.</li>
</ul>
<!-- /wp:list -->""",

    # Section 5
    """<!-- wp:heading -->
<h2 class="wp-block-heading">Evaluating Quality and Craftsmanship: BIS Hallmarking, Gemstone Hardness, and Prongs</h2>
<!-- /wp:heading -->""",

    """<!-- wp:paragraph -->
<p>When investing in fine gold multicolor earrings in India, discerning quality requires looking beyond aesthetic appeal to evaluate metallurgical authenticity, gemstone durability, and setting craftsmanship. Because multi-gemstone pieces incorporate stones of varying physical properties, specialized construction standards are vital.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>Here is an essential quality evaluation checklist for buyers:</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>BIS Hallmarking with 6-Digit HUID:</strong> Under Government of India regulations mandated by the Bureau of Indian Standards, all authentic gold jewellery must feature the triangular BIS logo, the purity mark (such as 750 for 18Kt gold or 585 for 14Kt gold), and an individual 6-digit alphanumeric Hallmark Unique Identification (HUID) code. You can verify this HUID directly on the official BIS Care mobile app before completing your purchase.</li>
<li><strong>18Kt vs 14Kt Metal Alloy Choice:</strong> For fine gemstone earrings, 18Kt and 14Kt gold are the industry gold standards. Pure 24Kt gold is too soft to hold small gemstone prongs securely over years of active wear. 18Kt gold contains 75% pure gold alloyed with strengthening metals, delivering rich golden warmth, while 14Kt gold (58.5% purity) provides enhanced tensile hardness, ideal for intricate micro-pave and everyday drop designs.</li>
<li><strong>Understanding Gemstone Hardness on the Mohs Scale:</strong> Multi-stone earrings often combine minerals of differing scratch resistance. Corundum gems like rubies and sapphires rate at 9 on the Mohs hardness scale, making them exceptionally resilient. Semi-precious stones like tourmalines and amethysts rate between 7 and 7.5, which is durable for regular use. In contrast, organic pearls rate around 3 to 4, requiring protective cup mountings to shield them from abrasive contact.</li>
<li><strong>Prong and Bezel Integrity:</strong> Inspect each stone setting under magnification. Prongs should feel smooth to the touch, gripping the girdle of each gemstone evenly without sharp burs that could catch on clothing. Shared-prong and channel settings must display uniform stone heights and symmetrical alignment.</li>
</ul>
<!-- /wp:list -->""",

    # Section 6: Curated Carousel
    """<!-- wp:heading -->
<h2 class="wp-block-heading">Curated BlueStone Multicolor Earring Highlights</h2>
<!-- /wp:heading -->""",

    carousel_html,

    curated_paragraph,

    # IN-BODY IMAGE PLACEHOLDER 2: LIFESTYLE
    """<!-- IN_BODY_IMAGE_LIFESTYLE_PLACEHOLDER -->""",

    # Section 7
    """<!-- wp:heading -->
<h2 class="wp-block-heading">Cleaning and Long-Term Care: Protecting Multi-Gemstone Settings</h2>
<!-- /wp:heading -->""",

    """<!-- wp:paragraph -->
<p>Maintaining the brilliant luster of multicolor gold earrings requires thoughtful care routines tailored to the most delicate stone in the piece. Because different gemstones react differently to heat, chemicals, and mechanical vibrations, standard single-method cleanings can inadvertently cause damage.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>Follow these expert care recommendations to preserve your earrings:</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Gentle Lukewarm Soaking:</strong> Prepare a bowl of lukewarm water mixed with a few drops of mild, fragrance-free dishwashing liquid. Submerge your earrings for 10 to 15 minutes to loosen daily oils, cosmetics, and dust particles.</li>
<li><strong>Soft-Bristle Detailing:</strong> Use an ultra-soft baby toothbrush to gently clean behind the open-back bezel settings and around prong crowns. Never use stiff nylon brushes or abrasive toothpastes, which can scratch softer stones and dull the polished gold finish.</li>
<li><strong>Rinse and Dry Thoroughly:</strong> Rinse thoroughly under a slow stream of lukewarm running water (ensuring the sink drain is securely plugged). Pat dry using a lint-free microfiber polishing cloth and let the earrings air dry completely on a towel before storage.</li>
<li><strong>Avoid Ultrasonic Machines:</strong> Never place multi-gemstone earrings in ultrasonic or steam cleaning devices. High-frequency sound waves can agitate natural micro-inclusions in emeralds, tourmalines, and pearls, potentially causing fractures or stone loosening.</li>
<li><strong>Individual Compartment Storage:</strong> Store each earring in a dedicated soft velvet pouch or compartmentalized jewellery box. Storing multi-stone pieces loose in a tray allows harder gemstones (like diamonds and sapphires) to scratch neighboring softer gems or polished gold prongs.</li>
</ul>
<!-- /wp:list -->""",

    # Section 8: Final Thoughts / Conclusion (MUST BE BEFORE Related Guides and FAQ!)
    """<!-- wp:heading -->
<h2 class="wp-block-heading">Final Thoughts on Investing in Multicolor Gold Earrings</h2>
<!-- /wp:heading -->""",

    """<!-- wp:paragraph -->
<p>Multicolor earrings are far more than a passing seasonal trend. They represent a joyful, enduring investment in fine jewellery that brings effortless versatility to your wardrobe. By combining certified 18Kt or 14Kt gold, genuine multi-hued gemstones, and ergonomic lightweight craftsmanship, a single pair of multicolor earrings can seamlessly accompany you from casual weekend brunches and corporate boardroom presentations to festive family weddings.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>When building your personal jewellery collection, prioritize certified hallmarking, durable stone settings, and balanced weight engineering. Whether you choose delicate ruby-accented huggies, vibrant tourmaline drops, or regal navratna-inspired hoops, multicolor earrings infuse everyday moments with radiant luxury and timeless individuality.</p>
<!-- /wp:paragraph -->""",

    # Section 9: Related Guides Section (Cluster Links)
    """<!-- wp:heading -->
<h2 class="wp-block-heading">More Jewellery &amp; Buying Guides</h2>
<!-- /wp:heading -->""",

    """<!-- wp:paragraph -->
<p>Expand your fine jewellery expertise with our comprehensive buying and styling resources: learn how to inspect gold hallmarks in our <a href="https://blog.bluestone.com/how-to-check-gold-purity-2026/">Gold Purity Verification Guide</a>, understand statutory taxes in our <a href="https://blog.bluestone.com/gst-on-gold-jewellery-in-india-what-youre-actually-paying-in-tax/">GST on Gold Jewellery Breakdown</a>, discover safety standards when shopping digitally in <a href="https://blog.bluestone.com/is-buying-gold-jewellery-online-safe-in-india-the-honest-answer/">Is Buying Gold Online Safe</a>, ensure perfect wrist proportions with our <a href="https://blog.bluestone.com/bangle-size-2026/">Bangle Size Measuring Guide</a>, and explore traditional enamel craft in our <a href="https://blog.bluestone.com/meenakari-earrings-designs-history-and-styling-tips/">Meenakari Earrings Styling Guide</a>.</p>
<!-- /wp:paragraph -->""",

    # Section 10: Frequently Asked Questions (LAST CONTENT SECTION!)
    """<!-- wp:heading -->
<h2 class="wp-block-heading">Frequently Asked Questions About Multicolor Earrings</h2>
<!-- /wp:heading -->""",

    """<!-- wp:paragraph -->
<p><strong>Q1: What are multicolor earrings in fine jewellery?</strong></p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>Multicolor earrings in fine jewellery are pieces crafted from authentic 18Kt or 14Kt gold that showcase two or more distinct colored gemstones, such as rubies, emeralds, sapphires, amethysts, tourmalines, citrines, or pearls. Unlike fashion costume jewellery made from plated base metals and synthetic resin, fine gold multicolor earrings offer lasting metallurgical integrity, secure gemstone prongs, and certified purity verified by BIS hallmarking.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p><strong>Q2: How do I match multicolor earrings with my outfits?</strong></p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>The most effective styling approach is the Hero Color Accent rule: identify one prominent gemstone color in your earrings and match it directly with a primary shade in your clothing or dupatta. Alternatively, treat multicolor earrings as your sole statement piece by styling them against neutral canvases like ivory raw silk, crisp white linen, charcoal grey, or black, which allows the natural gemstone colors to shine without competing patterns.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p><strong>Q3: Are multicolor gold earrings suitable for everyday office wear?</strong></p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>Yes, multicolor gold earrings are exceptionally well suited for daily office wear when designed in compact silhouettes like huggies, small hoops, or cluster studs. Selecting light weight earrings with flush or bezel stone settings prevents snagging on winter knits or scarves while providing an elegant, professional touch of color to formal workwear.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p><strong>Q4: How do I choose light weight earrings with multiple gemstones?</strong></p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>To find comfortable light weight earrings featuring multiple stones, check the gross gold weight and silhouette architecture. Seek designs utilizing open back bezel galleries or precision CAD laser settings, which reduce unnecessary metal mass while maximizing gemstone light refraction. For all-day comfort, look for pairs weighing between 2.0 and 4.5 grams with secure screw back or Bombay screw closures.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p><strong>Q5: Can I clean multi-gemstone gold earrings in an ultrasonic jewellery cleaner?</strong></p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>No, you should never place multi-gemstone earrings into an ultrasonic cleaner. Different gemstones exhibit widely varying hardness and structural tolerances. While corundum stones like sapphires and rubies can tolerate ultrasonic vibrations, stones like emeralds, tourmalines, and organic pearls can fracture, cloud, or suffer dislodgement from high-frequency sound waves. Clean them safely by soaking in lukewarm water with mild liquid soap and gently scrubbing with a baby-soft brush.</p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p><strong>Q6: How do I verify the authenticity of gold multicolor earrings in India?</strong></p>
<!-- /wp:paragraph -->""",

    """<!-- wp:paragraph -->
<p>Verify authenticity by checking for mandatory BIS hallmarking laser-engraved onto the earring stem or clasp. A genuine hallmark comprises the triangular BIS logo, the gold purity mark (such as 750 for 18Kt or 585 for 14Kt), and a unique 6-digit alphanumeric HUID code that can be verified through the BIS Care mobile application. Additionally, request authentic gemstone and diamond authenticity certification upon purchase.</p>
<!-- /wp:paragraph -->""",

    # Trailing Schema
    schema_html
]

full_content = "\n\n".join(content_parts)

draft_data = {
    "title": "How to Choose and Style Multicolor Earrings: An Informative Jewellery Guide (2026)",
    "slug": "multicolor-earrings-2026",
    "primary_kw": "multicolor earrings",
    "meta_title": "Multicolor Earrings Guide 2026: Styles, Gemstones & Care",
    "meta_desc": "Explore how to choose and style multicolor earrings in fine gold. Learn about multi-gemstone pairings, lightweight comfort, BIS hallmarking, and care in 2026.",
    "author_id": 270271337,
    "categories": [554493348, 554493465],
    "content": full_content
}

out_file = ROOT / "output/Week9_Rank80_draft.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(draft_data, f, indent=2, ensure_ascii=False)

print(f"Draft written to {out_file.name}")
print(f"Content length: {len(full_content)} chars")
# Count visible words
import re
plain_text = re.sub(r"<[^>]+>", " ", full_content)
plain_text = re.sub(r"\{.*?\}", " ", plain_text)
words = len(plain_text.split())
print(f"Approximate visible word count: {words}")
