#!/usr/bin/env python3
"""Build Week 3-4 Rank 7 and Rank 8 assets."""
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
        "No readable text anywhere. Any card, tag, notebook, diya label, laptop, or phone screen must be completely blank.\n\n"
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


def build_rank7(product_rows: dict[str, dict[str, str]], detail_rows: dict[str, dict[str, str]]) -> None:
    prefix = "Week34_Rank7_RomanticDiwaliLover"
    sections = {
        "meta": {
            "title": "Romantic Diwali Wishes for Lover 2026",
            "slug": "romantic-diwali-wishes-for-lover-2026",
            "meta_desc": "Romantic Diwali wishes for lover 2026 with sweet messages, captions, quotes, long notes, short lines, and heartfelt words to share festival love today.",
            "focus_kw": "romantic diwali wishes for lover",
            "yoast_title": "Romantic Diwali Wishes for Lover 2026",
        },
        "intro": [
            "Romantic Diwali wishes for lover should feel warm, bright, and personal, like a small diya kept only for the two of you. Use this 2026 collection for WhatsApp, cards, Instagram captions, and thoughtful notes when you want festival love to sound sincere.",
            "TL;DR: Pick a short line for chat, a deeper message for a card, a caption for couple photos, and a sweet gift note if your Diwali wish is going with jewellery.",
        ],
        "sections": [
            {"key": "main", "h2": "Romantic Diwali Wishes for Lover", "lines": [
                "Happy Diwali, my love. May our bond shine brighter than every diya tonight.",
                "This Diwali, I am grateful for your love, your smile, and the light you bring into my life.",
                "May every lamp we light remind us of the warmth we have found in each other.",
                "Happy Diwali to the person who makes my ordinary days feel festive.",
                "Your love is my favourite light, steady, soft, and always close to my heart.",
                "May this Diwali fill our story with more laughter, trust, and beautiful memories.",
                "With you, every celebration feels warmer and every prayer feels more complete.",
                "Happy Diwali, sweetheart. I hope our love keeps glowing through every season.",
                "You are the sparkle I was hoping life would bring me.",
                "This festival of lights feels special because I get to think of you.",
                "May our hearts stay bright, patient, honest, and full of love.",
                "Happy Diwali, my love. You make my world feel beautifully lit from within.",
            ]},
            {"key": "girlfriend", "h2": "Diwali Love Messages for Girlfriend", "lines": [
                "Happy Diwali to the woman who makes my heart feel calm and excited at the same time.",
                "Your smile has more light than the brightest Diwali evening.",
                "May this Diwali bring you joy, peace, and every dream your heart is holding.",
                "I wish I could light every diya with a thank you for having you in my life.",
                "Happy Diwali, beautiful. You make love feel gentle, safe, and full of hope.",
                "May your day be as bright as your heart and as graceful as your presence.",
                "You are my favourite blessing this Diwali and every day after it.",
                "Sending you love wrapped in lights, prayers, and a little extra romance.",
                "Happy Diwali to my favourite person, my best thought, and my brightest wish.",
                "May this festival bring us closer in all the quiet ways that matter.",
            ]},
            {"key": "boyfriend", "h2": "Diwali Wishes for Boyfriend", "lines": [
                "Happy Diwali to the man who makes my heart feel protected and cherished.",
                "May your Diwali be full of success, peace, sweets, and my love.",
                "You make every festival feel like a memory worth keeping.",
                "Happy Diwali, love. I am proud of the person you are and the dreams you chase.",
                "May your life glow with confidence, kindness, and steady happiness.",
                "This Diwali, I am sending you prayers, hugs, and all my heart.",
                "You are my calm in busy days and my sparkle in festive nights.",
                "Happy Diwali to the one who makes love feel simple and strong.",
                "May every diya bring you luck and every moment remind you that you are loved.",
                "With you, Diwali feels less like a day and more like home.",
            ]},
            {"key": "my_love", "h2": "Happy Diwali My Love", "lines": [
                "Happy Diwali, my love. May our hearts stay close even when life gets busy.",
                "My love, you are the light I wait for at the end of every day.",
                "Happy Diwali to the person I want beside me in every celebration.",
                "May this Diwali bring us more patience, more laughter, and more reasons to believe.",
                "My love, you make the festival feel softer and brighter.",
                "Happy Diwali. I hope your smile stays as warm as the lamps around us.",
                "Every diya looks more beautiful when I am thinking of you.",
                "My love, may our bond be blessed with trust, joy, and a future full of light.",
                "Happy Diwali from my heart to yours, with all the love I cannot fit into words.",
                "You are my favourite wish this Diwali.",
            ]},
            {"key": "quotes", "h2": "Romantic Diwali Quotes", "lines": [
                "Love is the diya that keeps glowing when the night feels long.",
                "The brightest Diwali is the one celebrated with the person your heart calls home.",
                "A festival becomes a memory when love is standing beside it.",
                "Some lights decorate the room. Some people decorate the heart.",
                "Diwali teaches us that even a small flame can make love feel endless.",
                "When love is true, every festival finds a deeper meaning.",
                "Your presence is the light I never want to lose.",
                "The sweetest Diwali gift is a heart that chooses you with honesty.",
                "Love glows best when it is patient, loyal, and kind.",
                "A diya lasts one evening, but a loving memory can shine for years.",
            ]},
            {"key": "short", "h2": "Short Romantic Diwali Wishes", "lines": [
                "Happy Diwali, my love.",
                "You are my brightest light.",
                "Diwali feels better with you.",
                "Love, light, and us.",
                "My heart celebrates you.",
                "You are my festive glow.",
                "Happy Diwali, sweetheart.",
                "Forever my favourite wish.",
                "Shining brighter with you.",
                "You make Diwali beautiful.",
            ]},
            {"key": "captions", "h2": "Diwali Captions for Couples", "lines": [
                "Two hearts, one festive glow.",
                "Diwali lights and love-filled nights.",
                "Celebrating us under a thousand lamps.",
                "My favourite Diwali view is you.",
                "Love made the lights brighter.",
                "Festive hearts, matching smiles.",
                "Diwali with my forever person.",
                "Our love, glowing softly.",
                "Sweets, lights, and your hand in mine.",
                "A little sparkle, a lot of love.",
            ]},
            {"key": "long", "h2": "Long Romantic Diwali Messages", "lines": [
                "Happy Diwali, my love. I hope this festival brings peace to your heart, success to your path, and more beautiful moments for us to share.",
                "This Diwali, I want you to know how deeply your love has changed my days. You make life feel warmer, kinder, and worth celebrating.",
                "May every diya we light carry a prayer for our future, one filled with trust, laughter, patience, and a love that keeps choosing us.",
                "Happy Diwali, sweetheart. Even when we are apart, my heart celebrates you with every lamp, every prayer, and every quiet wish.",
                "You are not just part of my Diwali. You are part of the hope I carry into every new beginning.",
                "May this festival remind us that love is not only grand moments. It is the small steady light we keep for each other.",
                "Happy Diwali to the person who makes my life feel blessed in ways I did not know how to ask for.",
                "I hope our love keeps growing brighter, not only tonight, but through all the ordinary mornings that follow.",
            ]},
            {"key": "deepavali", "h2": "Deepavali Wishes for Love", "lines": [
                "Happy Deepavali, my love. May light, peace, and sweetness surround you today.",
                "Wishing you a Deepavali filled with blessings and a heart full of my love.",
                "May this Deepavali make our bond stronger and our dreams clearer.",
                "Happy Deepavali to the one who brings brightness into my life every day.",
                "May our love glow like lamps that never lose their warmth.",
                "Sending Deepavali wishes to the person who makes my heart feel at home.",
                "May the festival bring us closer, kinder, and more grateful for each other.",
                "Happy Deepavali, sweetheart. You are the best part of my celebration.",
                "May your day shine with joy and your heart feel deeply loved.",
                "This Deepavali, I am thankful for you, for us, and for every light ahead.",
            ]},
        ],
        "faqs": [
            ["What are the best romantic Diwali wishes for lover in 2026?", "The best romantic Diwali wishes for lover in 2026 are warm, personal, and easy to send. Choose a line that mentions light, love, blessings, or togetherness, then add your partners name or one memory that belongs only to you both."],
            ["How do I say Happy Diwali my love?", "Say Happy Diwali my love with a short message that feels sincere. You can write, Happy Diwali, my love. May our bond keep glowing with trust, joy, and beautiful memories. It works well for WhatsApp, cards, and captions."],
            ["What can I write in a Diwali card for my girlfriend?", "In a Diwali card for your girlfriend, write one wish, one compliment, and one hope for your future together. Keep it respectful and specific, such as appreciating her smile, support, kindness, or the warmth she brings into your life."],
            ["What is a sweet Diwali message for boyfriend?", "A sweet Diwali message for boyfriend should celebrate his presence and your bond. Wish him peace, success, and happiness, then add a loving line that makes the message feel like it came from you, not a generic greeting."],
            ["Can I send romantic Diwali captions with couple photos?", "Yes, romantic Diwali captions work beautifully with couple photos when they are short and warm. Use captions about lights, love, togetherness, festive memories, or your favourite person, and avoid anything too long for a visual post."],
        ],
    }
    carousel_names = ["The Valeria Rose Pendant", "The Gigi Ring", "The Rohal Huggie Earrings", "The Kricia Charm Bracelet", "The Pear Evil Eye Toggle Bangle", "The Channing Bangle"]
    hero = consolidated(detail_rows, "The Sarvanya Pendant")
    flatlay = consolidated(detail_rows, "The Haily Ring")
    lifestyle = consolidated(detail_rows, "The Vicky Hoop Earrings")
    cfg = {
        "rank": "Week3-4 Rank 7",
        "sections_json": f"output/{prefix}_sections.json",
        "output_prefix": prefix,
        "carousel_id": "bs-cf-romanticdiwalilover",
        "occasion_year": "Diwali 2026",
        "carousel_alt_prefix": "romantic Diwali wishes for lover 2026 gift idea",
        "gift_h2": "Romantic Diwali Gift Ideas",
        "gift_blurb": "If your Diwali wish is going with a keepsake, choose something personal and wearable rather than loud. These BlueStone pieces pair naturally with a romantic note, a blank card, and a festival evening.",
        "conclusion_html": "Romantic Diwali wishes for lover work best when they feel like your real relationship. Pick one line, add a private detail, and send it with love that stays bright after the lamps go out.",
        "schema_keywords": ["romantic diwali wishes for lover", "happy diwali my love", "diwali wishes for boyfriend", "diwali love messages for girlfriend", "romantic diwali quotes", "diwali captions for couples"],
        "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
        "products": [product(product_rows, name) for name in carousel_names],
        "flatlay_insert_h2": "Romantic Diwali Quotes",
        "lifestyle_insert_h2": "Short Romantic Diwali Wishes",
        "more_reads_html": 'Read more festival lines in <a href="https://blog.bluestone.com/diwali-wishes-and-quotes-2026/">Diwali wishes and quotes</a>, <a href="https://blog.bluestone.com/diwali-quotes-for-instagram-2026/">Diwali captions for Instagram</a>, <a href="https://blog.bluestone.com/new-year-wishes-for-love-2026/">New Year wishes for love</a>, and <a href="https://blog.bluestone.com/happy-womens-day-wishes-quotes-2027/">Womens Day wishes</a>.',
        "how_to_html": "Choose a short romantic line for WhatsApp, a longer message for a card, and a simple caption for couple photos. Keep the tone affectionate, respectful, and specific to your relationship.",
        "faq_h2": "Frequently Asked Questions about Romantic Diwali Wishes",
        "min_lines": 80,
    }
    prompts = {
        "rank": "Week3-4 Rank 7",
        "slug": sections["meta"]["slug"],
        "primary_kw": sections["meta"]["focus_kw"],
        "output_prefix": prefix,
        "caption_occasion": "Romantic Diwali wishes",
        "caption_year": "2026",
        "flatlay_setting": "marble-vanity",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/romantic-diwali-wishes-for-lover-hero-2026.webp",
            "flatlay": "output/magnific_generated/romantic-diwali-wishes-for-lover-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/romantic-diwali-wishes-for-lover-lifestyle-2026.webp",
        },
        "media_titles": {"hero": "romantic Diwali wishes for lover 2026 Hero", "flatlay": "romantic Diwali wishes for lover 2026 Flatlay", "lifestyle": "romantic Diwali wishes for lover 2026 Lifestyle"},
        "schema_keywords": cfg["schema_keywords"],
        "slots": {
            "hero": {**hero, "alt": "romantic Diwali wishes for lover 2026 hero with The Sarvanya Pendant", "caption": "Romantic Diwali wishes 2026 mood: The Sarvanya Pendant", "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]}, "local_reference_images": [raw_image("Pendants", "The Sarvanya Pendant", "1_body_portrait.png"), raw_image("Pendants", "The Sarvanya Pendant", "0_primary.png")], "ref_roles": ["body_image", "front_primary"], "prompt": prompt_people(occasion="Romantic Diwali wishes for lover 2026 hero", scene="solo fair-skinned Indian adult woman in an elegant ivory festive kurta seated beside soft Diwali diyas, smiling while holding a completely blank cream love note card near her heart, full face visible, neck and pendant clearly visible, warm intimate home celebration mood", product_name=hero["name"], product=hero, body_part="neck", extra_negatives="large pendant, pendant covering chest, crowded decorations")},
            "flatlay": {**flatlay, "alt": "romantic Diwali wishes for lover 2026 flatlay with The Haily Ring", "caption": "Romantic Diwali wishes 2026 vibe: The Haily Ring", "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]}, "local_reference_images": [raw_image("Rings", "The Haily Ring", "0_primary.png"), raw_image("Rings", "The Haily Ring", "2_front.png"), raw_image("Rings", "The Haily Ring", "6_angle.png")], "ref_roles": ["primary", "front", "angle"], "prompt": prompt_flatlay(occasion="Romantic Diwali wishes for lover 2026", setting="marble-vanity", setting_prompt="soft cream marble vanity, small brass diya without markings, rose petals, blank cream love note card, warm lamp reflection, no text", product_name=flatlay["name"], product=flatlay)},
            "lifestyle": {**lifestyle, "alt": "romantic Diwali wishes for lover 2026 lifestyle with The Vicky Hoop Earrings", "caption": "Romantic Diwali wishes 2026 look: The Vicky Hoop Earrings", "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]}, "local_reference_images": [raw_image("Earrings", "The Vicky Hoop Earrings", "1_body_portrait.png"), raw_image("Earrings", "The Vicky Hoop Earrings", "0_primary.png")], "ref_roles": ["body_image", "front_primary"], "prompt": prompt_people(occasion="Romantic Diwali wishes for lover 2026 lifestyle", scene="solo fair-skinned Indian adult woman near a softly lit balcony with blurred Diwali lamps behind her, looking down at a completely blank phone screen with a gentle smile, full head visible and both ears visible, simple ivory festive blouse, no necklace and wrists out of frame", product_name=lifestyle["name"], product=lifestyle, body_part="ear", extra_negatives="necklace, bracelet, ring, watch, readable phone screen")},
        },
    }
    write_json(f"output/{prefix}_sections.json", sections)
    write_json("output/publish_configs/week34_rank7.json", cfg)
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    (ROOT / f"output/{prefix}_Checklist_v2.md").write_text("# Blog SEO + AEO/GEO Checklist v2, Week 3-4 Rank 7\n\nArticle: Romantic Diwali Wishes for Lover 2026\nStatus: Draft assets prepared\n\n- [x] Primary keyword: romantic diwali wishes for lover\n- [x] Optimize treated as New\n- [x] Type 3 hero and lifestyle use body_image plus design refs\n- [x] Product dimension wording uses product dimensions, not face size\n- [ ] WordPress post published\n- [ ] Type 3 images generated and patched\n- [ ] Live URL verified\n", encoding="utf-8")


def build_rank8(product_rows: dict[str, dict[str, str]], detail_rows: dict[str, dict[str, str]]) -> None:
    prefix = "Week34_Rank8_IntFriendshipQuotes"
    sections = {
        "meta": {
            "title": "Happy International Friendship Day Quotes 2026",
            "slug": "happy-international-friendship-day-quotes-2026",
            "meta_desc": "Happy International Friendship Day quotes 2026 with captions, friendship day caption ideas, short wishes, messages, status lines, and warm words for friends.",
            "focus_kw": "friendship day caption",
            "yoast_title": "Happy International Friendship Day Quotes 2026",
        },
        "intro": [
            "A good friendship day caption turns a photo, status, or message into a tiny celebration of the people who stayed. International Friendship Day is observed on July 30, so this 2026 collection gives you quotes, captions, wishes, and messages for best friends, groups, and long distance bonds.",
            "TL;DR: Use a short caption for photos, a heartfelt quote for best friends, a funny line for close groups, and a warmer message when the friendship has carried you through real life.",
        ],
        "sections": [
            {"key": "quotes", "h2": "Happy International Friendship Day Quotes", "lines": [
                "A true friend is a light that stays even when the room gets difficult.",
                "Friendship is the quiet promise that says, you do not have to face this alone.",
                "Some people become friends, and some friends become the safest part of life.",
                "International Friendship Day celebrates the people who turn ordinary days into memories.",
                "A good friend knows your story and still chooses to stand beside you.",
                "Friendship is love with laughter, honesty, patience, and fewer explanations.",
                "The best friendships feel like home, even across cities and years.",
                "A loyal friend is one of lifes most practical miracles.",
                "Friendship is not about constant presence. It is about steady care.",
                "Some bonds are built from small moments that never really leave.",
                "A real friend protects your peace without asking for applause.",
                "Friendship makes life softer, braver, and easier to believe in.",
            ]},
            {"key": "caption", "h2": "Friendship Day Caption", "lines": [
                "Chosen family, forever energy.",
                "Friendship Day with my safest chaos.",
                "Real bond, real laughs, real gratitude.",
                "My people, my peace.",
                "Friends who feel like home.",
                "Built on trust, jokes, and snacks.",
                "Same madness, stronger memories.",
                "International Friendship Day, but make it us.",
                "Good friends, golden memories.",
                "A friendship worth posting.",
                "My favourite kind of family.",
                "This bond needs no filter.",
            ]},
            {"key": "short", "h2": "Short Friendship Day Captions", "lines": [
                "Real ones stay.",
                "Forever my person.",
                "Friendship looks good on us.",
                "Best friend blessing.",
                "My safe place.",
                "Laughter lives here.",
                "Good times, great friends.",
                "Same side always.",
                "Bonded by memories.",
                "Grateful for you.",
            ]},
            {"key": "wishes", "h2": "International Friendship Day Wishes", "lines": [
                "Happy International Friendship Day. May our bond keep growing through every season.",
                "Wishing you a day full of laughter, old memories, and new reasons to smile.",
                "Happy Friendship Day to the person who makes life feel lighter.",
                "May you always be surrounded by loyal friends and peaceful conversations.",
                "Thank you for being a friend who shows up in real ways.",
                "Happy International Friendship Day 2026. You are celebrated more than you know.",
                "May our friendship stay strong through distance, change, and busy days.",
                "Wishing you happiness equal to the comfort your friendship gives me.",
                "Happy Friendship Day to one of the best parts of my life.",
                "May this day remind you how deeply your friendship is valued.",
            ]},
            {"key": "messages", "h2": "Friendship Day Messages", "lines": [
                "You have been there for the easy days and the complicated ones. That is why this Friendship Day feels like a thank you.",
                "Thank you for understanding my silence, laughing at my jokes, and standing by me without making it dramatic.",
                "A friend like you makes ordinary life feel kinder and more possible.",
                "You are the person I can call with news, panic, nonsense, or nothing at all.",
                "Happy Friendship Day. I hope you know how much your loyalty has meant to me.",
                "You have helped me become softer, braver, and more myself.",
                "Some friendships are quiet online but deeply alive in real life.",
                "I do not say it often enough, but I am grateful for you.",
                "Your friendship is one of the reasons my hard days do not win completely.",
                "Thank you for being my reminder that good people still exist.",
            ]},
            {"key": "best_friend", "h2": "Best Friend Quotes", "lines": [
                "A best friend is the person who can turn your worst mood into a survivable story.",
                "You are not just my best friend. You are my comfort person and truth mirror.",
                "Life gave me many people, but peace arrived with you.",
                "Best friends are proof that soulmates can arrive without romance.",
                "A best friend knows when to advise, when to listen, and when to send snacks.",
                "The best part of growing up is knowing some friendships grew with me.",
                "You are my favourite notification and my safest conversation.",
                "Best friends are not perfect people. They are the ones who stay real.",
                "You have seen my messy chapters and still saved me a seat.",
                "A best friend makes even silence feel understood.",
            ]},
            {"key": "funny", "h2": "Funny Friendship Day Captions", "lines": [
                "Friends who screenshot together stay together.",
                "You know too much, so you are family now.",
                "Our friendship is mostly love, snacks, and poor decisions.",
                "Best friend by choice, unpaid therapist by destiny.",
                "We are not dramatic. We are emotionally detailed.",
                "Thank you for tolerating my personality at full volume.",
                "Real friendship is sending the full screenshot without context.",
                "Friendship Day reminder: you are stuck with me.",
                "Good friends give advice. Best friends bring snacks.",
                "Our bond survived bad plans and worse jokes.",
            ]},
            {"key": "emotional", "h2": "Emotional Friendship Quotes", "lines": [
                "Some friends become the proof that life still knows how to be kind.",
                "A real friend does not always fix the pain, but they make it less lonely.",
                "Friendship is the hand you remember when everything else feels uncertain.",
                "The most emotional friendships are made of ordinary moments that stayed.",
                "A friend who understands your silence deserves a permanent place in your prayers.",
                "True friendship is love without performance and support without condition.",
                "Some people enter your life as friends and slowly become courage.",
                "A loyal friend turns survival into something softer.",
                "The heart remembers who stayed when staying was not easy.",
                "A good friend can make your past feel understood and your future feel possible.",
            ]},
            {"key": "status", "h2": "Friendship Day Status", "lines": [
                "Happy International Friendship Day to my favourite humans.",
                "Celebrating the friends who make life feel lighter.",
                "Grateful for real friends and honest laughter.",
                "Friendship Day 2026 with memories that still glow.",
                "To the people who stayed, thank you.",
                "My friends are my soft landing.",
                "Good friends make ordinary days worth saving.",
                "Celebrating loyalty, laughter, and late replies.",
                "For the friends who became family.",
                "International Friendship Day, full heart edition.",
            ]},
        ],
        "faqs": [
            ["What is a good friendship day caption for 2026?", "A good friendship day caption for 2026 is short, warm, and easy to understand with the photo. Try lines about chosen family, real bonds, laughter, loyalty, or memories, then tag the friend who makes it personal."],
            ["What are Happy International Friendship Day quotes?", "Happy International Friendship Day quotes are lines that celebrate friendship across distance, time, and everyday life. They usually focus on loyalty, comfort, memories, support, and the people who make ordinary days feel brighter."],
            ["When is International Friendship Day 2026?", "International Friendship Day is observed on July 30. In 2026, it falls on Thursday, July 30. You can post a caption, send a message, or share a short quote anytime during the day."],
            ["What should I write for my best friend on Friendship Day?", "For your best friend, write one honest thank you and one memory or quality you value. Keep it specific, such as thanking them for loyalty, laughter, advice, patience, or the way they make hard days feel easier."],
            ["Can I use funny Friendship Day captions for Instagram?", "Yes, funny Friendship Day captions work well on Instagram when the bond is playful. Keep the joke kind, avoid embarrassing private details, and use a line that matches the photo, group chat energy, or shared memory."],
        ],
    }
    carousel_names = ["The Thaloria Pendant", "The Shining Star Bracelet", "The Estrella Oval Bangle", "The Malocchio Charm Holder Bracelet", "The Teshvarya Pendant", "The Aleena Huggie Earrings"]
    hero = consolidated(detail_rows, "The Elize Evil Eye Bracelet")
    flatlay = consolidated(detail_rows, "The Lumeelle Cluster Pendant")
    lifestyle = consolidated(detail_rows, "The Rohal Huggie Earrings")
    cfg = {
        "rank": "Week3-4 Rank 8",
        "sections_json": f"output/{prefix}_sections.json",
        "output_prefix": prefix,
        "carousel_id": "bs-cf-intfriendshipquotes",
        "occasion_year": "International Friendship Day 2026",
        "carousel_alt_prefix": "friendship day caption 2026 gift idea",
        "gift_h2": "Friendship Day Gift Ideas",
        "gift_blurb": "If your caption is going with a small gift, choose something wearable and easy to remember after the post disappears. These BlueStone pieces keep the gesture thoughtful without making the article a product catalogue.",
        "conclusion_html": "A friendship day caption works best when it sounds like your real bond. Choose a line, add a name or memory, and let the friend know exactly why they matter.",
        "schema_keywords": ["friendship day caption", "happy international friendship day quotes", "international friendship day wishes", "friendship day messages", "best friend quotes", "funny friendship day captions"],
        "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
        "products": [product(product_rows, name) for name in carousel_names],
        "flatlay_insert_h2": "Friendship Day Caption",
        "lifestyle_insert_h2": "International Friendship Day Wishes",
        "more_reads_html": 'Read more friendship and celebration ideas in <a href="https://blog.bluestone.com/emotional-friendship-day-quotes-2026/">emotional Friendship Day quotes</a>, <a href="https://blog.bluestone.com/friendship-day-photos-2026/">friendship messages</a>, <a href="https://blog.bluestone.com/mother-daughter-quotes-2026/">mother daughter quotes</a>, and <a href="https://blog.bluestone.com/happy-rakhi-wishes-to-brother-2026/">Rakhi wishes to brother</a>.',
        "how_to_html": "Pick a caption that matches the photo first. Use short lines for selfies, emotional quotes for old memories, funny captions for group photos, and a longer message when the friend deserves more than one line.",
        "faq_h2": "Frequently Asked Questions about Friendship Day Captions",
        "min_lines": 80,
    }
    prompts = {
        "rank": "Week3-4 Rank 8",
        "slug": sections["meta"]["slug"],
        "primary_kw": sections["meta"]["focus_kw"],
        "output_prefix": prefix,
        "caption_occasion": "Friendship Day caption",
        "caption_year": "2026",
        "flatlay_setting": "cafe-tray",
        "workflow": "Higgsfield MCP nano_banana_pro. Do not generate until balance succeeds. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/happy-international-friendship-day-quotes-hero-2026.webp",
            "flatlay": "output/magnific_generated/happy-international-friendship-day-quotes-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/happy-international-friendship-day-quotes-lifestyle-2026.webp",
        },
        "media_titles": {"hero": "friendship day caption 2026 Hero", "flatlay": "friendship day caption 2026 Flatlay", "lifestyle": "friendship day caption 2026 Lifestyle"},
        "schema_keywords": cfg["schema_keywords"],
        "slots": {
            "hero": {**hero, "alt": "friendship day caption 2026 hero with The Elize Evil Eye Bracelet", "caption": "Friendship Day caption 2026 mood: The Elize Evil Eye Bracelet", "product": {"code": hero["code"], "name": hero["name"], "pdp": hero["pdp"]}, "local_reference_images": [raw_image("Bracelets", "The Elize Evil Eye Bracelet", "1_body_portrait.png"), raw_image("Bracelets", "The Elize Evil Eye Bracelet", "0_primary.png")], "ref_roles": ["body_image", "front_primary"], "prompt": prompt_people(occasion="Happy International Friendship Day quotes 2026 hero", scene="solo fair-skinned Indian adult woman in a bright cafe corner smiling while tying a simple blank friendship band onto a gift box, full face visible, wrist and bracelet clearly visible, warm candid friendship mood", product_name=hero["name"], product=hero, body_part="wrist", extra_negatives="other friendship bands on wrist, bracelet stack")},
            "flatlay": {**flatlay, "alt": "friendship day caption 2026 flatlay with The Lumeelle Cluster Pendant", "caption": "Friendship Day caption 2026 vibe: The Lumeelle Cluster Pendant", "product": {"code": flatlay["code"], "name": flatlay["name"], "pdp": flatlay["pdp"]}, "local_reference_images": [raw_image("Pendants", "The Lumeelle Cluster Pendant", "0_primary.png"), raw_image("Pendants", "The Lumeelle Cluster Pendant", "2_front.png"), raw_image("Pendants", "The Lumeelle Cluster Pendant", "5_close_up.png")], "ref_roles": ["primary", "front", "close_up"], "prompt": prompt_flatlay(occasion="Happy International Friendship Day quotes 2026", setting="cafe-tray", setting_prompt="a ceramic cafe tray on soft stoneware, plain coffee cup, folded linen napkin, blank cream friendship card, tiny unbranded gift box, no text", product_name=flatlay["name"], product=flatlay)},
            "lifestyle": {**lifestyle, "alt": "friendship day caption 2026 lifestyle with The Rohal Huggie Earrings", "caption": "Friendship Day caption 2026 look: The Rohal Huggie Earrings", "product": {"code": lifestyle["code"], "name": lifestyle["name"], "pdp": lifestyle["pdp"]}, "local_reference_images": [raw_image("Earrings", "The Rohal Huggie Earrings", "1_body_portrait.png"), raw_image("Earrings", "The Rohal Huggie Earrings", "0_primary.png")], "ref_roles": ["body_image", "front_primary"], "prompt": prompt_people(occasion="Happy International Friendship Day quotes 2026 lifestyle", scene="solo fair-skinned Indian adult woman in a cozy cafe looking at a completely blank phone screen and smiling at a friendship message, full head visible and both ears visible, soft ivory top, no necklace and wrists out of frame", product_name=lifestyle["name"], product=lifestyle, body_part="ear", extra_negatives="necklace, bracelet, ring, watch, readable phone screen")},
        },
    }
    write_json(f"output/{prefix}_sections.json", sections)
    write_json("output/publish_configs/week34_rank8.json", cfg)
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    (ROOT / f"output/{prefix}_Checklist_v2.md").write_text("# Blog SEO + AEO/GEO Checklist v2, Week 3-4 Rank 8\n\nArticle: Happy International Friendship Day Quotes 2026\nStatus: Draft assets prepared\n\n- [x] Primary keyword: friendship day caption\n- [x] New row published as New\n- [x] Type 3 hero and lifestyle use body_image plus design refs\n- [x] Product dimension wording uses product dimensions, not face size\n- [ ] WordPress post published\n- [ ] Type 3 images generated and patched\n- [ ] Live URL verified\n", encoding="utf-8")


def main() -> None:
    product_rows = load_csv("Seo Products - final products (1).csv")
    detail_rows = load_csv("Seo Products - consolidated.csv")
    build_rank7(product_rows, detail_rows)
    build_rank8(product_rows, detail_rows)


if __name__ == "__main__":
    main()
