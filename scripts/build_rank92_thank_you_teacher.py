#!/usr/bin/env python3
"""Build Rank 92 thank you note to teacher assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank92_ThankYouTeacher"
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
    return {
        "code": row["Design Code"],
        "name": name,
        "url": row["Link"],
        "png": f"ProductImages/seo images/{category}/{name}.png",
    }


def write_json(path: str, data: dict) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    rows = load_products()
    sections = {
        "meta": {
            "title": "Thank You Note to Teacher 2026: Messages and Wishes",
            "slug": "thank-you-note-to-teacher-2026",
            "meta_desc": "Thank you note to teacher 2026 with thanksgiving message to teacher, wishes for teacher, message for teacher, and thanks wishes for teacher for cards.",
            "focus_kw": "thank you note to teacher",
            "yoast_title": "Thank You Note to Teacher 2026",
        },
        "intro": [
            "A thank you note to teacher should sound respectful, specific, and warm. The best message does not need grand language; it simply names the care, patience, guidance, or encouragement that made a difference.",
            "TL;DR: write one clear thank you, add one specific classroom or life lesson, keep the tone sincere, and choose a short message for WhatsApp or a longer note for a card.",
        ],
        "sections": [
            {
                "key": "best",
                "h2": "Best Thank You Note to Teacher 2026",
                "lines": [
                    "Thank you for teaching with patience, kindness, and the steady belief that every student can improve.",
                    "Your guidance made lessons easier to understand and confidence easier to find.",
                    "Thank you for noticing effort, not only marks, and for encouraging progress in small steps.",
                    "A good teacher explains the subject; a great teacher helps students believe they can learn it.",
                    "Thank you for being the kind of teacher whose words stay useful beyond the classroom.",
                    "Your support has made a real difference, and I am grateful for your time and care.",
                    "Thank you for turning difficult lessons into moments of understanding.",
                    "You taught with discipline, warmth, and a rare ability to make students feel seen.",
                    "I will always remember the way you encouraged me when I needed it most.",
                    "Thank you for being a teacher who made learning feel possible.",
                ],
            },
            {
                "key": "short",
                "h2": "Short Thank You Messages for Teacher",
                "lines": [
                    "Thank you, teacher, for your patience and guidance.",
                    "Your lessons will stay with me always.",
                    "Grateful for your support and kindness.",
                    "Thank you for helping me grow.",
                    "You made learning easier and brighter.",
                    "Respect and gratitude for everything you do.",
                    "Thank you for believing in your students.",
                    "Your guidance means more than words can say.",
                    "A heartfelt thank you to a wonderful teacher.",
                    "You made a difference, and I am grateful.",
                ],
            },
            {
                "key": "thanksgiving",
                "h2": "Thanksgiving Message to Teacher",
                "lines": [
                    "This Thanksgiving, I am grateful for a teacher who gives time, care, and encouragement so generously.",
                    "Thank you for being one of the people who made learning feel hopeful this year.",
                    "Your patience in difficult moments is something students remember with respect.",
                    "I am thankful for every lesson, correction, reminder, and word of encouragement.",
                    "This season is a good time to say that your effort does not go unnoticed.",
                    "Thank you for showing that teaching is not only a job, but a daily act of care.",
                    "I am grateful for the way you guide students without making them feel small.",
                    "Your classroom has been a place of discipline, learning, and quiet confidence.",
                    "Thank you for giving your students reasons to keep trying.",
                    "May this Thanksgiving bring you the appreciation you give others all year.",
                ],
            },
            {
                "key": "wishes",
                "h2": "Wishes for Teacher",
                "lines": [
                    "Wishing you respect, happiness, and the satisfaction of knowing how many lives you shape.",
                    "May your days be filled with cooperative students, peaceful moments, and well-deserved appreciation.",
                    "Wishing you health, patience, and joy in every classroom you enter.",
                    "May your teaching journey continue to inspire students for years to come.",
                    "Wishing you the same kindness and encouragement you give your students.",
                    "May your effort be recognised and your heart stay proud of the work you do.",
                    "Wishing you a year of meaningful lessons and beautiful student memories.",
                    "May every thank you remind you that your work truly matters.",
                    "Wishing you calm mornings, bright classrooms, and students who value your guidance.",
                    "May you always receive the respect your dedication deserves.",
                ],
            },
            {
                "key": "message",
                "h2": "Message for Teacher",
                "lines": [
                    "Dear teacher, thank you for explaining patiently until confusion became clarity.",
                    "You helped me understand not only the lesson, but also the value of effort.",
                    "Your encouragement came at moments when giving up felt easier.",
                    "Thank you for correcting mistakes without taking away confidence.",
                    "You made the classroom feel structured, safe, and full of possibility.",
                    "I appreciate the way you gave attention to every student, not only the loudest ones.",
                    "Your guidance helped me become more disciplined and more hopeful.",
                    "Thank you for teaching with both knowledge and heart.",
                    "The lessons you gave will continue to help long after exams are over.",
                    "I am grateful to have learned from you.",
                ],
            },
            {
                "key": "thanks_wishes",
                "h2": "Thanks Wishes for Teacher",
                "lines": [
                    "Thank you and best wishes to a teacher who brings sincerity into every lesson.",
                    "May your kindness return to you through the success and gratitude of your students.",
                    "Thank you for your guidance, and may your teaching journey stay rewarding.",
                    "Wishing you happiness for every life you have touched with your lessons.",
                    "Thank you for your patience, and may you always feel proud of your work.",
                    "Best wishes to a teacher whose effort deserves respect every day.",
                    "May your students remember your lessons with affection and gratitude.",
                    "Thank you for being generous with your time, wisdom, and encouragement.",
                    "Wishing you peaceful days and many reasons to smile.",
                    "Thank you for everything, teacher. Your work truly matters.",
                ],
            },
            {
                "key": "from_student",
                "h2": "Thank You Note to Teacher from Student",
                "lines": [
                    "Dear teacher, thank you for helping me learn with patience and confidence.",
                    "I appreciate the way you explained things clearly and never made questions feel foolish.",
                    "Your encouragement helped me try again when I was unsure of myself.",
                    "Thank you for teaching me that improvement matters as much as results.",
                    "Your lessons have helped me become more focused and responsible.",
                    "I will remember your kindness and discipline with respect.",
                    "Thank you for giving your time even when the classroom was busy.",
                    "You made a difference in my learning, and I am grateful.",
                    "Your guidance is something I will carry forward.",
                    "Thank you for being a teacher I can remember with pride.",
                ],
            },
            {
                "key": "from_parent",
                "h2": "Thank You Note to Teacher from Parents",
                "lines": [
                    "Thank you for guiding our child with patience, structure, and genuine care.",
                    "We appreciate the way you notice progress and help students build confidence.",
                    "Your effort has made a positive difference in our child's learning and attitude.",
                    "Thank you for being supportive, disciplined, and approachable throughout the year.",
                    "As parents, we are grateful for the time and attention you give your students.",
                    "Your teaching has helped our child feel more capable and motivated.",
                    "Thank you for creating a classroom where learning feels safe and meaningful.",
                    "We respect the dedication you bring to your work every day.",
                    "Your guidance is a gift to students and families alike.",
                    "Thank you for being an important part of our child's growth.",
                ],
            },
            {
                "key": "funny",
                "h2": "Funny Thank You Messages for Teacher",
                "lines": [
                    "Thank you for explaining the same thing many times and still pretending it was fine.",
                    "You deserve a medal for surviving our questions, excuses, and handwriting.",
                    "Thank you for teaching us patience by using yours every single day.",
                    "You made tough lessons less scary and homework slightly less dramatic.",
                    "Thanks for knowing exactly when we were confused, even when we nodded confidently.",
                    "You taught us formulas, facts, and the art of listening before asking again.",
                    "Thank you for being strict enough to help and kind enough to forgive.",
                    "Your class made learning fun, even when tests tried to ruin the mood.",
                    "Thanks for being the teacher who could spot unfinished homework from a distance.",
                    "We are grateful for your lessons and your heroic tolerance.",
                ],
            },
            {
                "key": "card",
                "h2": "Thank You Teacher Card Messages",
                "lines": [
                    "Thank you for teaching with heart and helping students grow with confidence.",
                    "Your guidance has been a gift, and your lessons will be remembered.",
                    "With respect and gratitude, thank you for everything you do.",
                    "A teacher like you makes learning feel meaningful and possible.",
                    "Thank you for your patience, kindness, and dedication.",
                    "Your encouragement has made a lasting difference.",
                    "Grateful for your time, wisdom, and belief in your students.",
                    "Thank you for being a wonderful teacher and guide.",
                    "Your lessons reached beyond books, and I am thankful.",
                    "Wishing you happiness and appreciation for all your hard work.",
                ],
            },
            {
                "key": "gift",
                "h2": "Teacher Thank You Gift Ideas",
                "lines": [
                    "A thank you note should carry the emotion, while a small keepsake can make the moment memorable.",
                    "Choose a gift that feels respectful, simple, and useful rather than overly personal.",
                    "A pendant can feel graceful when the teacher enjoys delicate everyday jewellery.",
                    "A bangle or bracelet works well as a polished keepsake for a formal thank you.",
                    "Hoop earrings suit a teacher who likes practical and elegant accessories.",
                    "Avoid mentioning price in the card or message.",
                    "Keep the note focused on gratitude, not the gift itself.",
                    "A blank card with one sincere line often feels more meaningful than a long formal paragraph.",
                    "If gifting from a class, make the message collective and respectful.",
                    "The best teacher gift says, your effort was noticed.",
                ],
            },
        ],
        "section_leads": {
            "Best Thank You Note to Teacher 2026": "Use these all-rounder notes when you want a respectful message that works in cards, chats, and speeches.",
            "Short Thank You Messages for Teacher": "Short messages are ideal for WhatsApp, SMS, and quick handwritten cards.",
            "Thanksgiving Message to Teacher": "These Thanksgiving-style messages focus on gratitude, patience, and appreciation.",
            "Wishes for Teacher": "Use these wishes when the note should bless the teacher's work and year ahead.",
            "Message for Teacher": "These messages sound personal without becoming too casual.",
            "Thanks Wishes for Teacher": "Use these when you want gratitude and good wishes in the same line.",
            "Thank You Note to Teacher from Student": "These lines are written from a student's side and keep the tone sincere.",
            "Thank You Note to Teacher from Parents": "These parent messages are respectful, warm, and school-appropriate.",
            "Funny Thank You Messages for Teacher": "Funny messages work best when the teacher already enjoys light humour.",
            "Thank You Teacher Card Messages": "These card messages are polished enough for handwritten notes.",
            "Teacher Thank You Gift Ideas": "A gift is optional; the note should still carry the real thanks.",
        },
        "faqs": [
            ["How do I write a thank you note to teacher?", "Start with thank you, mention one specific lesson or quality, and close with respect. Keep it sincere, simple, and free from over-formal language."],
            ["What is a short thank you message for teacher?", "A short message can be: Thank you, teacher, for your patience, guidance, and belief in your students."],
            ["What can parents write in a thank you note to teacher?", "Parents can thank the teacher for patience, structure, encouragement, and the positive difference made in their child's learning."],
            ["What is a good Thanksgiving message to teacher?", "A good Thanksgiving message can be: This Thanksgiving, I am grateful for your patience, guidance, and the confidence you give your students."],
            ["Can I write a funny thank you message for teacher?", "Yes, if the humour is respectful and familiar. Avoid jokes about marks, salary, age, appearance, or classroom discipline."],
            ["Is jewellery a good thank you gift for teacher?", "Jewellery can work when it is simple, respectful, and appropriate. Pair it with a sincere card and avoid mentioning price."],
        ],
    }

    config = {
        "rank": 92,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-thankyouteacher",
        "occasion_year": "Thank You Note to Teacher 2026",
        "carousel_alt_prefix": "thank you note to teacher 2026 gift idea",
        "gift_h2": "Thank You Teacher Jewellery Gift Ideas",
        "gift_blurb": "If the note carries the gratitude, a small keepsake can make the thank you feel complete. These six approved BlueStone designs suit respectful teacher gifting without mentioning prices.",
        "conclusion_html": "A thank you note to teacher works best when it is specific, respectful, and honest. Pick one message, add a real classroom memory or lesson, and let the teacher know their effort was noticed.",
        "schema_keywords": [
            "thank you note to teacher",
            "thanksgiving message to teacher",
            "wishes for teacher",
            "message for teacher",
            "thanks wishes for teacher",
            "thank you messages for teacher",
        ],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(rows, "The Sarvanya Pendant", "Pendants"),
            product(rows, "The Tarentella Oval Bangle", "Bangles"),
            product(rows, "The Skein Hoop Earrings", "Earrings"),
            product(rows, "The Haily Ring", "Rings"),
            product(rows, "The Gigi Ring", "Rings"),
            product(rows, "The Shining Star Bracelet", "Bracelet"),
        ],
        "flatlay_insert_h2": "Thanksgiving Message to Teacher",
        "lifestyle_insert_h2": "Teacher Thank You Gift Ideas",
        "more_reads_html": "For more appreciation and occasion lines, see <a href=\"https://blog.bluestone.com/advance-happy-birthday-wishes-2026/\">advance birthday wishes 2026</a>, <a href=\"https://blog.bluestone.com/mother-daughter-quotes-2026/\">mother daughter quotes 2026</a>, <a href=\"https://blog.bluestone.com/humanity-quotes-2026/\">humanity quotes 2026</a>, and <a href=\"https://blog.bluestone.com/speedy-recovery-message-2026/\">speedy recovery message 2026</a>.",
        "how_to_html": "For a teacher, keep the message respectful and concrete. Mention patience, guidance, one lesson, or one habit the teacher helped build. Avoid making the note too casual unless the teacher knows you well.",
        "faq_h2": "Frequently Asked Questions about Thank You Notes to Teacher",
        "min_lines": 100,
        "section_leads": sections["section_leads"],
    }

    prompts = {
        "rank": 92,
        "slug": "thank-you-note-to-teacher-2026",
        "output_prefix": PREFIX,
        "occasion": "Thank You Note to Teacher 2026",
        "primary_kw": "thank you note to teacher",
        "caption_occasion": "Thank you note to teacher",
        "caption_year": "2026",
        "flatlay_setting": "study-desk",
        "workflow": "Higgsfield MCP nano_banana_pro. Campaign hybrid with mandatory body_image scale line for people shots. Do not generate until balance succeeds. Max 2 concurrent generations total across active blogs. If queue/generation error occurs, wait 40-50 seconds before retry.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/thank-you-note-to-teacher-hero-2026.webp",
            "flatlay": "output/magnific_generated/thank-you-note-to-teacher-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/thank-you-note-to-teacher-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "thank you note to teacher 2026 hero The Sarvanya Pendant",
            "flatlay": "thank you note to teacher 2026 flatlay The Tarentella Oval Bangle",
            "lifestyle": "thank you note to teacher 2026 lifestyle The Skein Hoop Earrings",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                "code": "BISW1080P132",
                "name": "The Sarvanya Pendant",
                "gender": "Female",
                "height_mm": 33.35,
                "width_mm": 23.79,
                "size_prompt_note": "pendant product height 33.35 mm and width 23.79 mm; product dimensions, not face size; copy worn neck scale from body_image",
                "alt": "thank you note to teacher 2026 hero with The Sarvanya Pendant",
                "caption": "Thank you note to teacher 2026 vibe: The Sarvanya Pendant",
                "product": {"code": "BISW1080P132", "name": "The Sarvanya Pendant", "pdp": "https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html"},
                "cdn": [
                    "https://kinclimg6.bluestone.com/giproduct/BISW1080P132_WAA18DIG4LNBTXXXX_ABCD00-BP-PICS-00000-1024-104460.png",
                    "https://kinclimg9.bluestone.com/giproduct/BISW1080P132_WAA18DIG4LNBTXXXX_ABCD00-PICS-00002-1024-104460.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Sarvanya Pendant/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Sarvanya Pendant/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} Thank you note to teacher 2026 hero, solo fair-skinned Indian adult woman teacher sitting at a neat study desk in a bright classroom corner, smiling softly while reading a blank cream thank-you card beside a closed notebook, plain pen, and small wrapped gift. Full head, full face, both eyes, complete smile, neck, pendant, hands, blank card, gift, and upper body visible with safe margins. Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, soft daylight, realistic shadows, 16:9.\n\nThe woman physically wears The Sarvanya Pendant from @img1 body_image and @img2 design on a fine chain at upper chest. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: pendant product height_mm=33.35 and width_mm=23.79. These are real product dimensions, NOT face-size instructions. Keep pendant size on the neck like @img1 body_image worn neck scale: subtle pendant size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the white gold and blue-toned pendant exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery in the image. Bare wrists, bare fingers, no watches, no bracelets, no rings, no earrings, no extra necklaces. Jewellery touches skin or fabric with soft contact shadow, never a floating cutout. The card and notebook must be blank with no letters, no handwriting, no symbols, no numbers.\n\nAvoid: cropped face, cropped eyes, cropped forehead, cropped head, readable text, handwriting, printed letters, numbers, symbols on card or notebook, man wearer, child, minor, second person, students in frame, extra hands, extra necklaces, rings, watches, earrings, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow.",
            },
            "flatlay": {
                "code": "BENS0325O09",
                "name": "The Tarentella Oval Bangle",
                "gender": "Female",
                "height_mm": 60.62,
                "width_mm": 12.9,
                "size_prompt_note": "bangle inner/face height 60.62 mm and width 12.9 mm; product dimensions, not face size",
                "alt": "thank you note to teacher 2026 flatlay with The Tarentella Oval Bangle",
                "caption": "Thank you note to teacher 2026 keepsake: The Tarentella Oval Bangle",
                "product": {"code": "BENS0325O09", "name": "The Tarentella Oval Bangle", "pdp": "https://www.bluestone.com/bangles/the-tarentella-oval-bangle~31547.html"},
                "cdn": [
                    "https://kinclimg7.bluestone.com/giproduct/BENS0325O09_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-72949.png",
                    "https://kinclimg1.bluestone.com/giproduct/BENS0325O09_YAA18DIG6XXXXXXXX_ABCD00-PICS-00001-1024-72949.png",
                    "https://kinclimg4.bluestone.com/giproduct/BENS0325O09_YAA18DIG6XXXXXXXX_ABCD00-PICS-00002-1024-72949.png",
                ],
                "local_reference_images": [
                    "ProductImages/seo images/Bangles/The Tarentella Oval Bangle.png"
                ],
                "ref_roles": ["primary", "angle", "angle"],
                "prompt": f"Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\nThank you note to teacher 2026 top-down flatlay. Flatlay setting ID: study-desk. Surface and props: dark wood study desk, closed notebook with no title, plain pen, soft blotter, blank cream thank-you card, small matte gift box. No readable text, no letters, no numbers, no symbols on any prop.\n\nThe identical Tarentella Oval Bangle from @img1, @img2 and @img3 rests naturally on the study desk at true PDP scale. Product dimensions from PDP: bangle product height_mm=60.62 and width_mm=12.9. These are product dimensions, NOT face-size instructions. Do not enlarge for visibility. Full oval bangle visible, polished yellow gold and diamond detail, 100 percent identical design, zero distortion, HD metal and stone detail.\n\nProps stay secondary and quiet. No people, no hands, no readable text, no brand marks. Jewellery is the clear subject but still true to real size.\n\nAvoid: hands, people, floating overlays, cutouts, incorrect bangle design, distorted metal, readable text, logos, price tags, brand marks on props, blown whites, HDR glow, illustration, CGI.",
            },
            "lifestyle": {
                "code": "BINK0363H03",
                "name": "The Skein Hoop Earrings",
                "gender": "Female",
                "height_mm": 17.95,
                "width_mm": 6.16,
                "size_prompt_note": "earring product height 17.95 mm and width 6.16 mm; product dimensions, not face size; copy worn ear scale from body_image",
                "alt": "thank you note to teacher 2026 lifestyle with The Skein Hoop Earrings",
                "caption": "Thank you note to teacher 2026 vibe: The Skein Hoop Earrings",
                "product": {"code": "BINK0363H03", "name": "The Skein Hoop Earrings", "pdp": "https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html"},
                "cdn": [
                    "https://kinclimg1.bluestone.com/giproduct/BINK0363H03_YAA18DIG6XXXXXXXX_ABCD00-BP-PICS-00000-1024-78023.png",
                    "https://kinclimg1.bluestone.com/giproduct/BINK0363H03_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-78023.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Earrings/The Skein Hoop Earrings/1_body_portrait.png",
                    "ProductImages/raw/Earrings/The Skein Hoop Earrings/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} Thank you note to teacher 2026 lifestyle, solo fair-skinned Indian adult woman teacher at a bright desk writing on a blank cream card with a plain pen, closed notebook and tea cup nearby. Full face, both ears, both eyes, complete smile, writing hand, blank card, and upper body visible with safe margins. Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, soft daylight, realistic shadows, 16:9.\n\nThe woman physically wears The Skein Hoop Earrings from @img1 body_image and @img2 design on her ears. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: earring product height_mm=17.95 and width_mm=6.16. These are real product dimensions, NOT face-size instructions. Keep earrings size on the ears like @img1 body_image worn ear scale: subtle earring size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the yellow gold hoop earrings exactly, 100 percent identical to refs, zero distortion, HD metal detail. These earrings are the single and only jewellery in the image. Bare neck, bare wrists, bare fingers, no watch, no bracelet, no rings, no necklace, no other earrings. Jewellery touches ears with soft contact shadow, never a floating cutout. The card and notebook must be blank with no letters, no handwriting, no symbols, no numbers.\n\nAvoid: background people, students, man wearer, child, minor, second person, extra hands, silhouettes, readable text, handwriting, printed letters, numbers, symbols on card or notebook, extra necklaces, rings, watches, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, cropped face, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow.",
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 92

Article: Thank You Note to Teacher 2026
Status: Draft assets prepared
Date: 2026-07-24

## A. Intent and Brief
- [x] Primary keyword: thank you note to teacher
- [x] Supporting keywords mapped to H2s and FAQs
- [x] Sheet New treated as New
- [x] Fresh slug: thank-you-note-to-teacher-2026
- [x] 2026 year lock used

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""

    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json("output/publish_configs/rank92.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
