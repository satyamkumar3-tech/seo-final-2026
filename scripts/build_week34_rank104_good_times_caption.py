#!/usr/bin/env python3
"""Build Week 3-4 Rank 104 good times caption article assets."""
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
    prefix = "Week34_Rank104_GoodTimesCaption"
    rank = 104
    slug = "good-times-caption-2026"
    focus_kw = "good times caption"
    title = "Good Times Caption 2026: Short Happy Lines"
    meta_desc = "Good times caption 2026 with short happy captions, friends lines, family memories, travel captions, weekend notes, and joyful status ideas to share online."
    keywords = ["good times caption"]

    hero = consolidated(rows, "The Sarvanya Pendant")
    flat = consolidated(rows, "The Haily Ring")
    life = consolidated(rows, "The Vicky Hoop Earrings")

    sections = [
        sec("main_caption", "Good Times Caption", [
            "Good times feel better when the caption is simple and true.",
            "Collecting little moments that make the heart feel full.",
            "Some days become memories before we even notice.",
            "Good times, kind people, and a heart that feels light.",
            "Here for the laughter, the warmth, and the stories we keep.",
            "A happy moment does not need a perfect plan.",
            "Good times are made of small joys and easy smiles.",
            "Keeping this memory close because it felt like sunshine.",
            "Some moments are too sweet to leave without a caption.",
            "Good times look simple, but they stay with us for years.",
            "This is what a peaceful kind of happiness looks like.",
            "Smiles, stories, and one more reason to feel grateful.",
        ]),
        sec("short", "Short Good Times Captions", [
            "Good times only.",
            "Joy in progress.",
            "Smiles saved here.",
            "Pure little happiness.",
            "A moment worth keeping.",
            "Golden hour, golden mood.",
            "Soft days, happy heart.",
            "Memories in the making.",
            "Simple joy wins.",
            "Here for this feeling.",
            "Happy looks good today.",
            "Good times, always.",
        ]),
        sec("friends", "Good Times Captions with Friends", [
            "Good times get louder when friends are around.",
            "The best memories usually begin with us saying yes.",
            "Friends turn ordinary plans into stories worth saving.",
            "Laughing with my favourite people and calling it a perfect day.",
            "Good times are better when everyone has a silly story to add.",
            "A group photo can hold years of comfort in one frame.",
            "Friendship is the reason this moment feels so easy.",
            "No big event, just the right people and a happy mood.",
            "These are the friends who make time feel softer.",
            "Good friends make good times feel unforgettable.",
            "Together is still my favourite place to be.",
            "Some friendships are built on laughter and little plans.",
        ]),
        sec("family", "Good Times Captions for Family", [
            "Family good times are the memories that feel like home.",
            "A simple day with family can become the warmest story.",
            "Good food, familiar voices, and hearts that know each other.",
            "The best family moments are often quiet, messy, and real.",
            "Home feels brighter when everyone is smiling together.",
            "A family laugh can fix more than a perfect plan ever could.",
            "Good times at home are the kind we return to in our minds.",
            "Love shows up in shared tea, old jokes, and easy comfort.",
            "Family memories do not need filters to feel beautiful.",
            "This moment feels like childhood, comfort, and gratitude.",
            "Good times with family always leave the heart softer.",
            "A happy home moment is a treasure in its own way.",
        ]),
        sec("travel", "Good Times Travel Captions", [
            "Good times travel with us long after the trip ends.",
            "New streets, easy laughter, and a camera full of memories.",
            "This trip gave me stories I will keep for a long time.",
            "A little sunshine, a little road, and a lot of happiness.",
            "Travel feels best when the mood is light and the company is kind.",
            "Good times found their way into every corner of this journey.",
            "Some places become special because of who we visit them with.",
            "Collecting views, laughs, and quiet moments of wonder.",
            "A good trip is measured in stories, not schedules.",
            "Wandering into memories that already feel precious.",
            "The road was simple, but the feeling was unforgettable.",
            "Every happy detour became part of the plan.",
        ]),
        sec("weekend", "Weekend Good Times Captions", [
            "Weekend good times are best when they feel unhurried.",
            "Slow morning, warm light, and no rush in the heart.",
            "This weekend is brought to you by laughter and lazy plans.",
            "Good times begin when the calendar finally lets us breathe.",
            "A quiet weekend can still make a beautiful memory.",
            "Coffee, comfort, and one soft little moment at a time.",
            "Weekend mood: grateful, relaxed, and ready to smile.",
            "No big agenda, just a happy pause.",
            "The best weekends make ordinary hours feel special.",
            "Good times are easier when the day is not chasing us.",
            "A little rest and a lot of joy.",
            "Keeping the weekend simple and the memories sweet.",
        ]),
        sec("memory", "Good Times Memory Quotes", [
            "Good times become memories when the heart decides to keep them.",
            "A happy memory is a small light we can revisit.",
            "Some moments pass quickly but stay gentle forever.",
            "The best memories do not ask for attention. They simply return when we need them.",
            "Good times remind us that joy can be found in ordinary places.",
            "A memory feels beautiful when it carries warmth without noise.",
            "What we remember most is how safe and happy we felt.",
            "Good times are proof that simple days can become special.",
            "A treasured memory is often made from laughter we did not plan.",
            "Some photos hold more feeling than words can explain.",
            "Good times may end, but their comfort can stay for years.",
            "The heart keeps a quiet album of its happiest days.",
        ]),
        sec("instagram", "Good Times Instagram Captions", [
            "Posting this because the joy was too good to keep offline.",
            "A little glimpse of a very good time.",
            "Good times caption found, memory officially saved.",
            "This photo carries a mood I want to remember.",
            "The feed needed one more happy little moment.",
            "Proof that simple plans can turn into favourite posts.",
            "A soft smile, a bright day, and a caption that feels honest.",
            "Good times look even better when they are real.",
            "Saving this square of happiness for later.",
            "A moment worth posting and a feeling worth keeping.",
            "Captioning the kind of day that made me pause.",
            "Some posts are just tiny thank you notes to life.",
        ]),
        sec("whatsapp_status", "Good Times Status for WhatsApp", [
            "Good times and peaceful energy.",
            "Living a little lighter today.",
            "Happy heart, simple day.",
            "Collecting memories, not worries.",
            "Good times are my current mood.",
            "Smiling through the small moments.",
            "A quiet kind of happiness.",
            "Feeling grateful for today.",
            "Simple joys, steady heart.",
            "More laughter, less stress.",
            "This moment feels enough.",
            "Good people, good times.",
        ]),
        sec("celebration", "Good Times Celebration Captions", [
            "Celebrating the moment, the people, and the joy in between.",
            "Good times deserve a little sparkle and a lot of gratitude.",
            "A celebration feels richer when the happiness is shared.",
            "Cheers to the tiny wins that made today brighter.",
            "Good times are worth dressing up for, even in simple ways.",
            "The best celebrations feel warm, honest, and full of laughter.",
            "A happy occasion becomes special when everyone feels included.",
            "This celebration is less about perfection and more about presence.",
            "Good times, sweet moments, and memories dressed in light.",
            "Marking this day with smiles that feel genuine.",
            "Some celebrations are loud, and some are beautifully soft.",
            "A little shine for a memory that deserves to stay.",
        ]),
        sec("gift_notes", "Good Times Gift Note Ideas", [
            "Here is a small keepsake for a memory that made us smile.",
            "For the good times we made and the many more waiting for us.",
            "A little sparkle for a day full of happy moments.",
            "May this piece remind you of laughter, warmth, and easy joy.",
            "For every simple moment that turned into something special.",
            "A small gift for someone who makes good times feel natural.",
            "Wear this as a tiny reminder of the happiness we shared.",
            "For the memories that feel soft, bright, and worth keeping.",
            "A thoughtful gift can make a good time feel even more personal.",
            "Choose jewellery that suits the person before choosing the message.",
            "Keep the note short, warm, and specific to the memory.",
            "The best gift note sounds like something only you would say.",
        ]),
    ]

    prompts = {
        "rank": "Week3-4 Rank 104",
        "slug": slug,
        "primary_kw": focus_kw,
        "output_prefix": prefix,
        "caption_occasion": "Good times caption",
        "caption_year": "2026",
        "flatlay_setting": "linen-bedside",
        "workflow": "Higgsfield CLI nano_banana_pro. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry. No visible screens/devices. No competitor URL was present in the sheet row, so content uses the plan keyword cluster per guide.",
        "higgsfield_jobs": {},
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/good-times-caption-hero-2026.webp",
            "flatlay": "output/magnific_generated/good-times-caption-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/good-times-caption-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "good times caption 2026 hero with The Sarvanya Pendant",
            "flatlay": "good times caption 2026 flatlay with The Haily Ring",
            "lifestyle": "good times caption 2026 lifestyle with The Vicky Hoop Earrings",
        },
        "schema_keywords": keywords,
        "slots": {
            "hero": slot(
                hero,
                "good times caption 2026 happy home moment with The Sarvanya Pendant",
                "Good times caption 2026 mood: The Sarvanya Pendant",
                [raw_image("Pendants", "The Sarvanya Pendant", "1_body_portrait.png"), raw_image("Pendants", "The Sarvanya Pendant", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Good times caption 2026 warm happy hero",
                    scene="solo fair-skinned Indian adult woman in a cream kurta smiling naturally at a sunlit home breakfast table with flowers, ceramic cups, folded fabric and a small wrapped gift box, camera pulled back upper-body medium portrait, full head and hairline visible, neck and pendant clearly visible, hands fully out of frame, no paper facing camera, no screen",
                    product_name="The Sarvanya Pendant",
                    product=hero,
                    body_part="neck",
                    extra_negatives="visible hands, rings, bracelet, bangle, watch, large pendant, extra necklace, background people, signage, phone, laptop, tablet, planner, calendar, readable notebook, readable book, poster, board, white blank card",
                ),
            ),
            "flatlay": slot(
                flat,
                "good times caption 2026 linen bedside flatlay with The Haily Ring",
                "Good times caption 2026 detail: The Haily Ring",
                [raw_image("Rings", "The Haily Ring", "0_primary.png"), raw_image("Rings", "The Haily Ring", "2_front.png"), raw_image("Rings", "The Haily Ring", "6_angle.png")],
                ["primary", "front", "angle"],
                prompt_flatlay(
                    occasion="Good times caption 2026 memory keepsake",
                    setting="linen-bedside",
                    setting_prompt="warm cream linen bedside surface with jasmine flowers, a ceramic cup, satin ribbon, folded fabric, a small wrapped gift box and a closed book blurred at the edge with cover turned away, no visible paper, no readable text, no phone, no laptop",
                    product_name="The Haily Ring",
                    product=flat,
                ),
            ),
            "lifestyle": slot(
                life,
                "good times caption 2026 lifestyle with The Vicky Hoop Earrings",
                "Good times caption 2026 look: The Vicky Hoop Earrings",
                [raw_image("Earrings", "The Vicky Hoop Earrings", "1_body_portrait.png"), raw_image("Earrings", "The Vicky Hoop Earrings", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Good times caption 2026 lifestyle memory",
                    scene="solo fair-skinned Indian adult woman laughing softly beside a window with flowers, ceramic cup, folded cream fabric and a wrapped gift box on a side table, full head visible and both ears visible, cream blouse, no necklace, wrists and hands out of frame, clean bright home with no screens and no readable objects",
                    product_name="The Vicky Hoop Earrings",
                    product=life,
                    body_part="ear",
                    extra_negatives="necklace, bracelet, ring, watch, phone, laptop, tablet, planner, calendar, readable notebook, readable book, poster, board, blank card, second person",
                ),
            ),
        },
    }

    write_json(
        f"output/{prefix}_sections.json",
        {
            "meta": {"title": title, "slug": slug, "meta_desc": meta_desc, "focus_kw": focus_kw, "yoast_title": title},
            "intro": [
                "A good times caption should make a happy photo feel even warmer without trying too hard. This 2026 collection includes short captions, friends captions, family lines, travel captions, weekend status ideas, celebration notes, and gift-note wording.",
                "TL;DR: Pick a short caption for quick posts, a friends or family line for group photos, a travel caption for trip memories, and a gift note when the moment deserves something more personal.",
            ],
            "sections": sections,
            "faqs": [
                ("What is a good times caption?", "A good times caption is a short line that describes a happy memory, easy laughter, or a meaningful moment. The best one sounds natural and matches the photo instead of feeling overly formal."),
                ("How do I write a short good times caption?", "Keep it simple and specific. Mention the feeling, the people, or the moment in a few words. Short lines such as good times only or memories in the making work well for casual posts."),
                ("Can I use good times caption lines for friends?", "Yes. For friends, choose captions about laughter, inside jokes, shared plans, and memories. Keep the tone relaxed so the line feels like part of the moment."),
                ("What should I write for family good times?", "For family good times, write about home, comfort, shared meals, familiar jokes, and gratitude. A warm and simple caption usually feels better than a dramatic one."),
                ("Are good times captions good for WhatsApp status?", "Yes. Good times captions work well as WhatsApp status when they are short, positive, and easy to read. Choose one line that reflects your current mood."),
                ("Can I add a jewellery gift note to a good times memory?", "Yes. A small jewellery gift note can mark a special memory, celebration, or shared moment. Keep the message personal, warm, and connected to the reason you are gifting it."),
            ],
        },
    )
    write_json(
        f"output/publish_configs/week34_rank{rank}.json",
        {
            "rank": "Week3-4 Rank 104",
            "sections_json": f"output/{prefix}_sections.json",
            "output_prefix": prefix,
            "carousel_id": "bs-cf-goodtimes",
            "occasion_year": "Good times caption 2026",
            "carousel_alt_prefix": "good times caption 2026 gift idea",
            "gift_h2": "Good Times Gift Ideas with Thoughtful Notes",
            "gift_blurb": "Good times feel even more personal when a keepsake marks the memory. These BlueStone pieces pair well with happy captions, friendship notes, family moments, and celebration messages.",
            "conclusion_html": "A good times caption works best when it sounds like the real moment. Choose a short line for quick posts, a warmer line for family or friends, and a simple note when the memory becomes a gift.",
            "schema_keywords": keywords,
            "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
            "products": [
                product(rows, "The Melene Evil Eye Pendant"),
                product(rows, "The Gigi Ring"),
                product(rows, "The Estrella Oval Bangle"),
                product(rows, "The Tapia Chain Bracelet"),
                product(rows, "The Ailia Evil Eye Layered Necklace"),
                product(rows, "The Malibu Ring"),
            ],
            "flatlay_insert_h2": "Good Times Memory Quotes",
            "lifestyle_insert_h2": "Good Times Gift Note Ideas",
            "more_reads_html": 'Read more warm lines in <a href="https://blog.bluestone.com/busy-people-quotes-2026/">busy people quotes</a>, <a href="https://blog.bluestone.com/unity-quotes-2026/">unity quotes</a>, <a href="https://blog.bluestone.com/student-success-motivational-quotes-2026/">student success motivational quotes</a>, and <a href="https://blog.bluestone.com/good-luck-wishes-2026/">good luck wishes</a>.',
            "how_to_html": "Choose the line that matches the photo first. Use a short caption for Instagram, a softer line for family photos, a relaxed status for WhatsApp, and a personal note when the good time is tied to a gift or celebration.",
            "faq_h2": "Frequently Asked Questions about Good Times Caption",
            "min_lines": 120,
        },
    )
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    checklist(prefix, rank, title, focus_kw, False)
    print(f"Built {prefix} with {sum(len(s['lines']) for s in sections)} shareable lines and supporting keywords mapped")


if __name__ == "__main__":
    main()
