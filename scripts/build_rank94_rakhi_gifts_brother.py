#!/usr/bin/env python3
"""Build Rank 94 raksha bandhan gifts for brother assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank94_RakhiGiftsBrother"
FILMIC_STYLE = (
    "Visual style: subtle cinematic film grain / analog grain, Kodak Portra color science, "
    "gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, "
    "editorial color grading, natural dynamic range, filmic contrast."
)


def rows_by_name() -> dict[str, dict[str, str]]:
    with (ROOT / "Seo Products - final products (1).csv").open(newline="", encoding="utf-8-sig") as f:
        return {row["Design Name"].strip(): row for row in csv.DictReader(f)}


def product(rows: dict[str, dict[str, str]], name: str, category: str) -> dict[str, str]:
    row = rows[name]
    return {"code": row["Design Code"], "name": name, "url": row["Link"], "png": f"ProductImages/seo images/{category}/{name}.png"}


def write_json(path: str, data: dict) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    rows = rows_by_name()
    sections = {
        "meta": {
            "title": "Raksha Bandhan Gifts for Brother 2026: Unique Ideas",
            "slug": "raksha-bandhan-gifts-for-brother-2026",
            "meta_desc": "Raksha Bandhan gifts for brother 2026 with unique rakhi gift ideas, useful keepsakes, jewellery picks, hampers, cards, and thoughtful surprises today.",
            "focus_kw": "raksha bandhan gifts for brother",
            "yoast_title": "Raksha Bandhan Gifts for Brother 2026",
        },
        "intro": [
            "Raksha Bandhan gifts for brother work best when they feel personal instead of predictable. The right gift says you know his style, his routine, and the kind of affection siblings rarely say directly.",
            "TL;DR: Pick a rakhi or keepsake if he likes meaning, a bracelet or pendant if he wears accessories, a practical hamper if he prefers daily-use gifts, and a handwritten note to make it feel like yours.",
        ],
        "sections": [
            {"key": "best", "h2": "Best Raksha Bandhan Gifts for Brother 2026", "lines": [
                "A modern rakhi with a lasting charm is a thoughtful choice for a brother who likes meaningful details.",
                "A bracelet works well when he prefers something he can wear beyond Raksha Bandhan day.",
                "A pendant suits a brother who already wears a chain or likes subtle accessories.",
                "A band ring can feel timeless for a brother with clean, classic style.",
                "A grooming kit is useful when he prefers practical gifts.",
                "A snack hamper is easy, warm, and safe for a brother who loves food.",
                "A wallet, cardholder, or travel pouch works for everyday use.",
                "A personalised mug or desk item is sweet for a younger brother or college-going sibling.",
                "A fitness accessory can be useful if he already follows that routine.",
                "The best Raksha Bandhan gift is the one he will actually use and remember.",
            ]},
            {"key": "unique", "h2": "Unique Rakhi Gifts for Brother", "lines": [
                "Choose a gift that feels connected to his personality, not only to the festival.",
                "For a protective elder brother, an evil eye rakhi or pendant can feel symbolic.",
                "For a stylish younger brother, a chain bracelet can feel fresh and wearable.",
                "For a minimalist brother, choose one clean design instead of a loud hamper.",
                "For a sentimental brother, add a small note about one memory from childhood.",
                "For a brother living away from home, send a compact gift with sweets and a handwritten card.",
                "For a newly married brother, choose something respectful and refined.",
                "For a brother who dislikes fuss, pick a practical accessory he can use quietly.",
                "Avoid gifts that feel like generic last-minute picks.",
                "A unique gift feels like it was selected for him, not for a list.",
            ]},
            {"key": "jewellery", "h2": "Jewellery Gift Ideas for Brother", "lines": [
                "Jewellery can be a strong Raksha Bandhan gift when it matches his daily style.",
                "A rakhi with a gold or evil eye charm keeps the ritual central.",
                "A bracelet is a good choice if he likes visible but simple accessories.",
                "A pendant can feel meaningful without being too festive.",
                "A band ring works for someone who prefers understated style.",
                "Choose yellow gold for a classic look and rose gold only if it suits his taste.",
                "Look for designs he can wear with shirts, kurtas, and casual outfits.",
                "Avoid oversized pieces if his style is simple.",
                "Do not make the gift message about price.",
                "Let the note say why the piece reminded you of him.",
            ]},
            {"key": "elder", "h2": "Raksha Bandhan Gift Ideas for Elder Brother", "lines": [
                "For an elder brother, choose something respectful, useful, and mature.",
                "A refined bracelet or pendant can feel like a grown-up keepsake.",
                "A formal wallet or cardholder is practical for work life.",
                "A premium pen or desk organiser suits a brother who values routine.",
                "A wellness hamper can be thoughtful if he has a busy schedule.",
                "A watch accessory box works if he already owns watches.",
                "A simple handwritten note can soften even a practical gift.",
                "Thank him for one thing he has done quietly over the years.",
                "Avoid childish designs unless your bond is very playful.",
                "A good elder-brother gift feels warm without becoming dramatic.",
            ]},
            {"key": "younger", "h2": "Raksha Bandhan Gift Ideas for Younger Brother", "lines": [
                "For a younger brother, choose something fun, useful, and not too formal.",
                "A trendy bracelet can work if he likes casual dressing.",
                "A gaming accessory is useful if that is genuinely his interest.",
                "A college backpack organiser or tech pouch can be practical.",
                "A snack box with his favourites is simple and affectionate.",
                "A pendant can work if he already wears chains.",
                "A personalised keychain or desk item can feel playful.",
                "A short funny note often suits younger siblings better than a long emotional card.",
                "Avoid gifts that feel like advice disguised as a present.",
                "Make the gift feel like affection, not supervision.",
            ]},
            {"key": "online", "h2": "Online Raksha Bandhan Gifts for Brother", "lines": [
                "Online gifting helps when your brother lives in another city.",
                "Check delivery timelines before choosing a personalised gift.",
                "Pick compact gifts if the delivery address is an office or hostel.",
                "Add a gift note whenever the website allows it.",
                "Choose jewellery, rakhis, hampers, books, or grooming kits from reliable sellers.",
                "Avoid fragile items if delivery may be rushed.",
                "Confirm his address quietly if you want the gift to be a surprise.",
                "Send the wish separately on Raksha Bandhan morning.",
                "A simple video call can make an online gift feel less distant.",
                "The emotion matters more than the shipping box.",
            ]},
            {"key": "budget", "h2": "Thoughtful Rakhi Gifts Without Overthinking", "lines": [
                "A good gift does not need to look extravagant.",
                "Choose one useful thing and one emotional line.",
                "A simple rakhi with sweets is still meaningful.",
                "A bracelet or pendant can be chosen for style rather than display.",
                "A handwritten card can make even a small gift memorable.",
                "Think about what he already wears, eats, reads, or uses.",
                "Avoid buying something only because it looks festive online.",
                "If he is practical, usefulness may matter more than surprise.",
                "If he is sentimental, the note may matter more than the item.",
                "Thoughtfulness is the real gift upgrade.",
            ]},
            {"key": "cards", "h2": "What to Write with a Raksha Bandhan Gift", "lines": [
                "Start with his name or your sibling nickname.",
                "Thank him for one real thing instead of writing only a general wish.",
                "Mention a childhood memory if the tone feels natural.",
                "Keep the line short if your bond is playful.",
                "Write a warmer paragraph if you both are comfortable with emotion.",
                "Avoid making the card sound like a formal speech.",
                "If the gift is jewellery, connect it with protection, strength, or style.",
                "If the gift is practical, say you wanted him to use it often.",
                "End with a simple Happy Raksha Bandhan.",
                "A sincere card makes the gift feel personal instantly.",
            ]},
            {"key": "last_minute", "h2": "Last-Minute Raksha Bandhan Gifts for Brother", "lines": [
                "If you are shopping late, choose reliable categories instead of risky experiments.",
                "A rakhi, sweets, grooming kit, wallet, or accessory is safer than a highly customised item.",
                "Digital gift cards work if your brother prefers choosing for himself.",
                "A same-day hamper can still feel thoughtful if you add a personal message.",
                "Do not apologise too much in the note.",
                "Make the wish warm and confident.",
                "If delivery may be late, send a message and plan a small follow-up gift.",
                "A phone call can rescue a rushed gift better than fancy packaging.",
                "Keep the choice simple and personal.",
                "Last-minute does not have to mean careless.",
            ]},
            {"key": "how_to_choose", "h2": "How to Choose the Right Gift for Your Brother", "lines": [
                "Start with his age, routine, and style.",
                "Ask whether he likes wearing accessories or prefers practical items.",
                "Notice whether he chooses classic, sporty, festive, or minimal looks.",
                "Choose jewellery only if he is likely to wear it.",
                "Choose food or grooming if he likes useful gifts.",
                "Choose tech only if you know the exact need.",
                "Avoid gifts that create maintenance work for him.",
                "Keep the festival emotion in the note even if the gift is practical.",
                "Do not compare your gift with anyone else's.",
                "The right gift should feel easy for him to accept.",
            ]},
            {"key": "sister", "h2": "Raksha Bandhan Gift from Sister to Brother", "lines": [
                "A sister's gift to her brother can be playful, protective, grateful, or quietly emotional.",
                "If he has always protected you, choose a symbolic design.",
                "If he makes you laugh, add a funny card with the gift.",
                "If he lives far away, send something he can keep near his desk or wardrobe.",
                "If he is newly working, choose something polished and useful.",
                "If he is younger, choose a gift that respects his growing independence.",
                "A rakhi gift does not need to explain the whole relationship.",
                "One honest line can carry years of sibling history.",
                "Let the gift feel like affection without pressure.",
                "That is what makes Raksha Bandhan gifting special.",
            ]},
            {"key": "summary", "h2": "Simple Rakhi Gift Checklist", "lines": [
                "Pick a gift he will use after the festival.",
                "Match the gift to his style, not only to your taste.",
                "Check delivery dates early.",
                "Choose jewellery only with real wearability in mind.",
                "Keep the card personal and short.",
                "Avoid price talk.",
                "Add sweets or a small festive touch if it feels right.",
                "Make sure the rakhi remains central to the emotion.",
                "Call or message him on the day.",
                "The best gift is thoughtful, wearable, useful, or emotionally specific.",
            ]},
        ],
        "section_leads": {},
        "faqs": [
            ["What are the best Raksha Bandhan gifts for brother?", "The best Raksha Bandhan gifts for brother include a meaningful rakhi, bracelet, pendant, wallet, grooming kit, snack hamper, tech accessory, or a useful keepsake with a personal note."],
            ["What is a unique rakhi gift for brother?", "A unique rakhi gift is one that matches his personality, such as an evil eye rakhi for meaning, a bracelet for everyday style, or a compact hamper with his favourite snacks and a handwritten card."],
            ["Can jewellery be a good Raksha Bandhan gift for brother?", "Yes. Jewellery works well if your brother already likes accessories. Choose a bracelet, pendant, ring, or rakhi design that feels wearable beyond the festival."],
            ["What should I gift my elder brother on Raksha Bandhan?", "For an elder brother, choose something mature and useful, such as a refined bracelet, pendant, wallet, desk accessory, grooming kit, or wellness hamper."],
            ["What should I gift my younger brother on Raksha Bandhan?", "For a younger brother, choose something fun and practical, such as a trendy bracelet, tech pouch, snack box, gaming accessory, personalised item, or simple pendant if he wears chains."],
            ["What should I write with a rakhi gift?", "Write one personal line thanking him for a real memory or quality. Keep it natural, then end with a warm Happy Raksha Bandhan."],
        ],
    }

    products = [
        product(rows, "The Protector Evil Eye Rakhi", "Adjustable Bracelets"),
        product(rows, "The Bandhan Bracelet For Him", "Bracelet"),
        product(rows, "The Serenity Evil Eye Pendant For Him", "Pendants"),
        product(rows, "The Talisman Evil Eye Steel Bracelet", "Adjustable Bracelets"),
        product(rows, "The Concatenate Bracelet For Him", "Bracelet"),
        product(rows, "The Jasper Band For Him", "Rings"),
    ]
    config = {
        "rank": 94,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-rakhigiftsbrother",
        "occasion_year": "Raksha Bandhan Gifts for Brother 2026",
        "carousel_alt_prefix": "raksha bandhan gifts for brother 2026 gift idea",
        "gift_h2": "Jewellery Gift Ideas for Brother",
        "gift_blurb": "For Raksha Bandhan, a wearable keepsake can make the ritual feel personal beyond the day itself. These approved BlueStone designs suit brothers who prefer meaningful, wearable gifts without mentioning prices.",
        "conclusion_html": "Raksha Bandhan gifts for brother should feel thoughtful, useful, and true to your sibling bond. Choose the idea that matches his routine, add a personal line, and let the gift carry the warmth you may not say every day.",
        "schema_keywords": ["raksha bandhan gifts for brother", "unique rakhi gifts for brother", "rakhi gift for brother", "raksha bandhan gift ideas for brother", "online rakhi gifts for brother"],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": products,
        "flatlay_insert_h2": "Unique Rakhi Gifts for Brother",
        "lifestyle_insert_h2": "Raksha Bandhan Gift from Sister to Brother",
        "more_reads_html": "Read more Raksha Bandhan ideas in <a href=\"https://blog.bluestone.com/raksha-bandhan-quotes-wishes-in-hindi-2026/\">Raksha Bandhan wishes in Hindi 2026</a>, <a href=\"https://blog.bluestone.com/rakhi-wishes-2026/\">rakhi wishes 2026</a>, <a href=\"https://blog.bluestone.com/birthday-wishes-for-cousin-2026/\">birthday wishes for cousin 2026</a>, and <a href=\"https://blog.bluestone.com/husband-birthday-wishes-2026/\">husband birthday wishes 2026</a>.",
        "how_to_html": "To choose a Raksha Bandhan gift for brother, start with his daily routine, then match the gift to his style. Add one personal line so the gift feels chosen, not generic.",
        "faq_h2": "Frequently Asked Questions about Raksha Bandhan Gifts for Brother",
        "min_lines": 100,
        "section_leads": {},
    }

    prompts = {
        "rank": 94,
        "slug": "raksha-bandhan-gifts-for-brother-2026",
        "output_prefix": PREFIX,
        "occasion": "Raksha Bandhan Gifts for Brother 2026",
        "primary_kw": "raksha bandhan gifts for brother",
        "caption_occasion": "Raksha Bandhan gifts for brother",
        "caption_year": "2026",
        "flatlay_setting": "gift-wrapping-station",
        "workflow": "Higgsfield MCP nano_banana_pro. Campaign hybrid with mandatory body_image scale line for people shots. Do not generate until balance succeeds. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/raksha-bandhan-gifts-for-brother-hero-2026.webp",
            "flatlay": "output/magnific_generated/raksha-bandhan-gifts-for-brother-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/raksha-bandhan-gifts-for-brother-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "raksha bandhan gifts for brother 2026 hero The Protector Evil Eye Rakhi",
            "flatlay": "raksha bandhan gifts for brother 2026 flatlay The Bandhan Bracelet For Him",
            "lifestyle": "raksha bandhan gifts for brother 2026 lifestyle The Serenity Evil Eye Pendant For Him",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                "code": "BIHM1002V07", "name": "The Protector Evil Eye Rakhi", "gender": "Male", "height_mm": 9.8, "width_mm": 10.21,
                "size_prompt_note": "rakhi product height 9.8 mm and width 10.21 mm; product dimensions, not face size; copy worn wrist scale from body_image",
                "alt": "raksha bandhan gifts for brother 2026 hero with The Protector Evil Eye Rakhi",
                "caption": "Raksha Bandhan gifts for brother 2026 vibe: The Protector Evil Eye Rakhi",
                "product": {"code": "BIHM1002V07", "name": "The Protector Evil Eye Rakhi", "pdp": rows["The Protector Evil Eye Rakhi"]["Link"]},
                "cdn": ["https://kinclimg4.bluestone.com/f_jpg,c_scale,w_1024,b_rgb:f0f0f0/giproduct/BIHM1002V07_YAA14XXXXXXXXXXXX_ABCD00-PICS-00001-1024-80608.png", "https://kinclimg4.bluestone.com/f_jpg,c_scale,w_1024,b_rgb:f0f0f0/giproduct/BIHM1002V07_YAA14XXXXXXXXXXXX_ABCD00-PICS-00000-1024-80608.png"],
                "local_reference_images": ["ProductImages/raw/Adjustable Bracelets/The Protector Evil Eye Rakhi/1_body_portrait.png", "ProductImages/raw/Adjustable Bracelets/The Protector Evil Eye Rakhi/0_primary.png"],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} Raksha Bandhan gifts for brother 2026 hero, a fair-skinned Indian adult sister tying rakhi on her fair-skinned adult Indian brother in a warm modern Indian living room. The brother is the clear wearer. Full heads, full faces, both smiles, brother wrist, rakhi, sister hands, and upper bodies visible with safe margins. Exactly two adult siblings, familial mood, no children. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, warm daylight, realistic shadows, 16:9.\n\nThe brother physically wears The Protector Evil Eye Rakhi from @img1 body_image and @img2 design on his wrist. GENDER LOCK: Male SKU on adult man only. Product dimensions from PDP: rakhi product height_mm=9.8 and width_mm=10.21. These are real product dimensions, NOT face-size instructions. Keep rakhi size on the wrist like @img1 body_image worn wrist scale: subtle rakhi size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the yellow gold evil eye rakhi with blue-white centre and red thread exactly, 100 percent identical to refs, zero distortion, HD metal and thread detail. This rakhi is the single and only jewellery in the image. Bare fingers, no watches, no bracelets, no rings, no earrings, no necklaces on anyone. No readable text anywhere.\n\nAvoid: cropped face, cropped head, child, extra people, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow.",
            },
            "flatlay": {
                "code": "BISV0910V12", "name": "The Bandhan Bracelet For Him", "gender": "Male", "height_mm": 177.8, "width_mm": 11.94,
                "size_prompt_note": "bracelet product length 177.8 mm and width 11.94 mm; product dimensions, not face size",
                "alt": "raksha bandhan gifts for brother 2026 flatlay with The Bandhan Bracelet For Him",
                "caption": "Raksha Bandhan gifts for brother 2026 keepsake: The Bandhan Bracelet For Him",
                "product": {"code": "BISV0910V12", "name": "The Bandhan Bracelet For Him", "pdp": rows["The Bandhan Bracelet For Him"]["Link"]},
                "cdn": ["https://kinclimg6.bluestone.com/giproduct/BISV0910V12_YAA18DIG6XXXXXXXX_ABCD00-PICS-00002-1024-99180.png", "https://kinclimg6.bluestone.com/giproduct/BISV0910V12_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-99180.png", "https://kinclimg6.bluestone.com/giproduct/BISV0910V12_YAA18DIG6XXXXXXXX_ABCD00-PICS-00001-1024-99180.png"],
                "local_reference_images": ["ProductImages/raw/Bracelets/The Bandhan Bracelet For Him/0_primary.png"],
                "ref_roles": ["primary", "angle", "angle"],
                "prompt": f"Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\nRaksha Bandhan gifts for brother 2026 top-down flatlay. Flatlay setting ID: gift-wrapping-station. Warm wooden gift-wrapping desk with marigold petals, roli rice bowl, blank cream card, neutral ribbon, and soft festive fabric. The identical Bandhan Bracelet For Him from @img1, @img2 and @img3 rests naturally on the surface at true PDP scale. Product dimensions from PDP: bracelet product length_mm=177.8 and width_mm=11.94. These are product dimensions, NOT face-size instructions. Do not enlarge for visibility. Full bracelet visible, polished yellow gold link bracelet with diamond-studded connectors, 100 percent identical design, zero distortion, HD metal and stone detail.\n\nProps stay secondary. No people, no hands, no logos, no readable text.\n\nAvoid: hands, people, floating overlays, cutouts, incorrect bracelet design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI.",
            },
            "lifestyle": {
                "code": "BIPO0987P67", "name": "The Serenity Evil Eye Pendant For Him", "gender": "Male", "height_mm": 30.87, "width_mm": 15.91,
                "size_prompt_note": "pendant product height 30.87 mm and width 15.91 mm; product dimensions, not face size; copy worn neck scale from body_image",
                "alt": "raksha bandhan gifts for brother 2026 lifestyle with The Serenity Evil Eye Pendant For Him",
                "caption": "Raksha Bandhan gifts for brother 2026 vibe: The Serenity Evil Eye Pendant For Him",
                "product": {"code": "BIPO0987P67", "name": "The Serenity Evil Eye Pendant For Him", "pdp": rows["The Serenity Evil Eye Pendant For Him"]["Link"]},
                "cdn": ["https://kinclimg8.bluestone.com/giproduct/BIPO0987P67_YAA18DIG6SYBSXXXX_ABCD00-BP-PICS-00000-1024-90209.png", "https://kinclimg8.bluestone.com/giproduct/BIPO0987P67_YAA18DIG6SYBSXXXX_ABCD00-PICS-00003-1024-90209.png"],
                "local_reference_images": ["ProductImages/raw/Pendants/The Serenity Evil Eye Pendant For Him/1_body_portrait.png", "ProductImages/raw/Pendants/The Serenity Evil Eye Pendant For Him/0_primary.png"],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} Raksha Bandhan gifts for brother 2026 lifestyle, solo fair-skinned Indian adult man in a bright home sitting near a festive gift tray with a blank rakhi card and marigold petals. Full head, full face, both eyes, complete smile, neck, pendant, blank card, and upper body visible with safe margins. Hands and wrists hidden below frame to prevent extra jewellery. Exactly one adult man in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, warm daylight, realistic shadows, 16:9.\n\nThe man physically wears The Serenity Evil Eye Pendant For Him from @img1 body_image and @img2 design on a fine chain at upper chest. GENDER LOCK: Male For Him product on adult man only. Product dimensions from PDP: pendant product height_mm=30.87 and width_mm=15.91. These are real product dimensions, NOT face-size instructions. Keep pendant size on the neck like @img1 body_image worn neck scale: subtle pendant size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the rectangular yellow gold evil eye pendant with blue centre and diamond border exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery in the image. Bare ears, no watches, no bracelets, no rings, no extra necklaces. No readable text anywhere.\n\nAvoid: visible wrists, visible fingers, cropped face, cropped head, woman wearer, child, second person, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow.",
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 94

Article: Raksha Bandhan Gifts for Brother 2026
Status: Local build ready; pending publish, Type 3 generation, live verification
Date: 2026-07-24

## A. Intent and Brief
- [x] Primary keyword: raksha bandhan gifts for brother
- [x] Sheet Optimize treated as New
- [x] Fresh slug: raksha-bandhan-gifts-for-brother-2026
- [x] 2026 year lock used

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [x] Type 3 prompts include body_image + design for people shots
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""
    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json("output/publish_configs/rank94.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / f"output/{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")
    print(f"Built {PREFIX}")


if __name__ == "__main__":
    main()
