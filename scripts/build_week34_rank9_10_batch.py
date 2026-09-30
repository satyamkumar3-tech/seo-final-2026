#!/usr/bin/env python3
"""Build Week 3-4 Rank 9 and Rank 10 assets."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILMIC_STYLE = (
    "Visual style: subtle cinematic film grain / analog grain, Kodak Portra color science, "
    "gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, "
    "editorial color grading, natural dynamic range, filmic contrast."
)
NO_SCREEN_RULE = (
    "No visible phones, laptops, tablets, TVs, or blank screens anywhere in the image. "
    "No poster card, no large blank paper, no upright rectangle, no white screen-like prop, no board, and no placard facing camera. "
    "Use warm physical props instead: wrapped gift box, flowers, diya, ceramic cup, brass bowl, tray, ribbon, folded fabric, or a closed book blurred in the background. "
    "If any device is unavoidable, show only the back or edge with the screen out of frame."
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
        f"{NO_SCREEN_RULE} No readable text anywhere. Any card, tag, notebook, label, package, paper, or prop must be blank or turned away from camera.\n\n"
        f"The woman physically wears {product_name} from @img1 body_image and @img2 design only on her {body_part}. "
        "GENDER LOCK: Female product on adult woman only. "
        f"Product dimensions from PDP: {product['size_prompt_note']}. "
        "These values describe only the jewellery product dimensions, never a face or body measurement. "
        f"Keep the jewellery size on the person like @img1 body_image worn {body_part} scale: subtle real PDP size, not enlarged. "
        "Use @img2 only for jewellery design.\n\n"
        "Replicate the jewellery exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. "
        "This is the single and only jewellery object in the entire image. Other visible people, if any, wear absolutely no jewellery.\n\n"
        "Avoid: visible phone, phone screen, laptop, tablet, TV, blank screen, floating jewellery overlay, giant product collage, "
        "product cutout over people, packshot composited on lifestyle photo, oversized jewellery, extra jewellery, extra earrings, "
        "extra necklace, extra rings, extra bracelets, watch, bangle, wrong gender wearer, second jewellery wearer, cropped face, "
        "cropped head, readable text, letters, numbers, logo, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow"
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
        f"{NO_SCREEN_RULE} "
        f"The identical {product_name} from @img1, @img2 and @img3 rests naturally on the surface at true PDP scale. "
        f"Product dimensions from PDP: {product['size_prompt_note']}. "
        "These values describe only the jewellery product dimensions, never a face or body measurement. "
        "Do not enlarge for visibility. Full jewellery visible, 100 percent identical design, zero distortion, HD metal and stone detail.\n\n"
        "Props stay secondary. No people, no hands, no logos, no readable text, no letters, no numbers, no other jewellery.\n\n"
        "Avoid: phones, laptops, tablets, TVs, blank screens, hands, people, floating overlays, cutouts, incorrect jewellery design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI."
    )


def checklist(prefix: str, rank: int, title: str, kw: str, optimize: bool) -> None:
    opt_line = "Optimize treated as New" if optimize else "New row published as New"
    (ROOT / f"output/{prefix}_Checklist_v2.md").write_text(
        f"# Blog SEO + AEO/GEO Checklist v2, Week 3-4 Rank {rank}\n\n"
        f"Article: {title}\nStatus: Draft assets prepared\n\n"
        f"- [x] Primary keyword: {kw}\n"
        f"- [x] {opt_line}\n"
        "- [x] Type 3 hero and lifestyle use body_image plus design refs\n"
        "- [x] Product dimension wording uses product dimensions, not face size\n"
        "- [x] Type 3 prompts avoid visible phones, laptops, tablets, TVs, and blank screens\n"
        "- [ ] WordPress post published\n"
        "- [ ] Type 3 images generated and patched\n"
        "- [ ] Live URL verified\n",
        encoding="utf-8",
    )


def build_rank9(product_rows: dict[str, dict[str, str]], detail_rows: dict[str, dict[str, str]]) -> None:
    prefix = "Week34_Rank9_DiwaliSlogan"
    sections = {
        "meta": {
            "title": "Slogan on Diwali 2026",
            "slug": "slogan-on-diwali-2026",
            "meta_desc": "Slogan on Diwali 2026 with short, catchy, eco friendly, poster, school, social media, and festival slogans for cards, speeches, campaigns, and captions.",
            "focus_kw": "slogan on diwali",
            "yoast_title": "Slogan on Diwali 2026",
        },
        "intro": [
            "A strong slogan on Diwali should be short enough to remember and warm enough to carry the spirit of the festival. Use these 2026 Diwali slogans for posters, school activities, captions, community campaigns, greeting cards, and eco friendly awareness.",
            "TL;DR: Choose a two to eight word line for a poster, a meaningful slogan for school work, an eco friendly line for awareness, and a festive slogan when you want the message to feel bright and positive.",
        ],
        "sections": [
            {"key": "main", "h2": "Slogan on Diwali", "lines": [
                "Light a lamp, spread a smile.",
                "Diwali shines when hearts are kind.",
                "Let every diya carry hope.",
                "Celebrate Diwali with love and light.",
                "Bright homes, brighter hearts.",
                "Diwali is light, joy, and togetherness.",
                "Glow with goodness this Diwali.",
                "A diya of hope can brighten many lives.",
                "Celebrate light, choose kindness.",
                "Let Diwali begin with gratitude.",
                "Lights outside, peace inside.",
                "Diwali glows best with happy hearts.",
            ]},
            {"key": "short", "h2": "Short Diwali Slogans", "lines": [
                "Light wins.",
                "Glow with joy.",
                "Shine with kindness.",
                "Diyas over darkness.",
                "Celebrate the light.",
                "Peace begins within.",
                "Choose joy today.",
                "Bright hearts rise.",
                "Hope lights homes.",
                "Let love glow.",
                "Festival of light.",
                "Sparkle with care.",
            ]},
            {"key": "poster", "h2": "Diwali Poster Slogans", "lines": [
                "Make your poster shine with a message of hope.",
                "One diya can turn a dark corner bright.",
                "Celebrate Diwali with clean homes and kind hearts.",
                "Let your lights speak of peace, joy, and unity.",
                "Decorate the world with love, not noise.",
                "This Diwali, brighten lives beyond your home.",
                "A beautiful Diwali begins with a thoughtful heart.",
                "Light lamps, share sweets, protect smiles.",
                "May every colour of rangoli welcome happiness.",
                "Diwali is brighter when everyone is included.",
                "Keep your poster simple, warm, and full of light.",
                "Spread sparkle, not smoke.",
            ]},
            {"key": "eco", "h2": "Eco Friendly Diwali Slogans", "lines": [
                "Celebrate Diwali with diyas, not pollution.",
                "Let the sky stay clear and the heart stay bright.",
                "Green Diwali, clean Diwali.",
                "Choose lights that do not dim nature.",
                "A peaceful Diwali is a beautiful Diwali.",
                "Say yes to lamps, flowers, sweets, and clean air.",
                "Celebrate tradition without harming tomorrow.",
                "Less smoke, more sparkle.",
                "A green Diwali is a gift to the next morning.",
                "Protect nature while celebrating light.",
                "Let happiness glow without noise.",
                "This Diwali, make the planet smile too.",
            ]},
            {"key": "school", "h2": "Diwali Slogans for School", "lines": [
                "Diwali teaches us that good always rises.",
                "Light the lamp of knowledge and kindness.",
                "A clean school, a bright Diwali.",
                "Celebrate safely, study sincerely, smile freely.",
                "Let every student shine like a diya.",
                "Good thoughts are the brightest lights.",
                "Share sweets, share respect, share joy.",
                "Diwali reminds us to choose truth over darkness.",
                "A festival becomes meaningful when we learn from it.",
                "Light up minds with hope and harmony.",
                "Celebrate culture with care.",
                "Let every classroom glow with unity.",
            ]},
            {"key": "english", "h2": "Diwali Slogan in English", "lines": [
                "May Diwali light every path with hope.",
                "Celebrate light, love, and fresh beginnings.",
                "Let goodness shine brighter than fireworks.",
                "A joyful heart is the best Diwali decoration.",
                "Light a diya, lift a spirit.",
                "Diwali is a promise that darkness cannot last.",
                "Share sweets, share smiles, share kindness.",
                "Let every home glow with peace.",
                "The real light of Diwali is compassion.",
                "Brighten your world with gratitude.",
                "Celebrate safely and shine gracefully.",
                "Let Diwali make your heart generous.",
            ]},
            {"key": "social", "h2": "Diwali Slogans for Social Media", "lines": [
                "Posting light, peace, and festive joy.",
                "Diyas, smiles, and a heart full of gratitude.",
                "This Diwali, let kindness trend.",
                "Glow mode on, stress mode off.",
                "Festival lights and family nights.",
                "Keeping it bright, warm, and grateful.",
                "Less noise, more love.",
                "A little sparkle, a lot of meaning.",
                "Diwali mood: peaceful and golden.",
                "Let the feed glow with good wishes.",
                "Celebrating light in every small moment.",
                "Good vibes, glowing diyas, grateful heart.",
            ]},
            {"key": "safe", "h2": "Safe Diwali Slogans", "lines": [
                "Celebrate safely, shine happily.",
                "A careful Diwali is a joyful Diwali.",
                "Keep lamps bright and children safe.",
                "Safety first, celebration always.",
                "Light diyas with care and celebrate with love.",
                "A safe home makes the festival brighter.",
                "Enjoy sweets, smiles, and safe celebrations.",
                "Protect little hands and happy hearts.",
                "Let caution be part of the celebration.",
                "Celebrate with care, remember with joy.",
            ]},
            {"key": "hindi_english", "h2": "Simple Diwali Slogans for Cards", "lines": [
                "May your Diwali glow with blessings.",
                "Wishing you light, laughter, and love.",
                "A bright Diwali for a beautiful heart.",
                "May joy enter with every diya.",
                "Celebrate the festival with a grateful soul.",
                "Let this card carry warmth and light.",
                "May peace sit beside every lamp you light.",
                "Sending festive glow and happy thoughts.",
                "May your home shine with love.",
                "A sweet Diwali wish from my heart.",
            ]},
        ],
        "faqs": [
            ["What is the best slogan on Diwali?", "The best slogan on Diwali is short, positive, and easy to remember. A simple line like Light a lamp, spread a smile works well because it carries the festival message without sounding complicated."],
            ["How do I write a Diwali slogan for school?", "To write a Diwali slogan for school, focus on light, knowledge, kindness, safety, culture, or eco friendly celebration. Keep the line short so it fits on a poster and is easy for students to say aloud."],
            ["What is an eco friendly Diwali slogan?", "An eco friendly Diwali slogan encourages clean air, less noise, and thoughtful celebration. Examples include Green Diwali, clean Diwali and Less smoke, more sparkle."],
            ["Can I use Diwali slogans for social media captions?", "Yes, Diwali slogans work well as social media captions when they are short and visual. Choose lines about diyas, gratitude, family, peace, festive glow, or kindness."],
            ["What makes a Diwali poster slogan effective?", "A Diwali poster slogan is effective when it is readable from a distance, emotionally clear, and connected to one idea such as light, safety, eco friendly celebration, unity, or joy."],
        ],
    }
    carousel_names = ["The Aagarna Pendant", "The Shining Star Bracelet", "The Ebony Ring", "The Pervinca Charm Holder Bracelet", "The Tapia Chain Bracelet", "The Anya Ring"]
    hero = consolidated(detail_rows, "The Thyvarne Pendant")
    flatlay = consolidated(detail_rows, "The Muricelle Bangle")
    lifestyle = consolidated(detail_rows, "The Asya Huggie Earrings")
    cfg = {
        "rank": "Week3-4 Rank 9",
        "sections_json": f"output/{prefix}_sections.json",
        "output_prefix": prefix,
        "carousel_id": "bs-cf-diwalislogan",
        "occasion_year": "Diwali 2026",
        "carousel_alt_prefix": "slogan on Diwali 2026 gift idea",
        "gift_h2": "Diwali Gift Ideas for Thoughtful Greetings",
        "gift_blurb": "If your Diwali slogan is going on a card or a small festive note, a keepsake can make the message feel more personal. These BlueStone pieces keep the gesture warm without taking attention away from the words.",
        "conclusion_html": "A slogan on Diwali works best when it is clear, positive, and easy to remember. Pick one line that matches your poster, card, campaign, or caption, then keep the design simple so the message shines.",
        "schema_keywords": ["slogan on diwali", "diwali slogan", "diwali slogan in english", "eco friendly diwali slogans", "diwali poster slogans", "short diwali slogans"],
        "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
        "products": [product(product_rows, name) for name in carousel_names],
        "flatlay_insert_h2": "Diwali Poster Slogans",
        "lifestyle_insert_h2": "Eco Friendly Diwali Slogans",
        "more_reads_html": 'Read more festive ideas in <a href="https://blog.bluestone.com/diwali-wishes-and-quotes-2026/">Diwali wishes and quotes</a>, <a href="https://blog.bluestone.com/diwali-quotes-for-instagram-2026/">Diwali captions for Instagram</a>, <a href="https://blog.bluestone.com/happy-diwali-poster-2026/">Diwali poster ideas</a>, and <a href="https://blog.bluestone.com/why-we-celebrate-diwali-2026/">why we celebrate Diwali</a>.',
        "how_to_html": "For a poster, choose the shortest slogan. For school work, choose a line about knowledge, kindness, or safety. For a campaign, use an eco friendly line. For a greeting card, pick a warm slogan and add the recipients name.",
        "faq_h2": "Frequently Asked Questions about Diwali Slogans",
        "min_lines": 90,
    }
    prompts = {
        "rank": "Week3-4 Rank 9",
        "slug": sections["meta"]["slug"],
        "primary_kw": sections["meta"]["focus_kw"],
        "output_prefix": prefix,
        "caption_occasion": "Diwali slogan",
        "caption_year": "2026",
        "flatlay_setting": "festive-mantel",
        "workflow": "Higgsfield CLI nano_banana_pro. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry. No visible screens/devices.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/slogan-on-diwali-hero-2026.webp",
            "flatlay": "output/magnific_generated/slogan-on-diwali-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/slogan-on-diwali-lifestyle-2026.webp",
        },
        "media_titles": {"hero": "slogan on Diwali 2026 Hero", "flatlay": "slogan on Diwali 2026 Flatlay", "lifestyle": "slogan on Diwali 2026 Lifestyle"},
        "schema_keywords": cfg["schema_keywords"],
        "slots": {
            "hero": {**hero, "alt": "slogan on Diwali 2026 hero with The Thyvarne Pendant", "caption": "Diwali slogan 2026 mood: The Thyvarne Pendant", "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]}, "local_reference_images": [raw_image("Pendants", "The Thyvarne Pendant", "1_body_portrait.png"), raw_image("Pendants", "The Thyvarne Pendant", "0_primary.png")], "ref_roles": ["body_image", "front_primary"], "prompt": prompt_people(occasion="Slogan on Diwali 2026 hero", scene="solo fair-skinned Indian adult woman in an ivory festive kurta arranging diyas and marigold flowers beside a small unbranded wrapped gift box and brass bowl, full face visible, neck and pendant clearly visible, warm home study corner, thoughtful creative festive mood", product_name=hero["name"], product=hero, body_part="neck", extra_negatives="poster card, blank rectangle, placard, poster text, blackboard text, large pendant, pendant covering chest")},
            "flatlay": {**flatlay, "alt": "slogan on Diwali 2026 flatlay with The Muricelle Bangle", "caption": "Diwali slogan 2026 vibe: The Muricelle Bangle", "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]}, "local_reference_images": [raw_image("Bangles", "The Muricelle Bangle", "0_primary.png"), raw_image("Bangles", "The Muricelle Bangle", "2_front.png"), raw_image("Bangles", "The Muricelle Bangle", "4_close_up.png")], "ref_roles": ["primary", "front", "close_up"], "prompt": prompt_flatlay(occasion="Slogan on Diwali 2026", setting="festive-mantel", setting_prompt="warm cream mantel with brass diya without markings, marigold petals, folded silk ribbon, blank cream poster card angled away, soft rangoli color blur, no text", product_name=flatlay["name"], product=flatlay)},
            "lifestyle": {**lifestyle, "alt": "slogan on Diwali 2026 lifestyle with The Asya Huggie Earrings", "caption": "Diwali slogan 2026 look: The Asya Huggie Earrings", "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]}, "local_reference_images": [raw_image("Earrings", "The Asya Huggie Earrings", "1_body_portrait.png"), raw_image("Earrings", "The Asya Huggie Earrings", "0_primary.png")], "ref_roles": ["body_image", "front_primary"], "prompt": prompt_people(occasion="Slogan on Diwali 2026 lifestyle", scene="solo fair-skinned Indian adult woman lighting a brass diya beside a small bowl of flowers and a closed blank notebook turned away from camera, full head visible and both ears visible, simple ivory festive blouse, no necklace and wrists out of frame, eco friendly Diwali mood", product_name=lifestyle["name"], product=lifestyle, body_part="ear", extra_negatives="necklace, bracelet, ring, watch, notebook text")},
        },
    }
    write_json(f"output/{prefix}_sections.json", sections)
    write_json("output/publish_configs/week34_rank9.json", cfg)
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    checklist(prefix, 9, "Slogan on Diwali 2026", "slogan on diwali", False)


def build_rank10(product_rows: dict[str, dict[str, str]], detail_rows: dict[str, dict[str, str]]) -> None:
    prefix = "Week34_Rank10_AdvanceHappyDiwali"
    sections = {
        "meta": {
            "title": "Advance Happy Diwali 2026 Wishes",
            "slug": "advance-happy-diwali-2026",
            "meta_desc": "Advance Happy Diwali 2026 wishes, messages, captions, quotes, and greetings to send early to family, friends, colleagues, clients, and loved ones today.",
            "focus_kw": "advance happy diwali",
            "yoast_title": "Advance Happy Diwali 2026 Wishes",
        },
        "intro": [
            "Advance Happy Diwali wishes are perfect when you want your greeting to arrive before the festival rush. Use this 2026 collection for family, friends, colleagues, clients, groups, cards, captions, and early festive messages.",
            "TL;DR: Send a short advance wish for WhatsApp, a warmer message for family, a respectful greeting for work, and a romantic or heartfelt line when the person deserves something more personal.",
        ],
        "sections": [
            {"key": "main", "h2": "Advance Happy Diwali Wishes", "lines": [
                "Advance Happy Diwali 2026. May your home glow with peace, joy, and prosperity.",
                "Sending early Diwali wishes filled with light, love, and good fortune.",
                "May this Diwali arrive with happiness before the lamps are even lit.",
                "Advance Happy Diwali. Wishing you a season of sweetness and success.",
                "May every diya you light bring warmth to your heart and blessings to your home.",
                "Sending you festive love early because good wishes should never wait.",
                "Advance Happy Diwali to you and your family. May the celebration be bright and beautiful.",
                "May this festival bring fresh hope, clear paths, and peaceful beginnings.",
                "Before the festive rush begins, wishing you a Diwali full of joy.",
                "May your Diwali be safe, sparkling, and full of meaningful moments.",
                "Advance Happy Diwali. Let the light arrive early and stay long.",
                "Wishing you prosperity, laughter, and a heart full of gratitude this Diwali.",
            ]},
            {"key": "short", "h2": "Short Advance Diwali Wishes", "lines": [
                "Advance Happy Diwali 2026.",
                "Early wishes, endless light.",
                "May your Diwali glow beautifully.",
                "Sending festive joy early.",
                "Light, love, and blessings.",
                "Have a bright Diwali ahead.",
                "Wishing you peace and sparkle.",
                "Diwali joy, sent early.",
                "May happiness arrive soon.",
                "Advance Diwali blessings.",
                "Stay blessed and glowing.",
                "Early festive hugs.",
            ]},
            {"key": "family", "h2": "Advance Happy Diwali Wishes for Family", "lines": [
                "Advance Happy Diwali to my family. May our home stay filled with love, laughter, and blessings.",
                "Wishing my family a Diwali that feels warm, safe, and beautifully peaceful.",
                "Before the festival begins, I want to thank you for being my greatest blessing.",
                "May our family celebrate this Diwali with health, togetherness, and sweet memories.",
                "Advance Happy Diwali. May every corner of our home glow with happiness.",
                "Wishing our family prosperity, protection, and endless reasons to smile.",
                "May the festival bring us closer and fill our home with gratitude.",
                "Sending early Diwali wishes to the people who make every festival meaningful.",
                "May our prayers be answered and our hearts stay united.",
                "Advance Happy Diwali to the family I am proud to call mine.",
            ]},
            {"key": "friends", "h2": "Advance Diwali Wishes for Friends", "lines": [
                "Advance Happy Diwali, my friend. May your life shine with luck and laughter.",
                "Sending early Diwali wishes because your friendship deserves the first light.",
                "May this Diwali bring you success, peace, and stories worth remembering.",
                "Advance Happy Diwali to the friend who makes celebrations louder and life lighter.",
                "May your festive season be full of sweets, smiles, and good news.",
                "Wishing you joy before the rush of messages begins.",
                "May every diya bring a new reason for you to smile.",
                "Advance Diwali wishes to one of my favourite people.",
                "Hope your Diwali is bright, safe, and beautifully chaotic in the best way.",
                "May friendship and festive lights keep your heart warm.",
            ]},
            {"key": "colleagues", "h2": "Advance Diwali Wishes for Colleagues", "lines": [
                "Advance Happy Diwali. Wishing you success, health, and a peaceful festive season.",
                "May this Diwali bring growth, clarity, and happiness to you and your family.",
                "Wishing you a bright Diwali ahead and a year full of good opportunities.",
                "Advance Diwali greetings. May your work and life both be blessed with balance.",
                "May the festival of lights bring positivity and prosperity to your path.",
                "Wishing you and your loved ones a safe and joyful Diwali celebration.",
                "Advance Happy Diwali. May this season bring renewed energy and happiness.",
                "May your festive break be restful, warm, and full of beautiful moments.",
                "Sending respectful Diwali wishes to you and your family in advance.",
                "May the coming days be bright with peace, progress, and celebration.",
            ]},
            {"key": "clients", "h2": "Advance Diwali Wishes for Clients", "lines": [
                "Advance Happy Diwali. Wishing you prosperity, success, and joyful celebrations.",
                "May the festival of lights bring growth, trust, and continued progress.",
                "Wishing you and your team a bright, safe, and prosperous Diwali.",
                "Advance Diwali greetings with sincere wishes for happiness and success.",
                "May this festive season open new opportunities and positive beginnings.",
                "Thank you for your trust. Wishing you a blessed Diwali in advance.",
                "May your business and home both shine with prosperity this Diwali.",
                "Sending warm advance Diwali wishes to you and your family.",
                "May the light of Diwali bring clarity, abundance, and good fortune.",
                "Wishing you a meaningful Diwali and a successful season ahead.",
            ]},
            {"key": "captions", "h2": "Advance Happy Diwali Captions", "lines": [
                "Sending Diwali light a little early.",
                "Advance wishes, festive heart.",
                "The glow begins before the day.",
                "Early Diwali mood is officially here.",
                "Diyas soon, joy already.",
                "Festive wishes before the rush.",
                "Let the light arrive early.",
                "Diwali countdown with a grateful heart.",
                "Early sparkle, endless blessings.",
                "Advance Happy Diwali from my home to yours.",
            ]},
            {"key": "romantic", "h2": "Advance Diwali Wishes for Love", "lines": [
                "Advance Happy Diwali, my love. May our bond glow brighter than every diya.",
                "Sending you my first Diwali wish because you are my favourite light.",
                "May this festival bring us closer, softer, and more grateful for each other.",
                "Advance Happy Diwali, sweetheart. You make every celebration feel warmer.",
                "Before the lamps are lit, my heart is already wishing happiness for you.",
                "May our love stay bright through every festive night and ordinary morning.",
                "Sending early Diwali hugs, prayers, and all my love.",
                "You are the light I am most thankful for this Diwali.",
                "Advance Happy Diwali to the person who makes my world glow.",
                "May our story keep shining with trust, joy, and beautiful memories.",
            ]},
            {"key": "status", "h2": "Advance Happy Diwali Status", "lines": [
                "Advance Happy Diwali 2026 to everyone celebrating.",
                "May the coming festival bring light to every home.",
                "Sending early Diwali blessings and warm wishes.",
                "Let the festive glow begin early.",
                "Wishing peace, prosperity, and happiness in advance.",
                "May your Diwali be safe, joyful, and bright.",
                "Early wishes for a beautiful festival of lights.",
                "Diwali is near and the heart is already glowing.",
                "Advance Happy Diwali from my family to yours.",
                "May every diya bring hope and every prayer bring peace.",
            ]},
        ],
        "faqs": [
            ["How do you wish Advance Happy Diwali?", "You can wish Advance Happy Diwali with a simple early greeting such as Advance Happy Diwali 2026. May your home glow with peace, joy, prosperity, and beautiful festive memories."],
            ["When should I send Advance Happy Diwali wishes?", "You can send Advance Happy Diwali wishes a few days before the festival, especially to people you may not message on the exact day. Early wishes work well for groups, colleagues, clients, and long distance loved ones."],
            ["What is a short Advance Diwali message?", "A short Advance Diwali message is: Advance Happy Diwali 2026. Wishing you light, love, prosperity, and a joyful celebration with your loved ones."],
            ["Can I send Advance Diwali wishes to clients?", "Yes, you can send Advance Diwali wishes to clients. Keep the tone respectful and professional, wish prosperity and success, and avoid overly casual or personal wording."],
            ["What should I write in an Advance Diwali caption?", "For an Advance Diwali caption, use a short line about early festive light, blessings, countdown, diyas, gratitude, or joy. Keep it simple so it works with photos or status posts."],
        ],
    }
    carousel_names = ["The Liza ring", "The Channing Bangle", "The Malocchio Charm Holder Bracelet", "The Ursa Hoop Earrings", "The Quinn Ring", "The Thaloria Pendant"]
    hero = consolidated(detail_rows, "The Protecteur Evil Eye Pendant")
    flatlay = consolidated(detail_rows, "The Estrella Oval Bangle")
    lifestyle = consolidated(detail_rows, "The Nettile Huggie Earrings")
    cfg = {
        "rank": "Week3-4 Rank 10",
        "sections_json": f"output/{prefix}_sections.json",
        "output_prefix": prefix,
        "carousel_id": "bs-cf-advancehappydiwali",
        "occasion_year": "Diwali 2026",
        "carousel_alt_prefix": "advance happy Diwali 2026 gift idea",
        "gift_h2": "Advance Diwali Gift Ideas",
        "gift_blurb": "When an early Diwali wish goes with a gift, keep the gesture meaningful and easy to wear. These BlueStone picks work well with a sealed envelope, a festive card, or a small wrapped box.",
        "conclusion_html": "Advance Happy Diwali wishes help your greeting arrive before the festive rush. Pick the line that fits your relationship, add a name if possible, and send it with warmth before the lamps are lit.",
        "schema_keywords": ["advance happy diwali", "advance happy diwali wishes", "advance diwali wishes", "advance happy diwali message", "advance happy diwali captions", "advance diwali greetings"],
        "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
        "products": [product(product_rows, name) for name in carousel_names],
        "flatlay_insert_h2": "Short Advance Diwali Wishes",
        "lifestyle_insert_h2": "Advance Diwali Wishes for Friends",
        "more_reads_html": 'Read more Diwali ideas in <a href="https://blog.bluestone.com/diwali-wishes-and-quotes-2026/">Diwali wishes and quotes</a>, <a href="https://blog.bluestone.com/romantic-diwali-wishes-for-lover-2026/">romantic Diwali wishes</a>, <a href="https://blog.bluestone.com/diwali-quotes-for-instagram-2026/">Diwali Instagram captions</a>, and <a href="https://blog.bluestone.com/slogan-on-diwali-2026/">Diwali slogans</a>.',
        "how_to_html": "Send short advance wishes to groups, warmer notes to family, respectful lines to colleagues or clients, and personal messages to loved ones. Add the persons name when you can, and avoid forwarding the same message to everyone.",
        "faq_h2": "Frequently Asked Questions about Advance Happy Diwali",
        "min_lines": 90,
    }
    prompts = {
        "rank": "Week3-4 Rank 10",
        "slug": sections["meta"]["slug"],
        "primary_kw": sections["meta"]["focus_kw"],
        "output_prefix": prefix,
        "caption_occasion": "Advance Happy Diwali",
        "caption_year": "2026",
        "flatlay_setting": "linen-bedside",
        "workflow": "Higgsfield CLI nano_banana_pro. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry. No visible screens/devices.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/advance-happy-diwali-hero-2026.webp",
            "flatlay": "output/magnific_generated/advance-happy-diwali-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/advance-happy-diwali-lifestyle-2026.webp",
        },
        "media_titles": {"hero": "advance happy Diwali 2026 Hero", "flatlay": "advance happy Diwali 2026 Flatlay", "lifestyle": "advance happy Diwali 2026 Lifestyle"},
        "schema_keywords": cfg["schema_keywords"],
        "slots": {
            "hero": {**hero, "alt": "advance happy Diwali 2026 hero with The Protecteur Evil Eye Pendant", "caption": "Advance Happy Diwali 2026 mood: The Protecteur Evil Eye Pendant", "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]}, "local_reference_images": [raw_image("Pendants", "The Protecteur Evil Eye Pendant", "1_body_portrait.png"), raw_image("Pendants", "The Protecteur Evil Eye Pendant", "0_primary.png")], "ref_roles": ["body_image", "front_primary"], "prompt": prompt_people(occasion="Advance Happy Diwali 2026 hero", scene="solo fair-skinned Indian adult woman in a cream festive kurta tying a silk ribbon around a small unbranded gift box beside diyas, marigold flowers, and a ceramic cup, full face visible, neck and pendant clearly visible, warm early festive greeting mood", product_name=hero["name"], product=hero, body_part="neck", extra_negatives="laptop-shaped rectangle, poster card, blank rectangle, open notebook, large pendant, pendant covering chest, envelope text")},
            "flatlay": {**flatlay, "alt": "advance happy Diwali 2026 flatlay with The Estrella Oval Bangle", "caption": "Advance Happy Diwali 2026 vibe: The Estrella Oval Bangle", "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]}, "local_reference_images": [raw_image("Bangles", "The Estrella Oval Bangle", "0_primary.png"), raw_image("Bangles", "The Estrella Oval Bangle", "2_front.png"), raw_image("Bangles", "The Estrella Oval Bangle", "4_close_up.png")], "ref_roles": ["primary", "front", "close_up"], "prompt": prompt_flatlay(occasion="Advance Happy Diwali 2026", setting="linen-bedside", setting_prompt="neutral linen bedside tray, sealed blank cream envelope, small unbranded wrapped gift, brass diya without markings, folded ribbon, marigold petals, no text", product_name=flatlay["name"], product=flatlay)},
            "lifestyle": {**lifestyle, "alt": "advance happy Diwali 2026 lifestyle with The Nettile Huggie Earrings", "caption": "Advance Happy Diwali 2026 look: The Nettile Huggie Earrings", "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]}, "local_reference_images": [raw_image("Earrings", "The Nettile Huggie Earrings", "1_body_portrait.png"), raw_image("Earrings", "The Nettile Huggie Earrings", "0_primary.png")], "ref_roles": ["body_image", "front_primary"], "prompt": prompt_people(occasion="Advance Happy Diwali 2026 lifestyle", scene="solo fair-skinned Indian adult woman tying a silk ribbon around a small blank gift box near warm diyas and flowers, full head visible and both ears visible, simple ivory festive blouse, no necklace and wrists out of frame, early festive wishes mood", product_name=lifestyle["name"], product=lifestyle, body_part="ear", extra_negatives="necklace, bracelet, ring, watch, gift label text")},
        },
    }
    write_json(f"output/{prefix}_sections.json", sections)
    write_json("output/publish_configs/week34_rank10.json", cfg)
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    checklist(prefix, 10, "Advance Happy Diwali 2026 Wishes", "advance happy diwali", False)


def main() -> None:
    product_rows = load_csv("Seo Products - final products (1).csv")
    detail_rows = load_csv("Seo Products - consolidated.csv")
    build_rank9(product_rows, detail_rows)
    build_rank10(product_rows, detail_rows)


if __name__ == "__main__":
    main()
