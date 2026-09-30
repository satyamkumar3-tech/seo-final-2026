#!/usr/bin/env python3
"""Build Rank 91 mother daughter quotes assets and Type 3 manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank91_MotherDaughterQuotes"
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
            "title": "Mother Daughter Quotes 2026: Heart Touching Lines",
            "slug": "mother-daughter-quotes-2026",
            "meta_desc": "Mother daughter quotes 2026 with mom and daughter quotes, daughter love quotes, heart touching mother quotes, and inspirational Mothers Day lines today.",
            "focus_kw": "mom and daughter quotes",
            "yoast_title": "Mother Daughter Quotes 2026",
        },
        "intro": [
            "Mom and daughter quotes should feel tender, honest, and easy to share. The best line can honour childhood memories, adult friendship, daily care, and the quiet way a mother and daughter keep returning to each other.",
            "TL;DR: choose a short quote for captions, a heart touching line for cards, a daughter love quote for emotional posts, and one personal memory when the message needs to sound truly yours.",
        ],
        "sections": [
            {
                "key": "best",
                "h2": "Best Mom and Daughter Quotes 2026",
                "lines": [
                    "A mother and daughter may argue over small things, but love keeps the door open.",
                    "The bond between a mother and daughter is made of memories, advice, laughter, and forgiveness.",
                    "A daughter grows, but a mother's blessing keeps walking beside her.",
                    "Mothers teach daughters how to love, and daughters teach mothers how love changes with time.",
                    "In every daughter, a mother sees a brave new version of her own heart.",
                    "A mother daughter bond is not perfect every day, but it is precious every season.",
                    "A daughter's smile can make a mother's tired day feel lighter.",
                    "A mother is the first home a daughter ever knows.",
                    "Daughters carry their mothers in habits, prayers, stories, and strength.",
                    "The sweetest family bond is one that learns to listen again and again.",
                ],
            },
            {
                "key": "mother_daughter",
                "h2": "Mother Daughter Quotes",
                "lines": [
                    "A mother and daughter are two hearts learning the same language in different years.",
                    "Mother daughter love is a conversation that begins before words.",
                    "A daughter may outgrow her mother's lap, but never the comfort of her care.",
                    "A mother becomes a daughter's first mirror and later her strongest witness.",
                    "Between a mother and daughter, love often hides in ordinary reminders.",
                    "A daughter carries her mother's courage even when she walks her own road.",
                    "A mother's advice may sound repeated, but it is usually love in practical clothes.",
                    "A daughter is a mother's yesterday, today, and tomorrow sitting at the same table.",
                    "The mother daughter bond is stitched with patience, pride, and second chances.",
                    "No distance fully quiets the pull between a mother and daughter.",
                ],
            },
            {
                "key": "daughter_love",
                "h2": "Daughter Love Quotes",
                "lines": [
                    "A daughter's love makes a home feel younger than its walls.",
                    "Daughter love is the soft courage that teaches a family to hope.",
                    "A daughter is a blessing who turns ordinary days into stories worth keeping.",
                    "The love for a daughter grows quietly, then fills every corner of life.",
                    "A daughter's kindness is one of the most beautiful gifts a mother can receive.",
                    "To love a daughter is to pray for her strength without holding back her wings.",
                    "A daughter brings music into the parts of life that had become too silent.",
                    "Daughter love is pride, protection, laughter, and a thousand small worries.",
                    "A daughter is loved not for what she achieves, but for who she is.",
                    "Every daughter deserves to hear that she is enough before the world tests her.",
                ],
            },
            {
                "key": "heart_touching",
                "h2": "Daughter Heart Touching Mother Quotes",
                "lines": [
                    "Mom, your love has been the quiet strength behind my loudest dreams.",
                    "I did not understand every sacrifice then, but I carry gratitude for them now.",
                    "A mother's love is the hand a daughter remembers even when she is walking alone.",
                    "Thank you, Mom, for loving me through every version of myself.",
                    "Your prayers reached places where my own confidence could not.",
                    "I learned tenderness from your care and courage from your patience.",
                    "The older I grow, the more I see how much of my strength came from you.",
                    "Mom, you are the first person who made love feel safe.",
                    "Your voice still becomes comfort when life feels too loud.",
                    "A daughter never forgets the mother who believed before the world noticed.",
                ],
            },
            {
                "key": "mothers_day",
                "h2": "Mothers Day Inspirational Quotes",
                "lines": [
                    "Mothers Day is a reminder to thank the woman who made love look like daily work.",
                    "A mother inspires not only by teaching, but by continuing with grace.",
                    "Behind many confident daughters stands a mother who whispered, try again.",
                    "A mother's strength is often quiet, but its effect lasts for generations.",
                    "Celebrate mothers for the meals, messages, sacrifices, and silent prayers too.",
                    "A mother turns care into courage long before anyone calls it inspiration.",
                    "Mothers Day belongs to every woman who made a child feel protected.",
                    "A mother's love is a lesson in patience that never fully ends.",
                    "The best tribute to a mother is to live with kindness she can recognise.",
                    "A mother's influence is not loud, but it is deeply rooted.",
                ],
            },
            {
                "key": "short",
                "h2": "Short Mother Daughter Quotes",
                "lines": [
                    "Mother and daughter, forever connected.",
                    "A daughter is a mother's living blessing.",
                    "Mom is home in human form.",
                    "Daughter love makes life softer.",
                    "A mother's heart remembers everything.",
                    "My mother, my first safe place.",
                    "Her daughter, her pride.",
                    "Love runs from mother to daughter.",
                    "A bond no distance can erase.",
                    "Two hearts, one family story.",
                ],
            },
            {
                "key": "emotional",
                "h2": "Emotional Mom and Daughter Quotes",
                "lines": [
                    "The emotional bond between a mother and daughter often grows deeper after difficult years.",
                    "A mother may not always have perfect words, but her worry usually comes from love.",
                    "A daughter understands her mother differently when life asks her to be strong.",
                    "Some mother daughter moments are healed by one honest conversation.",
                    "A mother's tears are often hidden behind practical advice.",
                    "A daughter's apology can become a beautiful bridge back to closeness.",
                    "Love between mother and daughter survives pauses, distance, and misunderstood days.",
                    "The bond becomes stronger when both hearts choose softness over pride.",
                    "A mother and daughter can become friends without forgetting their roots.",
                    "The deepest family love is not flawless; it keeps trying.",
                ],
            },
            {
                "key": "funny",
                "h2": "Funny Mother Daughter Quotes",
                "lines": [
                    "A mother and daughter can disagree for one hour and share snacks five minutes later.",
                    "Mom knows where everything is, including the truth you tried to hide.",
                    "Daughters inherit their mother's smile, style, and selective hearing.",
                    "A mother's missed call has more emotional power than any alarm.",
                    "Mother daughter shopping is love, debate, and a bill no one wants to discuss.",
                    "Behind every confident daughter is a mom asking if she ate properly.",
                    "Mom's advice arrives free, repeated, and usually correct.",
                    "A daughter becomes an adult, but her mother still checks the weather for her.",
                    "Mother daughter love means borrowing clothes and returning opinions.",
                    "The family group may be quiet, but Mom is always typing.",
                ],
            },
            {
                "key": "captions",
                "h2": "Mother Daughter Captions",
                "lines": [
                    "My first home and forever heart.",
                    "Mother daughter love, always.",
                    "Built from love, stories, and tea.",
                    "Mom and me, same heart.",
                    "A bond that grows with time.",
                    "Her daughter, her biggest fan.",
                    "Love passed down beautifully.",
                    "My mother, my blessing.",
                    "Two generations, one soft bond.",
                    "Forever grateful for this love.",
                ],
            },
            {
                "key": "long",
                "h2": "Long Mother Daughter Quotes",
                "lines": [
                    "A mother and daughter share a bond that changes shape but never loses its meaning.",
                    "In childhood, a mother is protection; in adulthood, she becomes memory, advice, and quiet friendship.",
                    "A daughter grows into her own life, yet still carries her mother's lessons in small daily choices.",
                    "The love is not always loud or easy, but it is often the thread that keeps a family tender.",
                    "A mother learns to let go while still blessing every step.",
                    "A daughter learns to understand the care that once felt like rules.",
                    "With time, both begin to see each other as human, not only as roles.",
                    "That is when the bond becomes even more beautiful.",
                    "It becomes a friendship built on history, forgiveness, and deep affection.",
                    "Mother daughter love is one of life's longest conversations.",
                ],
            },
            {
                "key": "gift",
                "h2": "Jewellery Gift Ideas for Mother and Daughter",
                "lines": [
                    "A quote carries the feeling, while a small keepsake can help the memory stay close.",
                    "For a mother, choose jewellery that feels graceful, wearable, and connected to her everyday style.",
                    "For a daughter, choose a piece that feels personal rather than overly formal.",
                    "A pendant can symbolise protection when the message is emotional.",
                    "A bracelet works well for a daughter who likes visible but delicate accessories.",
                    "A ring can mark a milestone, apology, celebration, or quiet thank you.",
                    "Avoid making the note about cost, size, or display.",
                    "Write one line from the heart and let the gift support it softly.",
                    "Matching styles are sweet only when both people would actually wear them.",
                    "The best gift says, our bond matters in ordinary life too.",
                ],
            },
        ],
        "section_leads": {
            "Best Mom and Daughter Quotes 2026": "Use these all-rounder lines when you want a warm quote for cards, captions, WhatsApp, or family posts.",
            "Mother Daughter Quotes": "These mother daughter quotes keep the tone emotional but still simple enough to share.",
            "Daughter Love Quotes": "Use these lines when the message is about a daughter's place in the family heart.",
            "Daughter Heart Touching Mother Quotes": "These are written from a daughter's side, ideal for a note to Mom.",
            "Mothers Day Inspirational Quotes": "These Mothers Day inspirational quotes honour care, patience, strength, and daily love.",
            "Short Mother Daughter Quotes": "Short lines work well for captions, status updates, and quick messages.",
            "Emotional Mom and Daughter Quotes": "Use these when the relationship has depth, history, and real feeling.",
            "Funny Mother Daughter Quotes": "Funny lines are safest when the humour is affectionate and familiar.",
            "Mother Daughter Captions": "These captions fit photos, reels, stories, and family albums.",
            "Long Mother Daughter Quotes": "Send a longer quote when the bond deserves more than one short sentence.",
            "Jewellery Gift Ideas for Mother and Daughter": "A gift is optional; the quote should still be the heart of the moment.",
        },
        "faqs": [
            ["What is the best mother daughter quote?", "A strong mother daughter quote is warm and specific. Try: A daughter grows, but a mother's blessing keeps walking beside her."],
            ["What are good mom and daughter quotes for captions?", "Good mom and daughter quotes for captions are short, emotional, and easy to read. Try: Mom and me, same heart, or My first home and forever heart."],
            ["What is a heart touching quote for mother from daughter?", "A heart touching quote from daughter to mother can be: Mom, your love has been the quiet strength behind my loudest dreams."],
            ["What are daughter love quotes?", "Daughter love quotes express pride, protection, tenderness, and gratitude for a daughter. They work well for birthday notes, family captions, and emotional posts."],
            ["Can I use these quotes for Mothers Day?", "Yes. Many of these quotes can work for Mothers Day, especially when you add one personal memory, a thank you, or a blessing."],
            ["Is jewellery a good gift for a mother or daughter?", "Jewellery can be thoughtful when it suits her daily style. Pair it with a sincere quote so the gift feels personal, not transactional."],
        ],
    }

    config = {
        "rank": 91,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-motherdaughter",
        "occasion_year": "Mother Daughter Quotes 2026",
        "carousel_alt_prefix": "mother daughter quotes 2026 gift idea",
        "gift_h2": "Mother Daughter Jewellery Gift Ideas",
        "gift_blurb": "If the quote says what the heart feels, a wearable keepsake can turn the moment into something she remembers. These six approved BlueStone designs suit mother daughter gifting without mentioning prices.",
        "conclusion_html": "Mother daughter quotes work best when they sound personal and gentle. Pick one line, add a memory or name, and let the message honour a bond that keeps growing through ordinary days.",
        "schema_keywords": [
            "mom and daughter quotes",
            "mother daughter quotes",
            "daughter love quotes",
            "daughter heart touching mother quotes",
            "mothers day inspirational quotes",
            "mother daughter captions",
        ],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(rows, "The Protecteur Evil Eye Pendant", "Pendants"),
            product(rows, "The Kricia Charm Bracelet", "Bracelet"),
            product(rows, "The Le Sommet Ring", "Rings"),
            product(rows, "The Ailia Evil Eye Layered Necklace", "Necklaces"),
            product(rows, "The Nettile Huggie Earrings", "Earrings"),
            product(rows, "The Pervinca Charm Holder Bracelet", "Bracelet"),
        ],
        "flatlay_insert_h2": "Daughter Love Quotes",
        "lifestyle_insert_h2": "Jewellery Gift Ideas for Mother and Daughter",
        "more_reads_html": "For more family occasion lines, see <a href=\"https://blog.bluestone.com/birthday-wishes-for-granddaughter-2026/\">birthday wishes for granddaughter 2026</a>, <a href=\"https://blog.bluestone.com/whatsapp-birthday-wishes-for-wife-2026/\">birthday wishes for wife 2026</a>, <a href=\"https://blog.bluestone.com/husband-birthday-wishes-2026/\">husband birthday wishes 2026</a>, and <a href=\"https://blog.bluestone.com/humanity-quotes-2026/\">humanity quotes 2026</a>.",
        "how_to_html": "Choose a quote based on the relationship moment. Use a short line for captions, a heart touching line for a private card, and a funny line only when the humour already belongs to your bond.",
        "faq_h2": "Frequently Asked Questions about Mother Daughter Quotes",
        "min_lines": 100,
        "section_leads": sections["section_leads"],
    }

    prompts = {
        "rank": 91,
        "slug": "mother-daughter-quotes-2026",
        "output_prefix": PREFIX,
        "occasion": "Mother Daughter Quotes 2026",
        "primary_kw": "mom and daughter quotes",
        "caption_occasion": "Mother daughter quotes",
        "caption_year": "2026",
        "flatlay_setting": "windowsill-daylight",
        "workflow": "Higgsfield MCP nano_banana_pro. Campaign hybrid with mandatory body_image scale line for people shots. Do not generate until balance succeeds. Max 2 concurrent generations.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{PREFIX}_insert_h2s.json",
        "product_media_json": f"output/{PREFIX}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/mother-daughter-quotes-hero-2026.webp",
            "flatlay": "output/magnific_generated/mother-daughter-quotes-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/mother-daughter-quotes-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "mother daughter quotes 2026 hero The Protecteur Evil Eye Pendant",
            "flatlay": "mother daughter quotes 2026 flatlay The Kricia Charm Bracelet",
            "lifestyle": "mother daughter quotes 2026 lifestyle The Le Sommet Ring",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                "code": "BISE0987P01",
                "name": "The Protecteur Evil Eye Pendant",
                "gender": "Female",
                "height_mm": 22.33,
                "width_mm": 14.46,
                "size_prompt_note": "pendant product height 22.33 mm and width 14.46 mm; product dimensions, not face size; copy worn neck scale from body_image",
                "alt": "mom and daughter quotes 2026 hero with The Protecteur Evil Eye Pendant",
                "caption": "Mother daughter quotes 2026 vibe: The Protecteur Evil Eye Pendant",
                "product": {"code": "BISE0987P01", "name": "The Protecteur Evil Eye Pendant", "pdp": "https://www.bluestone.com/pendants/the-protecteur-evil-eye-pendant~114379.html"},
                "cdn": [
                    "https://kinclimg8.bluestone.com/giproduct/BISE0987P01_YAA18DIG6BLTOSIG7_ABCD00-BP-PICS-00000-1024-78991.png",
                    "https://kinclimg7.bluestone.com/giproduct/BISE0987P01_YAA18DIG6BLTOSIG7_ABCD00-PICS-00002-1024-78991.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Pendants/The Protecteur Evil Eye Pendant/1_body_portrait.png",
                    "ProductImages/raw/Pendants/The Protecteur Evil Eye Pendant/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} Mother daughter quotes 2026 hero, two fair-skinned Indian adult women, a mother and adult daughter, sitting together in a bright modern Indian living room and smiling over a blank cream note card beside tea cups and a small wrapped gift. Both full faces, both eyes, complete smiles, upper bodies, hands, blank card, gift, and pendant visible with safe margins. Exactly two people in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, soft daylight, realistic shadows, 16:9.\n\nThe adult daughter physically wears The Protecteur Evil Eye Pendant from @img1 body_image and @img2 design on a fine chain at upper chest. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: pendant product height_mm=22.33 and width_mm=14.46. These are real product dimensions, NOT face-size instructions. Keep pendant size on the neck like @img1 body_image worn neck scale: subtle pendant size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the yellow gold evil eye pendant with blue stone halo and diamond center exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This pendant is the single and only jewellery in the image. Bare wrists, bare fingers, no watches, no bracelets, no rings, no earrings, no extra necklaces on either woman. Jewellery touches skin or fabric with soft contact shadow, never a floating cutout. The note card must be blank with no letters, no handwriting, no symbols, no numbers.\n\nAvoid: cropped face, cropped eyes, cropped forehead, cropped head, readable text, handwriting, printed letters, numbers, symbols on card, man wearer, child, minor, third person, extra hands, extra necklaces, rings, watches, earrings, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow.",
            },
            "flatlay": {
                "code": "BIPO0730V39",
                "name": "The Kricia Charm Bracelet",
                "gender": "Female",
                "height_mm": 165.1,
                "width_mm": 12.5,
                "size_prompt_note": "bracelet length 165.1 mm and charm width about 12.5 mm; product dimensions, not face size",
                "alt": "mother daughter quotes 2026 flatlay with The Kricia Charm Bracelet",
                "caption": "Mother daughter quotes 2026 keepsake: The Kricia Charm Bracelet",
                "product": {"code": "BIPO0730V39", "name": "The Kricia Charm Bracelet", "pdp": "https://www.bluestone.com/bracelets/the-kricia-charm-bracelet~75605.html"},
                "cdn": [],
                "local_reference_images": [
                    "ProductImages/raw/Bracelets/The Kricia Charm Bracelet/0_primary.png",
                    "ProductImages/raw/Bracelets/The Kricia Charm Bracelet/2_side_1.png",
                    "ProductImages/raw/Bracelets/The Kricia Charm Bracelet/3_back.png",
                ],
                "ref_roles": ["primary", "side", "back"],
                "prompt": f"Photoreal high-end jewellery still life, top-down editorial product flatlay. {FILMIC_STYLE}\n\nMother daughter quotes 2026 top-down flatlay. Flatlay setting ID: windowsill-daylight. Surface and props: painted cream windowsill, sheer curtain blur, small plant pot, blank envelope, blank cream note card, and a simple ceramic tea cup. No readable text, no letters, no numbers, no symbols on any prop.\n\nThe identical Kricia Charm Bracelet from @img1, @img2 and @img3 rests naturally on the windowsill at true PDP scale. Product dimensions from PDP: bracelet length_mm=165.1 and charm_width_mm=12.5. These are product dimensions, NOT face-size instructions. Do not enlarge for visibility. Full bracelet visible, yellow gold charm bracelet with delicate chain and multiple small symbolic charms, 100 percent identical design, zero distortion, HD metal and stone detail.\n\nProps stay secondary and quiet. No people, no hands, no readable text, no brand marks. Jewellery is the clear subject but still true to real size.\n\nAvoid: hands, people, floating overlays, cutouts, incorrect charm design, distorted metal, readable text, logos, price tags, brand marks on props, blown whites, HDR glow, illustration, CGI.",
            },
            "lifestyle": {
                "code": "BISE0932R181",
                "name": "The Le Sommet Ring",
                "gender": "Female",
                "height_mm": 21.93,
                "width_mm": 7.95,
                "size_prompt_note": "ring product face height 21.93 mm and width 7.95 mm; product dimensions, not face size; copy worn finger scale from body_image",
                "alt": "mother daughter quotes 2026 lifestyle with The Le Sommet Ring",
                "caption": "Mother daughter quotes 2026 vibe: The Le Sommet Ring",
                "product": {"code": "BISE0932R181", "name": "The Le Sommet Ring", "pdp": "https://www.bluestone.com/rings/the-le-sommet-ring~105031.html"},
                "cdn": [],
                "local_reference_images": [
                    "ProductImages/raw/Rings/The Le Sommet Ring/1_body_portrait.png",
                    "ProductImages/raw/Rings/The Le Sommet Ring/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": f"STRICT JEWELLERY-COMPLIANCE PHOTOREAL IMAGE. {FILMIC_STYLE} Mother daughter quotes 2026 lifestyle, solo fair-skinned Indian adult woman, an adult daughter, sitting near a bright window and writing a blank note card for her mother with a tea cup and small wrapped gift nearby. Full face, both eyes, complete smile, writing hand, ring, blank note card, gift, and upper body visible with safe margins. Exactly one person in the entire image. Camera pulled back medium shot, 85mm DSLR look, natural skin texture, soft daylight, realistic shadows, 16:9.\n\nThe woman physically wears The Le Sommet Ring from @img1 body_image and @img2 design on one finger. GENDER LOCK: Female product on adult woman only. Product dimensions from PDP: ring product face height_mm=21.93 and width_mm=7.95. These are real product dimensions, NOT face-size instructions. Keep ring size on the finger like @img1 body_image worn finger scale: subtle ring size, not enlarged. Use @img2 only for jewellery design.\n\nReplicate the rose gold and diamond layered ring exactly, 100 percent identical to refs, zero distortion, HD metal and stone detail. This ring is the single and only jewellery in the image. Bare neck, bare wrists, no watch, no bracelet, no earrings, no necklace, no other rings. Jewellery touches finger with soft contact shadow, never a floating cutout. The note card must be blank with no letters, no handwriting, no symbols, no numbers.\n\nAvoid: background people, man wearer, child, minor, second person, extra hands, silhouettes, readable text, handwriting, printed letters, numbers, symbols on card, extra necklaces, rings, watches, earrings, bracelets, bangles, floating jewellery overlay, giant jewellery collage, product cutout over people, packshot composited on lifestyle photo, oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, logos, distorted hands, cropped face, dark skin, deep brown skin, heavily tanned skin, illustration, CGI, HDR glow.",
            },
        },
    }

    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 91

Article: Mother Daughter Quotes 2026
Status: Draft assets prepared
Date: 2026-07-24

## A. Intent and Brief
- [x] Primary keyword: mom and daughter quotes
- [x] Supporting keywords mapped to H2s and FAQs
- [x] Sheet Optimize treated as New
- [x] Fresh slug: mother-daughter-quotes-2026
- [x] 2026 year lock used

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""

    write_json(f"output/{PREFIX}_sections.json", sections)
    write_json("output/publish_configs/rank91.json", config)
    write_json(f"output/{PREFIX}_type3_prompts.json", prompts)
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
