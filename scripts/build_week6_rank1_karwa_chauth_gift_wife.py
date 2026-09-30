#!/usr/bin/env python3
"""Build Week 6 Rank 1 Karwa Chauth gift for wife article assets."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from build_week34_rank9_10_batch import (  # noqa: E402
    checklist,
    consolidated,
    load_csv,
    product,
    prompt_flatlay,
    prompt_people,
    raw_image,
    write_json,
)


def sec(key: str, h2: str, lines: list[str]) -> dict[str, object]:
    return {"key": key, "h2": h2, "lines": lines}


def slot(item: dict[str, object], alt: str, caption: str, refs: list[str], roles: list[str], prompt: str) -> dict[str, object]:
    return {
        **item,
        "alt": alt,
        "caption": caption,
        "product": {"code": item["code"], "name": item["name"], "pdp": item["pdp"]},
        "local_reference_images": refs,
        "ref_roles": roles,
        "prompt": prompt,
    }


def main() -> None:
    rows = load_csv("docs/product/Seo Products - consolidated.csv")
    prefix = "Week6_Rank1_KarwaChauthGiftWife"
    rank = 1
    slug = "karwa-chauth-gift-for-wife-2026"
    focus_kw = "karwa chauth gift for wife"
    title = "Karwa Chauth Gift for Wife 2026: Thoughtful Ideas"
    meta_desc = "Karwa Chauth gift for wife 2026 with jewellery ideas, romantic gifts, first Karwa Chauth picks, luxury keepsakes, budget tips, and thoughtful notes now."
    keywords = [
        "karwa chauth gift for wife",
        "karwa chauth jewellery gift for wife",
        "first karwa chauth gift for wife",
        "romantic karwa chauth gift",
    ]

    hero = consolidated(rows, "The Teshvarya Pendant")
    flat = consolidated(rows, "The Ebony Ring")
    life = consolidated(rows, "The Faliha Purse Hoop Earrings")

    sections = [
        sec("main", "Karwa Chauth Gift for Wife", [
            "A delicate pendant that she can wear long after the festival evening.",
            "A pair of diamond earrings for a look that feels festive but wearable.",
            "A gold ring that marks the day without feeling too formal.",
            "A bracelet chosen in her everyday style, not only for the occasion.",
            "A jewellery piece paired with a short handwritten promise.",
            "A keepsake she can wear for Karwa Chauth dinner and future celebrations.",
            "A minimal necklace if she prefers quiet elegance over heavy styling.",
            "A gemstone accent if she enjoys colour in her festive wardrobe.",
            "A charm bracelet that can grow with memories over time.",
            "A classic ring for the wife who likes timeless gifts.",
            "A pair of huggie earrings for comfortable all-day festive wear.",
            "A pendant with a soft romantic note tucked inside the gift box.",
        ]),
        sec("jewellery", "Karwa Chauth Jewellery Gift for Wife", [
            "Choose a pendant when you want the gift to sit close to the heart.",
            "Choose earrings when she loves styling her festive outfits around her face.",
            "Choose a ring when the gift should feel personal and symbolic.",
            "Choose a bracelet when she likes everyday jewellery with a little movement.",
            "Choose a bangle if her festive style leans traditional and graceful.",
            "Choose a charm piece when you want the gift to carry a story.",
            "Choose diamond details when she enjoys subtle sparkle.",
            "Choose gemstone details when her wardrobe has rich festive colours.",
            "Choose yellow gold when she loves classic Indian occasion styling.",
            "Choose rose gold if her style is soft, modern, and romantic.",
            "Choose a lightweight design if she prefers comfort through long celebrations.",
            "Choose one strong piece instead of several pieces she may not wear often.",
        ]),
        sec("first", "First Karwa Chauth Gift for Wife", [
            "For her first Karwa Chauth, pick a gift that feels emotional, not excessive.",
            "A pendant works beautifully because it can become a memory she wears often.",
            "A ring can mark the first festival as a quiet promise.",
            "A simple bracelet pairs well with a note about your first celebration together.",
            "Earrings are a safe choice if you know her preferred metal tone.",
            "A jewellery gift with a personal message feels better than a rushed surprise.",
            "If she is new to the ritual, choose comfort and warmth over drama.",
            "Plan the gift around her taste, not only around festive tradition.",
            "Add a small note about what you admire in her patience and love.",
            "Pick a design she can wear to work, dinner, or family functions later.",
            "Make the unboxing calm, thoughtful, and private if she values quiet moments.",
            "Let the gift say that the first festival is only the beginning.",
        ]),
        sec("romantic", "Romantic Karwa Chauth Gift Ideas", [
            "A pendant with a note that says she is your favourite blessing.",
            "A ring paired with one memory from your first year together.",
            "A bracelet that reminds her of all the small ways she cares.",
            "Earrings gifted before dinner so she can wear them that evening.",
            "A jewellery box placed beside flowers and a ceramic cup of tea.",
            "A keepsake chosen because it matches the colour she wears most often.",
            "A surprise that includes a simple promise for the coming year.",
            "A gift note that thanks her for love, patience, and partnership.",
            "A piece selected from something she once admired casually.",
            "A quiet celebration at home with one meaningful jewellery gift.",
            "A romantic note that avoids clichés and sounds like your real voice.",
            "A small sparkle that turns the evening into a memory.",
        ]),
        sec("luxury", "Luxury Karwa Chauth Gift for Wife", [
            "A statement pendant if she enjoys dressing up for festive dinners.",
            "Diamond earrings that can move from festival outfits to formal occasions.",
            "A refined ring with a design that feels distinctive but not loud.",
            "A bracelet with polished detailing for a premium everyday feel.",
            "A jewellery gift chosen for craftsmanship instead of only size.",
            "A design that feels special but still fits her personal wardrobe.",
            "A piece she can style with silk, chiffon, or a modern kurta set.",
            "A luxury gift packed with a sincere note instead of a long speech.",
            "A timeless design if you want the gift to feel valuable for years.",
            "A gemstone piece if she likes colour and festive richness.",
            "A diamond accent if she prefers quiet sophistication.",
            "A premium keepsake for the wife who values detail and finish.",
        ]),
        sec("budget", "Budget-Friendly Karwa Chauth Gifts for Wife", [
            "A lightweight pendant that feels thoughtful without feeling heavy.",
            "Small earrings she can wear regularly after the festival.",
            "A minimal ring with clean lines and everyday comfort.",
            "A charm-style piece that gives the gift a personal angle.",
            "A simple bracelet paired with a heartfelt handwritten note.",
            "A jewellery gift chosen early so you are not forced into last-minute buying.",
            "A design in her usual style so it gets worn often.",
            "A piece that matches an outfit she already owns.",
            "A small keepsake with strong emotional meaning.",
            "A gift box styled with flowers, ribbon, and a warm note.",
            "A practical jewellery piece that still feels festive.",
            "A budget-conscious gift that feels personal because you noticed her taste.",
        ]),
        sec("traditional", "Traditional Karwa Chauth Gift Ideas", [
            "A gold pendant that pairs well with red, maroon, or cream festive outfits.",
            "A bangle-style piece for a wife who loves classic occasion dressing.",
            "A pair of earrings that works with sarees, suits, and lehengas.",
            "A jewellery gift placed with flowers and festive fabric.",
            "A design that respects tradition but feels comfortable to wear.",
            "A keepsake she can wear during puja and family dinner.",
            "A ring chosen for symbolism and daily wear.",
            "A bracelet that complements her existing bangles without crowding them.",
            "A pendant that adds sparkle without overpowering her look.",
            "A subtle diamond piece for a graceful festive finish.",
            "A gemstone accent if her festive wardrobe includes deep colours.",
            "A traditional gift note that thanks her for love and togetherness.",
        ]),
        sec("personalised", "Personalised Karwa Chauth Gift Ideas", [
            "Pick jewellery based on the metal colour she already wears most.",
            "Choose a design that matches her daily routine and comfort level.",
            "Add a note about one habit of hers that you genuinely love.",
            "Gift the piece in a setting that feels private and unrushed.",
            "Pair the jewellery with flowers she actually likes.",
            "Choose a piece connected to a shared memory from the year.",
            "Add a short promise instead of a generic greeting.",
            "Select a design that suits her neckline, hairstyle, or usual outfits.",
            "Make the gift personal by remembering what she once bookmarked or admired.",
            "Avoid guessing her ring size if you are not sure.",
            "If uncertain, choose earrings or a pendant before a fitted ring.",
            "Let the personal detail carry the emotion more than the size of the gift.",
        ]),
        sec("last_minute", "Last-Minute Karwa Chauth Gift Ideas for Wife", [
            "Choose a classic pendant if you need a safe and elegant option.",
            "Pick small earrings when you are unsure about sizing.",
            "Choose a bracelet only if you know her wrist preference.",
            "Avoid highly experimental designs when shopping late.",
            "Use her existing jewellery style as your shortcut.",
            "Match the metal tone to what she wears most often.",
            "Add a handwritten note to make a quick gift feel planned.",
            "Use flowers and ribbon to make the presentation warmer.",
            "Avoid gifts that need resizing if the festival is close.",
            "Pick a design she can wear beyond Karwa Chauth.",
            "Keep the message sincere and specific.",
            "A thoughtful simple gift is better than an impressive wrong one.",
        ]),
        sec("notes", "Karwa Chauth Gift Note Ideas for Wife", [
            "For the woman who makes love feel steady, warm, and real.",
            "A little sparkle for the light you bring into my life.",
            "For this Karwa Chauth and every ordinary day you make beautiful.",
            "Thank you for being my partner, my comfort, and my favourite person.",
            "Wear this as a small reminder of how deeply you are loved.",
            "For the wife whose presence makes every festival feel complete.",
            "A small gift for the big place you hold in my heart.",
            "May this keepsake remind you of our love and our promises.",
            "For every fast, every prayer, and every quiet act of care.",
            "You are my celebration today and every day.",
            "This is not just for the festival. It is for the love behind it.",
            "I chose this because it felt as graceful and special as you.",
        ]),
        sec("how_to_choose", "How to Choose the Best Karwa Chauth Gift for Wife", [
            "Start with her personal style before thinking about festival trends.",
            "Notice whether she wears pendants, rings, earrings, bangles, or bracelets most.",
            "Choose comfort if she will wear the gift through a long celebration.",
            "Avoid oversized pieces if she prefers minimal jewellery.",
            "Pick a gift that fits her wardrobe after the festival too.",
            "Check her metal preference before choosing yellow, white, or rose gold.",
            "Use earrings or pendants when sizing is uncertain.",
            "Choose rings only when you know the size or can adjust later.",
            "Pair the gift with a sincere note for emotional value.",
            "Keep the packaging warm, clean, and free of readable cards in photos.",
            "Do not make the gift feel like a duty purchase.",
            "The best Karwa Chauth gift for wife feels chosen, not merely bought.",
        ]),
    ]

    prompts = {
        "rank": "Week6 Rank 1",
        "slug": slug,
        "primary_kw": focus_kw,
        "output_prefix": prefix,
        "caption_occasion": "Karwa Chauth gift for wife",
        "caption_year": "2026",
        "flatlay_setting": "festive-mantel",
        "workflow": "Higgsfield CLI nano_banana_pro. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry. No visible screens/devices/cards/boards/readable text. Week 6 CSV has no competitor URL or supporting-keyword column, so content uses the primary keyword and natural related gift-guide phrases.",
        "higgsfield_jobs": {},
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/karwa-chauth-gift-for-wife-hero-2026.webp",
            "flatlay": "output/magnific_generated/karwa-chauth-gift-for-wife-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/karwa-chauth-gift-for-wife-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "karwa chauth gift for wife 2026 hero with The Teshvarya Pendant",
            "flatlay": "karwa chauth gift for wife 2026 flatlay with The Ebony Ring",
            "lifestyle": "karwa chauth gift for wife 2026 lifestyle with The Faliha Purse Hoop Earrings",
        },
        "schema_keywords": keywords,
        "slots": {
            "hero": slot(
                hero,
                "karwa chauth gift for wife 2026 hero with The Teshvarya Pendant",
                "Karwa Chauth gift for wife 2026 mood: The Teshvarya Pendant",
                [raw_image("Pendants", "The Teshvarya Pendant", "1_body_portrait.png"), raw_image("Pendants", "The Teshvarya Pendant", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Karwa Chauth gift for wife 2026 romantic festive hero",
                    scene="solo fair-skinned Indian adult wife in an elegant cream and maroon festive kurta smiling softly in a warm home festive corner with diyas, flowers, brass bowl, folded fabric and a wrapped gift box, camera pulled back upper-body medium portrait, full head and hairline visible, neck and pendant clearly visible, hands fully out of frame, no mehndi closeup, no paper facing camera, no screen, plain background with no signage",
                    product_name="The Teshvarya Pendant",
                    product=hero,
                    body_part="neck",
                    extra_negatives="visible hands, rings, bracelet, bangle, watch, large pendant, extra necklace, background people wearing jewellery, thali text, phone, laptop, tablet, social media screen, photo print, signage, letters, numbers, readable notebook, readable book, poster, board, white blank card",
                ),
            ),
            "flatlay": slot(
                flat,
                "karwa chauth gift for wife 2026 festive mantel flatlay with The Ebony Ring",
                "Karwa Chauth gift for wife 2026 detail: The Ebony Ring",
                [raw_image("Rings", "The Ebony Ring", "0_primary.png"), raw_image("Rings", "The Ebony Ring", "2_front.png"), raw_image("Rings", "The Ebony Ring", "6_angle.png")],
                ["primary", "front", "angle"],
                prompt_flatlay(
                    occasion="Karwa Chauth gift for wife 2026 jewellery keepsake",
                    setting="festive-mantel",
                    setting_prompt="warm festive mantel with diyas, marigold flowers, brass bowl, satin ribbon, folded cream and maroon fabric, a small wrapped gift box and a closed book turned away at the edge. The ring rests directly on the surface as a small finger ring, not around fabric or any object, not a napkin ring, not a bracelet, not a cuff. No visible phone, no laptop, no photo print, no readable text, no card facing camera",
                    product_name="The Ebony Ring",
                    product=flat,
                ),
            ),
            "lifestyle": slot(
                life,
                "karwa chauth gift for wife 2026 lifestyle with The Faliha Purse Hoop Earrings",
                "Karwa Chauth gift for wife 2026 look: The Faliha Purse Hoop Earrings",
                [raw_image("Earrings", "The Faliha Purse Hoop Earrings", "1_body_portrait.png"), raw_image("Earrings", "The Faliha Purse Hoop Earrings", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Karwa Chauth gift for wife 2026 lifestyle",
                    scene="solo fair-skinned Indian adult wife laughing softly beside a festive side table with diyas, flowers, brass bowl, folded cream fabric and a wrapped gift box, full head visible and both ears visible, cream festive blouse, no necklace, wrists and hands out of frame, warm clean home background with no screens and no readable objects",
                    product_name="The Faliha Purse Hoop Earrings, a gold mini handbag / purse shaped hoop earring design with a rectangular handle top, ribbed dangling purse body and small diamond baguette detail",
                    product=life,
                    body_part="ear",
                    extra_negatives="jhumka earrings, simple studs, plain hoops, floral earrings, chandbali earrings, necklace, bracelet, ring, watch, phone, laptop, tablet, camera, social media screen, selfie pose, photo print, planner, calendar, readable notebook, readable book, poster, board, blank card, second person",
                ),
            ),
        },
    }

    write_json(
        f"output/{prefix}_sections.json",
        {
            "meta": {"title": title, "slug": slug, "meta_desc": meta_desc, "focus_kw": focus_kw, "yoast_title": title},
            "intro": [
                "A Karwa Chauth gift for wife should feel romantic, personal, and useful beyond the festival day. This 2026 gift guide covers jewellery ideas, first Karwa Chauth gifts, luxury keepsakes, budget-friendly picks, traditional options, last-minute ideas, and heartfelt gift notes.",
                "TL;DR: Choose a pendant for romance, earrings for easy festive styling, a ring for symbolism, a bracelet for everyday wear, and a handwritten note when you want the gift to feel truly personal.",
            ],
            "sections": sections,
            "faqs": [
                ("What is the best Karwa Chauth gift for wife?", "The best Karwa Chauth gift for wife is something personal, wearable, and emotionally thoughtful. Jewellery works well because it can become a keepsake she wears beyond the festival."),
                ("Is jewellery a good Karwa Chauth gift for wife?", "Yes. Jewellery is a strong Karwa Chauth gift because it feels festive, romantic, and lasting. Choose a pendant, earrings, ring, bracelet, or bangle based on what she already loves wearing."),
                ("What should I gift my wife on her first Karwa Chauth?", "For a first Karwa Chauth, choose a meaningful keepsake rather than an overly complicated surprise. A pendant, ring, or earrings with a sincere note can make the first celebration memorable."),
                ("How do I choose a romantic Karwa Chauth gift?", "Start with her taste. Notice her favourite metal tone, usual jewellery type, and outfit style. Then add a short note about your love, gratitude, or a memory from your relationship."),
                ("What is a safe last-minute Karwa Chauth gift for wife?", "A pendant or earrings are safer last-minute options because they do not require exact sizing. Keep the design close to her everyday style and add a handwritten note."),
                ("Should I buy a traditional or modern Karwa Chauth gift?", "Choose based on her style. Traditional designs work well with sarees and festive suits, while modern minimal pieces are better if she prefers everyday wear after the celebration."),
            ],
        },
    )
    write_json(
        f"output/publish_configs/week6_rank{rank}.json",
        {
            "rank": "Week6 Rank 1",
            "sections_json": f"output/{prefix}_sections.json",
            "output_prefix": prefix,
            "carousel_id": "bs-cf-karwawife",
            "occasion_year": "Karwa Chauth gift for wife 2026",
            "carousel_alt_prefix": "karwa chauth gift for wife 2026 gift idea",
            "gift_h2": "Karwa Chauth Jewellery Gift Picks for Wife",
            "gift_blurb": "A jewellery gift can make Karwa Chauth feel more personal because it becomes part of her festive look and a keepsake for later. These BlueStone pieces pair well with romantic notes, first Karwa Chauth gifts, and thoughtful wife-gifting ideas.",
            "conclusion_html": "A Karwa Chauth gift for wife works best when it feels chosen for her, not only for the festival. Pick jewellery that matches her style, add a sincere note, and make the moment feel calm, warm, and personal.",
            "schema_keywords": keywords,
            "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
            "products": [
                product(rows, "The Sarvanya Pendant"),
                product(rows, "The Haily Ring"),
                product(rows, "The Vicky Hoop Earrings"),
                product(rows, "The Channing Bangle"),
                product(rows, "The Estrella Oval Bangle"),
                product(rows, "The Tapia Chain Bracelet"),
            ],
            "flatlay_insert_h2": "Karwa Chauth Jewellery Gift for Wife",
            "lifestyle_insert_h2": "Karwa Chauth Gift Note Ideas for Wife",
            "more_reads_html": 'Read more thoughtful occasion ideas in <a href="https://blog.bluestone.com/good-times-caption-2026/">good times caption</a>, <a href="https://blog.bluestone.com/farewell-message-for-seniors-2026/">farewell message for seniors</a>, <a href="https://blog.bluestone.com/bestie-captions-for-instagram-2026/">bestie captions for Instagram</a>, and <a href="https://blog.bluestone.com/unity-quotes-2026/">unity quotes</a>.',
            "how_to_html": "Choose by her real style first. If sizing is uncertain, prefer pendants or earrings. If she loves symbolic jewellery, choose a ring. If she wears daily pieces, pick a lightweight bracelet or bangle.",
            "faq_h2": "Frequently Asked Questions about Karwa Chauth Gift for Wife",
            "min_lines": 120,
        },
    )
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    checklist(prefix, rank, title, focus_kw, False)
    print(f"Built {prefix} with {sum(len(s['lines']) for s in sections)} gift-guide lines and related phrases mapped")


if __name__ == "__main__":
    main()
