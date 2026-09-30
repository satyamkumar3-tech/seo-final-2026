#!/usr/bin/env python3
"""Build Week 3-4 Rank 2 Diwali Instagram captions assets."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week34_Rank2_DiwaliInstagramCaptions"
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
            "title": "Diwali Quotes for Instagram 2026: Captions",
            "slug": "diwali-quotes-for-instagram-2026",
            "meta_desc": "Diwali quotes for Instagram 2026 with captions for posts, photos, vibes, reels, funny wishes, short lines, couple captions, and festive outfit captions.",
            "focus_kw": "diwali quotes for instagram",
            "yoast_title": "Diwali Quotes for Instagram 2026",
        },
        "intro": [
            "Diwali quotes for Instagram work best when they are bright, short, and easy to pair with photos. For 2026, use captions that match the exact mood of your post, from diya glow and family moments to outfit photos, reels, and funny festive updates.",
            "TL;DR: Pick a short caption for photo dumps, a warm Diwali vibes caption for family pictures, a funny Diwali message for friends, and a jewellery led line when your festive look deserves the spotlight.",
        ],
        "sections": [
            {
                "key": "primary_quotes",
                "h2": "Diwali Quotes for Instagram",
                "lines": [
                    "Let the lights do the talking tonight.",
                    "Diyas outside, gratitude inside.",
                    "A little light can change the whole frame.",
                    "Glowing softly through Diwali 2026.",
                    "This festival is proof that hope has a shine of its own.",
                    "Light, love, and one more reason to smile.",
                    "May every diya remind us to choose warmth.",
                    "Festive hearts, golden lights, peaceful nights.",
                    "Finding joy in every tiny flame.",
                    "Diwali looks better when the heart feels lighter.",
                ],
            },
            {
                "key": "post_captions",
                "h2": "Captions for Diwali Post",
                "lines": [
                    "Posted with lights, sweets, and a happy heart.",
                    "Diwali 2026, saved in one bright little post.",
                    "Festival photo dump, diya edition.",
                    "Keeping this memory as warm as the evening.",
                    "When the whole house looks like a celebration.",
                    "A post full of sparkle and soft blessings.",
                    "Diwali scenes from my favourite corner.",
                    "Golden hour met festival hour.",
                    "One post, many tiny festive moments.",
                    "The kind of light I want to remember.",
                ],
            },
            {
                "key": "vibes_caption",
                "h2": "Diwali Vibes Caption Ideas",
                "lines": [
                    "Diwali vibes only.",
                    "Soft lights, loud laughter, full heart.",
                    "Festive mood: officially switched on.",
                    "Glow mode, no filter needed.",
                    "Sweets, smiles, and diya light.",
                    "Rangoli colours and golden nights.",
                    "Current vibe: peaceful, festive, grateful.",
                    "Warm lights and warmer people.",
                    "A little sparkle, a lot of soul.",
                    "This is what home feels like in lights.",
                ],
            },
            {
                "key": "photo_captions",
                "h2": "Captions for Diwali Photos",
                "lines": [
                    "Caught somewhere between diya glow and happy chaos.",
                    "A festive photo with a soft little story.",
                    "This picture smells like sweets and fresh flowers.",
                    "Keeping the glow, saving the memory.",
                    "Lights framed, heart full.",
                    "The best photos are the ones that feel like home.",
                    "Diwali photos and tiny pockets of joy.",
                    "A little blur, a lot of warmth.",
                    "Festive frame, grateful heart.",
                    "One photo, one thousand tiny lights.",
                ],
            },
            {
                "key": "happy_captions",
                "h2": "Happy Diwali Captions for Instagram",
                "lines": [
                    "Happy Diwali 2026 from my glowing little corner.",
                    "Wishing your feed and your heart a bright Diwali.",
                    "Happy Diwali, may your year ahead shine gently.",
                    "Light, love, and laughter to everyone celebrating.",
                    "Happy Diwali to the people who make life brighter.",
                    "May this festival bring peace, prosperity, and pretty pictures.",
                    "Happy Diwali, with extra sweets and extra sparkle.",
                    "Sending warm Diwali wishes through this tiny square.",
                    "May your home glow and your heart stay light.",
                    "Happy Diwali 2026, keep shining kindly.",
                ],
            },
            {
                "key": "funny_message",
                "h2": "Funny Diwali Message Captions",
                "lines": [
                    "My diya is calm, my snack plate is not.",
                    "Currently accepting sweets as a love language.",
                    "Diwali budget: emotionally rich, sweet box rich.",
                    "Sparkle level: outfit high, sleep low.",
                    "If you need me, I am near the mithai.",
                    "This glow is 20 percent diya and 80 percent excitement.",
                    "Festival cleaning counted as my workout.",
                    "Trying to look graceful while hunting for kaju katli.",
                    "Diwali calories are clearly decorative.",
                    "My outfit understood the assignment before I did.",
                ],
            },
            {
                "key": "funny_wishes",
                "h2": "Funny Diwali Wishes for Instagram",
                "lines": [
                    "May your sweets be fresh and your relatives ask fewer questions.",
                    "Wishing you a Diwali with more snacks than notifications.",
                    "May your outfit stay perfect and your diya stay lit.",
                    "Happy Diwali, may your phone survive the group messages.",
                    "May the only thing bursting this year be your happiness.",
                    "Wishing you peace, prosperity, and a plate nobody steals from.",
                    "May your rangoli stay safe from every passing foot.",
                    "Happy Diwali, may your favourite sweet appear twice.",
                    "May your pictures be sharp and your laddoos softer.",
                    "Wishing you light, laughter, and zero awkward small talk.",
                ],
            },
            {
                "key": "vibes_quotes",
                "h2": "Diwali Vibes Quotes",
                "lines": [
                    "There is a special kind of peace in a room full of diyas.",
                    "Diwali vibes are made of light, memory, and belonging.",
                    "The evening glows differently when everyone is home.",
                    "Some festivals do not need captions, but Instagram does.",
                    "A diya does not rush, it simply shines.",
                    "This glow is what gratitude looks like in colour.",
                    "Festive nights are softer when shared.",
                    "Light feels more beautiful when it is passed on.",
                    "Diwali is a reminder to make space for joy.",
                    "May this glow stay long after the lamps fade.",
                ],
            },
            {
                "key": "short_captions",
                "h2": "Short Diwali Captions",
                "lines": [
                    "Lit with love.",
                    "Golden little night.",
                    "Diya diaries.",
                    "Festive and grateful.",
                    "Glow gathered here.",
                    "Light wins.",
                    "Home in lights.",
                    "Sweets and sparkle.",
                    "Made of glow.",
                    "Diwali mood.",
                ],
            },
            {
                "key": "outfit_captions",
                "h2": "Diwali Outfit Captions",
                "lines": [
                    "Wearing tradition with a little shine.",
                    "Outfit bright, heart brighter.",
                    "Dressed for diyas and family photos.",
                    "Festive fit, golden mood.",
                    "A little silk, a little sparkle, a lot of Diwali.",
                    "When the jewellery and the lights agree.",
                    "Diwali look: graceful, happy, glowing.",
                    "Styled by tradition, finished with light.",
                    "This outfit came with festive confidence.",
                    "Gold tones and good vibes.",
                ],
            },
            {
                "key": "reel_captions",
                "h2": "Diwali Reel Captions",
                "lines": [
                    "One reel for all the Diwali glow.",
                    "From rangoli to lights in three seconds.",
                    "Tiny moments, big festival energy.",
                    "Watch the house turn into a celebration.",
                    "Diwali transition, heart edition.",
                    "A reel full of light and happy noise.",
                    "Saving the sparkle one clip at a time.",
                    "When every corner deserves a close up.",
                    "Festive prep, final glow, full heart.",
                    "Diwali 2026 in motion.",
                ],
            },
            {
                "key": "jewellery_gift",
                "h2": "Diwali Gift Captions with Jewellery",
                "lines": [
                    "A little keepsake for a festival full of light.",
                    "Jewellery that holds the glow after the diyas fade.",
                    "A festive gift, a quiet blessing, a memory to keep.",
                    "For the person who makes every celebration brighter.",
                    "Wrapped in love, worn with light.",
                    "A Diwali gift that says you shine beautifully.",
                    "Some gifts sparkle because of the feeling behind them.",
                    "A small piece, a bright memory.",
                    "When the caption and the jewellery both glow.",
                    "Light you can wear, love you can remember.",
                ],
            },
        ],
        "faqs": [
            ["What are good Diwali quotes for Instagram in 2026?", "Good Diwali quotes for Instagram in 2026 are short, visual, and warm. Use lines about diyas, light, home, gratitude, sweets, outfits, rangoli, and family. Keep the caption easy to read so it works for photos, reels, and festive stories."],
            ["What caption should I use for a Diwali post?", "Use a caption that matches the photo mood. For a family photo, choose a warm line about home and light. For an outfit photo, mention sparkle or tradition. For a funny post, keep it playful with sweets, snacks, or festive chaos."],
            ["What is a simple Diwali vibes caption?", "A simple Diwali vibes caption can be: Diwali vibes only, Soft lights and full hearts, or Glow mode on. These short captions work well for photo dumps, reels, rangoli pictures, and diya photos."],
            ["What are funny Diwali wishes for Instagram?", "Funny Diwali wishes for Instagram can mention sweets, festive outfits, family questions, snack plates, or group messages. Keep the joke light and friendly so it feels festive instead of sarcastic."],
            ["Can I use Diwali quotes for Instagram with jewellery photos?", "Yes. Jewellery photos work well with captions about glow, light, tradition, and memories. Keep the line elegant and avoid price talk. A good example is: Light you can wear, love you can remember."],
            ["How long should Diwali Instagram captions be?", "For Instagram, one short line usually works best. Use 4 to 12 words for a clean caption, or add one longer sentence if the post is a family memory, a festive greeting, or a jewellery gift note."],
            ["When is Diwali 2026?", "Diwali 2026 is observed on Sunday, 8 November 2026. If you are writing captions, reels, or scheduled posts, use the 2026 date so the content feels current and accurate."],
        ],
    }

    config = {
        "rank": "Week3-4 Rank 2",
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-diwaliinstagramcaptions",
        "occasion_year": "Diwali 2026",
        "carousel_alt_prefix": "diwali quotes for instagram 2026 gift idea",
        "gift_h2": "Diwali Jewellery Gift Ideas for Caption Ready Photos",
        "gift_blurb": "If your Instagram post features a festive look, choose jewellery that supports the mood without stealing the whole frame. These BlueStone picks work for warm Diwali captions, outfit photos, and gift posts.",
        "conclusion_html": "Diwali quotes for Instagram should feel bright, personal, and easy to post. Save a few short captions now, match the line to your photo mood, and let your 2026 Diwali pictures carry the glow naturally.",
        "schema_keywords": [
            "diwali quotes for instagram",
            "captions for diwali post",
            "diwali vibes caption",
            "captions for diwali photos",
            "funny diwali message",
            "funny diwali wishes",
            "happy diwali captions for instagram",
            "diwali vibes quotes",
        ],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(product_rows, "The Valeria Rose Pendant", "ProductImages/seo images/Pendants/The Valeria Rose Pendant.png"),
            product(product_rows, "The Muricelle Bangle", "ProductImages/seo images/Bangles/The Muricelle Bangle.png"),
            product(product_rows, "The Nettile Huggie Earrings", "ProductImages/seo images/Earrings/The Nettile Huggie Earrings.png"),
            product(product_rows, "The Ebony Ring", "ProductImages/seo images/Rings/The Ebony Ring.png"),
            product(product_rows, "The Ailia Evil Eye Layered Necklace", "ProductImages/seo images/Necklaces/The Ailia Evil Eye Layered Necklace.png"),
            product(product_rows, "The Malocchio Charm Holder Bracelet", "ProductImages/seo images/Bracelet/The Malocchio Charm Holder Bracelet.png"),
        ],
        "flatlay_insert_h2": "Diwali Vibes Caption Ideas",
        "lifestyle_insert_h2": "Diwali Gift Captions with Jewellery",
        "more_reads_html": "Read more festive ideas in <a href=\"https://blog.bluestone.com/diwali-wishes-and-quotes-2026/\">Diwali wishes and quotes 2026</a>, <a href=\"https://blog.bluestone.com/why-we-celebrate-diwali-2026/\">why we celebrate Diwali 2026</a>, and <a href=\"https://blog.bluestone.com/diwali-poster-2026/\">Diwali poster 2026</a>.",
        "how_to_html": "For date context, Diwali 2026 is observed on Sunday, 8 November 2026. For a short festival background, you can read <a href=\"https://www.britannica.com/topic/Diwali-Hindu-festival\">Britannica on Diwali</a>. Save short captions for reels, warmer lines for family photos, and elegant jewellery captions for outfit posts.",
        "faq_h2": "Frequently Asked Questions about Diwali Instagram Captions",
        "min_lines": 100,
    }

    hero = consolidated(detail_rows, "The Sarvanya Pendant")
    flatlay = consolidated(detail_rows, "The Haily Ring")
    lifestyle = consolidated(detail_rows, "The Vicky Hoop Earrings")

    prompts = {
        "rank": "Week3-4 Rank 2",
        "slug": "diwali-quotes-for-instagram-2026",
        "primary_kw": "diwali quotes for instagram",
        "output_prefix": PREFIX,
        "caption_occasion": "Diwali quotes for Instagram",
        "caption_year": "2026",
        "flatlay_setting": "marble-vanity",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/diwali-quotes-for-instagram-hero-2026.webp",
            "flatlay": "output/magnific_generated/diwali-quotes-for-instagram-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/diwali-quotes-for-instagram-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "diwali quotes for instagram 2026 hero The Sarvanya Pendant",
            "flatlay": "diwali quotes for instagram 2026 flatlay The Haily Ring",
            "lifestyle": "diwali quotes for instagram 2026 lifestyle The Vicky Hoop Earrings",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                **hero,
                "alt": "diwali quotes for instagram 2026 hero with The Sarvanya Pendant",
                "caption": "Diwali quotes for Instagram 2026 vibe: The Sarvanya Pendant",
                "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]},
                "cdn": [
                    "https://kinclimg6.bluestone.com/giproduct/BISW1080P132_WAA18DIG4LNBTXXXX_ABCD00-BP-PICS-00000-1024-104460.png",
                    "https://kinclimg9.bluestone.com/giproduct/BISW1080P132_WAA18DIG4LNBTXXXX_ABCD00-PICS-00004-1024-104460.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Sarvanya Pendant/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Sarvanya Pendant/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} "
                    "Diwali quotes for Instagram 2026 hero, solo fair-skinned Indian adult woman seated beside a window in a warm modern Indian living room. A blank smartphone and a blank cream note card rest on the table near a small diya and marigold petals, hinting at a caption writing moment. Full head, full face, both eyes, complete smile, neck, pendant, upper body, blank phone, blank card, and diya visible with safe margins. Exactly one person only. 85mm DSLR look, natural skin texture, warm daylight mixed with soft diya glow, 16:9.\n\n"
                    "The woman physically wears The Sarvanya Pendant from @img1 body_image and @img2 design only on her neck. GENDER LOCK: Female product on adult woman only. "
                    f"Product dimensions from PDP: {hero['size_prompt_note']}. These are product dimensions, not face-size instructions. "
                    "Keep pendant size on the neck like @img1 body_image worn scale: subtle real PDP size, not enlarged. Use @img2 only for jewellery design.\n\n"
                    "Replicate the white gold diamond cluster pendant with blue accent exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery object in the entire image. Bare ears, wrists and fingers hidden or bare, no earrings, no rings, no bracelets, no bangles, no watch, no extra necklace. No readable text anywhere. Any phone, card, or gift tag must be completely blank.\n\n"
                    "Avoid: visible earrings, visible rings, cropped face, cropped head, readable text, letters, numbers, logo, man wearer, child, second person, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow."
                ),
            },
            "flatlay": {
                **flatlay,
                "alt": "diwali quotes for instagram 2026 flatlay with The Haily Ring",
                "caption": "Diwali quotes for Instagram 2026 flatlay: The Haily Ring",
                "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]},
                "cdn": [
                    "https://kinclimg0.bluestone.com/giproduct/BINS0639R11_YAA22XXXXXXXXXXXX_ABCD00-PICS-00000-1024-65665.png",
                    "https://kinclimg0.bluestone.com/giproduct/BINS0639R11_YAA22XXXXXXXXXXXX_ABCD00-PICS-00001-1024-65665.png",
                    "https://kinclimg0.bluestone.com/giproduct/BINS0639R11_YAA22XXXXXXXXXXXX_ABCD00-PICS-00002-1024-65665.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Rings/The Haily Ring/0_primary.png",
                    "ProductImages/raw/Rings/The Haily Ring/2_front.png",
                    "ProductImages/raw/Rings/The Haily Ring/4_back.png",
                ],
                "ref_roles": ["primary", "front", "back"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\n"
                    "Diwali quotes for Instagram 2026 top-down flatlay. Flatlay setting ID: marble-vanity. Surface and props: warm ivory marble vanity, a blank smartphone with no visible interface, a blank cream caption card, tiny diya, marigold petals, and soft beige silk. "
                    "The identical Haily Ring from @img1, @img2 and @img3 rests naturally on the surface at true PDP scale. "
                    f"Product dimensions from PDP: {flatlay['size_prompt_note']}. These are product dimensions, not face-size instructions. Do not enlarge for visibility. "
                    "Full ring visible, yellow gold ring with diamond detail, 100 percent identical design, zero distortion, HD metal and stone detail.\n\n"
                    "Props stay secondary. No people, no hands, no logos, no readable text, no letters, no numbers, no other jewellery.\n\n"
                    "Avoid: hands, people, floating overlays, cutouts, incorrect ring design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI."
                ),
            },
            "lifestyle": {
                **lifestyle,
                "alt": "diwali quotes for instagram 2026 lifestyle with The Vicky Hoop Earrings",
                "caption": "Diwali quotes for Instagram 2026 look: The Vicky Hoop Earrings",
                "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]},
                "cdn": [
                    "https://kinclimg5.bluestone.com/giproduct/BIIP0427H16_YAA18DIG6XXXXXXXX_ABCD00-BP-PICS-00000-1024-76610.png",
                    "https://kinclimg2.bluestone.com/giproduct/BIIP0427H16_YAA18DIG6XXXXXXXX_ABCD00-PICS-00004-1024-76610.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Earrings/The Vicky Hoop Earrings/1_body_portrait.png",
                    "ProductImages/raw/Earrings/The Vicky Hoop Earrings/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": (
                    f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} "
                    "Diwali quotes for Instagram 2026 lifestyle, solo fair-skinned Indian adult woman in a simple cream festive kurta standing near warm fairy lights and diyas in a modern Indian home, smiling as if ready for a festive outfit photo. A blank smartphone rests on a table in the foreground, screen completely blank and not held. Full head, full face, both ears, both eyes, complete smile, upper body, earrings, diyas, and blank phone visible with safe margins. Exactly one person only. 85mm DSLR look, natural skin texture, realistic shadows, 16:9.\n\n"
                    "The woman physically wears The Vicky Hoop Earrings from @img1 body_image and @img2 design only on her ears. GENDER LOCK: Female product on adult woman only. "
                    f"Product dimensions from PDP: {lifestyle['size_prompt_note']}. These are product dimensions, not face-size instructions. "
                    "Keep earrings size on the ears like @img1 body_image worn scale: subtle real PDP size, not enlarged. Use @img2 only for jewellery design.\n\n"
                    "Replicate the yellow gold diamond hoop earrings exactly, 100 percent identical to refs, zero distortion, HD metal detail. These earrings are the single and only jewellery object in the entire image. Bare neck, wrists and fingers hidden or bare, no necklace, no pendant, no bracelet, no bangle, no ring, no watch, no other earrings. No readable text anywhere. Any phone, card, or gift tag must be completely blank.\n\n"
                    "Avoid: extra earrings, visible rings, cropped face, cropped head, readable text, letters, numbers, logo, man wearer, child, second person, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow."
                ),
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Week 3-4 Rank 2

Article: Diwali Quotes for Instagram 2026
Status: Draft assets prepared
Date: 2026-07-27

## A. Intent and Brief
- [x] Primary keyword: diwali quotes for instagram
- [x] Sheet Optimize treated as New
- [x] Fresh slug: diwali-quotes-for-instagram-2026
- [x] 2026 year lock used
- [x] Supporting keywords mapped to H2 and FAQ

## B. SEO Structure
- [x] Title/H1 intent prepared
- [x] Yoast title under 60 chars
- [x] Meta description 150 to 160 chars
- [x] Primary keyword in intro and hero alt

## C. Content and Readability
- [x] Direct answer and TL;DR
- [x] 100+ caption, quote, wish, and message lines
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
    write_json("output/publish_configs/week34_rank2.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")
    print(f"wrote {PREFIX} assets")


if __name__ == "__main__":
    main()
