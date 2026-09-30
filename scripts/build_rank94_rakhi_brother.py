#!/usr/bin/env python3
"""Build Rank 94 Raksha Bandhan gifts for brother assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank94_RakhiBrother"
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


def consolidated(rows: dict[str, dict[str, str]], name: str) -> dict[str, str]:
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


def write_json(path: str, data: dict) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def people_prompt(slot: dict[str, str], scene: str, wearer: str, product_phrase: str, scale_phrase: str, avoid_extra: str) -> str:
    return (
        f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} "
        f"Unique rakhi gifts for brother 2026 {scene}. {wearer}. Full head, full face, both eyes, "
        "complete smile, upper body, festive rakhi home setting, and the jewellery area visible with safe margins. "
        "Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, "
        "warm festive window and diya light, realistic shadows, 16:9.\n\n"
        f"The person physically wears {slot['name']} from @img1 body_image and @img2 design. "
        f"GENDER LOCK: Male product on adult man only. Product dimensions from PDP: {slot['size_prompt_note']}. "
        f"Keep {scale_phrase} like @img1 body_image worn scale: subtle real product size, not enlarged. "
        "Use @img2 only for jewellery design.\n\n"
        f"Replicate {product_phrase} exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. "
        f"This is the single and only jewellery in the image. {avoid_extra} No readable text anywhere.\n\n"
        "Avoid: cropped face, cropped head, readable text, woman wearer, child, second person, extra jewellery, "
        "floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, "
        "heavily tanned skin, illustration, CGI, HDR glow."
    )


def main() -> None:
    csv_rows = rows_by_name("Seo Products - final products (1).csv")
    detail_rows = rows_by_name("KnowledgeBase/Product/Seo Products - consolidated.csv")

    sections = {
        "meta": {
            "title": "Unique Rakhi Gifts for Brother 2026: Raksha Bandhan Ideas",
            "slug": "raksha-bandhan-gifts-for-brother-2026",
            "meta_desc": "Raksha Bandhan gifts for brother 2026 with unique rakhi gifts for brother, best rakhi for brothers, rakhi combos, and thoughtful jewellery keepsake ideas.",
            "focus_kw": "unique rakhi gifts for brother",
            "yoast_title": "Unique Rakhi Gifts for Brother 2026: Raksha Bandhan Ideas",
        },
        "intro": [
            "Unique rakhi gifts for brother should feel personal, useful, and worthy of the bond you share. The best Raksha Bandhan gift is not only a return gift ritual; it is a reminder that your brother is seen, loved, teased, and protected too.",
            "TL;DR: choose a gift by his lifestyle first, then match it to his daily style. A bracelet, rakhi bracelet, pendant, chain, or ring works best when it feels wearable after the festival day.",
        ],
        "sections": [
            {"key": "best", "h2": "Best Raksha Bandhan Gifts for Brother", "lines": [
                "Choose a gift he can wear beyond the Rakhi ceremony.",
                "A bracelet works well for a brother who likes simple everyday accessories.",
                "A rakhi bracelet is meaningful because it keeps the festival thread wearable for longer.",
                "A pendant suits a brother who prefers subtle jewellery under a shirt.",
                "A chain is a classic choice for someone who likes clean styling.",
                "A ring can feel personal when you know his size and taste.",
                "Avoid gifts that feel too delicate for his daily routine.",
                "Pick a metal tone he already wears often.",
                "Keep the message warm and short with the gift.",
                "The best gift says you know him, not that you overspent.",
            ]},
            {"key": "unique", "h2": "Unique Rakhi Gifts for Brother", "lines": [
                "A personalised note with jewellery makes the gift feel less formal.",
                "Choose a protective motif if he likes meaningful accessories.",
                "Pick a minimal bracelet for a brother who dislikes loud styling.",
                "Select a pendant if he already wears chains.",
                "Choose a rakhi that can become a keepsake after the day.",
                "Add a photo card from childhood for an emotional touch.",
                "Pair sweets with a practical gift he can use.",
                "Choose one high quality keepsake instead of many small items.",
                "Make the packaging clean, simple, and masculine.",
                "A unique gift feels chosen for him, not chosen at random.",
            ]},
            {"key": "best_rakhi", "h2": "Best Rakhi for Brothers", "lines": [
                "The best rakhi for brothers is comfortable, secure, and meaningful.",
                "An evil eye rakhi can symbolise care and protection.",
                "A gold rakhi feels festive without being disposable.",
                "A bracelet style rakhi is easy to wear after the ceremony.",
                "Choose a lightweight design for daily comfort.",
                "Avoid sharp edges or overly bulky details.",
                "Think about his wrist size before choosing the design.",
                "A simple motif often looks more mature.",
                "Pick a colour that matches his usual wardrobe.",
                "The best rakhi becomes a memory, not clutter.",
            ]},
            {"key": "combo", "h2": "Rakhi Combo for Brother", "lines": [
                "A rakhi combo should feel festive but not overloaded.",
                "Pair a rakhi with sweets and a small note.",
                "Add a bracelet if you want the gift to last longer.",
                "Choose dry fruits or chocolates if he prefers practical hampers.",
                "A grooming item can work for a brother who likes self care.",
                "A wallet or card holder suits office use.",
                "Keep jewellery as the hero of the combo.",
                "Use a blank card so your message feels personal.",
                "Avoid noisy packaging with too many labels.",
                "A clean combo feels thoughtful and premium.",
            ]},
            {"key": "under_budget", "h2": "Rakhi Gift for Brother Under 500", "lines": [
                "If the budget is modest, focus on the emotion first.",
                "A handwritten note can make even a simple rakhi feel special.",
                "Add his favourite snack or chocolate.",
                "Choose a useful everyday item if jewellery is outside budget.",
                "A framed photo can work when the memory is strong.",
                "A small desk item suits a working brother.",
                "A playlist, letter, or printed memory card adds personality.",
                "Avoid apologising for the budget in the message.",
                "Warmth matters more than the size of the gift.",
                "A small gift can still feel deeply personal.",
            ]},
            {"key": "elder", "h2": "Rakhi Gifts for Elder Brother", "lines": [
                "For an elder brother, choose a gift that feels mature and respectful.",
                "A classic bracelet suits office and festive wear.",
                "A simple chain can feel timeless.",
                "A pendant with a protective symbol can feel meaningful.",
                "Choose neutral colours over playful designs.",
                "Add a note thanking him for steady support.",
                "Avoid gifts that feel too childish unless he enjoys humour.",
                "Pick durable designs for regular use.",
                "A clean gift box works better than loud decoration.",
                "The tone should be affectionate, not overly formal.",
            ]},
            {"key": "younger", "h2": "Rakhi Gifts for Younger Brother", "lines": [
                "For a younger brother, choose something stylish but practical.",
                "A modern bracelet can suit college or casual wear.",
                "A minimal pendant works if he likes simple chains.",
                "A playful note can make the gift feel natural.",
                "Choose a sturdy design if he is active.",
                "Avoid overly expensive gifts if he may not wear them often.",
                "Pair the gift with sweets he actually likes.",
                "Add a funny memory to the card.",
                "Let the gift feel cool rather than ceremonial.",
                "The best younger brother gift is easy to wear.",
            ]},
            {"key": "long_distance", "h2": "Long Distance Raksha Bandhan Gifts for Brother", "lines": [
                "When you cannot tie rakhi in person, the message matters even more.",
                "Send the rakhi early so it reaches before the festival.",
                "Add a voice note or video message with the gift.",
                "Choose jewellery that ships safely and wears easily.",
                "A bracelet or pendant is simple to send.",
                "Avoid fragile hampers if delivery is uncertain.",
                "Write the card as if you were speaking to him.",
                "Mention one memory that still makes you smile.",
                "Plan a quick call for the ceremony time.",
                "Distance cannot dilute a thoughtful Rakhi gift.",
            ]},
            {"key": "message", "h2": "What to Write with a Rakhi Gift", "lines": [
                "Keep the note short, warm, and true to your relationship.",
                "For an elder brother, thank him for guidance and protection.",
                "For a younger brother, add affection with a little teasing.",
                "For a long distance brother, mention that you miss the ritual.",
                "Do not make the note sound copied from a greeting card.",
                "Use his name or nickname if it feels natural.",
                "Add one line about why you chose the gift.",
                "A simple blessing works better than a long speech.",
                "End with love, laughter, or a family memory.",
                "The card should sound like you.",
            ]},
            {"key": "jewellery", "h2": "Jewellery Rakhi Gifts for Brother", "lines": [
                "Jewellery works well when it fits his daily life.",
                "A bracelet is the safest starting point for many brothers.",
                "A rakhi bracelet makes the festival memory wearable.",
                "A pendant suits brothers who like understated accessories.",
                "A chain is classic and easy to style.",
                "A ring needs accurate sizing before you choose it.",
                "Avoid choosing only by price or size.",
                "Look for comfort, finish, and long term wearability.",
                "Keep the design close to his personality.",
                "A meaningful keepsake can outlast the festival day.",
            ]},
            {"key": "choose", "h2": "How to Choose Raksha Bandhan Gifts for Brother", "lines": [
                "Start with his lifestyle: office, college, travel, gym, or casual daily wear.",
                "Notice whether he wears gold, steel, leather, or no accessories.",
                "Choose subtle designs if he is new to jewellery.",
                "Choose stronger shapes if he already likes accessories.",
                "Think about comfort before decoration.",
                "Check whether he prefers religious, protective, or modern motifs.",
                "Avoid guessing ring size if you are unsure.",
                "Use the gift card to explain the emotion.",
                "Keep the packaging clean and festive.",
                "The right Rakhi gift feels natural the moment he opens it.",
            ]},
        ],
        "faqs": [
            ["What are unique rakhi gifts for brother?", "Unique rakhi gifts for brother include a bracelet, rakhi bracelet, pendant, chain, ring, personalised note, photo card, grooming item, or a small hamper chosen around his lifestyle."],
            ["What is the best Raksha Bandhan gift for brother?", "The best Raksha Bandhan gift for brother is something he can use or wear after the festival, such as a comfortable bracelet, meaningful pendant, or practical combo with a heartfelt card."],
            ["Which jewellery is good for Rakhi gift for brother?", "Bracelets, rakhi bracelets, pendants, chains, and simple rings are good jewellery gifts for brother when the design matches his daily style."],
            ["What can I gift my brother on Rakhi under 500?", "Under 500, choose a thoughtful rakhi, handwritten note, favourite snack, photo card, small desk item, or a simple personalised keepsake."],
            ["What should I write with a Rakhi gift?", "Write one sincere line about your bond, one reason you chose the gift, and a warm wish for his health, happiness, and success."],
            ["How do I choose a rakhi combo for brother?", "Choose one hero item such as a rakhi or bracelet, then add sweets, dry fruits, a card, or a practical small gift without making the combo feel crowded."],
        ],
    }

    config = {
        "rank": 94,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-rakhibrother",
        "occasion_year": "Raksha Bandhan Gifts for Brother 2026",
        "carousel_alt_prefix": "unique rakhi gifts for brother 2026",
        "gift_h2": "BlueStone Rakhi Gift Ideas for Brother",
        "gift_blurb": "If you want the rakhi gift to last beyond the ceremony, choose a piece that fits his daily style. These approved BlueStone designs keep the emotion of Raksha Bandhan wearable.",
        "conclusion_html": "Unique Rakhi gifts for brother work best when they feel wearable, personal, and honest to your bond. Choose the design around his lifestyle, add a simple note, and let the gift carry the Raksha Bandhan memory beyond one festive day.",
        "schema_keywords": ["unique rakhi gifts for brother", "raksha bandhan gifts for brother", "best rakhi for brothers", "rakhi combo for brother", "rakhi gift for brother under 500"],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(csv_rows, "The Bandhan Bracelet For Him", "ProductImages/seo images/Bracelet/The Bandhan Bracelet For Him.png"),
            product(csv_rows, "The Network Link Bracelet", "ProductImages/seo images/Bracelet/The Network Link Bracelet.png"),
            product(csv_rows, "The Protector Evil Eye Rakhi", "ProductImages/seo images/Adjustable Bracelets/The Protector Evil Eye Rakhi.png"),
            product(csv_rows, "The Talisman Evil Eye Pendant For Him", "ProductImages/seo images/Pendants/The Talisman Evil Eye Pendant For Him.png"),
            product(csv_rows, "The Chevalier Gold Chain", "ProductImages/seo images/Chains/The Chevalier Gold Chain.png"),
            product(csv_rows, "The Jasper Band For Him", "ProductImages/seo images/Rings/The Jasper Band For Him.png"),
        ],
        "flatlay_insert_h2": "Best Rakhi for Brothers",
        "lifestyle_insert_h2": "Jewellery Rakhi Gifts for Brother",
        "more_reads_html": "Read more festive guides in <a href=\"https://blog.bluestone.com/rakhi-wishes-2026/\">rakhi wishes 2026</a>, <a href=\"https://blog.bluestone.com/raksha-bandhan-quotes-in-english/\">Raksha Bandhan quotes</a>, <a href=\"https://blog.bluestone.com/happy-friendship-day-images-2026/\">friendship day images 2026</a>, and <a href=\"https://blog.bluestone.com/why-we-celebrate-diwali-2026/\">why we celebrate Diwali 2026</a>.",
        "how_to_html": "Pick the gift by matching his routine first. Choose a bracelet for everyday comfort, a pendant for subtle styling, a chain for a classic look, and a rakhi bracelet when you want the festival thread to stay wearable.",
        "faq_h2": "Frequently Asked Questions about Rakhi Gifts for Brother",
        "min_lines": 100,
    }

    hero = consolidated(detail_rows, "The Bandhan Bracelet For Him")
    flatlay = consolidated(detail_rows, "The Protector Evil Eye Rakhi")
    lifestyle = consolidated(detail_rows, "The Talisman Evil Eye Pendant For Him")

    prompts = {
        "rank": 94,
        "slug": "raksha-bandhan-gifts-for-brother-2026",
        "primary_kw": "unique rakhi gifts for brother",
        "output_prefix": PREFIX,
        "output": {
            "hero": "output/magnific_generated/raksha-bandhan-gifts-for-brother-hero-2026.webp",
            "flatlay": "output/magnific_generated/raksha-bandhan-gifts-for-brother-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/raksha-bandhan-gifts-for-brother-lifestyle-2026.webp",
        },
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "caption_year": "2026",
        "caption_occasion": "Raksha Bandhan gifts for brother",
        "flatlay_setting": "rakhi-thali",
        "schema_keywords": config["schema_keywords"],
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "slots": {
            "hero": {
                **hero,
                "alt": "unique rakhi gifts for brother 2026 hero with The Bandhan Bracelet For Him",
                "caption": "Raksha Bandhan gifts for brother 2026 style: The Bandhan Bracelet For Him",
                "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]},
                "local_reference_images": [
                    "ProductImages/raw/Bracelets/The Bandhan Bracelet For Him/1_body_portrait.png",
                    "ProductImages/raw/Bracelets/The Bandhan Bracelet For Him/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": people_prompt(
                    hero,
                    "hero, adult brother receiving rakhi at a bright home celebration, smiling warmly while his wrist rests naturally near a rakhi thali",
                    "Solo fair-skinned Indian adult man, clean festive kurta, brotherly Raksha Bandhan moment",
                    "the yellow gold diamond bracelet for him",
                    "bracelet size on the wrist",
                    "Bare fingers except the featured bracelet wrist; no watch, no rings, no chain, no pendant, no earrings, no other bracelet.",
                ),
            },
            "flatlay": {
                **flatlay,
                "alt": "unique rakhi gifts for brother 2026 flatlay with The Protector Evil Eye Rakhi",
                "caption": "Raksha Bandhan gifts for brother 2026 keepsake: The Protector Evil Eye Rakhi",
                "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]},
                "local_reference_images": [
                    "ProductImages/raw/Adjustable Bracelets/The Protector Evil Eye Rakhi/0_primary.png",
                    "ProductImages/raw/Adjustable Bracelets/The Protector Evil Eye Rakhi/2_side_1.png",
                    "ProductImages/raw/Adjustable Bracelets/The Protector Evil Eye Rakhi/4_close_up.png",
                ],
                "ref_roles": ["primary", "side", "close_up"],
                "prompt": (
                    f"Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\n"
                    "Unique rakhi gifts for brother 2026 top-down flatlay. Flatlay setting ID: rakhi-thali. "
                    "Surface and props: brass rakhi thali, roli chawal bowl, diya, marigold petals, sweets, blank cream gift card, no readable text. "
                    "The identical Protector Evil Eye Rakhi from @img1, @img2 and @img3 rests naturally on the thali at true PDP scale. "
                    f"Product dimensions from PDP: {flatlay['size_prompt_note']}. Do not enlarge for visibility. "
                    "Full rakhi visible, yellow gold evil eye motif and thread details, 100 percent identical design, zero distortion, HD metal detail.\n\n"
                    "Props stay secondary. No people, no hands, no logos, no readable text.\n\n"
                    "Avoid: hands, people, floating overlays, cutouts, incorrect rakhi design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI."
                ),
            },
            "lifestyle": {
                **lifestyle,
                "alt": "unique rakhi gifts for brother 2026 lifestyle with The Talisman Evil Eye Pendant For Him",
                "caption": "Raksha Bandhan gifts for brother 2026 vibe: The Talisman Evil Eye Pendant For Him",
                "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]},
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Talisman Evil Eye Pendant For Him/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Talisman Evil Eye Pendant For Him/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": people_prompt(
                    lifestyle,
                    "lifestyle, adult brother standing near a window after the rakhi ceremony with a blank gift card and soft festive decor in the background",
                    "Solo fair-skinned Indian adult man in a simple kurta, relaxed and smiling",
                    "the yellow gold and evil eye pendant for him",
                    "pendant size on the neck",
                    "Hands and wrists hidden below frame; no watch, no rings, no bracelet, no chain other than the pendant chain, no earrings, no other necklace.",
                ),
            },
        },
    }

    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json(f"output/publish_configs/rank94.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    write_json(f"output/{PREFIX}_Checklist_v2.md", {"status": "drafted", "rank": 94, "slug": sections["meta"]["slug"]})
    print(f"wrote {PREFIX} sections/config/prompts")


if __name__ == "__main__":
    main()
