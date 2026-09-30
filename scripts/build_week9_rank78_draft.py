#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate complete draft for Week 9 Rank 78."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Load carousel media items
carousel_file = ROOT / "output" / "week9_rank78_carousel_media.json"
with open(carousel_file, "r", encoding="utf-8") as f:
    carousel_items = json.load(f)

# Build 3D Coverflow Carousel Block
cards_html = []
dots_html = []

for i, item in enumerate(carousel_items):
    pos_cls = "is-pos-0"
    if i == 1:
        pos_cls = "is-pos-1"
    elif i == 2:
        pos_cls = "is-pos-2"
    elif i == 3:
        pos_cls = "is-pos-3"
    elif i == 4:
        pos_cls = "is-pos--2"
    elif i == 5:
        pos_cls = "is-pos--1"

    card = f"""    <div class="bs-cf-card {pos_cls}" data-index="{i}">
      <a class="bs-cf-media" href="{item['url']}">
        <img src="{item['src']}" alt="{item['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{item['name']}</div>
        <a class="bs-cf-cta" href="{item['url']}">Buy now</a>
      </div>
    </div>"""
    cards_html.append(card)

    active_cls = " is-active" if i == 0 else ""
    dots_html.append(f'    <button type="button" class="bs-cf-dot{active_cls}" data-i="{i}" aria-label="Product {i+1}"></button>')

cards_block = "\n".join(cards_html)
dots_block = "\n".join(dots_html)

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
<div class="bs-cf" id="bs-cf-indian-gold-earrings-designs-hoops-2026" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone Indian Gold Hoop Earrings Collection">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
{cards_block}
  </div>
  <div class="bs-cf-dots" role="tablist">
{dots_block}
  </div>
</div>
<script>
(function(){{
  var root=document.getElementById('bs-cf-indian-gold-earrings-designs-hoops-2026');
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

# Curated Design Highlights paragraph
curated_para = """<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong> Explore signature handcrafted Indian hoops and modern balis, including <a href="https://www.bluestone.com/earrings/the-rohal-huggie-earrings~21864.html">The Rohal Huggie Earrings</a> with sleek channel accents, <a href="https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html">The Asya Huggie Earrings</a> crafted for everyday earlobe comfort, <a href="https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html">The Ursa Hoop Earrings</a> showcasing architectural diamond pavé contours, <a href="https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html">The Skein Hoop Earrings</a> offering intricate twisted gold wirework, <a href="https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html">The Aleena Huggie Earrings</a> adorned with delicate gemstone accents, and <a href="https://www.bluestone.com/earrings/the-nettile-huggie-earrings~108215.html">The Nettile Huggie Earrings</a> delivering a lavish statement silhouette for celebratory occasions.</p>
<!-- /wp:paragraph -->"""

# Article content blocks
content_parts = []

# Intro and Byline
content_parts.append("""<!-- wp:paragraph -->
<p style="text-align:center;">By Satyam, BlueStone Editorial</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Authentic <strong>indian gold earrings designs hoops</strong> seamlessly unite centuries-old craftsmanship with modern wearable comfort. Known across India as balis, baalis, or kanbalis, Indian gold hoops differ fundamentally from plain Western rings: they incorporate sculptural filigree, crescent contours, floral wirework, and delicate gemstone embellishments. Whether you seek lightweight everyday huggies for workwear or ornate chandbali statement hoops for wedding festivities, choosing the right pair requires balancing gold purity, clasp mechanics, gram weight, and certified hallmarking.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Quick Buying Checklist:</strong> Select 18K or 14K gold for structural strength and secure spring clasp tension in daily hoops, reserving 22K gold for rich yellow traditional balis; verify all three mandatory BIS hallmarks including the 6-digit alphanumeric HUID on the post; prioritize CAD-engineered hollow-tube styles between 2 and 4 grams to protect your earlobes from stretching; and choose hinged click-top saddleback clasps for effortless, snag-free all-day security.</p>
<!-- /wp:paragraph -->""")

# Section 1: Definition & Distinction
content_parts.append("""<!-- wp:heading -->
<h2 class="wp-block-heading">What Defines Authentic Indian Gold Earrings Designs Hoops?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>While Western hoop earrings are predominantly minimalist circular bands with smooth tubular profiles, Indian gold earrings designs hoops are artistic celebrations of cultural heritage. In Indian jewellery traditions, the hoop is rarely a plain circle. Instead, it serves as a structural canvas for master karigars (artisans) who apply classical decorative techniques dating back to the Vedic and Mughal eras.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Traditional Indian balis feature subtle inward or outward tapers, delicate granulation (rava work), openwork lace (jaali or filigree), and hanging accents such as tiny gold beads, pearls, or gemstone drops. Furthermore, regional variations across India bring distinctive design nuances:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>North Indian Baali:</strong> Renowned for delicate wire-wrapped fringes, crescent moon silhouettes, and small dangling jhumki or pearl cluster tassels that catch the light with subtle movement.</li>
<li><strong>South Indian Bali:</strong> Characterized by solid 22K yellow gold architecture, temple-inspired floral motifs, granulated borders, and deeply saturated finishes that complement traditional Kanjeevaram silks.</li>
<li><strong>Contemporary Indo-Western Fusion Hoops:</strong> Engineered with sleek geometric angles, channel-set natural diamonds, and refined ergonomic profiles designed to transition seamlessly from boardroom meetings to festive family dinners.</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Understanding these stylistic roots allows you to select a pair of gold hoops that reflects authentic craftsmanship while fulfilling your personal styling requirements.</p>
<!-- /wp:paragraph -->""")

# Section 2: 5 Iconic Styles
content_parts.append("""<!-- wp:heading -->
<h2 class="wp-block-heading">5 Iconic Styles of Indian Gold Hoop Earrings</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The repertoire of Indian gold hoop earrings encompasses diverse aesthetics, ranging from regal heirloom pieces to feather-light everyday accessories. Exploring these five iconic design styles will help you identify the ideal silhouette for your jewellery collection:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>1. Traditional Chandbali Hoops:</strong> Named after the crescent moon (chand), chandbali hoops combine the curvature of a circular hoop with an intricate crescent-shaped lower tier. Often adorned with micro-pearls or pavé-set gemstones, chandbalis make an unforgettable visual statement at weddings, sangeet ceremonies, and festive celebrations.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>2. Temple Motif Gold Balis:</strong> Deeply rooted in South Indian temple jewellery, these hoops feature sacred symbols such as lotus petals, peacocks, and floral creepers carved into warm 22K gold. The surface often showcases antique matte or nakshi detailing, giving the metal an auspicious heirloom appearance.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>3. Fine Filigree (Jaali) Gold Hoops:</strong> Filigree balis are created by twisting and soldering hair-thin gold wires into mesmerizing lace patterns. Because the interior of the design is largely openwork, filigree hoops achieve significant visual diameter and dimension while maintaining an exceptionally light gram weight.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>4. Huggie Balis for Daily Wear:</strong> Huggies are compact hoops that sit flush against or closely embrace the earlobe. In Indian styling, huggie balis feature textured gold rope borders, milgrain edging, or channel-set diamonds, providing continuous comfort without snagging on dupattas or phone screens.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>5. Textured and Twisted Fusion Hoops:</strong> Modern Indian jewellers create dynamic visual rhythm by twisting multiple gold strands together or applying diamond-cut finishes. These faceted surfaces reflect ambient light brilliantly, producing radiant sparkle without requiring large gemstone settings.</p>
<!-- /wp:paragraph -->""")

# Placeholder 1: Flatlay
content_parts.append("""<!-- TYPE3_FLATLAY_PLACEHOLDER -->""")

# Section 3: Light Weight Gold Earrings & CAD Engineering
content_parts.append("""<!-- wp:heading -->
<h2 class="wp-block-heading">Light Weight Gold Earrings: How CAD and Hollow-Tube Crafting Prevent Earlobe Sagging</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Historically, large Indian gold earrings were notorious for their substantial weight, which often caused piercing elongation, stretched earlobes, and physical discomfort after just a few hours. Today, modern metallurgy and advanced Computer-Aided Design (CAD) have revolutionized <strong>light weight gold earrings</strong>, allowing women to wear striking 25mm to 35mm gold hoops all day with complete ease.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Modern fine jewellers achieve feather-light comfort through specialized engineering techniques:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Precision Hollow-Tube Extrusion:</strong> Advanced electroforming and laser-seamed tubing create a hollow gold core with structurally fortified outer walls. This technique allows a bold, full-bodied 30mm hoop to weigh as little as 2.5 to 3.5 grams, compared to 12 grams for a solid wire equivalent.</li>
<li><strong>Micro-Filigree Laser Sintering:</strong> Computer-guided laser sintering produces delicate openwork filigree that distributes structural tension evenly across the hoop rim, preventing warping while drastically reducing net gold mass.</li>
<li><strong>The 4-Gram Daily Comfort Threshold:</strong> Dermatologists and jewellery ergonomic specialists recommend keeping daily-wear earrings under 3 to 4 grams per ear. Hoops adhering to this standard sit naturally on the earlobe without pulling the piercing downwards or compromising skin elasticity over time.</li>
<li><strong>Weight Distribution Balancing:</strong> Professional CAD modelling places the centre of gravity slightly forward along the vertical axis of the earlobe, ensuring the hoop hangs straight rather than tilting forward or twisting outward.</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>When shopping for lightweight gold earrings, always inspect the piece in person or verify the exact product gram weight in the technical specifications table to ensure long-term wearable comfort.</p>
<!-- /wp:paragraph -->""")

# Section 4: Gold Purity (22K vs 18K vs 14K)
content_parts.append("""<!-- wp:heading -->
<h2 class="wp-block-heading">Gold Purity in Hoops: 22K vs 18K vs 14K for Durability and Spring Tension</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Selecting the appropriate karatage for gold hoop earrings involves more than just color preference; it directly dictates the mechanical durability and longevity of the clasp mechanism. Because hoop earrings rely on flexible tension to snap securely into place, metal hardness is a paramount consideration.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here is how the three primary purity grades perform in Indian gold hoop earrings:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>22K Gold (91.6% Pure Gold):</strong> Celebrated for its rich, luminous marigold-yellow glow, 22K gold is the traditional choice for heirloom Indian jewellery. However, 22 karat gold is naturally soft and ductile. In thin hoops, 22K gold posts can bend under repeated pressure, and clasp hinges may loosen over time. 22K is best suited for solid traditional balis, broad statement cuffs, or occasional festive wear where gentle handling is assured.</li>
<li><strong>18K Gold (75.0% Pure Gold):</strong> The gold standard for fine contemporary jewellery. Blended with copper, silver, or zinc, 18K gold achieves exceptional tensile strength while maintaining a warm, luxurious yellow tone. It provides the necessary spring memory for secure click-top clasps and offers the ideal structural foundation for holding prong-set diamonds and precious gemstones securely.</li>
<li><strong>14K Gold (58.5% Pure Gold):</strong> The most scratch-resistant and mechanically robust alloy for active daily wear. 14K gold retains clasp spring tension flawlessly over thousands of open-and-close cycles, making it the premier choice for sleek everyday huggies, office-wear hoops, and travel jewellery.</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>For most buyers seeking versatile hoops that transition effortlessly between daily routines and celebratory gatherings, 18K yellow gold delivers the optimal equilibrium between authentic color warmth, structural security, and long-term durability.</p>
<!-- /wp:paragraph -->""")

# Section 5: Diameter & Face Shape Guide
content_parts.append("""<!-- wp:heading -->
<h2 class="wp-block-heading">Finding Your Ideal Hoop Diameter and Face Shape Match</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The diameter and profile thickness of a gold hoop dramatically influence your facial symmetry and overall styling presence. Selecting the right size requires understanding both millimeter dimensions and facial geometry:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Millimeter Sizing Breakdown:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>10mm to 15mm (Huggie & Micro-Hoop):</strong> Sits snug against the earlobe. Ideal for workplace attire, second piercings, active lifestyles, and minimalists who prefer understated elegance.</li>
<li><strong>18mm to 25mm (Everyday Classic Hoop):</strong> The most universally versatile size. It frames the jawline gracefully, pairs equally well with crisp linen shirts, salwar suits, and western casuals, and provides noticeable polish without overwhelming your features.</li>
<li><strong>30mm to 45mm (Statement Festive Bali):</strong> Designed for celebratory occasions, festive celebrations, and wedding ensembles. These larger hoops accentuate collarbones and necklines, especially when styled with swept-back hair and open-neck sarees or lehengas.</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>Harmonizing Hoops with Your Face Shape:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Round Face:</strong> Choose oval-shaped hoops, elongated drop balis, or angular geometric hoops. Avoid wide circular hoops that add visual width across the cheeks.</li>
<li><strong>Oval Face:</strong> The most versatile facial profile. Oval shapes can effortlessly carry any diameter, from petite huggies to broad 40mm statement balis.</li>
<li><strong>Square or Angular Face:</strong> Soft, perfectly circular gold hoops with rounded tubular edges beautifully soften a defined jawline and sharp cheekbones.</li>
<li><strong>Heart-Shaped Face:</strong> Select teardrop hoops, bottom-heavy balis, or chandelier-accented hoops that broaden toward the base to balance a narrower chin.</li>
</ul>
<!-- /wp:list -->""")

# Section 6: Clasp Engineering
content_parts.append("""<!-- wp:heading -->
<h2 class="wp-block-heading">Clasp Engineering: Which Gold Hoop Closures Are Safest for Everyday Wear?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Losing an expensive gold earring due to an insecure fastener is every jewellery owner's nightmare. Because hoop earrings are exposed to friction from scarves, sweaters, dupattas, and mobile phones, their closure engineering must be rock-solid.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Evaluate these four common gold hoop clasp mechanisms before finalizing your purchase:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Hinged Click-Top (Saddleback Closure):</strong> The gold post snaps with an audible "click" into a notched U-shaped clasp at the back of the hoop. This is the industry benchmark for security and convenience, offering a smooth outer profile that will not snag on clothing.</li>
<li><strong>Endless (Continuous Wire) Closure:</strong> The post slides directly into the hollow open end of the hoop tube, creating an uninterrupted 360-degree circular aesthetic. While extremely sleek and snag-free, endless clasps require dexterity to put on and take off, and frequent bending of the post can fatigue soft gold over time.</li>
<li><strong>Latch Back (Omega Clip):</strong> Features a hinged lever on the back of the hoop that lifts upward to clamp against the earlobe and post. Latch backs provide exceptional security for heavier gemstone statement hoops by distributing weight across the earlobe surface.</li>
<li><strong>South Indian Wire-Tuck Bali Clasp:</strong> A traditional curved gold wire that passes through the earlobe and hooks into a tiny welded loop or ball behind the ear. Highly traditional and reliable, though it requires gentle handling to prevent deforming the wire curve.</li>
</ul>
<!-- /wp:list -->""")

# Placeholder 2: Lifestyle
content_parts.append("""<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->""")

# Section 7: BIS Hallmarking & Net Weight Billing
content_parts.append("""<!-- wp:heading -->
<h2 class="wp-block-heading">BIS Hallmarking and Net Weight Rules: Protecting Your Gold Hoop Investment</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Purchasing authentic gold jewellery in India requires strict adherence to legal consumer protection standards established by the Bureau of Indian Standards (BIS) and the Ministry of Consumer Affairs. Never buy unhallmarked gold jewellery under any circumstances.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>The 3 Mandatory BIS Hallmarks:</strong> Under current Indian regulations, every hallmarked gold article must feature exactly three laser-etched stamps, typically engraved on the inner curve of the hoop or the post:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>1. The BIS Triangular Logo:</strong> Verifies that the piece has been scientifically tested and certified by a BIS-licensed Assaying and Hallmarking Centre (AHC).</li>
<li><strong>2. The Purity and Fineness Mark:</strong> Specifies the exact gold content, such as 22K916 (91.6% pure), 18K750 (75.0% pure), or 14K585 (58.5% pure).</li>
<li><strong>3. The 6-Digit Alphanumeric HUID:</strong> The Hallmark Unique Identification code (e.g., AB12CD). This code functions as an immutable digital certificate. By typing this 6-digit code into the official government <strong>BIS CARE app</strong> under the "Verify HUID" tab, you can instantly confirm the jeweller's registration, assaying date, article type, and certified purity grade.</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>The Net Weight Billing Rule:</strong> Indian law strictly mandates that customers must only pay for the net weight of gold. If your hoop earrings feature diamonds, coloured gemstones, enamel, or internal structural cores, the weight of these non-gold elements must be subtracted from the gross weight on your tax invoice. You must never pay the per-gram gold rate for gemstones or decorative lacquer.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Always demand an itemized invoice that clearly delineates net gold weight, purity grade, gemstone caratage, making charges, and the applicable 3% Goods and Services Tax (GST).</p>
<!-- /wp:paragraph -->""")

# Section 8: Care & Maintenance
content_parts.append("""<!-- wp:heading -->
<h2 class="wp-block-heading">Daily Care and Earlobe Comfort: Sleeping, Cleaning, and Storing Gold Hoops</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Maintaining the luster, hygiene, and clasp integrity of your gold hoop earrings requires simple yet consistent care habits:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Never Sleep in Medium or Large Hoops:</strong> While small huggies under 12mm can often be worn overnight safely, hoops larger than 15mm can easily catch on pillowcases or bedsheets during sleep. The lateral torque exerted while tossing and turning can bend the hinge pin or tear delicate earlobe tissue.</li>
<li><strong>The "Last On, First Off" Rule:</strong> Put your gold earrings on only after you have completed applying hairspray, perfumes, body lotions, and makeup. The chemical aerosols and oils in cosmetic products create a cloudy film on polished gold and diamonds.</li>
<li><strong>Gentle Home Cleaning:</strong> Soak your gold hoops in a bowl of lukewarm water mixed with a few drops of mild, chemical-free dishwashing liquid for ten minutes. Use an extra-soft baby toothbrush to gently dislodge skin oils and dust behind the hinge and clasp groove. Rinse thoroughly under warm running water and pat dry with a lint-free microfiber cloth.</li>
<li><strong>Individual Compartment Storage:</strong> Gold is a malleable metal susceptible to surface abrasions. Store each pair of hoops in individual velvet pouches or separate compartments within your jewellery box to prevent them from scratching against harder diamond rings or metal bangles.</li>
</ul>
<!-- /wp:list -->""")

# Section 9: Signature Designs Carousel
content_parts.append("""<!-- wp:heading -->
<h2 class="wp-block-heading">Discover Signature Gold Hoop and Bali Designs</h2>
<!-- /wp:heading -->

""" + carousel_html + "\n\n" + curated_para)

# Section 10: Conclusion
content_parts.append("""<!-- wp:heading -->
<h2 class="wp-block-heading">Final Thoughts: Choosing Timeless Indian Gold Hoops</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Indian gold hoop earrings remain one of the most rewarding and timeless additions to any fine jewellery collection. By blending centuries of artisan craftsmanship with precision CAD engineering, modern designs provide the regal beauty of traditional balis without the cumbersome weight of the past.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When selecting your ideal pair, prioritize certified BIS 3-part hallmarking with HUID verification, choose 18K gold for dependable clasp spring performance, and verify that the gram weight aligns with your earlobe comfort needs. With proper selection and mindful daily care, a well-crafted pair of Indian gold hoops will bring radiant elegance to your wardrobe for decades to come.</p>
<!-- /wp:paragraph -->""")

# Section 11: Internal Linking
content_parts.append("""<!-- wp:heading -->
<h2 class="wp-block-heading">More Jewellery &amp; Buying Guides</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Deepen your fine jewellery expertise with our comprehensive collection of expert buying guides. Learn how to verify hallmark purity stamps in our <a href="https://blog.bluestone.com/how-to-check-gold-purity-2026/">guide to checking gold purity</a>, understand invoice calculations and tax rates through our breakdown of <a href="https://blog.bluestone.com/gst-on-gold-jewellery-in-india-what-youre-actually-paying-in-tax/">GST on gold jewellery in India</a>, explore contemporary styling ideas in our curated <a href="https://blog.bluestone.com/gold-hoop-earrings-for-women-2026/">gold hoop earrings for women guide</a>, discover feather-light daily essentials in our <a href="https://blog.bluestone.com/lightweight-earrings-2026/">lightweight earrings buying guide</a>, and discover gemstone setting criteria in our <a href="https://blog.bluestone.com/ruby-earrings-2026/">ruby earrings buying guide</a>.</p>
<!-- /wp:paragraph -->""")

# Section 12: FAQs
content_parts.append("""<!-- wp:heading -->
<h2 class="wp-block-heading">Frequently Asked Questions about Indian Gold Hoop Earrings</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>What is the difference between Western hoop earrings and Indian gold balis?</strong><br/>While Western hoops typically feature plain, minimalist circular tubing, Indian gold balis incorporate cultural artisan detailing such as crescent chandbali silhouettes, temple engravings, delicate wire filigree (jaali work), rava granulation, and dangling accents like pearls or gold beads.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Are gold hoop earrings suitable for daily wear?</strong><br/>Yes, gold hoop earrings are exceptionally well suited for daily wear, provided you choose compact huggies or lightweight hoops between 12mm and 20mm in diameter. Opt for 18K or 14K gold with secure click-top clasps to ensure durability, comfort, and snag resistance.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>What is the ideal weight in grams for lightweight gold hoop earrings?</strong><br/>For daily, all-day comfort without earlobe stretching, lightweight gold hoop earrings should ideally weigh between 2 and 4 grams per pair. Modern CAD-engineered hollow-tube construction allows hoops to achieve bold visual dimensions while staying feather-light.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Which gold purity is best for Indian gold hoop earrings: 18K or 22K?</strong><br/>For hoops with functional snap clasps, spring tension hinges, or diamond pavé settings, 18K gold is superior because of its tensile strength and resistance to bending. 22K gold is softer and best reserved for solid traditional balis worn on special festive occasions.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>How can I verify if my Indian gold hoop earrings are authentic?</strong><br/>Always inspect the jewellery for the three mandatory BIS hallmarks: the triangular BIS logo, the purity grade (e.g., 22K916 or 18K750), and the 6-digit alphanumeric HUID code. You can verify the HUID code directly on the government BIS CARE mobile app.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Can I sleep wearing gold hoop earrings?</strong><br/>You can comfortably sleep in tiny, smooth huggie hoops under 12mm that fit snugly against the earlobe. However, hoops larger than 15mm should always be removed before bed to prevent bent posts, distorted clasps, or painful earlobe tugging during sleep.</p>
<!-- /wp:paragraph -->""")

# Section 13: JSON-LD Schemas
faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "What is the difference between Western hoop earrings and Indian gold balis?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "While Western hoops typically feature plain, minimalist circular tubing, Indian gold balis incorporate cultural artisan detailing such as crescent chandbali silhouettes, temple engravings, delicate wire filigree (jaali work), rava granulation, and dangling accents like pearls or gold beads."
            }
        },
        {
            "@type": "Question",
            "name": "Are gold hoop earrings suitable for daily wear?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes, gold hoop earrings are exceptionally well suited for daily wear, provided you choose compact huggies or lightweight hoops between 12mm and 20mm in diameter. Opt for 18K or 14K gold with secure click-top clasps to ensure durability, comfort, and snag resistance."
            }
        },
        {
            "@type": "Question",
            "name": "What is the ideal weight in grams for lightweight gold hoop earrings?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "For daily, all-day comfort without earlobe stretching, lightweight gold hoop earrings should ideally weigh between 2 and 4 grams per pair. Modern CAD-engineered hollow-tube construction allows hoops to achieve bold visual dimensions while staying feather-light."
            }
        },
        {
            "@type": "Question",
            "name": "Which gold purity is best for Indian gold hoop earrings: 18K or 22K?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "For hoops with functional snap clasps, spring tension hinges, or diamond pavé settings, 18K gold is superior because of its tensile strength and resistance to bending. 22K gold is softer and best reserved for solid traditional balis worn on special festive occasions."
            }
        },
        {
            "@type": "Question",
            "name": "How can I verify if my Indian gold hoop earrings are authentic?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Always inspect the jewellery for the three mandatory BIS hallmarks: the triangular BIS logo, the purity grade (e.g., 22K916 or 18K750), and the 6-digit alphanumeric HUID code. You can verify the HUID code directly on the government BIS CARE mobile app."
            }
        },
        {
            "@type": "Question",
            "name": "Can I sleep wearing gold hoop earrings?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "You can comfortably sleep in tiny, smooth huggie hoops under 12mm that fit snugly against the earlobe. However, hoops larger than 15mm should always be removed before bed to prevent bent posts, distorted clasps, or painful earlobe tugging during sleep."
            }
        }
    ]
}

blog_posting_schema = {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "How to Choose and Style Indian Gold Earrings Designs Hoops: The 2026 Jewellery Guide",
    "description": "Explore Indian gold earrings designs hoops in 2026. Discover traditional balis, lightweight gold hoop designs, 18K vs 22K purity, secure clasps, and BIS hallmarking.",
    "author": {
        "@type": "Person",
        "name": "Satyam",
        "url": "https://blog.bluestone.com"
    },
    "publisher": {
        "@type": "Organization",
        "name": "BlueStone",
        "url": "https://www.bluestone.com",
        "logo": {
            "@type": "ImageObject",
            "url": "https://www.bluestone.com/assets/images/logo.png"
        }
    },
    "datePublished": "2026-09-26T17:15:00+05:30",
    "dateModified": "2026-09-26T17:15:00+05:30",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://blog.bluestone.com/indian-gold-earrings-designs-hoops-2026/"
    },
    "keywords": [
        "indian gold earrings designs hoops",
        "light weight gold earrings",
        "gold hoop earrings",
        "gold balis",
        "chandbali hoops",
        "18k gold hoops",
        "BIS hallmark gold hoops"
    ]
}

schema_html = f"""<!-- wp:html -->
<script type="application/ld+json">
{json.dumps(faq_schema, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(blog_posting_schema, indent=2)}
</script>
<!-- /wp:html -->"""

content_parts.append(schema_html)

full_content = "\n\n".join(content_parts)

# Verify no em dashes, en dashes, or spaced hyphens in prose
prose_only = re.sub(r"<style[^>]*>.*?</style>", "", full_content, flags=re.I|re.S)
prose_only = re.sub(r"<script[^>]*>.*?</script>", "", prose_only, flags=re.I|re.S)

bad_chars = ["\u2014", "\u2013"]
for bc in bad_chars:
    if bc in full_content:
        raise ValueError(f"Prohibited character found in content: {repr(bc)}")
if " - " in prose_only:
    raise ValueError("Prohibited spaced hyphen ' - ' found in prose content!")

# Verify no raw HTML table
if "<table" in full_content or "<!-- wp:table" in full_content:
    raise ValueError("Prohibited HTML table block found in content!")

# Verify word count
words = re.findall(r"\b\w+\b", re.sub(r"<[^>]+>", " ", full_content))
word_count = len(words)
print(f"Generated draft word count: {word_count} words")

draft_data = {
    "rank": 78,
    "title": "How to Choose and Style Indian Gold Earrings Designs Hoops: The 2026 Jewellery Guide",
    "slug": "indian-gold-earrings-designs-hoops-2026",
    "primary_kw": "indian gold earrings designs hoops",
    "supporting_kws": ["light weight gold earrings"],
    "meta_title": "Indian Gold Earrings Designs Hoops: 2026 Buying & Styling Guide",
    "meta_desc": "Explore Indian gold earrings designs hoops in 2026. Discover traditional balis, lightweight gold hoop designs, 18K vs 22K purity, secure clasps, and BIS hallmarking.",
    "author_id": 270271337,
    "author_name": "Satyam",
    "categories": [554493348, 554493465],
    "word_count": word_count,
    "content": full_content
}

out_draft = ROOT / "output" / "Week9_Rank78_draft.json"
out_draft.write_text(json.dumps(draft_data, indent=2), encoding="utf-8")
print(f"Draft written to {out_draft}")
