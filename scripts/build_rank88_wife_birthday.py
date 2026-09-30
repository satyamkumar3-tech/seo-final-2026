#!/usr/bin/env python3
"""Build Rank 88 WhatsApp birthday wishes for wife assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank88_WifeBirthday"


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
            "title": "WhatsApp Birthday Wishes for Wife 2026: Romantic Lines",
            "slug": "whatsapp-birthday-wishes-for-wife-2026",
            "meta_desc": "WhatsApp birthday wishes for wife 2026 with romantic, short, loving, funny, advance, and my dear wife messages for chats, cards, captions, and images.",
            "focus_kw": "whatsapp birthday wishes for wife",
            "yoast_title": "WhatsApp Birthday Wishes for Wife 2026",
        },
        "intro": [
            "WhatsApp birthday wishes for wife should feel loving without sounding copied. The best line is short enough to send in a chat, warm enough to save, and personal enough to make her pause.",
            "TL;DR: choose a short message for morning WhatsApp, a romantic paragraph for private chat, a funny line only if she enjoys that tone, and an advance wish when travel or work may make you late.",
        ],
        "sections": [
            {
                "key": "best",
                "h2": "Best WhatsApp Birthday Wishes for Wife 2026",
                "lines": [
                    "Happy birthday, my love. Your smile makes my ordinary days feel blessed.",
                    "Wishing the happiest birthday to my wife, my best friend, and my favourite person.",
                    "Happy birthday, sweetheart. May 2026 bring you peace, health, confidence, and everything your heart quietly hopes for.",
                    "To my wife, thank you for turning our home into a place of love and comfort.",
                    "Happy birthday, jaan. I am grateful for your care, your patience, and the way you love.",
                    "May your day be full of flowers, laughter, rest, and the kind of attention you always give others.",
                    "Happy birthday to the woman who makes partnership feel soft, steady, and real.",
                    "I hope this year gives you more joy than stress and more dreams than doubts.",
                    "Happy birthday, wife. Loving you is still my favourite daily habit.",
                    "May your birthday remind you how deeply you are loved, seen, and celebrated.",
                ],
            },
            {
                "key": "birthday_greetings",
                "h2": "Birthday Greetings for Wife",
                "lines": [
                    "Warm birthday greetings to my beautiful wife. May your day be as gentle and bright as your heart.",
                    "Wishing you love, good health, peaceful mornings, and every success you deserve.",
                    "Happy birthday to the person who makes my life calmer, richer, and more meaningful.",
                    "May this new year of life bring you courage for big dreams and comfort for tired days.",
                    "Birthday greetings to my queen. You deserve every good thing that finds you.",
                    "May your year be full of happy surprises, safe people, and moments that feel like home.",
                    "Happy birthday, dear wife. Thank you for making love visible in small everyday ways.",
                    "Wishing you a birthday full of blessings and a year full of beautiful progress.",
                    "May your heart stay light and your smile stay easy through 2026.",
                    "Happy birthday to my partner, my calm, and my forever favourite.",
                ],
            },
            {
                "key": "birthday_msg",
                "h2": "Birthday Msg for Wife",
                "lines": [
                    "Birthday msg for wife: you are my peace after long days and my reason to keep becoming better.",
                    "Happy birthday, love. I may not say it perfectly, but I love you more than words manage.",
                    "You make our life beautiful in ways that never ask for applause.",
                    "On your birthday, I want to thank you for every unseen effort and every quiet kindness.",
                    "Happy birthday, meri jaan. You are loved in the morning, at night, and in every small moment between.",
                    "My favourite blessing is getting to call you my wife.",
                    "May your birthday bring you rest, joy, good food, and zero unnecessary stress.",
                    "You deserve a day where you are cared for the way you care for everyone else.",
                    "Happy birthday. I am proud of the woman you are and grateful for the life we share.",
                    "If I could gift you one thing, it would be a year that feels kind to your heart.",
                ],
            },
            {
                "key": "short_love",
                "h2": "Short Birthday Wishes for Wife with Love",
                "lines": [
                    "Happy birthday, my love. You are my home.",
                    "Love you today, tomorrow, and always.",
                    "Happy birthday to my favourite person.",
                    "You make my life beautifully complete.",
                    "Birthday love to my wife and best friend.",
                    "My heart is happiest with you.",
                    "Happy birthday, jaan. Stay blessed.",
                    "You are my forever smile.",
                    "Love, peace, and birthday joy to you.",
                    "Happy birthday, wife. I choose you always.",
                ],
            },
            {
                "key": "with_love",
                "h2": "Birthday Wishes for Wife with Love",
                "lines": [
                    "Happy birthday, my wife. My love for you grows in quiet ways every single year.",
                    "You are the person I want beside me in celebration, confusion, silence, and every ordinary evening.",
                    "May your birthday feel like the love you give so freely to everyone around you.",
                    "I love the way you care, laugh, plan, forgive, and still make space for hope.",
                    "Happy birthday, love. You are my blessing in both calm and chaos.",
                    "May this year bring you softness where life has been heavy.",
                    "Your happiness matters to me more than I can say in one WhatsApp message.",
                    "Happy birthday. I promise to keep choosing us with patience, respect, and love.",
                    "You are not just my wife, you are the heart of my everyday life.",
                    "May your birthday be full of reminders that you are cherished.",
                ],
            },
            {
                "key": "my_dear",
                "h2": "Happy Birthday My Dear Wife",
                "lines": [
                    "Happy birthday, my dear wife. You make my life brighter just by being in it.",
                    "My dear wife, may your birthday bring peace to your heart and joy to your smile.",
                    "Happy birthday, my dear. I am lucky to love you and luckier to be loved by you.",
                    "You are the warmth in our home and the softness in my hardest days.",
                    "Happy birthday, dear wife. May all your silent prayers find their answer this year.",
                    "My dear wife, thank you for being strong, gentle, and wonderfully you.",
                    "Happy birthday. I hope today gives you the comfort you give me every day.",
                    "To my dear wife, you deserve beauty, rest, laughter, and every blessing.",
                    "May your new year of life feel lighter, brighter, and deeply loved.",
                    "Happy birthday, my dear wife. You are my forever gift.",
                ],
            },
            {
                "key": "romantic_images",
                "h2": "Love Romantic Happy Birthday Images Messages",
                "lines": [
                    "Use this on an image: Happy birthday, my love. You are my favourite part of every day.",
                    "Image caption: My wife, my heart, my happiest blessing. Happy birthday.",
                    "Romantic image line: Your smile is still my favourite view.",
                    "Birthday image text: Loving you is the best story of my life.",
                    "Short overlay: Happy birthday to the queen of my heart.",
                    "Caption idea: One picture, endless love, and one beautiful birthday.",
                    "Image message: You are loved more than this photo can say.",
                    "Romantic caption: Every year with you becomes my favourite year.",
                    "Birthday image note: To my wife, with all my heart.",
                    "Sweet overlay: You make life softer. Happy birthday, love.",
                ],
            },
            {
                "key": "funny",
                "h2": "Funny Birthday Wishes for Wife on WhatsApp",
                "lines": [
                    "Happy birthday, wife. I promise to agree with you at least twice today.",
                    "You are ageing like fine wine, and I am ageing like the person who forgot where he kept the gift.",
                    "Happy birthday to my wife, the boss of my heart and also the remote control.",
                    "May your birthday be full of cake, gifts, and fewer questions about my planning skills.",
                    "Happy birthday, love. I cleaned one thing today, so please count that as romance.",
                    "You deserve diamonds, flowers, and a husband who remembers every instruction. I brought two out of three.",
                    "Happy birthday to the woman who is always right, especially today.",
                    "May your day be as beautiful as you and as calm as me when you ask what I forgot.",
                    "Happy birthday, wife. I love you more than my phone battery at one percent.",
                    "Let us celebrate you today and discuss my mistakes tomorrow.",
                ],
            },
            {
                "key": "advance_lover",
                "h2": "Advance Birthday Wishes for Lover",
                "lines": [
                    "Advance happy birthday, my love. I want my wish to reach before the birthday rush begins.",
                    "Your birthday is coming, but my heart is already celebrating you.",
                    "Happy birthday in advance to my wife, my lover, and my forever favourite person.",
                    "I may be early, but loving you has never followed a calendar.",
                    "Advance wishes, sweetheart. May your birthday week feel as special as you are.",
                    "Before the world sends wishes, here is mine with all my love.",
                    "Happy birthday in advance, jaan. I hope your day arrives with flowers, smiles, and peace.",
                    "I am sending this early because you deserve love before, during, and after your birthday.",
                    "Advance birthday wishes to the woman who owns my heart completely.",
                    "May your birthday countdown begin with my warmest hug in words.",
                ],
            },
            {
                "key": "long",
                "h2": "Long Birthday Messages for Wife",
                "lines": [
                    "Happy birthday, my love. I know one message can never hold everything you mean to me, but I hope today reminds you that your care, patience, laughter, and strength are noticed every day.",
                    "You have stood beside me through ordinary routines and difficult moments, and you still make life feel worth smiling about. May this year give you the peace you deserve.",
                    "On your birthday, I want to thank you for every small thing you do that keeps our life warm. I love you more deeply than I often say.",
                    "You are my partner, my comfort, and the person whose happiness matters to me in every season. Happy birthday, wife.",
                    "May this year bring you rest when you need it, excitement when you want it, and confidence in every dream you choose.",
                    "I hope you feel celebrated not only today but in the way I speak, listen, support, and show up for you.",
                    "Happy birthday to the woman whose love has made me better, softer, and more grateful.",
                    "If life gives us another thousand ordinary days, I would still choose to spend them beside you.",
                    "May your heart feel safe, your smile feel easy, and your dreams feel close this year.",
                    "You are my wife, my love, and my greatest everyday blessing.",
                ],
            },
            {
                "key": "captions",
                "h2": "Birthday Captions for Wife",
                "lines": [
                    "Birthday love for my forever person.",
                    "My wife, my heart, my happiest yes.",
                    "Celebrating the woman who makes life beautiful.",
                    "Queen of my heart, birthday of the year.",
                    "Another year of loving you louder.",
                    "My favourite smile turns a year wiser.",
                    "Birthday blessings for my beautiful wife.",
                    "She is the celebration.",
                    "Love looks like her.",
                    "Forever grateful for this birthday girl.",
                ],
            },
            {
                "key": "gift",
                "h2": "A Birthday Gift Idea for Your Wife",
                "lines": [
                    "A WhatsApp wish can begin the day, but a small keepsake can make the birthday feel remembered.",
                    "Choose jewellery that suits how she actually dresses, not only what looks grand in a display.",
                    "A pendant feels romantic when she likes everyday necklaces.",
                    "Bangles and rings work well when she enjoys visible, expressive pieces.",
                    "Earrings are a safe choice when her style is classic and easy to wear.",
                    "Keep the birthday note emotional and avoid making the gift sound like a transaction.",
                    "Do not mention price in the message.",
                    "A thoughtful gift says I noticed your style, not just the date.",
                    "Pair the piece with one personal line from the heart.",
                    "Let the wish lead and the jewellery quietly follow.",
                ],
            },
        ],
        "section_leads": {
            "Best WhatsApp Birthday Wishes for Wife 2026": "Use these all-rounder WhatsApp lines when you want love, respect, and warmth in one message.",
            "Birthday Greetings for Wife": "These greetings are polished enough for a card and still natural enough for WhatsApp.",
            "Birthday Msg for Wife": "Use these birthday msg for wife lines when you want a chat message that feels direct and personal.",
            "Short Birthday Wishes for Wife with Love": "Short wishes work best for morning texts, status replies, and a simple first message.",
            "Birthday Wishes for Wife with Love": "These lines are romantic but still grounded, so they feel like real partnership.",
            "Happy Birthday My Dear Wife": "Use this section when you want the phrase happy birthday my dear wife to sound tender and sincere.",
            "Love Romantic Happy Birthday Images Messages": "These lines fit image overlays, photo captions, and WhatsApp status images.",
            "Funny Birthday Wishes for Wife on WhatsApp": "Funny wishes are safest when they tease your own habits, not her age or appearance.",
            "Advance Birthday Wishes for Lover": "Use these if you may be busy later or want to start her birthday week early.",
            "Long Birthday Messages for Wife": "Send a longer message when the relationship deserves more than a one-line wish.",
            "Birthday Captions for Wife": "These captions work for photos, Stories, reels, and birthday collage posts.",
            "A Birthday Gift Idea for Your Wife": "A gift is optional. The wish should still carry the emotion.",
        },
        "faqs": [
            ["What is the best WhatsApp birthday wish for wife?", "A strong WhatsApp birthday wish for wife is short, loving, and personal. Try: Happy birthday, my love. Your smile makes my ordinary days feel blessed."],
            ["How do I write birthday greetings for wife?", "Start with Happy birthday, then add one quality you love about her and one blessing for the year ahead. Keep the tone warm, respectful, and natural."],
            ["What is a short birthday wish for wife with love?", "A short wish can be: Happy birthday, my love. You are my home. It is simple enough for WhatsApp and still feels romantic."],
            ["Can I send funny birthday wishes to my wife?", "Yes, if she enjoys that tone. Keep the joke affectionate and avoid teasing about age, appearance, or anything sensitive."],
            ["What can I write as happy birthday my dear wife?", "You can write: Happy birthday, my dear wife. You make my life brighter just by being in it. Add her name or a private detail if you want it to feel more personal."],
            ["Are advance birthday wishes for lover okay?", "Yes. Advance birthday wishes for lover are thoughtful when travel, work, or time zones may make you late. Say why you are early and keep the message loving."],
        ],
    }

    config = {
        "rank": 88,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-wifebirthday",
        "occasion_year": "Birthday Wishes for Wife 2026",
        "carousel_alt_prefix": "whatsapp birthday wishes for wife 2026 gift idea",
        "gift_h2": "Birthday Jewellery Gift Ideas for Wife",
        "gift_blurb": "If the birthday wish carries the emotion, a wearable keepsake can become the quiet reminder. These six approved BlueStone designs suit romantic birthday gifting without mentioning prices.",
        "conclusion_html": "WhatsApp birthday wishes for wife work best when they sound like your own love, not a copied line. Pick a wish, add her name or one private detail, and let the message begin her birthday with warmth.",
        "schema_keywords": [
            "whatsapp birthday wishes for wife",
            "birthday greetings for wife",
            "birthday msg for wife",
            "short birthday wishes for wife with love",
            "love romantic happy birthday images",
            "birthday wishes for wife with love",
            "happy birthday my dear wife",
            "advance birthday wishes for lover",
        ],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(rows, "The Thaloria Pendant", "Pendants"),
            product(rows, "The Pear Evil Eye Toggle Bangle", "Bangles"),
            product(rows, "The Ursa Hoop Earrings", "Earrings"),
            product(rows, "The Sarvanya Pendant", "Pendants"),
            product(rows, "The Quinn Ring", "Rings"),
            product(rows, "The Vicky Hoop Earrings", "Earrings"),
        ],
        "flatlay_insert_h2": "Love Romantic Happy Birthday Images Messages",
        "lifestyle_insert_h2": "A Birthday Gift Idea for Your Wife",
        "more_reads_html": "For more birthday inspiration, see <a href=\"https://blog.bluestone.com/advance-happy-birthday-wishes-2026/\">advance birthday wishes 2026</a>, <a href=\"https://blog.bluestone.com/birthday-wishes-for-nephew-2026/\">birthday wishes for nephew 2026</a>, <a href=\"https://blog.bluestone.com/birthday-wishes-for-cousin-brother-sister-2026/\">birthday wishes for cousin 2026</a>, and <a href=\"https://blog.bluestone.com/heart-touching-new-year-wishes-for-friends-2027/\">New Year wishes for friends 2027</a>.",
        "how_to_html": "For WhatsApp, send the first birthday wish early in the morning, then save a longer note for a card or private message. Mention one thing you genuinely love about your wife. If you use a funny line, pair it with a sincere second sentence.",
        "faq_h2": "Frequently Asked Questions about Birthday Wishes for Wife",
        "min_lines": 100,
        "section_leads": sections["section_leads"],
    }

    prompts = {
        "rank": 88,
        "slug": "whatsapp-birthday-wishes-for-wife-2026",
        "output_prefix": PREFIX,
        "occasion": "WhatsApp Birthday Wishes for Wife 2026",
        "primary_kw": "whatsapp birthday wishes for wife",
        "caption_occasion": "Birthday wishes for wife",
        "caption_year": "2026",
        "flatlay_setting": "marble-vanity",
        "workflow": "Higgsfield MCP nano_banana_pro. Campaign hybrid with mandatory body_image scale line for people shots. Do not generate until balance succeeds. Max 2 concurrent generations.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/whatsapp-birthday-wishes-for-wife-hero-2026.webp",
            "flatlay": "output/magnific_generated/whatsapp-birthday-wishes-for-wife-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/whatsapp-birthday-wishes-for-wife-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "whatsapp birthday wishes for wife 2026 hero The Thaloria Pendant",
            "flatlay": "whatsapp birthday wishes for wife 2026 flatlay The Pear Evil Eye Toggle Bangle",
            "lifestyle": "whatsapp birthday wishes for wife 2026 lifestyle The Ursa Hoop Earrings",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                "code": "BISW1080P131",
                "name": "The Thaloria Pendant",
                "gender": "Female",
                "height_mm": 36.91,
                "width_mm": 25.28,
                "size_prompt_note": "pendant product height 36.91 mm and width 25.28 mm; product dimensions, not face size; copy worn neck scale from body_image",
                "alt": "whatsapp birthday wishes for wife 2026 hero with The Thaloria Pendant",
                "caption": "Birthday wishes for wife 2026 vibe: The Thaloria Pendant",
                "product": {"code": "BISW1080P131", "name": "The Thaloria Pendant", "pdp": "https://www.bluestone.com/pendants/the-thaloria-pendant~165041.html"},
                "cdn": [
                    "https://kinclimg4.bluestone.com/giproduct/BISW1080P131_RAA18DIG4SYTZSURL_ABCD00-BP-PICS-00000-1024-113000.png",
                    "https://kinclimg7.bluestone.com/giproduct/BISW1080P131_RAA18DIG4SYTZSURL_ABCD00-PICS-00001-1024-113000.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Thaloria Pendant/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Thaloria Pendant/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": "STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. WhatsApp birthday wishes for wife 2026 hero, solo fair-skinned Indian adult woman in a bright bedroom or breakfast nook smiling at a blank birthday card and a blank phone screen on the table. Full head, full face, both eyes, complete smile, neck, pendant, hands, blank card, and upper body visible with safe margins. Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, soft daylight, realistic shadows, no HDR glare, 16:9.\n\nThe woman physically wears The Thaloria Pendant from @img1 body_image and @img2 design on a fine chain at upper chest. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: pendant product height_mm=36.91 and width_mm=25.28. These are real product dimensions, NOT face-size instructions. Keep pendant size on the neck like @img1 body_image worn neck scale: subtle pendant size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the rose gold fan pendant with center diamond halo, upper marquise purple stones, and lower trillion pink stones exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery in the image. Bare ears, bare wrists, bare fingers, no watch, no bracelet, no ring, no earrings. Jewellery touches fabric or skin with soft contact shadow, never a floating cutout. The card and phone screen must be blank with no letters, no handwriting, no symbols, no numbers.\n\nAvoid: cropped face, cropped eyes, cropped forehead, cropped head, readable text, handwriting, printed letters, numbers, symbols on card or phone, second person, extra hands, extra necklaces, rings, watches, earrings, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI.",
            },
            "flatlay": {
                "code": "BISL0804O13",
                "name": "The Pear Evil Eye Toggle Bangle",
                "gender": "Female",
                "height_mm": 57.18,
                "width_mm": 9.57,
                "size_prompt_note": "bangle face/inner dimension about 57.18 mm by 9.57 mm; product dimensions, not face size",
                "alt": "whatsapp birthday wishes for wife 2026 flatlay with The Pear Evil Eye Toggle Bangle",
                "caption": "Birthday wishes for wife 2026 keepsake: The Pear Evil Eye Toggle Bangle",
                "product": {"code": "BISL0804O13", "name": "The Pear Evil Eye Toggle Bangle", "pdp": "https://www.bluestone.com/bangles/the-pear-evil-eye-toggle-bangle~87037.html"},
                "cdn": [
                    "https://kinclimg9.bluestone.com/giproduct/BISL0804O13_RAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-60786.png",
                    "https://kinclimg9.bluestone.com/giproduct/BISL0804O13_RAA18DIG6XXXXXXXX_ABCD00-PICS-00002-1024-60786.png",
                    "https://kinclimg9.bluestone.com/giproduct/BISL0804O13_RAA18DIG6XXXXXXXX_ABCD00-PICS-00001-1024-60786.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Bangles/The Pear Evil Eye Toggle Bangle/0_primary.png",
                    "ProductImages/raw/Bangles/The Pear Evil Eye Toggle Bangle/2_front.png",
                    "ProductImages/raw/Bangles/The Pear Evil Eye Toggle Bangle/3_side_1.png",
                ],
                "ref_roles": ["primary", "front", "side"],
                "prompt": "Photoreal high-end jewellery still life, top-down editorial product flatlay, controlled soft key light, realistic gentle shadows, shallow depth of field, HD metal and stone detail, 16:9 landscape.\n\nWhatsApp birthday wishes for wife 2026 top-down flatlay. Flatlay setting ID: marble-vanity. Surface and props: soft marble vanity, blank cream birthday card, sealed envelope, silk ribbon, single rose, blank phone screen, and a small unlabeled perfume silhouette. No readable text, no letters, no numbers, no symbols on any prop.\n\nThe identical Pear Evil Eye Toggle Bangle from @img1, @img2 and @img3 rests naturally on the vanity at true PDP scale. Product dimensions from PDP: bangle face/inner dimension about 57.18 mm by 9.57 mm. These are product dimensions, NOT face-size instructions. Do not enlarge for visibility. Full bangle visible, thin rose gold bangle with circular blue evil eye bead and open pear pave diamond frame, 100 percent identical design, zero distortion.\n\nProps stay secondary and quiet. No people, no hands, no readable text, no brand marks. Jewellery is the clear subject but still true to real size.\n\nAvoid: hands, people, floating overlays, cutouts, incorrect bangle design, distorted stones, readable text, logos, price tags, brand marks on props, blown whites, HDR glare, illustration, CGI.",
            },
            "lifestyle": {
                "code": "BISP0427H21",
                "name": "The Ursa Hoop Earrings",
                "gender": "Female",
                "height_mm": 16.14,
                "width_mm": 10.07,
                "size_prompt_note": "earring overall height 16.14 mm and width 10.07 mm; product dimensions, not face size; copy worn ear scale from body_image",
                "alt": "whatsapp birthday wishes for wife 2026 lifestyle with The Ursa Hoop Earrings",
                "caption": "Birthday wishes for wife 2026 vibe: The Ursa Hoop Earrings",
                "product": {"code": "BISP0427H21", "name": "The Ursa Hoop Earrings", "pdp": "https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html"},
                "cdn": [
                    "https://kinclimg3.bluestone.com/giproduct/BISP0427H21_YAA18DIG6XXXXXXXX_ABCD00-BP-PICS-00000-1024-78187.png",
                    "https://kinclimg1.bluestone.com/giproduct/BISP0427H21_YAA18DIG6XXXXXXXX_ABCD00-PICS-00004-1024-78187.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Earrings/The Ursa Hoop Earrings/1_body_portrait.png",
                    "ProductImages/raw/Earrings/The Ursa Hoop Earrings/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": "STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. Birthday wishes for wife 2026 lifestyle, solo fair-skinned Indian adult woman only sitting alone near a bright window, smiling while reading a blank phone screen with a sealed birthday card and small wrapped gift on the table. Exactly one person in the entire image. No background people, no silhouettes, no extra faces, no staff, no extra hands. Full face, both ears, phone, blank card, and gift visible with safe margins. 85mm DSLR look, natural skin texture, soft daylight, realistic shadows, no HDR glare, 16:9.\n\nThe woman physically wears The Ursa Hoop Earrings from @img1 body_image and @img2 design on both ears. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: earring overall height_mm=16.14 and width_mm=10.07. These are real product dimensions, NOT face-size instructions. Keep earring size on the ear like @img1 body_image worn ear scale: subtle hoop size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the yellow gold hoop earrings with diamond accents exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. These earrings are the single and only jewellery in the image. Bare neck, bare wrists, bare fingers, no watch, no bracelet, no ring, no necklace. Jewellery touches ear with soft contact shadow, never a floating cutout. The phone screen and card must be blank with no letters, no handwriting, no symbols, no numbers.\n\nAvoid: background people, second person, extra hands, silhouettes, staff, readable text, handwriting, printed letters, numbers, symbols on phone or card, extra necklaces, rings, watches, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, cropped face, dark skin, deep brown skin, heavily tanned skin, illustration, CGI.",
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 88

Article: WhatsApp Birthday Wishes for Wife 2026
Status: Draft assets prepared
Date: 2026-07-23

## A. Intent and Brief
- [x] Primary keyword: whatsapp birthday wishes for wife
- [x] Supporting keywords mapped to H2s and FAQs
- [x] Sheet Optimize treated as New
- [x] Fresh slug: whatsapp-birthday-wishes-for-wife-2026
- [x] 2026 year lock used

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""

    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json("output/publish_configs/rank88.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
