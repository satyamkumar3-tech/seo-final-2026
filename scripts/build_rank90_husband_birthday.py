#!/usr/bin/env python3
"""Build Rank 90 husband birthday assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank90_HusbandBirthday"


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


def main() -> None:
    rows = load_products()
    sections = {
        "meta": {
            "title": "Husband Birthday Wishes 2026: Romantic Messages",
            "slug": "husband-birthday-wishes-2026",
            "meta_desc": "Husband birthday wishes 2026 with romantic, short, funny, emotional, blessing, long, WhatsApp, and loving messages for cards, captions, and gift ideas.",
            "focus_kw": "husband birthday",
            "yoast_title": "Husband Birthday Wishes 2026",
        },
        "intro": [
            "Husband birthday wishes should feel personal, warm, and easy to send. The right line can sound romantic without becoming dramatic, funny without becoming careless, and heartfelt without becoming too long.",
            "TL;DR: choose a short wish for WhatsApp, a romantic paragraph for a private note, a funny line only if it suits your bond, and one specific detail to make the birthday message feel like yours.",
        ],
        "sections": [
            {
                "key": "best",
                "h2": "Best Husband Birthday Wishes 2026",
                "lines": [
                    "Happy birthday, my husband. You make ordinary life feel steady, safe, and full of love.",
                    "Wishing you a birthday filled with peace, laughter, good food, and all the rest you deserve.",
                    "Happy birthday to the man who is my partner, my comfort, and my favourite everyday person.",
                    "May 2026 bring you health, confidence, calm mornings, and wins that make you proud.",
                    "Happy birthday, love. Thank you for showing up for us in quiet and beautiful ways.",
                    "You are the reason home feels warmer after a long day.",
                    "May your birthday remind you that you are deeply loved and truly appreciated.",
                    "Happy birthday to my husband, my best friend, and the person I still choose first.",
                    "I hope this year gives you more joy than pressure and more peace than worry.",
                    "Happy birthday. Loving you is still one of the easiest truths of my life.",
                ],
            },
            {
                "key": "romantic",
                "h2": "Romantic Birthday Wishes for Husband",
                "lines": [
                    "Happy birthday, my love. Your presence is the calm place my heart keeps returning to.",
                    "You are not only my husband, you are the love story I get to live every day.",
                    "May your birthday feel as warm as the love you have built around us.",
                    "I love the way you care, protect, listen, laugh, and keep choosing us.",
                    "Happy birthday. If life gives me another thousand days, I still want them beside you.",
                    "Your smile is my favourite beginning and your hug is my favourite ending.",
                    "May this birthday bring you the softness you give me when I need it most.",
                    "You make partnership feel real, patient, and beautifully human.",
                    "Happy birthday, jaan. You are my home in every season.",
                    "I love you more deeply than one message can carry.",
                ],
            },
            {
                "key": "short",
                "h2": "Short Husband Birthday Wishes",
                "lines": [
                    "Happy birthday, my love. Stay blessed.",
                    "You are my forever favourite.",
                    "Birthday love to my husband.",
                    "I choose you every day.",
                    "Happy birthday, my safe place.",
                    "You make life better.",
                    "Love you today and always.",
                    "Happy birthday, handsome.",
                    "My heart is happiest with you.",
                    "Blessings, love, and cake for you.",
                ],
            },
            {
                "key": "whatsapp",
                "h2": "Husband Birthday WhatsApp Messages",
                "lines": [
                    "Happy birthday, love. I hope your day starts with peace and ends with a smile.",
                    "Sending you birthday hugs through this message until I can give you the real one.",
                    "Happy birthday, husband. Thank you for being patient, loving, and wonderfully you.",
                    "May your phone be full of wishes and your heart be full of calm today.",
                    "I am grateful for your love in all the small moments no one else sees.",
                    "Happy birthday. Come home early; your biggest fan is waiting.",
                    "You deserve a day without stress, traffic, deadlines, or forgotten tea.",
                    "Happy birthday, jaan. May your year be kind to your dreams.",
                    "My first wish today is simple: may you feel loved the way you make me feel loved.",
                    "Happy birthday to the man whose message still makes me smile.",
                ],
            },
            {
                "key": "funny",
                "h2": "Funny Birthday Wishes for Husband",
                "lines": [
                    "Happy birthday, husband. I promise to let you choose the movie, unless it is too boring.",
                    "You are ageing like fine wine, and I am ageing like the person who remembers your passwords.",
                    "Happy birthday to the man who still thinks he knows where everything is kept.",
                    "May your cake be sweet and your birthday chores be magically postponed.",
                    "Happy birthday. Today, I will pretend your jokes are new.",
                    "You deserve rest, gifts, and at least one day without me asking why you kept that box.",
                    "Happy birthday to my favourite human and my least reliable finder of household items.",
                    "May your day be as calm as you look when you say everything is under control.",
                    "Happy birthday, love. I married you for romance and stayed for your snack-sharing skills.",
                    "Let us celebrate you today and discuss your cupboard organisation tomorrow.",
                ],
            },
            {
                "key": "emotional",
                "h2": "Emotional Birthday Wishes for Husband",
                "lines": [
                    "Happy birthday. I notice the pressure you carry and the love you still give.",
                    "You have been my strength in seasons when I did not know how to be strong.",
                    "Thank you for building a life with me, not just living beside me.",
                    "May this year be gentler on your heart and kinder to your efforts.",
                    "I am proud of the man you are and the man you keep becoming.",
                    "Happy birthday, husband. You are loved in more ways than I say out loud.",
                    "Your sacrifices, patience, and quiet care do not go unnoticed.",
                    "May you receive the same steadiness you have given to everyone around you.",
                    "You are my partner in ordinary days and difficult ones too.",
                    "Happy birthday. I hope today reminds you that you matter deeply.",
                ],
            },
            {
                "key": "blessings",
                "h2": "Birthday Blessings for Husband",
                "lines": [
                    "May God bless you with health, wisdom, protection, and peaceful success.",
                    "May your work bring progress without stealing your joy.",
                    "May your heart stay strong, your mind stay calm, and your path stay clear.",
                    "On your birthday, I pray for a year of good health and honest happiness.",
                    "May every effort you make find the right result at the right time.",
                    "May your life be protected from unnecessary stress and surrounded by love.",
                    "Happy birthday. May courage and patience walk with you through 2026.",
                    "May your dreams grow without making your heart heavy.",
                    "I pray that your year gives you laughter, respect, rest, and meaningful wins.",
                    "May your birthday begin a chapter full of grace.",
                ],
            },
            {
                "key": "long",
                "h2": "Long Birthday Messages for Husband",
                "lines": [
                    "Happy birthday, my love. One message can never hold everything you mean to me, but I hope it reminds you that your care, humour, patience, and strength are seen every day.",
                    "You have loved me in small practical ways and big emotional ways, and both have shaped the life we share.",
                    "I am grateful for the ordinary evenings, the shared decisions, the silly jokes, and the quiet support that makes marriage feel real.",
                    "May this birthday bring you rest from pressure and courage for everything you still want to build.",
                    "You deserve a year where your efforts are respected and your heart feels lighter.",
                    "Happy birthday to the man who has stood beside me through confusion, routine, laughter, and change.",
                    "I may not always say it perfectly, but I love the life we are making together.",
                    "May your dreams feel possible and your home always feel like a safe place to return.",
                    "Thank you for being my husband, my friend, and my constant person.",
                    "Happy birthday. I love you more with every honest year we share.",
                ],
            },
            {
                "key": "captions",
                "h2": "Birthday Captions for Husband",
                "lines": [
                    "Birthday love for my forever person.",
                    "My husband, my heart, my happiest yes.",
                    "Celebrating the man who makes life warmer.",
                    "Another year of loving him louder.",
                    "The birthday boy has my whole heart.",
                    "Love looks like him.",
                    "My favourite human, birthday edition.",
                    "Grateful for this man every day.",
                    "Husband, best friend, birthday king.",
                    "Forever proud to call him mine.",
                ],
            },
            {
                "key": "from_wife",
                "h2": "Birthday Wishes for Husband from Wife",
                "lines": [
                    "From your wife, happy birthday to the man who makes my life feel loved and steady.",
                    "I am grateful for your partnership, your patience, and your quiet ways of caring.",
                    "Happy birthday, husband. I love being the person who gets to celebrate you this closely.",
                    "May your birthday feel like a thank you for everything you do for us.",
                    "You are my favourite plan, my strongest habit, and my softest place.",
                    "Happy birthday from the woman who still smiles when you walk into the room.",
                    "I hope today gives you rest, attention, affection, and your favourite food.",
                    "You make marriage feel like friendship with deeper roots.",
                    "Happy birthday, my love. I am proud of us and proud of you.",
                    "Your wife loves you more than this card, caption, or message can say.",
                ],
            },
            {
                "key": "gift",
                "h2": "A Birthday Gift Idea for Your Husband",
                "lines": [
                    "A birthday message can carry the emotion, while a small keepsake can hold the memory.",
                    "Choose jewellery that matches how he actually dresses, not only what looks impressive online.",
                    "A band ring feels timeless when his style is simple and classic.",
                    "A bracelet works well when he likes visible but practical accessories.",
                    "A pendant can feel personal when he already wears chains or meaningful symbols.",
                    "Avoid price talk in the birthday note.",
                    "Write one private line with the gift so it feels emotional, not transactional.",
                    "Pick something he can wear after the celebration too.",
                    "Let the wish lead and the gift quietly follow.",
                    "The best gift says, I notice your style and I value who you are.",
                ],
            },
        ],
        "section_leads": {
            "Best Husband Birthday Wishes 2026": "Use these all-rounder wishes when you want a warm birthday message that works for cards, chats, and captions.",
            "Romantic Birthday Wishes for Husband": "These romantic wishes stay loving and grounded, so they feel real instead of copied.",
            "Short Husband Birthday Wishes": "Short wishes work for WhatsApp, first morning messages, and quick captions.",
            "Husband Birthday WhatsApp Messages": "These lines are ready to send when you want a sweet message that still sounds natural.",
            "Funny Birthday Wishes for Husband": "Funny wishes are safest when the joke is affectionate and never about sensitive topics.",
            "Emotional Birthday Wishes for Husband": "Use these when you want the message to recognise his effort and your shared life.",
            "Birthday Blessings for Husband": "These blessings fit family-friendly cards, private notes, and respectful WhatsApp messages.",
            "Long Birthday Messages for Husband": "Send a longer message when the relationship deserves more than one line.",
            "Birthday Captions for Husband": "These captions suit photos, reels, stories, and birthday collage posts.",
            "Birthday Wishes for Husband from Wife": "Use this section when the message should clearly sound like it comes from his wife.",
            "A Birthday Gift Idea for Your Husband": "A gift is optional; the birthday wish should still carry the heart of the day.",
        },
        "faqs": [
            ["What is the best husband birthday wish?", "A strong husband birthday wish is warm, personal, and specific. Try: Happy birthday, my husband. You make ordinary life feel steady, safe, and full of love."],
            ["How do I write a romantic birthday message for my husband?", "Start with Happy birthday, add one quality you love about him, and mention one shared detail. Keep the tone sincere rather than overly decorated."],
            ["What is a short husband birthday wish for WhatsApp?", "A short WhatsApp wish can be: Happy birthday, my love. You are my safe place, my favourite person, and my forever choice."],
            ["Can I send funny birthday wishes to my husband?", "Yes, if humour is part of your relationship. Keep the joke kind and avoid teasing about age, appearance, money, work pressure, or sensitive habits."],
            ["What should a wife write for husband birthday?", "A wife can write about gratitude, partnership, love, and one everyday habit she appreciates. The most touching lines usually sound specific to the marriage."],
            ["Is jewellery a good birthday gift for a husband?", "Jewellery can be thoughtful when it fits his style. A band ring, bracelet, chain, or pendant can work well if the note focuses on love and not price."],
        ],
    }

    config = {
        "rank": 90,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-husbandbirthday",
        "occasion_year": "Husband Birthday Wishes 2026",
        "carousel_alt_prefix": "husband birthday wishes 2026 gift idea",
        "gift_h2": "Birthday Jewellery Gift Ideas for Husband",
        "gift_blurb": "If the birthday wish carries the feeling, a wearable keepsake can carry the memory. These six approved BlueStone designs suit husband birthday gifting without mentioning prices.",
        "conclusion_html": "Husband birthday wishes work best when they sound like your real marriage, not a formal template. Pick one line, add his name or one private detail, and let the message make his day feel loved.",
        "schema_keywords": [
            "husband birthday",
            "husband birthday wishes",
            "romantic birthday wishes for husband",
            "short birthday wishes for husband",
            "funny birthday wishes for husband",
            "birthday wishes for husband from wife",
        ],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(rows, "The Talisman Evil Eye Pendant For Him", "Pendants"),
            product(rows, "The Jasper Band For Him", "Rings"),
            product(rows, "The Network Link Bracelet", "Bracelet"),
            product(rows, "The Chevalier Gold Chain", "Chains"),
            product(rows, "The Volara Bracelet For Him", "Bracelet"),
            product(rows, "The Tetyana Gold Chain", "Chains"),
        ],
        "flatlay_insert_h2": "Birthday Blessings for Husband",
        "lifestyle_insert_h2": "A Birthday Gift Idea for Your Husband",
        "more_reads_html": "For more birthday inspiration, see <a href=\"https://blog.bluestone.com/whatsapp-birthday-wishes-for-wife-2026/\">birthday wishes for wife 2026</a>, <a href=\"https://blog.bluestone.com/advance-happy-birthday-wishes-2026/\">advance birthday wishes 2026</a>, <a href=\"https://blog.bluestone.com/birthday-wishes-for-nephew-2026/\">birthday wishes for nephew 2026</a>, and <a href=\"https://blog.bluestone.com/birthday-wishes-for-cousin-brother-sister-2026/\">birthday wishes for cousin 2026</a>.",
        "how_to_html": "For your husband, write like you speak at home. Use one warm birthday line, one personal detail, and one blessing for his year ahead. Keep funny lines private if they could embarrass him in a family group.",
        "faq_h2": "Frequently Asked Questions about Husband Birthday Wishes",
        "min_lines": 100,
        "section_leads": sections["section_leads"],
    }

    prompts = {
        "rank": 90,
        "slug": "husband-birthday-wishes-2026",
        "output_prefix": PREFIX,
        "occasion": "Husband Birthday Wishes 2026",
        "primary_kw": "husband birthday",
        "caption_occasion": "Husband birthday wishes",
        "caption_year": "2026",
        "flatlay_setting": "linen-bedside",
        "workflow": "Higgsfield MCP nano_banana_pro. Campaign hybrid with mandatory body_image scale line for people shots. Do not generate until balance succeeds. Max 2 concurrent generations.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/husband-birthday-wishes-hero-2026.webp",
            "flatlay": "output/magnific_generated/husband-birthday-wishes-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/husband-birthday-wishes-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "husband birthday wishes 2026 hero The Talisman Evil Eye Pendant For Him",
            "flatlay": "husband birthday wishes 2026 flatlay The Jasper Band For Him",
            "lifestyle": "husband birthday wishes 2026 lifestyle The Network Link Bracelet",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                "code": "BIKR0987P33",
                "name": "The Talisman Evil Eye Pendant For Him",
                "gender": "Male",
                "height_mm": 38.3,
                "width_mm": 19.73,
                "size_prompt_note": "pendant product height 38.3 mm and width 19.73 mm; product dimensions, not face size; copy worn neck scale from body_image",
                "alt": "husband birthday wishes 2026 hero with The Talisman Evil Eye Pendant For Him",
                "caption": "Husband birthday wishes 2026 vibe: The Talisman Evil Eye Pendant For Him",
                "product": {"code": "BIKR0987P33", "name": "The Talisman Evil Eye Pendant For Him", "pdp": "https://www.bluestone.com/pendants/the-talisman-evil-eye-pendant-for-him~115385.html"},
                "cdn": [
                    "https://kinclimg7.bluestone.com/giproduct/BIKR0987P33_YAA18DIG6BLTOSIG7_ABCD00-BP-PICS-00000-1024-80312.png",
                    "https://kinclimg1.bluestone.com/giproduct/BIKR0987P33_YAA18DIG6BLTOSIG7_ABCD00-PICS-00002-1024-80312.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Talisman Evil Eye Pendant For Him/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Talisman Evil Eye Pendant For Him/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": "STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. Husband birthday wishes 2026 hero, solo fair-skinned Indian adult man, a husband, sitting in a bright home dining nook and smiling while reading a blank birthday card from his wife beside a small wrapped gift and blank phone screen. Full head, full face, both eyes, complete smile, neck, pendant, hands, blank card, gift, and upper body visible with safe margins. Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, soft daylight, realistic shadows, no HDR glare, 16:9.\n\nThe man physically wears The Talisman Evil Eye Pendant For Him from @img1 body_image and @img2 design on a fine chain at upper chest. GENDER LOCK: Male For Him product on adult man only. Product dimensions from PDP: pendant product height_mm=38.3 and width_mm=19.73. These are real product dimensions, NOT face-size instructions. Keep pendant size on the neck like @img1 body_image worn neck scale: subtle pendant size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the yellow gold evil eye pendant with blue stone detail exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery in the image. Bare wrists, bare fingers, no watch, no bracelet, no ring, no earrings. Jewellery touches fabric or skin with soft contact shadow, never a floating cutout. The card and phone screen must be blank with no letters, no handwriting, no symbols, no numbers.\n\nAvoid: cropped face, cropped eyes, cropped forehead, cropped head, readable text, handwriting, printed letters, numbers, symbols on card or phone, woman wearer, child, minor, second person, wife in frame, extra hands, extra necklaces, rings, watches, earrings, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI.",
            },
            "flatlay": {
                "code": "BISL0851R28",
                "name": "The Jasper Band For Him",
                "gender": "Male",
                "height_mm": 24.11,
                "width_mm": 11.92,
                "size_prompt_note": "ring product face height 24.11 mm and width 11.92 mm; product dimensions, not face size",
                "alt": "husband birthday wishes 2026 flatlay with The Jasper Band For Him",
                "caption": "Husband birthday wishes 2026 keepsake: The Jasper Band For Him",
                "product": {"code": "BISL0851R28", "name": "The Jasper Band For Him", "pdp": "https://www.bluestone.com/rings/the-jasper-band-for-him~93964.html"},
                "cdn": [
                    "https://kinclimg0.bluestone.com/giproduct/BISL0851R28_YAA22XXXXXXXXXXXX_ABCD00-PICS-00001-1024-70393.png",
                    "https://kinclimg7.bluestone.com/giproduct/BISL0851R28_YAA22XXXXXXXXXXXX_ABCD00-PICS-00000-1024-70393.png",
                    "https://kinclimg3.bluestone.com/giproduct/BISL0851R28_YAA22XXXXXXXXXXXX_ABCD00-PICS-00002-1024-70393.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Rings/The Jasper Band For Him/0_primary.png",
                    "ProductImages/raw/Rings/The Jasper Band For Him/2_front.png",
                    "ProductImages/raw/Rings/The Jasper Band For Him/3_back.png",
                ],
                "ref_roles": ["primary", "front", "back"],
                "prompt": "Photoreal high-end jewellery still life, top-down editorial product flatlay, controlled soft key light, realistic gentle shadows, shallow depth of field, HD metal and stone detail, 16:9 landscape.\n\nHusband birthday wishes 2026 top-down flatlay. Flatlay setting ID: linen-bedside. Surface and props: neutral linen bedding edge, blank cream birthday card, matte gift box, simple pen, ceramic cup, and a blank phone screen. No readable text, no letters, no numbers, no symbols on any prop.\n\nThe identical Jasper Band For Him from @img1, @img2 and @img3 rests naturally on the linen at true PDP scale. Product dimensions from PDP: ring product face height 24.11 mm and width 11.92 mm. These are product dimensions, NOT face-size instructions. Do not enlarge for visibility. Full ring visible, plain yellow gold band with masculine sculpted texture, 100 percent identical design, zero distortion.\n\nProps stay secondary and quiet. No people, no hands, no readable text, no brand marks. Jewellery is the clear subject but still true to real size.\n\nAvoid: hands, people, floating overlays, cutouts, incorrect ring design, distorted metal, readable text, logos, price tags, brand marks on props, blown whites, HDR glare, illustration, CGI.",
            },
            "lifestyle": {
                "code": "BISV0910V26",
                "name": "The Network Link Bracelet",
                "gender": "Male",
                "height_mm": 203.2,
                "width_mm": 8.54,
                "size_prompt_note": "bracelet length 203.2 mm and link width about 8.54 mm; product dimensions, not face size; copy worn wrist scale from body_image",
                "alt": "husband birthday wishes 2026 lifestyle with The Network Link Bracelet",
                "caption": "Husband birthday wishes 2026 vibe: The Network Link Bracelet",
                "product": {"code": "BISV0910V26", "name": "The Network Link Bracelet", "pdp": "https://www.bluestone.com/bracelets/the-network-link-bracelet~108784.html"},
                "cdn": [
                    "https://kinclimg9.bluestone.com/giproduct/BISV0910V26_YAA18DIG6XXXXXXXX_ABCD00-BP-PICS-00000-1024-82467.png",
                    "https://kinclimg3.bluestone.com/giproduct/BISV0910V26_YAA18DIG6XXXXXXXX_ABCD00-PICS-00001-1024-82467.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Bracelets/The Network Link Bracelet/1_body_portrait.png",
                    "ProductImages/raw/Bracelets/The Network Link Bracelet/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": "STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. Husband birthday wishes 2026 lifestyle, solo fair-skinned Indian adult man, a husband, sitting alone near a bright window and smiling while reading a blank phone screen with a blank birthday card and small wrapped gift on the table. Exactly one person in the entire image. No background people, no silhouettes, no extra faces, no wife in frame, no child, no extra hands. Full face, both wrists, phone, blank card, gift, and upper body visible with safe margins. 85mm DSLR look, natural skin texture, soft daylight, realistic shadows, no HDR glare, 16:9.\n\nThe man physically wears The Network Link Bracelet from @img1 body_image and @img2 design on one wrist. GENDER LOCK: Male product on adult man only. Product dimensions from PDP: bracelet length_mm=203.2 and link_width_mm=8.54. These are real product dimensions, NOT face-size instructions. Keep bracelet size on the wrist like @img1 body_image worn wrist scale: subtle bracelet size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the polished yellow gold network link bracelet exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This bracelet is the single and only jewellery in the image. Bare neck, bare fingers, no watch, no ring, no necklace, no earrings. Jewellery touches wrist with soft contact shadow, never a floating cutout. The phone screen and card must be blank with no letters, no handwriting, no symbols, no numbers.\n\nAvoid: background people, woman wearer, child, minor, second person, extra hands, silhouettes, staff, readable text, handwriting, printed letters, numbers, symbols on phone or card, extra necklaces, rings, watches, bracelets on other wrist, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, cropped face, dark skin, deep brown skin, heavily tanned skin, illustration, CGI.",
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 90

Article: Husband Birthday Wishes 2026
Status: Draft assets prepared
Date: 2026-07-23

## A. Intent and Brief
- [x] Primary keyword: husband birthday
- [x] Supporting keywords mapped to H2s and FAQs
- [x] Sheet New treated as New
- [x] Fresh slug: husband-birthday-wishes-2026
- [x] 2026 year lock used

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""

    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json("output/publish_configs/rank90.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
