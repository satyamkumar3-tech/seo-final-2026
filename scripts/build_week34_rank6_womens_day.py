#!/usr/bin/env python3
"""Build Week 3-4 Rank 6 Womens Day wishes assets."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week34_Rank6_WomensDayWishes"
FILMIC_STYLE = (
    "Visual style: subtle cinematic film grain / analog grain, Kodak Portra color science, "
    "gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, "
    "editorial color grading, natural dynamic range, filmic contrast."
)


def load_csv(path: str) -> dict[str, dict[str, str]]:
    with (ROOT / path).open(newline="", encoding="utf-8-sig") as f:
        return {row["Design Name"].strip(): row for row in csv.DictReader(f)}


def product(rows: dict[str, dict[str, str]], name: str) -> dict[str, str]:
    row = rows[name]
    matches = sorted((ROOT / "ProductImages/seo images").glob(f"*/{name}.png"))
    if not matches:
        raise SystemExit(f"Missing SEO carousel image for {name}")
    return {"code": row["Design Code"], "name": name, "url": row["Link"], "png": str(matches[0].relative_to(ROOT))}


def consolidated(rows: dict[str, dict[str, str]], name: str) -> dict[str, object]:
    row = rows[name]
    size_note = (
        row["size_prompt_note"]
        or f"product_height_mm={row['height_mm']}; product_width_mm={row['width_mm']}; these are product dimensions, not face-size instructions"
    )
    size_note = size_note.replace("face_height_mm", "product_height_mm").replace("face_width_mm", "product_width_mm")
    if "product dimensions" not in size_note:
        size_note += "; these are product dimensions, not face-size instructions"
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


def raw_image(category: str, name: str, filename: str) -> str:
    path = ROOT / "ProductImages/raw" / category / name / filename
    if not path.exists():
        raise SystemExit(f"Missing raw reference {path}")
    return str(path.relative_to(ROOT))


def write_json(path: str, data: object) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prompt_people(
    *,
    occasion: str,
    scene: str,
    product_name: str,
    product: dict[str, object],
    body_part: str,
    extra_negatives: str = "",
) -> str:
    return (
        f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} {occasion}, "
        f"{scene}. Exactly one jewellery wearer only. Casting: fair-skinned Indian adult woman only, "
        "light wheatish to fair North Indian or urban Indian complexion, clear fair skin tones. "
        "Shot on DSLR, natural skin texture, 85mm candid lifestyle look, 16:9 full frame with safe margins.\n\n"
        f"The woman physically wears {product_name} from @img1 body_image and @img2 design only on her {body_part}. "
        "GENDER LOCK: Female product on adult woman only. "
        f"Product dimensions from PDP: {product['size_prompt_note']}. "
        "These values describe only the jewellery product dimensions, never a face or body measurement. "
        f"Keep the jewellery size on the person like @img1 body_image worn {body_part} scale: subtle real PDP size, not enlarged. "
        "Use @img2 only for jewellery design.\n\n"
        "Replicate the jewellery exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. "
        "This is the single and only jewellery object in the entire image. Other visible people, if any, wear absolutely no jewellery. "
        "No readable text anywhere. Any card, tag, notebook, laptop, or phone screen must be completely blank.\n\n"
        "Avoid: floating jewellery overlay, giant product collage, product cutout over people, packshot composited on lifestyle photo, "
        "oversized jewellery, extra jewellery, extra earrings, extra necklace, extra rings, extra bracelets, watch, bangle, "
        "wrong gender wearer, second jewellery wearer, cropped face, cropped head, readable text, letters, numbers, logo, "
        "dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow"
        + (f", {extra_negatives}" if extra_negatives else "")
        + "."
    )


def prompt_flatlay(
    *,
    occasion: str,
    setting: str,
    setting_prompt: str,
    product_name: str,
    product: dict[str, object],
) -> str:
    return (
        "STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. Photoreal high-end jewellery still life, top-down editorial product flatlay. "
        f"{FILMIC_STYLE}\n\n"
        f"{occasion} top-down flatlay. Flatlay setting ID: {setting}. Surface and props: {setting_prompt}. "
        f"The identical {product_name} from @img1, @img2 and @img3 rests naturally on the surface at true PDP scale. "
        f"Product dimensions from PDP: {product['size_prompt_note']}. "
        "These values describe only the jewellery product dimensions, never a face or body measurement. "
        "Do not enlarge for visibility. Full jewellery visible, 100 percent identical design, zero distortion, HD metal and stone detail.\n\n"
        "Props stay secondary. No people, no hands, no logos, no readable text, no letters, no numbers, no other jewellery.\n\n"
        "Avoid: hands, people, floating overlays, cutouts, incorrect jewellery design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI."
    )


def main() -> None:
    product_rows = load_csv("Seo Products - final products (1).csv")
    detail_rows = load_csv("Seo Products - consolidated.csv")

    sections = {
        "meta": {
            "title": "Happy Womens Day Wishes Quotes 2027",
            "slug": "happy-womens-day-wishes-quotes-2027",
            "meta_desc": "Happy Womens Day wishes quotes 2027 with greetings, inspirational lines, thoughts, captions, messages, and special words to celebrate women with respect.",
            "focus_kw": "happy womens day wishes quotes",
            "yoast_title": "Happy Womens Day Wishes Quotes 2027",
        },
        "intro": [
            "Happy Womens Day wishes quotes feel best when they sound respectful, warm, and personal. International Womens Day is observed every year on March 8, so this 2027 collection gives you ready lines for cards, WhatsApp, Instagram captions, office greetings, and thoughtful notes.",
            "TL;DR: Choose inspirational Womens Day quotes for public posts, short greetings for WhatsApp, special lines for cards, and a personal thank you when you want the message to feel truly sincere.",
        ],
        "sections": [
            {
                "key": "main",
                "h2": "Happy Womens Day Wishes Quotes",
                "lines": [
                    "Happy Womens Day. May your courage, kindness, and dreams keep finding room to grow.",
                    "Wishing you a Womens Day filled with respect, joy, and every opportunity you deserve.",
                    "Happy Womens Day to every woman who leads with strength and still makes space for care.",
                    "May this day remind you that your voice, work, and presence matter deeply.",
                    "Happy Womens Day 2027. May your path feel lighter and your confidence feel louder.",
                    "Here is to women who build, heal, teach, lead, protect, and inspire every day.",
                    "Wishing you a day that celebrates your brilliance without asking you to be anything less than yourself.",
                    "Happy Womens Day. May you be surrounded by people who respect your dreams and honour your choices.",
                    "To every woman making life better in quiet and powerful ways, you are celebrated today.",
                    "May your strength be seen, your effort be valued, and your joy be protected.",
                ],
            },
            {
                "key": "thought",
                "h2": "Thought on Womens Day",
                "lines": [
                    "A thoughtful Womens Day message begins with respect before praise.",
                    "Celebrate women not only for what they give, but for who they are.",
                    "Equality becomes real when admiration turns into action.",
                    "A woman does not need to shrink her dreams to make others comfortable.",
                    "The best Womens Day thought is simple: listen, value, support, and share space.",
                    "Strength is not always loud. Sometimes it is the quiet decision to continue.",
                    "Progress grows when every woman gets safety, opportunity, dignity, and choice.",
                    "Honouring women means respecting their ambition as much as their kindness.",
                    "Womens Day is a reminder to celebrate achievement and question unfair limits.",
                    "A better world begins when every girl is taught that her future is fully hers.",
                ],
            },
            {
                "key": "inspirational",
                "h2": "Inspirational Womens Day Quotes",
                "lines": [
                    "You do not need permission to become the woman you already know you can be.",
                    "Let your dreams be louder than every doubt placed in your way.",
                    "A confident woman is not asking to be understood by everyone. She is choosing to stand fully in herself.",
                    "Your strength is not measured by how much you carry, but by how honestly you choose your path.",
                    "Every step you take with self respect becomes a message to the next woman watching.",
                    "Rise gently, rise boldly, rise in the way that keeps your spirit whole.",
                    "The world changes when women stop asking whether their ambition is too much.",
                    "You are allowed to be soft, powerful, thoughtful, and unstoppable at the same time.",
                    "Do not make your light smaller to keep the room comfortable.",
                    "Your courage may feel quiet today, but it is still courage.",
                    "A woman in her truth becomes a kind of hope for everyone around her.",
                    "Keep choosing growth, even when it asks you to leave old versions behind.",
                ],
            },
            {
                "key": "greetings",
                "h2": "Womens Day Greetings",
                "lines": [
                    "Happy Womens Day. Wishing you respect, happiness, good health, and beautiful success.",
                    "Warm Womens Day greetings to you and every woman who inspires your life.",
                    "May this Womens Day bring appreciation, encouragement, and new confidence your way.",
                    "Sending heartfelt greetings for a day that celebrates your strength and grace.",
                    "Happy Womens Day. May your work be valued and your dreams be supported.",
                    "Wishing you a day full of kindness, pride, and well deserved celebration.",
                    "Happy Womens Day to someone who brings light, courage, and care into every space.",
                    "May today remind you how deeply you are respected and appreciated.",
                    "Sending warm wishes for Womens Day 2027 and every strong day after it.",
                    "Happy Womens Day. May you keep shining in your own honest style.",
                ],
            },
            {
                "key": "unique",
                "h2": "Unique Womens Day Quotes",
                "lines": [
                    "A woman is not a chapter in someone elses story. She is the author of her own.",
                    "Her power is not in being perfect. It is in being fully present.",
                    "Celebrate the woman who learned to clap for herself before the world noticed.",
                    "She carries history, hope, questions, laughter, and tomorrow in one brave heart.",
                    "A woman who knows her worth changes the tone of every room she enters.",
                    "Her dreams are not decoration. They are direction.",
                    "Some women bloom loudly. Some bloom quietly. Both change the garden.",
                    "She is not difficult. She is detailed, determined, and done with shrinking.",
                    "A woman becomes unforgettable when she stops editing her strength.",
                    "Let her joy be as protected as her resilience is praised.",
                ],
            },
            {
                "key": "special",
                "h2": "Special Womens Day Quotes",
                "lines": [
                    "You are special not because you do everything, but because you bring heart to what you choose.",
                    "Happy Womens Day to a woman whose kindness has strength inside it.",
                    "May you always remember how much light your presence brings.",
                    "Your courage has helped people in ways you may never fully know.",
                    "The world is better because you care, speak, build, and keep going.",
                    "You deserve appreciation that is clear, respectful, and everyday.",
                    "Happy Womens Day to someone whose grace never hides her power.",
                    "May your life return the warmth you have given to others.",
                    "Your dreams are worthy of time, space, and serious support.",
                    "Today is a celebration of you, but your value has never needed a date.",
                ],
            },
            {
                "key": "positive",
                "h2": "Positive Happy Womens Day Quotes",
                "lines": [
                    "Happy Womens Day. Keep believing in the version of you that feels most alive.",
                    "May today bring fresh confidence, honest smiles, and hopeful beginnings.",
                    "You are growing beautifully, even on days that feel slow.",
                    "Let this Womens Day remind you that progress can be gentle and still be powerful.",
                    "Your kindness is not weakness. It is one of your strongest choices.",
                    "May you meet this year with courage, calm, and clear self respect.",
                    "There is power in every step you take toward your own happiness.",
                    "Happy Womens Day. May your future feel open, supported, and bright.",
                    "You bring value by being yourself, not by proving yourself every minute.",
                    "Celebrate how far you have come and how much more you are allowed to become.",
                ],
            },
            {
                "key": "short",
                "h2": "Short Womens Day Wishes",
                "lines": [
                    "Happy Womens Day.",
                    "Stay strong and keep shining.",
                    "You are deeply appreciated.",
                    "Wishing you joy and respect.",
                    "Keep rising in your own way.",
                    "Your voice matters.",
                    "Celebrate yourself today.",
                    "Proud of your strength.",
                    "May you always feel valued.",
                    "Happy Womens Day 2027.",
                ],
            },
            {
                "key": "colleagues",
                "h2": "Womens Day Messages for Colleagues",
                "lines": [
                    "Happy Womens Day. Your professionalism, ideas, and calm leadership are truly valued.",
                    "Wishing you a day of appreciation for the excellence you bring to our team.",
                    "Thank you for showing that strength at work can be thoughtful, collaborative, and clear.",
                    "Happy Womens Day to a colleague whose contribution makes the workplace better.",
                    "May your efforts be recognised, your growth supported, and your ideas heard.",
                    "Working with you is a reminder that talent and kindness can lead together.",
                    "Happy Womens Day. May every goal you are building toward move closer this year.",
                    "Your dedication brings confidence to the team and inspiration to everyone around you.",
                    "Wishing you respect, progress, and many well deserved wins ahead.",
                    "Happy Womens Day to all women colleagues who make work more meaningful and humane.",
                ],
            },
            {
                "key": "captions",
                "h2": "Womens Day Captions",
                "lines": [
                    "Strong women, honest dreams, brighter world.",
                    "Celebrating courage in every form.",
                    "Her story, her strength, her shine.",
                    "Respect women beyond one day.",
                    "Grace with courage, power with heart.",
                    "Womens Day 2027 with gratitude.",
                    "For the women who keep going.",
                    "Soft heart, strong spine.",
                    "Celebrating women, today and always.",
                    "Here is to every fearless beginning.",
                ],
            },
            {
                "key": "thank_you",
                "h2": "Thank You Womens Day Wishes",
                "lines": [
                    "Thank you for being a woman who inspires strength without losing warmth.",
                    "I am grateful for your guidance, kindness, and steady belief in others.",
                    "Thank you for showing what courage looks like in everyday life.",
                    "Your support has made more difference than you may realise.",
                    "Happy Womens Day, and thank you for being such a meaningful presence.",
                    "Thank you for leading with honesty, care, and quiet confidence.",
                    "I hope today gives back some of the appreciation you give so freely.",
                    "Thank you for making people around you feel seen and capable.",
                    "Your strength has taught me more than any speech could.",
                    "Happy Womens Day. Thank you for being exactly who you are.",
                ],
            },
        ],
        "faqs": [
            ["What are good happy Womens Day wishes quotes for 2027?", "Good happy Womens Day wishes quotes for 2027 should sound respectful, sincere, and easy to personalize. Choose a line about courage, dignity, appreciation, or dreams, then add the persons name or one real quality you admire."],
            ["What is a meaningful thought on Womens Day?", "A meaningful thought on Womens Day is that respect should continue beyond one celebration. Womens Day is a reminder to value womens voices, choices, safety, work, leadership, and everyday contributions with consistency."],
            ["What are inspirational Womens Day quotes for Instagram?", "Inspirational Womens Day quotes for Instagram work best when they are short and clear. Use lines about confidence, ambition, equality, and self respect, then pair them with a warm caption or a simple photo."],
            ["How do I write Womens Day greetings for colleagues?", "For colleagues, keep Womens Day greetings professional and warm. Appreciate their contribution, leadership, teamwork, or ideas without making the message too personal. A short note of respect is usually enough."],
            ["What can I write on a Womens Day card?", "On a Womens Day card, write one wish, one specific appreciation, and one blessing for the year ahead. Keep the tone kind and direct so the message feels personal rather than copied."],
        ],
    }

    carousel_names = [
        "The Asya Huggie Earrings",
        "The Haily Ring",
        "The Shining Star Bracelet",
        "The Thyvarne Pendant",
        "The Malocchio Charm Holder Bracelet",
        "The Estrella Oval Bangle",
    ]
    hero = consolidated(detail_rows, "The Teshvarya Pendant")
    flatlay = consolidated(detail_rows, "The Rafia Ring")
    lifestyle = consolidated(detail_rows, "The Aleena Huggie Earrings")
    cfg = {
        "rank": "Week3-4 Rank 6",
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-womensdaywishes",
        "occasion_year": "Womens Day 2027",
        "carousel_alt_prefix": "happy Womens Day wishes quotes 2027 gift idea",
        "gift_h2": "Womens Day Gift Ideas",
        "gift_blurb": "If your Womens Day wish is going with a keepsake, choose jewellery that feels wearable, thoughtful, and personal. These BlueStone picks keep the gift idea elegant without turning the message into a product list.",
        "conclusion_html": "Happy Womens Day wishes quotes become memorable when they sound real. Pick a line that matches the person, add one honest detail, and send it with respect that lasts beyond the day.",
        "schema_keywords": [
            "happy womens day wishes quotes",
            "thought on womens day",
            "inspirational womens day quotes",
            "womens day greetings",
            "unique womens day quotes",
            "special womens day quotes",
            "positive happy womens day quotes",
        ],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [product(product_rows, name) for name in carousel_names],
        "flatlay_insert_h2": "Inspirational Womens Day Quotes",
        "lifestyle_insert_h2": "Womens Day Greetings",
        "more_reads_html": 'Read more heartfelt lines in <a href="https://blog.bluestone.com/mother-daughter-quotes-2026/">mother daughter quotes</a>, <a href="https://blog.bluestone.com/thank-you-note-to-teacher-2026/">thank you note to teacher</a>, <a href="https://blog.bluestone.com/friendship-day-photos-2026/">friendship messages</a>, and <a href="https://blog.bluestone.com/new-year-wishes-for-love-2026/">New Year wishes for love</a>.',
        "how_to_html": 'International Womens Day is observed on March 8 every year. Choose a respectful quote for public posts, a warm greeting for WhatsApp, and a specific thank you when you are writing to someone close.',
        "faq_h2": "Frequently Asked Questions about Womens Day Wishes",
        "min_lines": 100,
    }
    prompts = {
        "rank": "Week3-4 Rank 6",
        "slug": sections["meta"]["slug"],
        "primary_kw": sections["meta"]["focus_kw"],
        "output_prefix": PREFIX,
        "caption_occasion": "Womens Day wishes",
        "caption_year": "2027",
        "flatlay_setting": "study-desk",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/happy-womens-day-wishes-quotes-hero-2027.webp",
            "flatlay": "output/magnific_generated/happy-womens-day-wishes-quotes-flatlay-2027.webp",
            "lifestyle": "output/magnific_generated/happy-womens-day-wishes-quotes-lifestyle-2027.webp",
        },
        "media_titles": {
            "hero": "happy Womens Day wishes quotes 2027 Hero",
            "flatlay": "happy Womens Day wishes quotes 2027 Flatlay",
            "lifestyle": "happy Womens Day wishes quotes 2027 Lifestyle",
        },
        "schema_keywords": cfg["schema_keywords"],
        "slots": {
            "hero": {
                **hero,
                "alt": "happy Womens Day wishes quotes 2027 hero with The Teshvarya Pendant",
                "caption": "Womens Day wishes 2027 mood: The Teshvarya Pendant",
                "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]},
                "local_reference_images": [
                    raw_image("Pendants", "The Teshvarya Pendant", "1_body_portrait.png"),
                    raw_image("Pendants", "The Teshvarya Pendant", "0_primary.png"),
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": prompt_people(
                    occasion="Happy Womens Day wishes quotes 2027 hero",
                    scene="solo fair-skinned Indian adult woman leader seated at a sunlit study desk, smiling softly while holding a completely blank cream note card near a teacup, full face visible, neck and pendant clearly visible, elegant ivory kurta, calm respectful celebration mood",
                    product_name=hero["name"],
                    product=hero,
                    body_part="neck",
                    extra_negatives="large pendant, pendant covering chest, unreadable card with markings",
                ),
            },
            "flatlay": {
                **flatlay,
                "alt": "happy Womens Day wishes quotes 2027 flatlay with The Rafia Ring",
                "caption": "Womens Day wishes 2027 vibe: The Rafia Ring",
                "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]},
                "local_reference_images": [
                    raw_image("Rings", "The Rafia Ring", "0_primary.png"),
                    raw_image("Rings", "The Rafia Ring", "2_front.png"),
                    raw_image("Rings", "The Rafia Ring", "5_angle.png"),
                ],
                "ref_roles": ["primary", "front", "angle"],
                "prompt": prompt_flatlay(
                    occasion="Happy Womens Day wishes quotes 2027",
                    setting="study-desk",
                    setting_prompt="a matte walnut study desk, closed plain linen notebook with no title, blank cream card, simple pen without branding, soft daylight from window, one ceramic teacup, no text",
                    product_name=flatlay["name"],
                    product=flatlay,
                ),
            },
            "lifestyle": {
                **lifestyle,
                "alt": "happy Womens Day wishes quotes 2027 lifestyle with The Aleena Huggie Earrings",
                "caption": "Womens Day wishes 2027 look: The Aleena Huggie Earrings",
                "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]},
                "local_reference_images": [
                    raw_image("Earrings", "The Aleena Huggie Earrings", "1_body_portrait.png"),
                    raw_image("Earrings", "The Aleena Huggie Earrings", "0_primary.png"),
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": prompt_people(
                    occasion="Happy Womens Day wishes quotes 2027 lifestyle",
                    scene="solo fair-skinned Indian adult woman near a bright home office window, writing on a completely blank cream note card, full head visible and both ears visible, warm thoughtful smile, hands low in frame, simple ivory blouse, no necklace and wrists out of frame",
                    product_name=lifestyle["name"],
                    product=lifestyle,
                    body_part="ear",
                    extra_negatives="necklace, bracelet, ring, watch, readable writing on card",
                ),
            },
        },
    }

    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json("output/publish_configs/week34_rank6.json", cfg)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    checklist = """# Blog SEO + AEO/GEO Checklist v2, Week 3-4 Rank 6

Article: Happy Womens Day Wishes Quotes 2027
Status: Draft assets prepared
Date: 2026-07-28

## Gates
- [x] Primary keyword: happy womens day wishes quotes
- [x] Optimize treated as New
- [x] Fresh slug: happy-womens-day-wishes-quotes-2027
- [x] International Womens Day year rolled forward to 2027
- [x] Carousel products from ProductImages/seo images only
- [x] Type 3 hero and lifestyle use body_image plus design refs
- [x] Product dimension wording uses product dimensions, not face size
- [x] Filmic prompt language included
- [ ] WordPress post published
- [ ] Type 3 images generated and patched
- [ ] Live URL verified
"""
    (ROOT / f"output/{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
