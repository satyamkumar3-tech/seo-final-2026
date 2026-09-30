#!/usr/bin/env python3
"""Build Rank 98 maternity quotes article assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank98_MaternityQuotes"
FILMIC_STYLE = (
    "Visual style: subtle cinematic film grain / analog grain, Kodak Portra color science, "
    "gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, "
    "editorial color grading, natural dynamic range, filmic contrast."
)


def rows_by_name(path: str) -> dict[str, dict[str, str]]:
    with (ROOT / path).open(newline="", encoding="utf-8-sig") as f:
        return {row["Design Name"].strip(): row for row in csv.DictReader(f)}


def product(rows: dict[str, dict[str, str]], name: str, png: str) -> dict[str, str]:
    row = rows[name]
    return {"code": row["Design Code"], "name": name, "url": row["Link"], "png": png}


def consolidated(rows: dict[str, dict[str, str]], name: str) -> dict[str, object]:
    row = rows[name]
    note = row["size_prompt_note"]
    note = note.replace("face_height_mm", "product_height_mm").replace("face_width_mm", "product_width_mm")
    return {
        "code": row["Design Code"],
        "name": name,
        "gender": row["GenderTag"],
        "category": row["DesignCategory"],
        "height_mm": float(row["height_mm"]) if row["height_mm"] else None,
        "width_mm": float(row["width_mm"]) if row["width_mm"] else None,
        "size_prompt_note": note + "; these are product dimensions, not face-size instructions",
        "pdp": row["Link"],
        "cdn_primary": row["Image link"],
    }


def write_json(path: str, data: object) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def people_prompt(slot: dict[str, object], scene: str, product_phrase: str, scale_phrase: str, extra_rules: str) -> str:
    return (
        f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} "
        f"Maternity quotes 2026 {scene}. Solo fair-skinned Indian adult pregnant woman, gentle hopeful expression, "
        "soft modern Indian home, blank cream journal or blank card nearby, warm window light, full head, full face, "
        "both eyes, complete smile, upper body and jewellery area visible with safe margins. Exactly one person in the entire image. "
        "Camera pulled back medium shot, 85mm DSLR look, natural skin texture, realistic shadows, 16:9.\n\n"
        f"The woman physically wears {slot['name']} from @img1 body_image and @img2 design. "
        "GENDER LOCK: Female product on adult woman only. "
        f"Product dimensions from PDP: {slot['size_prompt_note']}. "
        f"Keep {scale_phrase} like @img1 body_image worn scale: subtle real product size, not enlarged. "
        "Use @img2 only for jewellery design.\n\n"
        f"Replicate {product_phrase} exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. "
        f"This is the single and only jewellery in the image. {extra_rules} No readable text anywhere.\n\n"
        "Avoid: cropped face, cropped head, readable text, letters, numbers, logo, man wearer, child, baby, second person, "
        "extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, "
        "deep brown skin, heavily tanned skin, illustration, CGI, HDR glow."
    )


def main() -> None:
    csv_rows = rows_by_name("Seo Products - final products (1).csv")
    detail_rows = rows_by_name("KnowledgeBase/Product/Seo Products - consolidated.csv")

    sections = {
        "meta": {
            "title": "Maternity Quotes 2026: Pregnancy and Motherhood Lines",
            "slug": "maternity-quotes-2026",
            "meta_desc": "Maternity quotes 2026 for pregnancy, motherhood, baby bump captions, expecting mom wishes, maternity photo captions, and heartfelt mother-to-be lines.",
            "focus_kw": "maternity quotes",
            "yoast_title": "Maternity Quotes 2026: Pregnancy and Motherhood Lines",
        },
        "intro": [
            "Maternity quotes are for the quiet, emotional, and beautiful season when a woman is becoming someone new while still being fully herself.",
            "TL;DR: choose a maternity quote that matches the moment: soft for photos, emotional for journals, short for captions, and grateful for wishes to an expecting mom.",
        ],
        "sections": [
            {"key": "best", "h2": "Maternity Quotes", "lines": [
                "Motherhood begins long before the baby is in your arms.",
                "A mother-to-be carries love in the most patient way.",
                "Pregnancy is a season of waiting, wonder, and quiet strength.",
                "Every tiny kick is a reminder that love is already here.",
                "A new life grows, and so does a new version of you.",
                "Maternity is not just a phase, it is a soft beginning.",
                "Your body is writing a story your heart will remember forever.",
                "The journey to motherhood is filled with courage you may not even notice yet.",
                "A baby changes the future before arriving in the present.",
                "There is magic in becoming a home for someone you have not met.",
            ]},
            {"key": "short", "h2": "Short Maternity Quotes", "lines": [
                "Growing love, one day at a time.",
                "A tiny heartbeat, a whole new world.",
                "Motherhood is already blooming.",
                "Small kicks, big feelings.",
                "Made with love and patience.",
                "The sweetest wait of my life.",
                "A new chapter is growing.",
                "Already loved beyond words.",
                "My heart is making room.",
                "Waiting, glowing, becoming.",
            ]},
            {"key": "motherhood", "h2": "Pregnancy and Motherhood Quotes", "lines": [
                "Pregnancy teaches you that love can grow quietly and still change everything.",
                "Motherhood starts with a promise you make before the first hello.",
                "The first home a child knows is a mother's heartbeat.",
                "Every expecting mother carries both tenderness and bravery.",
                "The journey is not always simple, but the love is already deep.",
                "Pregnancy is a gentle reminder that life can begin in silence.",
                "A mother is made in small moments of hope, care, and patience.",
                "You are not just waiting for a baby, you are meeting a new part of yourself.",
                "Motherhood is love learning a new language.",
                "The smallest life can create the biggest transformation.",
            ]},
            {"key": "captions", "h2": "Maternity Photo Captions", "lines": [
                "Our little story is growing.",
                "Baby on the way, heart already full.",
                "This bump holds my favorite secret.",
                "Soft days, big dreams.",
                "Growing a miracle with every sunrise.",
                "A new love is under construction.",
                "Current mood: grateful and glowing.",
                "The beginning of our forever.",
                "Tiny kicks, endless joy.",
                "Waiting for the best hello.",
            ]},
            {"key": "baby_bump", "h2": "Baby Bump Captions", "lines": [
                "This little bump has the biggest place in my heart.",
                "My favorite curve is this baby bump.",
                "A tiny miracle, beautifully growing.",
                "Bump days are love notes from the future.",
                "Carrying dreams, hope, and a tiny heartbeat.",
                "The bump may be small, but the love is enormous.",
                "Baby bump, big blessing.",
                "Every photo now has a little extra love.",
                "Growing slowly, loving deeply.",
                "This bump is our sweetest countdown.",
            ]},
            {"key": "expecting_mom", "h2": "Expecting Mom Quotes", "lines": [
                "You are becoming a mother with grace, courage, and so much love.",
                "May this waiting season be full of peace and gentle joy.",
                "Your baby is already blessed to be loved by you.",
                "You carry more strength than you know.",
                "Every day brings you closer to a love that will change everything.",
                "An expecting mom is a beautiful mix of hope and bravery.",
                "You are growing life and growing into yourself at the same time.",
                "May your heart feel held through every new change.",
                "This journey is yours, and it is already meaningful.",
                "You are doing something deeply tender and powerful.",
            ]},
            {"key": "emotional", "h2": "Heart Touching Maternity Quotes", "lines": [
                "One day, the baby you are waiting for will hear how loved they were before they arrived.",
                "Pregnancy is a quiet kind of courage that the world does not always see.",
                "Your heart learned the meaning of forever before your arms did.",
                "There is a love that begins as a heartbeat and becomes a lifetime.",
                "The wait may feel long, but every day is part of the story.",
                "A mother-to-be is already giving comfort, protection, and hope.",
                "Your body may feel different, but your love is becoming clearer.",
                "Some chapters are written in kicks, cravings, dreams, and prayers.",
                "A baby arrives later, but motherhood arrives softly, day by day.",
                "The child you have not met is already changing the way you see love.",
            ]},
            {"key": "husband", "h2": "Maternity Quotes from Husband", "lines": [
                "Watching you become a mother makes me love you in a new way.",
                "You carry our baby with such tenderness and strength.",
                "I am grateful for you, for us, and for the little life we are waiting to meet.",
                "You are already an amazing mother.",
                "Every day, I see your courage more clearly.",
                "Our baby is lucky to have your heart.",
                "Thank you for carrying our greatest blessing.",
                "I cannot wait to see you hold the love you have already given so much to.",
                "You make this journey beautiful, even on the hard days.",
                "I am proud of you, always.",
            ]},
            {"key": "friend", "h2": "Maternity Wishes for a Friend", "lines": [
                "Wishing you a peaceful and beautiful maternity journey.",
                "Your baby is already surrounded by so much love.",
                "May this season bring you comfort, joy, and sweet memories.",
                "You are going to be a wonderful mother.",
                "Sending love to you and the little one growing with you.",
                "May every day of this journey remind you how strong you are.",
                "Your glow is beautiful, but your courage is even brighter.",
                "Wishing you gentle days and happy little moments.",
                "Your baby is blessed to begin life with your love.",
                "So happy for this new chapter in your life.",
            ]},
            {"key": "instagram", "h2": "Maternity Quotes for Instagram", "lines": [
                "Growing our greatest adventure.",
                "A little miracle is making everything feel new.",
                "New chapter, tiny co-author.",
                "My heart has never been this full.",
                "Baby loading, love overflowing.",
                "A soft season with the biggest meaning.",
                "The countdown has never felt sweeter.",
                "Carrying love, hope, and a little bit of wonder.",
                "Life lately: slower steps, fuller heart.",
                "Making room for the sweetest hello.",
            ]},
            {"key": "gift", "h2": "Maternity Gift Ideas with Quotes", "lines": [
                "A maternity quote can feel even sweeter when paired with a thoughtful keepsake.",
                "A delicate pendant can mark the beginning of motherhood in a graceful way.",
                "A bracelet can become an everyday reminder of this special season.",
                "Simple earrings work well for maternity photos and soft celebrations.",
                "Choose a design that feels comfortable, wearable, and personal.",
                "Add a blank card with one heartfelt line instead of a long message.",
                "Avoid price-led wording and focus on the emotion behind the gift.",
                "A keepsake can celebrate the mother-to-be, not just the baby.",
                "The best gift says: this moment matters, and so do you.",
                "Pair the quote with something she can wear beyond this season.",
            ]},
            {"key": "how_to", "h2": "How to Use Maternity Quotes", "lines": [
                "Use short maternity quotes for Instagram captions and WhatsApp status.",
                "Use emotional quotes for journals, letters, and photo albums.",
                "Use gentle wishes when writing to an expecting mom.",
                "Use baby bump captions for maternity shoots and announcement photos.",
                "Keep the quote personal if the message is private.",
                "Avoid advice unless the mother-to-be has asked for it.",
                "Focus on love, patience, courage, and hope.",
                "For public posts, keep private details out of the caption.",
                "For cards, add the expecting mother's name or a shared memory.",
                "The simplest line often feels the most honest.",
            ]},
        ],
        "faqs": [
            ["What are good maternity quotes?", "Good maternity quotes speak about love, waiting, strength, and becoming a mother. A simple line such as Motherhood begins long before the baby is in your arms works well for cards and captions."],
            ["What should I write for a maternity photo caption?", "Write something short and warm, such as growing our greatest adventure or baby on the way, heart already full. Keep the caption personal and easy to read."],
            ["Can I use maternity quotes for Instagram?", "Yes. Maternity quotes work beautifully for Instagram when they are short, sincere, and matched to the photo mood. Baby bump captions, expecting mom lines, and soft motherhood quotes are good choices."],
            ["What is a sweet quote for an expecting mom?", "A sweet quote for an expecting mom is: You are growing life and growing into yourself at the same time. It feels supportive without giving advice."],
            ["How do I write maternity wishes for a friend?", "Keep the message gentle and encouraging. You can write: Wishing you peaceful days, happy memories, and so much love as you wait to meet your little one."],
            ["Can I pair maternity quotes with a gift?", "Yes. A maternity quote with a pendant, bracelet, or earrings can become a thoughtful keepsake for the mother-to-be when the focus stays on emotion, not price."],
        ],
    }

    config = {
        "rank": 98,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-maternityquotes",
        "occasion_year": "Maternity Quotes 2026",
        "carousel_alt_prefix": "maternity quotes 2026 gift idea",
        "gift_h2": "BlueStone Gift Ideas for a Mother-to-Be",
        "gift_blurb": "Maternity quotes often celebrate the mother as much as the baby. These approved BlueStone pieces make gentle keepsakes for a mother-to-be without turning the article into a product catalogue.",
        "conclusion_html": "Maternity quotes are strongest when they sound calm, honest, and personal. Choose a line that fits the photo or card, add one real feeling, and let the message stay simple.",
        "schema_keywords": ["maternity quotes", "pregnancy quotes", "motherhood quotes", "baby bump captions", "expecting mom quotes", "maternity photo captions"],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(csv_rows, "The Melene Evil Eye Pendant", "ProductImages/seo images/Pendants/The Melene Evil Eye Pendant.png"),
            product(csv_rows, "The Kricia Charm Bracelet", "ProductImages/seo images/Bracelet/The Kricia Charm Bracelet.png"),
            product(csv_rows, "The Vicky Hoop Earrings", "ProductImages/seo images/Earrings/The Vicky Hoop Earrings.png"),
            product(csv_rows, "The Haily Ring", "ProductImages/seo images/Rings/The Haily Ring.png"),
            product(csv_rows, "The Malocchio Charm Holder Bracelet", "ProductImages/seo images/Bracelet/The Malocchio Charm Holder Bracelet.png"),
            product(csv_rows, "The Shining Star Bracelet", "ProductImages/seo images/Bracelet/The Shining Star Bracelet.png"),
        ],
        "flatlay_insert_h2": "Pregnancy and Motherhood Quotes",
        "lifestyle_insert_h2": "Maternity Gift Ideas with Quotes",
        "more_reads_html": "Read more heartfelt guides in <a href=\"https://blog.bluestone.com/mother-day-wish-in-hindi-2026/\">mother day wish in Hindi 2026</a>, <a href=\"https://blog.bluestone.com/mother-daughter-quotes-2026/\">mother daughter quotes 2026</a>, <a href=\"https://blog.bluestone.com/friendship-day-photos-2026/\">Friendship Day photos 2026</a>, and <a href=\"https://blog.bluestone.com/new-year-wishes-for-love-2026/\">New Year wishes for love 2026</a>.",
        "how_to_html": "When using maternity quotes, match the tone to the place. Keep Instagram captions short, card messages warm, and private notes more personal.",
        "faq_h2": "Frequently Asked Questions about Maternity Quotes",
        "min_lines": 100,
    }

    hero = consolidated(detail_rows, "The Protecteur Evil Eye Pendant")
    flatlay = consolidated(detail_rows, "The Shining Star Bracelet")
    lifestyle = consolidated(detail_rows, "The Asya Huggie Earrings")

    prompts = {
        "rank": 98,
        "slug": "maternity-quotes-2026",
        "primary_kw": "maternity quotes",
        "output_prefix": PREFIX,
        "caption_occasion": "Maternity quotes",
        "caption_year": "2026",
        "flatlay_setting": "linen-bedside",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/maternity-quotes-hero-2026.webp",
            "flatlay": "output/magnific_generated/maternity-quotes-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/maternity-quotes-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "maternity quotes 2026 hero The Protecteur Evil Eye Pendant",
            "flatlay": "maternity quotes 2026 flatlay The Shining Star Bracelet",
            "lifestyle": "maternity quotes 2026 lifestyle The Asya Huggie Earrings",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                **hero,
                "alt": "maternity quotes 2026 hero with The Protecteur Evil Eye Pendant",
                "caption": "Maternity quotes 2026 vibe: The Protecteur Evil Eye Pendant",
                "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]},
                "cdn": [
                    "https://kinclimg8.bluestone.com/giproduct/BISE0987P01_YAA18DIG6BLTOSIG7_ABCD00-BP-PICS-00000-1024-78991.png",
                    "https://kinclimg7.bluestone.com/giproduct/BISE0987P01_YAA18DIG6BLTOSIG7_ABCD00-PICS-00002-1024-78991.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Protecteur Evil Eye Pendant/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Protecteur Evil Eye Pendant/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": people_prompt(
                    hero,
                    "hero, sitting near a window holding a blank cream maternity journal, gentle visible baby bump suggested under soft fabric",
                    "the yellow gold evil eye pendant",
                    "pendant size on the neck",
                    "Hands rest softly on the blank journal; wrists and fingers are bare; no earrings, no bracelet, no bangles, no rings, no watch, no extra necklace.",
                ),
            },
            "flatlay": {
                **flatlay,
                "alt": "maternity quotes 2026 flatlay with The Shining Star Bracelet",
                "caption": "Maternity quotes 2026 keepsake: The Shining Star Bracelet",
                "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]},
                "cdn": [
                    "https://kinclimg5.bluestone.com/giproduct/BIMG0635V45_YAA18XXXXXXXXXXXX_ABCD00-PICS-00000-1024-47150.png",
                    "https://kinclimg5.bluestone.com/giproduct/BIMG0635V45_YAA18XXXXXXXXXXXX_ABCD00-PICS-00001-1024-47150.png",
                    "https://kinclimg5.bluestone.com/giproduct/BIMG0635V45_YAA18XXXXXXXXXXXX_ABCD00-PICS-00002-1024-47150.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Bracelets/The Shining Star Bracelet/0_primary.png",
                    "ProductImages/raw/Bracelets/The Shining Star Bracelet/2_side_1.png",
                    "ProductImages/raw/Bracelets/The Shining Star Bracelet/3_back.png",
                ],
                "ref_roles": ["primary", "angle", "back"],
                "prompt": (
                    f"Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\n"
                    "Maternity quotes 2026 top-down flatlay. Flatlay setting ID: linen-bedside. Surface and props: "
                    "soft rumpled ivory linen, nightstand edge, closed blank book with no title, dried flower, folded baby-soft cloth with no pattern or text. "
                    "The identical Shining Star Bracelet from @img1, @img2 and @img3 rests naturally on the linen at true PDP scale. "
                    f"Product dimensions from PDP: {flatlay['size_prompt_note']}. Do not enlarge for visibility. "
                    "Full bracelet visible, yellow gold bracelet with star charm and delicate chain, 100 percent identical design, zero distortion, HD metal and stone detail.\n\n"
                    "Props stay secondary. No people, no hands, no logos, no readable text.\n\n"
                    "Avoid: hands, people, floating overlays, cutouts, incorrect bracelet design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI."
                ),
            },
            "lifestyle": {
                **lifestyle,
                "alt": "maternity quotes 2026 lifestyle with The Asya Huggie Earrings",
                "caption": "Maternity quotes 2026 vibe: The Asya Huggie Earrings",
                "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]},
                "cdn": [
                    "https://kinclimg5.bluestone.com/giproduct/BISA0255D05_YAA14DIG6PRWHXXXX_ABCD00-BP-PICS-00000-1024-80521.png",
                    "https://kinclimg5.bluestone.com/giproduct/BISA0255D05_YAA14DIG6PRWHXXXX_ABCD00-PICS-00000-1024-80521.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Earrings/The Asya Huggie Earrings/1_body_portrait.png",
                    "ProductImages/raw/Earrings/The Asya Huggie Earrings/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": people_prompt(
                    lifestyle,
                    "lifestyle, smiling beside a blank cream baby shower card and a closed blank photo album on a linen-covered table",
                    "the yellow gold huggie earrings with pearl and diamond detail",
                    "earring size on the ears",
                    "Bare neck, hands and wrists hidden below frame; no necklace, no pendant, no bracelet, no bangles, no rings, no watch, no other earrings.",
                ),
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 98

Article: Maternity Quotes 2026
Status: Draft assets prepared
Date: 2026-07-24

## A. Intent and Brief
- [x] Primary keyword: maternity quotes
- [x] Sheet Action treated as New
- [x] Fresh slug: maternity-quotes-2026
- [x] 2026 year lock used
- [x] Supporting intent mapped to H2 and FAQ

## B. SEO Structure
- [x] Title/H1 intent prepared
- [x] Yoast title under 60 chars
- [x] Meta description 150 to 160 chars
- [x] Primary keyword in intro and hero alt

## C. Content and Readability
- [x] Direct answer and TL;DR
- [x] 100+ quote/caption/wish lines
- [x] No prices
- [x] No medical claims or advice
- [x] No em dash, en dash, or spaced hyphen intended

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [x] Type 3 prompts prepared with body_image plus design refs for hero and lifestyle
- [x] Fair-skinned Indian casting included for people shots
- [x] Product dimension wording uses product dimensions, not face size
- [x] Filmic style language included
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""

    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json("output/publish_configs/rank98.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")
    print(f"wrote {PREFIX} sections/config/prompts")


if __name__ == "__main__":
    main()
