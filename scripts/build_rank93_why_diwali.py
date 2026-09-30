#!/usr/bin/env python3
"""Build Rank 93 why we celebrate Diwali assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank93_WhyDiwali"
FILMIC_STYLE = (
    "Visual style: subtle cinematic film grain / analog grain, Kodak Portra color science, "
    "gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, "
    "editorial color grading, natural dynamic range, filmic contrast."
)


def load_products() -> dict[str, dict[str, str]]:
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
    rows = load_products()
    sections = {
        "meta": {
            "title": "Why We Celebrate Diwali 2026: Meaning and Story",
            "slug": "why-we-celebrate-diwali-2026",
            "meta_desc": "Why we celebrate Diwali 2026 explained with history, meaning, Lakshmi Puja, lights, family rituals, eco-friendly ideas, and simple answers for students.",
            "focus_kw": "why we celebrate diwali",
            "yoast_title": "Why We Celebrate Diwali 2026",
        },
        "intro": [
            "Why we celebrate Diwali is a question with many beautiful answers. Diwali is about light over darkness, good over evil, knowledge over ignorance, family togetherness, gratitude, and the hope of a fresh beginning.",
            "TL;DR: Diwali celebrates the victory of light, the return of Lord Rama in many traditions, Lakshmi Puja for prosperity, new beginnings for families and businesses, and the joy of sharing light with others.",
        ],
        "sections": [
            {"key": "meaning", "h2": "Why We Celebrate Diwali", "lines": [
                "Diwali is celebrated as the festival of lights across India and many Indian communities worldwide.",
                "The central idea is the victory of light over darkness and good over evil.",
                "Families light diyas to welcome positivity, wisdom, and hope into the home.",
                "Many people connect Diwali with the return of Lord Rama to Ayodhya after defeating Ravana.",
                "The lighting of lamps symbolises the joy of people welcoming righteousness back.",
                "Diwali is also linked with Goddess Lakshmi, who represents prosperity and auspiciousness.",
                "For many families, the festival is a time to clean, decorate, pray, forgive, and begin again.",
                "The celebration changes by region, but the emotional meaning remains warm and hopeful.",
                "Diwali is not only about lights outside the home; it is also about light inside the heart.",
                "That is why Diwali remains one of India's most loved festivals.",
            ]},
            {"key": "story", "h2": "The Story Behind Diwali", "lines": [
                "One popular Diwali story comes from the Ramayana.",
                "Lord Rama, Sita, and Lakshman returned to Ayodhya after fourteen years of exile.",
                "Rama had defeated Ravana, which represented the victory of dharma over adharma.",
                "People of Ayodhya lit rows of lamps to welcome them home.",
                "This is why diyas became an important part of Diwali celebrations.",
                "In some regions, Diwali is linked with Lord Krishna defeating Narakasura.",
                "In others, it marks the worship of Goddess Kali or the beginning of a new business year.",
                "Jain, Sikh, and Buddhist communities also have meaningful Diwali associations.",
                "The festival therefore holds many stories, not just one.",
                "Together, these stories teach courage, renewal, and the power of goodness.",
            ]},
            {"key": "lakshmi", "h2": "Why Lakshmi Puja Is Done on Diwali", "lines": [
                "Lakshmi Puja is performed to welcome prosperity, harmony, and auspicious energy.",
                "Families clean homes because cleanliness is seen as a way to invite positivity.",
                "Diyas, rangoli, flowers, and prayers create a warm and respectful atmosphere.",
                "The puja is not only about money; it is also about gratitude for shelter, food, work, and family.",
                "Many businesses close old accounts and begin new ledgers around Diwali.",
                "People pray for wisdom to use prosperity responsibly.",
                "Offerings are made with devotion rather than display.",
                "The lamp near the puja space represents clarity and hope.",
                "Lakshmi Puja reminds families to value both abundance and humility.",
                "That balance is a key reason Diwali feels spiritually rich.",
            ]},
            {"key": "lights", "h2": "Why We Light Diyas on Diwali", "lines": [
                "Diyas are small lamps that symbolise hope, purity, and the removal of darkness.",
                "Lighting a diya is a simple act with deep meaning.",
                "The flame reminds people that even a small light can change a dark space.",
                "Rows of diyas also connect to the welcome of Lord Rama in Ayodhya.",
                "Many families place diyas near doors, windows, balconies, and puja rooms.",
                "The light is believed to invite goodness and keep negativity away.",
                "Children often learn Diwali's meaning through the simple image of a glowing lamp.",
                "Diyas make homes feel festive without needing anything loud.",
                "They also create a shared ritual that families repeat every year.",
                "That is why diyas remain the heart of Diwali decor.",
            ]},
            {"key": "family", "h2": "How Families Celebrate Diwali", "lines": [
                "Families often begin with cleaning and decorating the home.",
                "Rangoli, flowers, lights, and diyas make the entrance feel welcoming.",
                "People wear festive clothes and gather for puja in the evening.",
                "Sweets and snacks are shared with relatives, neighbours, and friends.",
                "Many families exchange gifts as a gesture of love and goodwill.",
                "Children enjoy stories, lamps, sweets, and family photos.",
                "Elders bless younger family members for health and success.",
                "Some families visit temples or host guests at home.",
                "The best celebrations keep warmth above show.",
                "Diwali becomes memorable when everyone feels included.",
            ]},
            {"key": "students", "h2": "Why We Celebrate Diwali for Students", "lines": [
                "For students, Diwali can be explained as the festival of light and goodness.",
                "It teaches that truth and courage can defeat fear and injustice.",
                "The story of Rama's return shows the value of patience, duty, and hope.",
                "Lakshmi Puja teaches gratitude for what we have.",
                "Lighting diyas teaches that small positive actions matter.",
                "Cleaning the home teaches preparation before new beginnings.",
                "Sharing sweets teaches kindness and community.",
                "Eco-friendly Diwali teaches responsibility toward nature.",
                "The festival is both cultural and moral.",
                "A simple answer for students is: we celebrate Diwali to welcome light, goodness, and happiness.",
            ]},
            {"key": "regions", "h2": "Different Reasons for Diwali in India", "lines": [
                "North India often connects Diwali with Lord Rama's return to Ayodhya.",
                "Parts of South India connect it with Krishna's victory over Narakasura.",
                "Bengal and eastern regions may focus on Kali Puja.",
                "Many business communities mark a new financial or trading year.",
                "Jain communities remember Lord Mahavira's nirvana.",
                "Sikhs observe Bandi Chhor Divas around the Diwali period.",
                "Some Buddhist communities also observe the festival in regional ways.",
                "These meanings show India's cultural variety.",
                "The common thread is light, freedom, wisdom, and renewal.",
                "Diwali is therefore one festival with many doors of meaning.",
            ]},
            {"key": "modern", "h2": "Modern Meaning of Diwali", "lines": [
                "Modern Diwali is still rooted in old stories, but it also speaks to everyday life.",
                "People use the festival to reconnect with family after busy months.",
                "It is a time to pause, clean, decorate, and reset the home.",
                "Many people send wishes to colleagues, clients, and friends.",
                "The festival encourages generosity through gifts, sweets, and charity.",
                "It also reminds people to reduce bitterness and begin again.",
                "A modern Diwali can be joyful without becoming wasteful.",
                "The best celebration protects both tradition and the environment.",
                "Light becomes a symbol of emotional clarity too.",
                "That is why Diwali continues to feel relevant every year.",
            ]},
            {"key": "eco", "h2": "Eco-Friendly Diwali Celebration Ideas", "lines": [
                "Use clay diyas or reusable lights instead of excessive plastic decor.",
                "Choose flowers, rangoli powder, and fabric decorations where possible.",
                "Avoid loud crackers, especially near children, elders, pets, and hospitals.",
                "Share homemade sweets or thoughtful small gifts.",
                "Use blank gift cards and recyclable wrapping when possible.",
                "Support local artisans for diyas, decor, and festive items.",
                "Keep lamps safe and away from curtains or paper.",
                "Celebrate with music, food, stories, and family photos.",
                "Teach children that joy does not need noise to feel festive.",
                "An eco-friendly Diwali keeps the light and reduces the harm.",
            ]},
            {"key": "gift", "h2": "Diwali Gift Ideas with Meaning", "lines": [
                "A Diwali gift should feel warm, auspicious, and useful.",
                "Jewellery works well when it suits the person's daily style.",
                "A pendant can symbolise light, protection, or a fresh beginning.",
                "A bangle can feel festive and graceful for family gifting.",
                "Earrings are practical for someone who likes simple festive dressing.",
                "Avoid making the gift message about price.",
                "Add one line about light, gratitude, or blessings.",
                "Choose quality over size or display.",
                "A thoughtful gift should support the emotion, not replace it.",
                "The best Diwali gift says, may your year be bright.",
            ]},
            {"key": "summary", "h2": "Simple Answer: Why Do We Celebrate Diwali?", "lines": [
                "We celebrate Diwali to honour the victory of light over darkness.",
                "We celebrate it to remember stories of courage and goodness.",
                "We celebrate it to welcome prosperity with humility.",
                "We celebrate it to clean our homes and refresh our minds.",
                "We celebrate it to gather with family and share happiness.",
                "We celebrate it to light diyas as a sign of hope.",
                "We celebrate it to begin again with positive energy.",
                "We celebrate it to teach children values through tradition.",
                "We celebrate it to spread kindness in the community.",
                "In simple words, Diwali is a festival of light, love, and new beginnings.",
            ]},
        ],
        "section_leads": {},
        "faqs": [
            ["Why do we celebrate Diwali?", "We celebrate Diwali to honour light over darkness, good over evil, prosperity, family togetherness, and new beginnings."],
            ["What is the main story of Diwali?", "A popular story says Diwali marks Lord Rama, Sita, and Lakshman's return to Ayodhya after fourteen years of exile and Rama's victory over Ravana."],
            ["Why do we light diyas on Diwali?", "Diyas symbolise hope, purity, and the removal of darkness. They also connect to the lamps lit to welcome Lord Rama back to Ayodhya."],
            ["Why is Lakshmi Puja done on Diwali?", "Lakshmi Puja is done to welcome prosperity, auspiciousness, gratitude, and responsible abundance into the home."],
            ["How can students explain Diwali?", "Students can say Diwali is the festival of lights, celebrated to welcome goodness, happiness, and the victory of light over darkness."],
            ["How can we celebrate eco-friendly Diwali?", "Use diyas, reusable decor, simple gifts, fewer crackers, local products, and family activities that keep the festival joyful without excess waste."],
        ],
    }

    config = {
        "rank": 93,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-whydiwali",
        "occasion_year": "Why We Celebrate Diwali 2026",
        "carousel_alt_prefix": "why we celebrate diwali 2026 gift idea",
        "gift_h2": "Meaningful Diwali Jewellery Gift Ideas",
        "gift_blurb": "If Diwali is about light, renewal, and blessings, a thoughtful keepsake can carry that feeling beyond the evening puja. These approved BlueStone designs suit festive gifting without mentioning prices.",
        "conclusion_html": "Diwali is celebrated because light, goodness, gratitude, and family still matter. Whether you explain it through Rama's return, Lakshmi Puja, diyas, or new beginnings, the heart of Diwali is hope.",
        "schema_keywords": ["why we celebrate diwali", "diwali meaning", "diwali story", "lakshmi puja", "why do we light diyas on diwali", "eco friendly diwali"],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "content_mode": "education",
        "products": [
            product(rows, "The Xarvithis Pendant", "Pendants"),
            product(rows, "The Muricelle Bangle", "Bangles"),
            product(rows, "The Rohal Huggie Earrings", "Earrings"),
            product(rows, "The Quinn Ring", "Rings"),
            product(rows, "The Aagarna Pendant", "Pendants"),
            product(rows, "The Ebony Ring", "Rings"),
        ],
        "flatlay_insert_h2": "Why We Light Diyas on Diwali",
        "lifestyle_insert_h2": "Diwali Gift Ideas with Meaning",
        "more_reads_html": "Read more Diwali guides in <a href=\"https://blog.bluestone.com/happy-diwali-wishes-messages-quotes-2026/\">happy Diwali wishes 2026</a>, <a href=\"https://blog.bluestone.com/diwali-poster-2026/\">Diwali poster 2026</a>, <a href=\"https://blog.bluestone.com/happy-diwali-message-2026/\">happy Diwali message 2026</a>, and <a href=\"https://blog.bluestone.com/thank-you-note-to-teacher-2026/\">thank you note to teacher 2026</a>.",
        "how_to_html": "When explaining Diwali, start with the simple meaning: light over darkness and good over evil. Then add the story or ritual most relevant to your audience, such as Rama's return, Lakshmi Puja, diyas, or family togetherness.",
        "faq_h2": "Frequently Asked Questions about Why We Celebrate Diwali",
        "min_lines": 100,
        "section_leads": {},
    }

    prompts = {
        "rank": 93,
        "slug": "why-we-celebrate-diwali-2026",
        "output_prefix": PREFIX,
        "occasion": "Why We Celebrate Diwali 2026",
        "primary_kw": "why we celebrate diwali",
        "caption_occasion": "Why we celebrate Diwali",
        "caption_year": "2026",
        "flatlay_setting": "festive-mantel",
        "workflow": "Higgsfield MCP nano_banana_pro. Campaign hybrid with mandatory body_image scale line for people shots. Do not generate until balance succeeds. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/why-we-celebrate-diwali-hero-2026.webp",
            "flatlay": "output/magnific_generated/why-we-celebrate-diwali-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/why-we-celebrate-diwali-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "why we celebrate diwali 2026 hero The Xarvithis Pendant",
            "flatlay": "why we celebrate diwali 2026 flatlay The Muricelle Bangle",
            "lifestyle": "why we celebrate diwali 2026 lifestyle The Rohal Huggie Earrings",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                "code": "BISW1080P246", "name": "The Xarvithis Pendant", "gender": "Female", "height_mm": 20.5, "width_mm": 14.3,
                "size_prompt_note": "pendant product height 20.5 mm and width 14.3 mm; product dimensions, not face size; copy worn neck scale from body_image",
                "alt": "why we celebrate diwali 2026 hero with The Xarvithis Pendant", "caption": "Why we celebrate Diwali 2026 vibe: The Xarvithis Pendant",
                "product": {"code": "BISW1080P246", "name": "The Xarvithis Pendant", "pdp": "https://www.bluestone.com/pendants/the-xarvithis-pendant~156920.html"},
                "cdn": ["https://kinclimg2.bluestone.com/giproduct/BISW1080P246_RAA18DIG6XXXXXXXX_ABCD00-BP-PICS-00000-1024-103903.png", "https://kinclimg7.bluestone.com/giproduct/BISW1080P246_RAA18DIG6XXXXXXXX_ABCD00-PICS-00001-1024-103903.png"],
                "local_reference_images": ["ProductImages/raw/Pendants/The Xarvithis Pendant/1_body_portrait.png", "ProductImages/raw/Pendants/The Xarvithis Pendant/0_primary.png"],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} Why we celebrate Diwali 2026 hero, solo fair-skinned Indian adult woman in a warm modern Indian living room lighting a diya near a blank rangoli corner and small festive gift. Full head, full face, both eyes, complete smile, neck, pendant, hands, diya, and upper body visible with safe margins. Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, soft diya and window light, realistic shadows, 16:9.\n\nThe woman physically wears The Xarvithis Pendant from @img1 body_image and @img2 design on a fine chain at upper chest. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: pendant product height_mm=20.5 and width_mm=14.3. These are real product dimensions, NOT face-size instructions. Keep pendant size on the neck like @img1 body_image worn neck scale: subtle pendant size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the rose gold pendant exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery in the image. Bare wrists, bare fingers, no watches, no bracelets, no rings, no earrings, no extra necklaces. No readable text anywhere.\n\nAvoid: cropped face, cropped head, readable text, man wearer, child, second person, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow.",
            },
            "flatlay": {
                "code": "BISM0003O14", "name": "The Muricelle Bangle", "gender": "Female", "height_mm": 52.03, "width_mm": 14.3,
                "size_prompt_note": "bangle product height 52.03 mm and width 14.3 mm; product dimensions, not face size",
                "alt": "why we celebrate diwali 2026 flatlay with The Muricelle Bangle", "caption": "Why we celebrate Diwali 2026 keepsake: The Muricelle Bangle",
                "product": {"code": "BISM0003O14", "name": "The Muricelle Bangle", "pdp": "https://www.bluestone.com/bangles/the-muricelle-bangle~1001.html"},
                "cdn": ["https://kinclimg2.bluestone.com/giproduct/BISM0003O14_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-62802.png", "https://kinclimg2.bluestone.com/giproduct/BISM0003O14_YAA18DIG6XXXXXXXX_ABCD00-PICS-00001-1024-62802.png", "https://kinclimg2.bluestone.com/giproduct/BISM0003O14_YAA18DIG6XXXXXXXX_ABCD00-PICS-00002-1024-62802.png"],
                "local_reference_images": ["ProductImages/seo images/Bangles/The Muricelle Bangle.png"], "ref_roles": ["primary", "angle", "angle"],
                "prompt": f"Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\nWhy we celebrate Diwali 2026 top-down flatlay. Flatlay setting ID: festive-mantel. Surface and props: warm wooden festive mantel, small clay diya, marigold petals, blank cream gift tag, soft silk ribbon, no readable text. The identical Muricelle Bangle from @img1, @img2 and @img3 rests naturally on the surface at true PDP scale. Product dimensions from PDP: bangle product height_mm=52.03 and width_mm=14.3. These are product dimensions, NOT face-size instructions. Do not enlarge for visibility. Full bangle visible, yellow gold hinged bangle with diamond detail, 100 percent identical design, zero distortion, HD metal and stone detail.\n\nProps stay secondary. No people, no hands, no logos, no readable text.\n\nAvoid: hands, people, floating overlays, cutouts, incorrect bangle design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI.",
            },
            "lifestyle": {
                "code": "BIPM0001H28", "name": "The Rohal Huggie Earrings", "gender": "Female", "height_mm": 16.0, "width_mm": 4.8,
                "size_prompt_note": "earring product height 16.0 mm and width 4.8 mm; product dimensions, not face size; copy worn ear scale from body_image",
                "alt": "why we celebrate diwali 2026 lifestyle with The Rohal Huggie Earrings", "caption": "Why we celebrate Diwali 2026 vibe: The Rohal Huggie Earrings",
                "product": {"code": "BIPM0001H28", "name": "The Rohal Huggie Earrings", "pdp": "https://www.bluestone.com/earrings/the-rohal-huggie-earrings~21864.html"},
                "cdn": ["https://kinclimg8.bluestone.com/giproduct/BIPM0001H28_YAA18DIG6SYEMXXXX_ABCD00-BP-PICS-00000-1024-79820.png", "https://kinclimg5.bluestone.com/giproduct/BIPM0001H28_YAA18DIG6SYEMXXXX_ABCD00-PICS-00000-1024-79820.png"],
                "local_reference_images": ["ProductImages/raw/Earrings/The Rohal Huggie Earrings/1_body_portrait.png", "ProductImages/raw/Earrings/The Rohal Huggie Earrings/0_primary.png"],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} Why we celebrate Diwali 2026 lifestyle, solo fair-skinned Indian adult woman arranging diyas and marigold petals on a festive side table in a warm home. Full head, full face, both ears, both eyes, complete smile, hands, diyas, and upper body visible with safe margins. Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, soft diya glow, realistic shadows, 16:9.\n\nThe woman physically wears The Rohal Huggie Earrings from @img1 body_image and @img2 design on her ears. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: earring product height_mm=16.0 and width_mm=4.8. These are real product dimensions, NOT face-size instructions. Keep earrings size on the ears like @img1 body_image worn ear scale: subtle earring size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the yellow gold huggie earrings exactly, 100 percent identical to refs, zero distortion, HD metal detail. These earrings are the single and only jewellery in the image. Bare neck, bare wrists, bare fingers, no watch, no bracelet, no rings, no necklace, no other earrings. No readable text anywhere.\n\nAvoid: cropped face, cropped head, man wearer, child, second person, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow.",
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 93

Article: Why We Celebrate Diwali 2026
Status: Draft assets prepared
Date: 2026-07-24

## A. Intent and Brief
- [x] Primary keyword: why we celebrate diwali
- [x] Sheet New treated as New
- [x] Fresh slug: why-we-celebrate-diwali-2026
- [x] 2026 year lock used

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""
    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json("output/publish_configs/rank93.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
