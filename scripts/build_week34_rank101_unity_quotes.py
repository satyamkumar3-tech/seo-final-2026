#!/usr/bin/env python3
"""Build Week 3-4 Rank 101 unity quotes article assets."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from build_week34_rank9_10_batch import (  # noqa: E402
    ROOT,
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
    prefix = "Week34_Rank101_UnityQuotes"
    rank = 101
    slug = "unity-quotes-2026"
    kw = "unity quotes"
    title = "Unity Quotes 2026: Short Lines on Togetherness"
    meta_desc = "Unity quotes 2026 with short, inspirational, family, friendship, teamwork, student, community, and caption lines about togetherness and harmony today."
    keywords = [kw, "togetherness quotes", "team unity quotes", "family unity quotes", "community quotes"]

    hero = consolidated(rows, "The Ixea Evil Eye Pendant")
    flat = consolidated(rows, "The Channing Bangle")
    life = consolidated(rows, "The Kricia Charm Bracelet")

    sections = [
        sec("main", "Unity Quotes", [
            "Unity begins when people choose the same hope over separate doubts.",
            "A united heart can make even a difficult road feel lighter.",
            "When we stand together, small efforts become a lasting strength.",
            "Unity is not sameness. It is respect that makes differences feel safe.",
            "The strongest bonds are built by listening before judging.",
            "Togetherness grows when every voice is treated with care.",
            "A united family, team, or community can carry more than one person alone.",
            "Unity turns ordinary people into a circle of support.",
            "The beauty of unity is that no one has to feel invisible.",
            "Peace becomes practical when people decide to protect each other.",
            "A shared purpose can make separate paths meet with grace.",
            "Unity is the quiet strength of people who refuse to give up on one another.",
            "Real togetherness means making space, not taking control.",
            "Where unity lives, courage spreads from one person to the next.",
        ]),
        sec("short", "Short Unity Quotes", [
            "Together, we rise.",
            "Unity makes hope stronger.",
            "One bond can hold many hearts.",
            "Stand together, shine together.",
            "Harmony begins with respect.",
            "Togetherness is quiet strength.",
            "United hearts move mountains.",
            "Peace grows through unity.",
            "One team, one purpose.",
            "Unity is shared courage.",
            "Together feels lighter.",
            "Respect keeps unity alive.",
            "Many hands, one hope.",
            "Unity turns effort into impact.",
        ]),
        sec("family", "Unity Quotes for Family", [
            "A family stays strong when love is louder than ego.",
            "Unity at home begins with patience in small moments.",
            "A united family can face storms without losing warmth.",
            "The best family bond is built with forgiveness, respect, and honest care.",
            "When family members stand together, every celebration feels brighter.",
            "Home feels safe when every person knows they belong.",
            "Family unity is not perfect agreement. It is choosing love after disagreement.",
            "The strongest homes are held by trust, not by control.",
            "A united family makes ordinary days feel blessed.",
            "When one person struggles, family unity becomes a shared hand to hold.",
            "Love grows deeper when family listens with a soft heart.",
            "A family that stays united gives every member courage to grow.",
        ]),
        sec("teamwork", "Unity Quotes for Teamwork", [
            "A team becomes powerful when each person respects the work of the other.",
            "Unity at work turns deadlines into shared victories.",
            "The best teams do not compete for credit. They build the result together.",
            "A united team can solve problems that look too large for one mind.",
            "Team unity is built in the small choices to help, listen, and follow through.",
            "Shared purpose makes effort feel meaningful.",
            "A team wins when trust moves faster than blame.",
            "Unity does not remove pressure. It makes pressure easier to carry.",
            "Every strong team needs clear goals and kind communication.",
            "Progress becomes steady when people pull in the same direction.",
            "A united team celebrates every role, not only the loudest one.",
            "The real success of teamwork is knowing no one had to stand alone.",
        ]),
        sec("friends", "Unity Quotes for Friends", [
            "Friendship feels strongest when friends show up without being asked.",
            "Unity among friends is made of loyalty, laughter, and honest support.",
            "Good friends may think differently, but they protect the bond with care.",
            "A united circle of friends can make heavy days feel lighter.",
            "Real friends do not let distance weaken togetherness.",
            "Friendship unity means celebrating wins without jealousy.",
            "A true friend group gives everyone room to be themselves.",
            "Togetherness is a small message that arrives at the right time.",
            "Friends stay united when respect is stronger than misunderstanding.",
            "A loyal friend stands beside you in silence and in celebration.",
            "The best friendships feel like a soft place to return.",
            "Unity in friendship is choosing the bond again and again.",
        ]),
        sec("inspirational", "Inspirational Unity Quotes", [
            "A united dream has more strength than a lonely fear.",
            "When people gather with kindness, hope becomes visible.",
            "Unity is a bridge built one respectful choice at a time.",
            "The world feels less divided when one person chooses compassion first.",
            "Togetherness can turn a small beginning into a movement.",
            "A single voice can inspire, but united voices can transform.",
            "Unity asks us to protect what we share without erasing who we are.",
            "Every act of cooperation is a quiet vote for a better future.",
            "When hearts align, even slow progress becomes powerful.",
            "Unity is courage with company.",
            "A generous spirit makes community possible.",
            "The strongest light is the one many people help keep alive.",
        ]),
        sec("students", "Unity Quotes for Students", [
            "A classroom grows brighter when students learn together.",
            "Unity teaches students that success is not only personal.",
            "When classmates help one another, confidence spreads.",
            "A united class can make learning feel friendly and fearless.",
            "Respecting different ideas is the first lesson of unity.",
            "Students grow faster when competition is balanced with kindness.",
            "Team spirit begins with including the quietest voice.",
            "A group project works best when every effort is valued.",
            "Unity in school means no one is left outside the circle.",
            "Learning together creates memories that marks alone cannot give.",
            "A kind classmate can make school feel safer.",
            "Students who stand together learn leadership early.",
        ]),
        sec("community", "Unity Quotes for India and Community", [
            "A community becomes strong when people care beyond their own door.",
            "Unity in diversity is respect made visible.",
            "A peaceful society begins with neighbours who choose understanding.",
            "India shines brightest when many cultures stand with one heart.",
            "Community unity grows through service, patience, and shared responsibility.",
            "A festival, a street, or a city becomes beautiful when everyone feels included.",
            "Harmony is built when people honour both difference and belonging.",
            "A united community can protect hope during difficult times.",
            "Kindness is the simplest language of unity.",
            "Public peace begins with private respect.",
            "When communities stand together, progress feels possible.",
            "Unity is the strength of many stories held with dignity.",
        ]),
        sec("captions", "One Line Unity Captions", [
            "Together is a beautiful direction.",
            "One circle, many hearts.",
            "Unity looks good on everyone.",
            "Building harmony, one moment at a time.",
            "Better together, always.",
            "A little kindness can unite a room.",
            "Many voices, shared hope.",
            "Togetherness over ego.",
            "United by care.",
            "The bond is the blessing.",
            "Harmony feels like home.",
            "One purpose, gentle hearts.",
        ]),
        sec("cards", "Unity Message Ideas for Cards", [
            "May we always choose togetherness over distance.",
            "Wishing you a life surrounded by people who stand with you.",
            "May every bond in your life grow with trust and patience.",
            "Here is to unity, shared laughter, and peaceful hearts.",
            "May your family and friends stay connected through every season.",
            "Wishing you the kind of support that makes difficult days softer.",
            "May togetherness bring strength to every new chapter.",
            "Let this note remind you that you are not alone.",
            "May our bond stay warm, respectful, and steady.",
            "Wishing you harmony at home, at work, and in every relationship.",
            "May kindness keep every circle in your life bright.",
            "Here is to people who make unity feel natural.",
        ]),
        sec("gift_notes", "Unity Gift Note Ideas", [
            "Choose a small keepsake when the message is about a lasting bond.",
            "A pendant can sit close to the heart and echo a unity message softly.",
            "A bangle can feel like a circle of support and shared strength.",
            "A bracelet works well for friendship, team, or family togetherness notes.",
            "Write one sentence about the bond before you mention the gift.",
            "Use flowers, ribbon, a ceramic cup, or folded fabric for photos instead of screens.",
            "Keep the note personal and simple.",
            "A unity gift should feel thoughtful, not loud.",
            "Choose jewellery that matches the recipient's everyday style.",
            "Let the message carry the emotion and the gift carry the memory.",
            "A keepsake feels warmer when it celebrates shared history.",
            "The best unity gift says, we are connected, even when life is busy.",
        ]),
    ]

    prompts = {
        "rank": "Week3-4 Rank 101",
        "slug": slug,
        "primary_kw": kw,
        "output_prefix": prefix,
        "caption_occasion": "Unity quotes",
        "caption_year": "2026",
        "flatlay_setting": "windowsill-daylight",
        "workflow": "Higgsfield CLI nano_banana_pro. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry. No visible screens/devices.",
        "higgsfield_jobs": {},
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/unity-quotes-hero-2026.webp",
            "flatlay": "output/magnific_generated/unity-quotes-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/unity-quotes-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "unity quotes 2026 hero with The Ixea Evil Eye Pendant",
            "flatlay": "unity quotes 2026 flatlay with The Channing Bangle",
            "lifestyle": "unity quotes 2026 lifestyle with The Kricia Charm Bracelet",
        },
        "schema_keywords": keywords,
        "slots": {
            "hero": slot(
                hero,
                "unity quotes 2026 hero with The Ixea Evil Eye Pendant",
                "Unity quotes 2026 mood: The Ixea Evil Eye Pendant",
                [raw_image("Pendants", "The Ixea Evil Eye Pendant", "1_body_portrait.png"), raw_image("Pendants", "The Ixea Evil Eye Pendant", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Unity quotes 2026 hero",
                    scene="solo fair-skinned Indian adult woman in a soft ivory kurta arranging jasmine flowers and a small wrapped gift on a bright windowsill, peaceful togetherness mood, camera pulled back medium shot with generous safe margin above the hair, complete head and hairline fully visible, full face visible, neck and pendant clearly visible, no paper facing camera",
                    product_name="The Ixea Evil Eye Pendant",
                    product=hero,
                    body_part="neck",
                    extra_negatives="large pendant, extra necklace, phone, laptop, greeting card, poster, board",
                ),
            ),
            "flatlay": slot(
                flat,
                "unity quotes 2026 flatlay with The Channing Bangle",
                "Unity quotes 2026 detail: The Channing Bangle",
                [raw_image("Bangles", "The Channing Bangle", "0_primary.png"), raw_image("Bangles", "The Channing Bangle", "2_front.png"), raw_image("Bangles", "The Channing Bangle", "4_close_up.png")],
                ["primary", "front", "close_up"],
                prompt_flatlay(
                    occasion="Unity quotes 2026",
                    setting="windowsill-daylight",
                    setting_prompt="painted cream windowsill with sheer curtain blur, small plant pot turned away, jasmine flowers, silk ribbon, ceramic cup, folded cream fabric, no paper, no card, no text",
                    product_name="The Channing Bangle",
                    product=flat,
                ),
            ),
            "lifestyle": slot(
                life,
                "unity quotes 2026 lifestyle with The Kricia Charm Bracelet",
                "Unity quotes 2026 look: The Kricia Charm Bracelet",
                [raw_image("Bracelets", "The Kricia Charm Bracelet", "1_body_portrait.png"), raw_image("Bracelets", "The Kricia Charm Bracelet", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Unity quotes 2026 lifestyle",
                    scene="solo fair-skinned Indian adult woman gently tying a ribbon around a wrapped gift beside flowers and a ceramic cup, full head visible, wrist and bracelet clearly visible at natural worn scale, warm home setting about togetherness",
                    product_name="The Kricia Charm Bracelet",
                    product=life,
                    body_part="wrist",
                    extra_negatives="extra bracelet, watch, ring, phone, laptop, greeting card, poster, board, text",
                ),
            ),
        },
    }

    write_json(
        f"output/{prefix}_sections.json",
        {
            "meta": {"title": title, "slug": slug, "meta_desc": meta_desc, "focus_kw": kw, "yoast_title": title},
            "intro": [
                "Unity quotes are useful when you want a short line about togetherness, teamwork, family, friendship, or community harmony. This 2026 collection gives you copy-ready lines for captions, cards, school notes, office messages, and thoughtful gift notes.",
                "TL;DR: Use a short unity quote for captions, a family unity line for home, a teamwork quote for office groups, and a community quote when the message is about harmony and inclusion.",
            ],
            "sections": sections,
            "faqs": [
                ("What are the best unity quotes?", "The best unity quotes are short, warm, and easy to remember. Choose lines about respect, togetherness, shared purpose, and support when you want the message to work for family, friends, teams, or community moments."),
                ("How do I use unity quotes in captions?", "Pick a one-line quote that matches the photo. For a group photo, choose a togetherness caption. For a family post, use a warmer line about bonds. Keep it simple so the message feels natural."),
                ("Can unity quotes be used for students?", "Yes. Unity quotes work well for school assemblies, classroom boards, speeches, and group projects. Choose student-friendly lines about inclusion, teamwork, respect, and helping classmates succeed together."),
                ("What should I write in a unity card?", "Write one clear sentence about the bond you share, then add a wish for harmony or support. A good card message feels personal, calm, and sincere instead of sounding like a formal slogan."),
                ("Can I pair unity quotes with a gift?", "Yes. A small jewellery keepsake can make a unity message feel more memorable when the relationship is close. Keep the note thoughtful and avoid turning the message into a product pitch."),
                ("Are unity quotes only for teams?", "No. Unity quotes can be used for families, friends, schools, communities, workplaces, and social captions. The same idea works anywhere people need trust, respect, and shared effort."),
            ],
        },
    )
    write_json(
        f"output/publish_configs/week34_rank{rank}.json",
        {
            "rank": "Week3-4 Rank 101",
            "sections_json": f"output/{prefix}_sections.json",
            "output_prefix": prefix,
            "carousel_id": "bs-cf-unityquotes",
            "occasion_year": "Unity quotes 2026",
            "carousel_alt_prefix": "unity quotes 2026 gift idea",
            "gift_h2": "Unity Gift Ideas with Meaningful Notes",
            "gift_blurb": "A unity message often feels most special when it celebrates a bond. These BlueStone pieces pair well with family notes, friendship lines, team thank you messages, and thoughtful togetherness captions.",
            "conclusion_html": "Unity quotes work best when they feel simple, sincere, and easy to share. Choose the line that matches your bond, then add one personal detail to make it yours.",
            "schema_keywords": keywords,
            "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
            "products": [
                product(rows, "The Ixea Evil Eye Pendant"),
                product(rows, "The Liza ring"),
                product(rows, "The Channing Bangle"),
                product(rows, "The Kricia Charm Bracelet"),
                product(rows, "The Aarabhi Mangalsutra"),
                product(rows, "The Aleena Huggie Earrings"),
            ],
            "flatlay_insert_h2": "Unity Quotes for Family",
            "lifestyle_insert_h2": "Unity Gift Note Ideas",
            "more_reads_html": 'Read more thoughtful lines in <a href="https://blog.bluestone.com/friendship-day-quotes-2026/">Friendship Day quotes</a>, <a href="https://blog.bluestone.com/humanity-quotes-2026/">humanity quotes</a>, <a href="https://blog.bluestone.com/good-luck-wishes-2026/">good luck wishes</a>, and the <a href="https://www.un.org/en/observances/living-in-peace-day">UN observance on living together in peace</a>.',
            "how_to_html": "For captions, choose a line under ten words. For family or team notes, pick a warmer quote and add one specific memory or shared goal. For community messages, keep the tone inclusive and respectful.",
            "faq_h2": "Frequently Asked Questions about Unity Quotes",
            "min_lines": 120,
        },
    )
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    checklist(prefix, rank, title, kw, False)
    print(f"Built {prefix} with {sum(len(s['lines']) for s in sections)} shareable lines")


if __name__ == "__main__":
    main()
