#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate high-authority, Gutenberg-compliant draft for Week 9 Rank 71 (light-weight-gold-earrings-design-2026)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Load carousel media
carousel_media_path = ROOT / "output" / "week9_rank71_carousel_media.json"
if not carousel_media_path.exists():
    raise FileNotFoundError(f"Missing carousel media at {carousel_media_path}")

with open(carousel_media_path, "r", encoding="utf-8") as f:
    products = json.load(f)

slug = "light-weight-gold-earrings-design-2026"

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
<div class="bs-cf" id="bs-cf-{slug}" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone light weight gold earrings designs">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
    <div class="bs-cf-card is-pos-0" data-index="0">
      <a class="bs-cf-media" href="{products[0]['url']}">
        <img src="{products[0]['src']}" alt="{products[0]['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{products[0]['name']}</div>
        <a class="bs-cf-cta" href="{products[0]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-1" data-index="1">
      <a class="bs-cf-media" href="{products[1]['url']}">
        <img src="{products[1]['src']}" alt="{products[1]['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{products[1]['name']}</div>
        <a class="bs-cf-cta" href="{products[1]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-2" data-index="2">
      <a class="bs-cf-media" href="{products[2]['url']}">
        <img src="{products[2]['src']}" alt="{products[2]['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{products[2]['name']}</div>
        <a class="bs-cf-cta" href="{products[2]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-3" data-index="3">
      <a class="bs-cf-media" href="{products[3]['url']}">
        <img src="{products[3]['src']}" alt="{products[3]['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{products[3]['name']}</div>
        <a class="bs-cf-cta" href="{products[3]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos--2" data-index="4">
      <a class="bs-cf-media" href="{products[4]['url']}">
        <img src="{products[4]['src']}" alt="{products[4]['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{products[4]['name']}</div>
        <a class="bs-cf-cta" href="{products[4]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos--1" data-index="5">
      <a class="bs-cf-media" href="{products[5]['url']}">
        <img src="{products[5]['src']}" alt="{products[5]['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{products[5]['name']}</div>
        <a class="bs-cf-cta" href="{products[5]['url']}">Buy now</a>
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

highlights_p = f"""<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong> Explore signature lightweight earring styles from BlueStone crafted in fine 18K and 14K solid gold, including <a href="{products[0]['url']}">{products[0]['name']}</a>, <a href="{products[1]['url']}">{products[1]['name']}</a>, <a href="{products[2]['url']}">{products[2]['name']}</a>, <a href="{products[3]['url']}">{products[3]['name']}</a>, <a href="{products[4]['url']}">{products[4]['name']}</a>, and <a href="{products[5]['url']}">{products[5]['name']}</a>.</p>
<!-- /wp:paragraph -->"""

schema_json = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "BlogPosting",
            "@id": f"https://blog.bluestone.com/{slug}/#article",
            "isPartOf": {
                "@type": "WebPage",
                "@id": f"https://blog.bluestone.com/{slug}/"
            },
            "headline": "Light Weight Gold Earrings Design: 2026 Daily Wear Guide to Grams, 14K vs 18K Purity & Earlobe Comfort",
            "description": "Explore light weight gold earrings design in 2026. Discover weight ranges under 2g to 4g, 14K vs 18K purity, stud and hoop styles, earlobe comfort, and BIS hallmarking.",
            "datePublished": "2026-09-25T17:00:00+05:30",
            "dateModified": "2026-09-25T17:00:00+05:30",
            "author": {
                "@type": "Person",
                "name": "Satyam",
                "jobTitle": "BlueStone Editorial"
            },
            "publisher": {
                "@type": "Organization",
                "name": "BlueStone",
                "url": "https://www.bluestone.com"
            },
            "mainEntityOfPage": f"https://blog.bluestone.com/{slug}/"
        },
        {
            "@type": "FAQPage",
            "@id": f"https://blog.bluestone.com/{slug}/#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "What is considered a light weight gold earrings design in grams?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "In contemporary Indian jewellery terminology, a light weight gold earrings design typically weighs between 0.8 grams and 3.5 grams per pair. Ultra-light micro-studs often range between 0.8g and 1.5g, everyday huggies and small hoops sit comfortably between 1.5g and 2.5g, while articulated drop earrings and sui dhaga designs remain under 4.0g."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Are 14K or 18K light weight gold earrings durable enough for everyday sleep and shower?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Yes, 14K (58.5% gold) and 18K (75.0% gold) alloys provide high tensile strength and superior hardness compared to 22K gold. The added copper and silver alloys prevent delicate posts and hollow tubes from bending during sleep or daily activities. While removing them before sleep preserves high polish and prevents catching on pillowcases, well-engineered 14K and 18K studs can easily withstand continuous daily wear."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Can light weight gold earrings bend or warp easily?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Lightweight earrings crafted from 22K gold or stamped from thin foil metal can warp under direct pressure because pure gold is naturally malleable. However, modern lightweight gold earrings made with 14K or 18K gold and engineered using computer-aided hollow tubing or precision laser casting maintain structural rigidity, ensuring they resist accidental deformation during routine wear."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Which earring closure is safest for light weight gold earrings?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "For lightweight stud earrings, threaded screw backs and friction push backs with silicone-grip inserts offer the highest retention security. For hoops and huggies, hinged clicker clasps that lock flush into a recessed notch ensure the earring will not catch on scarves, knit sweaters, or telephone handsets."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How is the price of light weight gold earrings calculated under BIS rules?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Under Bureau of Indian Standards (BIS) regulations, pricing is strictly calculated based on net gold weight. The invoice formula multiplies the net weight of gold in grams by the prevailing daily gold rate for the specific karat (14K, 18K, or 22K), adds the manufacturing making charges, and applies a mandatory 3% Goods and Services Tax (GST) across the final total. Gemstones or enamel weights are never billed at the gold rate."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Do lightweight gold earrings carry mandatory BIS HUID hallmarking?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Yes, every authentic gold jewellery item sold in India, regardless of how light it weighs, must carry a laser-engraved 6-digit alphanumeric Hallmark Unique Identification (HUID) code alongside the triangular BIS logo and the karat purity mark (such as 750 for 18K or 585 for 14K). This certification guarantees precious metal purity and provides complete regulatory traceability."
                    }
                }
            ]
        }
    ]
}

schema_html = f"""<!-- wp:html -->
<script type="application/ld+json">
{json.dumps(schema_json, indent=2, ensure_ascii=False)}
</script>
<!-- /wp:html -->"""

content_blocks = [
    "<!-- wp:paragraph -->\n<p><em>By Satyam, BlueStone Editorial</em></p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:paragraph -->\n<p>Finding the ideal balance between precious metal luxury and effortless daily comfort is the driving force behind modern fine jewellery engineering. For decades, traditional Indian gold jewellery celebrated heavy, opulent silhouettes created primarily for grand weddings and seasonal festivals. Yet in contemporary living, women seek fine jewellery that moves seamlessly from morning commutes and corporate boardrooms to evening dinners and casual weekends. This lifestyle shift has propelled light weight gold earrings design into the forefront of personal style, establishing lightweight gold earrings as an indispensable daily luxury.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:paragraph -->\n<p>A masterfully designed pair of light weight gold earrings delivers all the radiant warmth, cultural prestige, and enduring value of genuine gold without the physical strain of heavy earlobe traction. Whether crafted as minimalist geometric studs, fluid sui dhaga threaders, architectural huggies, or feather-light miniature balis, these pieces remain comfortable across ten-to-twelve hour workdays. However, selecting fine gold earrings design light weight requires looking beyond surface aesthetics. Discerning buyers must evaluate gram weight thresholds, precious metal tensile strength, hollow construction integrity, earlobe ergonomics, and transparent billing standards. This comprehensive 2026 buying and educational guide provides the definitive technical and styling roadmap for choosing the perfect light weight gold earrings design.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">Understanding Light Weight Gold Earrings Design: Gram Weight Thresholds from Under 1 Gram to 4 Grams</h2>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>The term lightweight is frequently used across jewellery retail, but precise gram weight classifications are essential for buyers seeking true everyday comfort. In fine jewellery manufacturing, earrings are categorized into distinct weight brackets that directly determine their physical feel, structural behavior, and styling versatility.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:list -->\n<ul class=\"wp-block-list\">\n"
    "<li><strong>Ultra-Light Micro Designs (0.5 Grams to 1.5 Grams per pair):</strong> This category encompasses micro-studs, dainty geometric solitaires, and delicate floral pins. Weighing less than a single sheet of standard printer paper per ear, these pieces exert virtually zero downward pull on the earlobe piercing. They are ideal for second and third lobe piercings, young professionals, students, and individuals with sensitive piercings prone to irritation.</li>\n"
    "<li><strong>Featherlight Everyday Classics (1.5 Grams to 2.5 Grams per pair):</strong> Representing the golden sweet spot for daily wear, this weight tier includes small huggie hoops, curved office balis, and minimalist linear drop earrings. At approximately one gram per earlobe, these designs possess sufficient gold mass to incorporate micro-pave gemstone accents and robust clicker clasps while remaining completely unnoticeable during all-day wear.</li>\n"
    "<li><strong>Structured Lightweight Statement Styles (2.5 Grams to 4.0 Grams per pair):</strong> When you desire dimensional presence, gentle movement, or traditional motifs without heavy earlobe strain, this tier provides the optimal solution. Featuring elongated sui dhaga threaders, filigree drop silhouettes, and textured hollow hoops, these earrings deliver the visual impact of traditional 8-gram jhumkas at less than half the physical weight.</li>\n"
    "</ul>\n<!-- /wp:list -->",
    
    "<!-- wp:paragraph -->\n<p>Understanding these thresholds empowers you to make informed purchases based on your lifestyle needs. If you require jewellery that remains comfortably in place through sleep, telephone calls, and morning workouts, prioritizing earrings under 2.5 grams ensures uninterrupted ease.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- TYPE3_FLATLAY_PLACEHOLDER -->",
    
    "<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">Gold Purity and Structural Durability: Why 14K and 18K Excel in Light Weight Earrings Gold</h2>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>One of the most critical considerations when investing in light weight earrings gold is the selection of precious metal karatage. While 22K gold has long enjoyed cultural reverence in India for investment bullion and traditional bridal ornaments, its high gold content (91.6% pure gold) inherently makes it soft and ductile. In heavy traditional jewellery, structural strength is achieved simply by adding sheer metal thickness. In lightweight jewellery, however, thin 22K gold components can easily bend, warp, or lose their clasp tension under everyday handling.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:paragraph -->\n<p>Modern jewellery houses overcome this physical limitation by utilizing master alloys of 18K and 14K gold for intricate lightweight designs:</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:list -->\n<ul class=\"wp-block-list\">\n"
    "<li><strong>18K Gold (75.0% Pure Gold / 750 Hallmark):</strong> 18K gold represents the quintessential balance of rich golden aesthetic saturation and exceptional mechanical resilience. By alloying 75% pure gold with 25% strengthening metals such as copper and silver, the alloy achieves significantly higher tensile strength and Vickers hardness. This structural integrity allows master artisans to cast ultra-fine prongs, delicate wirework, and secure spring mechanisms that hold their shape indefinitely.</li>\n"
    "<li><strong>14K Gold (58.5% Pure Gold / 585 Hallmark):</strong> 14K gold is the international standard for active, high-durability daily fine jewellery. Containing 58.5% pure gold, it provides superior scratch resistance, rigid structural firmness, and exceptional resistance to bending. For ultra-fine hollow tubes, tension settings, and micro-hinges, 14K gold offers unbeatable durability, ensuring your earrings withstand daily gym sessions, active travel, and continuous wear without deformation.</li>\n"
    "<li><strong>22K Gold (91.6% Pure Gold / 916 Hallmark):</strong> While 22K gold produces unmatched rich yellow luster, its use in lightweight earrings requires careful design curation. In lightweight 22K designs, jewellers rely on domed stamping or solid wire loops rather than intricate openwork, as thin 22K prongs can yield over time.</li>\n"
    "</ul>\n<!-- /wp:list -->",
    
    "<!-- wp:paragraph -->\n<p>For modern working women seeking daily versatility, 18K and 14K gold provide the ultimate combination of luxury, color warmth, and long-term durability, protecting your precious investment against everyday wear and tear.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">Signature Architectures in Gold Earrings Design Light Weight: Studs, Huggies, Sui Dhaga, and Drops</h2>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>A sophisticated gold earrings design light weight relies on clever architectural form to maximize beauty while minimizing gram weight. Designers draw upon four primary silhouettes to deliver comfort, security, and refined style across every occasion.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">1. Minimalist Geometric and Floral Studs</h3>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>Stud earrings represent the ultimate foundational jewellery piece. Resting directly against the earlobe, studs eliminate snagging hazards and provide clean, polished elegance suitable for healthcare professionals, corporate executives, and active mothers. Contemporary lightweight studs feature laser-cut geometric hexagonal silhouettes, organic four-petal clover motifs, and flush-set gemstone accents. By utilizing shallow bezel cups or open gallery settings, craftsmen allow light to illuminate the central motif without adding unnecessary gold backing.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">2. Huggies and Micro Hoops</h3>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>Huggie earrings encircle the earlobe closely, resting snug against the lower rim with zero gap. This tailored contour prevents the earring from catching on headphone bands, winter collars, or mobile phones. Lightweight huggies feature hinged joint engineering with an integrated clicker post that snaps securely into a recessed back channel. Fluted surfaces, micro-twisted rope accents, and channel-set diamonds provide rich dimensional sparkle while maintaining an ultralight profile under two grams.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">3. Sui Dhaga (Threader) Earrings</h3>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>Sui Dhaga earrings, translating poetically to needle and thread, are celebrated across South Asia for their graceful fluidity and minimal mass. A thin, solid gold post guides a flexible micro-curb or box chain smoothly through the earlobe piercing, allowing the chain to drape symmetrically in front and behind the ear. Because threader earrings dispense with heavy solid posts, backings, and bulky hinges, they achieve a dramatic three-to-four centimeter vertical drop at a total weight of only 1.8 to 3.0 grams.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">4. Petite Articulated Dangler and Drop Earrings</h3>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>When transitioning from daytime desk work to celebratory evening dinners, petite drop earrings offer movement and festive brilliance. Unlike traditional heavy danglers that pull downward on the piercing, lightweight drops utilize articulated jump rings and laser-cut hollow charms that dance with head movements while distributing their minimal mass evenly across the earlobe.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->",
    
    "<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">Manufacturing Engineering: How Hollow Tubing, CAD Filigree, and Stamping Maximize Visual Volume</h2>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>Creating a substantial visual presence with featherlight gold requires advanced manufacturing technology. Premium jewellers employ specialized production techniques that allow gold jewellery to look bold and luxurious while remaining featherlight on the ear.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:list -->\n<ul class=\"wp-block-list\">\n"
    "<li><strong>Hollow Tube Extrusion:</strong> In classic hoop and bali designs, solid gold wire would make a medium-sized earring weigh eight grams or more. By extruding gold as a hollow cylinder with precision wall thickness (typically 0.15mm to 0.25mm), jewellers craft voluminous 25mm diameter hoops that weigh less than two grams. When engineered with internal ribbing or proper alloy temper, hollow hoops possess surprising crush resistance during normal daily handling.</li>\n"
    "<li><strong>Computer-Aided Design (CAD) and Laser-Cut Filigree:</strong> Traditional filigree required laborious hand-twisting of gold wires. Modern high-precision laser sintering and CAD openwork create intricate lace-like geometric meshes, honeycomb patterns, and lattice silhouettes. The negative open spaces between gold lines create dramatic visual surface area while reducing metal volume by 40% to 60% compared to solid sheet casting.</li>\n"
    "<li><strong>Electroforming and Precision Stamping:</strong> Electroforming involves depositing micron-thin layers of pure gold onto a conductive wax mandrel in an electrolytic chemical bath. Once the required thickness is reached, the core is melted away, leaving an ultra-light, seam-free, three-dimensional gold shell. Precision hydraulic die-stamping similarly shapes thin gold sheet into rigid domed motifs, delivering bold architectural contours with minimal metal mass.</li>\n"
    "</ul>\n<!-- /wp:list -->",
    
    "<!-- wp:paragraph -->\n<p>These advanced metallurgical techniques ensure that you never have to sacrifice eye-catching design presence to achieve total earlobe comfort.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">Curated BlueStone Light Weight Gold Earrings Highlights</h2>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>To experience the perfect fusion of lightweight comfort and artisanal gold craftsmanship, explore BlueStone's curated collection of fine gold earrings. Each piece is cast in certified 18K or 14K gold, precisely weighted for effortless all-day wear, and fitted with ergonomic, secure closures.</p>\n<!-- /wp:paragraph -->",
    
    carousel_html,
    
    highlights_p,
    
    "<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">Earlobe Ergonomics and Security: Earring Backings, Post Gauges, and Long-Wear Balance</h2>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>A truly exceptional light weight gold earrings design must prioritize earlobe biomechanics and closure security. Even the most stunning earring design becomes frustrating if the post irritates the ear canal or the clasp loosens unexpectedly during an active workday.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">Post Thickness and Gauge Specifications</h3>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>In standard Indian fine jewellery, earring posts are manufactured between 0.75mm and 0.90mm in diameter, corresponding to 19 to 20 gauge thickness. Posts thicker than 1.0mm can stretch or irritate piercing holes, especially on sensitive lobes. Conversely, posts thinner than 0.70mm risk bending when inserted into tight backings. Premium lightweight earrings feature smoothly rounded post tips that glide comfortably through the piercing without scraping delicate internal tissue.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">Closure Mechanisms for Active Daily Wear</h3>\n<!-- /wp:heading -->",
    
    "<!-- wp:list -->\n<ul class=\"wp-block-list\">\n"
    "<li><strong>Friction Push Backs (Butterfly Clasps):</strong> The most common closure for lightweight studs. Modern butterfly backs feature curved tension springs that grip precision grooves along the post. Pairing gold push backs with discreet medical-grade silicone inner sleeves provides dual-action grip, preventing the backing from sliding loose during phone calls or clothing changes.</li>\n"
    "<li><strong>Threaded Screw Backs:</strong> Highly popular across South India, threaded posts require the backing to be screwed clockwise onto threaded ridges. While taking a few extra seconds to put on, screw backs eliminate the risk of accidental loss, making them the gold standard for daily sleep-and-shower studs.</li>\n"
    "<li><strong>South Indian Bombay Screw Backs:</strong> Featuring a smooth tubular sheath that screws over the post, Bombay screws completely enclose the pointed post tip. This prevents the post from poking into the soft skin behind the ear during sleep or phone use.</li>\n"
    "<li><strong>Hinged Clicker Closures:</strong> Standard on huggies and hoops, a curved gold post snaps firmly into a female notch with an audible click. The seamless joint prevents hair from snagging and keeps the earring balanced centered on the lobe.</li>\n"
    "</ul>\n<!-- /wp:list -->",
    
    "<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">Billing Transparency and Authentication: BIS HUID Hallmarking, Net Gold Weight, and 3% GST</h2>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>Purchasing fine gold jewellery in India requires strict adherence to regulatory standards and transparent billing practices. Because lightweight earrings carry relatively low gold mass, understanding invoice breakdowns ensures you receive full value for your investment.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:list -->\n<ul class=\"wp-block-list\">\n"
    "<li><strong>Mandatory BIS Hallmarking with 6-Digit HUID:</strong> Under current Bureau of Indian Standards (BIS) regulations, every piece of gold jewellery sold by registered jewellers in India must carry three distinct laser engravings: the official triangular BIS logo, the karat purity mark (750 for 18K, 585 for 14K, or 916 for 22K), and a unique 6-digit alphanumeric Hallmark Unique Identification (HUID) code. You can verify your HUID code directly on the BIS CARE mobile application to confirm assay centre registration and purity certification.</li>\n"
    "<li><strong>Net Weight vs Gross Weight Billing:</strong> Reputable fine jewellers strictly follow net weight billing. If your lightweight earrings incorporate diamonds, coloured gemstones, or enamel accents, the weight of these non-gold elements must be subtracted completely from the gross weight. You should pay the prevailing gold rate exclusively on the net gold weight.</li>\n"
    "<li><strong>Making Charges Transparency:</strong> Making charges for lightweight jewellery compensate for high-precision CAD modeling, laser cutting, and microscopic stone setting. While making charges on lightweight pieces may represent a slightly higher percentage of total value due to intricate micro-craftsmanship, they must be itemized clearly on the tax invoice.</li>\n"
    "<li><strong>3% GST Compliance:</strong> Under Indian taxation law, a flat 3% Goods and Services Tax (GST) is applied to the combined value of gold and making charges. A legal tax invoice with registered GSTIN and HUID identification guarantees buyback authenticity and exchange validity across India.</li>\n"
    "</ul>\n<!-- /wp:list -->",
    
    "<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">Daily Care, Cleaning, and Storage Guidelines for Delicate Light Weight Gold Earrings</h2>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>Because lightweight gold earrings feature delicate walls, fine wires, and intricate laser openwork, following thoughtful care practices preserves their structural form and radiant shine for decades.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:list -->\n<ul class=\"wp-block-list\">\n"
    "<li><strong>Gentle Lukewarm Soaking:</strong> Everyday cosmetics, shampoo residue, and skin sebum can accumulate behind gemstone settings and inside hollow crevices. Clean your earrings once every fortnight by soaking them in a bowl of lukewarm water mixed with a few drops of gentle, fragrance-free liquid soap for ten minutes. Use an ultra-soft cosmetic brush to clean crevices gently, rinse in clear water, and dry thoroughly on a lint-free cloth.</li>\n"
    "<li><strong>Caution with Ultrasonic Cleaning on Hollow Pieces:</strong> While solid gold studs can safely undergo ultrasonic cleaning, hollow-tube hoops and electroformed designs should avoid high-frequency ultrasonic tanks. The intense vibrational cavitation can force liquid inside micro-drainage holes, which is difficult to dry and can compromise internal structural balance.</li>\n"
    "<li><strong>Individual Compartment Storage:</strong> Avoid tossing delicate earrings into a crowded jewellery box where heavier bangles or chunky rings can press against them. Store lightweight earrings in individual velvet-lined compartments, soft pouches, or on designated earring trees to prevent scratching and post deformation.</li>\n"
    "<li><strong>The Last-On, First-Off Ritual:</strong> Always put your gold earrings on as the final step after applying moisturizer, hairspray, and perfume. Similarly, remove your earrings first before taking off tight sweaters or evening dresses to prevent accidental snagging.</li>\n"
    "</ul>\n<!-- /wp:list -->",
    
    "<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">Final Thoughts on Selecting the Perfect Light Weight Gold Earrings Design</h2>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>Investing in a thoughtfully crafted light weight gold earrings design represents the modern pinnacle of wearable luxury. By combining precious metal value with ergonomic comfort, lightweight gold earrings liberate fine jewellery from safety deposit boxes and festival-only wear, integrating timeless radiance into your everyday journey. By selecting durable 18K or 14K gold alloys, choosing secure backings tailored to your lifestyle, and verifying BIS HUID certification, you acquire an enduring wardrobe staple that brings effortless confidence to every moment.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">More Jewellery &amp; Buying Guides</h2>\n<!-- /wp:heading -->",
    
    "<!-- wp:paragraph -->\n<p>Expand your fine jewellery expertise by exploring our curated companion guides: explore comprehensive earlobe comfort principles in our <a href=\"https://blog.bluestone.com/lightweight-earrings-2026/\">Lightweight Earrings Buying Guide 2026</a>, discover daily stud styling in our <a href=\"https://blog.bluestone.com/gold-stud-earrings-designs-for-daily-use-2026/\">Gold Stud Earrings Designs for Daily Use 2026 Guide</a>, evaluate versatile hoop architectures in our <a href=\"https://blog.bluestone.com/gold-hoop-earrings-for-women-2026/\">Gold Hoop Earrings for Women 2026 Guide</a>, master official hallmark verification with our <a href=\"https://blog.bluestone.com/how-to-check-gold-purity-2026/\">Guide to Checking Gold Purity</a>, and understand invoice transparency through our analysis of <a href=\"https://blog.bluestone.com/gst-on-gold-jewellery-in-india-what-youre-actually-paying-in-tax/\">GST on Gold Jewellery in India</a>.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">Frequently Asked Questions About Light Weight Gold Earrings Design</h2>\n<!-- /wp:heading -->",
    
    "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">What is considered a light weight gold earrings design in grams?</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>In contemporary Indian jewellery terminology, a light weight gold earrings design typically weighs between 0.8 grams and 3.5 grams per pair. Ultra-light micro-studs often range between 0.8g and 1.5g, everyday huggies and small hoops sit comfortably between 1.5g and 2.5g, while articulated drop earrings and sui dhaga designs remain under 4.0g.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">Are 14K or 18K light weight gold earrings durable enough for everyday sleep and shower?</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>Yes, 14K (58.5% gold) and 18K (75.0% gold) alloys provide high tensile strength and superior hardness compared to 22K gold. The added copper and silver alloys prevent delicate posts and hollow tubes from bending during sleep or daily activities. While removing them before sleep preserves high polish and prevents catching on pillowcases, well-engineered 14K and 18K studs can easily withstand continuous daily wear.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">Can light weight gold earrings bend or warp easily?</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>Lightweight earrings crafted from 22K gold or stamped from thin foil metal can warp under direct pressure because pure gold is naturally malleable. However, modern lightweight gold earrings made with 14K or 18K gold and engineered using computer-aided hollow tubing or precision laser casting maintain structural rigidity, ensuring they resist accidental deformation during routine wear.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">Which earring closure is safest for light weight gold earrings?</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>For lightweight stud earrings, threaded screw backs and friction push backs with silicone-grip inserts offer the highest retention security. For hoops and huggies, hinged clicker clasps that lock flush into a recessed notch ensure the earring will not catch on scarves, knit sweaters, or telephone handsets.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">How is the price of light weight gold earrings calculated under BIS rules?</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>Under Bureau of Indian Standards (BIS) regulations, pricing is strictly calculated based on net gold weight. The invoice formula multiplies the net weight of gold in grams by the prevailing daily gold rate for the specific karat (14K, 18K, or 22K), adds the manufacturing making charges, and applies a mandatory 3% Goods and Services Tax (GST) across the final total. Gemstones or enamel weights are never billed at the gold rate.</p>\n<!-- /wp:paragraph -->",
    
    "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">Do lightweight gold earrings carry mandatory BIS HUID hallmarking?</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>Yes, every authentic gold jewellery item sold in India, regardless of how light it weighs, must carry a laser-engraved 6-digit alphanumeric Hallmark Unique Identification (HUID) code alongside the triangular BIS logo and the karat purity mark (such as 750 for 18K or 585 for 14K). This certification guarantees precious metal purity and provides complete regulatory traceability.</p>\n<!-- /wp:paragraph -->",
    
    schema_html
]

full_content = "\n\n".join(content_blocks)

# Count plain text words
import re
plain_text = re.sub(r'<.*?>', ' ', full_content)
words = len(re.findall(r'\b\w+\b', plain_text))

draft_data = {
    "title": "Light Weight Gold Earrings Design: 2026 Daily Wear Guide to Grams, 14K vs 18K Purity & Earlobe Comfort",
    "slug": slug,
    "focus_kw": "light weight gold earrings design",
    "meta_title": "Light Weight Gold Earrings Design 2026: Grams, Purity & Comfort | BlueStone",
    "meta_desc": "Explore light weight gold earrings design in 2026. Discover weight ranges under 2g to 4g, 14K vs 18K purity, stud and hoop styles, earlobe comfort, and BIS hallmarking.",
    "content": full_content,
    "word_count": words
}

output_path = ROOT / "output" / "week9_rank71_draft.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(draft_data, f, indent=2, ensure_ascii=False)

print(f"Draft successfully written to {output_path}")
print(f"Total word count: {words} words")
