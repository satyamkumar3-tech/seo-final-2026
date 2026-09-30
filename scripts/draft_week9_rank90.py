#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Draft complete Gutenberg article for Week 9 Rank 90: earring styles for guys."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Load carousel snippet
carousel_snippet_path = ROOT / "output/week9_rank90_carousel_snippet.html"
carousel_html = carousel_snippet_path.read_text(encoding="utf-8")

article_blocks = []

def p(text):
    return f"<!-- wp:paragraph -->\n<p>{text}</p>\n<!-- /wp:paragraph -->"

def h2(text):
    return f"<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">{text}</h2>\n<!-- /wp:heading -->"

def h3(text):
    return f"<!-- wp:heading {{\"level\":3}} -->\n<h3 class=\"wp-block-heading\">{text}</h3>\n<!-- /wp:heading -->"

def ul(items):
    lis = "\n".join([f"<li>{item}</li>" for item in items])
    return f"<!-- wp:list -->\n<ul>\n{lis}\n</ul>\n<!-- /wp:list -->"

def ol(items):
    lis = "\n".join([f"<li>{item}</li>" for item in items])
    return f"<!-- wp:list {{\"ordered\":true}} -->\n<ol>\n{lis}\n</ol>\n<!-- /wp:list -->"

# --- Content Generation ---

# Byline
article_blocks.append(p("By Satyam, BlueStone Editorial"))

# Intro
intro_p1 = (
    "Choosing modern earring styles for guys has transformed from an alternative fashion statement into an essential dimension "
    "of contemporary men's grooming and fine jewellery. Today, whether you are stepping into a corporate boardroom, heading to a casual weekend brunch, "
    "or dressing for a traditional Indian wedding celebration, the right earring adds sharp intentionality and refined charisma to your look. "
    "From understated solid gold studs and close-fitting huggies to brilliant diamond accents and architectural ear cuffs, the modern jewellery landscape "
    "offers sophisticated choices designed specifically with masculine proportions, lasting comfort, and hypoallergenic security in mind."
)
article_blocks.append(p(intro_p1))

intro_p2 = (
    "Finding your ideal style requires understanding how silhouette, metal purity, backing mechanics, and ear placement interact with your facial features and daily routine. "
    "This 2026 definitive buying guide breaks down the most sought-after earring styles for guys, answers essential questions regarding ear placement and skin health, "
    "and provides practical styling frameworks to help you curate a timeless fine jewellery collection."
)
article_blocks.append(p(intro_p2))

# TL;DR Callout Box
tldr_content = (
    "<strong>Quick Style Takeaway (TL;DR):</strong><br/>"
    "1. <strong>First-Time Wearers:</strong> Begin with 3mm to 4mm solid 18K yellow or white gold studs or snug huggies that sit flush against the earlobe.<br/>"
    "2. <strong>Ear Placement:</strong> There is no archaic code dictating which ear guys wear earrings in 2026. Men wear earrings in the left ear, right ear, or both based purely on facial balance and personal aesthetic.<br/>"
    "3. <strong>Precious Metals:</strong> Prioritize certified 14K or 18K gold and platinum with BIS hallmark verification to prevent allergic contact dermatitis and ensure structural durability.<br/>"
    "4. <strong>Security:</strong> Choose threaded screw backs or reinforced hinged clicker huggies for active daily wear, workouts, and sleep without accidental loss."
)
article_blocks.append(p(tldr_content))

# Section 1: Evolution of Men's Earring Styles
article_blocks.append(h2("Why Earring Styles for Guys Are Defining Modern Men's Grooming in 2026"))
article_blocks.append(p(
    "Men adorning their ears with precious metals and gemstones is far from a temporary trend. In Indian heritage, the traditional Karnavedha ceremony "
    "dates back millennia, celebrating ear piercing in infancy for both boys and girls as an auspicious milestone believed to sharpen intellect and balance bodily energies. "
    "Centuries later, royal portraits of Indian maharajas and Mughal nobility depicted sovereigns wearing magnificent natural pearl drops, emerald balis, and diamond studs "
    "as unmistakable symbols of statecraft, wealth, and refined masculine elegance."
))
article_blocks.append(p(
    "In 2026, modern menswear has fully re-embraced this heritage through the lens of minimalist luxury. Contemporary men view fine jewellery not as an ornament reserved exclusively "
    "for grand occasions, but as a deliberate expression of self-assurance. Tailored linen shirts, sharp navy suits, and casual monochrome streetwear are now routinely paired "
    "with masterfully crafted gold and diamond accents, establishing earring styles for guys as a core pillar of modern personal style."
))

# Section 2: Stud Earrings
article_blocks.append(h2("Classic Stud Earrings: The Timeless Everyday Choice for Men"))
article_blocks.append(p(
    "Stud earrings remain the undisputed cornerstone of men's ear jewellery. Characterized by a singular decorative element mounted on a straight metal post that passes through the lobe, "
    "studs sit flush against the ear with minimal visual bulk. Their clean profile makes them universally flattering, exceptionally comfortable for sleeping or wearing sports helmets, "
    "and effortlessly compatible with formal office dress codes."
))
article_blocks.append(h3("Popular Stud Variations for Guys"))
stud_types = [
    "<strong>Solitaire Diamond Studs:</strong> Featuring a single round brilliant or princess cut natural diamond set in 18K white gold or yellow gold. A 0.15 to 0.50 carat stone provides an elegant, light-catching focal point that feels luxurious yet understated.",
    "<strong>Minimalist Geometric Gold Studs:</strong> Hexagons, cubes, brushed discs, and architectural pyramid studs crafted in solid 14K or 18K gold offer a clean, masculine texture without gemstone sparkle.",
    "<strong>Bezel-Set Studs:</strong> Unlike traditional prongs that elevate the stone, a bezel setting encircles the diamond or gemstone in a sleek metal rim. This protects the stone edges from daily knocks and prevents snagging on knitwear or grooming towels.",
    "<strong>Black Diamond and Dark Accent Studs:</strong> For a moody, contemporary aesthetic, natural black diamonds set in 18K white gold provide subtle luxury with a distinctly modern edge."
]
article_blocks.append(ul(stud_types))

# Section 3: Huggies and Hoops
article_blocks.append(h2("Men's Huggie and Hoop Earrings: Subtle Edge and Everyday Comfort"))
article_blocks.append(p(
    "While stud earrings offer pinpoint elegance, hoop earrings introduce fluid curves and dynamic movement to the jawline. For most men, the most versatile iteration is the huggie earring. "
    "As the name suggests, a huggie features a small outer diameter, typically between 10mm and 13mm, designed to sit snugly against the earlobe without hanging low or swinging."
))
article_blocks.append(p(
    "Unlike women's fashion hoops that often measure 25mm to 50mm, men's hoops prioritize compact proportions and substantial wire thickness. A hoop with a 1.5mm to 2.5mm profile width provides "
    "a solid, masculine presence. Furthermore, high-quality huggies feature integrated hinged snap closures, where the post snaps securely into the hollow rear segment, eliminating sharp protruding posts "
    "behind the ear and making them the ultimate sleep-friendly daily jewellery."
))
article_blocks.append(h3("Comparing Huggies and Traditional Small Hoops"))
hoop_comparisons = [
    "<strong>Huggie Earrings (10mm to 12mm):</strong> Sit virtually flush with the lower lobe curve. Ideal for daily corporate wear, gym workouts, and understated luxury.",
    "<strong>Small Balis / Classic Hoops (13mm to 15mm):</strong> Offer a slight daylight gap beneath the earlobe, creating gentle motion and a relaxed, bohemian or artistic aesthetic.",
    "<strong>Textured Gold Hoops:</strong> Designs featuring subtle knurling, ribbed facets, or pavé diamond channels reflect light with every head turn while maintaining a robust structural feel."
]
article_blocks.append(ul(hoop_comparisons))

# Section 4: Dangles, Drops, and Novelty Accents
article_blocks.append(h2("Dangles, Drops, and Novelty Accents: Making a Bold Aesthetic Statement"))
article_blocks.append(p(
    "For guys looking to push creative boundaries, drop and dangle earrings offer striking individuality. These designs incorporate a small stud or huggie base from which a mobile charm, "
    "delicate chain, or geometric motif descends below the earlobe. Popularized by international musicians, actors, and fashion innovators, drop earrings introduce a sense of relaxed swagger to urban outfits."
))
article_blocks.append(p(
    "When styling dangles, balance is paramount. Most men prefer wearing a drop earring as a single statement piece in one ear, while keeping the opposite ear bare or fitted with a discreet micro-stud. "
    "Look for refined motifs crafted in hallmarked yellow or white gold, such as feather motifs, bar drops, or architectural dagger silhouettes, ensuring the weight remains light to prevent lobe stretching."
))

# Section 5: Non-Pierced Alternatives
article_blocks.append(h2("Non-Pierced Alternatives: Ear Cuffs and Clip-On Designs"))
article_blocks.append(p(
    "You do not need a permanent ear piercing to explore men's ear styling. Non-pierced alternatives have advanced dramatically in precision engineering, offering comfortable, secure hold without skin trauma."
))
non_pierced_list = [
    "<strong>Architectural Ear Cuffs:</strong> Semi-circular gold bands designed to slip over the thinnest outer ridge of the upper ear helix and slide down into the conch groove. They rely on gentle spring tension rather than piercing holes.",
    "<strong>Magnetic Studs:</strong> Utilizing small, high-grade rare-earth magnets positioned on either side of the lobe. While practical for evening events, prolonged wear may cause localized pressure discomfort.",
    "<strong>Spring-Loaded Clip-Ons:</strong> Modern tension clips fitted with silicone cushioning pads that distribute weight evenly across the lobe surface without painful pinching."
]
article_blocks.append(ul(non_pierced_list))

# Section 6: In Which Ear Guys Wear Earrings (Supporting Keyword Spine)
article_blocks.append(h2("In Which Ear Do Guys Wear Earrings? Debunking Myths and Modern Styling Rules"))
article_blocks.append(p(
    "A frequent question among first-time buyers is in which ear guys wear earrings. Historically, Western pop culture in the late 1970s and 1980s circulated an informal code suggesting that an earring "
    "in the left ear signaled heterosexuality, while an earring in the right ear denoted homosexuality. In 2026, this outdated urban myth has been entirely discarded by global fashion and cultural communities alike."
))
article_blocks.append(p(
    "Modern men wear earrings in whichever ear best complements their facial symmetry, personal aesthetic, and lifestyle. In fact, many men choose to pierce both ears simultaneously, "
    "echoing the ancient Indian tradition of Karnavedha. Whether you choose single-ear or dual-ear styling, consider these practical guidelines:"
))
ear_choice_rules = [
    "<strong>Hair Parting and Facial Angle:</strong> If your hair is parted to the left, wearing an earring on your right ear creates balanced visual contrast by showcasing jewellery against an open facial profile.",
    "<strong>Phone and Headphone Habits:</strong> If you frequently hold a phone to your right ear for business calls, piercing your left ear prevents unwanted friction and clicking against the handset receiver.",
    "<strong>Dual Piercing Symmetry:</strong> Symmetrical studs or matching gold huggies worn in both ears frame the jawline beautifully, imparting a polished, deliberate appearance suited for both tailored suits and festive kurtas.",
    "<strong>Asymmetric Stack Styling:</strong> An increasingly popular trend is wearing a clean diamond stud in one ear while sporting a huggie paired with an upper helix cuff on the other."
]
article_blocks.append(ul(ear_choice_rules))

# In-Body Type 3 Lifestyle Placeholder
article_blocks.append("<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->")

# Section 7: Mid-Article Showcase & Carousel
article_blocks.append(h2("Curated Fine Gold and Diamond Earring Designs for Modern Men"))
article_blocks.append(p(
    "When selecting fine jewellery designed to last a lifetime, BlueStone brings master craftsmanship, certified natural diamonds, and BIS-hallmarked pure gold to men's accessories. "
    "Explore our handpicked curation of understated huggies and precision-engineered hoops tailored for daily wear:"
))

# Insert Carousel Block
article_blocks.append(carousel_html)

# Mandatory single Curated Design Highlights paragraph directly following carousel
article_blocks.append(p(
    "<strong>Curated Design Highlights:</strong> Explore signature fine jewellery essentials including "
    "<a href=\"https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html\">The Skein Hoop Earrings</a>, "
    "<a href=\"https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html\">The Asya Huggie Earrings</a>, "
    "<a href=\"https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html\">The Aleena Huggie Earrings</a>, "
    "<a href=\"https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html\">The Ursa Hoop Earrings</a>, "
    "<a href=\"https://www.bluestone.com/earrings/the-faliha-purse-hoop-earrings~73262.html\">The Faliha Purse Hoop Earrings</a>, and "
    "<a href=\"https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html\">The Vicky Hoop Earrings</a>."
))

# Section 8: Face Shape and Proportions
article_blocks.append(h2("Matching Earring Styles to Your Face Shape and Proportions"))
article_blocks.append(p(
    "Just as choosing the right sunglasses or beard neckline alters facial harmony, selecting the right earring silhouette can highlight your best features while softening harsh angles. "
    "Use this structural guideline to match your face shape to complementary earring designs:"
))
face_shapes = [
    "<strong>Square Face (Strong Jawline and Broad Forehead):</strong> Balance prominent angular bone structure with curved elements. Rounded huggies, slim balis, and circular diamond studs soften jaw contours without diminishing masculine definition.",
    "<strong>Round Face (Equal Width and Length with Soft Cheeks):</strong> Introduce visual length and structural definition with geometric studs, such as square-cut princess diamonds, pyramid studs, or triangular motifs. Avoid large circular hoops that accentuate roundness.",
    "<strong>Oval Face (Balanced Proportions and Gently Narrowing Chin):</strong> The most versatile facial profile. Oval faces effortlessly pull off virtually any style, from micro-studs and ribbed huggies to statement drop earrings.",
    "<strong>Heart or Diamond Face (Narrow Pointed Chin with Wide Cheekbones):</strong> Huggies with slight drop volume or bar studs draw visual balance downward, harmonizing the tapered lower third of the face.",
    "<strong>Earlobe Scale and Proportions:</strong> Match earring dimensions to your earlobe size. Larger earlobes look natural with 5mm to 6mm studs or 13mm hoops, whereas smaller lobes are complemented by 3mm to 4mm micro-studs to prevent visual crowding."
]
article_blocks.append(ul(face_shapes))

# Section 9: Precious Metals & Skin Health
article_blocks.append(h2("Precious Metals and Skin Health: 14K vs 18K Gold and Platinum"))
article_blocks.append(p(
    "Because the earlobe post sits in continuous direct contact with living tissue and perspiration, metal selection is not merely a style preference; it is a fundamental health consideration. "
    "Inferior alloy metals such as nickel, brass, low-grade steel, and copper frequently trigger allergic contact dermatitis, resulting in chronic redness, itching, swelling, and unsightly weeping."
))
article_blocks.append(p(
    "BlueStone crafts fine jewellery exclusively in genuine precious metals: solid gold and platinum. Understanding gold purity standards ensures you invest in pieces that look magnificent and safeguard skin health:"
))
metal_guide = [
    "<strong>18K Gold (750 Purity):</strong> Composed of 75% pure fine gold alloyed with noble metals like copper, silver, and zinc. 18K gold offers a warm, radiant lustre and exceptional hypoallergenic safety, making it the premier choice for luxury studs and huggies.",
    "<strong>14K Gold (585 Purity):</strong> Containing 58.5% pure gold, 14K provides superior tensile hardness and resistance to scratches and bending. It is ideal for active men who rarely take their earrings off during workouts or manual activities.",
    "<strong>White Gold:</strong> Pure gold alloyed with white noble metals and electroplated with rhodium for a crisp, mirror-like platinum sheen. Perfect for pairing with stainless steel luxury watches and silver-tone accessories.",
    "<strong>Platinum (950 Purity):</strong> An extraordinarily dense, naturally white metal that is 95% pure and completely hypoallergenic. Platinum will never tarnish, oxidize, or wear thin over decades of continuous wear.",
    "<strong>Mandatory BIS Hallmarking:</strong> In India, all authentic gold jewellery is legally certified with a Bureau of Indian Standards (BIS) hallmark and a unique 6-digit alphanumeric HUID (Hallmark Unique Identification). Always check for official hallmark laser engraving on the post or clasp before purchasing."
]
article_blocks.append(ul(metal_guide))

# In-Body Type 3 Flatlay Placeholder
article_blocks.append("<!-- TYPE3_FLATLAY_PLACEHOLDER -->")

# Section 10: Backing Mechanisms
article_blocks.append(h2("Earring Backing Mechanisms: Screw Backs, Push Backs, and Huggie Clasps"))
article_blocks.append(p(
    "A fine gold or diamond earring is only as reliable as the mechanism holding it in place. Because men lead physically active lives and frequently change shirts or take off motorcycle helmets, "
    "choosing the correct backing ensures peace of mind against accidental loss:"
))
backing_types = [
    "<strong>Threaded Screw Backs:</strong> The post features microscopic threading, allowing the earring back to screw on like a precision nut onto a bolt. Threaded screw backs provide the highest retention security available in fine jewellery, making them virtually impossible to pull off accidentally.",
    "<strong>Friction Push Backs (Butterfly Clasps):</strong> Slide smoothly onto a grooved post. While easy to insert and remove, friction backs can loosen over time with repeated wear and are more susceptible to snagging on knit sweaters or towels.",
    "<strong>Hinged Snap / Clicker Closures:</strong> Standard on premium huggies, this mechanism features a curved post that clicks firmly into a notched groove in the opposite curve. There are no loose parts to drop down the sink, and the smooth contour eliminates poking behind the ear during sleep.",
    "<strong>Post Gauge Considerations:</strong> Standard earlobe piercings for men utilize an 18-gauge (1.0mm) or 20-gauge (0.8mm) post thickness. Never force a thick post into a fresh or smaller piercing channel, as this causes micro-tears and localized inflammation."
]
article_blocks.append(ul(backing_types))

# Section 11: Styling Guide for Occasions
article_blocks.append(h2("How to Style Men's Earrings: From Corporate Boardrooms to Festive Celebrations"))
article_blocks.append(p(
    "Styling men's earrings successfully relies on context and proportion. An earring should elevate your outfit without creating visual discord. "
    "Here is how to style your pieces across key everyday scenarios:"
))
styling_scenarios = [
    "<strong>Corporate and Professional Settings:</strong> Keep designs minimal and flush. A single 3mm to 4mm diamond stud in 18K white gold or a slim, unadorned gold huggie communicates polish and attention to detail without breaching professional decorum.",
    "<strong>Smart Casual and Weekend Socials:</strong> Pair textured gold huggies or geometric studs with an open-collar linen shirt, knit polo, or tailored overshirt. This creates an effortless, sophisticated focal point that complements your watch or bracelet.",
    "<strong>Traditional Indian Festive and Wedding Wear:</strong> Festive occasions like Diwali, Eid, and wedding receptions are ideal for expressing heritage luxury. A classic gold bali, an ornate diamond cluster stud, or paired huggies harmonize impeccably with silk kurtas, bandhgalas, and embroidered sherwanis.",
    "<strong>Streetwear and Nightlife:</strong> Embrace bolder silhouettes, such as chunky ridged hoops, black diamond studs, or a subtle single drop charm paired with an oversized jacket, dark denim, and leather boots."
]
article_blocks.append(ul(styling_scenarios))

# Section 12: Hygiene, Aftercare, and Care
article_blocks.append(h2("Cleaning, Aftercare, and Long-Term Jewellery Maintenance"))
article_blocks.append(p(
    "Proper hygiene keeps your piercings healthy and your precious jewellery sparkling brilliantly for decades. Daily buildup of natural sebum, dead skin cells, hair styling products, "
    "and cologne can dull diamond brilliance and harbour bacteria behind the earlobe."
))
care_steps = [
    "<strong>Routine Weekly Cleaning:</strong> Soak your solid gold and diamond earrings in a bowl of lukewarm water mixed with a few drops of mild, fragrance-free dish soap for 10 minutes. Gently brush around prongs and behind the setting with an extra-soft toothbrush, then rinse thoroughly with warm water.",
    "<strong>Avoid Harsh Chemicals:</strong> Remove your fine earrings before entering chlorinated swimming pools, hot tubs, or applying alcohol-heavy cologne and hair pomades. Chlorine can cause micro-fissures in gold alloys over time.",
    "<strong>Fresh Piercing Healing Protocol:</strong> New earlobe piercings require 6 to 8 weeks of uninterrupted healing. Clean the area twice daily with sterile 0.9% saline spray. Never touch the piercing with unwashed hands, and avoid rotating or twisting the post, which disrupts healing tissue.",
    "<strong>Dedicated Storage:</strong> Store your gold and diamond earrings in individual velvet-lined compartments or soft fabric pouches to prevent diamonds from scratching softer metal surfaces."
]
article_blocks.append(ol(care_steps))

# Section 13: Final Thoughts (MUST BE BEFORE RELATED GUIDES AND FAQS)
article_blocks.append(h2("Final Thoughts on Choosing the Perfect Earring Styles for Guys"))
article_blocks.append(p(
    "Exploring earring styles for guys is ultimately about discovering an accessory that feels natural, comfortable, and distinctly authentic to who you are. "
    "Whether your taste leans toward the discreet brilliance of a solitaire diamond stud, the architectural lines of a textured huggie, or the bold statement of a single gold bali, "
    "the golden rule is to prioritize quality over fleeting novelties."
))
article_blocks.append(p(
    "By investing in certified 14K or 18K solid gold, natural certified diamonds, and precision-threaded screw back mechanisms from BlueStone, you ensure that your ear jewellery "
    "remains a permanent asset in your grooming wardrobe: timeless, hypoallergenic, and masterfully crafted to endure."
))

# Section 14: Mandatory Related Guides Section (Internal Blog Cluster Links)
article_blocks.append(h2("More Jewellery & Buying Guides"))
article_blocks.append(p(
    "Expand your fine jewellery expertise and explore our comprehensive guides on precious metals, certifications, and styling: "
    "read our detailed breakdown on <a href=\"https://blog.bluestone.com/how-to-check-gold-purity-2026/\">How to Check Gold Purity in 2026</a> to master hallmarking hallmarks and testing methods; "
    "understand real tax implications with our guide on <a href=\"https://blog.bluestone.com/gst-on-gold-jewellery-in-india-what-youre-actually-paying-in-tax/\">GST on Gold Jewellery in India</a>; "
    "explore cultural placement traditions in <a href=\"https://blog.bluestone.com/which-ear-should-a-guy-wear-an-earring-in/\">Which Ear Should a Guy Wear an Earring In?</a>; "
    "discover classic styling nuances in <a href=\"https://blog.bluestone.com/gold-studs-to-hoops-a-modern-mans-guide-to-earring-styles/\">Gold Studs to Hoops: A Modern Man's Guide</a>; and "
    "explore daily comfort essentials in our companion guide on <a href=\"https://blog.bluestone.com/daily-wear-gold-earrings-for-women-2026/\">Daily Wear Gold Earrings Buying Guide</a>."
))

# Section 15: Frequently Asked Questions (FINAL CONTENT SECTION BEFORE SCHEMA)
article_blocks.append(h2("Frequently Asked Questions About Earring Styles for Guys"))

faq_pairs = [
    (
        "What are the most popular earring styles for guys in 2026?",
        "The most popular earring styles for guys are classic solitaire diamond studs, minimalist geometric gold studs, and close-fitting huggie hoops. These styles offer an optimal balance of subtle masculinity, lightweight daily comfort, and versatile compatibility with both corporate workwear and relaxed casual fashion."
    ),
    (
        "In which ear do guys wear earrings today?",
        "In 2026, guys wear earrings in the left ear, right ear, or both ears based purely on personal aesthetic preference and facial symmetry. Outdated 1980s myths associating specific ears with sexual orientation have been completely retired; modern styling focuses entirely on personal comfort, hair parting balance, and individual confidence."
    ),
    (
        "Which earring style is best for first-time wearers?",
        "For first-time wearers, a small 3mm to 4mm round diamond stud or a compact 10mm to 11mm solid gold huggie with a smooth hinged clasp is the best choice. These designs do not pull on the earlobe, minimize the risk of snagging on clothing, and provide comfortable 24/7 wearability while the piercing settles."
    ),
    (
        "Can guys wear earrings in corporate or professional office environments?",
        "Yes, men can comfortably wear earrings in modern corporate environments by choosing discreet, high-quality fine jewellery. An understated 14K or 18K gold micro-stud or a flush-fitting huggie in white or yellow gold communicates refined grooming and attention to detail without breaching professional dress codes."
    ),
    (
        "Why is 14K or 18K gold recommended for men's earrings over silver or base metals?",
        "14K and 18K gold are naturally hypoallergenic and resistant to oxidation and tarnish, preventing allergic contact dermatitis, skin discoloration, and infection around the piercing channel. Furthermore, BlueStone crafts jewellery exclusively in authentic hallmarked gold and diamonds, ensuring lasting structural integrity and enduring resale value."
    ),
    (
        "What is the most secure earring backing mechanism for active men?",
        "Threaded screw backs are the most secure mechanism for stud earrings. The backing screws securely onto the threaded post, preventing it from sliding off during sports, gym workouts, or sleep. For hoops, a precision hinged clicker clasp that locks flush inside the rear curve provides reliable, seamless retention."
    )
]

for q_text, a_text in faq_pairs:
    article_blocks.append(h3(q_text))
    article_blocks.append(p(a_text))

# Section 16: Schemas (FAQPage and BlogPosting JSON-LD)
faq_schema_items = []
for q_text, a_text in faq_pairs:
    faq_schema_items.append({
        "@type": "Question",
        "name": q_text,
        "acceptedAnswer": {
            "@type": "Answer",
            "text": a_text
        }
    })

faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": faq_schema_items
}

blog_posting_schema = {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "How to Choose Earring Styles for Guys: The 2026 Buying Guide",
    "description": "Discover modern earring styles for guys in 2026. From subtle gold studs and huggies to diamond accents and ear placement rules, find your signature look.",
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
    "datePublished": "2026-09-28T18:20:00+05:30",
    "dateModified": "2026-09-28T18:20:00+05:30",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://blog.bluestone.com/earring-styles-for-guys-2026/"
    },
    "keywords": [
        "earring styles for guys",
        "in which ear guys wear earrings",
        "mens gold earrings",
        "mens diamond studs",
        "mens huggie earrings",
        "mens hoop earrings"
    ]
}

import json
schemas_html = f"""<!-- wp:html -->
<script type="application/ld+json">
{json.dumps(faq_schema, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(blog_posting_schema, indent=2)}
</script>
<!-- /wp:html -->"""

article_blocks.append(schemas_html)

full_html = "\n\n".join(article_blocks)

# Sanity verification for prohibited dashes: em dash, en dash, spaced hyphens
# Allow hyphens inside HTML tags, attributes, and words
assert "—" not in full_html, "Em dash found in draft!"
assert "–" not in full_html, "En dash found in draft!"
# Strip style and script tags before checking prose text
prose_only = re.sub(r"<style.*?</style>", "", full_html, flags=re.S)
prose_only = re.sub(r"<script.*?</script>", "", prose_only, flags=re.S)
text_only = re.sub(r"<[^>]+>", " ", prose_only)
assert " - " not in text_only, "Spaced hyphen found in prose text!"

out_draft = ROOT / "output/week9_rank90_draft.html"
with open(out_draft, "w", encoding="utf-8") as f:
    f.write(full_html)

word_count = len(text_only.split())
print(f"Draft written to {out_draft}")
print(f"Total word count: {word_count}")
h2_matches = re.findall(r'<h2[^>]*>(.*?)</h2>', full_html)
print(f"H2 count: {len(h2_matches)}")
for i, h in enumerate(h2_matches, 1):
    print(f"  H2 {i}: {h}")
