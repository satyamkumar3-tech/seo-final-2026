#!/usr/bin/env python3
"""Build Week 3-4 Rank 1 Diwali wishes and quotes assets."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week34_Rank1_DiwaliWishesQuotes"
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
    return {
        "code": row["Design Code"],
        "name": name,
        "url": row["Link"],
        "png": png,
    }


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
            "title": "Diwali Wishes and Quotes 2026: Messages",
            "slug": "diwali-wishes-and-quotes-2026",
            "meta_desc": "Diwali wishes and quotes 2026 for family, friends, WhatsApp, Instagram, Deepavali greetings, inspirational lines, short captions, and festive messages.",
            "focus_kw": "diwali wishes and quotes",
            "yoast_title": "Diwali Wishes and Quotes 2026",
        },
        "intro": [
            "Diwali wishes and quotes feel best when they carry light, warmth, and blessings in a few honest words. In 2026, Diwali falls on Sunday, 8 November, so this is the right year to use in your greeting cards, WhatsApp notes, captions, and festive posts.",
            "TL;DR: Use short Diwali wishes for WhatsApp, warmer Deepavali wishes for family, bright captions for Instagram, and inspirational Diwali quotes when you want the message to feel thoughtful rather than routine.",
        ],
        "sections": [
            {
                "key": "short",
                "h2": "Short Diwali Wishes and Quotes",
                "lines": [
                    "Wishing you a Diwali filled with light, love, and peaceful beginnings.",
                    "May every diya bring hope, joy, and a little more courage into your life.",
                    "Happy Diwali 2026. May your home glow with happiness and your heart glow with gratitude.",
                    "May this festival of lights bring fresh energy and beautiful memories.",
                    "Wishing you laughter, sweets, blessings, and a home full of warmth.",
                    "May your Diwali be bright, calm, and full of people who feel like home.",
                    "Let the lights remind you that hope always finds a way.",
                    "Happy Deepavali. May goodness, grace, and joy walk into your life.",
                    "May your year ahead shine as gently and steadily as a diya.",
                    "Sending Diwali wishes and quotes full of love, peace, and festive sparkle.",
                    "May this Diwali bring clarity to your mind and kindness to your days.",
                    "Wishing you a beautiful Diwali and a brighter tomorrow.",
                ],
            },
            {
                "key": "family",
                "h2": "Happy Diwali Wishes for Family",
                "lines": [
                    "Happy Diwali to the family that makes every festival feel complete.",
                    "May our home stay blessed with laughter, health, togetherness, and light.",
                    "This Diwali, I am grateful for every memory we have made around lamps, sweets, and stories.",
                    "Wishing our family a peaceful Diwali and a year filled with gentle wins.",
                    "May Lakshmi ji bless our home with prosperity, wisdom, and harmony.",
                    "Happy Diwali 2026. May we always find time for each other, no matter how busy life gets.",
                    "May this festival bring us closer and remind us what truly matters.",
                    "Wishing you all a Diwali full of love, blessings, and warm family moments.",
                    "May every corner of our home shine with hope and every heart feel included.",
                    "Happy Deepavali to my favourite people and my safest place.",
                    "May this Diwali bless our elders, guide our children, and keep our bonds strong.",
                    "Let us celebrate with gratitude, simple joy, and one more round of sweets.",
                ],
            },
            {
                "key": "friends",
                "h2": "Happy Diwali Quotes for Friends",
                "lines": [
                    "Happy Diwali, my friend. May your life sparkle brighter than the best festive lights.",
                    "Here is to laughter, late replies, shared sweets, and a friendship that still glows.",
                    "May your Diwali be bright, your snacks endless, and your worries tiny.",
                    "Wishing you a Diwali that feels as joyful as our best conversations.",
                    "May this year bring you growth, peace, and the kind of happiness you do not have to explain.",
                    "Happy Deepavali. May every dream you light this year find its way forward.",
                    "Friends make festivals louder, warmer, and far more memorable.",
                    "May the glow of Diwali stay with you long after the lamps fade.",
                    "Wishing you success without stress and celebration without chaos.",
                    "May your phone be full of good wishes and your heart full of calm.",
                    "Happy Diwali to the friend who turns ordinary days into memories.",
                    "May light, luck, and love follow you everywhere this festive season.",
                ],
            },
            {
                "key": "whatsapp",
                "h2": "Diwali Wishes and Quotes for WhatsApp",
                "lines": [
                    "Happy Diwali 2026. May your home be bright and your heart be peaceful.",
                    "Wishing you joy, prosperity, and a festival full of beautiful light.",
                    "May this Diwali bring health, happiness, and a fresh start.",
                    "Sending warm Diwali wishes to you and your family.",
                    "May every diya you light bring one blessing closer.",
                    "Happy Deepavali. Stay blessed, stay smiling, stay surrounded by love.",
                    "May your Diwali be simple, sweet, and full of good news.",
                    "Wishing you a bright festival and an even brighter year ahead.",
                    "May light remove every worry and bring calm into your home.",
                    "Happy Diwali. May hope glow in every corner of your life.",
                    "Let this message carry love, blessings, and a little festive sparkle.",
                    "May your celebrations be safe, joyful, and full of togetherness.",
                ],
            },
            {
                "key": "deepavali",
                "h2": "Happy Deepavali Quotes and Wishes",
                "lines": [
                    "Happy Deepavali. May light guide your choices and love fill your home.",
                    "May the festival of lights bring peace to your mind and strength to your heart.",
                    "Wishing you a Deepavali filled with blessings, sweets, and meaningful moments.",
                    "May every lamp remind you that even small hope can brighten a dark day.",
                    "Happy Deepavali 2026. May prosperity arrive with humility and happiness arrive with ease.",
                    "Let this Deepavali be a reminder to forgive, refresh, and begin again.",
                    "May your home glow with diyas and your life glow with kindness.",
                    "Wishing you success that feels steady and joy that feels real.",
                    "May the light of Deepavali stay with you through the year.",
                    "Happy Deepavali to you and everyone who makes your life brighter.",
                    "May blessings enter gently and stay generously.",
                    "May your celebration be safe, soulful, and full of gratitude.",
                ],
            },
            {
                "key": "inspirational",
                "h2": "Inspirational Diwali Quotes",
                "lines": [
                    "A diya does not remove every shadow, but it proves light can begin anywhere.",
                    "Diwali reminds us that renewal starts with one honest flame.",
                    "Let the light you seek also become the light you share.",
                    "Goodness does not need noise. Sometimes it glows quietly and changes the room.",
                    "May this Diwali teach us to choose hope even when the path is not fully clear.",
                    "The brightest homes are not only decorated with lamps, they are filled with kindness.",
                    "Every Diwali is a chance to clean the heart as carefully as the home.",
                    "Light over darkness is not only a festival theme, it is a daily practice.",
                    "The flame of a diya is small, but its lesson is brave.",
                    "Let gratitude be the first lamp you light this Diwali.",
                    "Prosperity feels complete only when it is shared with love.",
                    "May your courage glow brighter than your fear.",
                ],
            },
            {
                "key": "beautiful",
                "h2": "Beautiful Happy Diwali Wishes",
                "lines": [
                    "May your Diwali look beautiful, feel peaceful, and stay memorable.",
                    "Wishing you a festival wrapped in soft light, sweet moments, and loving blessings.",
                    "May your home bloom with rangoli colours and your heart bloom with gratitude.",
                    "Happy Diwali 2026. May every lamp bring a little more calm into your life.",
                    "May the glow of diyas make every ordinary corner feel special.",
                    "Wishing you a celebration that feels elegant, warm, and close to the heart.",
                    "May light find you, bless you, and stay with you.",
                    "Happy Deepavali. May your days ahead be as graceful as the first diya of the evening.",
                    "May the festival bring beauty to your home and softness to your thoughts.",
                    "Wishing you bright beginnings, gentle endings, and a heart full of hope.",
                    "May your Diwali memories be golden, joyful, and kind.",
                    "May every wish you send return to you as a blessing.",
                ],
            },
            {
                "key": "instagram",
                "h2": "Diwali Captions for Instagram",
                "lines": [
                    "Diyas, smiles, sweets, and a little festive magic.",
                    "Current mood: glowing from the inside out.",
                    "Diwali lights and grateful hearts.",
                    "A little sparkle, a lot of blessings.",
                    "Festival of lights, season of soft joy.",
                    "Rangoli colours, diya glow, family love.",
                    "Bright night, warm heart, happy Diwali.",
                    "Wearing light, sharing love, choosing joy.",
                    "May the glow stay longer than the celebration.",
                    "Deepavali moments worth saving.",
                    "Light outside, peace inside.",
                    "This Diwali, keeping it graceful and bright.",
                ],
            },
            {
                "key": "formal",
                "h2": "Formal Diwali Wishes for Colleagues and Clients",
                "lines": [
                    "Wishing you and your family a happy Diwali filled with prosperity, health, and peace.",
                    "May this festival of lights bring success, harmony, and new opportunities.",
                    "Happy Diwali 2026. Wishing you a bright festive season and a productive year ahead.",
                    "May your celebrations be joyful and your work ahead be rewarding.",
                    "Sending warm Diwali wishes to you and your loved ones.",
                    "May light, goodwill, and growth guide the coming year.",
                    "Wishing your team a safe, happy, and prosperous Diwali.",
                    "May this Diwali bring clarity, confidence, and shared success.",
                    "Happy Deepavali. Thank you for your trust and association.",
                    "Wishing you peace at home and progress in all your efforts.",
                    "May the festival bring brightness to your personal and professional life.",
                    "Warm Diwali greetings and best wishes for the year ahead.",
                ],
            },
            {
                "key": "gift",
                "h2": "Diwali Gift Ideas to Pair with Wishes",
                "lines": [
                    "A small keepsake can make a Diwali wish feel more personal.",
                    "For a sister or friend, earrings work well because they feel festive yet wearable.",
                    "For a mother, aunt, or mentor, a pendant can feel graceful and thoughtful.",
                    "For someone who loves traditional dressing, a bangle can match the festive mood.",
                    "For someone who prefers everyday style, a bracelet or ring can feel easier to wear.",
                    "Keep the note simple and avoid making the gift about price.",
                    "Write one sincere line about light, blessings, or gratitude.",
                    "Choose jewellery that suits the person's real routine, not only the festival photo.",
                    "A gift feels better when the message says why you chose it.",
                    "If you are unsure, pick a classic design with a soft festive detail.",
                    "The best Diwali gift supports the wish instead of replacing it.",
                    "Let the emotion lead, and let the keepsake quietly hold the memory.",
                ],
            },
            {
                "key": "how_to",
                "h2": "How to Choose the Right Diwali Message",
                "lines": [
                    "For parents and elders, choose respectful blessings and gratitude.",
                    "For siblings, keep the tone warm, playful, and personal.",
                    "For friends, use a short wish with personality.",
                    "For colleagues, keep the message polished and inclusive.",
                    "For Instagram, choose a caption that matches the photo mood.",
                    "For WhatsApp groups, keep it short enough to read quickly.",
                    "For greeting cards, add one memory or one personal blessing.",
                    "For Deepavali wishes, use language that feels traditional and sincere.",
                    "Avoid sending the same line to everyone if the relationship is close.",
                    "A good Diwali message should sound like you, only brighter.",
                ],
            },
        ],
        "faqs": [
            ["What are the best Diwali wishes and quotes for 2026?", "The best Diwali wishes and quotes for 2026 are short, warm, and easy to share. Mention light, blessings, family, prosperity, hope, and fresh beginnings. For close family, add a personal line. For WhatsApp, keep it crisp. For Instagram, make it visual and caption friendly."],
            ["How do I say Happy Diwali professionally?", "Say: Wishing you and your family a happy Diwali filled with prosperity, peace, and good health. For clients or colleagues, keep the message polished, inclusive, and free from jokes. Add a short note of gratitude if the relationship is work related."],
            ["What is a short Diwali quote for WhatsApp?", "A simple WhatsApp line is: May every diya bring hope, joy, and peace into your life. You can also write: Happy Diwali 2026. May your home glow with love and your year ahead shine with blessings."],
            ["What are beautiful Happy Deepavali quotes?", "Beautiful Happy Deepavali quotes usually focus on light, kindness, gratitude, and renewal. Try: Let the light you seek also become the light you share. Or write: May this Deepavali bring peace to your heart and warmth to your home."],
            ["Can I use Diwali wishes and quotes for Instagram captions?", "Yes. Keep Instagram captions short, visual, and mood based. Lines like Diwali lights and grateful hearts, or Light outside, peace inside, work well with festive outfits, diyas, rangoli, and family photos."],
            ["What should I write with a Diwali jewellery gift?", "Write a message that connects the gift to light and blessings. For example: May this little keepsake remind you of the warmth and brightness you bring into our lives. Keep it sincere, personal, and free from price talk."],
            ["When is Diwali 2026?", "Diwali 2026 is observed on Sunday, 8 November 2026. Use 2026 in wishes, captions, greeting cards, image alts, and festival posts for this edition."],
        ],
    }

    config = {
        "rank": "Week3-4 Rank 1",
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-diwaliwishesquotes",
        "occasion_year": "Diwali 2026",
        "carousel_alt_prefix": "diwali wishes and quotes 2026 gift idea",
        "gift_h2": "Diwali Jewellery Gift Ideas to Send with Wishes",
        "gift_blurb": "If your Diwali wish is going with a gift, keep the emotion soft and the piece wearable. These BlueStone picks suit festive notes without turning the article into a catalogue.",
        "conclusion_html": "Diwali wishes and quotes do not need to be complicated. Choose a line that fits the relationship, add the 2026 festival warmth, and let your message carry light in a way that feels genuinely yours.",
        "schema_keywords": [
            "diwali wishes and quotes",
            "happy diwali wishes",
            "happy deepavali quotes",
            "deepavali wishes quotes",
            "happy diwali quotes",
            "inspirational diwali quotes",
            "happy diwali wishes quotes",
        ],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(product_rows, "The Teshvarya Pendant", "ProductImages/seo images/Pendants/The Teshvarya Pendant.png"),
            product(product_rows, "The Channing Bangle", "ProductImages/seo images/Bangles/The Channing Bangle.png"),
            product(product_rows, "The Aleena Huggie Earrings", "ProductImages/seo images/Earrings/The Aleena Huggie Earrings.png"),
            product(product_rows, "The Haily Ring", "ProductImages/seo images/Rings/The Haily Ring.png"),
            product(product_rows, "The Rapett Evil Eye Charm Necklace", "ProductImages/seo images/Necklaces/The Rapett Evil Eye Charm Necklace.png"),
            product(product_rows, "The Pervinca Charm Holder Bracelet", "ProductImages/seo images/Bracelet/The Pervinca Charm Holder Bracelet.png"),
        ],
        "flatlay_insert_h2": "Happy Deepavali Quotes and Wishes",
        "lifestyle_insert_h2": "Diwali Gift Ideas to Pair with Wishes",
        "more_reads_html": "Read more festive guides in <a href=\"https://blog.bluestone.com/why-we-celebrate-diwali-2026/\">why we celebrate Diwali 2026</a>, <a href=\"https://blog.bluestone.com/diwali-poster-2026/\">Diwali poster 2026</a>, <a href=\"https://blog.bluestone.com/advance-happy-diwali-2026/\">advance happy Diwali 2026</a>, and <a href=\"https://blog.bluestone.com/slogan-on-diwali-2026/\">slogan on Diwali 2026</a>.",
        "how_to_html": "For date context, Diwali 2026 is observed on Sunday, 8 November 2026. For a short festival background, you can read <a href=\"https://www.britannica.com/topic/Diwali-Hindu-festival\">Britannica on Diwali</a>. Send wishes early for relatives in different time zones and keep card text personal.",
        "faq_h2": "Frequently Asked Questions about Diwali Wishes and Quotes",
        "min_lines": 100,
    }

    hero = consolidated(detail_rows, "The Teshvarya Pendant")
    flatlay = consolidated(detail_rows, "The Channing Bangle")
    lifestyle = consolidated(detail_rows, "The Aleena Huggie Earrings")

    prompts = {
        "rank": "Week3-4 Rank 1",
        "slug": "diwali-wishes-and-quotes-2026",
        "primary_kw": "diwali wishes and quotes",
        "output_prefix": PREFIX,
        "caption_occasion": "Diwali wishes and quotes",
        "caption_year": "2026",
        "flatlay_setting": "festive-mantel",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/diwali-wishes-and-quotes-hero-2026.webp",
            "flatlay": "output/magnific_generated/diwali-wishes-and-quotes-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/diwali-wishes-and-quotes-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "diwali wishes and quotes 2026 hero The Teshvarya Pendant",
            "flatlay": "diwali wishes and quotes 2026 flatlay The Channing Bangle",
            "lifestyle": "diwali wishes and quotes 2026 lifestyle The Aleena Huggie Earrings",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                **hero,
                "alt": "diwali wishes and quotes 2026 hero with The Teshvarya Pendant",
                "caption": "Diwali wishes and quotes 2026 vibe: The Teshvarya Pendant",
                "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]},
                "cdn": [
                    "https://kinclimg6.bluestone.com/giproduct/BISW1080P32_RAA18DIG6XXXXXXXX_ABCD00-BP-PICS-00000-1024-116053.png",
                    "https://kinclimg6.bluestone.com/giproduct/BISW1080P32_RAA18DIG6XXXXXXXX_ABCD00-PICS-00004-1024-116053.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Teshvarya Pendant/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Teshvarya Pendant/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} "
                    "Diwali wishes and quotes 2026 hero, solo fair-skinned Indian adult woman seated near a warm living room window, holding a completely blank cream Diwali greeting card beside a small diya and marigold petals. Full head, full face, both eyes, complete smile, neck, pendant, upper body, blank card, and diya visible with safe margins. Exactly one person only. 85mm DSLR look, natural skin texture, warm daylight mixed with soft diya glow, 16:9.\n\n"
                    "The woman physically wears The Teshvarya Pendant from @img1 body_image and @img2 design only on her neck. GENDER LOCK: Female product on adult woman only. "
                    f"Product dimensions from PDP: {hero['size_prompt_note']}. These are product dimensions, not face-size instructions. "
                    "Keep pendant size on the neck like @img1 body_image worn scale: subtle real PDP size, not enlarged. Use @img2 only for jewellery design.\n\n"
                    "Replicate the rose gold pendant exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery object in the entire image. Bare ears, bare wrists, bare fingers, no earrings, no rings, no bracelets, no bangles, no watch, no extra necklace. No readable text anywhere. Any card or gift tag must be completely blank.\n\n"
                    "Avoid: visible earrings, visible rings, cropped face, cropped head, readable text, letters, numbers, logo, man wearer, child, second person, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow."
                ),
            },
            "flatlay": {
                **flatlay,
                "alt": "diwali wishes and quotes 2026 flatlay with The Channing Bangle",
                "caption": "Diwali wishes and quotes 2026 keepsake: The Channing Bangle",
                "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]},
                "cdn": [
                    "https://kinclimg7.bluestone.com/giproduct/BIPS0003O06_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-21972.png",
                    "https://kinclimg0.bluestone.com/giproduct/BIPS0003O06_YAA18DIG6XXXXXXXX_ABCD00-PICS-00001-1024-21972.png",
                    "https://kinclimg7.bluestone.com/giproduct/BIPS0003O06_YAA18DIG6XXXXXXXX_ABCD00-PICS-00002-1024-21972.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Bangles/The Channing Bangle/0_primary.png",
                    "ProductImages/raw/Bangles/The Channing Bangle/2_front.png",
                    "ProductImages/raw/Bangles/The Channing Bangle/3_side_1.png",
                ],
                "ref_roles": ["primary", "front", "side"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\n"
                    "Diwali wishes and quotes 2026 top-down flatlay. Flatlay setting ID: festive-mantel. Surface and props: warm wooden festive mantel, small clay diya, marigold petals, silk ribbon, and a completely blank cream gift card. "
                    "The identical Channing Bangle from @img1, @img2 and @img3 rests naturally on the surface at true PDP scale. "
                    f"Product dimensions from PDP: {flatlay['size_prompt_note']}. These are product dimensions, not face-size instructions. Do not enlarge for visibility. "
                    "Full bangle visible, yellow gold bangle with refined diamond detail, 100 percent identical design, zero distortion, HD metal and stone detail.\n\n"
                    "Props stay secondary. No people, no hands, no logos, no readable text, no letters, no numbers, no other jewellery.\n\n"
                    "Avoid: hands, people, floating overlays, cutouts, incorrect bangle design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI."
                ),
            },
            "lifestyle": {
                **lifestyle,
                "alt": "diwali wishes and quotes 2026 lifestyle with The Aleena Huggie Earrings",
                "caption": "Diwali wishes and quotes 2026 vibe: The Aleena Huggie Earrings",
                "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]},
                "cdn": [
                    "https://kinclimg7.bluestone.com/giproduct/BIIP0279S08_RAA18DIG6SYRUXXXX_ABCD00-BP-PICS-00000-1024-79495.png",
                    "https://kinclimg7.bluestone.com/giproduct/BIIP0279S08_RAA18DIG6SYRUXXXX_ABCD00-PICS-00004-1024-79495.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Earrings/The Aleena Huggie Earrings/1_body_portrait.png",
                    "ProductImages/raw/Earrings/The Aleena Huggie Earrings/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} "
                    "Diwali wishes and quotes 2026 lifestyle, solo fair-skinned Indian adult woman arranging diyas and marigold petals near a completely blank greeting card in a warm modern Indian home. Full head, full face, both ears, both eyes, complete smile, upper body, hands, diyas, and blank card visible with safe margins. Exactly one person only. 85mm DSLR look, natural skin texture, soft diya glow, realistic shadows, 16:9.\n\n"
                    "The woman physically wears The Aleena Huggie Earrings from @img1 body_image and @img2 design only on her ears. GENDER LOCK: Female product on adult woman only. "
                    f"Product dimensions from PDP: {lifestyle['size_prompt_note']}. These are product dimensions, not face-size instructions. "
                    "Keep earrings size on the ears like @img1 body_image worn scale: subtle real PDP size, not enlarged. Use @img2 only for jewellery design.\n\n"
                    "Replicate the rose gold huggie earrings exactly, 100 percent identical to refs, zero distortion, HD metal detail. These earrings are the single and only jewellery object in the entire image. Bare neck, bare wrists, bare fingers, no necklace, no pendant, no bracelet, no bangle, no ring, no watch, no other earrings. No readable text anywhere. Any card or gift tag must be completely blank.\n\n"
                    "Avoid: extra earrings, visible rings, cropped face, cropped head, readable text, letters, numbers, logo, man wearer, child, second person, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow."
                ),
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Week 3-4 Rank 1

Article: Diwali Wishes and Quotes 2026
Status: Draft assets prepared
Date: 2026-07-27

## A. Intent and Brief
- [x] Primary keyword: diwali wishes and quotes
- [x] Sheet Optimize treated as New
- [x] Fresh slug: diwali-wishes-and-quotes-2026
- [x] 2026 year lock used
- [x] Supporting keywords mapped to H2 and FAQ

## B. SEO Structure
- [x] Title/H1 intent prepared
- [x] Yoast title under 60 chars
- [x] Meta description 150 to 160 chars
- [x] Primary keyword in intro and hero alt

## C. Content and Readability
- [x] Direct answer and TL;DR
- [x] 100+ wish, quote, caption, and message lines
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
    write_json(f"output/publish_configs/week34_rank1.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")
    print(f"wrote {PREFIX} assets")


if __name__ == "__main__":
    main()
