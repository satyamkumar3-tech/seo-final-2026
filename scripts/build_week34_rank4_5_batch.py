#!/usr/bin/env python3
"""Build Week 3-4 Rank 4 and Rank 5 assets."""
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


def load_csv(path: str) -> dict[str, dict[str, str]]:
    with (ROOT / path).open(newline="", encoding="utf-8-sig") as f:
        return {row["Design Name"].strip(): row for row in csv.DictReader(f)}


def product(rows: dict[str, dict[str, str]], name: str) -> dict[str, str]:
    row = rows[name]
    matches = sorted((ROOT / "ProductImages/seo images").glob(f"*/{name}.png"))
    if not matches:
        raise SystemExit(f"Missing SEO carousel image for {name}")
    return {"code": row["Design Code"], "name": name, "url": row["Link"], "png": str(matches[0])}


def consolidated(rows: dict[str, dict[str, str]], name: str) -> dict[str, object]:
    row = rows[name]
    size_note = row["size_prompt_note"] or f"product_height_mm={row['height_mm']}; product_width_mm={row['width_mm']}"
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
        f"Product dimensions from PDP: {product['size_prompt_note']}. These are product dimensions, not face-size instructions. "
        f"Keep the jewellery size on the person like @img1 body_image worn {body_part} scale: subtle real PDP size, not enlarged. "
        "Use @img2 only for jewellery design.\n\n"
        "Replicate the jewellery exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. "
        "This is the single and only jewellery object in the entire image. Others wear absolutely no other jewellery. "
        "No readable text anywhere. Any card, tag, notebook, or phone screen must be completely blank.\n\n"
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
        f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. Photoreal high-end jewellery still life, top-down editorial product flatlay. "
        f"{FILMIC_STYLE}\n\n"
        f"{occasion} top-down flatlay. Flatlay setting ID: {setting}. Surface and props: {setting_prompt}. "
        f"The identical {product_name} from @img1, @img2 and @img3 rests naturally on the surface at true PDP scale. "
        f"Product dimensions from PDP: {product['size_prompt_note']}. These are product dimensions, not face-size instructions. "
        "Do not enlarge for visibility. Full jewellery visible, 100 percent identical design, zero distortion, HD metal and stone detail.\n\n"
        "Props stay secondary. No people, no hands, no logos, no readable text, no letters, no numbers, no other jewellery.\n\n"
        "Avoid: hands, people, floating overlays, cutouts, incorrect jewellery design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI."
    )


def build_rank4(product_rows: dict[str, dict[str, str]], detail_rows: dict[str, dict[str, str]]) -> None:
    prefix = "Week34_Rank4_FriendshipDayQuotes"
    sections = {
        "meta": {
            "title": "Emotional Friendship Day Quotes 2026",
            "slug": "emotional-friendship-day-quotes-2026",
            "meta_desc": "Emotional Friendship Day quotes 2026 for best friends, girl gangs, captions, one line notes, funny wishes, and heartfelt messages to share with love today.",
            "focus_kw": "emotional friendship day quotes",
            "yoast_title": "Emotional Friendship Day Quotes 2026",
        },
        "intro": [
            "Emotional Friendship Day quotes help you say the things that usually hide behind memes, late replies, and long voice notes. In India, Friendship Day 2026 falls on Sunday, August 2, so this page gives you copy ready lines for best friends, girl gangs, captions, cards, and heartfelt messages.",
            "TL;DR: Pick a short quote for Instagram, a warmer message for WhatsApp, a funny line for close friends, and a longer note when the friendship has carried you through real life.",
        ],
        "sections": [
            {
                "key": "emotional",
                "h2": "Emotional Friendship Day Quotes",
                "lines": [
                    "A true friend is the person who remembers your real story even when the world only sees your smile.",
                    "Friendship is not measured by daily calls. It is measured by who still shows up when life becomes heavy.",
                    "Some friends become home because they make your heart feel safe without asking for explanations.",
                    "A real friend does not fix every problem. They sit beside you until you remember your strength.",
                    "The best friendships are quiet promises that say, I am here, even when everything else changes.",
                    "Friendship is the family your heart recognizes before your mind finds the right words.",
                    "A friend who protects your peace is one of life’s rarest gifts.",
                    "Some people enter your life as friends and slowly become part of your courage.",
                    "True friendship is love without performance, support without condition, and laughter without reason.",
                    "A loyal friend can turn an ordinary day into proof that you are not alone.",
                    "The most emotional friendships are built from small moments that stayed.",
                    "A friend who understands your silence deserves a permanent place in your prayers.",
                ],
            },
            {
                "key": "best_friend",
                "h2": "Best Friend Quotes for Friendship Day",
                "lines": [
                    "Happy Friendship Day to the one person who knows my chaos and still chooses me.",
                    "You are not just my best friend. You are my comfort person, my truth mirror, and my loudest cheer.",
                    "Life gave me many people, but it gave me peace when it gave me you.",
                    "My best friend is the person who can make me laugh in the middle of a breakdown.",
                    "Thank you for being the kind of friend who makes every memory brighter.",
                    "You are the proof that soulmates can arrive as friends.",
                    "A best friend is someone who turns ordinary plans into lifelong stories.",
                    "You have seen my worst moods and still saved a seat for me in your life.",
                    "Friendship Day feels special because I get to celebrate someone who made life softer.",
                    "Best friends are not perfect people. They are the ones who stay real.",
                    "You are my favourite notification and my safest conversation.",
                    "The best part of growing up is knowing some friendships grew with me.",
                ],
            },
            {
                "key": "instagram_short",
                "h2": "Instagram Short Best Friend Quotes",
                "lines": [
                    "Best friend energy, always.",
                    "Chosen family, real bond.",
                    "Forever my safe chaos.",
                    "Same madness, stronger bond.",
                    "Friendship Day with my favourite human.",
                    "Real ones stay.",
                    "My person, my peace.",
                    "Laughing through life together.",
                    "Built on trust and snacks.",
                    "Best friend, best blessing.",
                    "More than friends, less than ordinary.",
                    "This bond needs no filter.",
                ],
            },
            {
                "key": "one_line",
                "h2": "One Line Caption for Best Friend",
                "lines": [
                    "You make life feel lighter.",
                    "My forever call at any hour.",
                    "Friendship looks good on us.",
                    "My favourite kind of family.",
                    "You are my calm and my chaos.",
                    "A bond that keeps choosing us.",
                    "Best friend, biggest blessing.",
                    "Life is better with you in it.",
                    "Same story, same side.",
                    "Friendship Day, but make it us.",
                    "Some people feel like home.",
                    "My person in every season.",
                ],
            },
            {
                "key": "few_lines",
                "h2": "Few Lines for Best Friend",
                "lines": [
                    "You have been there for the loud days and the quiet ones. That is why this Friendship Day feels like a thank you.",
                    "Thank you for understanding my moods, my dreams, and my strange jokes without making me explain myself.",
                    "A best friend like you makes the hard parts easier and the happy parts unforgettable.",
                    "You are the person I can call with news, nonsense, panic, or silence, and all of it feels safe.",
                    "Happy Friendship Day. I hope you know how much your loyalty has meant to me.",
                    "You have helped me become softer, braver, and more myself. That is a rare gift.",
                    "Some friendships are not loud online, but they are deeply alive in real life.",
                    "I do not say it often, but I am grateful for the way you stand by me.",
                    "Your friendship is one of the reasons my ordinary days feel less ordinary.",
                    "Thank you for being my reminder that good people still exist.",
                ],
            },
            {
                "key": "girl_gang",
                "h2": "Girl Gang Quotes",
                "lines": [
                    "A girl gang is therapy, comedy, styling advice, and emergency support in one chat.",
                    "Behind every strong woman is a group chat that knows the full story.",
                    "Girl gang love means fixing crowns, sharing snacks, and defending each other loudly.",
                    "We are not dramatic. We are emotionally well networked.",
                    "A real girl gang celebrates your wins like they belong to everyone.",
                    "Friendship Day is for the girls who turned life into a shared playlist.",
                    "Good friends hype you up. Great friends also tell you when the outfit needs changing.",
                    "My girl gang is proof that friendship can be fierce and soft at once.",
                    "We shine differently, but we never let each other dim.",
                    "Some friendships sparkle because every woman in the circle brings her own light.",
                ],
            },
            {
                "key": "wishes",
                "h2": "Happy Friendship Day Quotes Wishes",
                "lines": [
                    "Happy Friendship Day. May our bond keep growing through every season of life.",
                    "Wishing you a day full of laughter, old memories, and the comfort of being loved.",
                    "Happy Friendship Day to the friend who makes every problem feel smaller.",
                    "May this year bring you loyal people, peaceful days, and reasons to smile.",
                    "Thank you for being my friend, my secret keeper, and my honest mirror.",
                    "Happy Friendship Day. You are one of the best parts of my life.",
                    "Wishing you the same warmth and support you have always given me.",
                    "May our friendship stay strong through distance, change, and busy schedules.",
                    "Happy Friendship Day to the one who makes ordinary moments unforgettable.",
                    "Cheers to a bond that survived mood swings, bad plans, and endless jokes.",
                ],
            },
            {
                "key": "funny",
                "h2": "Funny Friendship Day Quotes",
                "lines": [
                    "Happy Friendship Day to the person who knows too much and must be kept close.",
                    "You are my best friend because you tolerate my drama at no extra charge.",
                    "Our friendship is mostly love, laughter, and screenshots.",
                    "Thanks for being the friend I can be weird with professionally.",
                    "Happy Friendship Day. You are the reason my secrets need passwords.",
                    "A good friend gives advice. A best friend says, send me the full screenshot.",
                    "We are proof that questionable decisions create excellent memories.",
                    "Friendship Day reminder: you are stuck with me now.",
                    "You are my favourite unpaid therapist.",
                    "Thank you for laughing at my jokes before deciding if they are funny.",
                    "Our friendship is proof that bad ideas can have excellent emotional support.",
                    "Happy Friendship Day to the only person allowed to judge me accurately.",
                ],
            },
            {
                "key": "long_distance",
                "h2": "Long Distance Friendship Day Quotes",
                "lines": [
                    "Distance changes plans, not the place you hold in my heart.",
                    "We may not meet often, but our friendship still feels close.",
                    "A real friend can live far away and still feel like the nearest person.",
                    "Happy Friendship Day from miles away. I miss our talks, our laughter, and our random plans.",
                    "Distance has only proved that our bond is not built on convenience.",
                    "Some friendships survive time zones because the love is honest.",
                    "I may not see you every week, but I still carry your friendship every day.",
                    "Happy Friendship Day. One call with you still fixes my mood.",
                    "The best friendships do not need constant presence, only constant care.",
                    "Until we meet again, know that you are missed and celebrated.",
                ],
            },
        ],
        "faqs": [
            ["What are good emotional Friendship Day quotes for 2026?", "Good emotional Friendship Day quotes for 2026 should feel honest, warm, and personal. Choose a line that mentions loyalty, comfort, memories, or support, then add your friend’s name or one shared moment. A simple quote works best when it sounds like your real friendship."],
            ["What is a one line caption for best friend?", "A good one line caption for best friend is short, affectionate, and easy to understand without context. Try lines like “My person in every season” or “Chosen family, real bond.” Keep it natural and avoid making the caption longer than the photo needs."],
            ["What can I write in a few lines for best friend?", "In a few lines for best friend, thank them for staying, listening, and making life easier. Mention one quality you genuinely value, such as loyalty or humour. The best message feels specific, not copied, even when you begin with a ready line."],
            ["What are girl gang quotes for Friendship Day?", "Girl gang quotes for Friendship Day celebrate shared confidence, laughter, support, and the group chat that holds everything together. Use them for photos with your closest women friends, especially when the mood is playful, stylish, and emotionally warm."],
            ["When is Friendship Day 2026 in India?", "Friendship Day 2026 in India falls on Sunday, August 2. Many people in India celebrate it on the first Sunday of August with messages, captions, small gifts, and plans with close friends. You can send your message the same morning or post it with photos through the day."],
        ],
    }

    carousel_names = [
        "The Kricia Charm Bracelet",
        "The Malocchio Charm Holder Bracelet",
        "The Tapia Chain Bracelet",
        "The Haily Ring",
        "The Aleena Huggie Earrings",
        "The Teshvarya Pendant",
    ]
    hero = consolidated(detail_rows, "The Elize Evil Eye Bracelet")
    flatlay = consolidated(detail_rows, "The Gigi Ring")
    lifestyle = consolidated(detail_rows, "The Vicky Hoop Earrings")
    cfg = {
        "rank": "Week3-4 Rank 4",
        "sections_json": f"output/{prefix}_sections.json",
        "output_prefix": prefix,
        "carousel_id": "bs-cf-friendshipquotes",
        "occasion_year": "Friendship Day 2026",
        "carousel_alt_prefix": "emotional Friendship Day quotes 2026 gift idea",
        "gift_h2": "Friendship Day Gift Ideas",
        "gift_blurb": "If your message is going with a small gift, choose something wearable and easy to keep beyond Friendship Day. These BlueStone picks feel thoughtful without turning the post into a product list.",
        "conclusion_html": "Emotional Friendship Day quotes work best when they sound like your real bond. Choose one line, add a tiny memory, and send it before the day becomes only another story update.",
        "schema_keywords": ["emotional friendship day quotes", "instagram short best friend quotes", "one line caption for best friend", "few lines for best friend", "girl gang quotes", "best friendship day quotes", "happy friendship day quotes wishes"],
        "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
        "products": [product(product_rows, name) for name in carousel_names],
        "flatlay_insert_h2": "Girl Gang Quotes",
        "lifestyle_insert_h2": "Happy Friendship Day Quotes Wishes",
        "more_reads_html": 'Read more celebration lines in <a href="https://blog.bluestone.com/friendship-day-photos-2026/">Friendship Day photos 2026</a>, <a href="https://blog.bluestone.com/mother-daughter-quotes-2026/">mother daughter quotes 2026</a>, <a href="https://blog.bluestone.com/diwali-quotes-for-instagram-2026/">Diwali quotes for Instagram 2026</a>, and <a href="https://blog.bluestone.com/new-year-wishes-for-love-2026/">New Year wishes for love 2026</a>.',
        "how_to_html": 'In India, Friendship Day 2026 falls on Sunday, August 2. For date context, see <a href="https://www.timeanddate.com/holidays/india/friendship-day">Timeanddate on Friendship Day in India</a>. Use an emotional quote for a close friend, a short caption for photos, and a funny line when the bond is playful.',
        "faq_h2": "Frequently Asked Questions about Friendship Day Quotes",
        "min_lines": 100,
    }
    prompts = {
        "rank": "Week3-4 Rank 4",
        "slug": sections["meta"]["slug"],
        "primary_kw": sections["meta"]["focus_kw"],
        "output_prefix": prefix,
        "caption_occasion": "Friendship Day quotes",
        "caption_year": "2026",
        "flatlay_setting": "cafe-tray",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/emotional-friendship-day-quotes-hero-2026.webp",
            "flatlay": "output/magnific_generated/emotional-friendship-day-quotes-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/emotional-friendship-day-quotes-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "emotional Friendship Day quotes 2026 Hero",
            "flatlay": "emotional Friendship Day quotes 2026 Flatlay",
            "lifestyle": "emotional Friendship Day quotes 2026 Lifestyle",
        },
        "schema_keywords": cfg["schema_keywords"],
        "slots": {
            "hero": {
                **hero,
                "alt": "emotional Friendship Day quotes 2026 hero with The Elize Evil Eye Bracelet",
                "caption": "Friendship Day quotes 2026 mood: The Elize Evil Eye Bracelet",
                "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]},
                "local_reference_images": [
                    raw_image("Bracelets", "The Elize Evil Eye Bracelet", "1_body_portrait.png"),
                    raw_image("Bracelets", "The Elize Evil Eye Bracelet", "0_primary.png"),
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": prompt_people(
                    occasion="Emotional Friendship Day quotes 2026 hero",
                    scene="two fair-skinned Indian adult women best friends in a bright cafe, one friend laughs while sliding a completely blank cream note card across the table, full faces visible, warm candid friendship mood",
                    product_name=hero["name"],
                    product=hero,
                    body_part="wrist",
                ),
            },
            "flatlay": {
                **flatlay,
                "alt": "emotional Friendship Day quotes 2026 flatlay with The Gigi Ring",
                "caption": "Friendship Day quotes 2026 vibe: The Gigi Ring",
                "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]},
                "local_reference_images": [
                    raw_image("Rings", "The Gigi Ring", "0_primary.png"),
                    raw_image("Rings", "The Gigi Ring", "2_front.png"),
                    raw_image("Rings", "The Gigi Ring", "6_angle.png"),
                ],
                "ref_roles": ["primary", "front", "angle"],
                "prompt": prompt_flatlay(
                    occasion="Emotional Friendship Day quotes 2026",
                    setting="cafe-tray",
                    setting_prompt="a ceramic tray on soft stoneware, plain espresso cup and saucer, folded napkin, blank cream friendship card, no text",
                    product_name=flatlay["name"],
                    product=flatlay,
                ),
            },
            "lifestyle": {
                **lifestyle,
                "alt": "emotional Friendship Day quotes 2026 lifestyle with The Vicky Hoop Earrings",
                "caption": "Friendship Day quotes 2026 look: The Vicky Hoop Earrings",
                "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]},
                "local_reference_images": [
                    raw_image("Earrings", "The Vicky Hoop Earrings", "1_body_portrait.png"),
                    raw_image("Earrings", "The Vicky Hoop Earrings", "0_primary.png"),
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": prompt_people(
                    occasion="Emotional Friendship Day quotes 2026 lifestyle",
                    scene="solo fair-skinned Indian adult woman in a soft ivory top smiling while looking at a blank phone screen in a cozy cafe corner, friendship gift bag blurred in background, full head and both ears visible, hands mostly out of frame",
                    product_name=lifestyle["name"],
                    product=lifestyle,
                    body_part="ear",
                    extra_negatives="readable phone screen",
                ),
            },
        },
    }
    write_json(f"output/{prefix}_sections.json", sections)
    write_json(f"output/publish_configs/week34_rank4.json", cfg)
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    checklist = f"""# Blog SEO + AEO/GEO Checklist v2, Week 3-4 Rank 4

Article: Emotional Friendship Day Quotes 2026
Status: Draft assets prepared
Date: 2026-07-28

## Gates
- [x] Primary keyword: emotional friendship day quotes
- [x] Optimize treated as New
- [x] Fresh slug: emotional-friendship-day-quotes-2026
- [x] Friendship Day 2026 date checked: August 2, 2026
- [x] Carousel products from ProductImages/seo images only
- [x] Type 3 hero and lifestyle use body_image plus design refs
- [x] Product dimension wording uses product dimensions, not face size
- [x] Filmic prompt language included
- [ ] WordPress post published
- [ ] Type 3 images generated and patched
- [ ] Live URL verified
"""
    (ROOT / f"output/{prefix}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


def build_rank5(product_rows: dict[str, dict[str, str]], detail_rows: dict[str, dict[str, str]]) -> None:
    prefix = "Week34_Rank5_RakhiGiftSister"
    sections = {
        "meta": {
            "title": "Best Gift for Sister on Raksha Bandhan 2026",
            "slug": "best-gift-for-sister-on-raksha-bandhan-2026",
            "meta_desc": "Best gift for sister on Raksha Bandhan 2026 with thoughtful jewellery ideas, unique Rakhi gifts, note lines, and tips to pick a lasting keepsake for her.",
            "focus_kw": "best gift for sister on raksha bandhan",
            "yoast_title": "Best Gift for Sister on Raksha Bandhan 2026",
        },
        "intro": [
            "The best gift for sister on Raksha Bandhan is something personal, wearable, and chosen with her everyday style in mind. Raksha Bandhan 2026 falls on Friday, August 28, so this guide helps you shortlist jewellery gifts, note ideas, and simple ways to make the gesture feel thoughtful.",
            "TL;DR: Pick a bracelet for daily wear, earrings for effortless styling, a pendant for a keepsake, a ring for a personal surprise, and a bangle when she likes festive statement pieces.",
        ],
        "sections": [
            {
                "key": "best",
                "h2": "Best Gift for Sister on Raksha Bandhan",
                "lines": [
                    "Choose a gift she can wear after the festival, not something that feels useful for one day only.",
                    "Look at her current jewellery style before choosing: minimal, colourful, classic, playful, or festive.",
                    "A bracelet is a strong Rakhi option because it feels close to the symbolism of the thread.",
                    "A pendant works well when you want a keepsake she can wear with workwear and festive outfits.",
                    "Earrings are a safe choice if you know she enjoys easy everyday styling.",
                    "A ring feels personal, so choose it when you know her size or preferred fit.",
                    "Evil eye jewellery can feel meaningful for a sister because it carries a protective sentiment.",
                    "Gold and diamond designs work best when the gift needs to feel lasting without being loud.",
                    "Add a handwritten note, because the words often become as memorable as the gift.",
                    "Avoid buying only by trend. Her real lifestyle should lead the choice.",
                ],
            },
            {
                "key": "best_rakhi",
                "h2": "Best Rakhi Gift for Sister",
                "lines": [
                    "A daily wear bracelet suits sisters who like light pieces they can keep on often.",
                    "A charm bracelet is thoughtful when she likes jewellery with a story or symbol.",
                    "Studs or huggies work well for a sister who prefers comfort and low-maintenance style.",
                    "A delicate pendant is ideal when you want a keepsake that feels emotional but versatile.",
                    "A bangle is a good choice for sisters who enjoy festive dressing and visible sparkle.",
                    "A ring can become a sweet surprise if she already wears rings regularly.",
                    "For a younger sister, choose something playful, protective, and easy to style.",
                    "For an elder sister, choose something elegant, polished, and meaningful.",
                    "For a married sister, choose a piece that suits both daily routines and festive visits.",
                    "For a long-distance sister, choose a gift that can travel safely and still feel personal.",
                ],
            },
            {
                "key": "top10",
                "h2": "Top 10 Rakhi Gifts for Sister",
                "lines": [
                    "A protective evil eye bracelet for everyday wear.",
                    "A charm bracelet with a soft festive story.",
                    "A dainty pendant she can layer or wear solo.",
                    "Diamond huggie earrings for a neat daily look.",
                    "A minimal gold ring for a personal keepsake.",
                    "A polished bangle for festive outfits.",
                    "A heart or floral pendant for a romantic soft style.",
                    "A chain bracelet for clean office-friendly styling.",
                    "A small jewellery gift with a handwritten Rakhi note.",
                    "A piece that matches her current wardrobe instead of only the festival mood.",
                ],
            },
            {
                "key": "good_gift",
                "h2": "Good Gift for Raksha Bandhan",
                "lines": [
                    "A good Raksha Bandhan gift feels useful, emotional, and easy for your sister to wear.",
                    "If she dresses simply, pick a clean piece with one beautiful detail.",
                    "If she loves colour, look for a gemstone, enamel, or evil eye accent.",
                    "If she has a busy work life, choose compact earrings or a bracelet that does not snag.",
                    "If she loves festive photos, choose a bangle, pendant, or ring with visible polish.",
                    "If she is sentimental, add a message that explains why you chose that design.",
                    "If you are unsure, choose jewellery that sits close to daily styling rather than heavy occasion wear.",
                    "If you are gifting from far away, keep the message warm and the design practical.",
                    "If she already owns many earrings, try a bracelet or pendant instead.",
                    "If she likes meaningful symbols, protective motifs can make the gift feel more personal.",
                ],
            },
            {
                "key": "ideas",
                "h2": "Raksha Bandhan Gifts for Sister Ideas",
                "lines": [
                    "For the minimalist sister, pick a slim chain bracelet or small huggie earrings.",
                    "For the expressive sister, choose a ring, charm bracelet, or colourful accent piece.",
                    "For the traditional sister, a bangle or pendant can feel festive and graceful.",
                    "For the college-going sister, choose a compact piece she can wear with casual looks.",
                    "For the working sister, choose jewellery that looks polished without being distracting.",
                    "For the sister who travels, choose secure earrings or a light pendant.",
                    "For the sister who loves Instagram, choose a piece that photographs beautifully.",
                    "For the sister who loves symbols, choose evil eye or floral details.",
                    "For the sister who prefers classics, choose gold tones and clean shapes.",
                    "For the sister who says she wants nothing, gift something small with a very personal note.",
                ],
            },
            {
                "key": "unique",
                "h2": "Unique Gifts for Sister on Rakhi",
                "lines": [
                    "Make a jewellery gift unique by connecting it to a memory, not only the design.",
                    "Choose an evil eye detail if you want the gift to say, I wish you protection.",
                    "Choose a charm bracelet if your sister likes small details with meaning.",
                    "Choose a ring if you want the gift to feel personal and unexpected.",
                    "Choose huggies if she likes pieces she can wear from morning to evening.",
                    "Choose a pendant if you want a keepsake that stays close to the heart.",
                    "Add a blank card with one handwritten line instead of a long printed message.",
                    "Wrap the gift with a rakhi, roli chawal, and a simple note for a complete festive feel.",
                    "Pair the jewellery with a photo memory if you want the gift to feel intimate.",
                    "The most unique gift is the one that looks like her, not just like a trend.",
                ],
            },
            {
                "key": "note",
                "h2": "Rakhi Gift Note for Sister",
                "lines": [
                    "This is a small gift for the sister who has made my life brighter in so many ways.",
                    "Wear this as a little reminder that I am always cheering for you.",
                    "Happy Raksha Bandhan. May this gift carry love, protection, and every good wish.",
                    "I chose this because it felt like you: graceful, strong, and full of warmth.",
                    "Thank you for being my sister, my guide, and my favourite critic.",
                    "This gift is not enough to match what you mean to me, but it carries my heart.",
                    "May you always feel protected, loved, and celebrated.",
                    "For every fight, every secret, and every memory, Happy Rakhi.",
                    "A little sparkle for the sister who brings light into our home.",
                    "Keep this close as a reminder that your brother is always on your side.",
                ],
            },
            {
                "key": "budgetless",
                "h2": "How to Choose Without Talking About Budget",
                "lines": [
                    "Focus on how often she will wear the piece.",
                    "Check whether she prefers yellow gold, rose tones, white tones, or mixed styling.",
                    "Notice if she wears more earrings, bracelets, rings, or pendants.",
                    "Think about her daily routine before choosing anything too delicate or heavy.",
                    "Choose secure clasps and comfortable shapes for everyday wear.",
                    "Avoid guessing ring size unless you can check an existing ring discreetly.",
                    "Prefer a design that can move from office to dinner to festive gatherings.",
                    "Let the note explain the emotion behind the gift.",
                    "Keep the packaging simple, clean, and festive.",
                    "If in doubt, choose a timeless design with one meaningful detail.",
                ],
            },
        ],
        "faqs": [
            ["What is the best gift for sister on Raksha Bandhan?", "The best gift for sister on Raksha Bandhan is something she can use beyond the festival, such as a bracelet, pendant, earrings, ring, or bangle chosen around her personal style. A handwritten note makes the gift feel more thoughtful and less generic."],
            ["What are the top 10 Rakhi gifts for sister?", "Top Rakhi gifts for sister include bracelets, charm bracelets, pendants, huggie earrings, rings, bangles, evil eye jewellery, floral designs, simple gold pieces, and a personalised note. Choose based on her routine, not only the festival mood."],
            ["What is a good gift for Raksha Bandhan if my sister likes simple jewellery?", "A good gift for Raksha Bandhan for a sister who likes simple jewellery is a slim bracelet, small huggie earrings, a delicate pendant, or a minimal ring. Pick clean shapes and comfortable designs she can wear often."],
            ["What are unique gifts for sister on Rakhi?", "Unique gifts for sister on Rakhi are gifts tied to meaning: an evil eye motif for protection, a charm bracelet for memories, a pendant for closeness, or a ring for a personal surprise. Add a note explaining why you chose it."],
            ["When is Raksha Bandhan 2026?", "Raksha Bandhan 2026 falls on Friday, August 28. If you are sending a gift to your sister, plan ahead for delivery and keep the note short, warm, and specific to your bond."],
        ],
    }
    carousel_names = [
        "The Elize Evil Eye Bracelet",
        "The Pervinca Charm Holder Bracelet",
        "The Shining Star Bracelet",
        "The Lumeelle Cluster Pendant",
        "The Asya Huggie Earrings",
        "The Estrella Oval Bangle",
    ]
    hero = consolidated(detail_rows, "The Kricia Charm Bracelet")
    flatlay = consolidated(detail_rows, "The Pear Evil Eye Toggle Bangle")
    lifestyle = consolidated(detail_rows, "The Thaloria Pendant")
    cfg = {
        "rank": "Week3-4 Rank 5",
        "sections_json": f"output/{prefix}_sections.json",
        "output_prefix": prefix,
        "carousel_id": "bs-cf-rakhigiftsister",
        "occasion_year": "Raksha Bandhan 2026",
        "carousel_alt_prefix": "best gift for sister on Raksha Bandhan 2026 gift idea",
        "gift_h2": "Jewellery Gift Ideas for Sister",
        "gift_blurb": "Here are six BlueStone picks that suit different sister styles, from everyday bracelets to festive accents. Use them as a starting point, then choose the one that feels most like her.",
        "conclusion_html": "The best gift for sister on Raksha Bandhan is not only the most decorative one. It is the one that understands her style, carries your blessing, and stays useful after the festival morning.",
        "schema_keywords": ["best gift for sister on raksha bandhan", "best rakhi gift for sister", "top 10 rakhi gifts for sister", "good gift for raksha bandhan", "raksha bandhan gifts for sister ideas", "unique gifts for sister on rakhi"],
        "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
        "products": [product(product_rows, name) for name in carousel_names],
        "flatlay_insert_h2": "Top 10 Rakhi Gifts for Sister",
        "lifestyle_insert_h2": "Unique Gifts for Sister on Rakhi",
        "more_reads_html": 'Read more Rakhi ideas in <a href="https://blog.bluestone.com/happy-rakhi-wishes-to-brother-2026/">happy Rakhi wishes to brother 2026</a>, <a href="https://blog.bluestone.com/rakhi-for-bhaiya-bhabhi-2026/">rakhi for bhaiya bhabhi 2026</a>, <a href="https://blog.bluestone.com/raksha-bandhan-gifts-for-brother-2026/">Raksha Bandhan gifts for brother 2026</a>, and <a href="https://blog.bluestone.com/raksha-bandhan-hindi-2026/">Raksha Bandhan Hindi 2026</a>.',
        "how_to_html": 'Raksha Bandhan 2026 falls on Friday, August 28. For muhurat context, see <a href="https://www.drikpanchang.com/festivals/raksha-bandhan/raksha-bandhan-date-time.html?geoname-id=1273294">Drik Panchang on Raksha Bandhan 2026</a>. If you are gifting jewellery, match the design to her daily style first, then add a note that explains the emotion.',
        "faq_h2": "Frequently Asked Questions about Rakhi Gifts for Sister",
        "min_lines": 80,
    }
    prompts = {
        "rank": "Week3-4 Rank 5",
        "slug": sections["meta"]["slug"],
        "primary_kw": sections["meta"]["focus_kw"],
        "output_prefix": prefix,
        "caption_occasion": "Rakhi gift for sister",
        "caption_year": "2026",
        "flatlay_setting": "gift-wrapping-station",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/best-gift-for-sister-on-raksha-bandhan-hero-2026.webp",
            "flatlay": "output/magnific_generated/best-gift-for-sister-on-raksha-bandhan-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/best-gift-for-sister-on-raksha-bandhan-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "best gift for sister on Raksha Bandhan 2026 Hero",
            "flatlay": "best gift for sister on Raksha Bandhan 2026 Flatlay",
            "lifestyle": "best gift for sister on Raksha Bandhan 2026 Lifestyle",
        },
        "schema_keywords": cfg["schema_keywords"],
        "slots": {
            "hero": {
                **hero,
                "alt": "best gift for sister on Raksha Bandhan 2026 hero with The Kricia Charm Bracelet",
                "caption": "Rakhi gift for sister 2026 mood: The Kricia Charm Bracelet",
                "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]},
                "local_reference_images": [
                    raw_image("Bracelets", "The Kricia Charm Bracelet", "1_body_portrait.png"),
                    raw_image("Bracelets", "The Kricia Charm Bracelet", "0_primary.png"),
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": prompt_people(
                    occasion="Best gift for sister on Raksha Bandhan 2026 hero",
                    scene="fair-skinned Indian adult sister seated in a warm modern Indian living room beside a rakhi thali and a blank cream gift card, smiling softly while holding the card near a wrapped gift, full face visible, one wrist naturally visible",
                    product_name=hero["name"],
                    product=hero,
                    body_part="wrist",
                ),
            },
            "flatlay": {
                **flatlay,
                "alt": "best gift for sister on Raksha Bandhan 2026 flatlay with The Pear Evil Eye Toggle Bangle",
                "caption": "Rakhi gift for sister 2026 vibe: The Pear Evil Eye Toggle Bangle",
                "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]},
                "local_reference_images": [
                    raw_image("Bangles", "The Pear Evil Eye Toggle Bangle", "0_primary.png"),
                    raw_image("Bangles", "The Pear Evil Eye Toggle Bangle", "3_side_1.png"),
                    raw_image("Bangles", "The Pear Evil Eye Toggle Bangle", "5_angle.png"),
                ],
                "ref_roles": ["primary", "side", "angle"],
                "prompt": prompt_flatlay(
                    occasion="Best gift for sister on Raksha Bandhan 2026",
                    setting="gift-wrapping-station",
                    setting_prompt="warm kraft paper roll surface, folded cream cloth, matte scissors, twine, roli chawal bowl, small diya, completely blank gift tag",
                    product_name=flatlay["name"],
                    product=flatlay,
                ),
            },
            "lifestyle": {
                **lifestyle,
                "alt": "best gift for sister on Raksha Bandhan 2026 lifestyle with The Thaloria Pendant",
                "caption": "Rakhi gift for sister 2026 look: The Thaloria Pendant",
                "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]},
                "local_reference_images": [
                    raw_image("Pendants", "The Thaloria Pendant", "1_body_portrait.png"),
                    raw_image("Pendants", "The Thaloria Pendant", "0_primary.png"),
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": prompt_people(
                    occasion="Best gift for sister on Raksha Bandhan 2026 lifestyle",
                    scene="fair-skinned Indian adult woman in an ivory kurta near softly blurred Rakhi decor, upper torso portrait, full head, full face, neck, pendant, shoulders, and upper chest visible, hands and wrists completely out of frame",
                    product_name=lifestyle["name"],
                    product=lifestyle,
                    body_part="neck",
                    extra_negatives="hands, wrists",
                ),
            },
        },
    }
    write_json(f"output/{prefix}_sections.json", sections)
    write_json(f"output/publish_configs/week34_rank5.json", cfg)
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    checklist = f"""# Blog SEO + AEO/GEO Checklist v2, Week 3-4 Rank 5

Article: Best Gift for Sister on Raksha Bandhan 2026
Status: Draft assets prepared
Date: 2026-07-28

## Gates
- [x] Primary keyword: best gift for sister on raksha bandhan
- [x] Optimize treated as New
- [x] Fresh slug: best-gift-for-sister-on-raksha-bandhan-2026
- [x] Raksha Bandhan 2026 date checked: August 28, 2026
- [x] Carousel products from ProductImages/seo images only
- [x] Type 3 hero and lifestyle use body_image plus design refs
- [x] Product dimension wording uses product dimensions, not face size
- [x] Filmic prompt language included
- [ ] WordPress post published
- [ ] Type 3 images generated and patched
- [ ] Live URL verified
"""
    (ROOT / f"output/{prefix}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


def main() -> None:
    product_rows = load_csv("Seo Products - final products (1).csv")
    detail_rows = load_csv("Seo Products - consolidated.csv")
    build_rank4(product_rows, detail_rows)
    build_rank5(product_rows, detail_rows)
    print("built Week 3-4 Rank 4 and Rank 5 configs")


if __name__ == "__main__":
    main()
