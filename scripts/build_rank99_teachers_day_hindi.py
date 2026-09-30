#!/usr/bin/env python3
"""Build Rank 99 Teachers Day wishes in Hindi article assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank99_TeachersDayHindi"
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
        f"Teachers Day wishes in Hindi 2026 {scene}. Solo fair-skinned Indian adult woman teacher, warm respectful expression, "
        "modern Indian classroom or study corner, blank cream card nearby, soft daylight, full head, full face, both eyes, "
        "complete smile, upper body and jewellery area visible with safe margins. Exactly one person in the entire image. "
        "Camera pulled back medium shot, 85mm DSLR look, natural skin texture, realistic shadows, 16:9.\n\n"
        f"The woman physically wears {slot['name']} from @img1 body_image and @img2 design. "
        "GENDER LOCK: Female product on adult woman only. "
        f"Product dimensions from PDP: {slot['size_prompt_note']}. "
        f"Keep {scale_phrase} like @img1 body_image worn scale: subtle real product size, not enlarged. "
        "Use @img2 only for jewellery design.\n\n"
        f"Replicate {product_phrase} exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. "
        f"This is the single and only jewellery in the image. {extra_rules} No readable text anywhere. "
        "Any card, notebook, blackboard, phone, or paper must be completely blank.\n\n"
        "Avoid: cropped face, cropped head, readable text, letters, numbers, logo, man wearer, child, student crowd, second person, "
        "extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, "
        "deep brown skin, heavily tanned skin, illustration, CGI, HDR glow."
    )


def main() -> None:
    csv_rows = rows_by_name("Seo Products - final products (1).csv")
    detail_rows = rows_by_name("KnowledgeBase/Product/Seo Products - consolidated.csv")

    sections = {
        "meta": {
            "title": "Teachers Day Wishes in Hindi 2026: शुभकामनाएं",
            "slug": "teachers-day-wishes-in-hindi-2026",
            "meta_desc": "Teachers Day wishes in Hindi 2026 with shikshak diwas ki hardik shubhkamnaye, short messages, quotes, captions, cards, and respectful teacher lines for school.",
            "focus_kw": "teachers day wishes in hindi",
            "yoast_title": "Teachers Day Wishes in Hindi 2026: शुभकामनाएं",
        },
        "intro": [
            "Teachers Day wishes in Hindi तब सबसे अच्छे लगते हैं जब उनमें सम्मान, सादगी और दिल से निकली हुई कृतज्ञता हो.",
            "TL;DR: अपने शिक्षक को छोटी, साफ और सम्मान भरी पंक्ति भेजें. कार्ड के लिए भावुक संदेश, WhatsApp के लिए छोटा wish, और caption के लिए सरल Hindi line सबसे अच्छा काम करती है.",
        ],
        "sections": [
            {"key": "best", "h2": "Teachers Day Wishes in Hindi", "lines": [
                "गुरु का आशीर्वाद जीवन की सबसे बड़ी सीख बन जाता है.",
                "शिक्षक दिवस की हार्दिक शुभकामनाएं, आपने हमें सीखने का साहस दिया.",
                "आपकी शिक्षा ने हमारी सोच और हमारा आत्मविश्वास दोनों बदले.",
                "जो रास्ता कठिन लगता था, आपने उसे समझ और धैर्य से आसान बनाया.",
                "आप जैसे शिक्षक जीवन में प्रेरणा बनकर आते हैं.",
                "आपकी हर सीख आज भी हमारे साथ चलती है.",
                "शिक्षक दिवस पर आपको सम्मान, आभार और ढेर सारी शुभकामनाएं.",
                "आपने किताबों से आगे जीवन को समझना सिखाया.",
                "आपकी मेहनत ने कई सपनों को दिशा दी.",
                "आपका आशीर्वाद हमेशा हमारे जीवन को रोशन करता रहे.",
            ]},
            {"key": "shikshak_diwas", "h2": "Shikshak Diwas Ki Hardik Shubhkamnaye", "lines": [
                "शिक्षक दिवस की हार्दिक शुभकामनाएं, आपका मार्गदर्शन हमारे लिए अनमोल है.",
                "शिक्षक दिवस पर आपको सादर प्रणाम और दिल से धन्यवाद.",
                "आपकी सीख ने हमें बेहतर इंसान बनने की प्रेरणा दी.",
                "आपका ज्ञान, धैर्य और स्नेह हमेशा याद रहेगा.",
                "शिक्षक दिवस की शुभकामनाएं, आपने हर सवाल का जवाब धैर्य से दिया.",
                "आपने हमें केवल पढ़ाया नहीं, जीवन में आगे बढ़ना भी सिखाया.",
                "आपका सम्मान शब्दों में पूरा नहीं हो सकता.",
                "शिक्षक दिवस पर आपका आभार, आपने हमें भरोसा करना सिखाया.",
                "आपकी प्रेरणा से हर मुश्किल आसान लगती है.",
                "शिक्षक दिवस की हार्दिक शुभकामनाएं, आप हमारे जीवन की खास रोशनी हैं.",
            ]},
            {"key": "short", "h2": "Short Teachers Day Wishes in Hindi", "lines": [
                "शिक्षक दिवस की शुभकामनाएं.",
                "गुरुजी, आपका धन्यवाद.",
                "आपका मार्गदर्शन अमूल्य है.",
                "आपसे सीखना सौभाग्य है.",
                "आप हमारे प्रेरणा स्रोत हैं.",
                "शिक्षक दिवस पर सादर प्रणाम.",
                "आपकी सीख हमेशा याद रहेगी.",
                "धन्यवाद, प्रिय शिक्षक.",
                "आपने हमें बेहतर बनाया.",
                "गुरु का आशीर्वाद सबसे बड़ा उपहार है.",
            ]},
            {"key": "emotional", "h2": "Heart Touching Teachers Day Wishes in Hindi", "lines": [
                "आपने हमें तब संभाला जब हमें खुद पर भरोसा कम था.",
                "आपकी एक बात ने कई बार हमारी सोच बदल दी.",
                "आपने हमें marks से ज्यादा मेहनत की कीमत समझाई.",
                "आज हम जो भी सीख पाए हैं, उसमें आपका बड़ा योगदान है.",
                "आपका स्नेह और अनुशासन दोनों हमारे लिए आशीर्वाद रहे.",
                "आपने हमें गिरकर उठना और फिर कोशिश करना सिखाया.",
                "आपकी क्लास सिर्फ पढ़ाई नहीं, जीवन की तैयारी थी.",
                "शिक्षक दिवस पर दिल से धन्यवाद, आपने हमें दिशा दी.",
                "आपकी सीख हमारे फैसलों में आज भी साथ रहती है.",
                "आपने हमें सपने देखने और उन्हें पूरा करने की हिम्मत दी.",
            ]},
            {"key": "teacher_quotes", "h2": "Teachers Day Quotes in Hindi", "lines": [
                "गुरु वह दीपक है जो खुद जलकर दूसरों को रोशनी देता है.",
                "एक अच्छा शिक्षक किताब से पहले इंसान को पढ़ना सिखाता है.",
                "ज्ञान का असली अर्थ वही समझाता है जो धैर्य से सिखाता है.",
                "शिक्षक वह शक्ति है जो साधारण बच्चे में असाधारण विश्वास जगाती है.",
                "गुरु की सीख समय के साथ और भी मूल्यवान हो जाती है.",
                "शिक्षक का सम्मान ज्ञान का सम्मान है.",
                "एक शिक्षक कई पीढ़ियों की सोच बदल सकता है.",
                "गुरु बिना ज्ञान अधूरा और जीवन की दिशा धुंधली रहती है.",
                "शिक्षा का सुंदर रूप शिक्षक के व्यवहार में दिखता है.",
                "गुरु का आशीर्वाद हर सफलता की नींव बन सकता है.",
            ]},
            {"key": "whatsapp", "h2": "Teachers Day WhatsApp Wishes in Hindi", "lines": [
                "Happy Teachers Day, सर. आपकी सीख हमेशा याद रहेगी.",
                "मैम, शिक्षक दिवस की हार्दिक शुभकामनाएं और बहुत धन्यवाद.",
                "आपके मार्गदर्शन के लिए दिल से आभार.",
                "शिक्षक दिवस पर आपको सम्मान और शुभकामनाएं.",
                "आपने हमें मेहनत और ईमानदारी की कीमत समझाई.",
                "आप जैसे शिक्षक मिलना सौभाग्य की बात है.",
                "आपकी हर सलाह आज भी काम आती है.",
                "Happy Teachers Day, आपका आशीर्वाद बना रहे.",
                "आपने हमें पढ़ाई के साथ संस्कार भी सिखाए.",
                "शिक्षक दिवस की शुभकामनाएं, आप सच में प्रेरणा हैं.",
            ]},
            {"key": "sir", "h2": "Teachers Day Wishes in Hindi for Sir", "lines": [
                "सर, आपकी सीख और अनुशासन ने हमें सही दिशा दी.",
                "शिक्षक दिवस की शुभकामनाएं सर, आपका मार्गदर्शन हमेशा याद रहेगा.",
                "आपने हमें मेहनत से कभी डरना नहीं सिखाया.",
                "सर, आपने हमारी कमियों को समझकर हमें बेहतर बनाया.",
                "आपकी सलाह ने कई बार सही फैसला लेने में मदद की.",
                "आपने हमें पढ़ाई के साथ आत्मविश्वास भी दिया.",
                "आप जैसे शिक्षक को सादर प्रणाम.",
                "सर, आपकी क्लास ने हमें सोचने का नया तरीका दिया.",
                "शिक्षक दिवस पर आपका दिल से धन्यवाद.",
                "आपकी मेहनत और धैर्य के लिए बहुत आभार.",
            ]},
            {"key": "mam", "h2": "Teachers Day Wishes in Hindi for Mam", "lines": [
                "मैम, आपकी मुस्कान और सीख दोनों हमेशा याद रहेंगी.",
                "शिक्षक दिवस की शुभकामनाएं मैम, आपने हमें प्यार से सिखाया.",
                "आपने हर गलती को सीखने का मौका बनाया.",
                "मैम, आपका धैर्य और मार्गदर्शन हमारे लिए बहुत खास है.",
                "आपने हमें आत्मविश्वास से बोलना और सोचना सिखाया.",
                "आपकी क्लास में सीखना हमेशा आसान लगा.",
                "मैम, आपका स्नेह और प्रेरणा अमूल्य है.",
                "शिक्षक दिवस पर आपको सम्मान और धन्यवाद.",
                "आपने हमें पढ़ाई के साथ विनम्रता भी सिखाई.",
                "आप हमारे लिए हमेशा प्रेरणा रहेंगी.",
            ]},
            {"key": "from_students", "h2": "Teachers Day Message in Hindi from Students", "lines": [
                "प्रिय शिक्षक, आपने हमें सीखने का सही अर्थ समझाया.",
                "आपके कारण हमारी पढ़ाई में रुचि और जीवन में अनुशासन आया.",
                "पूरी क्लास की तरफ से आपको शिक्षक दिवस की शुभकामनाएं.",
                "आपने हर विद्यार्थी को बराबर समझा और आगे बढ़ाया.",
                "आपकी मेहनत ने हमारी मेहनत को सही दिशा दी.",
                "हम आपके धैर्य, स्नेह और मार्गदर्शन के लिए आभारी हैं.",
                "आपकी सीख हमें स्कूल के बाद भी याद रहेगी.",
                "शिक्षक दिवस पर हमारी ओर से सादर प्रणाम.",
                "आपने हमें अच्छे marks से ज्यादा अच्छा इंसान बनना सिखाया.",
                "धन्यवाद, आपने हमारी journey को meaningful बनाया.",
            ]},
            {"key": "caption", "h2": "Teachers Day Captions in Hindi", "lines": [
                "गुरु की सीख, जीवन की रोशनी.",
                "मेरे शिक्षक, मेरी प्रेरणा.",
                "ज्ञान देने वालों को सादर नमन.",
                "शिक्षक दिवस पर दिल से धन्यवाद.",
                "सीख, सम्मान और आभार.",
                "गुरु बिना रास्ता अधूरा.",
                "आपकी सीख हमेशा साथ है.",
                "Teachers Day, gratitude in every word.",
                "एक अच्छा शिक्षक जीवन बदल देता है.",
                "शिक्षक दिवस 2026 की शुभकामनाएं.",
            ]},
            {"key": "cards", "h2": "Teachers Day Card Message in Hindi", "lines": [
                "प्रिय शिक्षक, आपने हमें हर दिन कुछ नया सीखने की प्रेरणा दी.",
                "आपका मार्गदर्शन मेरे जीवन की सबसे सुंदर सीखों में से एक है.",
                "इस शिक्षक दिवस पर मैं आपका दिल से धन्यवाद करता हूं.",
                "आपकी क्लास ने मुझे पढ़ाई से प्यार करना सिखाया.",
                "आपने मुझे समझाया कि कोशिश कभी बेकार नहीं जाती.",
                "आपके आशीर्वाद और सीख के लिए मैं हमेशा आभारी रहूंगा.",
                "आपने मेरी गलतियों को patience से सुधारा.",
                "आपका विश्वास मेरे लिए बहुत बड़ा gift रहा है.",
                "शिक्षक दिवस पर आपको सम्मान, आभार और शुभकामनाएं.",
                "आप जैसे गुरु जीवन में बहुत कम मिलते हैं.",
            ]},
            {"key": "gift", "h2": "Teachers Day Gift Ideas with Hindi Wishes", "lines": [
                "एक छोटा सा keepsake और साफ Hindi message शिक्षक दिवस को यादगार बना सकता है.",
                "Pendant के साथ एक blank card में धन्यवाद की एक sincere line लिखें.",
                "Ring या bracelet को gift करते समय message को simple रखें.",
                "Earrings जैसे wearable gift के साथ respectful wish अच्छा लगता है.",
                "Gift का focus price पर नहीं, gratitude पर रखें.",
                "Teacher के style और comfort को ध्यान में रखकर design चुनें.",
                "Card में लंबा भाषण नहीं, एक honest sentence काफी होता है.",
                "अगर group gift है तो सब students की तरफ से short note जोड़ें.",
                "BlueStone jewellery को soft keepsake की तरह mention करें, catalogue की तरह नहीं.",
                "सबसे अच्छा gift वही है जिसमें सम्मान और याद दोनों हों.",
            ]},
            {"key": "how_to", "h2": "How to Write Teachers Day Wishes in Hindi", "lines": [
                "पहले शिक्षक का नाम या Sir, Mam जैसे respectful संबोधन लिखें.",
                "एक specific सीख या याद जोड़ें जिससे message personal लगे.",
                "बहुत heavy words से बचें, simple Hindi ज्यादा natural लगती है.",
                "WhatsApp के लिए दो line का message रखें.",
                "Card के लिए थोड़ा भावुक लेकिन साफ message लिखें.",
                "अगर class की तरफ से message है तो collective gratitude लिखें.",
                "Jokes तभी जोड़ें जब teacher के साथ रिश्ता informal हो.",
                "Readable text वाले image पोस्ट से बचें अगर design clean रखना है.",
                "शब्दों में सम्मान, आभार और warmth होनी चाहिए.",
                "अंत में शुभकामनाएं या सादर प्रणाम लिखना अच्छा लगता है.",
            ]},
        ],
        "faqs": [
            ["Teachers Day wishes in Hindi कैसे लिखें?", "Teachers Day wishes in Hindi लिखते समय शिक्षक का सम्मान, एक छोटी याद और धन्यवाद जोड़ें. Message बहुत लंबा न रखें. Simple line जैसे आपकी सीख हमेशा याद रहेगी, शिक्षक दिवस की शुभकामनाएं अच्छा काम करती है."],
            ["Shikshak Diwas ki hardik shubhkamnaye कैसे बोलें?", "आप लिख सकते हैं: शिक्षक दिवस की हार्दिक शुभकामनाएं, आपका मार्गदर्शन हमारे लिए अमूल्य है. यह line formal card, WhatsApp और school message तीनों में अच्छी लगती है."],
            ["Teacher ke liye short Hindi wish क्या है?", "Short Hindi wish हो सकती है: शिक्षक दिवस की शुभकामनाएं, आपने हमें बेहतर बनना सिखाया. यह छोटी, respectful और copy ready line है."],
            ["Sir ke liye Teachers Day message in Hindi क्या लिखें?", "Sir के लिए लिखें: सर, आपकी सीख और अनुशासन ने हमें सही दिशा दी. शिक्षक दिवस की हार्दिक शुभकामनाएं और दिल से धन्यवाद."],
            ["Mam ke liye Teachers Day wish in Hindi क्या लिखें?", "Mam के लिए लिखें: मैम, आपने हर गलती को सीखने का मौका बनाया. शिक्षक दिवस की शुभकामनाएं और आपके धैर्य के लिए धन्यवाद."],
            ["Teachers Day card में Hindi message कितना लंबा होना चाहिए?", "Card message 2 से 4 lines का हो तो अच्छा लगता है. एक greeting, एक personal thank you, और एक respectful closing जोड़ें."],
        ],
    }

    config = {
        "rank": 99,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-teachersdayhindi",
        "occasion_year": "Teachers Day 2026",
        "carousel_alt_prefix": "teachers day wishes in Hindi 2026 gift idea",
        "gift_h2": "BlueStone Gift Ideas for Teachers Day 2026",
        "gift_blurb": "A Teachers Day gift should feel respectful, useful, and easy to wear. These BlueStone pieces work as soft keepsakes beside a sincere Hindi note.",
        "conclusion_html": "Teachers Day wishes in Hindi are strongest when they sound respectful and real. Pick one short line, add a personal memory if you can, and let the message carry simple gratitude.",
        "schema_keywords": ["teachers day wishes in hindi", "teachers day quotes in hindi", "shikshak diwas ki hardik shubhkamnaye", "teachers day message in hindi", "teachers day captions in hindi"],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(csv_rows, "The Aagarna Pendant", "ProductImages/seo images/Pendants/The Aagarna Pendant.png"),
            product(csv_rows, "The Tarentella Oval Bangle", "ProductImages/seo images/Bangles/The Tarentella Oval Bangle.png"),
            product(csv_rows, "The Anya Ring", "ProductImages/seo images/Rings/The Anya Ring.png"),
            product(csv_rows, "The Nettile Huggie Earrings", "ProductImages/seo images/Earrings/The Nettile Huggie Earrings.png"),
            product(csv_rows, "The Malibu Ring", "ProductImages/seo images/Rings/The Malibu Ring.png"),
            product(csv_rows, "The Rafia Ring", "ProductImages/seo images/Rings/The Rafia Ring.png"),
        ],
        "flatlay_insert_h2": "Shikshak Diwas Ki Hardik Shubhkamnaye",
        "lifestyle_insert_h2": "Teachers Day Quotes in Hindi",
        "more_reads_html": "Read more thoughtful guides in <a href=\"https://blog.bluestone.com/thank-you-note-to-teacher-2026/\">thank you note to teacher 2026</a>, <a href=\"https://blog.bluestone.com/5-september-teachers-day-2026/\">5 September Teachers Day 2026</a>, <a href=\"https://blog.bluestone.com/mother-day-wish-in-hindi-2026/\">mother day wish in Hindi 2026</a>, and <a href=\"https://blog.bluestone.com/friendship-day-shayari-2026/\">Friendship Day shayari 2026</a>.",
        "how_to_html": "For date context, India celebrates Teachers Day on 5 September. For background on Dr Sarvepalli Radhakrishnan, you can refer to <a href=\"https://www.britannica.com/biography/Sarvepalli-Radhakrishnan\">Britannica</a>. Keep your own message short, respectful, and personal.",
        "faq_h2": "Frequently Asked Questions about Teachers Day Wishes in Hindi",
        "min_lines": 100,
    }

    hero = consolidated(detail_rows, "The Lumeelle Cluster Pendant")
    flatlay = consolidated(detail_rows, "The Rafia Ring")
    lifestyle = consolidated(detail_rows, "The Ursa Hoop Earrings")

    prompts = {
        "rank": 99,
        "slug": "teachers-day-wishes-in-hindi-2026",
        "primary_kw": "teachers day wishes in hindi",
        "output_prefix": PREFIX,
        "caption_occasion": "Teachers Day wishes in Hindi",
        "caption_year": "2026",
        "flatlay_setting": "study-desk",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/teachers-day-wishes-in-hindi-hero-2026.webp",
            "flatlay": "output/magnific_generated/teachers-day-wishes-in-hindi-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/teachers-day-wishes-in-hindi-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "teachers day wishes in Hindi 2026 hero The Lumeelle Cluster Pendant",
            "flatlay": "teachers day wishes in Hindi 2026 flatlay The Rafia Ring",
            "lifestyle": "teachers day wishes in Hindi 2026 lifestyle The Ursa Hoop Earrings",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                **hero,
                "alt": "teachers day wishes in Hindi 2026 hero with The Lumeelle Cluster Pendant",
                "caption": "Teachers Day wishes in Hindi 2026 vibe: The Lumeelle Cluster Pendant",
                "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]},
                "cdn": [
                    "https://kinclimg7.bluestone.com/giproduct/BISW1080P133_RAA18DIG4SYEMXXXX_ABCD00-BP-PICS-00000-1024-114851.png",
                    "https://kinclimg8.bluestone.com/giproduct/BISW1080P133_RAA18DIG4SYEMXXXX_ABCD00-PICS-00000-1024-114851.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Lumeelle Cluster Pendant/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Lumeelle Cluster Pendant/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": people_prompt(
                    hero,
                    "hero, sitting at a teacher desk with a blank cream thank you card and closed notebook, soft classroom window light",
                    "the rose gold cluster pendant with green emerald accents and diamond cluster detail",
                    "pendant size on the neck",
                    "Hands stay low near a blank card; wrists and fingers are bare; no earrings, no bracelet, no bangles, no rings, no watch, no extra necklace.",
                ),
            },
            "flatlay": {
                **flatlay,
                "alt": "teachers day wishes in Hindi 2026 flatlay with The Rafia Ring",
                "caption": "Teachers Day wishes in Hindi 2026 keepsake: The Rafia Ring",
                "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]},
                "cdn": [
                    "https://kinclimg5.bluestone.com/giproduct/BIAB0503R03_YAA18DIG6XXXXXXXX_ABCD00-PICS-00001-1024-42032.png",
                    "https://kinclimg5.bluestone.com/giproduct/BIAB0503R03_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-42032.png",
                    "https://kinclimg5.bluestone.com/giproduct/BIAB0503R03_YAA18DIG6XXXXXXXX_ABCD00-PICS-00002-1024-42032.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Rings/The Rafia Ring/0_primary.png",
                    "ProductImages/raw/Rings/The Rafia Ring/2_front.png",
                    "ProductImages/raw/Rings/The Rafia Ring/3_back.png",
                ],
                "ref_roles": ["primary", "front", "back"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\n"
                    "Teachers Day wishes in Hindi 2026 top-down flatlay. Flatlay setting ID: study-desk. Surface and props: warm wooden teacher desk, completely blank cream card, capped fountain pen, closed blank notebook, chalk pieces with no writing, and tiny dried flowers. "
                    "The identical Rafia Ring from @img1, @img2 and @img3 rests naturally on the blank card corner at true PDP scale. "
                    f"Product dimensions from PDP: {flatlay['size_prompt_note']}. Do not enlarge for visibility. "
                    "Full ring visible, yellow gold ring with diamond floral cluster detail, 100 percent identical design, zero distortion, HD metal and stone detail.\n\n"
                    "Props stay secondary. No people, no hands, no logos, no readable text, no letters, no numbers, no other jewellery.\n\n"
                    "Avoid: hands, people, floating overlays, cutouts, incorrect ring design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI."
                ),
            },
            "lifestyle": {
                **lifestyle,
                "alt": "teachers day wishes in Hindi 2026 lifestyle with The Ursa Hoop Earrings",
                "caption": "Teachers Day wishes in Hindi 2026 vibe: The Ursa Hoop Earrings",
                "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]},
                "cdn": [
                    "https://kinclimg3.bluestone.com/giproduct/BISP0427H21_YAA18DIG6XXXXXXXX_ABCD00-BP-PICS-00000-1024-78187.png",
                    "https://kinclimg1.bluestone.com/giproduct/BISP0427H21_YAA18DIG6XXXXXXXX_ABCD00-PICS-00004-1024-78187.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Earrings/The Ursa Hoop Earrings/1_body_portrait.png",
                    "ProductImages/raw/Earrings/The Ursa Hoop Earrings/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": people_prompt(
                    lifestyle,
                    "lifestyle, smiling beside a blank classroom board and a blank thank you card on a desk, soft respectful mood",
                    "the yellow gold hoop earrings with diamond accents",
                    "earring size on the ears",
                    "Bare neck, bare wrists, bare fingers; no necklace, no pendant, no bracelet, no bangles, no rings, no watch.",
                ),
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 99

Article: Teachers Day Wishes in Hindi 2026
Status: Draft assets prepared
Date: 2026-07-24

## A. Intent and Brief
- [x] Primary keyword: teachers day wishes in hindi
- [x] Sheet Action treated as New
- [x] Fresh slug: teachers-day-wishes-in-hindi-2026
- [x] 2026 year lock used
- [x] Supporting keyword mapped to H2 and FAQ: shikshak diwas ki hardik shubhkamnaye

## B. SEO Structure
- [x] Title/H1 intent prepared
- [x] Yoast title under 60 chars
- [x] Meta description 150 to 160 chars
- [x] Primary keyword in intro and hero alt

## C. Content and Readability
- [x] Direct answer and TL;DR
- [x] 100+ Hindi wish/message/caption lines
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
    write_json("output/publish_configs/rank99.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")
    print(f"wrote {PREFIX} sections/config/prompts")


if __name__ == "__main__":
    main()
