#!/usr/bin/env python3
"""Build Rank 96 Mother Day wish in Hindi assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank96_MotherDayHindi"
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
        f"Mother Day wish in Hindi 2026 {scene}. Solo fair-skinned Indian adult mother, graceful warm expression, "
        "modern Indian home, blank cream greeting card nearby, soft flowers, full head, full face, both eyes, complete smile, "
        "upper body and jewellery area visible with safe margins. Exactly one person in the entire image. Camera pulled back "
        "medium shot, 85mm DSLR look, natural skin texture, warm window light, realistic shadows, 16:9.\n\n"
        f"The woman physically wears {slot['name']} from @img1 body_image and @img2 design. "
        "GENDER LOCK: Female product on adult woman only. "
        f"Product dimensions from PDP: {slot['size_prompt_note']}. "
        f"Keep {scale_phrase} like @img1 body_image worn scale: subtle real product size, not enlarged. "
        "Use @img2 only for jewellery design.\n\n"
        f"Replicate {product_phrase} exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. "
        f"This is the single and only jewellery in the image. {extra_rules} No readable text anywhere.\n\n"
        "Avoid: cropped face, cropped head, readable text, man wearer, child, second person, extra jewellery, "
        "floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, "
        "heavily tanned skin, illustration, CGI, HDR glow."
    )


def main() -> None:
    csv_rows = rows_by_name("Seo Products - final products (1).csv")
    detail_rows = rows_by_name("KnowledgeBase/Product/Seo Products - consolidated.csv")

    sections = {
        "meta": {
            "title": "Mother Day Wish in Hindi 2026: Maa Ke Liye Wishes",
            "slug": "mother-day-wish-in-hindi-2026",
            "meta_desc": "Mother Day Wish in Hindi 2026 with Maa ke liye wishes, Happy Mothers Day quotes in Hindi, shayari, status, captions, and heartfelt lines for mom cards.",
            "focus_kw": "mother day wish in hindi",
            "yoast_title": "Mother Day Wish in Hindi 2026: Maa Ke Liye Wishes",
        },
        "intro": [
            "Mother day wish in hindi लिखते समय सबसे जरूरी बात भावनाओं की सच्चाई है. मां के लिए मैसेज छोटा हो सकता है, लेकिन उसमें आभार, प्यार और सम्मान साफ दिखना चाहिए.",
            "TL;DR: मां के लिए एक प्यारा Hindi wish चुनें, उसमें अपना नाम या याद जोड़ें, और कार्ड, WhatsApp, caption या shayari के हिसाब से tone रखें.",
        ],
        "sections": [
            {"key": "best", "h2": "Mother Day Wish in Hindi", "lines": [
                "मां, आपके बिना मेरी दुनिया अधूरी है. Happy Mother Day.",
                "मां, आपका प्यार मेरी सबसे बड़ी ताकत है.",
                "आपकी दुआओं ने मुझे हमेशा संभाला है, मां.",
                "मां, आप मेरी पहली दोस्त और सबसे बड़ी प्रेरणा हैं.",
                "आपकी मुस्कान मेरे हर दिन को बेहतर बना देती है.",
                "मां, आपका आशीर्वाद मेरे लिए सबसे बड़ा उपहार है.",
                "आपके प्यार जैसा सुकून कहीं नहीं मिलता.",
                "मां, आपने मुझे जीना और मुस्कुराना सिखाया.",
                "मेरी हर सफलता में आपकी मेहनत छुपी है.",
                "Happy Mother Day, मां. आप मेरी दुनिया हैं.",
            ]},
            {"key": "quotes", "h2": "Happy Mothers Day Quotes in Hindi", "lines": [
                "मां वह रोशनी है जो अंधेरे समय में भी रास्ता दिखाती है.",
                "मां का प्यार शब्दों से नहीं, एहसासों से समझ आता है.",
                "जिस घर में मां की हंसी हो, वहां खुशियां खुद रास्ता ढूंढ लेती हैं.",
                "मां की दुआ हर मुश्किल को आसान बना देती है.",
                "मां का दिल बच्चों की हर खामोशी पढ़ लेता है.",
                "दुनिया बदल सकती है, मां का प्यार नहीं.",
                "मां की गोद सबसे सुरक्षित जगह होती है.",
                "मां वह रिश्ता है जिसमें शिकायत कम और अपनापन ज्यादा होता है.",
                "मां का आशीर्वाद जीवन की सबसे सुंदर पूंजी है.",
                "मां के बिना कोई भी खुशी पूरी नहीं लगती.",
            ]},
            {"key": "shayari", "h2": "Happy Mothers Day Shayari", "lines": [
                "तेरी दुआओं से ही मेरी राह आसान होती है, मां.",
                "तेरे आंचल में ही मेरी हर थकान सो जाती है.",
                "दुनिया ने जब भी परखा, मां की दुआ साथ आई.",
                "मां, तेरी ममता ने हर डर को छोटा कर दिया.",
                "तेरी मुस्कान से मेरा हर दिन त्योहार बन जाता है.",
                "मां, तेरे बिना मेरी कोई पहचान पूरी नहीं.",
                "तेरी बातें आज भी मेरे फैसलों को संभालती हैं.",
                "मां, तेरे प्यार का कर्ज कभी चुकाया नहीं जा सकता.",
                "तेरी गोद में सारी दुनिया की शांति मिलती है.",
                "मां, तू है तो हर मुश्किल में भी उम्मीद है.",
            ]},
            {"key": "short", "h2": "Short Mother Day Wishes in Hindi", "lines": [
                "मां, आप सबसे खास हैं.",
                "मां, आपको ढेर सारा प्यार.",
                "Happy Mother Day, मेरी प्यारी मां.",
                "आपकी दुआ मेरी ताकत है.",
                "मां, आप मेरी दुनिया हैं.",
                "आपका प्यार मेरा सुकून है.",
                "मां, हमेशा मुस्कुराती रहिए.",
                "आपके बिना सब अधूरा है.",
                "मां, दिल से धन्यवाद.",
                "आप मेरी पहली खुशी हैं.",
            ]},
            {"key": "emotional", "h2": "Heart Touching Mothers Day Wishes in Hindi", "lines": [
                "मां, जब मैं शब्दों में कमजोर पड़ जाता हूं, तब भी आपका प्यार मुझे समझ लेता है.",
                "आपने मेरी हर गलती को सीख में बदल दिया.",
                "मेरी छोटी खुशियों के लिए आपने अपनी बड़ी इच्छाएं छोड़ीं.",
                "मां, आपकी चुप दुआओं ने मुझे कई बार टूटने से बचाया.",
                "मैं आज जो भी हूं, उसमें आपका धैर्य और त्याग है.",
                "आपने मुझे सिर्फ प्यार नहीं दिया, आपने मुझे हिम्मत भी दी.",
                "मां, आपके हाथों की गर्माहट आज भी मेरा सबसे बड़ा सुकून है.",
                "काश मैं आपको उतनी खुशी दे पाऊं जितनी आपने मुझे दी है.",
                "आप मेरी जिंदगी की सबसे सुंदर blessing हैं.",
                "Happy Mother Day, मां. आपका प्यार मेरी उम्र भर की पूंजी है.",
            ]},
            {"key": "from_daughter", "h2": "Mother Day Wish in Hindi from Daughter", "lines": [
                "मां, आपकी बेटी होने पर मुझे गर्व है.",
                "आपने मुझे मजबूत होना सिखाया, लेकिन दिल से नरम रहना भी सिखाया.",
                "मां, आपकी बातें मेरी जिंदगी की सबसे जरूरी सीख हैं.",
                "आपकी तरह बन पाना आसान नहीं, लेकिन मैं कोशिश करती रहूंगी.",
                "मेरी हर मुस्कान में आपकी परवरिश दिखती है.",
                "आपने मुझे अपनी आवाज, अपना साहस और अपना प्यार दिया.",
                "मां, आप मेरी पहली role model हैं.",
                "जब भी मैं डरती हूं, आपकी हिम्मत याद आती है.",
                "आपकी बेटी हमेशा आपका आशीर्वाद चाहती है.",
                "Happy Mother Day, मां. आपसे बेहतर कोई नहीं.",
            ]},
            {"key": "from_son", "h2": "Mother Day Wish in Hindi from Son", "lines": [
                "मां, आपका बेटा हमेशा आपकी दुआओं का आभारी रहेगा.",
                "आपने मुझे जिम्मेदारी, सम्मान और प्यार का मतलब सिखाया.",
                "मेरी हर उपलब्धि में आपका विश्वास शामिल है.",
                "मां, आपने मुझे गिरकर उठना सिखाया.",
                "आपकी चिंता कभी कभी डांट लगती है, लेकिन उसमें सबसे गहरा प्यार होता है.",
                "मैं आपको रोज नहीं कह पाता, पर आप मेरी सबसे बड़ी ताकत हैं.",
                "मां, आपकी आंखों की खुशी मेरे लिए सबसे बड़ी जीत है.",
                "आपका आशीर्वाद मेरे हर कदम के साथ रहे.",
                "Happy Mother Day, मां. आपका बेटा आपसे बहुत प्यार करता है.",
                "आपका प्यार मेरी जिंदगी का सबसे भरोसेमंद सहारा है.",
            ]},
            {"key": "status", "h2": "Mothers Day Status in Hindi", "lines": [
                "मां की मुस्कान से बड़ा कोई celebration नहीं.",
                "मेरी जिंदगी की सबसे प्यारी blessing, मेरी मां.",
                "मां का प्यार हर दिन नया साहस देता है.",
                "Happy Mother Day to my forever home.",
                "मां, आपके बिना कुछ भी पूरा नहीं.",
                "मेरी पहली teacher, मेरी पहली friend, मेरी मां.",
                "मां की दुआ में दुनिया की सबसे बड़ी शक्ति है.",
                "आज का दिन मां के नाम.",
                "मां, आप मेरी हर खुशी की वजह हैं.",
                "Love you maa, always and forever.",
            ]},
            {"key": "captions", "h2": "Mother Day Captions in Hindi", "lines": [
                "मां के साथ हर फोटो blessing बन जाती है.",
                "मेरी smile की असली वजह.",
                "मां, मेरी जिंदगी की सबसे सुंदर कहानी.",
                "Home is wherever maa is.",
                "मां के हाथों में दुनिया का सबसे प्यारा सुकून.",
                "Forever grateful for you, maa.",
                "मेरे दिल की सबसे प्यारी जगह.",
                "मां, आपकी बेटी या बेटा हमेशा आपका रहेगा.",
                "Aaj ka pyaar sirf maa ke naam.",
                "Happy Mother Day to my safest place.",
            ]},
            {"key": "card", "h2": "Mother Day Card Message in Hindi", "lines": [
                "मां, इस कार्ड में शब्द कम हैं, लेकिन प्यार बहुत सारा है.",
                "आपकी हर दुआ, हर सीख और हर त्याग के लिए धन्यवाद.",
                "मैं हमेशा आपकी मेहनत को याद रखूंगा.",
                "मां, आपने मुझे जिंदगी को प्यार से देखना सिखाया.",
                "आपके बिना मेरी कहानी अधूरी है.",
                "यह छोटा सा message आपके बड़े प्यार के लिए है.",
                "मां, आप हमेशा healthy, happy और peaceful रहें.",
                "मैं चाहता हूं कि इस साल आपको उतनी खुशी मिले जितनी आप सबको देती हैं.",
                "आपके आशीर्वाद से ही मेरा हर दिन बेहतर है.",
                "Happy Mother Day, मां. दिल से धन्यवाद.",
            ]},
            {"key": "gift", "h2": "Mother Day Gift Ideas with Wishes in Hindi", "lines": [
                "एक प्यारा wish और thoughtful gift साथ में ज्यादा यादगार लगते हैं.",
                "Pendant मां के लिए soft और graceful gift हो सकता है.",
                "Bracelet रोज पहनने वाली मां के लिए सुंदर keepsake बन सकता है.",
                "Earrings उन मांओं के लिए अच्छे हैं जिन्हें simple festive style पसंद है.",
                "Gift के साथ handwritten Hindi note जरूर रखें.",
                "Message में price नहीं, emotion लिखें.",
                "मां के daily style के हिसाब से design चुनें.",
                "छोटा gift भी बड़ा लग सकता है अगर wish सच्चा हो.",
                "एक line लिखें: मां, यह आपके प्यार की छोटी सी याद है.",
                "सबसे अच्छा gift वही है जो मां को अपनेपन का एहसास दे.",
            ]},
        ],
        "faqs": [
            ["Mother day wish in Hindi कैसे लिखें?", "Mother day wish in Hindi लिखते समय मां के लिए प्यार, आभार और एक personal memory जोड़ें. Message छोटा हो सकता है, बस सच्चा होना चाहिए."],
            ["Happy Mothers Day quotes in Hindi में क्या लिखें?", "आप मां की दुआ, त्याग, ममता, मुस्कान और आशीर्वाद पर short quote लिख सकते हैं. Simple Hindi words सबसे ज्यादा emotional लगते हैं."],
            ["मां के लिए short wish क्या हो सकता है?", "मां, आप मेरी सबसे बड़ी ताकत हैं. Happy Mother Day. यह short और heartfelt wish card या WhatsApp दोनों के लिए अच्छा है."],
            ["Daughter की तरफ से Mother Day wish क्या लिखें?", "मां, आपकी बेटी होने पर मुझे गर्व है. आपने मुझे प्यार, हिम्मत और self respect सिखाया. Happy Mother Day."],
            ["Son की तरफ से Mother Day wish क्या लिखें?", "मां, आपका बेटा आपकी दुआओं और प्यार के लिए हमेशा आभारी रहेगा. Happy Mother Day, love you maa."],
            ["Mother Day gift के साथ Hindi message कैसे लिखें?", "Gift के साथ एक simple line लिखें: मां, यह छोटा सा gift आपके बड़े प्यार और आशीर्वाद के लिए मेरी तरफ से धन्यवाद है."],
        ],
    }

    config = {
        "rank": 96,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-motherhindi",
        "occasion_year": "Mother Day Wish in Hindi 2026",
        "carousel_alt_prefix": "mother day wish in hindi 2026 gift idea",
        "gift_h2": "BlueStone Gift Ideas for Maa",
        "gift_blurb": "Mother Day wish in Hindi feels even warmer when it comes with a keepsake chosen around Maa's daily style. These approved BlueStone designs suit graceful gifting without mentioning prices.",
        "conclusion_html": "Mother day wish in hindi tabhi yaad rehta hai jab woh copied nahi, dil se likha hua lage. Apni maa ke liye ek simple line chunen, ek personal memory add karen, aur pyaar ke saath bhej den.",
        "schema_keywords": ["mother day wish in hindi", "happy mothers day quotes in hindi", "happy mothers day shayari", "happy mothers day wishes in hindi", "mother day card message in hindi"],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(csv_rows, "The Teshvarya Pendant", "ProductImages/seo images/Pendants/The Teshvarya Pendant.png"),
            product(csv_rows, "The Pervinca Charm Holder Bracelet", "ProductImages/seo images/Bracelet/The Pervinca Charm Holder Bracelet.png"),
            product(csv_rows, "The Aleena Huggie Earrings", "ProductImages/seo images/Earrings/The Aleena Huggie Earrings.png"),
            product(csv_rows, "The Valeria Rose Pendant", "ProductImages/seo images/Pendants/The Valeria Rose Pendant.png"),
            product(csv_rows, "The Malocchio Charm Holder Bracelet", "ProductImages/seo images/Bracelet/The Malocchio Charm Holder Bracelet.png"),
            product(csv_rows, "The Ursa Hoop Earrings", "ProductImages/seo images/Earrings/The Ursa Hoop Earrings.png"),
        ],
        "flatlay_insert_h2": "Happy Mothers Day Shayari",
        "lifestyle_insert_h2": "Mother Day Gift Ideas with Wishes in Hindi",
        "more_reads_html": "Read more heartfelt guides in <a href=\"https://blog.bluestone.com/mother-daughter-quotes-2026/\">mother daughter quotes 2026</a>, <a href=\"https://blog.bluestone.com/raksha-bandhan-gifts-for-brother-2026/\">Raksha Bandhan gifts for brother 2026</a>, <a href=\"https://blog.bluestone.com/new-year-wishes-for-love-2026/\">New Year wishes for love 2026</a>, and <a href=\"https://blog.bluestone.com/thank-you-note-to-teacher-2026/\">thank you note to teacher 2026</a>.",
        "how_to_html": "Hindi wish bhejte waqt pehle relation ka tone choose karen. Daughter ya son ke message mein ek memory add karen, WhatsApp ke liye short line rakhen, aur card ke liye thoda emotional note likhen.",
        "faq_h2": "Frequently Asked Questions about Mother Day Wish in Hindi",
        "min_lines": 100,
    }

    hero = consolidated(detail_rows, "The Teshvarya Pendant")
    flatlay = consolidated(detail_rows, "The Pervinca Charm Holder Bracelet")
    lifestyle = consolidated(detail_rows, "The Aleena Huggie Earrings")

    prompts = {
        "rank": 96,
        "slug": "mother-day-wish-in-hindi-2026",
        "primary_kw": "mother day wish in hindi",
        "output_prefix": PREFIX,
        "caption_occasion": "Mother Day wish in Hindi",
        "caption_year": "2026",
        "flatlay_setting": "marble-vanity",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/mother-day-wish-in-hindi-hero-2026.webp",
            "flatlay": "output/magnific_generated/mother-day-wish-in-hindi-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/mother-day-wish-in-hindi-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "mother day wish in hindi 2026 hero The Teshvarya Pendant",
            "flatlay": "mother day wish in hindi 2026 flatlay The Pervinca Charm Holder Bracelet",
            "lifestyle": "mother day wish in hindi 2026 lifestyle The Aleena Huggie Earrings",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                **hero,
                "alt": "mother day wish in hindi 2026 hero with The Teshvarya Pendant",
                "caption": "Mother Day wish in Hindi 2026 vibe: The Teshvarya Pendant",
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
                "prompt": people_prompt(
                    hero,
                    "hero, sitting near a window reading a blank Mother's Day card with flowers on a table",
                    "the rose gold pendant",
                    "pendant size on the neck",
                    "Hands and wrists are hidden below frame or covered by the blank card; no earrings, no bracelet, no bangles, no rings, no watch, no extra necklace.",
                ),
            },
            "flatlay": {
                **flatlay,
                "alt": "mother day wish in hindi 2026 flatlay with The Pervinca Charm Holder Bracelet",
                "caption": "Mother Day wish in Hindi 2026 keepsake: The Pervinca Charm Holder Bracelet",
                "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]},
                "cdn": [
                    "https://kinclimg5.bluestone.com/giproduct/BIAV0865V24_YAA14AMETXXXXXXXX_ABCD00-PICS-00000-1024-71416.png",
                    "https://kinclimg5.bluestone.com/giproduct/BIAV0865V24_YAA14AMETXXXXXXXX_ABCD00-PICS-00001-1024-71416.png",
                    "https://kinclimg5.bluestone.com/giproduct/BIAV0865V24_YAA14AMETXXXXXXXX_ABCD00-PICS-00002-1024-71416.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Bracelets/The Pervinca Charm Holder Bracelet/0_primary.png",
                    "ProductImages/raw/Bracelets/The Pervinca Charm Holder Bracelet/2_side_1.png",
                    "ProductImages/raw/Bracelets/The Pervinca Charm Holder Bracelet/3_back.png",
                ],
                "ref_roles": ["primary", "angle", "back"],
                "prompt": (
                    f"Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\n"
                    "Mother Day wish in Hindi 2026 top-down flatlay. Flatlay setting ID: marble-vanity. "
                    "Surface and props: soft marble vanity, pale pink flowers, blank cream greeting card, fountain pen, tea cup, no readable text. "
                    "The identical Pervinca Charm Holder Bracelet from @img1, @img2 and @img3 rests naturally on the surface at true PDP scale. "
                    f"Product dimensions from PDP: {flatlay['size_prompt_note']}. Do not enlarge for visibility. "
                    "Full bracelet visible, yellow gold bracelet with amethyst charm holder detail, 100 percent identical design, zero distortion, HD metal and stone detail.\n\n"
                    "Props stay secondary. No people, no hands, no logos, no readable text.\n\n"
                    "Avoid: hands, people, floating overlays, cutouts, incorrect bracelet design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI."
                ),
            },
            "lifestyle": {
                **lifestyle,
                "alt": "mother day wish in hindi 2026 lifestyle with The Aleena Huggie Earrings",
                "caption": "Mother Day wish in Hindi 2026 vibe: The Aleena Huggie Earrings",
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
                "prompt": people_prompt(
                    lifestyle,
                    "lifestyle, smiling gently beside a small breakfast tray and blank Mother's Day card",
                    "the rose gold huggie earrings",
                    "earring size on the ears",
                    "Bare neck, hands and wrists hidden below frame; no necklace, no pendant, no bracelet, no bangles, no rings, no watch, no other earrings.",
                ),
            },
        },
    }

    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json(f"output/publish_configs/rank96.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    write_json(f"output/{PREFIX}_Checklist_v2.md", {"status": "drafted", "rank": 96, "slug": sections["meta"]["slug"]})
    print(f"wrote {PREFIX} sections/config/prompts")


if __name__ == "__main__":
    main()
