#!/usr/bin/env python3
"""Build Week 3-4 Rank 3 Rakhi wishes to brother assets."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week34_Rank3_RakhiWishesBrother"
FILMIC_STYLE = (
    "Visual style: subtle cinematic film grain / analog grain, Kodak Portra color science, "
    "gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, "
    "editorial color grading, natural dynamic range, filmic contrast."
)


def load_csv(path: str) -> dict[str, dict[str, str]]:
    with (ROOT / path).open(newline="", encoding="utf-8-sig") as f:
        return {row["Design Name"].strip(): row for row in csv.DictReader(f)}


def product(rows: dict[str, dict[str, str]], name: str, png: str) -> dict[str, str]:
    row = rows[name]
    return {"code": row["Design Code"], "name": name, "url": row["Link"], "png": png}


def consolidated(rows: dict[str, dict[str, str]], name: str) -> dict[str, object]:
    row = rows[name]
    size_note = (
        row["size_prompt_note"]
        or f"product_height_mm={row['height_mm']}; product_width_mm={row['width_mm']}; these are product dimensions, not face-size instructions"
    )
    size_note = size_note.replace("face_height_mm", "product_height_mm").replace("face_width_mm", "product_width_mm")
    return {
        "code": row["Design Code"],
        "name": name,
        "gender": row["GenderTag"],
        "category": row["DesignCategory"],
        "height_mm": float(row["height_mm"]),
        "width_mm": float(row["width_mm"]),
        "size_prompt_note": size_note,
        "pdp": row["Link"],
        "cdn_primary": row["Image link"],
    }


def write_json(path: str, data: object) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    product_rows = load_csv("Seo Products - final products (1).csv")
    detail_rows = load_csv("Seo Products - consolidated.csv")

    sections = {
        "meta": {
            "title": "Happy Rakhi Wishes to Brother 2026",
            "slug": "happy-rakhi-wishes-to-brother-2026",
            "meta_desc": "Happy Rakhi wishes to brother 2026 with quotes, messages, notes, captions, short lines, funny wishes, emotional Rakhi words, and gift ideas for brothers.",
            "focus_kw": "happy rakhi wishes to brother",
            "yoast_title": "Happy Rakhi Wishes to Brother 2026",
        },
        "intro": [
            "Happy Rakhi wishes to brother feel best when they sound protective, playful, grateful, and personal. In 2026, Raksha Bandhan falls on Friday, August 28, so this guide gives you ready lines for cards, WhatsApp, Instagram captions, and a small note to send with a gift.",
            "TL;DR: Use emotional Rakhi wishes for an elder brother, funny Rakhi messages for a close brother, short Rakhi quotes for captions, and a simple handwritten note when you are sending a rakhi or jewellery gift.",
        ],
        "sections": [
            {
                "key": "wishes",
                "h2": "Happy Rakhi Wishes to Brother",
                "lines": [
                    "Happy Rakhi, brother. May your life stay full of strength, peace, and good news.",
                    "Wishing you a Raksha Bandhan filled with love, laughter, and every blessing you deserve.",
                    "Happy Rakhi to the brother who makes every memory louder, warmer, and safer.",
                    "May this Rakhi remind you how deeply you are loved and how proudly you are celebrated.",
                    "Happy Raksha Bandhan 2026. May our bond keep growing with every passing year.",
                    "To my brother, my first teammate and forever protector, Happy Rakhi.",
                    "May this thread carry prayers for your happiness, health, and success.",
                    "Happy Rakhi. Thank you for being my safe place and my favourite troublemaker.",
                    "Wishing you a bright Raksha Bandhan and a year full of steady wins.",
                    "May your days be strong, your heart be light, and your dreams move forward.",
                ],
            },
            {
                "key": "quotation",
                "h2": "Rakhi Quotation for Brother",
                "lines": [
                    "A rakhi is small, but the bond it carries can hold a lifetime.",
                    "A brother is the person who turns protection into love without making a speech.",
                    "Rakhi is not only a thread. It is memory, promise, prayer, and home.",
                    "Some bonds are not loud every day, but they stand strong when life needs them.",
                    "A brother may tease you all year, but he still becomes your shield when it matters.",
                    "The most beautiful Rakhi gift is knowing your brother is always on your side.",
                    "A sibling bond grows through fights, jokes, secrets, and quiet loyalty.",
                    "Rakhi celebrates the kind of love that argues, forgives, and stays.",
                    "A brother is childhood proof that love can be annoying and priceless at once.",
                    "The thread changes every year, but the promise stays.",
                ],
            },
            {
                "key": "quotes",
                "h2": "Rakhi Quotes for Brother",
                "lines": [
                    "You are my brother, my backup plan, and my favourite family chaos.",
                    "Rakhi feels complete because I get to celebrate you.",
                    "A brother like you makes every festival feel more like home.",
                    "Thank you for protecting me, irritating me, and loving me in your own way.",
                    "Our bond is built on shared snacks, secret jokes, and lifelong loyalty.",
                    "Happy Rakhi to the one person who understands my childhood without explanation.",
                    "You have always been the calm after my panic and the joke after my drama.",
                    "No matter how grown up we get, Rakhi brings us back to who we were.",
                    "Brother, you are proof that family can also be friendship.",
                    "May this Rakhi bring you everything you quietly work so hard for.",
                ],
            },
            {
                "key": "message",
                "h2": "Rakhi Msg for Brother",
                "lines": [
                    "Happy Rakhi, bhai. I hope this year gives you success, peace, and many reasons to smile.",
                    "Sending love, prayers, and a big thank you for always standing by me.",
                    "This Rakhi, I just want you to know how much your support means to me.",
                    "You may not say much, but your care has always been loud enough.",
                    "Happy Raksha Bandhan. May you stay protected, blessed, and loved every day.",
                    "Thank you for being my brother, my guide, and sometimes my emergency helpline.",
                    "I am lucky to have a brother who shows love through actions, not just words.",
                    "May your life be filled with the same warmth you bring into mine.",
                    "Happy Rakhi 2026. I am sending this message with a heart full of gratitude.",
                    "Distance may keep us apart today, but our Rakhi bond stays close.",
                ],
            },
            {
                "key": "note",
                "h2": "Rakhi Note for Brother",
                "lines": [
                    "Dear brother, this rakhi carries my prayers for your happiness and safety.",
                    "Bhai, thank you for being the person I can trust without thinking twice.",
                    "This little thread is for every time you protected me, guided me, and made me laugh.",
                    "Happy Rakhi. I hope this year brings you calm, confidence, and beautiful progress.",
                    "You are more than my brother. You are one of my strongest blessings.",
                    "I may not say it often, but I am grateful for everything you do.",
                    "Keep this rakhi as a reminder that someone is always praying for you.",
                    "May you always be surrounded by good people, good health, and good fortune.",
                    "Thank you for growing up with me and still choosing to stand by me.",
                    "With this rakhi, I send love, respect, and a promise to always be there too.",
                ],
            },
            {
                "key": "elder",
                "h2": "Emotional Rakhi Wishes for Elder Brother",
                "lines": [
                    "Happy Rakhi to my elder brother, my guide before I knew what guidance meant.",
                    "You protected me in ways I only understood after growing up.",
                    "Thank you for being strong when I needed someone to lean on.",
                    "May your life be as generous and steady as the love you have always shown me.",
                    "I am proud to call you my brother and grateful to call you my support.",
                    "Happy Raksha Bandhan. May every prayer tied in this rakhi reach you as a blessing.",
                    "Your care has shaped my confidence more than you know.",
                    "I may have argued with you, but I have always looked up to you.",
                    "You made childhood safer and adulthood easier to face.",
                    "Happy Rakhi, bhai. You deserve every good thing coming your way.",
                ],
            },
            {
                "key": "younger",
                "h2": "Rakhi Wishes for Younger Brother",
                "lines": [
                    "Happy Rakhi to my younger brother, my forever partner in mischief.",
                    "Watching you grow has been one of my happiest privileges.",
                    "May you stay kind, brave, curious, and full of laughter.",
                    "You may be younger, but you have a heart that protects everyone around you.",
                    "Happy Raksha Bandhan. Keep chasing your dreams and annoying me forever.",
                    "I am proud of the person you are becoming.",
                    "This rakhi carries my love, my blessings, and a tiny warning to behave.",
                    "May your year be full of confidence, friendship, and success.",
                    "You will always be my little brother, no matter how tall you get.",
                    "Happy Rakhi, champ. Keep shining in your own style.",
                ],
            },
            {
                "key": "funny",
                "h2": "Funny Rakhi Wishes for Brother",
                "lines": [
                    "Happy Rakhi. Your gift budget is now officially under review.",
                    "Bhai, thanks for protecting me from everyone except your own jokes.",
                    "This rakhi comes with love, blessings, and a reminder that I know all your secrets.",
                    "Happy Raksha Bandhan to the person who stole my snacks and still stole my heart.",
                    "You are annoying, dramatic, and somehow still my favourite brother.",
                    "May your wallet be ready and your excuses be weak.",
                    "Happy Rakhi. I forgive you for childhood crimes, but only after the gift arrives.",
                    "Brother, you are proof that patience can be built at home.",
                    "Thanks for being my free bodyguard and unpaid comedian.",
                    "Happy Rakhi. Please act emotional before asking what gift I want.",
                ],
            },
            {
                "key": "caption",
                "h2": "Rakhi Captions for Brother",
                "lines": [
                    "Rakhi with my forever protector.",
                    "Brother, bond, blessings, and a little chaos.",
                    "Same fights, same love, stronger bond.",
                    "Rakhi 2026 with my favourite troublemaker.",
                    "A thread full of memories.",
                    "Sibling love, wrapped in tradition.",
                    "Bhai and I, still a team.",
                    "Rakhi glow and brother energy.",
                    "Protected by love, powered by jokes.",
                    "This bond deserves a post.",
                ],
            },
            {
                "key": "short",
                "h2": "Short Rakhi Wishes to Brother",
                "lines": [
                    "Happy Rakhi, bhai.",
                    "Blessed to have you.",
                    "My brother, my strength.",
                    "Rakhi love from me to you.",
                    "Stay happy, stay blessed.",
                    "Forever grateful for you.",
                    "My protector, my friend.",
                    "Happy Raksha Bandhan 2026.",
                    "A thread full of love.",
                    "Brotherhood, blessings, and joy.",
                ],
            },
            {
                "key": "distance",
                "h2": "Rakhi Wishes for Brother Far Away",
                "lines": [
                    "Distance may delay the rakhi, but it cannot weaken the bond.",
                    "Happy Rakhi from miles away. I am sending love, prayers, and a tight hug.",
                    "This year we may not sit together, but my wishes are right beside you.",
                    "May this Raksha Bandhan bring you comfort, success, and a feeling of home.",
                    "Bhai, wherever you are, remember that your sister is always praying for you.",
                    "Happy Rakhi. I miss the laughter, the sweets, and our small festival fights.",
                    "Sending a rakhi through love until I can tie one in person.",
                    "May our bond stay close even when cities keep us apart.",
                    "Happy Raksha Bandhan 2026. You are missed more than you know.",
                    "The thread may travel late, but the blessing reaches on time.",
                ],
            },
            {
                "key": "gift",
                "h2": "Rakhi Gift Message for Brother",
                "lines": [
                    "This gift is a small reminder of a bond I value every day.",
                    "Wear this as a little blessing from your sister.",
                    "A simple keepsake for the brother who has always kept me safe.",
                    "May this gift carry love, luck, and a lot of Rakhi warmth.",
                    "For the brother who deserves something thoughtful, strong, and lasting.",
                    "This is not just a gift. It is a thank you in a form you can keep.",
                    "I chose this because it felt like you: steady, stylish, and protective.",
                    "May it remind you of home whenever you wear it.",
                    "A Rakhi gift for my brother, with prayers for every good thing ahead.",
                    "Small gift, big love, forever bond.",
                ],
            },
        ],
        "faqs": [
            ["What are the best happy Rakhi wishes to brother?", "The best happy Rakhi wishes to brother are warm, personal, and easy to send. Mention protection, childhood memories, gratitude, blessings, and your bond. For a close brother, add a funny line. For an elder brother, keep the wish respectful and emotional."],
            ["What is a good rakhi quotation for brother?", "A good rakhi quotation for brother is: A rakhi is small, but the bond it carries can hold a lifetime. You can also write: The thread changes every year, but the promise stays."],
            ["What should I write in a rakhi note for brother?", "In a rakhi note for brother, write one sincere thank you, one blessing, and one personal memory. Keep it short enough for a card. For example: This rakhi carries my prayers for your happiness, safety, and success."],
            ["What is a short Rakhi msg for brother?", "A short Rakhi msg for brother can be: Happy Rakhi, bhai. May your life stay full of strength, peace, and good news. Another simple line is: My brother, my strength, my forever friend."],
            ["Can I use Rakhi quotes as Instagram captions?", "Yes. Rakhi quotes work well as Instagram captions when they are short and visual. Use lines like A thread full of memories, or Same fights, same love, stronger bond, for brother photos and Raksha Bandhan reels."],
            ["What gift message should I send with a Rakhi gift for brother?", "Write a gift message that feels thoughtful rather than formal. You can say: Wear this as a little blessing from your sister, or I chose this because it felt like you: steady, stylish, and protective."],
            ["When is Raksha Bandhan 2026?", "Raksha Bandhan 2026 falls on Friday, August 28, 2026. Use this date for scheduled posts, cards, captions, and family reminders."],
        ],
    }

    config = {
        "rank": "Week3-4 Rank 3",
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-rakhiwishesbrother",
        "occasion_year": "Raksha Bandhan 2026",
        "carousel_alt_prefix": "happy Rakhi wishes to brother 2026 gift idea",
        "gift_h2": "Rakhi Gift Ideas for Brother",
        "gift_blurb": "If your Rakhi wish is going with a gift, keep the piece wearable and the note personal. These BlueStone picks suit brothers who prefer clean, meaningful, everyday festive style.",
        "conclusion_html": "Happy Rakhi wishes to brother do not need to sound perfect. Choose a line that feels like your real bond, add one personal memory if you can, and let the rakhi carry the blessing.",
        "schema_keywords": [
            "happy rakhi wishes to brother",
            "rakhi quotation",
            "rakhi quotes",
            "rakhi msg for brother",
            "rakhi note for brother",
        ],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(product_rows, "The Protector Evil Eye Rakhi", "ProductImages/seo images/Adjustable Bracelets/The Protector Evil Eye Rakhi.png"),
            product(product_rows, "The Bandhan Bracelet For Him", "ProductImages/seo images/Bracelet/The Bandhan Bracelet For Him.png"),
            product(product_rows, "The Serenity Evil Eye Pendant For Him", "ProductImages/seo images/Pendants/The Serenity Evil Eye Pendant For Him.png"),
            product(product_rows, "The Talisman Evil Eye Pendant For Him", "ProductImages/seo images/Pendants/The Talisman Evil Eye Pendant For Him.png"),
            product(product_rows, "The Jasper Band For Him", "ProductImages/seo images/Rings/The Jasper Band For Him.png"),
            product(product_rows, "The Chevalier Gold Chain", "ProductImages/seo images/Chains/The Chevalier Gold Chain.png"),
        ],
        "flatlay_insert_h2": "Rakhi Note for Brother",
        "lifestyle_insert_h2": "Rakhi Gift Message for Brother",
        "more_reads_html": "Read more sibling gifting ideas in <a href=\"https://blog.bluestone.com/rakhi-for-bhaiya-bhabhi-2026/\">rakhi for bhaiya bhabhi 2026</a> and <a href=\"https://blog.bluestone.com/raksha-bandhan-gifts-for-brother-2026/\">Raksha Bandhan gifts for brother 2026</a>.",
        "how_to_html": "Raksha Bandhan 2026 falls on Friday, August 28, 2026. For official festival context, see <a href=\"https://www.incredibleindia.gov.in/en/festivals-and-events/rakshabandhan\">Incredible India on Raksha Bandhan</a>. Keep your message relationship specific: emotional for elder brothers, playful for close brothers, and short for captions.",
        "faq_h2": "Frequently Asked Questions about Rakhi Wishes to Brother",
        "min_lines": 100,
    }

    hero = consolidated(detail_rows, "The Protector Evil Eye Rakhi")
    flatlay = consolidated(detail_rows, "The Bandhan Bracelet For Him")
    lifestyle = consolidated(detail_rows, "The Serenity Evil Eye Pendant For Him")

    prompts = {
        "rank": "Week3-4 Rank 3",
        "slug": "happy-rakhi-wishes-to-brother-2026",
        "primary_kw": "happy rakhi wishes to brother",
        "output_prefix": PREFIX,
        "caption_occasion": "Happy Rakhi wishes to brother",
        "caption_year": "2026",
        "flatlay_setting": "gift-wrapping-station",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/happy-rakhi-wishes-to-brother-hero-2026.webp",
            "flatlay": "output/magnific_generated/happy-rakhi-wishes-to-brother-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/happy-rakhi-wishes-to-brother-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "happy Rakhi wishes to brother 2026 hero The Protector Evil Eye Rakhi",
            "flatlay": "happy Rakhi wishes to brother 2026 flatlay The Bandhan Bracelet For Him",
            "lifestyle": "happy Rakhi wishes to brother 2026 lifestyle The Serenity Evil Eye Pendant For Him",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                **hero,
                "alt": "happy Rakhi wishes to brother 2026 hero with The Protector Evil Eye Rakhi",
                "caption": "Happy Rakhi wishes to brother 2026: The Protector Evil Eye Rakhi",
                "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]},
                "local_reference_images": [
                    "ProductImages/raw/Adjustable Bracelets/The Protector Evil Eye Rakhi/1_body_portrait.png",
                    "ProductImages/raw/Adjustable Bracelets/The Protector Evil Eye Rakhi/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} "
                    "Happy Rakhi wishes to brother 2026 hero, fair-skinned Indian adult man seated in a warm modern Indian home near a rakhi gift table. Frame shows his full face, natural smile, upper body, and one forearm resting naturally on the table with The Protector Evil Eye Rakhi visible on that wrist. A blank cream Rakhi card, diya, roli chawal thali, and sweets sit nearby. Exactly one person only. 85mm DSLR look, natural skin texture, warm daylight, 16:9.\n\n"
                    "The man physically wears The Protector Evil Eye Rakhi from @img1 body_image and @img2 design only on one wrist. GENDER LOCK: Male product on adult man only. "
                    f"Product dimensions from PDP: {hero['size_prompt_note']}. These are product dimensions, not face-size instructions. "
                    "Keep rakhi size on the wrist like @img1 body_image worn scale: subtle real PDP size, not enlarged. Use @img2 only for jewellery design.\n\n"
                    "Replicate the evil eye rakhi exactly, 100 percent identical to refs, zero distortion, HD thread and metal detail. This rakhi is the single and only jewellery object in the entire image. No rings, no watch, no bracelet, no bangle, no chain, no pendant, no earrings, no other jewellery. No readable text anywhere. Any card or gift tag must be completely blank.\n\n"
                    "Avoid: extra bracelet, watch, ring, cropped face, cropped head, readable text, letters, numbers, logo, woman wearer, child, second person, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow."
                ),
            },
            "flatlay": {
                **flatlay,
                "alt": "happy Rakhi wishes to brother 2026 flatlay with The Bandhan Bracelet For Him",
                "caption": "Happy Rakhi wishes to brother 2026 gift note: The Bandhan Bracelet For Him",
                "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]},
                "local_reference_images": [
                    "ProductImages/raw/Bracelets/The Bandhan Bracelet For Him/0_primary.png",
                    "ProductImages/raw/Bracelets/The Bandhan Bracelet For Him/2_side_1.png",
                    "ProductImages/raw/Bracelets/The Bandhan Bracelet For Him/3_back.png",
                ],
                "ref_roles": ["primary", "side", "back"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\n"
                    "Happy Rakhi wishes to brother 2026 top-down flatlay. Flatlay setting ID: gift-wrapping-station. Surface and props: warm kraft paper, folded cream cloth, small diya, roli chawal, simple sweets, rakhi thread spool, and a completely blank cream note card. "
                    "The identical Bandhan Bracelet For Him from @img1, @img2 and @img3 rests naturally on the surface at true PDP scale. "
                    f"Product dimensions from PDP: {flatlay['size_prompt_note']}. These are product dimensions, not face-size instructions. Do not enlarge for visibility. "
                    "Full bracelet visible, yellow gold bracelet with refined masculine link detail, 100 percent identical design, zero distortion, HD metal detail.\n\n"
                    "Props stay secondary. No people, no hands, no logos, no readable text, no letters, no numbers, no other jewellery.\n\n"
                    "Avoid: hands, people, floating overlays, cutouts, incorrect bracelet design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI."
                ),
            },
            "lifestyle": {
                **lifestyle,
                "alt": "happy Rakhi wishes to brother 2026 lifestyle with The Serenity Evil Eye Pendant For Him",
                "caption": "Happy Rakhi wishes to brother 2026 look: The Serenity Evil Eye Pendant For Him",
                "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]},
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Serenity Evil Eye Pendant For Him/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Serenity Evil Eye Pendant For Him/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} "
                    "Happy Rakhi wishes to brother 2026 lifestyle, fair-skinned Indian adult man in a simple ivory kurta standing in a warm modern Indian home near softly blurred Rakhi decor. Upper torso portrait only: full head, full face, both eyes, natural smile, neck, pendant, shoulders, and upper chest visible with safe margins. Hands and wrists are completely out of frame. Exactly one person only. 85mm DSLR look, natural skin texture, soft daylight, 16:9.\n\n"
                    "The man physically wears The Serenity Evil Eye Pendant For Him from @img1 body_image and @img2 design only on his neck. GENDER LOCK: Male product on adult man only. "
                    f"Product dimensions from PDP: {lifestyle['size_prompt_note']}. These are product dimensions, not face-size instructions. "
                    "Keep pendant size on the neck like @img1 body_image worn scale: subtle real PDP size, not enlarged. Use @img2 only for jewellery design.\n\n"
                    "Replicate the yellow gold evil eye pendant exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery object in the entire image. No earrings, no nose pin, no rings, no bracelets, no watch, no extra necklace. Hands and wrists must not appear. No readable text anywhere.\n\n"
                    "Avoid: hands, wrists, watch, bracelet, ring, extra chain, cropped face, cropped head, readable text, letters, numbers, logo, woman wearer, child, second person, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow."
                ),
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Week 3-4 Rank 3

Article: Happy Rakhi Wishes to Brother 2026
Status: Draft assets prepared
Date: 2026-07-28

## A. Intent and Brief
- [x] Primary keyword: happy rakhi wishes to brother
- [x] Sheet Optimize treated as New
- [x] Fresh slug: happy-rakhi-wishes-to-brother-2026
- [x] 2026 year lock used
- [x] Supporting keywords mapped to H2 and FAQ

## B. SEO Structure
- [x] Title/H1 intent prepared
- [x] Yoast title under 60 chars
- [x] Meta description 150 to 160 chars
- [x] Primary keyword in intro and hero alt

## C. Content and Readability
- [x] Direct answer and TL;DR
- [x] 100+ wish, quote, note, message, and caption lines
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
    write_json("output/publish_configs/week34_rank3.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")
    print(f"wrote {PREFIX} assets")


if __name__ == "__main__":
    main()
