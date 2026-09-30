#!/usr/bin/env python3
"""Build Rank 92 thank you note to teacher assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank92_TeacherThankYou"
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
            "title": "Thank You Note to Teacher 2026: Messages & Wishes",
            "slug": "thank-you-note-to-teacher-2026",
            "meta_desc": "Thank you note to teacher 2026 with thanksgiving message to teacher, wishes for teacher, message for teacher, and thanks wishes for teacher examples today.",
            "focus_kw": "thank you note to teacher",
            "yoast_title": "Thank You Note to Teacher 2026",
        },
        "intro": [
            "A thank you note to teacher should sound respectful, specific, and warm. The best message does not need big words; it needs one honest reason your teacher mattered.",
            "TL;DR: mention what the teacher helped with, keep the tone sincere, add one personal detail, and close with a simple wish for their happiness and health.",
        ],
        "sections": [
            {
                "key": "best",
                "h2": "Best Thank You Note to Teacher 2026",
                "lines": [
                    "Thank you for teaching with patience, kindness, and belief in every student.",
                    "Your lessons stayed with me because you taught with care, not just rules.",
                    "Thank you for making learning feel possible even on difficult days.",
                    "A good teacher explains chapters; a great teacher builds confidence.",
                    "Your support helped me try harder and believe in my own effort.",
                    "Thank you for correcting mistakes without making them feel like failures.",
                    "Your classroom gave us discipline, encouragement, and many good memories.",
                    "I will always be grateful for the way you noticed every small improvement.",
                    "Thank you for being a teacher whose words still guide us outside school.",
                    "Your kindness made learning feel safer and more joyful.",
                ],
            },
            {
                "key": "thanksgiving",
                "h2": "Thanksgiving Message to Teacher",
                "lines": [
                    "This Thanksgiving, I am grateful for the teacher who made learning feel meaningful.",
                    "Thank you for giving your time, patience, and heart to every lesson.",
                    "I am thankful for your guidance because it helped me grow beyond marks.",
                    "Your encouragement was one of the gifts I will always remember.",
                    "Thanksgiving feels like the right day to honour your effort and care.",
                    "Thank you for turning ordinary school days into lessons for life.",
                    "I am grateful for your corrections, because they helped me become better.",
                    "Your belief gave students the courage to keep trying.",
                    "May this Thanksgiving bring you the same kindness you give to others.",
                    "Thank you for being a steady light in the classroom.",
                ],
            },
            {
                "key": "wishes",
                "h2": "Wishes for Teacher",
                "lines": [
                    "Wishing you happiness, good health, and many proud teaching moments.",
                    "May your dedication return to you as respect, joy, and peace.",
                    "Wishing you a year filled with appreciation and bright student smiles.",
                    "May every class you teach bring you fresh energy and purpose.",
                    "Wishing you success in every goal and comfort in every busy day.",
                    "May your kindness continue to inspire many more students.",
                    "Wishing you love from your students and pride in your journey.",
                    "May your work always be valued the way it deserves to be.",
                    "Wishing you peaceful days, grateful hearts, and happy memories.",
                    "May your teaching legacy keep growing beautifully.",
                ],
            },
            {
                "key": "message",
                "h2": "Message for Teacher",
                "lines": [
                    "Dear Teacher, thank you for helping me understand both lessons and life.",
                    "Your guidance made difficult subjects easier and school days brighter.",
                    "You taught us to ask questions, respect effort, and keep improving.",
                    "Thank you for being strict when needed and kind when it mattered most.",
                    "Your words helped me stay focused when I wanted to give up.",
                    "I appreciate the time you spent explaining things again and again.",
                    "You made every student feel seen, and that is a rare gift.",
                    "Thank you for teaching with heart and discipline together.",
                    "Your encouragement changed the way I looked at my own abilities.",
                    "I will always remember your lessons with gratitude.",
                ],
            },
            {
                "key": "thanks_wishes",
                "h2": "Thanks Wishes for Teacher",
                "lines": [
                    "Thank you and best wishes to a teacher who made learning feel personal.",
                    "Wishing you joy for every moment you spent helping students grow.",
                    "Thank you for your lessons, your patience, and your quiet support.",
                    "Best wishes to the teacher who made hard work feel worthwhile.",
                    "Thank you for giving your students courage along with knowledge.",
                    "Wishing you respect, happiness, and many beautiful memories.",
                    "Thank you for being the kind of teacher students remember with pride.",
                    "Best wishes for continued success, health, and fulfilment.",
                    "Thank you for helping us become more confident learners.",
                    "Wishing you every happiness you have helped others discover.",
                ],
            },
            {
                "key": "short",
                "h2": "Short Thank You Notes for Teacher",
                "lines": [
                    "Thank you for believing in me.",
                    "Your guidance made a real difference.",
                    "Grateful for your patience and care.",
                    "Thank you for making learning easier.",
                    "You are a teacher I will always remember.",
                    "Your support helped me grow.",
                    "Thank you for every thoughtful lesson.",
                    "You taught with kindness and purpose.",
                    "Grateful for your time and effort.",
                    "Thank you for inspiring me.",
                ],
            },
            {
                "key": "emotional",
                "h2": "Heart Touching Thank You Note to Teacher",
                "lines": [
                    "You helped me see that effort matters even before results arrive.",
                    "Thank you for noticing the student behind the marks.",
                    "Your kindness gave confidence to a learner who needed it.",
                    "Some lessons end in a notebook, but yours stayed in my heart.",
                    "I may forget chapters, but I will not forget your encouragement.",
                    "Thank you for making me feel capable when I doubted myself.",
                    "Your patience changed fear into curiosity.",
                    "You taught us that discipline can be gentle and strong together.",
                    "A teacher like you becomes part of a student's life story.",
                    "Thank you for helping me become a better version of myself.",
                ],
            },
            {
                "key": "parents",
                "h2": "Thank You Message to Teacher from Parents",
                "lines": [
                    "Thank you for guiding our child with patience, care, and discipline.",
                    "We appreciate the way you encourage learning beyond textbooks.",
                    "Your support has helped our child become more confident and responsible.",
                    "Thank you for creating a classroom where children feel respected.",
                    "We are grateful for your regular effort and thoughtful attention.",
                    "Your teaching has made a visible difference in our child's growth.",
                    "Thank you for balancing kindness with high expectations.",
                    "We value the time and heart you give to every student.",
                    "Your guidance is a blessing to families as well as children.",
                    "Wishing you continued happiness and success in your teaching journey.",
                ],
            },
            {
                "key": "student",
                "h2": "Thank You Message to Teacher from Student",
                "lines": [
                    "Thank you for making me feel brave enough to ask questions.",
                    "I am grateful for the way you explained things without losing patience.",
                    "Your classes helped me learn, improve, and stay motivated.",
                    "Thank you for encouraging me even when I made mistakes.",
                    "You made school feel less stressful and more meaningful.",
                    "I will always remember your advice and your support.",
                    "Thank you for helping me find confidence in my own effort.",
                    "Your teaching made a difficult subject feel possible.",
                    "I am lucky to have learned from you.",
                    "Thank you for being a teacher who truly cares.",
                ],
            },
            {
                "key": "caption",
                "h2": "Teacher Thank You Captions",
                "lines": [
                    "For the teacher who made learning brighter.",
                    "Grateful for guidance that stays for life.",
                    "A small thank you for a big difference.",
                    "Lessons, patience, and endless encouragement.",
                    "Thank you, teacher, for believing first.",
                    "A classroom memory worth keeping.",
                    "Respect and gratitude for a true mentor.",
                    "The best teachers leave lasting light.",
                    "Thankful for every lesson and smile.",
                    "Because good teachers shape good futures.",
                ],
            },
            {
                "key": "gift",
                "h2": "Jewellery Gift Ideas for Teacher",
                "lines": [
                    "A note should lead the gesture; a gift should only support the gratitude.",
                    "Choose jewellery that feels graceful, modest, and wearable for everyday moments.",
                    "A delicate pendant can feel thoughtful for a teacher who likes classic style.",
                    "A small bracelet works well when the message is simple and appreciative.",
                    "A ring can be a keepsake for a milestone farewell or long-term mentor.",
                    "Keep the card personal so the gift never feels transactional.",
                    "Avoid mentioning price, comparison, or obligation in the message.",
                    "Respect school and institutional gift rules before choosing anything valuable.",
                    "If unsure, a handwritten note with a small keepsake is safest.",
                    "The best teacher gift says respect, not display.",
                ],
            },
        ],
        "section_leads": {
            "Best Thank You Note to Teacher 2026": "Use these all-purpose lines for cards, WhatsApp, farewell notes, and appreciation posts.",
            "Thanksgiving Message to Teacher": "These Thanksgiving messages keep the tone grateful without sounding too formal.",
            "Wishes for Teacher": "Pair these wishes with a short thank you when you want a warm close.",
            "Message for Teacher": "These messages work well when you want a fuller note instead of one line.",
            "Thanks Wishes for Teacher": "Use these when you want gratitude and blessings in the same message.",
            "Short Thank You Notes for Teacher": "Short notes work best for tags, cards, and quick replies.",
            "Heart Touching Thank You Note to Teacher": "Choose these emotional notes for a mentor, class teacher, or favourite teacher.",
            "Thank You Message to Teacher from Parents": "Parents can use these respectful lines for school notes and year-end messages.",
            "Thank You Message to Teacher from Student": "Students can keep the message honest, simple, and specific.",
            "Teacher Thank You Captions": "These captions are useful for photos, stories, reels, and farewell posts.",
            "Jewellery Gift Ideas for Teacher": "A gift is optional; the thank you note should still carry the heart of the moment.",
        },
        "faqs": [
            ["How do I write a thank you note to teacher?", "Start with thank you, mention one specific lesson or quality, say how it helped you, and close with a respectful wish."],
            ["What is a good short thank you note to teacher?", "A good short note is: Thank you for believing in me and making learning feel possible."],
            ["What can parents write to thank a teacher?", "Parents can write: Thank you for guiding our child with patience, care, and discipline. We truly appreciate your effort."],
            ["What is a Thanksgiving message to teacher?", "A Thanksgiving message to teacher expresses gratitude for patience, guidance, encouragement, and the care behind daily lessons."],
            ["What are good wishes for teacher?", "Good wishes include happiness, good health, success, respect from students, and many proud teaching moments."],
            ["Is jewellery a good thank you gift for teacher?", "Jewellery can be thoughtful only when appropriate and allowed by school rules. Keep it modest and pair it with a sincere handwritten note."],
        ],
    }

    config = {
        "rank": 92,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-teacherthanks",
        "occasion_year": "Teacher Thank You Notes 2026",
        "carousel_alt_prefix": "thank you note to teacher 2026 gift idea",
        "gift_h2": "Teacher Appreciation Jewellery Gift Ideas",
        "gift_blurb": "A teacher thank you note is complete on its own, but a modest keepsake can make a farewell, class milestone, or mentor moment feel remembered. These approved BlueStone designs stay graceful and low-key.",
        "conclusion_html": "A thank you note to teacher works best when it is sincere, specific, and respectful. Choose one line, add one real classroom memory, and let the teacher know their effort mattered.",
        "schema_keywords": [
            "thank you note to teacher",
            "thanksgiving message to teacher",
            "wishes for teacher",
            "message for teacher",
            "thanks wishes for teacher",
            "teacher thank you captions",
        ],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(rows, "The Aagarna Pendant", "Pendants"),
            product(rows, "The Shining Star Bracelet", "Bracelet"),
            product(rows, "The Quinn Ring", "Rings"),
            product(rows, "The Asya Huggie Earrings", "Earrings"),
            product(rows, "The Malocchio Charm Holder Bracelet", "Bracelet"),
            product(rows, "The Ebony Ring", "Rings"),
        ],
        "flatlay_insert_h2": "Thanksgiving Message to Teacher",
        "lifestyle_insert_h2": "Jewellery Gift Ideas for Teacher",
        "more_reads_html": "For more appreciation and occasion ideas, see <a href=\"https://blog.bluestone.com/mother-daughter-quotes-2026/\">mother daughter quotes 2026</a>, <a href=\"https://blog.bluestone.com/humanity-quotes-2026/\">humanity quotes 2026</a>, <a href=\"https://blog.bluestone.com/speedy-recovery-message-2026-get-well-soon-wishes/\">speedy recovery messages 2026</a>, and <a href=\"https://blog.bluestone.com/advance-happy-birthday-wishes-2026/\">advance birthday wishes 2026</a>.",
        "how_to_html": "Before sending, replace generic words with one real detail. Mention a subject, a habit, a moment of encouragement, or a lesson that made you better.",
        "faq_h2": "Frequently Asked Questions about Thank You Notes to Teachers",
        "min_lines": 100,
        "section_leads": sections["section_leads"],
    }

    prompts = {
        "rank": 92,
        "slug": "thank-you-note-to-teacher-2026",
        "output_prefix": PREFIX,
        "occasion": "Teacher Thank You Notes 2026",
        "primary_kw": "thank you note to teacher",
        "caption_occasion": "Thank you note to teacher",
        "caption_year": "2026",
        "flatlay_setting": "study-desk",
        "workflow": "Higgsfield MCP nano_banana_pro. Campaign hybrid with mandatory body_image scale line for people shots. Do not generate until balance succeeds. Max 2 concurrent generations.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/thank-you-note-to-teacher-hero-2026.webp",
            "flatlay": "output/magnific_generated/thank-you-note-to-teacher-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/thank-you-note-to-teacher-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "thank you note to teacher 2026 hero The Aagarna Pendant",
            "flatlay": "thank you note to teacher 2026 flatlay The Shining Star Bracelet",
            "lifestyle": "thank you note to teacher 2026 lifestyle The Quinn Ring",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                "code": "BIIP0550P16",
                "name": "The Aagarna Pendant",
                "gender": "Female",
                "height_mm": 20.31,
                "width_mm": 13.41,
                "size_prompt_note": "pendant product height 20.31 mm and width 13.41 mm; product dimensions, not face size; copy worn neck scale from body_image",
                "alt": "thank you note to teacher 2026 hero with The Aagarna Pendant",
                "caption": "Thank you note to teacher 2026 vibe: The Aagarna Pendant",
                "product": {"code": "BIIP0550P16", "name": "The Aagarna Pendant", "pdp": "https://www.bluestone.com/pendants/the-aagarna-pendant~54965.html"},
                "cdn": [],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Aagarna Pendant/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Aagarna Pendant/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} Thank you note to teacher 2026 hero, fair-skinned Indian adult woman teacher sitting at a bright classroom desk, smiling warmly while reading a blank cream thank you card from a student. Books, soft chalkboard blur, fountain pen, and a small wrapped gift nearby. Full face, both eyes, complete smile, upper body, hands, blank card, gift, and pendant visible with safe margins. Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, soft daylight, realistic shadows, 16:9.\n\nThe teacher physically wears The Aagarna Pendant from @img1 body_image and @img2 design on a fine chain at upper chest. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: pendant product height_mm=20.31 and width_mm=13.41. These are real product dimensions, NOT face-size instructions. Keep pendant size on the neck like @img1 body_image worn neck scale: subtle pendant size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the yellow gold open circular pendant with refined diamond detail exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery in the image. Bare wrists, bare fingers, no watches, no bracelets, no rings, no earrings, no extra necklaces. Jewellery touches skin or fabric with soft contact shadow, never a floating cutout. The note card must be blank with no letters, no handwriting, no symbols, no numbers.\n\nAvoid: cropped face, cropped eyes, cropped forehead, cropped head, readable text, handwriting, printed letters, numbers, symbols on card, man wearer, child, minor, second person, background student, extra hands, extra necklaces, rings, watches, earrings, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow.",
            },
            "flatlay": {
                "code": "BIMG0635V45",
                "name": "The Shining Star Bracelet",
                "gender": "Female",
                "height_mm": 9.5,
                "width_mm": 152.4,
                "size_prompt_note": "bracelet charm height 9.5 mm and bracelet width/length 152.4 mm; product dimensions, not face size",
                "alt": "thank you note to teacher 2026 flatlay with The Shining Star Bracelet",
                "caption": "Thank you note to teacher 2026 keepsake: The Shining Star Bracelet",
                "product": {"code": "BIMG0635V45", "name": "The Shining Star Bracelet", "pdp": "https://www.bluestone.com/bracelets/the-shining-star-bracelet~63731.html"},
                "cdn": [],
                "local_reference_images": [
                    "ProductImages/raw/Bracelets/The Shining Star Bracelet/0_primary.png",
                    "ProductImages/raw/Bracelets/The Shining Star Bracelet/2_front.png",
                    "ProductImages/raw/Bracelets/The Shining Star Bracelet/3_back.png",
                ],
                "ref_roles": ["primary", "front", "back"],
                "prompt": f"Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\nThank you note to teacher 2026 top-down flatlay. Flatlay setting ID: study-desk. Surface and props: warm wooden teacher desk, blank cream note card, capped fountain pen, closed notebook, apple, tiny dried flowers, and soft classroom daylight. No readable text, no letters, no numbers, no symbols on any prop.\n\nThe identical Shining Star Bracelet from @img1, @img2 and @img3 rests naturally on the desk at true PDP scale. Product dimensions from PDP: bracelet charm_height_mm=9.5 and bracelet_width_or_length_mm=152.4. These are product dimensions, NOT face-size instructions. Do not enlarge for visibility. Full bracelet visible, yellow gold fine chain bracelet with small polished star charm, 100 percent identical design, zero distortion, HD metal detail.\n\nProps stay secondary and quiet. No people, no hands, no readable text, no brand marks. Jewellery is the clear subject but still true to real size.\n\nAvoid: hands, people, floating overlays, cutouts, incorrect star charm design, distorted metal, readable text, logos, price tags, brand marks on props, blown whites, HDR glow, illustration, CGI.",
            },
            "lifestyle": {
                "code": "BIAR0097R16",
                "name": "The Quinn Ring",
                "gender": "Female",
                "height_mm": 21.6,
                "width_mm": 7.84,
                "size_prompt_note": "ring product face height 21.6 mm and width 7.84 mm; product dimensions, not face size; copy worn finger scale from body_image",
                "alt": "thank you note to teacher 2026 lifestyle with The Quinn Ring",
                "caption": "Thank you note to teacher 2026 vibe: The Quinn Ring",
                "product": {"code": "BIAR0097R16", "name": "The Quinn Ring", "pdp": "https://www.bluestone.com/rings/the-quinn-ring~57845.html"},
                "cdn": [],
                "local_reference_images": [
                    "ProductImages/raw/Rings/The Quinn Ring/1_body_portrait.png",
                    "ProductImages/raw/Rings/The Quinn Ring/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} Thank you note to teacher 2026 lifestyle, solo fair-skinned Indian adult woman sitting near a sunlit study table writing a blank thank you card for her teacher, with a tea cup, notebook, and small wrapped gift nearby. Full face, both eyes, complete gentle smile, writing hand, ring, blank note card, gift, and upper body visible with safe margins. Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, soft daylight, realistic shadows, 16:9.\n\nThe woman physically wears The Quinn Ring from @img1 body_image and @img2 design on one finger. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: ring product face height_mm=21.6 and width_mm=7.84. These are real product dimensions, NOT face-size instructions. Keep ring size on the finger like @img1 body_image worn finger scale: subtle ring size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the yellow gold and diamond wave ring exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This ring is the single and only jewellery in the image. Bare neck, bare wrists, no watch, no bracelet, no earrings, no necklace, no other rings. Jewellery touches finger with soft contact shadow, never a floating cutout. The note card must be blank with no letters, no handwriting, no symbols, no numbers.\n\nAvoid: background people, man wearer, child, minor, second person, extra hands, silhouettes, readable text, handwriting, printed letters, numbers, symbols on card, extra necklaces, rings, watches, earrings, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, cropped face, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow.",
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
