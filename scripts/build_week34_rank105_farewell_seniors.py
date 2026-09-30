#!/usr/bin/env python3
"""Build Week 3-4 Rank 105 farewell message for seniors article assets."""
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
    prefix = "Week34_Rank105_FarewellSeniors"
    rank = 105
    slug = "farewell-message-for-seniors-2026"
    focus_kw = "farewell message for seniors"
    title = "Farewell Message for Seniors 2026: Heartfelt Lines"
    meta_desc = "Farewell message for seniors 2026 with heartfelt school, college, office, funny, emotional, short, WhatsApp, speech, and gift note lines for seniors now."
    keywords = ["farewell message for seniors"]

    hero = consolidated(rows, "The Aagarna Pendant")
    flat = consolidated(rows, "The Quinn Ring")
    life = consolidated(rows, "The Nettile Huggie Earrings")

    sections = [
        sec("main", "Farewell Message for Seniors", [
            "Dear seniors, your journey has inspired us more than you may ever know.",
            "You leave behind lessons, laughter, and a standard we will always remember.",
            "Farewell to the seniors who made every ordinary day feel warmer and wiser.",
            "Your guidance helped us feel less new and more confident.",
            "We will miss your presence, your jokes, and the way you made things easier.",
            "Thank you for leading with kindness and leaving with grace.",
            "May your next chapter be as bright as the memories you leave behind.",
            "You were seniors by title, but mentors by heart.",
            "The halls will feel different without your energy and encouragement.",
            "Farewell, seniors. May success meet you wherever you go.",
            "Your advice will stay with us long after this goodbye.",
            "Today we say farewell, but we keep your example close.",
        ]),
        sec("short", "Short Farewell Messages for Seniors", [
            "Farewell, seniors. Shine wherever life takes you.",
            "Thank you for every lesson and every smile.",
            "Your next chapter is lucky to have you.",
            "Goodbye for now, and best wishes always.",
            "You made this place better by being here.",
            "We will miss your guidance and warmth.",
            "Keep growing, keep winning, keep smiling.",
            "Farewell to our favourite seniors.",
            "May your future be full of proud moments.",
            "Your memories will stay with us.",
            "Good luck for the road ahead.",
            "Thank you for showing us the way.",
        ]),
        sec("emotional", "Emotional Farewell Message for Seniors", [
            "Saying goodbye to seniors like you feels difficult because you made this place feel safe.",
            "Your kindness turned nervous beginnings into confident days.",
            "We did not just learn from your achievements. We learned from your patience.",
            "The memories you leave behind will keep reminding us to be better.",
            "Farewell is a small word for the gratitude we feel today.",
            "You gave us advice when we needed direction and laughter when we needed comfort.",
            "It is hard to imagine the same corridors without your voices.",
            "Your final day here is not the end of your impact on us.",
            "We will carry your encouragement into our own senior year.",
            "Thank you for being the kind of seniors juniors hope to become.",
            "May this goodbye open a future full of peace, success, and happiness.",
            "You are leaving the campus, but not the stories we will keep telling.",
        ]),
        sec("school", "Farewell Message for School Seniors", [
            "Dear school seniors, thank you for making junior years feel less scary.",
            "You showed us how to balance fun, discipline, and friendship.",
            "Your classroom stories and corridor laughs will stay with us.",
            "We learned confidence by watching you lead school events with ease.",
            "Farewell to the seniors who made assemblies, games, and clubs memorable.",
            "May your board results, dreams, and next school chapter make you proud.",
            "You taught us that growing up can be graceful and fun at the same time.",
            "The school gates will miss your energy, but your memories will stay.",
            "Thank you for cheering us on during competitions and nervous first attempts.",
            "We hope your future classrooms welcome you with the same warmth you gave us.",
            "Farewell, seniors. Keep your school spirit alive wherever you go.",
            "May every lesson learned here help you build a brave future.",
        ]),
        sec("college", "Farewell Message for College Seniors", [
            "College felt easier because seniors like you shared notes, advice, and honest stories.",
            "Thank you for turning confusing semesters into manageable memories.",
            "Your batch gave us friendship goals, leadership goals, and placement-season courage.",
            "Farewell to the seniors who made campus life feel complete.",
            "May your careers begin with confidence and your dreams keep expanding.",
            "We will miss your hostel stories, event energy, and late-night guidance.",
            "You taught us that college is about people as much as classes.",
            "The canteen, fest ground, and department corridors will remember your laughter.",
            "Thank you for making juniors feel included in every celebration.",
            "May your next city, workplace, or course bring you everything you deserve.",
            "Farewell, seniors. Your college legacy is safe in our hearts.",
            "We hope to make you proud when it becomes our turn to lead.",
        ]),
        sec("office", "Farewell Message for Seniors at Office", [
            "Working with seniors like you has been a lesson in patience, clarity, and professionalism.",
            "Thank you for mentoring us without making us feel small.",
            "Your guidance made tough tasks feel possible and new responsibilities feel manageable.",
            "Farewell to a senior who led with calm confidence and real kindness.",
            "We will miss your advice, your problem-solving, and your steady presence.",
            "May your next role bring growth, respect, and well-earned success.",
            "You showed us that good leadership is both firm and thoughtful.",
            "The team will feel your absence, but your methods will remain with us.",
            "Thank you for helping us become better colleagues and better learners.",
            "Farewell, and may every new project value your talent the way we do.",
            "Your professionalism set a standard we will continue to follow.",
            "Wishing you a future filled with meaningful work and peaceful wins.",
        ]),
        sec("funny", "Funny Farewell Messages for Seniors", [
            "Farewell, seniors. We promise to miss you almost as much as we miss free treats.",
            "You are leaving, but your legendary excuses will remain in our hearts.",
            "Goodbye seniors, and thank you for teaching us which rules are flexible.",
            "We will miss your advice, your drama, and your snacks.",
            "May your future be bright and your group chats stay chaotic.",
            "Farewell to the seniors who made deadlines look optional and confidence look easy.",
            "Your juniors are now officially promoted to confused seniors in training.",
            "Please come back sometimes, preferably with food.",
            "We learned a lot from you, including how to look busy at the right moment.",
            "Good luck ahead. Do not forget the juniors who laughed at your jokes.",
            "Farewell, seniors. Your attendance strategies were truly educational.",
            "May your next chapter have fewer deadlines and better Wi-Fi.",
        ]),
        sec("whatsapp", "Farewell Message for Seniors on WhatsApp", [
            "Farewell seniors, and thank you for every little help you gave us.",
            "Wishing you success, happiness, and a beautiful new beginning.",
            "Your batch will always be remembered with respect and warmth.",
            "Thank you for being seniors we could actually talk to.",
            "Good luck for your next chapter. Keep shining.",
            "We will miss the way you made everything feel easier.",
            "Farewell, and may life reward all your hard work.",
            "Your memories will stay in every corner of this place.",
            "Thank you for guiding us like elder friends.",
            "Best wishes for a future full of good news.",
            "Goodbye seniors. Stay happy and stay connected.",
            "May your journey ahead be successful and peaceful.",
        ]),
        sec("speech", "Farewell Speech Lines for Seniors", [
            "Today is not just a farewell. It is a thank you for every moment our seniors gave us.",
            "We stand here with gratitude for a batch that taught us leadership through example.",
            "Our seniors helped us understand this place before we truly belonged to it.",
            "They turned nervous questions into honest conversations and difficult days into manageable ones.",
            "Their achievements will inspire us, but their kindness will stay with us even more.",
            "A senior batch is remembered not only by results, but by the juniors they encourage.",
            "You have given us memories that will outlast this farewell event.",
            "As you move ahead, we hope every dream you carried here finds its path.",
            "We promise to continue the warmth and guidance you showed us.",
            "Thank you for being mentors, friends, leaders, and examples.",
            "This goodbye is filled with respect, pride, and good wishes.",
            "Farewell seniors, and may your next journey be brighter than you imagined.",
        ]),
        sec("gift_notes", "Farewell Gift Note Ideas for Seniors", [
            "A small keepsake for a senior who made this journey easier.",
            "Wear this as a reminder of the people who will always cheer for you.",
            "For your next chapter, with gratitude from your juniors.",
            "A little sparkle for the memories, lessons, and laughter you leave behind.",
            "Thank you for guiding us with patience and kindness.",
            "May this gift remind you that your presence here mattered.",
            "For the senior who turned advice into encouragement.",
            "Carry this small token into a future full of proud moments.",
            "A farewell gift for someone we will remember with warmth.",
            "Choose a wearable piece that matches their everyday style.",
            "Keep the farewell note specific, sincere, and pressure-free.",
            "The best gift message says thank you without making the goodbye heavy.",
        ]),
        sec("captions", "Farewell Captions for Seniors", [
            "Goodbyes are hard when the seniors were this special.",
            "A farewell full of memories and gratitude.",
            "The batch may leave, but the stories stay.",
            "Seniors today, inspiration always.",
            "Thank you for the lessons, laughs, and legacy.",
            "One last photo for a batch we will miss.",
            "Farewell to the people who made this place brighter.",
            "The next chapter begins, but the memories remain.",
            "Respect, gratitude, and a little bit of goodbye sadness.",
            "For the seniors who became our comfort zone.",
            "Leaving with pride, remembered with love.",
            "Good luck, seniors. Keep shining.",
        ]),
    ]

    prompts = {
        "rank": "Week3-4 Rank 105",
        "slug": slug,
        "primary_kw": focus_kw,
        "output_prefix": prefix,
        "caption_occasion": "Farewell message for seniors",
        "caption_year": "2026",
        "flatlay_setting": "gift-wrapping-station",
        "workflow": "Higgsfield CLI nano_banana_pro. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry. No visible screens/devices/cards/boards/readable text. No competitor URL was present in the sheet row, so content uses the plan keyword cluster per guide.",
        "higgsfield_jobs": {},
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/farewell-message-for-seniors-hero-2026.webp",
            "flatlay": "output/magnific_generated/farewell-message-for-seniors-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/farewell-message-for-seniors-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "farewell message for seniors 2026 hero with The Aagarna Pendant",
            "flatlay": "farewell message for seniors 2026 flatlay with The Quinn Ring",
            "lifestyle": "farewell message for seniors 2026 lifestyle with The Nettile Huggie Earrings",
        },
        "schema_keywords": keywords,
        "slots": {
            "hero": slot(
                hero,
                "farewell message for seniors 2026 heartfelt farewell hero with The Aagarna Pendant",
                "Farewell message for seniors 2026 mood: The Aagarna Pendant",
                [raw_image("Pendants", "The Aagarna Pendant", "1_body_portrait.png"), raw_image("Pendants", "The Aagarna Pendant", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Farewell message for seniors 2026 heartfelt hero",
                    scene="solo fair-skinned Indian adult woman senior in an elegant cream kurta smiling gently in a warm farewell gathering corner with a plain cream wall, flowers, ribbon, a wrapped gift box, ceramic cup and folded fabric, camera pulled back upper-body medium portrait, full head and hairline visible, neck and pendant clearly visible, hands fully out of frame, no paper facing camera, no screen, no banner, no garland letters, no alphabet shapes, no signage, no readable farewell sign",
                    product_name="The Aagarna Pendant",
                    product=hero,
                    body_part="neck",
                    extra_negatives="visible hands, rings, bracelet, bangle, watch, large pendant, extra necklace, background people wearing jewellery, signage, farewell banner, decorative letter garland, alphabet cutouts, letters on wall, words, phone, laptop, tablet, planner, calendar, readable notebook, readable book, poster, board, white blank card",
                ),
            ),
            "flatlay": slot(
                flat,
                "farewell message for seniors 2026 gift wrapping flatlay with The Quinn Ring",
                "Farewell message for seniors 2026 detail: The Quinn Ring",
                [raw_image("Rings", "The Quinn Ring", "0_primary.png"), raw_image("Rings", "The Quinn Ring", "2_front.png"), raw_image("Rings", "The Quinn Ring", "6_angle.png")],
                ["primary", "front", "angle"],
                prompt_flatlay(
                    occasion="Farewell message for seniors 2026 gift note",
                    setting="gift-wrapping-station",
                    setting_prompt="cream fabric gift-wrapping surface with satin ribbon, jasmine flowers, small wrapped gift box, brass bowl, folded cloth and a closed book turned away at the edge, no visible paper, no readable text, no card facing camera, no phone, no laptop",
                    product_name="The Quinn Ring",
                    product=flat,
                ),
            ),
            "lifestyle": slot(
                life,
                "farewell message for seniors 2026 lifestyle with The Nettile Huggie Earrings",
                "Farewell message for seniors 2026 look: The Nettile Huggie Earrings",
                [raw_image("Earrings", "The Nettile Huggie Earrings", "1_body_portrait.png"), raw_image("Earrings", "The Nettile Huggie Earrings", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Farewell message for seniors 2026 lifestyle",
                    scene="solo fair-skinned Indian adult woman senior laughing softly beside a window after a farewell moment, flowers and wrapped gift box on a side table, full head visible and both ears visible, cream blouse, no necklace, wrists and hands out of frame, warm clean indoor background with no screens and no readable objects",
                    product_name="The Nettile Huggie Earrings",
                    product=life,
                    body_part="ear",
                    extra_negatives="necklace, bracelet, ring, watch, phone, laptop, tablet, planner, calendar, readable notebook, readable book, poster, board, blank card, farewell sign, second person",
                ),
            ),
        },
    }

    write_json(
        f"output/{prefix}_sections.json",
        {
            "meta": {"title": title, "slug": slug, "meta_desc": meta_desc, "focus_kw": focus_kw, "yoast_title": title},
            "intro": [
                "A farewell message for seniors should feel respectful, warm, and personal without sounding too heavy. This 2026 collection includes short messages, emotional lines, school and college notes, office farewells, funny messages, WhatsApp text, speech lines, captions, and gift-note ideas.",
                "TL;DR: Choose a short line for WhatsApp, an emotional message for a card, a speech line for the stage, a funny note for close seniors, and a gift note when you want the goodbye to feel more personal.",
            ],
            "sections": sections,
            "faqs": [
                ("What is the best farewell message for seniors?", "The best farewell message for seniors is sincere, specific, and respectful. Thank them for their guidance, mention a memory or quality you admire, and wish them success in their next chapter."),
                ("How do I write a short farewell message for seniors?", "Keep it to one or two lines. Say thank you, add a warm wish, and avoid making the message too formal if you know the senior personally."),
                ("What should juniors say to seniors on farewell?", "Juniors can thank seniors for guidance, friendship, support, and inspiration. A good message should make the seniors feel remembered, not just officially appreciated."),
                ("Can farewell messages for seniors be funny?", "Yes, funny farewell messages work well when you share a close bond. Keep the humour kind and avoid jokes that may embarrass anyone during the farewell."),
                ("What is a good farewell speech line for seniors?", "A good speech line is: Today is not only a goodbye, it is a thank you for the guidance, laughter, and example our seniors leave behind."),
                ("Can jewellery work as a farewell gift for seniors?", "Yes. A small jewellery keepsake can mark gratitude and a new chapter. Pair it with a short note that thanks the senior for their presence and wishes them well."),
            ],
        },
    )
    write_json(
        f"output/publish_configs/week34_rank{rank}.json",
        {
            "rank": "Week3-4 Rank 105",
            "sections_json": f"output/{prefix}_sections.json",
            "output_prefix": prefix,
            "carousel_id": "bs-cf-farewellseniors",
            "occasion_year": "Farewell message for seniors 2026",
            "carousel_alt_prefix": "farewell message for seniors 2026 gift idea",
            "gift_h2": "Farewell Gift Ideas for Seniors with Thoughtful Notes",
            "gift_blurb": "A farewell gift feels meaningful when it marks gratitude, guidance, and the next chapter. These BlueStone pieces pair well with senior farewell notes, speeches, captions, and warm goodbye messages.",
            "conclusion_html": "A farewell message for seniors works best when it feels honest and specific. Choose a short line for quick sharing, a warmer note for cards, and a thoughtful gift message when you want the goodbye to stay memorable.",
            "schema_keywords": keywords,
            "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
            "products": [
                product(rows, "The Teshvarya Pendant"),
                product(rows, "The Rafia Ring"),
                product(rows, "The Ebony Ring"),
                product(rows, "The Rohal Huggie Earrings"),
                product(rows, "The Asya Huggie Earrings"),
                product(rows, "The Shining Star Bracelet"),
            ],
            "flatlay_insert_h2": "Farewell Gift Note Ideas for Seniors",
            "lifestyle_insert_h2": "Farewell Captions for Seniors",
            "more_reads_html": 'Read more thoughtful lines in <a href="https://blog.bluestone.com/good-times-caption-2026/">good times caption</a>, <a href="https://blog.bluestone.com/student-success-motivational-quotes-2026/">student success motivational quotes</a>, <a href="https://blog.bluestone.com/good-luck-wishes-2026/">good luck wishes</a>, and <a href="https://blog.bluestone.com/unity-quotes-2026/">unity quotes</a>.',
            "how_to_html": "Match the message to your relationship. Use a respectful tone for formal seniors, a funny line for close seniors, a speech line for the farewell stage, and a short gift note when you want the memory to feel personal.",
            "faq_h2": "Frequently Asked Questions about Farewell Message for Seniors",
            "min_lines": 120,
        },
    )
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    checklist(prefix, rank, title, focus_kw, False)
    print(f"Built {prefix} with {sum(len(s['lines']) for s in sections)} shareable lines and supporting keywords mapped")


if __name__ == "__main__":
    main()
