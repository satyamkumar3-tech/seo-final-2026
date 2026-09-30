#!/usr/bin/env python3
"""Build Rank 100 Rakhi for bhaiya bhabhi assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank100_RakhiBhaiyaBhabhi"
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


def main() -> None:
    csv_rows = rows_by_name("Seo Products - final products (1).csv")
    detail_rows = rows_by_name("KnowledgeBase/Product/Seo Products - consolidated.csv")

    sections = {
        "meta": {
            "title": "Rakhi for Bhaiya Bhabhi 2026: Gift Ideas",
            "slug": "rakhi-for-bhaiya-bhabhi-2026",
            "meta_desc": "Rakhi for bhaiya bhabhi 2026 gift ideas with rakhi sets, couple keepsakes, bhaiya gifts, bhabhi gifts, thali tips, messages, and shopping checklist for 2026.",
            "focus_kw": "rakhi for bhaiya bhabhi",
            "yoast_title": "Rakhi for Bhaiya Bhabhi 2026: Gift Ideas",
        },
        "intro": [
            "Rakhi for bhaiya bhabhi is about celebrating two people who make the family bond warmer: your brother and the sister-in-law who became part of the tradition.",
            "TL;DR: choose one rakhi or bracelet for bhaiya, one wearable keepsake for bhabhi, add a simple note, and keep the gift thoughtful rather than flashy.",
        ],
        "sections": [
            {"key": "best", "h2": "Rakhi for Bhaiya Bhabhi", "lines": [
                "Pick a rakhi design for bhaiya that he can wear beyond the ceremony.",
                "Choose a bhabhi gift that feels graceful, comfortable, and not too loud.",
                "Keep the pair balanced: one meaningful piece for him and one elegant keepsake for her.",
                "A shared card can make the gift feel warmer than two separate packets.",
                "If bhaiya likes minimal style, choose a bracelet or rakhi with clean details.",
                "If bhabhi likes daily wear, choose a pendant, earrings, or charm bracelet.",
                "A rakhi thali, sweets, and a blank note keep the moment festive without overdoing it.",
                "Avoid random gifts that do not match their lifestyle.",
                "The best choice feels personal, wearable, and easy to remember.",
                "Think of the gift as a memory of Raksha Bandhan 2026, not just a festival purchase.",
            ]},
            {"key": "set_ideas", "h2": "Rakhi Set Ideas for Bhaiya and Bhabhi", "lines": [
                "Pair an evil eye rakhi for bhaiya with a delicate pendant for bhabhi.",
                "Pair a gold bracelet for bhaiya with huggie earrings for bhabhi.",
                "Pair a simple rakhi with a charm bracelet if bhabhi likes meaningful details.",
                "Choose matching metal tones if you want the gifts to feel like a set.",
                "Keep both gifts in one festive tray with separate name cards.",
                "For newly married bhaiya bhabhi, choose softer and more classic designs.",
                "For a practical couple, choose everyday pieces instead of heavy occasion wear.",
                "For long-distance gifting, add a message card and delivery note.",
                "If only one main gift is possible, choose the rakhi first and add a thoughtful card for bhabhi.",
                "A balanced set should feel equal in thought, even if the products are different.",
            ]},
            {"key": "bhaiya", "h2": "Rakhi Gift Ideas for Bhaiya", "lines": [
                "An adjustable rakhi bracelet works well if he likes festive pieces with daily use.",
                "A steel or gold bracelet can become a cleaner post-festival keepsake.",
                "A simple chain suits brothers who avoid loud jewellery.",
                "A pendant for him works if his style is casual and minimal.",
                "Choose a design that does not clash with his watch or everyday accessories.",
                "For elder bhaiya, keep the look mature and understated.",
                "For younger bhaiya, a modern bracelet can feel more natural.",
                "If he travels often, choose a secure bracelet design.",
                "Avoid oversized pieces if he does not already wear jewellery.",
                "Add a short note about protection, support, and sibling memories.",
            ]},
            {"key": "bhabhi", "h2": "Rakhi Gift Ideas for Bhabhi", "lines": [
                "A pendant is a graceful choice when you want something personal but easy to wear.",
                "Huggie earrings work well for bhabhi if she prefers everyday elegance.",
                "A charm bracelet can feel warm, personal, and family oriented.",
                "Choose designs she can wear with Indian and western outfits.",
                "Avoid guessing sizes unless you are sure about rings or bangles.",
                "If she is new to the family, keep the design classic and safe.",
                "If she likes colour, choose a subtle stone accent rather than a very loud piece.",
                "A simple note can make the gift feel more personal.",
                "For a bhabhi who does not wear much jewellery, choose lightweight designs.",
                "A thoughtful bhabhi gift says she is part of the Rakhi bond too.",
            ]},
            {"key": "newly_married", "h2": "Rakhi for Newly Married Bhaiya Bhabhi", "lines": [
                "For a newly married couple, keep the gifting warm and inclusive.",
                "Choose a rakhi for bhaiya and a soft welcome-style keepsake for bhabhi.",
                "Avoid overly private jokes if the relationship is still new.",
                "A handwritten card can make the first Rakhi after marriage feel special.",
                "Pick classic pieces that do not feel too experimental.",
                "Include sweets, roli, rice, and a clean thali for the ceremony.",
                "A couple gift can be useful, but separate wearable pieces feel more personal.",
                "Mention how happy you are to celebrate with both of them.",
                "Keep the tone respectful, affectionate, and family-first.",
                "The goal is to make bhabhi feel included, not like an afterthought.",
            ]},
            {"key": "premium", "h2": "Premium Rakhi Gifts for Bhaiya Bhabhi", "lines": [
                "Premium gifting works best when it still feels wearable.",
                "Choose fine metal, neat finish, and versatile styling over large size.",
                "For bhaiya, a clean bracelet can feel premium without being flashy.",
                "For bhabhi, a pendant or earrings can feel elegant and personal.",
                "Use a good gift box and a blank card instead of too many decorative extras.",
                "Do not write price-led copy in the message.",
                "Mention the reason you chose the design, not the cost.",
                "Premium does not have to mean heavy.",
                "A refined piece is more likely to be worn after Rakhi.",
                "The best premium gift feels thoughtful before it feels expensive.",
            ]},
            {"key": "budget", "h2": "Thoughtful Rakhi Gifts Without Overthinking", "lines": [
                "A simple rakhi with a sincere card can still feel complete.",
                "Choose one strong keepsake instead of many small fillers.",
                "A compact pendant or bracelet can feel more useful than decorative hampers.",
                "If budget is tight, focus on presentation and message.",
                "Add homemade sweets or a printed photo if it suits the family mood.",
                "A small but thoughtful gift beats a random expensive one.",
                "Choose practical designs they can repeat.",
                "Do not compare your gift with anyone else's.",
                "A warm note can carry the emotion of the festival.",
                "The thought matters most when the gift is chosen with care.",
            ]},
            {"key": "long_distance", "h2": "Long Distance Rakhi for Bhaiya Bhabhi", "lines": [
                "Send the rakhi early so it reaches before 28 August 2026.",
                "Add a short message for both bhaiya and bhabhi.",
                "Choose easy-to-wear pieces that do not need size adjustments.",
                "Use a delivery address where someone will be available.",
                "Avoid fragile decorations if shipping is long-distance.",
                "Send a photo or video message on the day of Rakhi.",
                "Keep the card simple and personal.",
                "If you cannot send sweets, add a warm blessing in the note.",
                "A bracelet or pendant can travel better than a delicate hamper.",
                "Distance changes the delivery, not the feeling.",
            ]},
            {"key": "messages", "h2": "Messages to Write with Rakhi for Bhaiya Bhabhi", "lines": [
                "Happy Raksha Bandhan to my dearest bhaiya and bhabhi. You both make family feel complete.",
                "Bhaiya, thank you for always standing by me. Bhabhi, thank you for adding so much warmth to our home.",
                "Wishing you both a Rakhi filled with love, laughter, and sweet memories.",
                "This Rakhi is for the bond we grew up with and the family bond we now celebrate together.",
                "To bhaiya and bhabhi, may your home always stay blessed and happy.",
                "Thank you for being my support system and my favourite team.",
                "Happy Rakhi 2026. Sending love, respect, and a little festive sparkle.",
                "May this Raksha Bandhan bring protection, joy, and togetherness to both of you.",
                "Bhabhi, thank you for making bhaiya's world warmer and our family happier.",
                "Bhaiya, this rakhi carries all my childhood memories and all my prayers for you.",
            ]},
            {"key": "captions", "h2": "Rakhi Captions for Bhaiya Bhabhi", "lines": [
                "Rakhi love for my favourite bhaiya bhabhi duo.",
                "A thread for bhaiya, a blessing for bhabhi.",
                "Family feels fuller with both of you.",
                "Raksha Bandhan 2026, love wrapped in tradition.",
                "Bhaiya bhabhi, my forever festive team.",
                "One rakhi, many memories.",
                "Sibling love, family warmth, festive smiles.",
                "For the brother who protects and the bhabhi who cares.",
                "Rakhi moments with my favourite couple.",
                "Tradition, sweets, and a lot of love.",
            ]},
            {"key": "checklist", "h2": "How to Choose Rakhi for Bhaiya Bhabhi", "lines": [
                "Start with bhaiya's actual wearing style.",
                "Choose bhabhi's gift around comfort and daily use.",
                "Check metal tone, size needs, and closure type before buying.",
                "Avoid designs that are too delicate for regular wear.",
                "Keep the gift card blank until you write a personal note.",
                "Use one theme across the packaging so the set feels planned.",
                "Do not add too many unrelated products.",
                "Keep the ceremony thali neat and uncluttered.",
                "Add sweets only if delivery timing is safe.",
                "Choose the gift at least a few days before Raksha Bandhan.",
            ]},
        ],
        "faqs": [
            ["What is the best rakhi for bhaiya bhabhi?", "The best rakhi for bhaiya bhabhi is a balanced set: a rakhi or bracelet for bhaiya and a wearable keepsake such as a pendant, earrings, or charm bracelet for bhabhi. Keep both pieces practical and personal."],
            ["What can I gift bhabhi on Rakhi?", "You can gift bhabhi a pendant, huggie earrings, charm bracelet, or another lightweight daily-wear keepsake. Add a short note so she feels included in the Raksha Bandhan celebration."],
            ["Should I buy one gift or two gifts for bhaiya bhabhi?", "Two small, thoughtful gifts usually feel better than one random large gift. Choose a rakhi or bracelet for bhaiya and a separate elegant piece for bhabhi."],
            ["What should I write with rakhi for bhaiya bhabhi?", "Write a warm line for both of them, such as: Happy Raksha Bandhan to my dearest bhaiya and bhabhi. You both make family feel complete."],
            ["When is Raksha Bandhan 2026?", "Raksha Bandhan 2026 falls on Friday, 28 August 2026. If you are sending rakhi to bhaiya bhabhi by courier, plan the order a few days earlier."],
            ["What jewellery is good for Rakhi gifting?", "Bracelets, adjustable rakhis, pendants, earrings, and simple chains work well for Rakhi gifting when the design matches the person's daily style and comfort."],
        ],
    }

    config = {
        "rank": 100,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-rakhibhaiyabhabhi",
        "occasion_year": "Raksha Bandhan 2026",
        "carousel_alt_prefix": "rakhi for bhaiya bhabhi 2026 gift idea",
        "gift_h2": "BlueStone Rakhi Gift Ideas for Bhaiya Bhabhi",
        "gift_blurb": "For bhaiya bhabhi, the softest gifting route is a balanced pair: one rakhi or bracelet for him and one graceful wearable piece for her.",
        "conclusion_html": "Rakhi for bhaiya bhabhi works best when it feels balanced, warm, and easy to wear. Choose around their everyday style, add one sincere note, and let the Raksha Bandhan 2026 memory feel personal.",
        "schema_keywords": ["rakhi for bhaiya bhabhi", "rakhi set for bhaiya bhabhi", "raksha bandhan gifts for bhaiya bhabhi", "bhabhi rakhi gift", "rakhi gift for bhaiya"],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(csv_rows, "The Protector Evil Eye Rakhi", "ProductImages/seo images/Adjustable Bracelets/The Protector Evil Eye Rakhi.png"),
            product(csv_rows, "The Talisman Evil Eye Steel Bracelet", "ProductImages/seo images/Adjustable Bracelets/The Talisman Evil Eye Steel Bracelet.png"),
            product(csv_rows, "The Bandhan Bracelet For Him", "ProductImages/seo images/Bracelet/The Bandhan Bracelet For Him.png"),
            product(csv_rows, "The Aagarna Pendant", "ProductImages/seo images/Pendants/The Aagarna Pendant.png"),
            product(csv_rows, "The Nettile Huggie Earrings", "ProductImages/seo images/Earrings/The Nettile Huggie Earrings.png"),
            product(csv_rows, "The Kricia Charm Bracelet", "ProductImages/seo images/Bracelet/The Kricia Charm Bracelet.png"),
        ],
        "flatlay_insert_h2": "Rakhi Set Ideas for Bhaiya and Bhabhi",
        "lifestyle_insert_h2": "Rakhi Gift Ideas for Bhabhi",
        "more_reads_html": "Read more Raksha Bandhan guides in <a href=\"https://blog.bluestone.com/raksha-bandhan-gifts-for-brother-2026/\">Raksha Bandhan gifts for brother 2026</a>, <a href=\"https://blog.bluestone.com/rakhi-wishes-2026/\">Rakhi wishes 2026</a>, <a href=\"https://blog.bluestone.com/raksha-bandhan-wishes-in-hindi-2026/\">Raksha Bandhan wishes in Hindi 2026</a>, and <a href=\"https://blog.bluestone.com/friendship-day-shayari-2026/\">Friendship Day shayari 2026</a>.",
        "how_to_html": "For date planning, Raksha Bandhan 2026 falls on Friday, 28 August 2026. You can also read a short festival background on <a href=\"https://www.britannica.com/topic/Raksha-Bandhan\">Britannica</a>. Order early if you are sending rakhi to another city.",
        "faq_h2": "Frequently Asked Questions about Rakhi for Bhaiya Bhabhi",
        "min_lines": 100,
    }

    hero = consolidated(detail_rows, "The Protector Evil Eye Rakhi")
    flatlay = consolidated(detail_rows, "The Kricia Charm Bracelet")
    lifestyle = consolidated(detail_rows, "The Aagarna Pendant")

    prompts = {
        "rank": 100,
        "slug": "rakhi-for-bhaiya-bhabhi-2026",
        "primary_kw": "rakhi for bhaiya bhabhi",
        "output_prefix": PREFIX,
        "caption_occasion": "Rakhi for bhaiya bhabhi",
        "caption_year": "2026",
        "flatlay_setting": "rakhi-thali",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/rakhi-for-bhaiya-bhabhi-hero-2026.webp",
            "flatlay": "output/magnific_generated/rakhi-for-bhaiya-bhabhi-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/rakhi-for-bhaiya-bhabhi-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "rakhi for bhaiya bhabhi 2026 hero The Protector Evil Eye Rakhi",
            "flatlay": "rakhi for bhaiya bhabhi 2026 flatlay The Kricia Charm Bracelet",
            "lifestyle": "rakhi for bhaiya bhabhi 2026 lifestyle The Aagarna Pendant",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                **hero,
                "alt": "rakhi for bhaiya bhabhi 2026 hero with The Protector Evil Eye Rakhi",
                "caption": "Rakhi for bhaiya bhabhi 2026 vibe: The Protector Evil Eye Rakhi",
                "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]},
                "cdn": [
                    "https://kinclimg4.bluestone.com/giproduct/BIHM1002V07_YAA14XXXXXXXXXXXX_ABCD00-BP-PICS-00000-1024-80608.png",
                    "https://kinclimg4.bluestone.com/giproduct/BIHM1002V07_YAA14XXXXXXXXXXXX_ABCD00-PICS-00000-1024-80608.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Adjustable Bracelets/The Protector Evil Eye Rakhi/1_body_portrait.png",
                    "ProductImages/raw/Adjustable Bracelets/The Protector Evil Eye Rakhi/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} Rakhi for bhaiya bhabhi 2026 hero, warm modern Indian living room rakhi ceremony. "
                    "A fair-skinned Indian adult sister ties rakhi on her fair-skinned adult Indian brother's wrist while bhabhi sits nearby smiling softly. Exactly three adults only: sister, bhaiya, bhabhi. Full heads, full faces, brother wrist, rakhi, and upper bodies visible with safe margins. No children, no extra people. 85mm DSLR look, natural skin texture, warm daylight, 16:9.\n\n"
                    f"The brother physically wears {hero['name']} from @img1 body_image and @img2 design on his wrist. GENDER LOCK: Male SKU on adult man only. Product dimensions from PDP: {hero['size_prompt_note']}. Keep rakhi size on the wrist like @img1 body_image worn scale: small natural rakhi size, not enlarged. Use @img2 only for jewellery design.\n\n"
                    "Replicate the yellow gold evil eye rakhi with blue-white centre and thread detail exactly, 100 percent identical to refs, zero distortion, HD metal and thread detail. This rakhi is the single and only jewellery in the entire image. Everyone else has bare neck, bare ears, bare wrists, bare fingers, no rings, no bracelets, no bangles, no watches, no necklaces. No readable text anywhere. Any card or gift tag must be blank.\n\n"
                    "Avoid: extra jewellery, visible rings, watches, cropped faces, cropped heads, child, extra people, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow."
                ),
            },
            "flatlay": {
                **flatlay,
                "alt": "rakhi for bhaiya bhabhi 2026 flatlay with The Kricia Charm Bracelet",
                "caption": "Rakhi for bhaiya bhabhi 2026 keepsake: The Kricia Charm Bracelet",
                "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]},
                "cdn": [
                    "https://kinclimg1.bluestone.com/giproduct/BIPO0730V39_YAA18DIG6SYEMSYBS_ABCD00-PICS-00000-1024-52474.png",
                    "https://kinclimg8.bluestone.com/giproduct/BIPO0730V39_YAA18DIG6SYEMSYBS_ABCD00-PICS-00001-1024-52474.png",
                    "https://kinclimg5.bluestone.com/giproduct/BIPO0730V39_YAA18DIG6SYEMSYBS_ABCD00-PICS-00002-1024-52474.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Bracelets/The Kricia Charm Bracelet/0_primary.png",
                    "ProductImages/raw/Bracelets/The Kricia Charm Bracelet/2_side_1.png",
                    "ProductImages/raw/Bracelets/The Kricia Charm Bracelet/3_back.png",
                ],
                "ref_roles": ["primary", "angle", "back"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\n"
                    "Rakhi for bhaiya bhabhi 2026 top-down flatlay. Flatlay setting ID: rakhi-thali. Surface and props: brass rakhi thali, roli chawal bowl, diya unlit, marigold petals, sweets, and a completely blank cream gift card. "
                    "The identical Kricia Charm Bracelet from @img1, @img2 and @img3 rests naturally on the thali at true PDP scale. "
                    f"Product dimensions from PDP: {flatlay['size_prompt_note']}. Do not enlarge for visibility. Full bracelet visible, yellow gold charm bracelet with green stone accents, 100 percent identical design, zero distortion, HD metal and stone detail.\n\n"
                    "Props stay secondary. No people, no hands, no logos, no readable text, no letters, no numbers, no other jewellery.\n\n"
                    "Avoid: hands, people, floating overlays, cutouts, incorrect bracelet design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI."
                ),
            },
            "lifestyle": {
                **lifestyle,
                "alt": "rakhi for bhaiya bhabhi 2026 lifestyle with The Aagarna Pendant",
                "caption": "Rakhi for bhaiya bhabhi 2026 vibe: The Aagarna Pendant",
                "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]},
                "cdn": [
                    "https://kinclimg4.bluestone.com/giproduct/BIIP0550P16_YAA14DIG6SYEMXXXX_ABCD00-BP-PICS-00000-1024-42508.png",
                    "https://kinclimg8.bluestone.com/giproduct/BIIP0550P16_YAA14DIG6SYEMXXXX_ABCD00-PICS-00001-1024-42508.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Aagarna Pendant/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Aagarna Pendant/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} Rakhi for bhaiya bhabhi 2026 lifestyle, solo fair-skinned Indian adult bhabhi sitting near a festive coffee table with a completely blank rakhi card and small gift box, warm modern Indian home, soft respectful smile, full head, full face, upper body and jewellery area visible with safe margins. Exactly one person only. 85mm DSLR look, natural skin texture, warm daylight, 16:9.\n\n"
                    f"The woman physically wears {lifestyle['name']} from @img1 body_image and @img2 design only on her neck. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: {lifestyle['size_prompt_note']}. Keep pendant size on the neck like @img1 body_image worn scale: subtle real PDP size, not enlarged. Use @img2 only for jewellery design.\n\n"
                    "Replicate the yellow gold emerald and diamond pendant exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery in the entire image. No earrings, no rings, no bracelet, no bangle, no watch, no extra necklace. Hands should be hidden below frame or resting under the table, no fingers visible. No readable text anywhere. Any card, gift tag, phone, or paper must be completely blank.\n\n"
                    "Avoid: visible rings, visible fingers, cropped face, cropped head, readable text, letters, numbers, logo, man wearer, child, second person, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow."
                ),
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 100

Article: Rakhi for Bhaiya Bhabhi 2026
Status: Draft assets prepared
Date: 2026-07-27

## A. Intent and Brief
- [x] Primary keyword: rakhi for bhaiya bhabhi
- [x] Sheet Action treated as New
- [x] Fresh slug: rakhi-for-bhaiya-bhabhi-2026
- [x] 2026 year lock used
- [x] Supporting keyword mapped to H2 and FAQ

## B. SEO Structure
- [x] Title/H1 intent prepared
- [x] Yoast title under 60 chars
- [x] Meta description 150 to 160 chars
- [x] Primary keyword in intro and hero alt

## C. Content and Readability
- [x] Direct answer and TL;DR
- [x] 100+ gift idea/message/checklist lines
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
    write_json("output/publish_configs/rank100.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")
    print(f"wrote {PREFIX} sections/config/prompts")


if __name__ == "__main__":
    main()
