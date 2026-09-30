#!/usr/bin/env python3
"""Build Rank 95 new year wishes for love assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank95_NewYearLove"
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
            "title": "New Year Wishes for Love 2026: Romantic Messages",
            "slug": "new-year-wishes-for-love-2026",
            "meta_desc": "New Year wishes for love 2026 with romantic messages for husband, boyfriend, girlfriend, my love, quotes, captions, and heartfelt greetings for midnight.",
            "focus_kw": "new year wishes for love",
            "yoast_title": "New Year Wishes for Love 2026 | Romantic Messages",
        },
        "intro": [
            "New year wishes for love should feel personal, hopeful, and warm without sounding copied. The best line sounds like it belongs only to the two of you.",
            "TL;DR: Use a short romantic wish for chat, a deeper note for your husband, boyfriend, girlfriend, or my love, and a sweet caption when you are posting a New Year photo together.",
        ],
        "sections": [
            {"key": "romantic", "h2": "New Year Wishes for Love", "lines": [
                "Happy New Year, my love. May 2026 bring us more laughter, deeper trust, and quiet moments that feel like home.",
                "This new year, I do not need a perfect plan. I only need your hand in mine and a heart brave enough to keep choosing us.",
                "Happy New Year to the one who makes ordinary days feel softer, brighter, and worth remembering.",
                "May 2026 bring us patience during hard days, sweetness during busy days, and love that keeps growing in simple ways.",
                "My favorite countdown is the one that ends with you beside me.",
                "Happy New Year, love. I hope this year gives us reasons to smile that we cannot even imagine yet.",
                "A new year feels beautiful because I get to enter it loving you.",
                "May our 2026 be full of honest talks, warm hugs, shared dreams, and tiny wins that become big memories.",
                "Happy New Year to my safest place and my favorite adventure.",
                "No matter where the year takes us, I want my heart to keep finding its way back to you.",
            ]},
            {"key": "husband", "h2": "New Year Greetings for Husband", "lines": [
                "Happy New Year, husband. Thank you for being my partner in plans, problems, laughter, and late-night dreams.",
                "May 2026 bring you success, peace, health, and the kind of happiness you quietly give everyone else.",
                "I am grateful for your love, your patience, and the way you make our home feel steady.",
                "Happy New Year to the man who turns responsibility into care and everyday life into companionship.",
                "This year, I hope you feel supported in every dream you have been carrying silently.",
                "May our marriage keep growing in friendship, respect, romance, and small acts of kindness.",
                "Happy New Year, my love. I choose you again, in the morning rush and in the quiet night.",
                "Thank you for being my teammate when life is messy and my joy when life is sweet.",
                "I hope 2026 gives you the confidence to chase what matters and the comfort of knowing I am with you.",
                "Happy New Year to my husband, my best friend, and the calm center of my world.",
            ]},
            {"key": "boyfriend", "h2": "New Year Wishes for Boyfriend", "lines": [
                "Happy New Year, boyfriend. I hope 2026 gives us more dates, more inside jokes, and more reasons to believe in us.",
                "You make my year better just by being in it.",
                "May this new year bring you every goal you are working for and every smile you deserve.",
                "Happy New Year to the person who makes my phone light up and my heart feel lighter.",
                "I hope 2026 lets us grow closer without losing the fun that made us begin.",
                "You are my favorite plan for this year and every year after.",
                "Happy New Year, love. I am excited for every small memory we have not made yet.",
                "May your dreams feel possible and may my love make the journey softer.",
                "I do not know everything 2026 will bring, but I know I want to share it with you.",
                "Happy New Year to my favorite person to miss, message, and meet.",
            ]},
            {"key": "girlfriend", "h2": "Happy New Year Wishes for Girlfriend", "lines": [
                "Happy New Year, beautiful. May 2026 treat you with the gentleness, respect, and joy you deserve.",
                "You are the sweetest part of my year and the person I want beside me for the next one.",
                "I hope this new year brings your dreams closer and your worries further away.",
                "Happy New Year to the girl who makes love feel easy and life feel bright.",
                "May your smile stay fearless, your heart stay hopeful, and your days stay full of good news.",
                "Loving you is my favorite habit, and I want to carry it into 2026.",
                "Happy New Year, my love. I hope I can make you feel as cherished as you make me feel lucky.",
                "This year, I want to celebrate your wins, hold you through hard days, and love you better.",
                "May 2026 be kind to your heart and generous to your dreams.",
                "Happy New Year to my girlfriend, my favorite hello, and my hardest goodbye.",
            ]},
            {"key": "my_love", "h2": "Happy New Year My Love Messages", "lines": [
                "Happy New Year, my love. You are the wish I want to keep repeating.",
                "If 2026 gives me your laughter, your hand, and your trust, it will already be a blessed year.",
                "My love, may this year bring us closer to the life we keep talking about.",
                "Happy New Year. I want our love to feel peaceful, playful, and honest in every season.",
                "The world celebrates midnight once, but my heart celebrates you every day.",
                "My love, thank you for making hope feel practical and romance feel real.",
                "May 2026 hold more hugs after hard days and more smiles for no reason.",
                "Happy New Year to the person who feels like both home and a new beginning.",
                "I love you today, I will love you tomorrow, and I hope this year gives me more ways to show it.",
                "My favorite resolution is to love you with more patience, presence, and joy.",
            ]},
            {"key": "quotes", "h2": "Happy New Year Love Quotes", "lines": [
                "A new year is sweeter when the heart knows where it belongs.",
                "Love turns a calendar change into a promise of togetherness.",
                "The best beginning is not midnight. It is the moment two people choose each other again.",
                "In every year, the most precious memory is the one made with love.",
                "A shared dream can make even an ordinary January feel magical.",
                "New Year love is not about grand words. It is about steady presence.",
                "The future feels less unknown when your favorite person walks beside you.",
                "Real romance is entering a new year with gratitude and gentleness.",
                "Some fireworks fade quickly, but a loyal heart keeps glowing.",
                "The most romantic resolution is to keep showing up.",
            ]},
            {"key": "short", "h2": "Short New Year Wishes for Love", "lines": [
                "Happy New Year, my forever favorite.",
                "New year, same heart, deeper love.",
                "Here is to us in 2026.",
                "You are my happiest beginning.",
                "My love, my year, my joy.",
                "Cheers to another year of us.",
                "You make the future feel kind.",
                "Happy New Year, sweetheart.",
                "More love, more laughter, more us.",
                "Midnight is better with you.",
            ]},
            {"key": "long", "h2": "Long New Year Wishes for Love", "lines": [
                "Happy New Year, my love. As 2026 begins, I want you to know that loving you has made my life warmer, steadier, and more meaningful.",
                "I hope this year gives us the courage to grow, the patience to understand each other, and the joy to celebrate even small moments.",
                "You are not just part of my year. You are part of the future I quietly imagine when everything is calm.",
                "May we forgive quickly, listen better, laugh louder, and protect the love we have built together.",
                "Happy New Year to the person who has seen my messy days and still chosen to stay close.",
                "This year, I do not promise perfection, but I promise effort, honesty, and a heart that keeps returning to you.",
                "May 2026 bring us more peace than pressure and more togetherness than distance.",
                "I hope every month gives us one memory we will smile about later.",
                "Thank you for making love feel less like a fantasy and more like a daily blessing.",
                "Happy New Year, my love. I am grateful for the past, hopeful for the future, and happy that both include you.",
            ]},
            {"key": "captions", "h2": "New Year Love Captions for Instagram", "lines": [
                "Entering 2026 with my favorite person.",
                "New year, old love, fresh memories.",
                "My midnight smile has a name.",
                "Cheers to the love that made this year brighter.",
                "Together is my favorite New Year plan.",
                "One more year of laughing at our own jokes.",
                "Love looks good on 2026.",
                "Soft launch? No, full New Year sparkle.",
                "My favorite resolution is us.",
                "New Year glow, same heart.",
            ]},
            {"key": "distance", "h2": "New Year Wishes for Long Distance Love", "lines": [
                "Happy New Year, my love. Distance may keep us apart tonight, but it cannot make you feel far from my heart.",
                "I wish I could hold your hand at midnight, but I am sending all my love across the miles.",
                "May 2026 bring us closer to the day when goodbyes become shorter and hugs become longer.",
                "No distance can change how deeply I am rooting for you this year.",
                "Happy New Year. I miss you, love you, and believe in the future we are building.",
                "Tonight I am counting memories instead of miles.",
                "May this year give us more visits, more calls, and more reasons to keep trusting the wait.",
                "You are far in location, not in importance.",
                "Happy New Year to the person I want beside me in every countdown.",
                "Our love is proof that closeness is not only measured in distance.",
            ]},
            {"key": "card", "h2": "What to Write in a New Year Card for Love", "lines": [
                "Start with their name or your private nickname to make the card feel personal.",
                "Mention one memory from the past year instead of writing only general romance.",
                "Add one hope for 2026 that includes both of you.",
                "Keep the tone natural if your relationship is playful.",
                "Choose a deeper message if the card is for a husband, wife, or long-term partner.",
                "Avoid copying a line that sounds too formal for your actual bond.",
                "Use simple words like thank you, I love you, and I am proud of us.",
                "If you are giving a gift, let the card explain the emotion rather than the price.",
                "End with a promise you can actually keep.",
                "A sincere card is better than a perfect quote.",
            ]},
            {"key": "gift", "h2": "New Year Gift Ideas for Someone You Love", "lines": [
                "A thoughtful New Year gift should feel like a blessing for the year ahead.",
                "A pendant can carry a romantic wish without feeling too loud.",
                "A bangle can feel graceful for someone who likes festive dressing.",
                "Hoop earrings work well for daily wear and New Year photos.",
                "A ring can mark commitment when the relationship tone is clear.",
                "Choose a design that fits their everyday style, not only your idea of romance.",
                "Pair the gift with a short handwritten note.",
                "Avoid making the message about cost or size.",
                "The best gift supports the wish you are sending.",
                "Let the keepsake say: I want your year to feel loved.",
            ]},
        ],
        "section_leads": {},
        "faqs": [
            ["What are the best New Year wishes for love?", "The best New Year wishes for love are personal, warm, and future-facing. Mention your bond, add one hope for 2026, and keep the line natural enough to sound like you."],
            ["How do I wish Happy New Year to my love?", "Say Happy New Year, my love, then add a specific feeling such as gratitude, hope, trust, or excitement for the year ahead. A simple personal line often works better than a long formal quote."],
            ["What should I write to my husband for New Year?", "Write a message that thanks him for partnership, wishes him peace and success, and says you are excited to keep building your life together in 2026."],
            ["What is a romantic New Year wish for boyfriend?", "Try: Happy New Year, love. I hope 2026 gives us more laughter, stronger trust, and many small memories that make us believe in us even more."],
            ["What is a sweet New Year wish for girlfriend?", "Try: Happy New Year, beautiful. May 2026 treat you with the kindness, joy, and success you deserve, and may I keep making you feel loved."],
            ["Can I use these New Year love wishes as captions?", "Yes. Short wishes work best as captions, while longer messages suit cards, private chats, and midnight notes. Add a photo-specific detail if you are posting on Instagram."],
        ],
    }

    config = {
        "rank": 95,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-nylove",
        "occasion_year": "New Year Wishes for Love 2026",
        "carousel_alt_prefix": "new year wishes for love 2026 gift idea",
        "gift_h2": "Romantic New Year Jewellery Gift Ideas",
        "gift_blurb": "If your New Year wish is about love, commitment, and a fresh beginning, a thoughtful keepsake can make the message linger after midnight. These approved BlueStone designs suit romantic gifting without mentioning prices.",
        "conclusion_html": "New Year wishes for love work best when they feel true to your relationship. Choose the line that sounds like you, add one personal detail, and send it with warmth before the midnight rush.",
        "schema_keywords": ["new year wishes for love", "new year greetings for husband", "new year wishes for boyfriend", "happy new year wishes for girlfriend", "happy new year love quotes", "happy new year wishes for boyfriend"],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(rows, "The Thyvarne Pendant", "Pendants"),
            product(rows, "The Estrella Oval Bangle", "Bangles"),
            product(rows, "The Vicky Hoop Earrings", "Earrings"),
            product(rows, "The Quinn Ring", "Rings"),
            product(rows, "The Aagarna Pendant", "Pendants"),
            product(rows, "The Gigi Ring", "Rings"),
        ],
        "flatlay_insert_h2": "Happy New Year My Love Messages",
        "lifestyle_insert_h2": "New Year Gift Ideas for Someone You Love",
        "more_reads_html": "Read more New Year inspiration in <a href=\"https://blog.bluestone.com/new-year-wishes-for-friends-2026/\">New Year wishes for friends 2026</a>, <a href=\"https://blog.bluestone.com/husband-birthday-wishes-2026/\">husband birthday wishes 2026</a>, <a href=\"https://blog.bluestone.com/mother-daughter-quotes-2026/\">mother daughter quotes 2026</a>, and <a href=\"https://blog.bluestone.com/thank-you-note-to-teacher-2026/\">thank you note to teacher 2026</a>.",
        "how_to_html": "Pick the line that matches your relationship stage. Use a soft wish for a new relationship, a grateful note for a husband or long-term partner, and a short caption for social posts.",
        "faq_h2": "Frequently Asked Questions about New Year Wishes for Love",
        "min_lines": 100,
        "section_leads": {},
    }

    prompts = {
        "rank": 95,
        "slug": "new-year-wishes-for-love-2026",
        "output_prefix": PREFIX,
        "occasion": "New Year Wishes for Love 2026",
        "primary_kw": "new year wishes for love",
        "caption_occasion": "New Year wishes for love",
        "caption_year": "2026",
        "flatlay_setting": "cafe-tray",
        "workflow": "Higgsfield MCP nano_banana_pro. Campaign hybrid with mandatory body_image scale line for people shots. Do not generate until balance succeeds. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/new-year-wishes-for-love-hero-2026.webp",
            "flatlay": "output/magnific_generated/new-year-wishes-for-love-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/new-year-wishes-for-love-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "new year wishes for love 2026 hero The Thyvarne Pendant",
            "flatlay": "new year wishes for love 2026 flatlay The Estrella Oval Bangle",
            "lifestyle": "new year wishes for love 2026 lifestyle The Vicky Hoop Earrings",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                "code": "BISW1080P28", "name": "The Thyvarne Pendant", "gender": "Female", "height_mm": 17.5, "width_mm": 17.5,
                "size_prompt_note": "pendant product height 17.5 mm and width 17.5 mm; product dimensions, not face size; copy worn neck scale from body_image",
                "alt": "new year wishes for love 2026 hero with The Thyvarne Pendant", "caption": "New Year wishes for love 2026 vibe: The Thyvarne Pendant",
                "product": {"code": "BISW1080P28", "name": "The Thyvarne Pendant", "pdp": "https://www.bluestone.com/pendants/the-thyvarne-pendant~173761.html"},
                "cdn": ["https://kinclimg8.bluestone.com/giproduct/BISW1080P28_RAA18DIG6MALAXXXX_ABCD00-BP-PICS-00000-1024-114065.png", "https://kinclimg3.bluestone.com/giproduct/BISW1080P28_RAA18DIG6MALAXXXX_ABCD00-PICS-00004-1024-114065.png"],
                "local_reference_images": ["ProductImages/raw/Pendants/The Thyvarne Pendant/1_body_portrait.png", "ProductImages/raw/Pendants/The Thyvarne Pendant/0_primary.png"],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} New Year wishes for love 2026 hero, solo fair-skinned Indian adult woman in a warm modern Indian apartment near a softly lit window, midnight celebration mood with a blank cream greeting card and a small wrapped gift on a table in the background. Full head, full face, both eyes, complete smile, neck, pendant, and upper body visible with safe margins. Hands and wrists hidden below frame to prevent extra jewellery. Exactly one person in the entire image. Camera pulled back medium chest-up shot, 85mm DSLR look, natural skin texture, warm lamp light, realistic shadows, 16:9.\n\nThe woman physically wears The Thyvarne Pendant from @img1 body_image and @img2 design on a fine chain at upper chest. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: pendant product height_mm=17.5 and width_mm=17.5. These are real product dimensions, NOT face-size instructions. Keep pendant size on the neck like @img1 body_image worn neck scale: subtle pendant size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the rose gold pendant exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery in the image. Bare ears, bare wrists, bare fingers, no watch, no bracelet, no rings, no earrings, no extra necklaces. No readable text anywhere.\n\nAvoid: cropped face, cropped head, readable text, man wearer, child, second person, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow.",
            },
            "flatlay": {
                "code": "BIDG0393O37", "name": "The Estrella Oval Bangle", "gender": "Female", "height_mm": 50.19, "width_mm": 7.1,
                "size_prompt_note": "bangle product height 50.19 mm and width 7.1 mm; product dimensions, not face size",
                "alt": "new year wishes for love 2026 flatlay with The Estrella Oval Bangle", "caption": "New Year wishes for love 2026 keepsake: The Estrella Oval Bangle",
                "product": {"code": "BIDG0393O37", "name": "The Estrella Oval Bangle", "pdp": "https://www.bluestone.com/bangles/the-estrella-oval-bangle~34771.html"},
                "cdn": ["https://kinclimg1.bluestone.com/giproduct/BIDG0393O37_YAA18DIG6XXXXXXXX_ABCD00-PICS-00001-1024-28014.png", "https://kinclimg1.bluestone.com/giproduct/BIDG0393O37_YAA18DIG6XXXXXXXX_ABCD00-PICS-00002-1024-28014.png", "https://kinclimg1.bluestone.com/giproduct/BIDG0393O37_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-28014.png"],
                "local_reference_images": ["ProductImages/raw/Bangles/The Estrella Oval Bangle/0_primary.png", "ProductImages/raw/Bangles/The Estrella Oval Bangle/2_front.png", "ProductImages/raw/Bangles/The Estrella Oval Bangle/3_side_1.png"],
                "ref_roles": ["primary", "front", "side"],
                "prompt": f"Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\nNew Year wishes for love 2026 top-down flatlay. Flatlay setting ID: cafe-tray. Surface and props: warm cafe tray on ivory linen, blank cream greeting card, two empty champagne-style flutes with no labels, soft fairy lights blurred at edge, one small wrapped gift, no readable text. The identical Estrella Oval Bangle from @img1, @img2 and @img3 rests naturally on the surface at true PDP scale. Product dimensions from PDP: bangle product height_mm=50.19 and width_mm=7.1. These are product dimensions, NOT face-size instructions. Do not enlarge for visibility. Full bangle visible, yellow gold oval bangle with diamond detail, 100 percent identical design, zero distortion, HD metal and stone detail.\n\nProps stay secondary. No people, no hands, no logos, no readable text.\n\nAvoid: hands, people, floating overlays, cutouts, incorrect bangle design, readable text, logos, price tags, blown whites, HDR glow, illustration, CGI.",
            },
            "lifestyle": {
                "code": "BIIP0427H16", "name": "The Vicky Hoop Earrings", "gender": "Female", "height_mm": 14.75, "width_mm": 6.04,
                "size_prompt_note": "earring product height 14.75 mm and width 6.04 mm; product dimensions, not face size; copy worn ear scale from body_image",
                "alt": "new year wishes for love 2026 lifestyle with The Vicky Hoop Earrings", "caption": "New Year wishes for love 2026 vibe: The Vicky Hoop Earrings",
                "product": {"code": "BIIP0427H16", "name": "The Vicky Hoop Earrings", "pdp": "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html"},
                "cdn": ["https://kinclimg5.bluestone.com/giproduct/BIIP0427H16_YAA18DIG6XXXXXXXX_ABCD00-BP-PICS-00000-1024-76610.png", "https://kinclimg2.bluestone.com/giproduct/BIIP0427H16_YAA18DIG6XXXXXXXX_ABCD00-PICS-00004-1024-76610.png"],
                "local_reference_images": ["ProductImages/raw/Earrings/The Vicky Hoop Earrings/1_body_portrait.png", "ProductImages/raw/Earrings/The Vicky Hoop Earrings/0_primary.png"],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} New Year wishes for love 2026 lifestyle, solo fair-skinned Indian adult woman smiling near a decorated home table with a blank New Year card, soft fairy lights, and a wrapped gift in the background. Full head, full face, both ears, both eyes, complete smile, neck, earrings, and upper body visible with safe margins. Hands and wrists hidden below frame to prevent extra jewellery. Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, warm indoor light, realistic shadows, 16:9.\n\nThe woman physically wears The Vicky Hoop Earrings from @img1 body_image and @img2 design on her ears. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: earring product height_mm=14.75 and width_mm=6.04. These are real product dimensions, NOT face-size instructions. Keep earrings size on the ears like @img1 body_image worn ear scale: subtle earring size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the yellow gold hoop earrings exactly, 100 percent identical to refs, zero distortion, HD metal detail. These earrings are the single and only jewellery in the image. Bare neck, bare wrists, bare fingers, no watch, no bracelet, no rings, no necklace, no other earrings. No readable text anywhere.\n\nAvoid: cropped face, cropped head, man wearer, child, second person, extra jewellery, floating jewellery overlay, oversized jewellery, packshot collage, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow.",
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 95

Article: New Year Wishes for Love 2026
Status: Draft assets prepared
Date: 2026-07-24

## A. Intent and Brief
- [x] Primary keyword: new year wishes for love
- [x] Sheet Optimize treated as New
- [x] Old cluster URL untouched
- [x] Fresh slug: new-year-wishes-for-love-2026
- [x] 2026 year lock used
- [x] Supporting keywords mapped to H2/FAQ

## B. SEO Structure
- [x] Title/H1 intent prepared
- [x] Yoast title <= 60 chars
- [x] Meta description 150-160 chars
- [x] Primary keyword in intro and hero alt

## C. Content and Readability
- [x] Direct answer + TL;DR
- [x] 100+ message lines
- [x] No prices
- [x] No old year wish lines in body

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [x] Type 3 prompts prepared with body_image + design refs for hero and lifestyle
- [x] Fair-skinned Indian casting included for people shots
- [x] Product dimension wording uses product/category dimensions, not face size
- [x] Filmic style language included
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""
    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json("output/publish_configs/rank95.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
