#!/usr/bin/env python3
"""Build Rank 87 advance birthday wishes article assets and Type 3 prompt manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank87_AdvanceBirthday"


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
            "title": "Advance Birthday Wishes 2026: Early Messages for Friends",
            "slug": "advance-happy-birthday-wishes-2026",
            "meta_desc": "Send advance birthday wishes 2026 with warm early messages for best friend, lover, family, WhatsApp, captions, and sweet sorry I am early notes today.",
            "focus_kw": "advance birthday wishes",
            "yoast_title": "Advance Birthday Wishes 2026",
        },
        "intro": [
            "Advance birthday wishes are perfect when you want your message to arrive before the rush, before midnight notifications, and before everyone else says the same thing.",
            "TL;DR: send an early wish when you may be busy later, when the person lives in another time zone, or when you want your message to feel thoughtful instead of last minute.",
        ],
        "sections": [
            {
                "key": "best",
                "h2": "Best Advance Birthday Wishes 2026",
                "lines": [
                    "Sending advance birthday wishes because someone as special as you deserves love before the day even begins.",
                    "Happy birthday in advance. May 2026 bring you health, confidence, peace, and the kind of joy that stays.",
                    "I may be early, but my wishes are full of love. Have a birthday as wonderful as your heart.",
                    "Advance happy birthday. May your special day arrive with smiles, blessings, and beautiful surprises.",
                    "Wishing you in advance so my message reaches before the crowd. You deserve the first warm thought.",
                    "Happy birthday in advance to someone who makes ordinary days feel brighter.",
                    "Before the clock strikes your birthday, I want you to know how deeply you are valued.",
                    "Advance birthday wishes for a year filled with better mornings, kinder people, and dreams moving closer.",
                    "I am sending my wish early because your happiness should never wait.",
                    "Happy birthday in advance. May every month ahead give you one fresh reason to celebrate.",
                ],
            },
            {
                "key": "best_friend",
                "h2": "Advance Birthday Wishes for Best Friend",
                "lines": [
                    "Advance happy birthday, best friend. I am early because you are too important for a late wish.",
                    "Before everyone floods your phone, here is my first reminder that you are loved beyond words.",
                    "Happy birthday in advance to the friend who turns chaos into memories and boring days into stories.",
                    "I hope your birthday brings cake, laughter, peace, and the exact happiness your heart needs.",
                    "Advance birthday wishes, bestie. Thank you for being my safe place and my loudest laughter.",
                    "Sending this early because our friendship deserves a little extra time to celebrate.",
                    "May your birthday week be full of good news, real smiles, and people who show up for you.",
                    "Happy birthday in advance to my favourite human in the group chat.",
                    "I am counting down to your birthday with gratitude for every memory we have made.",
                    "Advance wishes, best friend. May this year be softer, stronger, and brighter for you.",
                ],
            },
            {
                "key": "advance_happy",
                "h2": "Advance Happy Birthday Wishes",
                "lines": [
                    "Advance happy birthday. May your day be filled with love from the people who know you best.",
                    "Wishing you early so the happiness starts before the celebration does.",
                    "Advance happy birthday to someone who deserves a full week of smiles.",
                    "May your birthday arrive with peace in your heart and excitement in your plans.",
                    "Happy birthday in advance. I hope the coming year treats you gently and generously.",
                    "Sending warm early wishes for health, success, and beautiful memories.",
                    "Advance happy birthday. May your special day be easy, bright, and full of care.",
                    "I am early, but the blessing is sincere. Have a wonderful birthday ahead.",
                    "May your birthday be the beginning of a calm and successful year.",
                    "Advance happy birthday. You deserve joy before, during, and after the day.",
                ],
            },
            {
                "key": "lover",
                "h2": "Advance Birthday Wishes for Lover",
                "lines": [
                    "Advance happy birthday, my love. I want my wish to reach your heart before the world gets noisy.",
                    "Your birthday is not here yet, but my love for you is already celebrating.",
                    "Happy birthday in advance to the person who makes my days warmer and my future softer.",
                    "May your birthday bring you the peace, comfort, and love you give me so easily.",
                    "I am sending this early because loving you has made every special day feel bigger.",
                    "Advance birthday wishes, sweetheart. I hope your smile stays bright all year.",
                    "Before your birthday arrives, I want to remind you that you are deeply loved.",
                    "Happy birthday in advance, my favourite person. May life be extra kind to you.",
                    "I do not need the exact date to celebrate you. You are special every day.",
                    "Advance wishes, love. May your year be full of us, laughter, and quiet happiness.",
                ],
            },
            {
                "key": "friend",
                "h2": "Advance Birthday Wishes for Friend",
                "lines": [
                    "Happy birthday in advance, friend. May your day be full of laughter and your year full of progress.",
                    "Sending early wishes because good friends deserve thoughtful reminders.",
                    "Advance birthday wishes to a friend who brings honesty, warmth, and fun wherever they go.",
                    "May your birthday bring peace, health, and people who celebrate you properly.",
                    "I am wishing you early so the birthday happiness starts now.",
                    "Advance happy birthday, dear friend. Stay blessed and keep shining.",
                    "May the year ahead reward your patience, effort, and kind heart.",
                    "Happy birthday in advance. I hope this new chapter feels exciting and safe.",
                    "Your birthday may be coming soon, but my gratitude for your friendship is already here.",
                    "Advance wishes for cake, comfort, confidence, and good news.",
                ],
            },
            {
                "key": "family",
                "h2": "Advance Birthday Wishes for Family",
                "lines": [
                    "Advance happy birthday to one of the most loved people in our family.",
                    "Sending early blessings for health, happiness, and a year full of peaceful days.",
                    "Happy birthday in advance. May our family always have reasons to celebrate you.",
                    "Before the birthday rush begins, here is my warmest wish for your beautiful year ahead.",
                    "May your birthday bring laughter to the house and blessings to your heart.",
                    "Advance wishes with love from the family that is always proud of you.",
                    "I am early, but the love is timeless. Happy birthday in advance.",
                    "May this year bring strength for hard days and joy for ordinary ones.",
                    "Advance happy birthday. Your presence makes family moments warmer.",
                    "Wishing you a birthday filled with love, respect, and familiar smiles.",
                ],
            },
            {
                "key": "whatsapp",
                "h2": "Advance Birthday Wishes for WhatsApp",
                "lines": [
                    "Happy birthday in advance. Stay blessed and keep smiling.",
                    "Advance happy birthday. Wishing you health, joy, and success.",
                    "Sending early wishes before your phone gets too busy.",
                    "May your birthday be as special as your heart.",
                    "Advance birthday wishes. Have a bright and beautiful year.",
                    "Happy birthday in advance. Lots of love and good vibes.",
                    "Early wish, full heart, endless blessings.",
                    "May your day arrive with cake, smiles, and good news.",
                    "Advance happy birthday. Celebrate well and stay happy.",
                    "Wishing you early because you deserve the first smile.",
                ],
            },
            {
                "key": "funny",
                "h2": "Funny Advance Birthday Wishes",
                "lines": [
                    "Happy birthday in advance because I might forget later, and honesty is a gift.",
                    "I am early this year. Please mark this rare achievement in family history.",
                    "Advance birthday wishes. Now you cannot accuse me of being late.",
                    "Sending this early before my memory starts acting like expired cake.",
                    "Happy birthday in advance. You are welcome for the premium early delivery.",
                    "I am not early, everyone else is simply late to the celebration.",
                    "Advance wishes because your birthday deserves a trailer before the main event.",
                    "Consider this the first notification in your birthday spam season.",
                    "Happy birthday in advance. Age responsibly, or at least entertainingly.",
                    "I wished early, so I have officially earned extra cake.",
                ],
            },
            {
                "key": "short",
                "h2": "Short Advance Birthday Wishes",
                "lines": [
                    "Happy birthday in advance. Stay blessed.",
                    "Advance wishes for a beautiful year.",
                    "Early love for your special day.",
                    "Advance happy birthday, dear one.",
                    "Wishing you joy before the day begins.",
                    "Birthday countdown starts with love.",
                    "Early wish, warm heart.",
                    "Advance blessings for you.",
                    "May your birthday be wonderful.",
                    "Celebrating you a little early.",
                ],
            },
            {
                "key": "captions",
                "h2": "Advance Birthday Captions",
                "lines": [
                    "Starting the birthday love early.",
                    "Too special to wish late.",
                    "Birthday countdown, heart full.",
                    "Early wishes, real love.",
                    "Celebrating before the candles.",
                    "Advance birthday energy unlocked.",
                    "First wish, warmest wish.",
                    "Because your day deserves a head start.",
                    "A little early, fully heartfelt.",
                    "Birthday week begins now.",
                ],
            },
            {
                "key": "sorry_early",
                "h2": "Sorry I Am Early Birthday Messages",
                "lines": [
                    "Sorry I am early, but I did not want my wish to get lost in the birthday rush.",
                    "I know your birthday is not today, but my excitement arrived before the date.",
                    "Sorry for wishing early. I just wanted to be the first reason you smiled.",
                    "I may be ahead of time, but the love behind this wish is exactly on time.",
                    "Forgive the early message. Your birthday deserves a long celebration anyway.",
                    "Sorry I am early, but special people deserve advance happiness.",
                    "The calendar can wait. My warm wish could not.",
                    "I am early because your birthday is already on my mind.",
                    "Sorry for the advance wish. I hope it starts your birthday mood early.",
                    "Early or not, the blessing is real. Happy birthday in advance.",
                ],
            },
            {
                "key": "gift",
                "h2": "A Small Early Birthday Gift Idea",
                "lines": [
                    "An advance birthday wish can feel even warmer when it arrives with a small keepsake.",
                    "Choose jewellery only when it suits the relationship and the person's everyday style.",
                    "For a best friend, pick something easy to wear, not too formal or too loud.",
                    "For love, a pendant, ring, bracelet, or earrings can make the early message feel more personal.",
                    "Keep the note simple so the gift does not overpower the feeling.",
                    "Avoid mentioning price in the message.",
                    "A good early gift says I remembered you before the day became busy.",
                    "The most thoughtful piece is the one they can wear beyond birthday week.",
                    "Let comfort and personal style guide the choice.",
                    "The wish is the heart of the moment, and the keepsake is only the quiet reminder.",
                ],
            },
        ],
        "section_leads": {
            "Best Advance Birthday Wishes 2026": "Use these warm all-purpose lines when you want to wish someone before the date without sounding awkward.",
            "Advance Birthday Wishes for Best Friend": "Best friend wishes can be playful, loyal, and a little emotional because the bond already carries that tone.",
            "Advance Happy Birthday Wishes": "These clear advance happy birthday wishes work for colleagues, cousins, neighbours, and anyone you want to greet politely.",
            "Advance Birthday Wishes for Lover": "Romantic advance wishes should feel soft and private, not overly public or performative.",
            "Advance Birthday Wishes for Friend": "Friendship wishes work best when they are warm, easy to send, and not too formal.",
            "Advance Birthday Wishes for Family": "Family advance wishes can carry blessings, pride, and a little extra affection.",
            "Advance Birthday Wishes for WhatsApp": "Use these when you need a compact line for chats, groups, or quick replies.",
            "Funny Advance Birthday Wishes": "Funny lines are safest when they tease your timing, not the person.",
            "Short Advance Birthday Wishes": "Short wishes are useful when you want a clean one-liner with no extra decoration.",
            "Advance Birthday Captions": "These captions fit photo posts, countdown Stories, and birthday-week updates.",
            "Sorry I Am Early Birthday Messages": "If you feel awkward about wishing too soon, say it lightly and keep the warmth clear.",
            "A Small Early Birthday Gift Idea": "A gift is optional. The early message should still carry the emotion.",
        },
        "faqs": [
            ["What is the best advance birthday wish?", "The best advance birthday wish is warm, simple, and explains why you are early. Try: Sending advance birthday wishes because someone as special as you deserves love before the day even begins."],
            ["How do I say happy birthday in advance?", "Say Happy birthday in advance, then add one personal blessing. For example: Happy birthday in advance. May your day be full of love and your year full of peace."],
            ["Can I send advance birthday wishes to my best friend?", "Yes. Best friends often appreciate early wishes because they feel thoughtful. Add a shared memory or a playful line so the message does not sound copied."],
            ["Are advance birthday wishes good for WhatsApp?", "Yes. Keep WhatsApp wishes short and easy to read. A simple line such as Advance happy birthday, stay blessed and keep smiling works well."],
            ["What is a funny advance birthday wish?", "A funny advance wish can be: Happy birthday in advance because I might forget later, and honesty is a gift. Keep the joke about your timing, not their age or appearance."],
            ["Can I send a gift with advance birthday wishes?", "Yes, if the relationship feels close enough. A small keepsake can make the early wish memorable, but the message should stay personal and never mention price."],
        ],
    }

    config = {
        "rank": 87,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-advancebirthday",
        "occasion_year": "Advance Birthday Wishes 2026",
        "carousel_alt_prefix": "advance birthday wishes 2026 gift idea",
        "gift_h2": "Early Birthday Gift Ideas That Feel Thoughtful",
        "gift_blurb": "An early wish already shows attention. If you add a keepsake, keep it personal, wearable, and quiet. These six approved BlueStone designs fit best-friend, love, and family gifting without turning the article into a catalogue.",
        "conclusion_html": "Advance birthday wishes work because they say, I remembered before the rush. Pick a short line, add the person's name, and let the early message feel thoughtful, not accidental.",
        "schema_keywords": [
            "advance birthday wishes",
            "advance birthday wishes for best friend",
            "advance happy birthday wishes to best friend",
            "advance happy birthday wishes",
            "happy birthday in advance",
        ],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(rows, "The Thyvarne Pendant", "Pendants"),
            product(rows, "The Estrella Oval Bangle", "Bangles"),
            product(rows, "The Faliha Purse Hoop Earrings", "Earrings"),
            product(rows, "The Haily Ring", "Rings"),
            product(rows, "The Pervinca Charm Holder Bracelet", "Bracelet"),
            product(rows, "The Kricia Charm Bracelet", "Bracelet"),
        ],
        "flatlay_insert_h2": "Advance Birthday Wishes for WhatsApp",
        "lifestyle_insert_h2": "A Small Early Birthday Gift Idea",
        "more_reads_html": "Keep planning with <a href=\"https://blog.bluestone.com/birthday-wishes-for-cousin-brother-sister-2026/\">birthday wishes for cousin 2026</a>, <a href=\"https://blog.bluestone.com/birthday-wishes-for-nephew-2026/\">birthday wishes for nephew 2026</a>, <a href=\"https://blog.bluestone.com/happy-birthday-wishes-for-uncle-2026/\">birthday wishes for uncle 2026</a>, and <a href=\"https://blog.bluestone.com/sorry-for-late-wishes-2026/\">sorry for late wishes 2026</a>.",
        "how_to_html": "Send advance birthday wishes one to three days early for close friends and family, or earlier if travel, exams, work, or time zones may get in the way. Keep the tone natural, add a name, and avoid making the message sound like a reminder.",
        "faq_h2": "Frequently Asked Questions about Advance Birthday Wishes",
        "min_lines": 100,
        "section_leads": sections["section_leads"],
    }

    prompts = {
        "rank": 87,
        "slug": "advance-happy-birthday-wishes-2026",
        "output_prefix": PREFIX,
        "occasion": "Advance Birthday Wishes 2026",
        "primary_kw": "advance birthday wishes",
        "caption_occasion": "Advance birthday wishes",
        "caption_year": "2026",
        "flatlay_setting": "study-desk",
        "workflow": "Higgsfield MCP nano_banana_pro. Campaign hybrid with mandatory body_image scale line for people shots. Do not generate until balance succeeds. Max 2 concurrent generations.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/advance-birthday-wishes-hero-2026.webp",
            "flatlay": "output/magnific_generated/advance-birthday-wishes-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/advance-birthday-wishes-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "advance birthday wishes 2026 hero The Thyvarne Pendant",
            "flatlay": "advance birthday wishes 2026 flatlay The Estrella Oval Bangle",
            "lifestyle": "advance birthday wishes 2026 lifestyle The Faliha Purse Hoop Earrings",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                "code": "BISW1080P28",
                "name": "The Thyvarne Pendant",
                "gender": "Female",
                "height_mm": 17.5,
                "width_mm": 17.5,
                "size_prompt_note": "pendant product height 17.5 mm and width 17.5 mm; product dimensions, not face size; copy worn neck scale from body_image",
                "alt": "advance birthday wishes 2026 hero with The Thyvarne Pendant",
                "caption": "Advance birthday wishes 2026 vibe: The Thyvarne Pendant",
                "product": {"code": "BISW1080P28", "name": "The Thyvarne Pendant", "pdp": "https://www.bluestone.com/pendants/the-thyvarne-pendant~173761.html"},
                "cdn": [
                    "https://kinclimg8.bluestone.com/giproduct/BISW1080P28_RAA18DIG6MALAXXXX_ABCD00-BP-PICS-00000-1024-114065.png",
                    "https://kinclimg3.bluestone.com/giproduct/BISW1080P28_RAA18DIG6MALAXXXX_ABCD00-PICS-00004-1024-114065.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Thyvarne Pendant/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Thyvarne Pendant/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": "Photoreal candid lifestyle photograph with high-end jewellery commercial fidelity on the worn piece only. Natural skin texture, controlled soft key light, gentle fill, realistic shadows, proper shallow depth of field at 85mm, balanced exposure, no blown whites, no HDR glare, DSLR, HD, 16:9 with safe margins.\n\nCasting required: solo fair-skinned Indian adult woman only, light wheatish to fair urban Indian complexion. Exactly one person in frame. No second person, no extra hands.\n\nAdvance birthday wishes 2026 candid home moment: the woman smiles while preparing a blank cream birthday card and sealed envelope on a warm desk beside a tea cup and soft pastel flowers. Full face and upper body visible. The card and envelope must be blank with no letters, no handwriting, no symbols, no numbers.\n\nThe woman physically wears The Thyvarne Pendant from @img1 body_image and @img2 design on a fine chain at her upper chest. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: pendant product height_mm=17.5 and width_mm=17.5. These are real product dimensions, NOT face-size instructions. Keep pendant size on the neck like @img1 body_image worn neck scale: small pendant size, subtle, not enlarged. Use @img2 only for the jewellery design.\n\nReplicate the yellow gold circular diamond pendant exactly. HD hyperreal metal and stone detail, 100 percent identical to refs, zero distortion. This pendant is the single and only jewellery in the image. Bare ears, bare wrists, bare fingers, no watch, no bracelet, no ring, no earrings. Jewellery touches fabric/skin with a soft contact shadow and is never a floating cutout.\n\nAvoid: readable text, handwriting, printed letters, numbers, symbols on card, second person, extra hands, extra necklaces, rings, watches, earrings, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, cropped face, dark skin, deep brown skin, heavily tanned skin, illustration, CGI.",
            },
            "flatlay": {
                "code": "BIDG0393O37",
                "name": "The Estrella Oval Bangle",
                "gender": "Female",
                "height_mm": 50.19,
                "width_mm": 7.1,
                "size_prompt_note": "bangle inner diameter/height 50.19 mm and band width 7.1 mm; product dimensions, not face size",
                "alt": "advance birthday wishes 2026 flatlay with The Estrella Oval Bangle",
                "caption": "Advance birthday wishes 2026 keepsake: The Estrella Oval Bangle",
                "product": {"code": "BIDG0393O37", "name": "The Estrella Oval Bangle", "pdp": "https://www.bluestone.com/bangles/the-estrella-oval-bangle~34771.html"},
                "cdn": [
                    "https://kinclimg1.bluestone.com/giproduct/BIDG0393O37_YAA18DIG6XXXXXXXX_ABCD00-PICS-00001-1024-28014.png",
                    "https://kinclimg1.bluestone.com/giproduct/BIDG0393O37_YAA18DIG6XXXXXXXX_ABCD00-PICS-00002-1024-28014.png",
                    "https://kinclimg1.bluestone.com/giproduct/BIDG0393O37_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-28014.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Bangles/The Estrella Oval Bangle/0_primary.png",
                    "ProductImages/raw/Bangles/The Estrella Oval Bangle/2_front.png",
                    "ProductImages/raw/Bangles/The Estrella Oval Bangle/3_side_1.png",
                ],
                "ref_roles": ["primary", "front", "side"],
                "prompt": "Photoreal high-end jewellery still life, top-down editorial product flatlay, controlled soft key light, realistic gentle shadows, shallow depth of field, HD metal and stone detail, 16:9 landscape.\n\nAdvance birthday wishes 2026 top-down flatlay. Flatlay setting ID: study-desk. Surface and props: warm study desk, blank cream greeting card, sealed envelope, wooden pencil, plain ribbon, tiny flower stem, and a phone with a completely blank dark screen. No readable text, no letters, no numbers, no symbols on any prop.\n\nThe identical Estrella Oval Bangle from @img1, @img2 and @img3 rests naturally on the desk at true PDP scale. Product dimensions from PDP: bangle inner diameter height_mm=50.19 and band_width_mm=7.1. These are product dimensions, NOT face-size instructions. Do not enlarge for visibility. Full bangle visible, polished yellow gold with diamond/star detail, crisp oval form, 100 percent identical design, zero distortion.\n\nProps stay secondary and quiet. No people, no hands, no readable text, no brand marks. Jewellery is the clear subject but still true to real size.\n\nAvoid: hands, people, floating overlays, cutouts, incorrect bangle design, distorted stones, readable text, logos, price tags, brand marks on props, blown whites, HDR glare, illustration, CGI.",
            },
            "lifestyle": {
                "code": "BIJP0686H03",
                "name": "The Faliha Purse Hoop Earrings",
                "gender": "Female",
                "height_mm": 13.86,
                "width_mm": 13.12,
                "size_prompt_note": "earring overall height 13.86 mm and width 13.12 mm; product dimensions, not face size; copy worn ear scale from body_image",
                "alt": "advance birthday wishes 2026 lifestyle with The Faliha Purse Hoop Earrings",
                "caption": "Advance birthday wishes 2026 vibe: The Faliha Purse Hoop Earrings",
                "product": {"code": "BIJP0686H03", "name": "The Faliha Purse Hoop Earrings", "pdp": "https://www.bluestone.com/earrings/the-faliha-purse-hoop-earrings~73262.html"},
                "cdn": [
                    "https://kinclimg5.bluestone.com/giproduct/BIJP0686H03_YAA18DIG4XXXXXXXX_ABCD00-BP-PICS-00000-1024-84306.png",
                    "https://kinclimg9.bluestone.com/giproduct/BIJP0686H03_YAA18DIG4XXXXXXXX_ABCD00-PICS-00003-1024-84306.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Earrings/The Faliha Purse Hoop Earrings/1_body_portrait.png",
                    "ProductImages/raw/Earrings/The Faliha Purse Hoop Earrings/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": "Photoreal candid lifestyle photograph with high-end jewellery commercial fidelity on the worn piece only. Natural skin texture, controlled soft key light, gentle fill, realistic shadows, proper shallow depth of field at 85mm, balanced exposure, no blown whites, no HDR glare, DSLR, HD, 16:9 with safe margins.\n\nCasting required: solo fair-skinned Indian adult woman only, light wheatish to fair urban Indian complexion. Exactly one person in frame. No second person, no extra hands.\n\nAdvance birthday wishes 2026 lifestyle moment: the woman sits by a bright cafe window smiling at a blank phone screen, with a sealed birthday card and small wrapped gift on the table. Her full face and ears are visible. The phone screen and card must be blank with no letters, no handwriting, no symbols, no numbers.\n\nThe woman physically wears The Faliha Purse Hoop Earrings from @img1 body_image and @img2 design on both ears. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: earring overall height_mm=13.86 and width_mm=13.12. These are real product dimensions, NOT face-size instructions. Keep earring size on the ear like @img1 body_image worn ear scale: subtle hoop size, not enlarged. Use @img2 only for the jewellery design.\n\nReplicate the yellow gold purse hoop earrings with horizontal baguette diamond bar exactly. HD hyperreal metal and stones, 100 percent identical to refs, zero distortion. These earrings are the single and only jewellery in the image. Bare neck, bare wrists, bare fingers, no watch, no bracelet, no ring, no necklace. Jewellery touches ear with a soft contact shadow and is never a floating cutout.\n\nAvoid: readable text, handwriting, printed letters, numbers, symbols on phone or card, second person, extra hands, extra necklaces, rings, watches, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, cropped face, dark skin, deep brown skin, heavily tanned skin, illustration, CGI.",
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 87

Article: Advance Birthday Wishes 2026
Status: Draft assets prepared
Date: 2026-07-23

## A. Intent and Brief
- [x] Primary keyword: advance birthday wishes
- [x] Supporting keywords mapped to H2s and FAQs
- [x] Sheet Action New respected
- [x] Fresh slug: advance-happy-birthday-wishes-2026
- [x] 2026 year lock used

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""

    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json("output/publish_configs/rank87.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
