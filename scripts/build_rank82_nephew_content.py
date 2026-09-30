#!/usr/bin/env python3
"""Build Rank 82 nephew birthday article config and Type 3 prompt manifest."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


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
    print(target)


def main() -> None:
    rows = load_products()
    prefix = "Week1_Rank82_NephewBirthday"

    sections = {
        "meta": {
            "title": "Happy Birthday Wishes for Nephew 2026: Sweet and Funny Lines",
            "slug": "birthday-wishes-for-nephew-2026",
            "meta_desc": "Find happy birthday wishes for nephew 2026, with sweet, funny, heartfelt, boy, English, caption and quote ideas for cards, WhatsApp and family posts now.",
            "focus_kw": "happy birthday wishes for nephew",
            "yoast_title": "Happy Birthday Wishes for Nephew 2026",
        },
        "intro": [
            "Happy birthday wishes for nephew should feel proud, warm and a little playful. Whether he is a little boy, a teen, or a grown man with his own quiet style, the best message sounds like family and not like a copied forward.",
            "TL;DR: choose a short wish for WhatsApp, a heartfelt line for a card, and a funny message only if your nephew enjoys that tone. Add his name, one real detail, and a simple blessing for 2026.",
        ],
        "sections": [
            {
                "key": "best",
                "h2": "Best Happy Birthday Wishes for Nephew",
                "lines": [
                    "Happy birthday, my dear nephew. May 2026 bring you confidence, good friends and reasons to smile every day.",
                    "Wishing you a birthday filled with laughter, love and the kind of memories your heart keeps for years.",
                    "Happy birthday to the nephew who makes our family brighter, louder and much more fun.",
                    "May your new year of life be full of brave choices, happy surprises and quiet wins.",
                    "Happy birthday, beta. Watching you grow has been one of the sweetest joys of our family.",
                    "You are loved more than you know and celebrated more than one day can show.",
                    "May your birthday bring cake, blessings, good health and a future that feels exciting.",
                    "Happy birthday to a nephew who carries kindness, curiosity and a spark that is fully his own.",
                    "Keep growing with courage, laughing with your whole heart and choosing people who value you.",
                    "Happy birthday. May this year make you proud of yourself in small and big ways.",
                ],
            },
            {
                "key": "short",
                "h2": "Short Birthday Wishes for Nephew",
                "lines": [
                    "Happy birthday, champ. Stay happy and blessed.",
                    "Proud of you today and always, dear nephew.",
                    "Wishing you cake, joy and endless smiles.",
                    "Happy birthday to our family superstar.",
                    "Grow strong, stay kind and keep shining.",
                    "Big love on your special day, beta.",
                    "Happy birthday, nephew. You are deeply loved.",
                    "More laughter, more courage, more good news.",
                    "Blessings, fun and bright days ahead.",
                    "Have the happiest birthday, my favourite troublemaker.",
                ],
            },
            {
                "key": "heartfelt",
                "h2": "Heart Touching Birthday Wishes for Nephew",
                "lines": [
                    "Happy birthday, my nephew. Your journey has given our family so many proud and tender moments.",
                    "I hope you always know that you have a safe place in this family, no matter how grown up you become.",
                    "May life be gentle where you need rest and exciting where you need courage.",
                    "You have a good heart, and I hope the world gives you people who protect it well.",
                    "Happy birthday. I pray your dreams become clearer and your confidence becomes stronger this year.",
                    "You are not just my nephew, you are one of the beautiful reasons our family feels complete.",
                    "May every challenge teach you something and every blessing remind you how loved you are.",
                    "I have watched you become thoughtful, funny and strong in your own way. That is a gift.",
                    "Happy birthday, beta. Keep your heart soft, your choices wise and your smile close.",
                    "No matter where life takes you, remember that this family will always cheer for you.",
                ],
            },
            {
                "key": "funny",
                "h2": "Funny Happy Birthday Nephew Messages",
                "lines": [
                    "Happy birthday, nephew. May your cake be bigger than your homework pile.",
                    "Another year older, still not too old to be spoiled by the family.",
                    "Happy birthday to the boy who can turn any normal house into a noise festival.",
                    "May your gifts be many and your relatives ask fewer awkward questions this year.",
                    "Happy birthday. You are officially old enough to pretend you are mature.",
                    "Keep being smart, funny and just naughty enough to stay interesting.",
                    "May your birthday be full of snacks, games and zero boring lectures.",
                    "Happy birthday, champion. Your family still reserves the right to embarrass you.",
                    "Grow taller, wiser and slightly less dramatic, if possible.",
                    "Happy birthday from the relative who knows you are the real boss of the family.",
                ],
            },
            {
                "key": "boy",
                "h2": "Birthday Wishes for Nephew Boy",
                "lines": [
                    "Happy birthday to our sweet boy. May you grow healthy, curious and full of joy.",
                    "Wishing my little nephew a day full of cake, balloons and happy family hugs.",
                    "May your childhood stay bright, playful and protected by everyone who loves you.",
                    "Happy birthday, little champ. Keep learning, laughing and asking your wonderful questions.",
                    "You make every family gathering cuter, louder and more alive.",
                    "May your toys be fun, your cake be yummy and your smile stay big.",
                    "Happy birthday to the boy who fills our home with tiny adventures.",
                    "Grow with courage, kindness and the confidence to be exactly yourself.",
                    "May your birthday be as magical as your imagination.",
                    "Happy birthday, beta. You are our little blessing with a big personality.",
                ],
            },
            {
                "key": "english",
                "h2": "Birthday Wishes for Nephew in English",
                "lines": [
                    "Happy birthday, dear nephew. May your day be bright and your year be even brighter.",
                    "Wishing you success, good health, happiness and the courage to follow your dreams.",
                    "You are a wonderful nephew and a very special part of our family.",
                    "May your birthday be filled with love, laughter and beautiful surprises.",
                    "Happy birthday. Keep believing in yourself and keep moving toward what matters.",
                    "I hope this year gives you confidence, peace and many reasons to celebrate.",
                    "You deserve a birthday that feels joyful from morning to night.",
                    "Happy birthday, nephew. May your future be blessed with love and opportunity.",
                    "Sending warm wishes for your special day and the year ahead.",
                    "May you always stay kind, strong and surrounded by people who care.",
                ],
            },
            {
                "key": "from_aunt",
                "h2": "Birthday Wishes for Nephew from Aunt",
                "lines": [
                    "Happy birthday from your aunt. You will always be one of my favourite reasons to smile.",
                    "Watching you grow has been a beautiful gift. I am so proud of you.",
                    "May your birthday bring all the love, fun and blessings you deserve.",
                    "You are not just my nephew, you are my little piece of joy in the family.",
                    "Happy birthday, beta. I hope this year treats you with kindness and success.",
                    "Auntie is sending you love, blessings and one extra excuse to eat cake.",
                    "May you always feel supported, understood and deeply loved.",
                    "Happy birthday to the nephew who makes family moments sweeter.",
                    "I am cheering for your dreams today and every day.",
                    "Stay thoughtful, stay brave and never forget how special you are to me.",
                ],
            },
            {
                "key": "from_uncle",
                "h2": "Birthday Wishes for Nephew from Uncle",
                "lines": [
                    "Happy birthday from your uncle. Keep your head high and your heart clean.",
                    "Wishing you strength, wisdom, good friends and a year full of progress.",
                    "You are growing into someone the whole family can be proud of.",
                    "Happy birthday, champ. Make good choices and enjoy the ride.",
                    "May this year bring you discipline for your goals and joy for your heart.",
                    "I hope you keep learning, keep laughing and keep showing up for yourself.",
                    "Happy birthday. You have more potential than you probably realise.",
                    "Celebrate today, then go build the kind of year you will remember.",
                    "You will always have my guidance, my blessings and my loudest cheers.",
                    "Happy birthday, nephew. Stay grounded, stay curious and stay kind.",
                ],
            },
            {
                "key": "quotes",
                "h2": "Birthday Quotes for Nephew",
                "lines": [
                    "A nephew is a little piece of childhood joy that grows into family pride.",
                    "The best birthday gift for a nephew is a heart that believes in him.",
                    "Nephews make families younger, brighter and a little more mischievous.",
                    "A nephew's birthday is a reminder that love can grow across generations.",
                    "Every nephew carries a new story for the family to celebrate.",
                    "Blessings for a nephew are really prayers for his courage, health and happiness.",
                    "The bond with a nephew is made of pride, laughter and quiet protection.",
                    "A birthday becomes sweeter when the family gathers around a loved child.",
                    "A nephew may grow taller than you, but he never grows out of your blessings.",
                    "Love for a nephew is simple, steady and impossible to measure.",
                ],
            },
            {
                "key": "caption",
                "h2": "Birthday Captions for Nephew",
                "lines": [
                    "Birthday cheers for the nephew who owns our hearts.",
                    "Family star, cake lover and birthday legend.",
                    "Watching you grow is the sweetest timeline.",
                    "Proud aunt and uncle energy today.",
                    "Another year of nephew magic.",
                    "Small boy, big smile, endless love.",
                    "Celebrating our favourite family champ.",
                    "Cake, hugs and one very loved nephew.",
                    "The birthday boy deserves the whole spotlight.",
                    "More joy to the nephew who makes life brighter.",
                ],
            },
            {
                "key": "whatsapp",
                "h2": "WhatsApp Birthday Messages for Nephew",
                "lines": [
                    "Happy birthday, beta. May your day be full of cake, blessings and laughter.",
                    "Wishing you a beautiful birthday and a year full of happy news.",
                    "Happy birthday, nephew. Stay healthy, stay kind and keep making us proud.",
                    "Lots of love from all of us. Enjoy your special day fully.",
                    "May God bless you with confidence, happiness and a bright future.",
                    "Happy birthday. Sending hugs, smiles and a little family mischief your way.",
                    "Have a wonderful birthday, champ. Call us after the cake cutting.",
                    "May your day be joyful and your year be peaceful.",
                    "Happy birthday to the most loved nephew in the family group.",
                    "Blessings and love for your new year of life.",
                ],
            },
            {
                "key": "gift",
                "h2": "A Thoughtful Birthday Gift for Your Nephew",
                "lines": [
                    "If your nephew likes simple style, choose a piece he can wear often instead of only on one occasion.",
                    "For a little nephew, a nazariya bracelet can feel protective, sweet and family approved.",
                    "For a teen or grown nephew, a clean bracelet or chain can feel more personal than a generic gift.",
                    "Pair the gift with one handwritten line so the gesture does not feel only material.",
                    "Choose comfort first. A birthday gift should suit his routine, age and personal style.",
                    "Avoid loud designs if he prefers quiet everyday pieces.",
                    "A soft keepsake works best when it feels like blessing, not pressure.",
                    "Keep the note simple: proud of you, love you, and wishing you a bright year.",
                    "Jewellery is optional. The real message is that you noticed what suits him.",
                    "Let the birthday wish lead, and let the gift quietly follow.",
                ],
            },
        ],
        "section_leads": {
            "Best Happy Birthday Wishes for Nephew": "Use these all-rounder wishes for cards, WhatsApp, calls and family captions.",
            "Short Birthday Wishes for Nephew": "Short lines work best when you want something quick, warm and easy to personalize.",
            "Heart Touching Birthday Wishes for Nephew": "Choose a deeper message when the bond is close or when you want the wish to feel memorable.",
            "Funny Happy Birthday Nephew Messages": "Funny wishes should feel affectionate, never mocking.",
            "Birthday Wishes for Nephew Boy": "These are gentle lines for a younger nephew, especially when the family wants something cute and blessing-led.",
            "Birthday Wishes for Nephew in English": "Use these clear English wishes when you want a polished line for a card or family group.",
            "Birthday Wishes for Nephew from Aunt": "Aunt wishes can be extra warm, proud and a little indulgent.",
            "Birthday Wishes for Nephew from Uncle": "Uncle wishes can balance affection with guidance and encouragement.",
            "Birthday Quotes for Nephew": "Use these as captions, card openers or speech lines.",
            "Birthday Captions for Nephew": "These captions are short enough for Instagram, stories and family photo posts.",
            "WhatsApp Birthday Messages for Nephew": "Keep WhatsApp messages simple, readable and family friendly.",
            "A Thoughtful Birthday Gift for Your Nephew": "Let the relationship decide the gift style, not the other way around.",
        },
        "faqs": [
            ["What are the best happy birthday wishes for nephew?", "The best happy birthday wishes for nephew are warm, specific and age appropriate. Mention his name, add one real quality you admire, and wish him health, confidence and happiness for 2026. Keep WhatsApp wishes short and save longer heartfelt notes for cards."],
            ["How do I write birthday wishes for nephew in English?", "Start with Happy birthday, dear nephew, then add one personal sentence about pride, love or blessings. Use simple English and avoid overdecorated wording. A good line is: Happy birthday, dear nephew. May your year be full of courage, joy and good people."],
            ["What should I write for a nephew boy's birthday?", "For a nephew boy, keep the message playful and blessing-led. Wish him cake, fun, health, learning and bright childhood memories. Lines about being a little champ, family star or sweet blessing work well for younger nephews."],
            ["Can birthday wishes for nephew be funny?", "Yes, funny birthday wishes work if your nephew enjoys jokes and the tone stays affectionate. Avoid teasing about sensitive things like appearance, studies or money. Light lines about cake, family mischief and being spoiled are safer."],
            ["What is a short birthday quote for nephew?", "A short birthday quote for nephew is: A nephew is family pride wrapped in laughter and love. It works for cards, captions and quick birthday posts because it feels warm without becoming too long."],
            ["Is jewellery a good birthday gift for a nephew?", "Jewellery can be a thoughtful birthday gift for a nephew when it suits his age and style. A kids nazariya bracelet can feel protective for a little nephew, while a simple bracelet or chain may suit a teen or adult nephew. Keep the wish as the emotional centre."],
        ],
    }

    config = {
        "rank": 82,
        "sections_json": f"output/{prefix}_sections.json",
        "output_prefix": prefix,
        "carousel_id": "bs-cf-nephewbirthday",
        "occasion_year": "Birthday Wishes for Nephew 2026",
        "carousel_alt_prefix": "happy birthday wishes for nephew 2026 gift idea",
        "gift_h2": "Birthday Gift Ideas That Still Feel Personal",
        "gift_blurb": "If the birthday wish is the heart of the moment, a small keepsake can become the reminder he carries forward. These six approved BlueStone designs stay age-aware, clean and giftable, with no prices in the article.",
        "conclusion_html": "The best happy birthday wishes for nephew sound like they came from your own family table. Pick a line, add his name, and let the message carry pride, blessings and a little birthday mischief into 2026.",
        "schema_keywords": [
            "happy birthday wishes for nephew",
            "happy birthday nephew",
            "birthday wishes for nephew in english",
            "birthday quotes for nephew",
            "birthday wishes for nephew boy",
        ],
        "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
        "products": [
            product(rows, "The Novare Evil Eye Kids Nazariya Bracelet", "Kids Bracelets"),
            product(rows, "The Fonseca Bracelet For Him", "Bracelet"),
            product(rows, "The Concatenate Bracelet For Him", "Bracelet"),
            product(rows, "The Amandine Bracelet For Him", "Bracelet"),
            product(rows, "The Bandhan Bracelet For Him", "Bracelet"),
            product(rows, "The Chevalier Gold Chain", "Chains"),
        ],
        "flatlay_insert_h2": "Birthday Wishes for Nephew Boy",
        "lifestyle_insert_h2": "A Thoughtful Birthday Gift for Your Nephew",
        "more_reads_html": "Read more family birthday ideas in <a href=\"https://blog.bluestone.com/happy-birthday-big-brother-2026/\">happy birthday big brother 2026</a>, <a href=\"https://blog.bluestone.com/happy-birthday-wishes-for-uncle-2026/\">happy birthday wishes for uncle 2026</a>, <a href=\"https://blog.bluestone.com/birthday-wishes-for-cousin-brother-sister-2026/\">birthday wishes for cousin 2026</a>, and <a href=\"https://blog.bluestone.com/sorry-for-late-wishes-2026/\">sorry for late wishes 2026</a>. For cultural context, see <a href=\"https://en.wikipedia.org/wiki/Birthday\">birthday traditions</a>.",
        "how_to_html": "To choose the right birthday wish for your nephew, match the line to his age and your relationship. Use a cute blessing for a young boy, a funny line for a playful teen, and a proud heartfelt note for a grown nephew. Add one personal detail before sending.",
        "faq_h2": "Frequently Asked Questions about Birthday Wishes for Nephew",
        "min_lines": 100,
        "section_leads": sections["section_leads"],
    }

    people_negative = (
        "floating jewellery overlay, giant bracelet collage, product cutout over people, packshot composited on lifestyle photo, "
        "oversized jewellery, jewellery enlarged for visibility, wrong gender wearer, watches, extra bracelets, rings, earrings, "
        "necklaces, readable text, logos, distorted hands, cropped faces, dark skin, deep brown skin, heavily tanned skin, illustration, CGI"
    )
    product_negative = (
        "hands, people, floating overlays, cutouts, incorrect bracelet design, distorted links, readable text, logos, price tags, "
        "brand marks on props, blown whites, HDR glare, illustration, CGI"
    )

    prompts = {
        "rank": 82,
        "slug": "birthday-wishes-for-nephew-2026",
        "output_prefix": prefix,
        "occasion": "Birthday Wishes for Nephew 2026",
        "primary_kw": "happy birthday wishes for nephew",
        "caption_occasion": "Happy birthday wishes for nephew 2026",
        "caption_year": "2026",
        "flatlay_setting": "cafe-tray",
        "workflow": "Higgsfield MCP nano_banana_pro. Campaign hybrid with mandatory body_image scale line. Do not generate until balance succeeds. Max 2 concurrent generations for this workflow.",
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/birthday-wishes-for-nephew-hero-2026.webp",
            "flatlay": "output/magnific_generated/birthday-wishes-for-nephew-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/birthday-wishes-for-nephew-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "happy birthday wishes for nephew 2026 hero The Fonseca Bracelet For Him",
            "flatlay": "happy birthday wishes for nephew 2026 flatlay The Concatenate Bracelet For Him",
            "lifestyle": "happy birthday wishes for nephew 2026 lifestyle The Novare Evil Eye Kids Nazariya Bracelet",
        },
        "schema_keywords": config["schema_keywords"],
        "slots": {
            "hero": {
                "code": "BIPO0945V20",
                "name": "The Fonseca Bracelet For Him",
                "gender": "Male",
                "height_mm": 11.52,
                "width_mm": 190.5,
                "size_prompt_note": "bracelet cross-section height 11.52 mm and bracelet length 190.5 mm; product dimensions, not face size; copy wrist scale from body_image",
                "alt": "happy birthday wishes for nephew 2026 hero with The Fonseca Bracelet For Him",
                "caption": "Happy birthday wishes for nephew 2026 vibe: The Fonseca Bracelet For Him",
                "product": {"code": "BIPO0945V20", "name": "The Fonseca Bracelet For Him", "pdp": rows["The Fonseca Bracelet For Him"]["Link"]},
                "cdn": [
                    "https://kinclimg9.bluestone.com/giproduct/BIPO0945V20_YAA18DIG6SYSBXXXX_ABCD00-BP-PICS-00000-1024-87481.png",
                    "https://kinclimg9.bluestone.com/giproduct/BIPO0945V20_YAA18DIG6SYSBXXXX_ABCD00-PICS-00000-1024-87481.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Bracelets/The Fonseca Bracelet For Him/1_body_portrait.png",
                    "ProductImages/raw/Bracelets/The Fonseca Bracelet For Him/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": (
                    "Photoreal candid lifestyle photograph with high-end jewellery commercial fidelity on the worn piece only. Natural skin texture, controlled soft key light, gentle fill, realistic shadows, proper shallow depth of field at 85mm, balanced exposure, no blown whites, no HDR glare, DSLR, HD, 16:9 with safe margins.\n\n"
                    "Casting required: fair-skinned Indian young adult man as the nephew, with one fair-skinned Indian older aunt or uncle partly in scene. Light wheatish to fair urban Indian complexions. The young adult man is the clear wearer.\n\n"
                    "Happy birthday wishes for nephew 2026 candid home birthday mid-shot, a young adult nephew smiles while receiving a blank cream birthday card beside a small cake. Faces and upper bodies fill most of the frame. No readable text.\n\n"
                    "The young adult man physically wears The Fonseca Bracelet For Him from @img1 body_image and @img2 design on his wrist. GENDER LOCK: Male product on adult man only. Product dimensions from PDP: bracelet cross-section height_mm=11.52 and bracelet length_mm=190.5. These are real product dimensions, NOT face-size instructions. Keep the bracelet size on the wrist like @img1 body_image worn wrist scale. Use @img2 only for the jewellery design. Do not make it bigger for visibility.\n\n"
                    "Replicate the polished yellow gold link bracelet with rectangular diamond-studded centre panel and woven chain links exactly. HD hyperreal metal and stones, 100 percent identical to refs, zero distortion. This bracelet is the single and only jewellery in the image. Other people wear absolutely no jewellery. Jewellery touches skin with a soft contact shadow and is never a floating cutout.\n\n"
                    f"Avoid: {people_negative}."
                ),
            },
            "flatlay": {
                "code": "BISV0910V22",
                "name": "The Concatenate Bracelet For Him",
                "gender": "Male",
                "height_mm": 203.2,
                "width_mm": 8.5,
                "size_prompt_note": "bracelet length 203.2 mm and link width 8.5 mm; product dimensions, not face size",
                "alt": "happy birthday wishes for nephew 2026 flatlay with The Concatenate Bracelet For Him",
                "caption": "Happy birthday wishes for nephew 2026 keepsake: The Concatenate Bracelet For Him",
                "product": {"code": "BISV0910V22", "name": "The Concatenate Bracelet For Him", "pdp": rows["The Concatenate Bracelet For Him"]["Link"]},
                "cdn": [
                    "https://kinclimg1.bluestone.com/giproduct/BISV0910V22_YAA18DIG6XXXXXXXX_ABCD00-PICS-00000-1024-81503.png",
                    "https://kinclimg1.bluestone.com/giproduct/BISV0910V22_YAA18DIG6XXXXXXXX_ABCD00-PICS-00002-1024-81503.png",
                    "https://kinclimg1.bluestone.com/giproduct/BISV0910V22_YAA18DIG6XXXXXXXX_ABCD00-PICS-00003-1024-81503.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Bracelets/The Concatenate Bracelet For Him/0_primary.png",
                    "ProductImages/raw/Bracelets/The Concatenate Bracelet For Him/2_side_1.png",
                    "ProductImages/raw/Bracelets/The Concatenate Bracelet For Him/3_back.png",
                ],
                "ref_roles": ["primary", "side", "back"],
                "prompt": (
                    "Photoreal high-end jewellery still life, top-down editorial product flatlay, controlled soft key light, realistic gentle shadows, shallow depth of field, HD metal and stone detail, 16:9 landscape.\n\n"
                    "Happy birthday wishes for nephew 2026 top-down flatlay. Flatlay setting ID: cafe-tray. Surface and props: warm ceramic tray on a clean table, plain espresso cup, folded neutral napkin, small blank cream birthday card with no readable text, and one closed matte gift box with no logo.\n\n"
                    "The identical Concatenate Bracelet For Him from @img1, @img2 and @img3 rests naturally on the tray at true PDP scale. Product dimensions from PDP: bracelet length_mm=203.2 and link_width_mm=8.5. These are product dimensions, NOT face-size instructions. Do not enlarge for visibility. Full bracelet visible, polished yellow gold interlocking links, rectangular diamond centre plate, crisp clasp detail, 100 percent identical design, zero distortion.\n\n"
                    "Props stay secondary and quiet. No people, no hands, no readable text, no brand marks. Jewellery is the clear subject but still true to real size.\n\n"
                    f"Avoid: {product_negative}."
                ),
            },
            "lifestyle": {
                "code": "BIAV1005V201",
                "name": "The Novare Evil Eye Kids Nazariya Bracelet",
                "gender": "Kids",
                "height_mm": 6,
                "width_mm": 127,
                "size_prompt_note": "kids bracelet length 127 mm and motif height 6 mm; product dimensions, not face size; copy wrist scale from body_image",
                "alt": "happy birthday wishes for nephew 2026 lifestyle with The Novare Evil Eye Kids Nazariya Bracelet",
                "caption": "Happy birthday wishes for nephew 2026 vibe: The Novare Evil Eye Kids Nazariya Bracelet",
                "product": {"code": "BIAV1005V201", "name": "The Novare Evil Eye Kids Nazariya Bracelet", "pdp": rows["The Novare Evil Eye Kids Nazariya Bracelet"]["Link"]},
                "cdn": [
                    "https://kinclimg4.bluestone.com/giproduct/BIAV1005V201_YAA14BEEYXXXXXXXX_ABCD00-BP-PICS-00000-1024-115872.png",
                    "https://kinclimg4.bluestone.com/giproduct/BIAV1005V201_YAA14BEEYXXXXXXXX_ABCD00-PICS-00000-1024-115872.png",
                ],
                "local_reference_images": [
                    "ProductImages/raw/Kids Bracelets/The Novare Evil Eye Kids Nazariya Bracelet/1_body_portrait.png",
                    "ProductImages/raw/Kids Bracelets/The Novare Evil Eye Kids Nazariya Bracelet/0_primary.png",
                ],
                "ref_roles": ["body_image", "front_primary"],
                "prompt": (
                    "Photoreal candid lifestyle photograph with high-end jewellery commercial fidelity on the worn piece only. Natural skin texture, controlled soft key light, gentle fill, realistic shadows, proper shallow depth of field at 85mm, balanced exposure, no blown whites, no HDR glare, DSLR, HD, 16:9 with safe margins.\n\n"
                    "Casting required: fair-skinned Indian little boy nephew with one fair-skinned Indian adult family hand partly visible only for birthday context. Light wheatish to fair Indian complexions. The child is the clear wearer.\n\n"
                    "Happy birthday wishes for nephew 2026 close lifestyle moment, a little boy reaches toward a small birthday cupcake on a clean family table while a blank birthday card sits nearby. His face is joyful and fully visible. No readable text.\n\n"
                    "The little boy physically wears The Novare Evil Eye Kids Nazariya Bracelet from @img1 body_image and @img2 design on his wrist. GENDER LOCK: Kids product on child only. Product dimensions from PDP: kids bracelet length_mm=127 and motif_height_mm=6. These are real product dimensions, NOT face-size instructions. Keep the bracelet size on the child wrist like @img1 body_image worn wrist scale. Use @img2 only for the jewellery design. Do not make it bigger for visibility.\n\n"
                    "Replicate the delicate black and yellow gold nazariya bracelet with small blue evil eye centre exactly. HD hyperreal metal, bead and enamel detail, 100 percent identical to refs, zero distortion. This bracelet is the single and only jewellery in the image. No other jewellery on the child or adult. Jewellery touches skin with a soft contact shadow and is never a floating cutout.\n\n"
                    f"Avoid: {people_negative}."
                ),
            },
        },
    }

    checklist = """# Checklist v2: Rank 82 Nephew Birthday

- [x] New blog only, old Optimize URL treated as reference.
- [x] Primary keyword in intro, meta, title and hero alt.
- [x] Supporting keywords mapped to H2s and FAQs.
- [x] No prices, no old years, no duplicate content H1.
- [x] Type 2 carousel uses approved SEO images only.
- [x] Type 3 prompts use body_image for people slots and category-correct product dimensions.
- [x] Flatlay setting rotated to cafe-tray.
"""

    write_json(f"output/{prefix}_sections.json", sections)
    write_json(f"output/publish_configs/rank82.json", config)
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    (ROOT / f"output/{prefix}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
