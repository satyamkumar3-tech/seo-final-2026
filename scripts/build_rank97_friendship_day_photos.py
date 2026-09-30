#!/usr/bin/env python3
"""Build Rank 97 Friendship Day photos article assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank97_FriendshipDayPhotos"
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
        f"Friendship Day photos 2026 {scene}. Solo fair-skinned Indian adult woman, warm candid smile, "
        "bright modern Indian cafe, blank phone screen or blank cream friendship card nearby, soft daylight, "
        "full head, full face, both eyes, complete smile, upper body and jewellery area visible with safe margins. "
        "Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, "
        "realistic shadows, 16:9.\n\n"
        f"The woman physically wears {slot['name']} from @img1 body_image and @img2 design. "
        "GENDER LOCK: Female product on adult woman only. "
        f"Product dimensions from PDP: {slot['size_prompt_note']}. "
        f"Keep {scale_phrase} like @img1 body_image worn scale: subtle real product size, not enlarged. "
        "Use @img2 only for jewellery design.\n\n"
        f"Replicate {product_phrase} exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. "
        f"This is the single and only jewellery in the image. {extra_rules} No readable text anywhere.\n\n"
        "Avoid: cropped face, cropped head, readable text, letters, numbers, logo, man wearer, child, second person, "
        "extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, "
        "deep brown skin, heavily tanned skin, illustration, CGI, HDR glow."
    )


def main() -> None:
    csv_rows = rows_by_name("Seo Products - final products (1).csv")
    detail_rows = rows_by_name("KnowledgeBase/Product/Seo Products - consolidated.csv")

    sections = {
        "meta": {
            "title": "Friendship Day Photos 2026: Happy Friendship Day Images",
            "slug": "friendship-day-photos-2026",
            "meta_desc": "Friendship Day photos 2026 with Happy Friendship Day images, greetings, captions, wishes, quotes, WhatsApp status, and photo message ideas for friends.",
            "focus_kw": "friendship day photos",
            "yoast_title": "Friendship Day Photos 2026: Happy Friendship Day Images",
        },
        "intro": [
            "Friendship day photos work best when the image feels personal, not generic. A warm photo, one honest line, and a caption that sounds like your friendship can make the post feel instantly shareable.",
            "TL;DR: choose a Friendship Day photo style first, add a short wish or caption, keep the card or phone screen clean, and send it with a line that names what your friend means to you.",
        ],
        "sections": [
            {"key": "best", "h2": "Friendship Day Photos", "lines": [
                "Use a smiling selfie with a caption about being lucky to have your friend.",
                "Share an old college photo with a line about memories that still feel new.",
                "Post a cafe photo if your friendship is built on long conversations.",
                "Use a travel photo for the friend who made ordinary trips unforgettable.",
                "Share a childhood picture if you both grew up through every awkward phase together.",
                "Pick a candid laugh photo because real friendship rarely poses perfectly.",
                "Use a group photo when your whole circle deserves the love.",
                "Post a simple hand-in-frame photo with coffee cups for a soft aesthetic.",
                "Share a blurred background photo with one clear line about loyalty.",
                "Choose a photo where the emotion is obvious even before the caption.",
            ]},
            {"key": "images", "h2": "Happy Friendship Day Images", "lines": [
                "Happy Friendship Day to the person who makes normal days feel special.",
                "Friends like you turn small moments into favorite memories.",
                "Here is to the friend who knows my chaos and still stays.",
                "Happy Friendship Day, grateful for every laugh and every rescue call.",
                "Some people become family without needing the same surname.",
                "You make life lighter, funnier, and easier to survive.",
                "A good friend is a safe place with better jokes.",
                "Happy Friendship Day to my forever gossip partner.",
                "Thanks for being the calm, the comedy, and the courage.",
                "Real friendship is being seen fully and loved anyway.",
            ]},
            {"key": "greetings", "h2": "Friendship Day Photos Greetings", "lines": [
                "Happy Friendship Day, may our bond keep growing with every year.",
                "Wishing you a day full of smiles, memories, and calls from people who love you.",
                "Thank you for being the friend who shows up without making it a big deal.",
                "May this Friendship Day remind you how deeply valued you are.",
                "Sending love to the friend who made so many days brighter.",
                "Happy Friendship Day, you are one of my life's best gifts.",
                "May our friendship stay honest, funny, and beautifully low-maintenance.",
                "Cheers to the person who knows my stories and still asks for updates.",
                "Wishing you happiness today and always, my dear friend.",
                "Happy Friendship Day, thank you for making life feel less heavy.",
            ]},
            {"key": "captions", "h2": "Friendship Day Captions for Photos", "lines": [
                "Best friends, best stories.",
                "My favorite notification in human form.",
                "Proof that chaos can be comforting.",
                "A little dramatic, always loyal.",
                "Same madness, different outfits.",
                "Friendship looks good on us.",
                "Old memories, new laughter.",
                "The friend who makes everything easier.",
                "Real bond, zero filters needed.",
                "My person for every silly plan.",
            ]},
            {"key": "whatsapp", "h2": "Friendship Day Photos for WhatsApp Status", "lines": [
                "Status today: grateful for friends who became home.",
                "Happy Friendship Day to the people who make life softer.",
                "Some friendships do not need daily talks, just honest hearts.",
                "Blessed with friends who know the real me.",
                "Forever thankful for laughter that arrives exactly when needed.",
                "Friendship is the best kind of everyday celebration.",
                "To my closest people, thank you for staying.",
                "A photo cannot hold all our memories, but it can start the smile.",
                "Happy Friendship Day to my tiny circle with a huge place in my heart.",
                "Good friends make even ordinary photos feel precious.",
            ]},
            {"key": "funny", "h2": "Funny Friendship Day Image Captions", "lines": [
                "We are not normal, and that is our brand.",
                "Friends who roast together stay together.",
                "Thanks for knowing too much and using it responsibly.",
                "Our friendship runs on screenshots and snacks.",
                "You are the reason my camera roll is unexplainable.",
                "Best friend: unpaid therapist, full-time comedian.",
                "We have evidence, so we must stay friends forever.",
                "Happy Friendship Day to my partner in questionable decisions.",
                "Our photos are cute because the stories are chaotic.",
                "Friendship level: can send ugly selfies without warning.",
            ]},
            {"key": "emotional", "h2": "Heart Touching Friendship Day Photos Quotes", "lines": [
                "A true friend remembers the version of you that survived hard days.",
                "Friendship is not about being available every minute, it is about being real when it matters.",
                "Some friends arrive quietly and change the way life feels.",
                "A good friend does not fix every problem, but they make you feel less alone inside it.",
                "The best friendships are made of trust, time, and small acts of care.",
                "A photo can fade, but the person who stood beside you becomes part of your story.",
                "Real friends celebrate your joy without measuring it against their own.",
                "Friendship is the comfort of being understood without explaining everything.",
                "The right friend makes your younger self feel protected.",
                "Some bonds are simple, steady, and rare enough to treasure.",
            ]},
            {"key": "girls", "h2": "Friendship Day Photos for Girl Best Friend", "lines": [
                "Happy Friendship Day to the girl who turns every plan into a memory.",
                "You are my safe place, style advisor, and truth teller.",
                "To the friend who knows my moods before I name them, thank you.",
                "Every good photo with you has a better story behind it.",
                "You make friendship feel easy, bright, and honest.",
                "Here is to all our laughs, late replies, and loyal moments.",
                "Happy Friendship Day to my favorite girl gang energy.",
                "You are the sister life let me choose.",
                "Our friendship deserves a whole album, not just one post.",
                "Thank you for being soft when life gets sharp.",
            ]},
            {"key": "boys", "h2": "Friendship Day Photos for Boy Best Friend", "lines": [
                "Happy Friendship Day to the friend who keeps things real.",
                "Thanks for the jokes, advice, and silent support.",
                "Some brothers are chosen by friendship, not family.",
                "You are the friend who makes every plan less boring.",
                "Here is to loyalty, laughter, and years of inside jokes.",
                "Happy Friendship Day to the person who shows up without drama.",
                "A true friend makes even simple photos worth keeping.",
                "Thanks for being the calm in many confusing days.",
                "Friendship like this does not need big speeches.",
                "Respect, trust, and terrible jokes, that is our bond.",
            ]},
            {"key": "instagram", "h2": "Friendship Day Photos for Instagram", "lines": [
                "Post one clear photo and keep the caption short if the image is emotional.",
                "Use carousel posts for then-and-now friendship photos.",
                "Pair a cafe photo with a warm one-line memory.",
                "For group photos, mention the circle rather than tagging only one person.",
                "Use a blank-card image if you want a clean, aesthetic greeting post.",
                "Avoid overloading the caption with too many hashtags.",
                "A simple line often feels more premium than a long paragraph.",
                "Use natural daylight photos for a softer Friendship Day mood.",
                "If the photo is funny, let the caption be even shorter.",
                "End with one personal phrase only your friend will understand.",
            ]},
            {"key": "gift", "h2": "Friendship Day Gift Ideas for Photo Messages", "lines": [
                "A small keepsake can make a Friendship Day photo message feel more personal.",
                "Bracelets work well for friends who like everyday jewellery.",
                "Earrings suit friends who enjoy simple festive styling.",
                "Pendants feel thoughtful when the bond is close and sentimental.",
                "A ring can work as a self-love gift between best friends.",
                "Choose a design around your friend's daily style, not only the occasion.",
                "Add a blank card with one line that feels handwritten and honest.",
                "Keep the message emotional, not price-led.",
                "A photo, a small note, and a wearable keepsake can become a sweet memory.",
                "The best gift is the one that says I know you.",
            ]},
            {"key": "download", "h2": "How to Choose Friendship Day Photos to Download or Share", "lines": [
                "Pick a photo that matches your friend's personality before choosing the caption.",
                "Use bright images for cheerful greetings and softer photos for emotional quotes.",
                "Avoid images with cluttered text if you want the caption to stand out.",
                "Check that the photo crops well for WhatsApp and Instagram.",
                "Use one main message instead of many tiny lines on the same image.",
                "If sharing publicly, choose a photo your friend would also like.",
                "For private messages, a personal memory matters more than a polished edit.",
                "Keep names, screenshots, and private details out of public posts.",
                "Use 2026 in the caption if you want the image to feel fresh.",
                "When unsure, send the photo with one sincere line and a heart.",
            ]},
        ],
        "faqs": [
            ["What should I write with Friendship Day photos?", "Write one short line that explains why the photo matters. For example, Happy Friendship Day to the friend who made this memory unforgettable. Keep it personal, warm, and easy to read."],
            ["How do I caption Happy Friendship Day images?", "Use a caption that matches the image mood. Funny photos need a playful one-liner, while emotional images work better with a simple thank-you note or a memory-based wish."],
            ["Can I use Friendship Day photos for WhatsApp status?", "Yes. Choose a clear image, avoid private details, and add a short status such as grateful for friends who became home. Short captions are easier to read on WhatsApp."],
            ["What is a good Friendship Day photo greeting?", "A good greeting is warm and specific. Try: Happy Friendship Day, thank you for making ordinary days feel brighter and hard days feel lighter."],
            ["Which Friendship Day photos are best for Instagram?", "Candid laughter, cafe moments, old memories, travel photos, and clean blank-card images work well on Instagram. Keep the caption short so the photo remains the focus."],
            ["Can I pair a Friendship Day image with a gift?", "Yes. A photo message with a small keepsake such as a bracelet, pendant, earrings, or ring can feel thoughtful when the design matches your friend's everyday style."],
        ],
    }

    config = {
        "rank": 97,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-friendshipphotos",
        "occasion_year": "Friendship Day Photos 2026",
        "carousel_alt_prefix": "friendship day photos 2026 gift idea",
        "gift_h2": "BlueStone Gift Ideas for Friendship Day Photo Messages",
        "gift_blurb": "Friendship Day photos feel more personal when the message comes with a keepsake chosen around your friend's everyday style. These approved BlueStone designs keep the gifting note soft and wearable.",
        "conclusion_html": "Friendship day photos do not need perfect poses to feel special. Pick a memory, add one sincere caption, and send it in a way that sounds like your bond.",
        "schema_keywords": ["friendship day photos", "happy friendship day images", "friendship day photos greetings", "friendship day captions", "friendship day wishes"],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(csv_rows, "The Shining Star Bracelet", "ProductImages/seo images/Bracelet/The Shining Star Bracelet.png"),
            product(csv_rows, "The Quinn Ring", "ProductImages/seo images/Rings/The Quinn Ring.png"),
            product(csv_rows, "The Ixea Evil Eye Pendant", "ProductImages/seo images/Pendants/The Ixea Evil Eye Pendant.png"),
            product(csv_rows, "The Tapia Chain Bracelet", "ProductImages/seo images/Bracelet/The Tapia Chain Bracelet.png"),
            product(csv_rows, "The Nettile Huggie Earrings", "ProductImages/seo images/Earrings/The Nettile Huggie Earrings.png"),
            product(csv_rows, "The Haily Ring", "ProductImages/seo images/Rings/The Haily Ring.png"),
        ],
        "flatlay_insert_h2": "Friendship Day Photos Greetings",
        "lifestyle_insert_h2": "Friendship Day Gift Ideas for Photo Messages",
        "more_reads_html": "Read more heartfelt guides in <a href=\"https://blog.bluestone.com/mother-day-wish-in-hindi-2026/\">mother day wish in Hindi 2026</a>, <a href=\"https://blog.bluestone.com/mother-daughter-quotes-2026/\">mother daughter quotes 2026</a>, <a href=\"https://blog.bluestone.com/raksha-bandhan-gifts-for-brother-2026/\">Raksha Bandhan gifts for brother 2026</a>, and <a href=\"https://blog.bluestone.com/new-year-wishes-for-love-2026/\">New Year wishes for love 2026</a>.",
        "how_to_html": "For a Friendship Day photo post, choose the image mood first. Use funny captions for silly photos, emotional notes for old memories, and short greetings for WhatsApp status.",
        "faq_h2": "Frequently Asked Questions about Friendship Day Photos",
        "min_lines": 100,
    }

    hero = consolidated(detail_rows, "The Sarvanya Pendant")
    flatlay = consolidated(detail_rows, "The Tapia Chain Bracelet")
    lifestyle = consolidated(detail_rows, "The Faliha Purse Hoop Earrings")

    prompts = {
        "rank": 97,
        "slug": "friendship-day-photos-2026",
        "primary_kw": "friendship day photos",
        "output_prefix": PREFIX,
        "caption_occasion": "Friendship Day photos",
        "caption_year": "2026",
        "flatlay_setting": "cafe-tray",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/friendship-day-photos-hero-2026.webp",
            "flatlay": "output/magnific_generated/friendship-day-photos-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/friendship-day-photos-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "friendship day photos 2026 hero The Sarvanya Pendant",
            "flatlay": "friendship day photos 2026 flatlay The Tapia Chain Bracelet",
            "lifestyle": "friendship day photos 2026 lifestyle The Faliha Purse Hoop Earrings",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                **hero,
                "alt": "friendship day photos 2026 hero with The Sarvanya Pendant",
                "caption": "Friendship Day photos 2026 vibe: The Sarvanya Pendant",
                "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]},
                "cdn": [
                    "https://kinclimg6.bluestone.com/giproduct/BISW1080P132_WAA18DIG4LNBTXXXX_ABCD00-BP-PICS-00000-1024-104460.png",
                    "https://kinclimg9.bluestone.com/giproduct/BISW1080P132_WAA18DIG4LNBTXXXX_ABCD00-PICS-00002-1024-104460.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Sarvanya Pendant/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Sarvanya Pendant/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": people_prompt(
                    hero,
                    "hero, smiling at a blank phone screen while choosing a friendship photo to share, with two plain coffee cups and a blank cream card on the table",
                    "the white gold and blue-toned pendant",
                    "pendant size on the neck",
                    "Bare ears, hands and wrists hidden below frame or behind the blank card; no earrings, no bracelet, no bangles, no rings, no watch, no extra necklace.",
                ),
            },
            "flatlay": {
                **flatlay,
                "alt": "friendship day photos 2026 flatlay with The Tapia Chain Bracelet",
                "caption": "Friendship Day photos 2026 keepsake: The Tapia Chain Bracelet",
                "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]},
                "cdn": [
                    "https://kinclimg5.bluestone.com/giproduct/BIPO0987V31_YAA18DIG6XXXXXXXX_ABCD00-PICS-00001-1024-79780.png",
                    "https://kinclimg5.bluestone.com/giproduct/BIPO0987V31_YAA18DIG6XXXXXXXX_ABCD00-PICS-00002-1024-79780.png",
                    "https://kinclimg5.bluestone.com/giproduct/BIPO0987V31_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-79780.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Bracelets/The Tapia Chain Bracelet/0_primary.png",
                    "ProductImages/raw/Bracelets/The Tapia Chain Bracelet/2_side_1.png",
                    "ProductImages/raw/Bracelets/The Tapia Chain Bracelet/3_back.png",
                ],
                "ref_roles": ["primary", "angle", "back"],
                "prompt": (
                    f"Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\n"
                    "Friendship Day photos 2026 top-down flatlay. Flatlay setting ID: cafe-tray. Surface and props: "
                    "ceramic cafe tray, plain espresso cup and saucer, folded blank napkin, blank cream friendship card, soft daylight, no readable text. "
                    "The identical Tapia Chain Bracelet from @img1, @img2 and @img3 rests naturally on the tray at true PDP scale. "
                    f"Product dimensions from PDP: {flatlay['size_prompt_note']}. Do not enlarge for visibility. "
                    "Full bracelet visible, yellow gold chain bracelet with diamond detail, 100 percent identical design, zero distortion, HD metal and stone detail.\n\n"
                    "Props stay secondary. No people, no hands, no logos, no readable text.\n\n"
                    "Avoid: hands, people, floating overlays, cutouts, incorrect bracelet design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI."
                ),
            },
            "lifestyle": {
                **lifestyle,
                "alt": "friendship day photos 2026 lifestyle with The Faliha Purse Hoop Earrings",
                "caption": "Friendship Day photos 2026 vibe: The Faliha Purse Hoop Earrings",
                "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]},
                "cdn": [
                    "https://kinclimg5.bluestone.com/giproduct/BIJP0686H03_YAA18DIG4XXXXXXXX_ABCD00-BP-PICS-00000-1024-84306.png",
                    "https://kinclimg9.bluestone.com/giproduct/BIJP0686H03_YAA18DIG4XXXXXXXX_ABCD00-PICS-00003-1024-84306.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Earrings/The Faliha Purse Hoop Earrings/1_body_portrait.png",
                    "ProductImages/raw/Earrings/The Faliha Purse Hoop Earrings/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": people_prompt(
                    lifestyle,
                    "lifestyle, laughing softly beside a blank friendship card and a small photo album with no visible photos or text",
                    "the yellow gold purse hoop earrings with horizontal baguette diamond bar",
                    "earring size on the ears",
                    "Bare neck, hands and wrists hidden below frame; no necklace, no pendant, no bracelet, no bangles, no rings, no watch, no other earrings.",
                ),
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 97

Article: Friendship Day Photos 2026
Status: Draft assets prepared
Date: 2026-07-24

## A. Intent and Brief
- [x] Primary keyword: friendship day photos
- [x] Sheet Action treated as New
- [x] Fresh slug: friendship-day-photos-2026
- [x] 2026 year lock used
- [x] Supporting keywords mapped to H2 and FAQ

## B. SEO Structure
- [x] Title/H1 intent prepared
- [x] Yoast title under 60 chars
- [x] Meta description 150 to 160 chars
- [x] Primary keyword in intro and hero alt

## C. Content and Readability
- [x] Direct answer and TL;DR
- [x] 100+ message/caption/photo idea lines
- [x] No prices
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
    write_json("output/publish_configs/rank97.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")
    print(f"wrote {PREFIX} sections/config/prompts")


if __name__ == "__main__":
    main()
