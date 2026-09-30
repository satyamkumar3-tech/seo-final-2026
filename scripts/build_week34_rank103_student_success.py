#!/usr/bin/env python3
"""Build Week 3-4 Rank 103 student success motivational quotes article assets."""
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
    prefix = "Week34_Rank103_StudentSuccessMotivational"
    rank = 103
    slug = "student-success-motivational-quotes-2026"
    focus_kw = "motivational bio"
    title = "Motivational Bio 2026: Student Success Quotes"
    meta_desc = "Motivational bio 2026 with student success motivational quotes, life problem quotes, WhatsApp status, result day lines, and short study captions for students."
    keywords = [
        "motivational bio",
        "student success motivational quotes",
        "life problem quotes",
        "motivational whatsapp status",
        "quotes for results day",
    ]

    hero = consolidated(rows, "The Thaloria Pendant")
    flat = consolidated(rows, "The Anya Ring")
    life = consolidated(rows, "The Ursa Hoop Earrings")

    sections = [
        sec("student_success", "Student Success Motivational Quotes", [
            "Success begins when a student decides to try one more time.",
            "Every chapter you study today becomes confidence tomorrow.",
            "A good student is not perfect. A good student keeps improving.",
            "Small daily effort can beat last-minute pressure.",
            "Your future is built in the quiet hours no one claps for.",
            "Marks matter, but discipline shapes the person behind them.",
            "A student who learns from mistakes is already moving forward.",
            "The goal is not to know everything. The goal is to keep learning.",
            "Success in studies comes from focus, patience, and honest revision.",
            "Do not compare your pace with someone else's highlight moment.",
            "Every difficult subject becomes easier when you return to it calmly.",
            "Study with purpose, rest without guilt, and begin again with courage.",
            "A student wins when fear becomes practice.",
            "Your effort today can become the story you tell with pride later.",
        ]),
        sec("motivational_bio", "Motivational Bio", [
            "Learning daily, growing quietly.",
            "Student today, achiever in progress.",
            "Focused on effort, not excuses.",
            "Building my future one page at a time.",
            "Dream big, study steady.",
            "Progress over perfection.",
            "Discipline is my quiet flex.",
            "Turning pressure into preparation.",
            "Small steps, serious goals.",
            "Learning, failing, improving, repeating.",
            "My dreams need my discipline.",
            "Success starts with showing up.",
            "Focused mind, humble heart.",
            "Preparing for the life I want.",
        ]),
        sec("short", "Short Motivational Quotes for Students", [
            "Start where you are.",
            "One page can change momentum.",
            "Effort compounds quietly.",
            "Focus beats fear.",
            "Revise, reset, rise.",
            "Keep your promise to yourself.",
            "A calm mind learns better.",
            "Progress is still progress.",
            "Do the next right thing.",
            "Confidence grows through practice.",
            "Your effort is not wasted.",
            "Study now, smile later.",
            "Discipline makes dreams practical.",
            "Begin again without drama.",
        ]),
        sec("life_problem", "Life Problem Quotes", [
            "Life problems do not end your story. They teach you how to write the next page.",
            "A problem feels smaller when you face it one step at a time.",
            "Hard days can become proof that you are stronger than your doubts.",
            "Every life problem asks for patience before it gives a lesson.",
            "Do not let one bad result decide your whole future.",
            "A difficult season can train a calm and brave mind.",
            "Problems are not punishments. Sometimes they are preparation.",
            "When life feels heavy, return to the smallest task you can complete.",
            "The answer may not arrive fast, but your courage can stay steady.",
            "A student facing problems still deserves hope, rest, and support.",
            "Life problems become lighter when you stop fighting them alone.",
            "Your current struggle is not your final identity.",
        ]),
        sec("whatsapp", "Motivational WhatsApp Status", [
            "Studying quietly, dreaming loudly.",
            "My focus is under construction.",
            "Today's effort is tomorrow's confidence.",
            "No shortcut, just steady work.",
            "I am becoming better, one day at a time.",
            "Less scrolling, more growing.",
            "My goals need my attention.",
            "Pressure is temporary, progress is personal.",
            "I choose discipline over excuses.",
            "Dreams look better with effort.",
            "Preparing for my own success story.",
            "One focused hour can change the day.",
            "Results follow honest work.",
            "Stay calm and keep studying.",
        ]),
        sec("results_day", "Quotes for Results Day", [
            "A result is feedback, not the full measure of your future.",
            "Celebrate your effort, learn from the number, and keep moving.",
            "Good results deserve gratitude, and difficult results deserve patience.",
            "One result day cannot define a student who is still growing.",
            "Marks can open doors, but character keeps you moving through them.",
            "If the result is good, stay humble. If it is hard, stay hopeful.",
            "Result day is a milestone, not the end of the road.",
            "Your worth is bigger than one sheet of marks.",
            "Success on result day feels sweeter when effort was honest.",
            "A low score can still become the beginning of a better method.",
            "Thank yourself for trying, then plan your next step.",
            "Every result teaches something if you are willing to listen.",
        ]),
        sec("exam", "Exam Motivation Quotes", [
            "Exams test preparation, but they also train courage.",
            "Read the question calmly and trust the work you have done.",
            "Revision is self-respect in student form.",
            "A focused mind can do more than a panicked one.",
            "Do not study to fear the exam. Study to understand the subject.",
            "Sleep, food, and calm thinking are part of preparation too.",
            "The best exam plan is steady practice before pressure arrives.",
            "One difficult paper does not cancel your ability.",
            "Stay honest with your revision and gentle with your nerves.",
            "Your preparation is stronger when your routine is simple.",
            "During exams, protect your peace as carefully as your notes.",
            "A student who stays calm has already won half the battle.",
        ]),
        sec("hard_work", "Hard Work Quotes for Student Success", [
            "Hard work is not loud. It often looks like showing up quietly.",
            "The student who practices daily builds confidence before the test.",
            "Discipline is doing the work even when motivation is absent.",
            "Hard work gives talent a direction.",
            "You do not need perfect conditions to begin.",
            "A notebook full of honest effort is never wasted.",
            "Student success grows from routine, not random panic.",
            "Hard work turns confusion into clarity over time.",
            "Do the boring basics. They become the strong foundation.",
            "Every revision session is a vote for your future self.",
            "Hard work feels heavy until results make it meaningful.",
            "The best students respect small habits.",
        ]),
        sec("captions", "Study Captions for Instagram", [
            "Late nights, clear goals.",
            "Focused on the next chapter.",
            "Student mode: steady and serious.",
            "Notes, dreams, and discipline.",
            "A quiet desk and a loud dream.",
            "Studying for the future me.",
            "Small progress, big purpose.",
            "Learning my way forward.",
            "Books today, confidence tomorrow.",
            "Building better habits.",
            "My study era is personal.",
            "One page closer.",
        ]),
        sec("gift_notes", "Motivational Gift Note Ideas for Students", [
            "Choose a small keepsake when you want to celebrate effort, not only marks.",
            "A pendant can feel like a quiet reminder to stay brave.",
            "A ring can mark a personal promise to keep learning.",
            "Earrings work well for a subtle everyday confidence gift.",
            "Write one line about effort before mentioning success.",
            "Use a closed book, flowers, ribbon, or a ceramic cup in photos instead of screens.",
            "Keep the note calm and encouraging.",
            "Avoid making the message sound like pressure to perform.",
            "A thoughtful gift can honour both struggle and progress.",
            "Choose jewellery that feels wearable during everyday student life.",
            "The best note says, I see your effort and I believe in you.",
            "Let the gift celebrate growth, patience, and the next chapter.",
        ]),
    ]

    prompts = {
        "rank": "Week3-4 Rank 103",
        "slug": slug,
        "primary_kw": focus_kw,
        "output_prefix": prefix,
        "caption_occasion": "Motivational bio",
        "caption_year": "2026",
        "flatlay_setting": "study-desk",
        "workflow": "Higgsfield CLI nano_banana_pro. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry. No visible screens/devices.",
        "higgsfield_jobs": {},
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/student-success-motivational-quotes-hero-2026.webp",
            "flatlay": "output/magnific_generated/student-success-motivational-quotes-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/student-success-motivational-quotes-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "motivational bio 2026 hero with The Thaloria Pendant",
            "flatlay": "motivational bio 2026 flatlay with The Anya Ring",
            "lifestyle": "motivational bio 2026 lifestyle with The Ursa Hoop Earrings",
        },
        "schema_keywords": keywords,
        "slots": {
            "hero": slot(
                hero,
                "motivational bio 2026 student success hero with The Thaloria Pendant",
                "Motivational bio 2026 mood: The Thaloria Pendant",
                [raw_image("Pendants", "The Thaloria Pendant", "1_body_portrait.png"), raw_image("Pendants", "The Thaloria Pendant", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Motivational bio 2026 student success hero",
                    scene="solo fair-skinned Indian adult woman student in a cream kurta sitting beside a clean study desk with flowers, ceramic cup, folded fabric and a small wrapped gift, calm hopeful expression, camera pulled back upper-body medium portrait with hands fully out of frame, full head and hairline visible, neck and pendant clearly visible, no paper facing camera, no screen",
                    product_name="The Thaloria Pendant",
                    product=hero,
                    body_part="neck",
                    extra_negatives="visible hands, rings, bracelet, bangle, watch, large pendant, extra necklace, background people, blackboard, whiteboard, signage, phone, laptop, tablet, planner, calendar, readable notebook, readable book, poster, board",
                ),
            ),
            "flatlay": slot(
                flat,
                "motivational bio 2026 study desk flatlay with The Anya Ring",
                "Motivational bio 2026 detail: The Anya Ring",
                [raw_image("Rings", "The Anya Ring", "0_primary.png"), raw_image("Rings", "The Anya Ring", "2_front.png"), raw_image("Rings", "The Anya Ring", "6_angle.png")],
                ["primary", "front", "angle"],
                prompt_flatlay(
                    occasion="Motivational bio 2026 student success",
                    setting="study-desk",
                    setting_prompt="clean matte wooden study desk with closed notebook turned away and blurred at edge, plain pen, ceramic cup, jasmine flowers, folded cream fabric, small wrapped gift, no visible paper, no readable text, no phone, no laptop",
                    product_name="The Anya Ring",
                    product=flat,
                ),
            ),
            "lifestyle": slot(
                life,
                "motivational bio 2026 lifestyle with The Ursa Hoop Earrings",
                "Motivational bio 2026 look: The Ursa Hoop Earrings",
                [raw_image("Earrings", "The Ursa Hoop Earrings", "1_body_portrait.png"), raw_image("Earrings", "The Ursa Hoop Earrings", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Motivational bio 2026 lifestyle",
                    scene="solo fair-skinned Indian adult woman student smiling softly while tying ribbon on a wrapped gift beside flowers and a ceramic cup, full head visible and both ears visible, cream blouse, no necklace and wrists out of frame, clean study corner with no screens and no readable books",
                    product_name="The Ursa Hoop Earrings",
                    product=life,
                    body_part="ear",
                    extra_negatives="necklace, bracelet, ring, watch, phone, laptop, tablet, planner, calendar, readable notebook, readable book, blackboard, whiteboard, poster, board",
                ),
            ),
        },
    }

    write_json(
        f"output/{prefix}_sections.json",
        {
            "meta": {"title": title, "slug": slug, "meta_desc": meta_desc, "focus_kw": focus_kw, "yoast_title": title},
            "intro": [
                "A motivational bio should be short enough for a profile and strong enough to remind you why you started. This 2026 collection covers student success motivational quotes, life problem quotes, motivational WhatsApp status, quotes for results day, study captions, and gift note ideas.",
                "TL;DR: Use a motivational bio for profiles, a student success quote for study motivation, a life problem quote for tough days, a WhatsApp status for quick sharing, and a results day quote when marks arrive.",
            ],
            "sections": sections,
            "faqs": [
                ("What is a good motivational bio for students?", "A good motivational bio for students is short, positive, and focused on effort. Choose a line about learning, discipline, progress, or future goals. Keep it natural enough for Instagram, WhatsApp, or a school profile."),
                ("What are student success motivational quotes?", "Student success motivational quotes are lines that encourage study discipline, confidence, patience, and steady improvement. They work best when they remind students to keep trying without making success feel like pressure."),
                ("Can I use life problem quotes for study motivation?", "Yes. Life problem quotes can help students handle pressure, low marks, stress, or uncertainty. Choose lines that offer courage and perspective, then pair them with a practical next step."),
                ("What should I post as a motivational WhatsApp status?", "Post a short line that feels focused and easy to relate to. Status lines like, dreams need discipline, or progress over perfection, work well because they are direct, positive, and quick to read."),
                ("What are good quotes for results day?", "Good quotes for results day should balance celebration with perspective. A result can matter, but it should not define a student's whole future. Choose lines about learning, effort, next steps, and self-belief."),
                ("Can jewellery fit a student success gift note?", "Yes. A small jewellery keepsake can mark effort, growth, or a new chapter. Keep the note encouraging rather than pressuring the student, and choose a piece that feels wearable for everyday life."),
            ],
        },
    )
    write_json(
        f"output/publish_configs/week34_rank{rank}.json",
        {
            "rank": "Week3-4 Rank 103",
            "sections_json": f"output/{prefix}_sections.json",
            "output_prefix": prefix,
            "carousel_id": "bs-cf-studentsuccess",
            "occasion_year": "Motivational bio 2026",
            "carousel_alt_prefix": "motivational bio 2026 student success gift idea",
            "gift_h2": "Student Success Gift Ideas with Motivational Notes",
            "gift_blurb": "A motivational note feels more personal when it celebrates effort and growth. These BlueStone pieces pair well with student success wishes, result day messages, and thoughtful encouragement.",
            "conclusion_html": "A motivational bio or student success quote works best when it feels honest and specific. Choose one line that matches your goal, then use it as a small reminder to keep going.",
            "schema_keywords": keywords,
            "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
            "products": [
                product(rows, "The Aagarna Pendant"),
                product(rows, "The Pervinca Charm Holder Bracelet"),
                product(rows, "The Le Sommet Ring"),
                product(rows, "The Pear Evil Eye Toggle Bangle"),
                product(rows, "The Teshvarya Pendant"),
                product(rows, "The Aleena Huggie Earrings"),
            ],
            "flatlay_insert_h2": "Life Problem Quotes",
            "lifestyle_insert_h2": "Motivational Gift Note Ideas for Students",
            "more_reads_html": 'Read more encouraging lines in <a href="https://blog.bluestone.com/exam-quotes-wishes-for-students-2026/">exam quotes for students</a>, <a href="https://blog.bluestone.com/good-luck-wishes-2026/">good luck wishes</a>, <a href="https://blog.bluestone.com/unity-quotes-2026/">unity quotes</a>, and <a href="https://www.unicef.org/education">UNICEF education resources</a>.',
            "how_to_html": "Use the profile-style lines for bios, the results day quotes after marks are announced, and the life problem quotes when a student needs perspective. Keep the tone encouraging, not pressuring.",
            "faq_h2": "Frequently Asked Questions about Motivational Bio and Student Success Quotes",
            "min_lines": 120,
        },
    )
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    checklist(prefix, rank, title, focus_kw, False)
    print(f"Built {prefix} with {sum(len(s['lines']) for s in sections)} shareable lines and supporting keywords mapped")


if __name__ == "__main__":
    main()
