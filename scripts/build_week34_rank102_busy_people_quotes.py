#!/usr/bin/env python3
"""Build Week 3-4 Rank 102 busy people quotes article assets."""
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
    prefix = "Week34_Rank102_BusyPeopleQuotes"
    rank = 102
    slug = "busy-people-quotes-2026"
    kw = "busy people quotes"
    secondary_kw = "busy person quotes"
    title = "Busy People Quotes 2026: Short Lines for Life"
    meta_desc = "Busy people quotes 2026 with busy person quotes, short captions, funny lines, friendship notes, work-life thoughts, and messages for people who care today."
    keywords = [kw, secondary_kw, "busy life quotes", "busy friends quotes", "work life quotes"]

    hero = consolidated(rows, "The Protecteur Evil Eye Pendant")
    flat = consolidated(rows, "The Muricelle Bangle")
    life = consolidated(rows, "The Skein Hoop Earrings")

    sections = [
        sec("main", "Busy People Quotes", [
            "Busy people still make time for what their heart refuses to forget.",
            "A full calendar does not always mean a full heart.",
            "Some people are busy building a life, not avoiding the people they love.",
            "Being busy is easier to understand when effort still comes with care.",
            "A busy life needs small pauses where the soul can breathe.",
            "The people who care will find one honest minute, even on a crowded day.",
            "Busy people teach us that time is precious, but attention is priceless.",
            "Do not measure love only by availability. Measure it by intention too.",
            "A busy person may be quiet, but that does not always mean they are distant.",
            "Real priorities show up in the way people return after the rush.",
            "Busy days become softer when someone checks in with kindness.",
            "A thoughtful message can travel through the busiest schedule.",
            "People are not machines. Even ambition needs rest and warmth.",
            "The best busy people protect both their goals and their relationships.",
        ]),
        sec("secondary", "Busy Person Quotes", [
            "A busy person is not always unavailable. Sometimes they are simply carrying too much.",
            "The right busy person will not leave you guessing forever.",
            "A busy person who cares will return with honesty, not excuses.",
            "Respect a busy person, but do not disappear from your own needs.",
            "A busy person needs patience, not pressure, when the bond is real.",
            "If a busy person values you, their effort will still have a shape.",
            "A good busy person makes space for people, even if the space is small.",
            "Busy person quotes remind us that time is limited, but care can still be clear.",
            "A busy person may miss calls, but they should not miss respect.",
            "The busiest person still deserves a peaceful message.",
            "A busy person with a kind heart will appreciate simple understanding.",
            "The right bond survives busy seasons because both sides keep choosing it.",
            "A busy person can be loved, but they should not be worshipped for absence.",
            "Even a busy person can offer one sincere line when it matters.",
        ]),
        sec("short", "Short Busy People Quotes", [
            "Busy, but still human.",
            "Time is tight, care is clear.",
            "Busy days need soft hearts.",
            "A small message can matter.",
            "Goals need rest too.",
            "Busy is not heartless.",
            "Make time for meaning.",
            "Care finds a window.",
            "A pause can save peace.",
            "Ambition needs balance.",
            "Do less, feel more.",
            "Busy seasons pass.",
            "Kindness fits any schedule.",
            "Priorities speak quietly.",
        ]),
        sec("life", "Busy Life Quotes", [
            "A busy life can look successful and still need tenderness.",
            "Do not let a full day turn into an empty connection.",
            "Life moves fast, but the heart still needs slow moments.",
            "The art of a busy life is knowing when to stop proving and start living.",
            "A full schedule should not steal every peaceful breath.",
            "Busy life becomes beautiful when purpose and rest learn to share space.",
            "You can chase dreams without losing yourself.",
            "A busy life needs boundaries, not only discipline.",
            "Some of the best memories are made in the pauses between responsibilities.",
            "When life gets crowded, protect the people who make it feel calm.",
            "Success feels better when it does not cost every relationship.",
            "Busy days should end with gratitude, not only exhaustion.",
        ]),
        sec("work", "Busy People Quotes for Work", [
            "A hardworking person deserves appreciation, not only more work.",
            "Busy teams need clear goals and kinder communication.",
            "Work can fill the day, but respect should fill the room.",
            "The best professionals know when effort needs recovery.",
            "A busy office becomes lighter when people help without drama.",
            "Productivity is not the same as peace.",
            "A strong work ethic should not erase personal wellbeing.",
            "Busy people at work need trust, clarity, and realistic timelines.",
            "The best work culture values people, not only output.",
            "Deadlines are easier when teamwork is real.",
            "A busy person can still be generous with credit.",
            "The smartest workers protect focus and rest together.",
        ]),
        sec("friends", "Busy Friends Quotes", [
            "Busy friends may reply late, but real friends do not forget the bond.",
            "A friendship can survive distance when both hearts stay kind.",
            "Good friends understand busy seasons without turning love into a test.",
            "A late reply is easier to forgive when effort remains honest.",
            "Busy friends need gentle check-ins, not guilt every time.",
            "Friendship grows when people give each other room to breathe.",
            "The best friends return with warmth after the rush.",
            "Busy days cannot break a friendship built on trust.",
            "A simple thinking of you can keep a friendship alive.",
            "Real friendship is patient, but it is not one-sided forever.",
            "Busy friends still need celebrations, laughter, and care.",
            "A good friend understands your schedule and your silence.",
        ]),
        sec("relationship", "Busy Person Quotes for Relationships", [
            "Love can understand busyness, but it still needs reassurance.",
            "A busy partner should not make you feel permanently invisible.",
            "Healthy love respects time, work, rest, and communication.",
            "The right person will not use busyness as a wall forever.",
            "Even in a busy season, a relationship needs small signs of care.",
            "A message sent with honesty can calm many doubts.",
            "Busy love survives when both people explain instead of assuming.",
            "Patience is beautiful when effort is mutual.",
            "A person can be busy and still emotionally present.",
            "Do not confuse constant absence with ambition.",
            "The right relationship makes room for dreams and tenderness.",
            "Love should feel steady, even when schedules are not.",
        ]),
        sec("funny", "Funny Busy People Quotes", [
            "I am not ignoring life. I am buffering.",
            "My calendar has more confidence than I do.",
            "Busy is my personality until Sunday evening.",
            "If rest were a meeting, I would reschedule it twice.",
            "I have plans with my to-do list and it keeps arguing.",
            "Currently busy pretending I have everything under control.",
            "My schedule needs a vacation before I do.",
            "I am booked, blessed, and slightly confused.",
            "Busy people run on reminders and hope.",
            "I need a reminder to check my reminders.",
            "If multitasking were an art, my coffee would be the artist.",
            "My free time is in witness protection.",
        ]),
        sec("captions", "Busy People Captions", [
            "Busy days, steady heart.",
            "Building quietly, breathing slowly.",
            "A little tired, still trying.",
            "Booked but grateful.",
            "Goals today, peace tonight.",
            "Making time for what matters.",
            "Busy season, soft spirit.",
            "Doing my best with a full plate.",
            "Less noise, more focus.",
            "A pause between responsibilities.",
            "Still showing up.",
            "Busy, but choosing kindness.",
        ]),
        sec("messages", "Messages for Busy People", [
            "I know life is full right now, but I hope you are taking care of yourself too.",
            "Just a small reminder that you are doing enough and you deserve rest.",
            "Your hard work matters, but your peace matters too.",
            "I hope today gives you one quiet moment to breathe.",
            "You do not have to reply quickly. I just wanted to send care your way.",
            "Even busy people need soft reminders that they are loved.",
            "Take your time, but do not forget yourself in the rush.",
            "I see your effort and I hope it leads to something beautiful.",
            "May your busy day end with calm and comfort.",
            "You are allowed to pause without feeling guilty.",
            "Sending you patience, strength, and a little peace for today.",
            "You are busy, but you are also human. Be kind to yourself.",
        ]),
        sec("gift_notes", "Busy Person Gift Note Ideas", [
            "Choose a small keepsake when you want to say, I see your effort.",
            "A pendant works well for someone who likes quiet everyday meaning.",
            "A bangle can feel like a reminder to pause and breathe.",
            "Earrings make a gentle gift for someone who prefers subtle style.",
            "Write one line about care before you mention the busy season.",
            "Use a ceramic cup, flowers, ribbon, or folded fabric for photos instead of screens.",
            "Avoid making the gift note sound like pressure to reply.",
            "Keep the message short for someone with a packed schedule.",
            "A thoughtful gift should feel calming, not demanding.",
            "Choose jewellery that works with everyday routines.",
            "The best note tells a busy person they are valued, not just needed.",
            "Let the gift carry warmth and the message carry understanding.",
        ]),
    ]

    prompts = {
        "rank": "Week3-4 Rank 102",
        "slug": slug,
        "primary_kw": kw,
        "output_prefix": prefix,
        "caption_occasion": "Busy people quotes",
        "caption_year": "2026",
        "flatlay_setting": "cafe-tray",
        "workflow": "Higgsfield CLI nano_banana_pro. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry. No visible screens/devices.",
        "higgsfield_jobs": {},
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/busy-people-quotes-hero-2026.webp",
            "flatlay": "output/magnific_generated/busy-people-quotes-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/busy-people-quotes-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "busy people quotes 2026 hero with The Protecteur Evil Eye Pendant",
            "flatlay": "busy people quotes 2026 flatlay with The Muricelle Bangle",
            "lifestyle": "busy people quotes 2026 lifestyle with The Skein Hoop Earrings",
        },
        "schema_keywords": keywords,
        "slots": {
            "hero": slot(
                hero,
                "busy people quotes 2026 hero with The Protecteur Evil Eye Pendant",
                "Busy people quotes 2026 mood: The Protecteur Evil Eye Pendant",
                [raw_image("Pendants", "The Protecteur Evil Eye Pendant", "1_body_portrait.png"), raw_image("Pendants", "The Protecteur Evil Eye Pendant", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Busy people quotes 2026 hero",
                    scene="solo fair-skinned Indian adult woman in a cream kurta pausing beside a bright home windowsill with flowers, ceramic cup, brass bowl and a small wrapped gift before a busy day, calm reflective mood, clean plain background with no other people, no wall boards, no menu boards, no signage, camera pulled back upper-body medium portrait with hands fully out of frame, full head and hairline visible, neck and pendant clearly visible, no paper facing camera",
                    product_name="The Protecteur Evil Eye Pendant",
                    product=hero,
                    body_part="neck",
                    extra_negatives="visible hands, rings, bracelet, bangle, watch, large pendant, extra necklace, background people, cafe menu board, blackboard, signage, phone, laptop, planner, calendar, readable note, poster, board",
                ),
            ),
            "flatlay": slot(
                flat,
                "busy people quotes 2026 flatlay with The Muricelle Bangle",
                "Busy people quotes 2026 detail: The Muricelle Bangle",
                [raw_image("Bangles", "The Muricelle Bangle", "0_primary.png"), raw_image("Bangles", "The Muricelle Bangle", "2_front.png"), raw_image("Bangles", "The Muricelle Bangle", "4_close_up.png")],
                ["primary", "front", "close_up"],
                prompt_flatlay(
                    occasion="Busy people quotes 2026",
                    setting="cafe-tray",
                    setting_prompt="matte ceramic tray on a warm cafe table with plain espresso cup and saucer, folded cream napkin, jasmine flowers, silk ribbon, small wrapped gift, no paper, no card, no text",
                    product_name="The Muricelle Bangle",
                    product=flat,
                ),
            ),
            "lifestyle": slot(
                life,
                "busy people quotes 2026 lifestyle with The Skein Hoop Earrings",
                "Busy people quotes 2026 look: The Skein Hoop Earrings",
                [raw_image("Earrings", "The Skein Hoop Earrings", "1_body_portrait.png"), raw_image("Earrings", "The Skein Hoop Earrings", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Busy people quotes 2026 lifestyle",
                    scene="solo fair-skinned Indian adult woman smiling softly while tying ribbon on a wrapped gift beside a ceramic cup and flowers, full head visible and both ears visible, cream blouse, no necklace and wrists out of frame, peaceful pause in a busy day",
                    product_name="The Skein Hoop Earrings",
                    product=life,
                    body_part="ear",
                    extra_negatives="necklace, bracelet, ring, watch, phone, laptop, planner, calendar, readable note, poster, board",
                ),
            ),
        },
    }

    write_json(
        f"output/{prefix}_sections.json",
        {
            "meta": {"title": title, "slug": slug, "meta_desc": meta_desc, "focus_kw": kw, "yoast_title": title},
            "intro": [
                "Busy people quotes help when you want to understand someone with a packed life, encourage a hardworking friend, or remind yourself that rest matters too. This 2026 collection includes busy person quotes, short captions, funny lines, work-life thoughts, friendship notes, relationship messages, and gift note ideas.",
                "TL;DR: Use busy people quotes when the message is about time, effort, patience, and care. Use busy person quotes when you are speaking about one specific person who is hardworking, unavailable, or trying to balance many responsibilities.",
            ],
            "sections": sections,
            "faqs": [
                ("What are the best busy people quotes?", "The best busy people quotes are honest without sounding harsh. Choose lines that recognise effort, limited time, and the need for rest. A good quote should feel understanding, but it should not excuse neglect or one-sided relationships."),
                ("What are good busy person quotes?", "Good busy person quotes speak to one person who has a full schedule or a heavy season. Use them when you want to show patience, encourage balance, or gently remind someone that care still matters even when life is crowded."),
                ("Can I use busy people quotes as captions?", "Yes. Short busy people quotes work well as captions for work days, travel days, cafe breaks, or reflective photos. Pick one line that sounds calm and human, not overly dramatic, so the caption feels relatable."),
                ("How do I message a busy friend?", "Send a short note that does not demand an instant reply. A line like, take your time, I just wanted to send care, respects their schedule while keeping the friendship warm and open."),
                ("Are busy people always ignoring you?", "No. Some busy people are genuinely overloaded, while others use busyness as distance. Look for patterns. A caring person may reply late, but they usually return with clarity, warmth, and some form of effort."),
                ("Can jewellery fit a busy person message?", "Yes. A subtle jewellery keepsake can pair well with a note about effort, balance, or appreciation. Keep the message gentle and avoid making the gift feel like pressure to respond or perform."),
            ],
        },
    )
    write_json(
        f"output/publish_configs/week34_rank{rank}.json",
        {
            "rank": "Week3-4 Rank 102",
            "sections_json": f"output/{prefix}_sections.json",
            "output_prefix": prefix,
            "carousel_id": "bs-cf-busypeople",
            "occasion_year": "Busy people quotes 2026",
            "carousel_alt_prefix": "busy people quotes 2026 gift idea",
            "gift_h2": "Gift Ideas for Busy People with Thoughtful Notes",
            "gift_blurb": "A thoughtful gift for a busy person should feel easy, warm, and undemanding. These BlueStone pieces pair well with short notes about effort, appreciation, balance, and care.",
            "conclusion_html": "Busy people quotes work best when they balance empathy with honesty. Pick the line that fits your situation, then add one personal detail so it feels real.",
            "schema_keywords": keywords,
            "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
            "products": [
                product(rows, "The Tarentella Oval Bangle"),
                product(rows, "The Muricelle Bangle"),
                product(rows, "The Haily Ring"),
                product(rows, "The Vicky Hoop Earrings"),
                product(rows, "The Shining Star Bracelet"),
                product(rows, "The Malibu Ring"),
            ],
            "flatlay_insert_h2": "Busy Person Quotes",
            "lifestyle_insert_h2": "Busy Person Gift Note Ideas",
            "more_reads_html": 'Read more thoughtful lines in <a href="https://blog.bluestone.com/unity-quotes-2026/">unity quotes</a>, <a href="https://blog.bluestone.com/good-luck-wishes-2026/">good luck wishes</a>, <a href="https://blog.bluestone.com/friendship-day-quotes-2026/">Friendship Day quotes</a>, and <a href="https://www.who.int/news-room/questions-and-answers/item/stress">WHO guidance on stress</a>.',
            "how_to_html": "Choose a short quote for captions, a warmer line for a busy friend, and a direct busy person quote when one specific person is on your mind. Keep the tone understanding but honest.",
            "faq_h2": "Frequently Asked Questions about Busy People Quotes",
            "min_lines": 120,
        },
    )
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    checklist(prefix, rank, title, kw, False)
    print(f"Built {prefix} with {sum(len(s['lines']) for s in sections)} shareable lines and secondary keyword {secondary_kw!r}")


if __name__ == "__main__":
    main()
