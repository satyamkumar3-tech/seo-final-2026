#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Draft generation script for Week 9 Rank 66: Garba Jewellery 2026."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Load carousel media
carousel_media_path = ROOT / "output" / "week9_rank66_carousel_media.json"
with open(carousel_media_path, "r", encoding="utf-8") as f:
    carousel_products = json.load(f)

# Build Carousel HTML from template
template_path = ROOT / "templates" / "eid_carousel_6_snippet.html"
tmpl = template_path.read_text(encoding="utf-8")

# Replace container ID and label
tmpl = tmpl.replace('id="bs-cf-eid"', 'id="bs-cf-garba-jewellery-2026"')
tmpl = tmpl.replace("document.getElementById('bs-cf-eid')", "document.getElementById('bs-cf-garba-jewellery-2026')")
tmpl = tmpl.replace('aria-label="BlueStone Eid gift ideas"', 'aria-label="BlueStone Garba jewellery designs"')

# Build the 6 cards HTML exactly
cards_html = []
pos_classes = ["is-pos-0", "is-pos-1", "is-pos-2", "is-pos-3", "is-pos--2", "is-pos--1"]
for idx, (p, pos) in enumerate(zip(carousel_products, pos_classes)):
    card = f"""    <div class="bs-cf-card {pos}" data-index="{idx}">
      <a class="bs-cf-media" href="{p['url']}">
        <img src="{p['src']}" alt="{p['alt']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{p['name']}</div>
        <a class="bs-cf-cta" href="{p['url']}">Buy now</a>
      </div>
    </div>"""
    cards_html.append(card)

cards_block = "\n".join(cards_html)

# Replace the stage contents in template
stage_pattern = re.compile(r'<div class="bs-cf-stage">.*?</div>\s*<div class="bs-cf-dots"', re.DOTALL)
new_stage = f'<div class="bs-cf-stage">\n{cards_block}\n  </div>\n  <div class="bs-cf-dots"'
carousel_html = stage_pattern.sub(new_stage, tmpl)

content_blocks = [
    # Byline
    '<!-- wp:paragraph -->\n<p>By Satyam, BlueStone Editorial</p>\n<!-- /wp:paragraph -->',
    
    # Intro
    '<!-- wp:paragraph -->\n<p>Navratri is a festival defined by kinetic energy, devotional reverence, and celebratory joy. Across nine vibrant autumn nights, dancers gather to immerse themselves in Garba and Dandiya Raas, moving in synchronized circles to swirling rhythms, percussive dhol beats, and clapping sequences. Yet beneath the radiant mirror-work chaniya cholis and swirling dupattas lies an essential styling challenge: finding authentic, dance-proof garba jewellery that delivers opulent festive drama without pulling, catching, or slipping during intense physical motion.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p>For decades, many festive participants turned to heavy oxidised imitation pieces or costume trinkets. However, modern jewellery connoisseurs increasingly seek the lasting elegance, skin safety, and real investment value of fine gold and precious gemstone jewelry. Fine jewellery brings hallmarked authenticity, hypoallergenic purity, and heirloom craftsmanship to festive celebrations. When you invest in genuine 18kt and 22kt gold jewellery, you acquire versatile adornments that gracefully transition from festive circular dance grounds to Diwali dinners, wedding ceremonies, and milestone celebrations for generations to come.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p><strong>Quick Buyer Guide &amp; Key Takeaways:</strong> Dance-proof garba jewellery requires four foundational principles: lightweight ergonomic engineering (under 10 grams for earrings to protect earlobes), ultra-secure mechanical fastenings (threaded Bombay screw-backs for studs and hoops, double-safety latch box catches for wristwear), snag-free stone settings (smooth bezel and channel settings that will not snare silk threads or mirrors), and certified <a href="https://blog.bluestone.com/how-to-check-gold-purity-2026/">BIS-hallmarked gold purity</a>. Balancing festive visual impact with structural integrity ensures you twirl with total peace of mind.</p>\n<!-- /wp:paragraph -->',

    # Section 1
    '<!-- wp:heading {"level":2} -->\n<h2>Quick Buyer Guide: What Makes Jewellery Truly Dance-Proof for Garba 2026?</h2>\n<!-- /wp:heading -->',

    '<!-- wp:paragraph -->\n<p>Dancing Garba is unlike attending a seated formal gala or a calm wedding reception. During a typical two-hour session, a dancer executes hundreds of high-speed pirouettes, sudden direction changes, and energetic overhead clapping motions. This vigorous physical activity subjects jewellery to dynamic centrifugal forces, moisture from perspiration, and repetitive contact with fabric and wooden dandiya sticks. Choosing standard occasion jewellery without verifying its physical resilience often leads to detached clasps, stretched earlobes, or lost ornaments.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p>To ensure your fine jewellery remains safe, comfortable, and pristine throughout the nine nights, keep these core engineering criteria in mind:</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:list -->\n<ul class="wp-block-list">\n<li><strong>Ergonomic Weight Balancing:</strong> Excessive weight pulls delicate earlobes down and turns wrist bangles into bruised contact points. Prioritize lightweight hollow-form gold construction, electroformed contours, and tapered silhouettes that preserve substantial visual volume while remaining exceptionally light against the body.</li>\n<li><strong>Mechanical Fastener Integrity:</strong> Friction-based push backs (butterfly backs) and open s-hooks are prone to slipping loose when subjected to perspiration and rapid spins. Seek out threaded screw-back posts, click-shut huggie mechanisms, and multi-hinged clasps equipped with secondary wire safety catches.</li>\n<li><strong>Smooth, Rubover Setting Profiles:</strong> Mirror-work lehengas, resham embroidery, and delicate tissue dupattas easily catch on sharp, elevated claws. Choosing bezel-set gems, flush-set pavé diamonds, or rubover gemstone cups ensures your attire glides smoothly across the jewellery surface without catching.</li>\n<li><strong>Hypoallergenic Gold Metallurgy:</strong> Perspiration combined with non-precious base metals such as nickel, brass, or copper causes green oxidation marks, painful chafing, and allergic contact dermatitis. Certified 18kt and 22kt fine gold from reputed jewellers like BlueStone remains non-reactive, soothing, and skin-safe across hours of perspiration.</li>\n</ul>\n<!-- /wp:list -->',

    # Section 2
    '<!-- wp:heading {"level":2} -->\n<h2>Essential Garba Jewellery Checklist: Weight, Comfort, and Movement Dynamics</h2>\n<!-- /wp:heading -->',

    '<!-- wp:paragraph -->\n<p>Before stepping onto the dance arena, every jewellery ensemble should pass a deliberate physical movement check. Understanding how different jewellery weights interact with your body allows you to curate an ensemble that accentuates your grace without causing physical exhaustion.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:list -->\n<ul class="wp-block-list">\n<li><strong>Earrings (Target: Under 8 to 10 Grams Per Pair):</strong> Earlobes have no bone or cartilage support. Heavy chandelier earrings swing with momentum during pirouettes, causing painful micro-tears. Opt for contoured hoop earrings or huggies that sit close to the lobe, distributing mass evenly along the natural ear contour.</li>\n<li><strong>Bangles and Kadas (Target: Contoured Oval Architecture):</strong> Traditional round bangles slide freely up and down the forearm, colliding aggressively during dandiya strikes. Contoured oval bangles with secure side clasps match the anatomical cross-section of your wrist, preventing uncomfortable friction.</li>\n<li><strong>Neckpieces (Target: Snug Collarbone Placement):</strong> Long, free-swinging sautoirs or multiple loose chains are prone to tangling in wooden dandiya sticks or snagging on dupattas. Select structured chokers, princess-length necklaces (16 to 18 inches), or layered necklaces anchored with secure central bails.</li>\n<li><strong>Rings (Target: Comfort-Fit Inner Curves):</strong> Avoid high-domed cocktail rings with sharp edges that can scratch your dance partner during synchronized clapping. Choose smooth band rings with rounded comfort-fit interiors that sit comfortably across the knuckles.</li>\n</ul>\n<!-- /wp:list -->',

    '<!-- wp:paragraph -->\n<p><strong>The Pre-Festive Movement Test:</strong> Wear your chosen jewellery pieces at home with your planned hairstyle. Perform three full spins, clap your hands firmly overhead ten times, and gently shake your head side-to-side. If any piece shifts position, pulls painfully on skin, or rattles loosely, adjust the clasp tension or select a more streamlined alternative before the event begins.</p>\n<!-- /wp:paragraph -->',

    # Carousel Block
    carousel_html,

    # Curated Highlights (Single paragraph only)
    '<!-- wp:paragraph -->\n<p><strong>Curated Design Highlights:</strong> Explore signature festive creations engineered for dance and elegance, from the sculptural radiance of <a href="https://www.bluestone.com/bangles/the-muricelle-bangle~1001.html">The Muricelle Bangle</a> and the feather-light security of <a href="https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html">The Skein Hoop Earrings</a> to the layered charm of <a href="https://www.bluestone.com/necklaces/the-ailia-evil-eye-layered-necklace~116379.html">The Ailia Evil Eye Layered Necklace</a>, the oval ergonomics of <a href="https://www.bluestone.com/bangles/the-tarentella-oval-bangle~31547.html">The Tarentella Oval Bangle</a>, the close-fit grip of <a href="https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html">The Ursa Hoop Earrings</a>, and the floral festive glow of <a href="https://www.bluestone.com/pendants/the-teshvarya-pendant~173771.html">The Teshvarya Pendant</a>.</p>\n<!-- /wp:paragraph -->',

    # Section 3
    '<!-- wp:heading {"level":2} -->\n<h2>Category Breakdown: Choosing Necklaces, Earrings, and Bangles for High-Energy Dance</h2>\n<!-- /wp:heading -->',

    '<!-- wp:paragraph -->\n<p>Curating a harmonious festive look requires matching the functional anatomy of each jewellery category to the energetic nature of Garba dance styles. Here is how to select the ideal silhouettes across every key adornment category.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p><strong>Earrings: Hoop Earrings and Huggies Over Loose Chandbalis</strong><br/>Earrings serve as the primary facial frame in festive photography, capturing light with every turn of the head. While traditional oversized jhumkas look magnificent in still portraits, their dangling bells and bell-shaped domes swing uncontrollably during rapid spinning. Sculptural hoop earrings like <a href="https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html">The Skein Hoop Earrings</a> or broad huggie hoops like <a href="https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html">The Ursa Hoop Earrings</a> deliver dramatic golden shimmer while hugging the lobe securely. Their self-contained geometry eliminates snagging risks, allowing you to dance through the night without discomfort.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p><strong>Wristwear: Ergonomic Hinged Bangles Over Loose Stacks</strong><br/>Garba clapping requires unrestricted forearm mobility. When you wear dozens of loose, unfastened glass or lightweight metal bangles, they slide toward the elbow during raised-arm sequences and crash together with painful force during dandiya strikes. Sturdy, hallmarked gold hinged bangles such as <a href="https://www.bluestone.com/bangles/the-muricelle-bangle~1001.html">The Muricelle Bangle</a> and <a href="https://www.bluestone.com/bangles/the-tarentella-oval-bangle~31547.html">The Tarentella Oval Bangle</a> stay anchored precisely at the wrist. To find your exact measurement before ordering, consult our detailed <a href="https://blog.bluestone.com/bangle-size-2026/">bangle size guide</a> to ensure a slip-proof fit.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p><strong>Neckwear: Structured Chokers and Fixed-Bail Pendants</strong><br/>A neckline adorned with multiple free-floating delicate chains invites disaster during communal dancing, where dangling pendants can catch on a partner\'s dandiya stick. Instead, choose a layered necklace with fixed spacer bars like <a href="https://www.bluestone.com/necklaces/the-ailia-evil-eye-layered-necklace~116379.html">The Ailia Evil Eye Layered Necklace</a> or an articulated floral pendant like <a href="https://www.bluestone.com/pendants/the-teshvarya-pendant~173771.html">The Teshvarya Pendant</a> suspended from a sturdy gold chain. These designs remain centred against the sternum, catching stage lighting without shifting awkwardly.</p>\n<!-- /wp:paragraph -->',

    '<!-- TYPE3_FLATLAY_PLACEHOLDER -->',

    # Section 4
    '<!-- wp:heading {"level":2} -->\n<h2>Styling Gemstone Jewelry with Vibrant Navratri Attire</h2>\n<!-- /wp:heading -->',

    '<!-- wp:paragraph -->\n<p>Navratri is deeply rooted in colour symbolism, with each of the nine sacred nights dedicated to a distinct manifestation of Goddess Durga. Incorporating authentic fine gemstone jewelry allows you to honour these traditional colour codes while elevating hand-embroidered kutch-work, bandhani, and patola silhouettes with vibrant, natural brilliance.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p>Natural precious and semi-precious gemstones offer vivid hues that perfectly mirror the daily festival palette:</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:list -->\n<ul class="wp-block-list">\n<li><strong>Pratipada (Yellow) &amp; Chaturthi (Orange):</strong> Sunny citrines, glowing imperial topazes, and yellow sapphires set in 18kt yellow gold mirror the auspicious warmth of turmeric and marigold blossoms.</li>\n<li><strong>Dwitiya (Green):</strong> Deep green emeralds, peridots, and green tourmalines provide lush, aristocratic contrast against rich crimson and rani pink cholis.</li>\n<li><strong>Tritiya (Grey) &amp; Panchami (White):</strong> Lustrous south sea pearls, iridescent moonstones, and natural brilliant-cut diamonds introduce ethereal sophistication against slate-grey, pearl-white, or ivory raw silk lehengas.</li>\n<li><strong>Shashti (Red) &amp; Ashtami (Pink):</strong> Fiery rubies, pink sapphires, and rhodolite garnets amplify traditional sindoor-red bandhani dupattas with timeless regal majesty.</li>\n<li><strong>Saptami (Royal Blue) &amp; Navami (Purple):</strong> Deep blue sapphires, tanzanites, and vibrant amethysts create breathtaking tonal depth against peacock blue, royal purple, and midnight indigo outfits.</li>\n</ul>\n<!-- /wp:list -->',

    '<!-- wp:paragraph -->\n<p><strong>Gemstone Setting Security for Active Dancers:</strong> When wearing gemstone jewelry during active festive dancing, the setting architecture is paramount. While multi-prong claw settings elevate gemstones for maximum light entry in formal evening rings, high prongs can snag on mirrored embroidery or loosen if struck by a dandiya. Look for protective bezel cups, channel channels, or semi-bezel borders certified to standard hardness metrics by authorities like the <a href="https://www.gia.edu/">Gemological Institute of America</a>. Smooth bezel metal borders shield gemstone girdles from accidental edge chipping, keeping your precious gems secure through hours of enthusiastic celebration.</p>\n<!-- /wp:paragraph -->',

    '<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->',

    # Section 5
    '<!-- wp:heading {"level":2} -->\n<h2>Clasp and Setting Security: Protecting Fine Gold from Snags and Impact</h2>\n<!-- /wp:heading -->',

    '<!-- wp:paragraph -->\n<p>The difference between a cherished heirloom that lasts for decades and a piece lost on a crowded festival ground comes down to mechanical security. High-quality fine jewellery incorporates specialized clasp engineering designed to withstand movement and accidental pulling. Understanding these closures ensures you make informed buying decisions.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:list -->\n<ul class="wp-block-list">\n<li><strong>Threaded Bombay Screw-Backs:</strong> Widely recognized as the gold standard for Indian festive earrings, threaded screw posts feature spiral grooves that require several deliberate rotations to fasten. Unlike friction push-backs that loosen when coated with sweat or hairspray, threaded screws remain locked until physically unthreaded.</li>\n<li><strong>Hinged Snap-Bars and Saddle Clasps:</strong> Common on premium hoop earrings, these feature a curved metal post that clicks firmly into a notched cradle. A reassuring audible "click" confirms the closure is engaged, ensuring the hoop cannot slip open during spins.</li>\n<li><strong>Box Clasps with Figure-Eight Safety Latches:</strong> The preferred closure for structured kadas and heavy tennis bracelets. The tongue clicks into the main box housing, and an external hinged wire arm swings over an exterior peg, providing secondary mechanical locking even if the primary tongue release is accidentally pressed.</li>\n<li><strong>Heavy-Gauge Lobster Claw Clasps:</strong> Standard spring rings are notoriously fragile and difficult to operate. Heavy-gauge solid gold lobster claws feature thicker internal steel springs and smooth contoured triggers that withstand substantial tensile stress without snapping.</li>\n</ul>\n<!-- /wp:list -->',

    '<!-- wp:paragraph -->\n<p><strong>Verifying Hallmarking and Purity:</strong> Never compromise on the legal authenticity of your fine gold jewellery. In India, statutory regulations enforced by the <a href="https://www.bis.gov.in/">Bureau of Indian Standards</a> mandate that all gold jewellery carry the three-part BIS hallmark: the triangular BIS mark, the karatage/fineness grade (such as 22K916 for 22kt or 18K750 for 18kt), and a unique 6-digit alphanumeric HUID (Hallmark Unique Identification) code laser-engraved onto every piece. Authentic hallmarking guarantees metal purity and protects your financial investment.</p>\n<!-- /wp:paragraph -->',

    # Section 6
    '<!-- wp:heading {"level":2} -->\n<h2>Post-Festivity Jewellery Care: Protecting Gold and Gemstones from Sweat and Friction</h2>\n<!-- /wp:heading -->',

    '<!-- wp:paragraph -->\n<p>Dancing Garba for several consecutive nights exposes fine jewellery to intense perspiration, ambient dust, cosmetic powders, and aerosolized perfumes. Perspiration contains natural body salts, urea, and trace lactic acids that can dull the mirror polish of fine gold and form a cloudy film over gemstone facets. Establishing an attentive post-festivity cleaning routine preserves your jewellery in showroom condition.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:list -->\n<ul class="wp-block-list">\n<li><strong>Immediate Post-Dance Microfiber Wipe:</strong> The moment you remove your jewellery after an evening of dance, gently buff every surface with a clean, dry, lint-free microfiber cloth. This immediately absorbs surface sweat and prevents chemical residues from hardening onto the gold.</li>\n<li><strong>Gentle Lukewarm Rinse for Plain Gold:</strong> For plain gold hoops, chains, and sturdy diamond jewellery, immerse the pieces in a shallow bowl of lukewarm water mixed with two drops of mild, detergent-free baby shampoo. Gently clean behind settings with a soft-bristled baby toothbrush, rinse under running lukewarm water with the drain covered, and pat thoroughly dry.</li>\n<li><strong>Specialized Care for Organic and Porous Gems:</strong> Never immerse organic or porous gems like pearls, opals, corals, or emeralds in hot water or chemical detergents. Pearls are especially susceptible to perspiration acids; wipe them exclusively with a damp cotton cloth and allow them to air-dry flat before storage.</li>\n<li><strong>Individual Anti-Tarnish Fabric Pouches:</strong> Never toss multiple jewellery pieces together into a shared jewellery box, as diamonds and hard gemstones will readily scratch the mirror-finish gold of adjacent bangles. Store each design in its individual velvet-lined pouch or compartmentalized drawer.</li>\n</ul>\n<!-- /wp:list -->',

    # Section 7
    '<!-- wp:heading {"level":2} -->\n<h2>Final Thoughts: Investing in Timeless Garba Jewellery Beyond the Nine Nights</h2>\n<!-- /wp:heading -->',

    '<!-- wp:paragraph -->\n<p>While the nine nights of Navratri provide a magnificent excuse to celebrate and shine, the true beauty of curated fine gold and gemstone jewellery lies in its enduring versatility. Fast fashion and imitation costume pieces inevitably tarnish, lose stones, or break after a single season, ending up forgotten in dresser drawers. In contrast, authentic fine jewellery crafted from hallmarked 18kt and 22kt gold offers permanent beauty, skin-kind comfort, and lasting intrinsic value.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p>A pair of sculptural gold hoop earrings like <a href="https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html">The Skein Hoop Earrings</a> that frames your face during Garba twirls will look equally captivating paired with a tailored blazer for corporate meetings or a silk saree at a family wedding. Similarly, an ergonomic gold kada like <a href="https://www.bluestone.com/bangles/the-muricelle-bangle~1001.html">The Muricelle Bangle</a> serves as a timeless everyday wrist accent long after the festive dhol rhythms fade. By prioritizing thoughtful craftsmanship, secure engineering, and certified purity, your festive jewellery becomes a lifelong source of pride, elegance, and joyous memories.</p>\n<!-- /wp:paragraph -->',

    # Section 8 - Related Guides
    '<!-- wp:heading {"level":2} -->\n<h2>More Jewellery &amp; Buying Guides</h2>\n<!-- /wp:heading -->',

    '<!-- wp:paragraph -->\n<p>Expand your jewellery knowledge and plan your festive acquisitions with our expert buyer resources:</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p>Discover how to evaluate precious metal authenticity with our definitive guide on <a href="https://blog.bluestone.com/how-to-check-gold-purity-2026/">how to check gold purity</a>, exploring HUID markings and karat testing methods. Learn the complete tax breakdown on fine jewellery purchases by reviewing our transparent analysis of <a href="https://blog.bluestone.com/gst-on-gold-jewellery-in-india-what-youre-actually-paying-in-tax/">GST on gold jewellery in India</a>, ensuring you understand making charges and tax slabs. If you are shopping from home, explore our trusted recommendations on <a href="https://blog.bluestone.com/is-buying-gold-jewellery-online-safe-in-india-the-honest-answer/">buying gold jewellery online safely</a>. Ensure a flawless wrist fit for every occasion with our comprehensive <a href="https://blog.bluestone.com/bangle-size-2026/">bangle size guide</a>, and plan your purchases strategically by consulting our calendar of the <a href="https://blog.bluestone.com/best-day-to-buy-gold-2026/">best days to buy gold in 2026</a>.</p>\n<!-- /wp:paragraph -->',

    # Section 9 - FAQs
    '<!-- wp:heading {"level":2} -->\n<h2>Frequently Asked Questions About Garba Jewellery</h2>\n<!-- /wp:heading -->',

    '<!-- wp:paragraph -->\n<p><strong>What type of jewellery is best suited for energetic Garba dancing?</strong></p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>The best jewellery for Garba dancing features lightweight construction (under 10 grams per earring), contoured silhouettes that sit flush against the body, and ultra-secure closures such as threaded Bombay screw-backs or click-lock huggie hoops. Smooth hoop earrings, contoured oval kadas, and fixed-bail pendants minimize snagging on mirror-work chaniya cholis while withstanding high-speed pirouettes.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p><strong>Can I wear real gold jewellery while playing Garba and Dandiya?</strong></p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Yes, wearing real 18kt or 22kt hallmarked gold jewellery during Garba is both safe and beneficial because fine gold is hypoallergenic and non-reactive to perspiration. However, you should avoid fragile, hollow-cast long chains or delicate dangling jhumkas that could catch on dandiya sticks. Stick to structured kadas, hoops, and close-fitting necklaces with sturdy clasps.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p><strong>How do I prevent my earrings from hurting or tearing my earlobes during Garba?</strong></p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>To prevent earlobe strain during long dance sessions, keep total earring weight below 8 to 10 grams per pair. Choose huggie earrings or contoured hoop designs that distribute weight along the lower curve of the lobe rather than pulling vertically. If wearing statement pieces, use medical earlobe support patches behind the lobe to transfer weight away from the piercing.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p><strong>What gemstones pair best with traditional Navratri chaniya choli colours?</strong></p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Precious and semi-precious gemstone jewelry provides brilliant harmony with Navratri colour themes. Vibrant green emeralds contrast beautifully with red or rani pink outfits, fiery rubies complement mustard yellow and orange attire, deep blue sapphires enhance royal blue or peacock tones, and lustrous pearls or diamonds bring balance to multi-coloured kutch-work embroidery.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p><strong>How can I protect my fine jewellery from sweat and perfume during Navratri?</strong></p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Always follow the golden rule of jewellery: make it the last item you put on and the first item you take off. Apply cosmetics, moisturizers, and hairsprays at least ten minutes before wearing your jewellery to avoid chemical film deposits. After dancing, immediately wipe each piece with a clean, dry microfiber cloth to absorb moisture before storing in individual fabric pouches.</p>\n<!-- /wp:paragraph -->',

    '<!-- wp:paragraph -->\n<p><strong>Are bangles or kadas better for Garba?</strong></p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Contoured oval kadas with secure side hinge mechanisms are significantly better than stacks of loose round bangles for Garba. Round bangles slide up and down the forearm during clapping and can bruise the wrist or crack during dandiya impact. Contoured kadas stay firmly in place, allowing full forearm freedom and effortless rhythm.</p>\n<!-- /wp:paragraph -->',

    # Trailing Schema
    """<!-- wp:html -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BlogPosting",
      "@id": "https://blog.bluestone.com/garba-jewellery-2026/#article",
      "isPartOf": {
        "@type": "WebPage",
        "@id": "https://blog.bluestone.com/garba-jewellery-2026/"
      },
      "headline": "How to Choose and Style Garba Jewellery in 2026: An Expert Buyer's Guide",
      "description": "Master how to choose dance-proof garba jewellery in 2026. Discover lightweight gold hoops, secure clasps, gemstone jewelry pairings, and sweat-safe care tips.",
      "inLanguage": "en-IN",
      "mainEntityOfPage": "https://blog.bluestone.com/garba-jewellery-2026/",
      "datePublished": "2026-09-25T13:30:00+05:30",
      "dateModified": "2026-09-25T13:30:00+05:30",
      "author": {
        "@type": "Person",
        "name": "Satyam",
        "jobTitle": "BlueStone Editorial"
      },
      "publisher": {
        "@type": "Organization",
        "name": "BlueStone",
        "url": "https://www.bluestone.com",
        "logo": {
          "@type": "ImageObject",
          "url": "https://www.bluestone.com/theme/bluestone/images/new-logo.png"
        }
      },
      "keywords": [
        "garba jewellery",
        "gemstone jewelry",
        "navratri jewellery",
        "dance-proof gold jewellery",
        "garba jewellery 2026"
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://blog.bluestone.com/garba-jewellery-2026/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What type of jewellery is best suited for energetic Garba dancing?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The best jewellery for Garba dancing features lightweight construction (under 10 grams per earring), contoured silhouettes that sit flush against the body, and ultra-secure closures such as threaded Bombay screw-backs or click-lock huggie hoops. Smooth hoop earrings, contoured oval kadas, and fixed-bail pendants minimize snagging on mirror-work chaniya cholis while withstanding high-speed pirouettes."
          }
        },
        {
          "@type": "Question",
          "name": "Can I wear real gold jewellery while playing Garba and Dandiya?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, wearing real 18kt or 22kt hallmarked gold jewellery during Garba is both safe and beneficial because fine gold is hypoallergenic and non-reactive to perspiration. However, you should avoid fragile, hollow-cast long chains or delicate dangling jhumkas that could catch on dandiya sticks. Stick to structured kadas, hoops, and close-fitting necklaces with sturdy clasps."
          }
        },
        {
          "@type": "Question",
          "name": "How do I prevent my earrings from hurting or tearing my earlobes during Garba?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "To prevent earlobe strain during long dance sessions, keep total earring weight below 8 to 10 grams per pair. Choose huggie earrings or contoured hoop designs that distribute weight along the lower curve of the lobe rather than pulling vertically. If wearing statement pieces, use medical earlobe support patches behind the lobe to transfer weight away from the piercing."
          }
        },
        {
          "@type": "Question",
          "name": "What gemstones pair best with traditional Navratri chaniya choli colours?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Precious and semi-precious gemstone jewelry provides brilliant harmony with Navratri colour themes. Vibrant green emeralds contrast beautifully with red or rani pink outfits, fiery rubies complement mustard yellow and orange attire, deep blue sapphires enhance royal blue or peacock tones, and lustrous pearls or diamonds bring balance to multi-coloured kutch-work embroidery."
          }
        },
        {
          "@type": "Question",
          "name": "How can I protect my fine jewellery from sweat and perfume during Navratri?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Always follow the golden rule of jewellery: make it the last item you put on and the first item you take off. Apply cosmetics, moisturizers, and hairsprays at least ten minutes before wearing your jewellery to avoid chemical film deposits. After dancing, immediately wipe each piece with a clean, dry microfiber cloth to absorb moisture before storing in individual fabric pouches."
          }
        },
        {
          "@type": "Question",
          "name": "Are bangles or kadas better for Garba?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Contoured oval kadas with secure side hinge mechanisms are significantly better than stacks of loose round bangles for Garba. Round bangles slide up and down the forearm during clapping and can bruise the wrist or crack during dandiya impact. Contoured kadas stay firmly in place, allowing full forearm freedom and effortless rhythm."
          }
        }
      ]
    }
  ]
}
</script>
<!-- /wp:html -->"""
]

raw_article = "\n\n".join(content_blocks)

# Validation checks
# Check for em dashes, en dashes, spaced hyphens
em_dash_count = raw_article.count("—")
en_dash_count = raw_article.count("–")
spaced_hyphen_count = len(re.findall(r"\s+-\s+", raw_article))

print(f"Validation checks:")
print(f"  Em dashes: {em_dash_count}")
print(f"  En dashes: {en_dash_count}")
print(f"  Spaced hyphens: {spaced_hyphen_count}")

# Check word count of visible text
clean_text = re.sub(r"<[^>]+>", " ", raw_article)
clean_text = re.sub(r"<!--.*?-->", " ", clean_text, flags=re.DOTALL)
words = clean_text.split()
word_count = len(words)
print(f"  Visible word count: {word_count}")

draft_payload = {
    "title": "How to Choose and Style Garba Jewellery in 2026: An Expert Buyer's Guide",
    "slug": "garba-jewellery-2026",
    "focus_keyphrase": "garba jewellery",
    "meta_description": "Master how to choose dance-proof garba jewellery in 2026. Discover lightweight gold hoops, secure clasps, gemstone jewelry pairings, and sweat-safe care tips.",
    "author_id": 270271337,
    "categories": [554493348, 554493465],  # Gold + Jewellery Problem & Solution (Jewellery Education)
    "raw_content": raw_article,
    "word_count": word_count
}

out_file = ROOT / "output" / "Week9_Rank66_garba_jewellery_draft.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(draft_payload, f, indent=2, ensure_ascii=False)

print(f"Saved draft to {out_file}")
