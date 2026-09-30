#!/usr/bin/env python3
"""Build Rank 84 New Year friends article assets."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Week1_Rank84_NewYearFriends"


def load_products():
    with (ROOT / "Seo Products - final products (1).csv").open(newline="", encoding="utf-8-sig") as f:
        return {row["Design Name"].strip(): row for row in csv.DictReader(f)}


def product(rows, name, category):
    row = rows[name]
    return {
        "code": row["Design Code"],
        "name": name,
        "url": row["Link"],
        "png": f"ProductImages/seo images/{category}/{name}.png",
    }


def main():
    rows = load_products()
    sections = {
        "meta": {
            "title": "Heart Touching New Year Wishes for Friends 2027",
            "slug": "heart-touching-new-year-wishes-for-friends-2027",
            "meta_desc": "Find heart touching New Year wishes for friends 2027, funny messages, love quotes, girlfriend wishes, boyfriend wishes, captions, and warm notes to send.",
            "focus_kw": "heart touching new year wishes for friends",
            "yoast_title": "Heart Touching New Year Wishes for Friends 2027"
        },
        "intro": [
            "Heart touching New Year wishes for friends should sound warm, hopeful, and easy to forward. Use these 2027 lines for WhatsApp, Instagram captions, greeting cards, group chats, or a private note to someone who made the year lighter.",
            "TL;DR: choose a short wish for chats, a longer message for close friends, a funny line for your group, and a romantic New Year wish only when the relationship already has that tone."
        ],
        "sections": [
            {
                "h2": "Best Heart Touching New Year Wishes for Friends 2027",
                "lines": [
                    "Happy New Year 2027, my friend. May this year bring you peace, courage, good health, and the kind of happiness that stays quietly with you.",
                    "A new year feels better because I know I am walking into it with a friend like you. May 2027 be gentle, bright, and full of good surprises.",
                    "Thank you for being part of my ordinary days and my difficult ones. Wishing you a New Year filled with strength and beautiful moments.",
                    "May 2027 give you reasons to smile, people who understand you, and dreams that slowly become real.",
                    "Happy New Year to the friend who made last year easier. I hope the coming year is kinder to you in every way.",
                    "May this New Year bring fresh hope to your heart and quiet confidence to every step you take.",
                    "I am grateful for your friendship, your honesty, and the way you show up. Happy New Year 2027.",
                    "May the year ahead heal what was heavy and open doors that feel right for you.",
                    "Happy New Year, dear friend. May you find more peace, more laughter, and more reasons to believe in yourself.",
                    "Here is to another year of friendship, memories, and standing by each other without needing perfect words."
                ]
            },
            {
                "h2": "New Year Wishes for Friends",
                "lines": [
                    "Happy New Year, friend. May your days be lighter and your dreams feel closer.",
                    "Wishing you a year full of good health, real joy, and peaceful mornings.",
                    "May 2027 bring you new chances, better energy, and people who value you.",
                    "Happy New Year to someone who makes friendship feel easy and true.",
                    "May this year give you courage for hard days and gratitude for good ones.",
                    "Wishing you laughter that comes easily and success that feels meaningful.",
                    "May your heart stay hopeful and your plans move in the right direction.",
                    "Happy New Year. I hope this year treats you with kindness.",
                    "May every month of 2027 bring one beautiful reason to celebrate.",
                    "Thank you for being my friend. Wishing you a warm and wonderful New Year."
                ]
            },
            {
                "h2": "Happy New Year My Love",
                "lines": [
                    "Happy New Year, my love. May 2027 bring us closer, softer, and stronger together.",
                    "Starting another year with you in my heart feels like the best blessing.",
                    "May this New Year give us more honest talks, quiet comfort, and memories we will keep.",
                    "Happy New Year, my love. Thank you for being my calm place and my happiest thought.",
                    "I hope 2027 gives you everything you deserve, and gives us more reasons to smile together.",
                    "With you, even a new beginning feels familiar and safe. Happy New Year.",
                    "May our love grow with patience, laughter, and little everyday moments.",
                    "Happy New Year to the person who makes my heart feel at home.",
                    "I do not need a perfect year, I just want a year where we keep choosing each other.",
                    "May 2027 be kind to you, to me, and to the love we are building."
                ]
            },
            {
                "h2": "A Soft New Year Gift Idea",
                "lines": [
                    "A New Year note already says a lot, but a small keepsake can make it feel more personal.",
                    "For friends, choose something wearable and easy, not too formal or too loud.",
                    "For love, a pendant, ring, bracelet, or pair of earrings can quietly mark a new beginning.",
                    "Keep the gift message warm and simple so the feeling stays ahead of the product.",
                    "Choose designs that suit their everyday style and routine.",
                    "Avoid prices in the note and let the gesture feel thoughtful.",
                    "A good keepsake says, I want this year to be good to you.",
                    "The best gift is the one they can wear beyond New Year's week."
                ]
            },
            {
                "h2": "New Year Wishes for BF",
                "lines": [
                    "Happy New Year, my love. May 2027 bring you success, health, and the confidence to chase what matters.",
                    "I am proud of you and excited to see what this year brings for you.",
                    "May your year be strong, peaceful, and full of wins that feel personal.",
                    "Happy New Year to the one who makes my days warmer.",
                    "I hope 2027 gives you rest when you need it and courage when life asks for more.",
                    "May we support each other better and laugh even more this year.",
                    "Happy New Year, boyfriend. Thank you for being my favourite person to talk to.",
                    "May your dreams move closer and your heart stay light.",
                    "I hope this year brings us more memories, more trust, and more quiet happiness.",
                    "Happy New Year. I am lucky to begin another year with you."
                ]
            },
            {
                "h2": "New Year Wishes for Girlfriend",
                "lines": [
                    "Happy New Year, my beautiful girl. May 2027 bring you peace, joy, and everything your heart is hoping for.",
                    "You made last year sweeter. I hope this New Year gives you all the love you give so freely.",
                    "May your smile stay bright and your dreams feel closer with every month.",
                    "Happy New Year to the girl who makes ordinary days feel special.",
                    "I hope 2027 is gentle with you and generous with your dreams.",
                    "May we grow with more trust, more laughter, and more little memories.",
                    "Happy New Year, love. I am grateful for your care, your patience, and your heart.",
                    "May this year bring you confidence, comfort, and reasons to feel proud of yourself.",
                    "I hope every new beginning this year feels a little easier because we have each other.",
                    "Happy New Year, girlfriend. You are my favourite part of every year."
                ]
            },
            {
                "h2": "New Year Wishes for GF",
                "lines": [
                    "Happy New Year, GF. May this year be as soft and bright as your smile.",
                    "Wishing you a 2027 filled with love, calm, and beautiful little wins.",
                    "May this year make your heart lighter and your dreams clearer.",
                    "Happy New Year to my favourite person and sweetest teammate.",
                    "I hope 2027 gives you everything you are working so hard for.",
                    "May we make more memories, take better care of each other, and keep laughing together.",
                    "Happy New Year, baby. You make every beginning feel better.",
                    "May your days be peaceful and your confidence grow stronger.",
                    "Here is to love that feels steady, kind, and real.",
                    "Happy New Year. I am so happy you are in my life."
                ]
            },
            {
                "h2": "New Year Quotes for Love",
                "lines": [
                    "A new year is beautiful when love gives it a place to begin.",
                    "Love is not only fireworks at midnight, it is choosing each other the next morning too.",
                    "The best New Year promise is to stay kind when life gets busy.",
                    "When love is real, every year becomes another chapter, not another test.",
                    "New beginnings feel softer when they are held by the right person.",
                    "Love makes time feel less like a calendar and more like a story.",
                    "A good year is not perfect, it is shared with someone who stays.",
                    "May love be patient with us while we learn the year ahead.",
                    "The heart remembers who made the year easier.",
                    "A New Year with love is a quiet kind of hope."
                ]
            },
            {
                "h2": "Funny Happy New Year Wishes",
                "lines": [
                    "Happy New Year. May your resolutions last longer than your phone battery.",
                    "Wishing you a year full of money, peace, and fewer unnecessary meetings.",
                    "May 2027 bring success, snacks, and the discipline we keep pretending to have.",
                    "Happy New Year. New calendar, same us, slightly better excuses.",
                    "May your Wi-Fi stay strong and your problems stay small.",
                    "Cheers to another year of laughing at our own bad decisions.",
                    "Happy New Year. May your group chat remain dramatic but loyal.",
                    "May this year give you abs, savings, or at least good memes.",
                    "New Year, new goals, same need for naps.",
                    "Wishing you joy, health, and the courage to mute notifications."
                ]
            },
            {
                "h2": "Short New Year Captions for Friends",
                "lines": [
                    "New year, same real friends.",
                    "2027 looks better with my people.",
                    "Friends who made the year worth it.",
                    "More memories, less overthinking.",
                    "Cheers to us and the chaos.",
                    "Good friends, fresh beginnings.",
                    "Same bond, new calendar.",
                    "Grateful for this friendship.",
                    "A new year with old favourites.",
                    "Here for every chapter."
                ]
            },
            {
                "h2": "Long New Year Messages for Best Friend",
                "lines": [
                    "Happy New Year, best friend. I hope 2027 brings you the kind of peace you do not have to explain and the kind of joy that finds you on ordinary days.",
                    "Thank you for being the person I can laugh with, complain to, and trust without performing. May this year give you everything your heart has been quietly asking for.",
                    "A new year reminds me how lucky I am to have someone who understands both my silence and my excitement. Wishing you love, health, and beautiful progress.",
                    "I hope 2027 is the year you stop doubting your own light. You deserve good people, good news, and good mornings.",
                    "May this year be kind to your dreams and patient with your healing. I am always cheering for you.",
                    "Happy New Year to the friend who has seen my messy side and stayed anyway. I hope life returns that loyalty to you in beautiful ways.",
                    "I wish you courage for every hard choice and comfort for every tired evening.",
                    "May our friendship keep growing through busy days, distance, and all the strange little turns life takes.",
                    "Thank you for making so many memories feel warmer. Let us make 2027 a year worth remembering.",
                    "No matter what this year brings, I hope you know you are deeply valued."
                ]
            },
            {
                "h2": "New Year WhatsApp Wishes for Friends",
                "lines": [
                    "Happy New Year 2027, friend. May your year be full of peace, progress, and good people.",
                    "Wishing you a fresh start, a strong heart, and many reasons to smile.",
                    "May this year bring better days and beautiful surprises your way.",
                    "Happy New Year. Thank you for being part of my life.",
                    "May 2027 be kinder, brighter, and lighter for you.",
                    "Sending you warm wishes for success, health, and happiness.",
                    "Happy New Year, dost. Stay blessed and keep shining.",
                    "May your dreams get closer and your worries get smaller.",
                    "Wishing you laughter, love, and a peaceful year ahead.",
                    "Happy New Year. Let us make more memories this year."
                ]
            }
        ],
        "faqs": [
            ["What is a heart touching New Year wish for a friend?", "A heart touching wish is warm, personal, and hopeful. Try: Happy New Year 2027, my friend. May this year bring you peace, courage, good health, and the kind of happiness that stays quietly with you."],
            ["How do I wish my best friend Happy New Year?", "Mention gratitude, one personal quality, and a hope for the year ahead. Keep it honest rather than overly formal."],
            ["What can I write for Happy New Year my love?", "Write a romantic but simple line such as: Happy New Year, my love. May 2027 bring us closer, softer, and stronger together."],
            ["What are funny Happy New Year wishes for friends?", "Use light humour that does not insult anyone. For example: Happy New Year. May your resolutions last longer than your phone battery."],
            ["How do I write New Year wishes for my girlfriend?", "Keep it affectionate and respectful. Wish her peace, confidence, happiness, and shared memories for the year ahead."],
            ["How do I write New Year wishes for my boyfriend?", "Wish him success, health, confidence, and remind him that you are proud of him. Add one line about your bond."],
            ["Can I send the same New Year wish to many friends?", "Yes for group chats, but for close friends add their name or one shared memory so it feels less forwarded."],
            ["Should New Year wishes mention 2027?", "Yes. For a fresh seasonal post or greeting, using 2027 makes the message feel current and ready to send."]
        ]
    }
    config = {
        "rank": 84,
        "sections_json": f"output/{PREFIX}_sections.json",
        "output_prefix": PREFIX,
        "carousel_id": "bs-cf-newyearfriends",
        "occasion_year": "New Year 2027",
        "carousel_alt_prefix": "heart touching new year wishes for friends 2027 gift idea",
        "gift_h2": "A Soft New Year Gift Idea",
        "gift_blurb": "If your New Year wish comes with a small keepsake, keep it warm and personal. These six approved BlueStone designs fit friendship, love, and fresh-start gifting without turning the article into a catalogue.",
        "conclusion_html": "Heart touching New Year wishes for friends feel best when they sound like your real bond. Pick a line, add a name or memory, and send it before the midnight rush.",
        "schema_keywords": [
            "heart touching new year wishes for friends",
            "new year wishes for friends",
            "happy new year my love",
            "new year wishes for bf",
            "new year quotes for love",
            "funny happy new year wishes",
            "new year wishes for girlfriend",
            "new year wishes for gf"
        ],
        "type3_prompts_json": f"output/{PREFIX}_type3_prompts.json",
        "products": [
            product(rows, "The Valeria Rose Pendant", "Pendants"),
            product(rows, "The Lumeelle Cluster Pendant", "Pendants"),
            product(rows, "The Gigi Ring", "Rings"),
            product(rows, "The Shining Star Bracelet", "Bracelet"),
            product(rows, "The Rohal Huggie Earrings", "Earrings"),
            product(rows, "The Aagarna Pendant", "Pendants")
        ],
        "flatlay_insert_h2": "New Year Wishes for BF",
        "lifestyle_insert_h2": "New Year Wishes for Girlfriend",
        "more_reads_html": "Keep the celebration going with <a href=\"https://blog.bluestone.com/humanity-quotes-2026/\">humanity quotes 2026</a>, <a href=\"https://blog.bluestone.com/birthday-wishes-for-cousin-brother-sister-2026/\">birthday wishes for cousin 2026</a>, <a href=\"https://blog.bluestone.com/sorry-for-late-wishes-2026/\">sorry for late wishes 2026</a>, and <a href=\"https://blog.bluestone.com/exam-quotes-wishes-for-students-2026/\">exam quotes for students 2026</a>.",
        "how_to_html": "Send friendship wishes early, romantic wishes privately, and funny wishes only where the tone is already playful. For the calendar moment, New Year 2027 begins on January 1, 2027 according to the <a href=\"https://www.timeanddate.com/calendar/?year=2027&country=35\">2027 India calendar</a>.",
        "faq_h2": "Frequently Asked Questions about New Year Wishes for Friends",
        "min_lines": 110
    }
    checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 84

Article: Heart Touching New Year Wishes for Friends 2027
Status: Draft assets prepared
Date: 2026-07-23

## A. Intent and Brief
- [x] Primary keyword: heart touching new year wishes for friends
- [x] Supporting keywords mapped to H2s and FAQs
- [x] Sheet Optimize treated as New
- [x] Fresh slug: heart-touching-new-year-wishes-for-friends-2027
- [x] 2027 New Year lock used

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""
    (ROOT / "output" / f"{PREFIX}_sections.json").write_text(json.dumps(sections, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (ROOT / "output" / "publish_configs" / "rank84.json").write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (ROOT / "output" / f"{PREFIX}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
