#!/usr/bin/env python3
"""Build Week 3-4 Rank 106 friends Instagram comments article assets."""
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
    prefix = "Week34_Rank106_FriendsInstagramComments"
    rank = 106
    slug = "bestie-captions-for-instagram-2026"
    focus_kw = "good comments for friends pictures on instagram"
    title = "Good Comments for Friends Pictures on Instagram 2026"
    meta_desc = "Good comments for friends pictures on Instagram 2026 with short, funny, cute, stylish, best comments on friends photos, and Instagram comments for friends."
    keywords = [
        "good comments for friends pictures on instagram",
        "instagram comments for friends",
        "best comments on friends photos",
    ]

    hero = consolidated(rows, "The Lumeelle Cluster Pendant")
    flat = consolidated(rows, "The Rafia Ring")
    life = consolidated(rows, "The Asya Huggie Earrings")

    sections = [
        sec("main_comments", "Good Comments for Friends Pictures on Instagram", [
            "This picture has best friend energy written all over it.",
            "You make every frame look warmer and happier.",
            "This photo is proof that friendship has its own glow.",
            "The smile, the vibe, the confidence, everything is perfect.",
            "A picture this happy deserves all the love.",
            "Your photo just made my feed brighter.",
            "Best friend looks, main character mood.",
            "This is the kind of picture that feels like a good memory.",
            "You look effortlessly happy and beautifully yourself.",
            "The friendship glow is real in this one.",
            "Saving this picture under pure joy.",
            "This photo deserves a permanent spot on the happy side of Instagram.",
        ]),
        sec("instagram_comments_for_friends", "Instagram Comments for Friends", [
            "My favourite human looking iconic again.",
            "This is exactly why your posts need a warning for too much charm.",
            "You are the reason this feed has personality.",
            "Friendship looks so good on you.",
            "The confidence is quiet, but the impact is loud.",
            "You did not post a picture. You posted a whole mood.",
            "My timeline needed this level of happiness.",
            "This smile could fix anyone's day.",
            "You make casual look unforgettable.",
            "The best friend glow is unbeatable.",
            "This is the kind of post that gets instant love.",
            "You look like the main reason the group chat is alive.",
        ]),
        sec("best_comments_friends_photos", "Best Comments on Friends Photos", [
            "Best comments on friends photos should sound warm, real, and a little personal.",
            "This picture is giving happiness, confidence, and bestie magic.",
            "The whole photo feels like sunshine and good company.",
            "Your smile is the highlight of this post.",
            "This is a perfect mix of cute, classy, and confident.",
            "A friend like you makes every picture feel special.",
            "This photo has the kind of energy people remember.",
            "You look comfortable, happy, and completely glowing.",
            "The caption may be short, but this picture says everything.",
            "Your vibe is doing all the talking here.",
            "This post deserves applause from the entire friend circle.",
            "One photo, endless best friend appreciation.",
        ]),
        sec("short", "Short Comments for Friends Pictures", [
            "Too good.",
            "Bestie glow.",
            "Pure charm.",
            "Iconic as always.",
            "Main character.",
            "Feed favourite.",
            "Picture perfect.",
            "Happy looks good.",
            "Too cute.",
            "Always shining.",
            "Best vibe.",
            "Instant favourite.",
        ]),
        sec("funny", "Funny Comments for Friends Pictures", [
            "Please leave some good photos for the rest of us.",
            "This much confidence should be illegal.",
            "Posting fire and pretending it is casual.",
            "I know the behind-the-scenes story, but I will behave.",
            "Bestie, the camera clearly has favourites.",
            "This picture called me underdressed.",
            "Your face card is working overtime.",
            "I came, I saw, I commented dramatically.",
            "The group chat needs to discuss this slay immediately.",
            "Not you making a normal day look premium.",
            "This post is why I cannot compete with my friends.",
            "Someone tell Instagram to give this photo a crown.",
        ]),
        sec("cute", "Cute Comments for Friends Pictures", [
            "You look like happiness in human form.",
            "This picture is soft, sweet, and so you.",
            "Your smile makes the whole post feel brighter.",
            "Cutest person on my feed today.",
            "A little sunshine, a little sparkle, all bestie.",
            "This photo feels like a hug from a friend.",
            "You look happy, and that is my favourite thing.",
            "The sweetest smile with the warmest vibe.",
            "This is adorable in the most natural way.",
            "Your joy is the best part of this picture.",
            "Soft smile, kind energy, perfect post.",
            "This photo has comfort and cuteness together.",
        ]),
        sec("stylish", "Stylish Comments for Friends Pictures", [
            "The styling, the pose, the confidence, everything works.",
            "This look deserves its own appreciation post.",
            "You make style look effortless.",
            "Classy, confident, and completely photo-ready.",
            "The outfit is speaking, and the attitude agrees.",
            "A stylish picture with an even better vibe.",
            "This is how you make a simple post feel editorial.",
            "Your style always knows what it is doing.",
            "Every detail in this photo feels polished.",
            "The elegance is natural and the confidence is clear.",
            "This look belongs on a mood board.",
            "Style level: best friend with main character timing.",
        ]),
        sec("girl_best_friend", "Comments for Girl Best Friend Pictures", [
            "My best girl looking beautiful as always.",
            "You carry happiness like it was made for you.",
            "This picture is sweet, strong, and so naturally pretty.",
            "Best friend, you are glowing in every possible way.",
            "Your smile deserves its own fan club.",
            "This photo has beauty and bestie energy together.",
            "You look like the reason good memories happen.",
            "The prettiest person with the kindest heart.",
            "Always proud to hype this beautiful human.",
            "This is exactly why you are the favourite in every photo.",
            "Your picture just made the whole feed softer.",
            "A best friend like you makes every day better.",
        ]),
        sec("boy_best_friend", "Comments for Boy Best Friend Pictures", [
            "Brother energy, best friend loyalty, perfect picture.",
            "Looking sharp, confident, and fully in your zone.",
            "This picture has solid best friend legend vibes.",
            "You make casual look cooler than it should.",
            "Respectfully, this post is a win.",
            "The confidence is clean and the smile is real.",
            "Best friend looking like the calmest main character.",
            "This photo has the exact energy of a good day.",
            "Always showing up with effortless style.",
            "This one deserves all the likes from the group.",
            "Good picture, great friend, best memories.",
            "The brother from another mother glow is strong here.",
        ]),
        sec("squad", "Comments for Friends Group Photos", [
            "This group photo has too many good memories in one frame.",
            "The squad energy is unbeatable here.",
            "Friendship looks loud, happy, and perfect in this picture.",
            "This frame deserves a place in the memory folder.",
            "Every smile in this photo has a story behind it.",
            "The best kind of chaos captured beautifully.",
            "A picture full of people who make life lighter.",
            "This is what good company looks like.",
            "Group photo, golden mood, unforgettable people.",
            "The friendship chemistry is doing all the work.",
            "This picture feels like a whole chapter of memories.",
            "A perfect reminder that the right people make everything better.",
        ]),
        sec("gift_notes", "Friendship Gift Note Ideas for Instagram Friends", [
            "For the friend who makes every picture and every memory better.",
            "A small keepsake for the person I always want to hype up.",
            "Wear this as a reminder that your friendship makes life brighter.",
            "For the bestie whose photos deserve love and whose heart deserves more.",
            "A little sparkle for the friend who brings the best energy.",
            "For every candid, every comment, and every memory we keep.",
            "Choose a gift that feels as natural as your friendship.",
            "Keep the note short, warm, and specific to the friend.",
            "A thoughtful jewellery note can turn an Instagram memory into a real keepsake.",
            "Pair the comment with a gift when the friendship deserves something lasting.",
            "The best gift note sounds personal, not copied.",
            "Let the message celebrate the friend, not just the photo.",
        ]),
    ]

    prompts = {
        "rank": "Week3-4 Rank 106",
        "slug": slug,
        "primary_kw": focus_kw,
        "output_prefix": prefix,
        "caption_occasion": "Good comments for friends pictures on Instagram",
        "caption_year": "2026",
        "flatlay_setting": "cafe-tray",
        "workflow": "Higgsfield CLI nano_banana_pro. People shots require @img1 body_image plus @img2 design. Max 2 concurrent generations total. If queue/generation error occurs, wait 40-50 seconds before retry. No visible screens/devices/cards/boards/readable text. No competitor URL was present in the sheet row, so content uses the plan keyword cluster per guide.",
        "higgsfield_jobs": {},
        "higgsfield": {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1},
        "insert_h2s_json": f"output/{prefix}_insert_h2s.json",
        "product_media_json": f"output/{prefix}_product_media.json",
        "output": {
            "hero": "output/magnific_generated/bestie-captions-for-instagram-hero-2026.webp",
            "flatlay": "output/magnific_generated/bestie-captions-for-instagram-flatlay-2026.webp",
            "lifestyle": "output/magnific_generated/bestie-captions-for-instagram-lifestyle-2026.webp",
        },
        "media_titles": {
            "hero": "good comments for friends pictures on Instagram 2026 hero with The Lumeelle Cluster Pendant",
            "flatlay": "good comments for friends pictures on Instagram 2026 flatlay with The Rafia Ring",
            "lifestyle": "good comments for friends pictures on Instagram 2026 lifestyle with The Asya Huggie Earrings",
        },
        "schema_keywords": keywords,
        "slots": {
            "hero": slot(
                hero,
                "good comments for friends pictures on Instagram 2026 hero with The Lumeelle Cluster Pendant",
                "Good comments for friends pictures on Instagram 2026 mood: The Lumeelle Cluster Pendant",
                [raw_image("Pendants", "The Lumeelle Cluster Pendant", "1_body_portrait.png"), raw_image("Pendants", "The Lumeelle Cluster Pendant", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Good comments for friends pictures on Instagram 2026 friendship hero",
                    scene="solo fair-skinned Indian adult woman in a cream kurta smiling warmly in a sunlit cafe-style home corner with flowers, ceramic cups, folded fabric and a wrapped gift box, camera pulled back upper-body medium portrait, full head and hairline visible, neck and pendant clearly visible, hands fully out of frame, no phone, no camera screen, no photo print, no paper facing camera, plain background with no signage",
                    product_name="The Lumeelle Cluster Pendant",
                    product=hero,
                    body_part="neck",
                    extra_negatives="visible hands, rings, bracelet, bangle, watch, large pendant, extra necklace, background people wearing jewellery, phone in hand, selfie pose, camera, laptop, tablet, social media screen, photo print, signage, letters, numbers, readable notebook, readable book, poster, board, white blank card",
                ),
            ),
            "flatlay": slot(
                flat,
                "good comments for friends pictures on Instagram 2026 cafe tray flatlay with The Rafia Ring",
                "Good comments for friends pictures on Instagram 2026 detail: The Rafia Ring",
                [raw_image("Rings", "The Rafia Ring", "0_primary.png"), raw_image("Rings", "The Rafia Ring", "2_front.png"), raw_image("Rings", "The Rafia Ring", "6_angle.png")],
                ["primary", "front", "angle"],
                prompt_flatlay(
                    occasion="Good comments for friends pictures on Instagram 2026 friendship keepsake",
                    setting="cafe-tray",
                    setting_prompt="warm cafe tray with ceramic cups, jasmine flowers, ribbon, folded cream fabric placed away from the jewellery, a small wrapped gift box and a closed book turned away at the edge. The ring rests directly on the wooden tray as a small finger ring, not around fabric or any object, not a napkin ring, not a bracelet, not a cuff. No visible phone, no laptop, no photo print, no readable text, no card facing camera",
                    product_name="The Rafia Ring",
                    product=flat,
                ),
            ),
            "lifestyle": slot(
                life,
                "good comments for friends pictures on Instagram 2026 lifestyle with The Asya Huggie Earrings",
                "Good comments for friends pictures on Instagram 2026 look: The Asya Huggie Earrings",
                [raw_image("Earrings", "The Asya Huggie Earrings", "1_body_portrait.png"), raw_image("Earrings", "The Asya Huggie Earrings", "0_primary.png")],
                ["body_image", "front_primary"],
                prompt_people(
                    occasion="Good comments for friends pictures on Instagram 2026 lifestyle",
                    scene="solo fair-skinned Indian adult woman laughing softly beside a cafe table with flowers, ceramic cup, folded cream fabric and a wrapped gift box, full head visible and both ears visible, cream blouse, no necklace, wrists and hands out of frame, warm clean background with no phone, no screens, no photo prints and no readable objects",
                    product_name="The Asya Huggie Earrings",
                    product=life,
                    body_part="ear",
                    extra_negatives="necklace, bracelet, ring, watch, phone, laptop, tablet, camera, social media screen, selfie pose, photo print, planner, calendar, readable notebook, readable book, poster, board, blank card, second person",
                ),
            ),
        },
    }

    write_json(
        f"output/{prefix}_sections.json",
        {
            "meta": {"title": title, "slug": slug, "meta_desc": meta_desc, "focus_kw": focus_kw, "yoast_title": title},
            "intro": [
                "Good comments for friends pictures on Instagram should feel quick, warm, and natural. This 2026 collection includes Instagram comments for friends, best comments on friends photos, short comments, funny lines, cute comments, stylish compliments, group photo comments, and friendship gift-note ideas.",
                "TL;DR: Use a short comment for quick hype, a funny comment for close besties, a cute comment for soft pictures, a stylish comment for outfit posts, and a group-photo line when the whole squad deserves love.",
            ],
            "sections": sections,
            "faqs": [
                ("What are good comments for friends pictures on Instagram?", "Good comments for friends pictures on Instagram are short, warm, and specific lines that appreciate the photo, the smile, the outfit, or the friendship behind the post."),
                ("What are the best Instagram comments for friends?", "The best Instagram comments for friends feel natural and personal. Use a line that matches the picture, such as a cute compliment for a soft photo or a funny comment for a close bestie."),
                ("How do I write best comments on friends photos?", "To write best comments on friends photos, mention one clear thing you like: the smile, outfit, mood, confidence, group vibe, or memory. Keep it honest and easy to read."),
                ("Can I use funny comments on friends pictures?", "Yes. Funny comments work well when you know the friend closely. Keep the humour kind, avoid anything embarrassing, and choose a line that feels like your real friendship."),
                ("What should I comment on a girl best friend's picture?", "Comment on her smile, confidence, style, or happy energy. A warm line like your smile makes the whole post brighter feels sweet without being too formal."),
                ("Can friendship comments be used with gift notes?", "Yes. A friendship comment can become a short gift note when it is personal and warm. Pair it with a small keepsake when you want the memory to feel lasting."),
            ],
        },
    )
    write_json(
        f"output/publish_configs/week34_rank{rank}.json",
        {
            "rank": "Week3-4 Rank 106",
            "sections_json": f"output/{prefix}_sections.json",
            "output_prefix": prefix,
            "carousel_id": "bs-cf-friendcomments",
            "occasion_year": "Good comments for friends pictures on Instagram 2026",
            "carousel_alt_prefix": "good comments for friends pictures on Instagram 2026 gift idea",
            "gift_h2": "Friendship Gift Ideas for Instagram Friends",
            "gift_blurb": "A sweet comment can make a friend's post feel special, and a keepsake can make the memory last longer. These BlueStone pieces pair well with bestie captions, Instagram comments for friends, and thoughtful friendship notes.",
            "conclusion_html": "Good comments for friends pictures on Instagram work best when they sound like your real friendship. Choose a short comment for quick hype, a funny line for close besties, and a warm note when the picture reminds you of a memory worth keeping.",
            "schema_keywords": keywords,
            "type3_prompts_json": f"output/{prefix}_type3_prompts.json",
            "products": [
                product(rows, "The Melene Evil Eye Pendant"),
                product(rows, "The Malibu Ring"),
                product(rows, "The Pervinca Charm Holder Bracelet"),
                product(rows, "The Pear Evil Eye Toggle Bangle"),
                product(rows, "The Kricia Charm Bracelet"),
                product(rows, "The Faliha Purse Hoop Earrings"),
            ],
            "flatlay_insert_h2": "Best Comments on Friends Photos",
            "lifestyle_insert_h2": "Friendship Gift Note Ideas for Instagram Friends",
            "more_reads_html": 'Read more friendship-friendly lines in <a href="https://blog.bluestone.com/good-times-caption-2026/">good times caption</a>, <a href="https://blog.bluestone.com/unity-quotes-2026/">unity quotes</a>, <a href="https://blog.bluestone.com/farewell-message-for-seniors-2026/">farewell message for seniors</a>, and <a href="https://blog.bluestone.com/busy-people-quotes-2026/">busy people quotes</a>.',
            "how_to_html": "Match the comment to the photo before posting. Use cute lines for smiling pictures, stylish lines for outfit photos, funny comments for close friends, and group-photo comments when the whole squad is in frame.",
            "faq_h2": "Frequently Asked Questions about Good Comments for Friends Pictures on Instagram",
            "min_lines": 120,
        },
    )
    write_json(f"output/{prefix}_type3_prompts.json", prompts)
    checklist(prefix, rank, title, focus_kw, False)
    print(f"Built {prefix} with {sum(len(s['lines']) for s in sections)} shareable lines and supporting keywords mapped")


if __name__ == "__main__":
    main()
