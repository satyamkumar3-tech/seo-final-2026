#!/usr/bin/env python3
"""Build Rank 83 Diwali poster article config and Type 3 prompt manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_products() -> dict[str, dict[str, str]]:
    with (ROOT / "Seo Products - final products (1).csv").open(newline="", encoding="utf-8-sig") as f:
        return {row["Design Name"].strip(): row for row in csv.DictReader(f)}


def product(rows: dict[str, dict[str, str]], name: str, category: str) -> dict[str, str]:
    row = rows[name]
    return {
        "code": row["Design Code"],
        "name": name,
        "url": row["Link"],
        "png": f"ProductImages/seo images/{category}/{name}.png",
    }


def write_json(path: str, data: dict) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(target)


def main() -> None:
    rows = load_products()
    prefix = "Week1_Rank83_DiwaliPoster"

    sections = {
        "meta": {
            "title": "Happy Diwali Poster 2026: Design Ideas, Wishes and Captions",
            "slug": "diwali-poster-2026",
            "meta_desc": "Create a happy Diwali poster 2026 with simple design ideas, wishes, captions, school themes, office layouts, WhatsApp poster text and style tips today!",
            "focus_kw": "happy diwali poster",
            "yoast_title": "Happy Diwali Poster 2026: Ideas and Wishes",
        },
        "intro": [
            "A happy Diwali poster works best when it feels bright, clear and easy to read. For Diwali 2026, use one strong festive idea, a short wish, and enough empty space so the design does not look crowded.",
            "TL;DR: pick a diya, rangoli, lotus or light trail as the main visual. Add a short greeting, keep the colours warm, and avoid stuffing the poster with too many fonts, slogans or tiny details.",
            "Diwali 2026 falls on Sunday, 8 November 2026, so this guide keeps the poster wording, captions and festive references locked to 2026.",
        ],
        "sections": [
            {
                "key": "ideas",
                "h2": "Happy Diwali Poster Ideas for 2026",
                "lines": [
                    "Use one large diya in the centre with a warm glow and a short Happy Diwali 2026 message.",
                    "Create a rangoli border and leave the middle clean for the main wish.",
                    "Try a lotus and light trail layout for a calm, elegant festive poster.",
                    "Use a family doorway scene with diyas on both sides for a welcoming theme.",
                    "Make a sweets-and-lamps poster for a warm home celebration feel.",
                    "Use a dark navy background with gold highlights for a premium Diwali mood.",
                    "Choose a white and marigold palette if you want a softer poster.",
                    "Build a school poster around light over darkness and knowledge over ignorance.",
                    "Create an office poster with minimal diyas, clean typography and a professional greeting.",
                    "Use a blank gift card, diya and rangoli corner for social media poster images.",
                ],
            },
            {
                "key": "design",
                "h2": "Diwali Poster Design Tips",
                "lines": [
                    "Start with the message before choosing the decoration.",
                    "Use no more than two fonts in one poster.",
                    "Keep the main greeting large enough to read on a phone screen.",
                    "Place diyas, rangoli or flowers around the edges instead of covering the whole design.",
                    "Use gold, saffron, maroon, cream, emerald or deep blue for a classic Diwali palette.",
                    "Add contrast between text and background so the wish is easy to read.",
                    "Leave breathing space around the central greeting.",
                    "Avoid tiny decorative text because it becomes blurry when shared.",
                    "Use one hero visual rather than five competing festive icons.",
                    "Export the final poster in a clean vertical or square format for sharing.",
                ],
            },
            {
                "key": "wishes",
                "h2": "Diwali Wishes Poster Text",
                "lines": [
                    "May the lights of Diwali 2026 bring joy, peace and prosperity to your home.",
                    "Wishing you a bright Diwali filled with love, laughter and new beginnings.",
                    "May every diya remind you that hope can brighten any corner.",
                    "Happy Diwali 2026. May your home glow with blessings and your heart with gratitude.",
                    "Let this Diwali bring warmth to your family and light to your dreams.",
                    "Wishing you a safe, joyful and beautiful Diwali celebration.",
                    "May the festival of lights fill your life with courage and kindness.",
                    "Happy Diwali. May prosperity, peace and happiness stay close all year.",
                    "May your Diwali be as bright as the lamps you light.",
                    "Wishing you a Diwali full of sweet moments and golden memories.",
                ],
            },
            {
                "key": "ka_poster",
                "h2": "Diwali Ka Poster Ideas in Simple English",
                "lines": [
                    "Diwali ka poster can show one diya, one wish and one clean background.",
                    "Add a rangoli corner if you want the poster to feel more Indian and festive.",
                    "Use Happy Diwali 2026 as the main line and keep the rest short.",
                    "For school projects, add a small line about light, hope and goodness.",
                    "For family sharing, use warm wishes and avoid formal corporate wording.",
                    "For social media, keep the poster bright and uncluttered.",
                    "Use marigold flowers, lamps and soft gold borders for a simple festive look.",
                    "Do not crowd the poster with too many images or quotes.",
                    "Choose readable text over fancy fonts.",
                    "A clean Diwali ka poster looks more premium than an overloaded design.",
                ],
            },
            {
                "key": "school",
                "h2": "Diwali Poster for School Projects",
                "lines": [
                    "Use the theme light over darkness for a classic school poster.",
                    "Draw a diya at the centre and add short points around it.",
                    "Write one simple message about sharing sweets, kindness and happiness.",
                    "Add a clean rangoli border with four or five colours.",
                    "Use safe celebration themes if the school prefers eco-friendly Diwali messaging.",
                    "Keep the handwriting large, neat and easy to read from a distance.",
                    "Add a small line about family, hope and togetherness.",
                    "Use poster colours or sketch pens that do not bleed through the paper.",
                    "Avoid copying too many decorative elements from different references.",
                    "Finish with a simple Happy Diwali 2026 line at the bottom.",
                ],
            },
            {
                "key": "office",
                "h2": "Diwali Wishes Poster for Office",
                "lines": [
                    "Use a clean layout with one diya, one greeting and enough blank space.",
                    "Keep the message inclusive and warm for colleagues, clients and teams.",
                    "Try a line like Wishing you a bright and prosperous Diwali 2026.",
                    "Use elegant gold accents instead of heavy decoration.",
                    "Avoid very casual jokes in formal office posters.",
                    "Make the brand or team name small and secondary if it must appear.",
                    "Choose a balanced colour palette that works on email and print.",
                    "Keep the design readable at thumbnail size for workplace chats.",
                    "Use a short closing such as warm wishes from the team.",
                    "A minimal poster often feels more polished for professional sharing.",
                ],
            },
            {
                "key": "images",
                "h2": "Diwali Poster Images and Layouts",
                "lines": [
                    "Square poster images work well for Instagram and WhatsApp.",
                    "Vertical poster images suit stories, status updates and mobile greetings.",
                    "Landscape posters are better for blog headers, banners and email greetings.",
                    "Use a clear focal point such as one diya, one rangoli or one festive doorway.",
                    "Keep important text away from the edges so it is not cropped.",
                    "Use warm light effects carefully so the poster does not look washed out.",
                    "Avoid placing text over busy rangoli details.",
                    "Use blank areas of the image for the greeting.",
                    "Choose a layout before adding decorations.",
                    "Save a copy without text if you want to reuse the background later.",
                ],
            },
            {
                "key": "captions",
                "h2": "Captions for Happy Diwali Poster",
                "lines": [
                    "Lights, love and a little more hope this Diwali.",
                    "A bright Diwali 2026 for every home and heart.",
                    "Diyas lit, hearts warm, wishes sent.",
                    "May your Diwali glow softly and beautifully.",
                    "Festival of lights, season of gratitude.",
                    "Golden evenings and sweet beginnings.",
                    "A poster full of light for a festival full of love.",
                    "Happy Diwali from our home to yours.",
                    "Rangoli colours, diya glow and festive joy.",
                    "Let the light lead the way.",
                ],
            },
            {
                "key": "eco",
                "h2": "Eco Friendly Diwali Poster Ideas",
                "lines": [
                    "Use diyas, flowers and rangoli instead of fireworks as the main visual.",
                    "Write a short line about celebrating with light, kindness and care.",
                    "Choose earth tones, leaf motifs and warm lamp glow.",
                    "Add a message about clean homes, safe streets and joyful families.",
                    "Keep the poster positive rather than preachy.",
                    "Use reusable decoration themes if the poster is for school.",
                    "Try a caption like light up hearts, not the sky.",
                    "Show sweets, lamps and flowers for a gentle celebration mood.",
                    "Avoid smoky backgrounds if the message is eco-friendly.",
                    "Let the design feel festive, not gloomy.",
                ],
            },
            {
                "key": "mistakes",
                "h2": "Common Diwali Poster Mistakes to Avoid",
                "lines": [
                    "Do not use too many fonts in one poster.",
                    "Do not place pale text on a bright yellow background.",
                    "Do not make the greeting too small for mobile sharing.",
                    "Do not crowd every corner with icons.",
                    "Do not use low-resolution images that blur after upload.",
                    "Do not add long paragraphs when a short wish will work better.",
                    "Do not let decoration cover the main message.",
                    "Do not mix too many colour palettes at once.",
                    "Do not use readable brand names or logos in generic festive designs.",
                    "Do not forget to check spelling before sharing the poster.",
                ],
            },
            {
                "key": "gift",
                "h2": "A Festive Keepsake to Pair with a Diwali Poster",
                "lines": [
                    "A Diwali poster can carry the wish, while a small keepsake can carry the memory.",
                    "Choose jewellery that feels festive but wearable beyond one evening.",
                    "A pendant, ring, bracelet, bangle or earrings can work when the bond is close.",
                    "Keep the gift note shorter than the poster message.",
                    "Pick pieces that suit the person's everyday style.",
                    "Avoid making the gesture feel like a catalogue.",
                    "Let the wish stay central and the gift stay thoughtful.",
                    "Warm gold tones often pair naturally with Diwali styling.",
                    "Choose comfort and meaning before decoration.",
                    "A simple keepsake can make a festive greeting feel more personal.",
                ],
            },
        ],
        "section_leads": {
            "Happy Diwali Poster Ideas for 2026": "Use these ideas when you need a quick visual direction before you start designing.",
            "Diwali Poster Design Tips": "A good Diwali poster is festive, but it still needs hierarchy and readability.",
            "Diwali Wishes Poster Text": "Copy one of these short wishes into a poster, greeting card or status image.",
            "Diwali Ka Poster Ideas in Simple English": "These ideas are useful when you want a simple bilingual or family-friendly direction.",
            "Diwali Poster for School Projects": "School posters should be neat, positive and easy to explain.",
            "Diwali Wishes Poster for Office": "Office posters need warmth without becoming too crowded or casual.",
            "Diwali Poster Images and Layouts": "Choose the layout based on where the poster will be shared.",
            "Captions for Happy Diwali Poster": "Use these as social captions when you share the poster image.",
            "Eco Friendly Diwali Poster Ideas": "Eco-friendly posters work best when the tone stays joyful.",
            "Common Diwali Poster Mistakes to Avoid": "Avoid these issues before exporting or printing your design.",
            "A Festive Keepsake to Pair with a Diwali Poster": "This soft gift section keeps the brand presence useful and light.",
        },
        "faqs": [
            ["What should I write on a happy Diwali poster?", "Write a short wish such as Happy Diwali 2026 or May the lights of Diwali bring joy, peace and prosperity. Keep the main line large and add only one supporting sentence so the poster stays readable."],
            ["How can I make a Diwali poster design look attractive?", "Use one main festive element like a diya, rangoli, lotus or light trail. Keep the background clean, choose two fonts at most, and use warm colours such as gold, saffron, maroon, cream and deep blue."],
            ["What are simple Diwali ka poster ideas for school?", "For school, draw a large diya in the centre, add a rangoli border, and write a short message about light over darkness. Keep the handwriting neat and avoid crowding the chart paper with too many decorations."],
            ["Can I use Diwali poster images for WhatsApp status?", "Yes, vertical and square Diwali poster images work well for WhatsApp status. Keep the text away from edges so it is not cropped, and use a short greeting that is readable on a phone screen."],
            ["What is a good office Diwali wishes poster line?", "A good office line is: Wishing you and your family a bright, joyful and prosperous Diwali 2026. It is warm, inclusive and professional enough for teams, clients and workplace greetings."],
            ["What colours work best for a Diwali poster?", "Gold, saffron, maroon, cream, emerald and deep blue work well for Diwali posters. Use contrast carefully so the greeting stays readable against the festive background."],
        ],
    }

    config = {
        "rank": 83,
        "sections_json": f"output/{prefix}_sections.json",
        "output_prefix": prefix,
        "carousel_id": "bs-cf-diwaliposter",
        "occasion_year": "Diwali Poster 2026",
        "carousel_alt_prefix": "happy Diwali poster 2026 gift idea",
        "gift_h2": "Festive Gift Ideas to Add to the Moment",
        "gift_blurb": "If you are sharing a Diwali poster with a personal note, a small festive keepsake can make the greeting feel warmer. These six approved BlueStone designs stay elegant and giftable, with no prices in the article.",
        "conclusion_html": "A happy Diwali poster does not need to be overloaded to feel festive. Choose one strong visual, one clear wish and a warm 2026 message, then let the light, colour and empty space do the rest.",
        "schema_keywords": [
            "happy diwali poster",
            "diwali poster design",
            "diwali wishes poster",
            "diwali ka poster",
            "diwali poster images",
        ],
        "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
        "products": [
            product(rows, "The Valeria Rose Pendant", "Pendants"),
            product(rows, "The Tarentella Oval Bangle", "Bangles"),
            product(rows, "The Asya Huggie Earrings", "Earrings"),
            product(rows, "The Gigi Ring", "Rings"),
            product(rows, "The Pervinca Charm Holder Bracelet", "Bracelet"),
            product(rows, "The Yfel Evil Eye Pendant Necklace", "Necklaces"),
        ],
        "flatlay_insert_h2": "Diwali Poster for School Projects",
        "lifestyle_insert_h2": "A Festive Keepsake to Pair with a Diwali Poster",
        "more_reads_html": "Read more Diwali ideas in <a href=\"https://blog.bluestone.com/happy-diwali-wishes-messages-quotes-2026/\">happy Diwali wishes 2026</a>, <a href=\"https://blog.bluestone.com/diwali-wishes-quotes-2026/\">Diwali wishes quotes 2026</a>, <a href=\"https://blog.bluestone.com/environment-friendly-diwali-2026/\">environment friendly Diwali 2026</a>, and <a href=\"https://blog.bluestone.com/deepawali-wishes-2026/\">Deepawali wishes 2026</a>. For the 2026 date, see <a href=\"https://www.drikpanchang.com/hindu-festivals/diwali/diwali.html\">Drik Panchang's Diwali calendar</a>.",
        "how_to_html": "To make the right Diwali poster, decide the use first. For school, keep it explanatory. For WhatsApp, keep it short. For office, keep it polished. For family, keep it warm and personal. Then choose one central festive visual and one clear 2026 greeting.",
        "faq_h2": "Frequently Asked Questions about Happy Diwali Posters",
        "min_lines": 100,
        "section_leads": sections["section_leads"],
    }

    people_negative = (
        "readable text, handwriting, printed letters, numbers, symbols on poster, second person, extra hands, earrings other than the referenced earrings, "
        "extra necklaces, rings, watches, extra bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, "
        "packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, cropped face, "
        "dark skin, deep brown skin, heavily tanned skin, illustration, CGI"
    )
    product_negative = (
        "hands, people, floating overlays, cutouts, incorrect bangle design, distorted stones, readable text, logos, price tags, brand marks on props, "
        "blown whites, HDR glare, illustration, CGI"
    )

    prompts = {
        "rank": 83,
        "slug": "diwali-poster-2026",
        "output_prefix": prefix,
        "occasion": "Diwali Poster 2026",
        "primary_kw": "happy diwali poster",
        "caption_occasion": "Happy Diwali poster 2026",
        "caption_year": "2026",
        "flatlay_setting": "festive-mantel",
        "workflow": "Higgsfield MCP nano_banana_pro. Campaign hybrid with mandatory body_image scale line. Do not generate until balance succeeds. Max 2 concurrent generations.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/happy-diwali-poster-hero-2026.webp",
            "flatlay": "output/magnific_generated/happy-diwali-poster-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/happy-diwali-poster-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "happy Diwali poster 2026 hero The Asya Huggie Earrings",
            "flatlay": "happy Diwali poster 2026 flatlay The Muricelle Bangle",
            "lifestyle": "happy Diwali poster 2026 lifestyle The Gigi Ring",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                "code": "BISA0255D05",
                "name": "The Asya Huggie Earrings",
                "gender": "Female",
                "height_mm": 19.77,
                "width_mm": 8.47,
                "size_prompt_note": "earring overall height 19.77 mm and width 8.47 mm; product dimensions, not face size; copy ear scale from body_image",
                "alt": "happy Diwali poster 2026 hero with The Asya Huggie Earrings",
                "caption": "Happy Diwali poster 2026 vibe: The Asya Huggie Earrings",
                "product": {"code": "BISA0255D05", "name": "The Asya Huggie Earrings", "pdp": rows["The Asya Huggie Earrings"]["Link"]},
                "cdn": [
                    "https://kinclimg5.bluestone.com/giproduct/BISA0255D05_YAA14DIG6PRWHXXXX_ABCD00-BP-PICS-00000-1024-80521.png",
                    "https://kinclimg5.bluestone.com/giproduct/BISA0255D05_YAA14DIG6PRWHXXXX_ABCD00-PICS-00000-1024-80521.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Earrings/The Asya Huggie Earrings/1_body_portrait.png",
                    "ProductImages/raw/Earrings/The Asya Huggie Earrings/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": (
                    "Photoreal candid lifestyle photograph with high-end jewellery commercial fidelity on the worn piece only. Natural skin texture, controlled soft key light, gentle fill, realistic shadows, proper shallow depth of field at 85mm, balanced exposure, no blown whites, no HDR glare, DSLR, HD, 16:9 with safe margins.\n\n"
                    "Casting required: solo fair-skinned Indian adult woman designing a Diwali poster at home, light wheatish to fair urban Indian complexion. Exactly one person in frame. No second person, no extra hands.\n\n"
                    "Happy Diwali poster 2026 candid home creative scene, the woman smiles while arranging diyas and marigold petals beside a completely blank cream poster sheet. The poster sheet must be blank with no letters, no handwriting, no symbols, no numbers. Face and upper body visible.\n\n"
                    "The woman physically wears The Asya Huggie Earrings from @img1 body_image and @img2 design on both ears. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: earring overall height_mm=19.77 and width_mm=8.47. These are real product dimensions, NOT face-size instructions. Keep earring size on the ear like @img1 body_image worn ear scale: subtle huggie size, not enlarged. Use @img2 only for the jewellery design.\n\n"
                    "Replicate the yellow gold huggie earrings with pearl-white detail exactly. HD hyperreal metal and stones, 100 percent identical to refs, zero distortion. These earrings are the single and only jewellery in the image. Bare neck, bare wrists, no ring, no watch, no necklace. Jewellery touches ear with a soft contact shadow and is never a floating cutout.\n\n"
                    f"Avoid: {people_negative}."
                ),
            },
            "flatlay": {
                "code": "BISM0003O14",
                "name": "The Muricelle Bangle",
                "gender": "Female",
                "height_mm": 52.03,
                "width_mm": 14.3,
                "size_prompt_note": "bangle inner diameter/height 52.03 mm and band width 14.3 mm; product dimensions, not face size",
                "alt": "happy Diwali poster 2026 flatlay with The Muricelle Bangle",
                "caption": "Happy Diwali poster 2026 keepsake: The Muricelle Bangle",
                "product": {"code": "BISM0003O14", "name": "The Muricelle Bangle", "pdp": rows["The Muricelle Bangle"]["Link"]},
                "cdn": [
                    "https://kinclimg2.bluestone.com/giproduct/BISM0003O14_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-62802.png",
                    "https://kinclimg2.bluestone.com/giproduct/BISM0003O14_YAA18DIG6XXXXXXXX_ABCD00-PICS-00001-1024-62802.png",
                    "https://kinclimg2.bluestone.com/giproduct/BISM0003O14_YAA18DIG6XXXXXXXX_ABCD00-PICS-00002-1024-62802.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Bangles/The Muricelle Bangle/0_primary.png",
                    "ProductImages/raw/Bangles/The Muricelle Bangle/3_side_1.png",
                    "ProductImages/raw/Bangles/The Muricelle Bangle/2_front.png",
                ],
                "ref_roles": ["primary", "side", "front"],
                "prompt": (
                    "Photoreal high-end jewellery still life, top-down editorial product flatlay, controlled soft key light, realistic gentle shadows, shallow depth of field, HD metal and stone detail, 16:9 landscape.\n\n"
                    "Happy Diwali poster 2026 top-down flatlay. Flatlay setting ID: festive-mantel. Surface and props: warm wood festive mantel, two small unlit brass diyas, marigold petals, a tiny rangoli colour dish, blank cream poster card with no readable text, and a plain silk ribbon.\n\n"
                    "The identical Muricelle Bangle from @img1, @img2 and @img3 rests naturally on the mantel at true PDP scale. Product dimensions from PDP: bangle inner diameter height_mm=52.03 and band_width_mm=14.3. These are product dimensions, NOT face-size instructions. Do not enlarge for visibility. Full bangle visible, polished yellow gold with diamond detail, crisp oval form, 100 percent identical design, zero distortion.\n\n"
                    "Props stay secondary and quiet. No people, no hands, no readable text, no brand marks. Jewellery is the clear subject but still true to real size.\n\n"
                    f"Avoid: {product_negative}."
                ),
            },
            "lifestyle": {
                "code": "BINS0639R18",
                "name": "The Gigi Ring",
                "gender": "Female",
                "height_mm": 23,
                "width_mm": 16.12,
                "size_prompt_note": "ring top/head height 23 mm and width 16.12 mm; product dimensions, not face size; copy finger scale from body_image",
                "alt": "happy Diwali poster 2026 lifestyle with The Gigi Ring",
                "caption": "Happy Diwali poster 2026 vibe: The Gigi Ring",
                "product": {"code": "BINS0639R18", "name": "The Gigi Ring", "pdp": rows["The Gigi Ring"]["Link"]},
                "cdn": [
                    "https://kinclimg4.bluestone.com/giproduct/BINS0639R18_YAA18DIG6XXXXXXXX_ABCD00-BP-PICS-00000-1024-71114.png",
                    "https://kinclimg4.bluestone.com/giproduct/BINS0639R18_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-71114.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Rings/The Gigi Ring/1_body_portrait.png",
                    "ProductImages/raw/Rings/The Gigi Ring/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": (
                    "Photoreal candid lifestyle photograph with high-end jewellery commercial fidelity on the worn piece only. Natural skin texture, controlled soft key light, gentle fill, realistic shadows, proper shallow depth of field at 85mm, balanced exposure, no blown whites, no HDR glare, DSLR, HD, 16:9 with safe margins.\n\n"
                    "Casting required: solo fair-skinned Indian adult woman, light wheatish to fair urban Indian complexion. Exactly one person in frame. No second person, no extra hands.\n\n"
                    "Happy Diwali poster 2026 close lifestyle moment, the woman places one diya beside a blank Diwali poster card and marigold petals on a clean table. Her face is softly visible in the background and the hand action is natural. The card must be blank with no letters, no handwriting, no symbols, no numbers.\n\n"
                    "The woman physically wears The Gigi Ring from @img1 body_image and @img2 design on one finger. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: ring top/head height_mm=23 and width_mm=16.12. These are real product dimensions, NOT face-size instructions. Keep ring size on the finger like @img1 body_image worn finger scale: normal ring size, subtle, not enlarged. Use @img2 only for the jewellery design.\n\n"
                    "Replicate the polished yellow gold diamond ring exactly. HD hyperreal metal and stones, 100 percent identical to refs, zero distortion. This ring is the single and only jewellery in the image. Bare ears, bare neck, bare wrists, no watch, no bracelet. Jewellery touches skin with a soft contact shadow and is never a floating cutout.\n\n"
                    f"Avoid: {people_negative}."
                ),
            },
        },
    }

    checklist = """# Checklist v2: Rank 83 Diwali Poster

- [x] New blog only.
- [x] Year locked to Diwali 2026, Sunday, 8 November 2026.
- [x] Primary keyword in intro, meta, title and hero alt.
- [x] Supporting keywords mapped to H2s and FAQs.
- [x] No prices, no old years, no duplicate content H1.
- [x] Type 2 carousel uses approved SEO images only.
- [x] Type 3 prompts use body_image for people slots and category-correct product dimensions.
- [x] Flatlay setting rotated to festive-mantel.
"""

    write_json(f"output/{prefix}_sections.json", sections)
    write_json(f"output/publish_configs/rank83.json", config)
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    (ROOT / f"output/{prefix}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
