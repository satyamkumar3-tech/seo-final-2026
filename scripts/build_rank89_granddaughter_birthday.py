#!/usr/bin/env python3
"""Build Rank 89 birthday wishes for granddaughter assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank89_GranddaughterBirthday"


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
            "title": "Birthday Wishes for Granddaughter 2026: Sweet Messages",
            "slug": "birthday-wishes-for-granddaughter-2026",
            "meta_desc": "Birthday wishes for granddaughter 2026 with sweet, short, heartfelt, funny, blessing, and grandparent messages for cards, WhatsApp, captions, and gifts.",
            "focus_kw": "birthday wishes for granddaughter",
            "yoast_title": "Birthday Wishes for Granddaughter 2026",
        },
        "intro": [
            "Birthday wishes for granddaughter should feel tender, proud, and easy to send. The best message sounds like it came from a grandparent who has watched her grow, not from a copied template.",
            "TL;DR: use a short wish for WhatsApp, a heartfelt note for a card, a blessing for family groups, and one personal memory when you want the message to feel truly yours.",
        ],
        "sections": [
            {
                "key": "best",
                "h2": "Best Birthday Wishes for Granddaughter 2026",
                "lines": [
                    "Happy birthday, my dear granddaughter. May your life stay bright, kind, and full of beautiful surprises.",
                    "Wishing you a birthday filled with laughter, cake, hugs, and the confidence to chase every dream.",
                    "Happy birthday to the granddaughter who makes our family feel younger, happier, and more hopeful.",
                    "May 2026 bring you health, courage, good friends, and moments that make your heart proud.",
                    "You are a blessing we never stop thanking life for. Happy birthday, sweetheart.",
                    "Happy birthday, granddaughter. May your smile stay easy and your path stay full of light.",
                    "Watching you grow has been one of the sweetest gifts of our lives.",
                    "May your birthday remind you how deeply you are loved by your family.",
                    "Happy birthday to the girl who carries sunshine into every room she enters.",
                    "May this new year of life give you joy, wisdom, and beautiful reasons to celebrate.",
                ],
            },
            {
                "key": "heartfelt",
                "h2": "Heart Touching Birthday Wishes for Granddaughter",
                "lines": [
                    "You came into our lives like a small miracle and grew into a reason for endless pride.",
                    "Happy birthday, my granddaughter. Your kindness is the kind of beauty that never fades.",
                    "Every year, you teach us that love can grow larger without making noise.",
                    "May you always know that you have a safe place in our hearts.",
                    "Your dreams matter, your voice matters, and your happiness matters to us deeply.",
                    "Happy birthday. We are proud not only of what you do, but of who you are becoming.",
                    "May life treat your gentle heart with the same care you give others.",
                    "You are loved more than any birthday card could ever hold.",
                    "May your journey be protected, peaceful, and full of people who value you.",
                    "Happy birthday, dear granddaughter. You are one of our greatest joys.",
                ],
            },
            {
                "key": "from_grandparents",
                "h2": "Birthday Wishes for Granddaughter from Grandparents",
                "lines": [
                    "From your grandparents, happy birthday with all our blessings, love, and pride.",
                    "You make our home brighter every time you visit, call, or send one little message.",
                    "Happy birthday, beta. We pray your life stays peaceful, healthy, and successful.",
                    "You are our little star, even when you are all grown up.",
                    "May your birthday bring you the same happiness you bring into our old hearts.",
                    "We bless you with courage for hard days and gratitude for good days.",
                    "Happy birthday from the grandparents who will always cheer for you first.",
                    "May your path be kind, your choices be wise, and your heart stay soft.",
                    "We may not always say it perfectly, but we love you more than words manage.",
                    "Happy birthday, granddaughter. Our blessings are with you today and every day.",
                ],
            },
            {
                "key": "short",
                "h2": "Short Birthday Wishes for Granddaughter",
                "lines": [
                    "Happy birthday, dear granddaughter. Stay blessed.",
                    "Love, joy, and blessings to you today.",
                    "You make us proud every day.",
                    "Happy birthday to our sweet sunshine.",
                    "May your year be bright and kind.",
                    "Keep smiling, keep shining, sweetheart.",
                    "Birthday hugs from your loving family.",
                    "You are loved more than you know.",
                    "Happy birthday, our precious girl.",
                    "Blessings, laughter, and cake for you.",
                ],
            },
            {
                "key": "blessings",
                "h2": "Birthday Blessings for Granddaughter",
                "lines": [
                    "May God bless you with health, wisdom, protection, and a heart full of peace.",
                    "May every step you take lead you toward safety, happiness, and honest success.",
                    "On your birthday, we pray your life is surrounded by good people and good choices.",
                    "May your mind stay strong, your heart stay kind, and your dreams stay alive.",
                    "Blessings to you, granddaughter, for a year filled with grace and gentle growth.",
                    "May your birthday open a year where stress becomes lighter and joy becomes easier.",
                    "We pray that your talents find the right opportunities at the right time.",
                    "May you always be protected from harm and guided toward what is good for you.",
                    "Happy birthday. May love, faith, and courage walk beside you in 2026.",
                    "May your life bloom in ways that make your soul feel peaceful.",
                ],
            },
            {
                "key": "whatsapp",
                "h2": "Birthday Wishes for Granddaughter for WhatsApp",
                "lines": [
                    "Happy birthday, my sweet granddaughter. Sending you love, blessings, and the biggest virtual hug.",
                    "May your day be full of cake, smiles, photos, and happy little surprises.",
                    "Happy birthday, beta. We are so proud of you and love you very much.",
                    "Wishing you a beautiful birthday and a year that feels kind to your heart.",
                    "Stay happy, stay healthy, and keep shining in your own lovely way.",
                    "Happy birthday. Your grandparents are thinking of you with so much love today.",
                    "May this birthday bring you new confidence and old familiar comfort.",
                    "Sending blessings across this message, with more love than the phone can hold.",
                    "Happy birthday, granddaughter. May every dream that is good for you come closer.",
                    "Enjoy your special day, sweetheart. You deserve all the joy today.",
                ],
            },
            {
                "key": "funny",
                "h2": "Funny Birthday Wishes for Granddaughter",
                "lines": [
                    "Happy birthday, granddaughter. You are proof that our family became cooler with time.",
                    "May your cake be bigger than your homework, office work, or responsibilities.",
                    "Happy birthday from the grandparents who still think you are five, no matter your age.",
                    "You keep growing up, and we keep pretending we are not getting older.",
                    "May your birthday be full of gifts and zero lectures from anyone.",
                    "Happy birthday. We promise not to tell embarrassing childhood stories today, maybe.",
                    "You are sweet, smart, and slightly responsible for all our phone storage being full of photos.",
                    "May your day be as fun as your smile and as peaceful as a silent family group.",
                    "Happy birthday, beta. Eat cake first; wisdom can wait until tomorrow.",
                    "Another year wiser, but still our little mischief partner.",
                ],
            },
            {
                "key": "adult",
                "h2": "Birthday Wishes for Grown-Up Granddaughter",
                "lines": [
                    "Happy birthday to our grown-up granddaughter, who still holds the same place in our hearts.",
                    "We admire the woman you are becoming and the grace with which you handle life.",
                    "May your adult life bring you independence without loneliness and ambition without pressure.",
                    "Happy birthday. You are strong, thoughtful, and more loved than you realise.",
                    "We are proud of your choices, your courage, and your ability to keep moving forward.",
                    "May this year bring clarity in work, peace in relationships, and joy in small routines.",
                    "You may be grown now, but our blessings still follow you like a quiet hand on your head.",
                    "Happy birthday, granddaughter. Build the life that feels honest to your heart.",
                    "May your dreams mature beautifully without losing their sparkle.",
                    "We love seeing you become your own person.",
                ],
            },
            {
                "key": "little",
                "h2": "Cute Birthday Wishes for Little Granddaughter",
                "lines": [
                    "Happy birthday to our little princess, whose smile can melt any serious mood.",
                    "May your day be full of balloons, stories, sweets, and happy little dances.",
                    "You are tiny in size and huge in joy.",
                    "Happy birthday, sweetheart. May your childhood stay safe, bright, and full of love.",
                    "Your giggles are the music our family loves most.",
                    "May every candle on your cake bring one new reason to smile.",
                    "Happy birthday to the little star who makes grandparents feel young again.",
                    "You are our cuddly blessing and our favourite little storyteller.",
                    "May your world stay colourful, curious, and kind.",
                    "Happy birthday, baby girl. You are loved beyond words.",
                ],
            },
            {
                "key": "captions",
                "h2": "Birthday Captions for Granddaughter",
                "lines": [
                    "Our granddaughter, our sunshine, our birthday joy.",
                    "Celebrating the girl who makes the family brighter.",
                    "Birthday blessings for our precious granddaughter.",
                    "Small girl, big love, endless pride.",
                    "She is growing beautifully and loved deeply.",
                    "Granddaughter love, birthday edition.",
                    "A family blessing in one beautiful smile.",
                    "Proud grandparents, happy hearts.",
                    "Another year of watching her shine.",
                    "Birthday girl, forever our little star.",
                ],
            },
            {
                "key": "long",
                "h2": "Long Birthday Messages for Granddaughter",
                "lines": [
                    "Happy birthday, my dear granddaughter. Every year, you give us new reasons to feel proud, thankful, and hopeful about the future.",
                    "You have grown in ways that are beautiful to watch: kinder, wiser, stronger, and still wonderfully yourself.",
                    "May this birthday remind you that your family is always standing behind you with love and blessings.",
                    "Whenever life feels confusing, remember that your worth is not measured by one result, one mistake, or one difficult season.",
                    "We pray that you find work that respects you, friendships that protect you, and dreams that keep your spirit alive.",
                    "Happy birthday. You have brought sweetness into our lives from the very beginning.",
                    "If we could gift you one thing forever, it would be confidence in your own heart.",
                    "May this year give you health, peace, laughter, progress, and quiet moments of gratitude.",
                    "We love you in the ordinary ways too: in every call, every memory, and every blessing we say for you.",
                    "Happy birthday, granddaughter. May your life keep unfolding with grace.",
                ],
            },
            {
                "key": "gift",
                "h2": "A Birthday Gift Idea for Your Granddaughter",
                "lines": [
                    "A birthday wish can be the emotional part of the day, while a small keepsake can become a memory she wears.",
                    "Choose jewellery that suits her age, routine, and personal style instead of only choosing what looks grand.",
                    "A pendant feels sweet when she likes everyday necklaces.",
                    "Hoop earrings suit a granddaughter who enjoys simple, polished style.",
                    "A bangle or bracelet can feel protective and festive without being too loud.",
                    "For a younger granddaughter, keep the gift gentle, safe, and family-approved.",
                    "Write one short note with the gift so the emotion stays clear.",
                    "Avoid price talk in the birthday message.",
                    "Let the blessing come first and the gift follow softly.",
                    "The best gift says, we noticed who you are becoming.",
                ],
            },
        ],
        "section_leads": {
            "Best Birthday Wishes for Granddaughter 2026": "Use these all-rounder wishes when you want a warm message that works in cards, chats, and family groups.",
            "Heart Touching Birthday Wishes for Granddaughter": "These lines are emotional without becoming heavy, ideal for a grandparent card.",
            "Birthday Wishes for Granddaughter from Grandparents": "Use these when the message is clearly coming from nana-nani, dada-dadi, or both grandparents together.",
            "Short Birthday Wishes for Granddaughter": "Short wishes are useful for WhatsApp, SMS, captions, and quick morning greetings.",
            "Birthday Blessings for Granddaughter": "These birthday blessings keep the tone graceful, family-friendly, and sincere.",
            "Birthday Wishes for Granddaughter for WhatsApp": "Use these copy-ready lines when you want a message that feels personal but not too long.",
            "Funny Birthday Wishes for Granddaughter": "Funny wishes work best when the joke is gentle and affectionate.",
            "Birthday Wishes for Grown-Up Granddaughter": "These messages fit an adult granddaughter who is studying, working, or building her own life.",
            "Cute Birthday Wishes for Little Granddaughter": "Use these softer lines for a young granddaughter, or as captions for childhood photos.",
            "Birthday Captions for Granddaughter": "These captions suit photo posts, reels, family albums, and birthday collages.",
            "Long Birthday Messages for Granddaughter": "Send a longer message when you want to say more than a quick happy birthday.",
            "A Birthday Gift Idea for Your Granddaughter": "A gift is optional; the blessing should still carry the heart of the birthday.",
        },
        "faqs": [
            ["What is the best birthday wish for granddaughter?", "A good birthday wish for granddaughter is loving, specific, and proud. Try: Happy birthday, my dear granddaughter. May your life stay bright, kind, and full of beautiful surprises."],
            ["How do grandparents wish a granddaughter happy birthday?", "Grandparents can mention pride, blessings, and one personal memory. Keep the tone warm and simple, then add a prayer for health, peace, and happiness."],
            ["What is a short birthday wish for granddaughter?", "A short birthday wish can be: Happy birthday, dear granddaughter. Stay blessed, keep smiling, and know that you are deeply loved."],
            ["What can I write for a grown-up granddaughter?", "For a grown-up granddaughter, write about pride, independence, courage, and the person she is becoming. Avoid sounding childish unless that is your shared family style."],
            ["Can birthday wishes for granddaughter be funny?", "Yes, if the humour is gentle. Joke about cake, old photos, or grandparents still seeing her as little, but avoid teasing age, looks, relationships, or sensitive topics."],
            ["Is jewellery a suitable birthday gift for a granddaughter?", "Jewellery can be thoughtful when it suits her age and style. Keep the note emotional and avoid price talk. A simple pendant, earrings, bracelet, or bangle can become a lasting keepsake."],
        ],
    }

    config = {
        "rank": 89,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-granddaughter",
        "occasion_year": "Birthday Wishes for Granddaughter 2026",
        "carousel_alt_prefix": "birthday wishes for granddaughter 2026 gift idea",
        "gift_h2": "Birthday Jewellery Gift Ideas for Granddaughter",
        "gift_blurb": "If the birthday wish carries the blessing, a wearable keepsake can hold the memory. These six approved BlueStone designs suit thoughtful granddaughter gifting without mentioning prices.",
        "conclusion_html": "Birthday wishes for granddaughter feel best when they sound like family love, not a formal greeting. Pick one line, add her name or a memory, and let your blessing make the birthday feel warmer.",
        "schema_keywords": [
            "birthday wishes for granddaughter",
            "heart touching birthday wishes for granddaughter",
            "birthday wishes for granddaughter from grandparents",
            "short birthday wishes for granddaughter",
            "birthday blessings for granddaughter",
            "birthday wishes for granddaughter 2026",
        ],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(rows, "The Valeria Rose Pendant", "Pendants"),
            product(rows, "The Skein Bangle", "Bangles"),
            product(rows, "The Vicky Hoop Earrings", "Earrings"),
            product(rows, "The Anya Ring", "Rings"),
            product(rows, "The Ailia Evil Eye Layered Necklace", "Necklaces"),
            product(rows, "The Novare Evil Eye Kids Nazariya Bracelet", "Kids Bracelets"),
        ],
        "flatlay_insert_h2": "Birthday Blessings for Granddaughter",
        "lifestyle_insert_h2": "A Birthday Gift Idea for Your Granddaughter",
        "more_reads_html": "For more family birthday inspiration, see <a href=\"https://blog.bluestone.com/birthday-wishes-for-cousin-brother-sister-2026/\">birthday wishes for cousin 2026</a>, <a href=\"https://blog.bluestone.com/birthday-wishes-for-nephew-2026/\">birthday wishes for nephew 2026</a>, <a href=\"https://blog.bluestone.com/whatsapp-birthday-wishes-for-wife-2026/\">birthday wishes for wife 2026</a>, and <a href=\"https://blog.bluestone.com/advance-happy-birthday-wishes-2026/\">advance birthday wishes 2026</a>.",
        "how_to_html": "For a granddaughter, start with love, add one blessing, and mention one real quality if you can. Keep WhatsApp wishes short, save longer emotions for a card, and avoid jokes that could embarrass her in a family group.",
        "faq_h2": "Frequently Asked Questions about Birthday Wishes for Granddaughter",
        "min_lines": 100,
        "section_leads": sections["section_leads"],
    }

    prompts = {
        "rank": 89,
        "slug": "birthday-wishes-for-granddaughter-2026",
        "output_prefix": PREFIX,
        "occasion": "Birthday Wishes for Granddaughter 2026",
        "primary_kw": "birthday wishes for granddaughter",
        "caption_occasion": "Birthday wishes for granddaughter",
        "caption_year": "2026",
        "flatlay_setting": "gift-wrapping-station",
        "workflow": "Higgsfield MCP nano_banana_pro. Campaign hybrid with mandatory body_image scale line for people shots. Do not generate until balance succeeds. Max 2 concurrent generations.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/birthday-wishes-for-granddaughter-hero-2026.webp",
            "flatlay": "output/magnific_generated/birthday-wishes-for-granddaughter-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/birthday-wishes-for-granddaughter-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "birthday wishes for granddaughter 2026 hero The Valeria Rose Pendant",
            "flatlay": "birthday wishes for granddaughter 2026 flatlay The Skein Bangle",
            "lifestyle": "birthday wishes for granddaughter 2026 lifestyle The Vicky Hoop Earrings",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                "code": "BIHS1145P21",
                "name": "The Valeria Rose Pendant",
                "gender": "Female",
                "height_mm": 21.0,
                "width_mm": 15.1,
                "size_prompt_note": "pendant product height 21.0 mm and width 15.1 mm; product dimensions, not face size; copy worn neck scale from body_image",
                "alt": "birthday wishes for granddaughter 2026 hero with The Valeria Rose Pendant",
                "caption": "Birthday wishes for granddaughter 2026 vibe: The Valeria Rose Pendant",
                "product": {"code": "BIHS1145P21", "name": "The Valeria Rose Pendant", "pdp": "https://www.bluestone.com/pendants/the-valeria-rose-pendant~181266.html"},
                "cdn": [
                    "https://kinclimg2.bluestone.com/giproduct/BIHS1145P21_RAA18DIG6XXXXXXXX_ABCD00-BP-PICS-00000-1024-119073.png",
                    "https://kinclimg2.bluestone.com/giproduct/BIHS1145P21_RAA18DIG6XXXXXXXX_ABCD00-PICS-00004-1024-119073.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Valeria Rose Pendant/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Valeria Rose Pendant/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": "STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. Birthday wishes for granddaughter 2026 hero, solo fair-skinned Indian adult woman, a grown-up granddaughter, sitting in a bright family living room and smiling while reading a blank birthday card from grandparents beside a small wrapped gift and blank phone screen. Full head, full face, both eyes, complete smile, neck, pendant, hands, blank card, gift, and upper body visible with safe margins. Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, soft daylight, realistic shadows, no HDR glare, 16:9.\n\nThe woman physically wears The Valeria Rose Pendant from @img1 body_image and @img2 design on a fine chain at upper chest. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: pendant product height_mm=21.0 and width_mm=15.1. These are real product dimensions, NOT face-size instructions. Keep pendant size on the neck like @img1 body_image worn neck scale: subtle pendant size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the rose gold heart pendant with right-side pave diamonds and left-side open triple rose gold bands exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery in the image. Bare ears, bare wrists, bare fingers, no watch, no bracelet, no ring, no earrings. Jewellery touches fabric or skin with soft contact shadow, never a floating cutout. The card and phone screen must be blank with no letters, no handwriting, no symbols, no numbers.\n\nAvoid: cropped face, cropped eyes, cropped forehead, cropped head, readable text, handwriting, printed letters, numbers, symbols on card or phone, child, minor, second person, grandparents in frame, extra hands, extra necklaces, rings, watches, earrings, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI.",
            },
            "flatlay": {
                "code": "BINK0363B03",
                "name": "The Skein Bangle",
                "gender": "Female",
                "height_mm": 51.51,
                "width_mm": 59.04,
                "size_prompt_note": "bangle product dimensions about 51.51 mm by 59.04 mm; product dimensions, not face size",
                "alt": "birthday wishes for granddaughter 2026 flatlay with The Skein Bangle",
                "caption": "Birthday wishes for granddaughter 2026 keepsake: The Skein Bangle",
                "product": {"code": "BINK0363B03", "name": "The Skein Bangle", "pdp": "https://www.bluestone.com/bangles/the-skein-bangle~27491.html"},
                "cdn": [
                    "https://kinclimg1.bluestone.com/giproduct/BINK0363B03_YAA18DIG6XXXXXXXX_ABCD00-PICS-00003-1024-20291.png",
                    "https://kinclimg1.bluestone.com/giproduct/BINK0363B03_YAA18DIG6XXXXXXXX_ABCD00-PICS-00002-1024-20291.png",
                    "https://kinclimg1.bluestone.com/giproduct/BINK0363B03_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-20291.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Bangles/The Skein Bangle/3_side_1.png",
                    "ProductImages/raw/Bangles/The Skein Bangle/2_front.png",
                    "ProductImages/raw/Bangles/The Skein Bangle/0_primary.png",
                ],
                "ref_roles": ["side", "front", "primary"],
                "prompt": "Photoreal high-end jewellery still life, top-down editorial product flatlay, controlled soft key light, realistic gentle shadows, shallow depth of field, HD metal and stone detail, 16:9 landscape.\n\nBirthday wishes for granddaughter 2026 top-down flatlay. Flatlay setting ID: gift-wrapping-station. Surface and props: soft cream wrapping paper, blank folded birthday card, silk ribbon, small sealed envelope, pale flowers, and a blank phone screen. No readable text, no letters, no numbers, no symbols on any prop.\n\nThe identical Skein Bangle from @img1, @img2 and @img3 rests naturally on the wrapping paper at true PDP scale. Product dimensions from PDP: bangle product dimensions about 51.51 mm by 59.04 mm. These are product dimensions, NOT face-size instructions. Do not enlarge for visibility. Full bangle visible, classic yellow gold circular bangle with detailed geometric chain pattern and small pave diamonds, 100 percent identical design, zero distortion.\n\nProps stay secondary and quiet. No people, no hands, no readable text, no brand marks. Jewellery is the clear subject but still true to real size.\n\nAvoid: hands, people, floating overlays, cutouts, incorrect bangle design, distorted stones, readable text, logos, price tags, brand marks on props, blown whites, HDR glare, illustration, CGI.",
            },
            "lifestyle": {
                "code": "BIIP0427H16",
                "name": "The Vicky Hoop Earrings",
                "gender": "Female",
                "height_mm": 14.75,
                "width_mm": 6.04,
                "size_prompt_note": "earring overall height 14.75 mm and width 6.04 mm; product dimensions, not face size; copy worn ear scale from body_image",
                "alt": "birthday wishes for granddaughter 2026 lifestyle with The Vicky Hoop Earrings",
                "caption": "Birthday wishes for granddaughter 2026 vibe: The Vicky Hoop Earrings",
                "product": {"code": "BIIP0427H16", "name": "The Vicky Hoop Earrings", "pdp": "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html"},
                "cdn": [
                    "https://kinclimg5.bluestone.com/giproduct/BIIP0427H16_YAA18DIG6XXXXXXXX_ABCD00-BP-PICS-00000-1024-76610.png",
                    "https://kinclimg2.bluestone.com/giproduct/BIIP0427H16_YAA18DIG6XXXXXXXX_ABCD00-PICS-00004-1024-76610.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Earrings/The Vicky Hoop Earrings/1_body_portrait.png",
                    "ProductImages/raw/Earrings/The Vicky Hoop Earrings/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": "STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. Birthday wishes for granddaughter 2026 lifestyle, solo fair-skinned Indian adult woman, a grown-up granddaughter, sitting alone near a bright window and smiling while holding a blank birthday card with a small wrapped gift on the table. Exactly one person in the entire image. No background people, no silhouettes, no extra faces, no grandparents, no child, no extra hands. Full face, both ears, blank card, gift, and upper body visible with safe margins. 85mm DSLR look, natural skin texture, soft daylight, realistic shadows, no HDR glare, 16:9.\n\nThe woman physically wears The Vicky Hoop Earrings from @img1 body_image and @img2 design on both ears. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: earring overall height_mm=14.75 and width_mm=6.04. These are real product dimensions, NOT face-size instructions. Keep earring size on the ear like @img1 body_image worn ear scale: subtle hoop size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the yellow gold hoop earrings with small diamond accents exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. These earrings are the single and only jewellery in the image. Bare neck, bare wrists, bare fingers, no watch, no bracelet, no ring, no necklace. Jewellery touches ear with soft contact shadow, never a floating cutout. The card must be blank with no letters, no handwriting, no symbols, no numbers.\n\nAvoid: background people, child, minor, second person, extra hands, silhouettes, staff, readable text, handwriting, printed letters, numbers, symbols on card, extra necklaces, rings, watches, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, cropped face, dark skin, deep brown skin, heavily tanned skin, illustration, CGI.",
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 89

Article: Birthday Wishes for Granddaughter 2026
Status: Draft assets prepared
Date: 2026-07-23

## A. Intent and Brief
- [x] Primary keyword: birthday wishes for granddaughter
- [x] Supporting keywords mapped to H2s and FAQs
- [x] Sheet Optimize treated as New
- [x] Fresh slug: birthday-wishes-for-granddaughter-2026
- [x] 2026 year lock used

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""

    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json("output/publish_configs/rank89.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
