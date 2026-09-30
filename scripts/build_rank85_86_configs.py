#!/usr/bin/env python3
"""Build Rank 85 and 86 generic publish configs and article sections."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_products():
    rows = {}
    with (ROOT / "Seo Products - final products (1).csv").open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            rows[row["Design Name"].strip()] = row
    return rows


def product(rows, name, category):
    row = rows[name]
    return {
        "code": row["Design Code"],
        "name": name,
        "url": row["Link"],
        "png": f"ProductImages/seo images/{category}/{name}.png",
    }


def write(prefix, sections, config, checklist):
    out = ROOT / "output"
    cfg_dir = out / "publish_configs"
    out.mkdir(exist_ok=True)
    cfg_dir.mkdir(exist_ok=True)
    (out / f"{prefix}_sections.json").write_text(json.dumps(sections, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (cfg_dir / f"rank{config['rank']}.json").write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / f"{prefix}_Checklist_v2.md").write_text(checklist, encoding="utf-8")


def main():
    rows = load_products()

    rank85_prefix = "Week1_Rank85_HumanityQuotes"
    rank85_sections = {
        "meta": {
            "title": "Humanity Quotes 2026: Kind, Short and Heart Touching Lines",
            "slug": "humanity-quotes-2026",
            "meta_desc": "Read humanity quotes 2026 for kindness, compassion, helping others, Instagram captions, school speeches, and thoughtful messages for everyday sharing.",
            "focus_kw": "humanity quotes",
            "yoast_title": "Humanity Quotes 2026: Kind and Heart Touching Lines"
        },
        "intro": [
            "Humanity quotes work best when they sound simple, steady, and useful. Use these lines for captions, speeches, cards, WhatsApp notes, or a quiet reminder to be kinder than the moment asks.",
            "TL;DR: choose a short quote for social media, a warmer line for someone who needs support, and a thoughtful paragraph when you want the message to feel personal."
        ],
        "sections": [
            {
                "h2": "Best Humanity Quotes for 2026",
                "lines": [
                    "Humanity begins with noticing another person's pain before it becomes convenient.",
                    "Be the kind of person whose presence makes the room feel safer.",
                    "The world becomes lighter when one person chooses patience over pride.",
                    "Humanity is not a grand speech, it is a small act done with a clean heart.",
                    "Kindness is the language people remember long after the day is over.",
                    "A humane heart does not ask who is watching before it helps.",
                    "The best people carry strength gently and use it to protect others.",
                    "Compassion is courage with a softer voice.",
                    "A better world starts with the way we treat the person in front of us.",
                    "Humanity is love made practical."
                ]
            },
            {
                "h2": "Short Humanity Quotes",
                "lines": [
                    "Stay human, stay kind.",
                    "Kindness is quiet power.",
                    "Help first, judge later.",
                    "A soft heart is not a weak heart.",
                    "Be gentle with unseen battles.",
                    "Humanity looks good on everyone.",
                    "Choose people over ego.",
                    "Compassion never goes out of style.",
                    "Small kindness, big impact.",
                    "Leave people lighter."
                ]
            },
            {
                "h2": "Heart Touching Humanity Quotes",
                "lines": [
                    "Sometimes one gentle word becomes the support someone needed all day.",
                    "A person may forget your advice, but they rarely forget your kindness.",
                    "Humanity is sitting beside someone without trying to fix them too quickly.",
                    "The purest help is the one given without making the other person feel small.",
                    "A good heart is seen in the way it treats people who can offer nothing back.",
                    "When life feels heavy, a little compassion can feel like a hand on the shoulder.",
                    "The world needs people who can be honest without becoming cruel.",
                    "Humanity is choosing mercy when anger would be easier.",
                    "A kind person is a shelter many people never forget.",
                    "Being human means caring even when the answer is not simple."
                ]
            },
            {
                "h2": "Humanity Quotes on Kindness",
                "lines": [
                    "Kindness is the simplest proof that humanity is still alive.",
                    "A kind act may look small, but it can change the way someone survives a day.",
                    "Do not wait to be rich, powerful, or perfect before being useful.",
                    "The kindest people are often the ones who know what silence can hide.",
                    "Offer respect before you know someone's status.",
                    "Kindness does not need a stage to matter.",
                    "A kind heart repairs more than it announces.",
                    "If you can make life softer for someone, do it.",
                    "Real kindness protects dignity.",
                    "Let your success make you generous, not distant."
                ]
            },
            {
                "h2": "Humanity Quotes for Instagram Captions",
                "lines": [
                    "Soft heart, strong values.",
                    "Choosing kindness, one ordinary day at a time.",
                    "Human first, always.",
                    "A little compassion looks good on the feed too.",
                    "Good energy starts with good intentions.",
                    "Make kindness your quiet signature.",
                    "More empathy, less noise.",
                    "Some things trend for a day, humanity should last longer.",
                    "Do good without turning it into a performance.",
                    "Grace, patience, and a little more kindness."
                ]
            },
            {
                "h2": "Humanity Quotes for School Speech",
                "lines": [
                    "Humanity teaches us that progress is incomplete without compassion.",
                    "A good society is built not only by smart minds, but also by responsible hearts.",
                    "When we respect differences, we make space for peace.",
                    "Helping others is not a small lesson, it is the foundation of character.",
                    "Education should make us more thoughtful, not only more successful.",
                    "The future needs people who can compete with skill and cooperate with kindness.",
                    "Humanity means using our voice for fairness and our hands for service.",
                    "A strong nation is built by citizens who care about one another.",
                    "Let us measure growth by how safely the weakest person can live.",
                    "The best lesson is simple, treat every person with dignity."
                ]
            },
            {
                "h2": "A Soft Gift Idea for Kind Souls",
                "lines": [
                    "A small keepsake can make a thank-you feel more personal when words are not enough.",
                    "Choose jewellery that feels gentle and everyday, not loud or overly formal.",
                    "Pick a design that suits the person's routine, comfort, and style.",
                    "A pendant, bracelet, ring, or pair of earrings can quietly mark a caring bond.",
                    "Keep the note simple so the gesture feels thoughtful, not showy.",
                    "The best gift says, I noticed your kindness.",
                    "For mentors, friends, and family, choose pieces that can be worn often.",
                    "Avoid turning the moment into a catalogue, let the sentiment lead."
                ]
            },
            {
                "h2": "Humanity Quotes About Helping Others",
                "lines": [
                    "Help that preserves dignity is the truest form of care.",
                    "You do not need to solve everything to stand beside someone.",
                    "A helping hand is most powerful when it expects no applause.",
                    "Serve people in a way that lets them keep their self-respect.",
                    "Sometimes the best help is listening without interrupting.",
                    "If someone is carrying too much, be one less weight in their day.",
                    "Humanity grows when help becomes a habit.",
                    "The world changes through people who show up.",
                    "Generosity is not only what you give, it is how you make people feel.",
                    "A little help at the right time can become lifelong hope."
                ]
            },
            {
                "h2": "Humanity Quotes on Love and Compassion",
                "lines": [
                    "Love without compassion becomes pride, compassion makes love useful.",
                    "The most beautiful hearts are the ones that can understand pain without judging it.",
                    "Compassion is love that has learned to listen.",
                    "A caring heart notices what others are too busy to see.",
                    "Love becomes humanity when it reaches beyond our own circle.",
                    "Let compassion be the first answer, even when you need boundaries.",
                    "A humane world is built by people who refuse to become numb.",
                    "Compassion does not make you less practical, it makes you more complete.",
                    "Love people enough to respect their dignity.",
                    "The best kind of love leaves room for understanding."
                ]
            },
            {
                "h2": "Humanity Quotes in Simple English",
                "lines": [
                    "Be kind to people.",
                    "Help when you can.",
                    "Respect every person.",
                    "Listen before you judge.",
                    "Care is never wasted.",
                    "Good hearts make good days.",
                    "Share hope with others.",
                    "Treat people with dignity.",
                    "Choose peace when possible.",
                    "Let your actions show humanity."
                ]
            },
            {
                "h2": "Positive Humanity Quotes",
                "lines": [
                    "There is still goodness in the world, and we can add to it today.",
                    "A kind decision can turn an ordinary day into someone's remembered moment.",
                    "Hope grows when people refuse to give up on each other.",
                    "Even difficult times reveal the strength of caring hearts.",
                    "The future feels brighter when compassion is practiced daily.",
                    "Goodness does not have to be loud to be real.",
                    "Every helpful act is a vote for a better world.",
                    "People heal faster in places where kindness is normal.",
                    "A generous spirit can brighten more lives than it knows.",
                    "Humanity survives through ordinary people doing ordinary good."
                ]
            },
            {
                "h2": "Humanity Quotes to Share on WhatsApp",
                "lines": [
                    "May we all become a little kinder today.",
                    "A good heart is still the most beautiful thing a person can have.",
                    "Let us speak gently, help quietly, and respect everyone.",
                    "Humanity starts with how we treat people in small moments.",
                    "Be someone's reason to believe in goodness again.",
                    "Kindness costs less than ego and gives more than pride.",
                    "A little care can reach places advice cannot.",
                    "Stay humble, stay helpful, stay human.",
                    "The world needs more people who choose compassion.",
                    "May our actions carry more kindness than our words promise."
                ]
            }
        ],
        "faqs": [
            ["What are humanity quotes?", "Humanity quotes are short lines about kindness, compassion, dignity, helping others, and treating people with respect. They are often used in captions, school speeches, WhatsApp messages, greeting cards, and reflective posts."],
            ["What is the best short humanity quote?", "A simple short quote is: Stay human, stay kind. It works because it is easy to remember, positive, and useful for captions, posters, and everyday reminders."],
            ["Can I use humanity quotes for Instagram?", "Yes. Choose a short, clean line such as Human first, always or Make kindness your quiet signature. These work well because they are brief, readable, and not too formal."],
            ["How do I write a heart touching humanity message?", "Start with a real feeling, keep the language simple, and focus on dignity or care. A good message should sound warm without becoming dramatic or preachy."],
            ["Are humanity quotes suitable for school speeches?", "Yes. For speeches, use quotes that connect kindness with responsibility, respect, education, and citizenship. Keep the words clear so younger listeners can follow the message easily."],
            ["What should I avoid in humanity quotes?", "Avoid insulting groups, making fake claims, or sounding morally superior. The strongest humanity quotes are humble, inclusive, and practical."],
            ["How can I personalize a humanity quote?", "Add a name, a small context, or one specific action. For example, mention listening, helping, or standing beside someone during a hard day."],
            ["Can humanity quotes be used with a gift note?", "Yes. A short quote can make a thoughtful gift note feel more meaningful, especially when the gift is for a mentor, friend, volunteer, teacher, or family member who has shown kindness."]
        ]
    }
    rank85_config = {
        "rank": 85,
        "sections_json": f"output/{rank85_prefix}_sections.json",
        "output_prefix": rank85_prefix,
        "carousel_id": "bs-cf-humanityquotes",
        "occasion_year": "Humanity Quotes 2026",
        "carousel_alt_prefix": "humanity quotes 2026 gift idea",
        "gift_h2": "A Soft Gift Idea for Kind Souls",
        "gift_blurb": "If these humanity quotes are for someone who has stood by you, keep the gift quiet and thoughtful. These six approved BlueStone designs work as gentle keepsakes without turning the article into a product catalogue.",
        "conclusion_html": "Humanity quotes are strongest when they make kindness feel doable. Pick one line, add a personal detail, and let the message carry warmth without trying too hard.",
        "schema_keywords": ["humanity quotes", "kindness quotes", "compassion quotes", "humanity quotes 2026"],
        "type3_prompts_json": f"output/{rank85_prefix}_type3_prompts.json",
        "products": [
            product(rows, "The Aagarna Pendant", "Pendants"),
            product(rows, "The Kricia Charm Bracelet", "Bracelet"),
            product(rows, "The Rafia Ring", "Rings"),
            product(rows, "The Rohal Huggie Earrings", "Earrings"),
            product(rows, "The Keeper Multiwearable Charm", "Charms"),
            product(rows, "The Shining Star Bracelet", "Bracelet")
        ],
        "flatlay_insert_h2": "Humanity Quotes About Helping Others",
        "lifestyle_insert_h2": "Humanity Quotes on Love and Compassion",
        "more_reads_html": "Explore more thoughtful lines in <a href=\"https://blog.bluestone.com/birthday-wishes-for-cousin-brother-sister-2026/\">birthday wishes for cousin 2026</a>, <a href=\"https://blog.bluestone.com/exam-quotes-wishes-for-students-2026/\">exam quotes for students 2026</a>, <a href=\"https://blog.bluestone.com/sorry-for-late-wishes-2026/\">sorry for late wishes 2026</a>, and <a href=\"https://blog.bluestone.com/shayari-on-teachers-in-hindi-2026/\">shayari on teachers in Hindi 2026</a>.",
        "how_to_html": "Match the quote to the moment. Use short lines for captions, warmer lines for notes, and simple speech lines for school or community settings. For broader context on dignity and rights, see the <a href=\"https://www.un.org/en/about-us/universal-declaration-of-human-rights\">Universal Declaration of Human Rights</a>.",
        "faq_h2": "Frequently Asked Questions about Humanity Quotes",
        "min_lines": 110
    }
    rank85_checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 85

Article: Humanity Quotes 2026
Status: Draft assets prepared
Date: 2026-07-23

## A. Intent and Brief
- [x] Primary keyword: humanity quotes
- [x] Supporting keyword mapped to H2s and FAQs
- [x] Action treated as New
- [x] Fresh slug: humanity-quotes-2026
- [x] 2026 editorial freshness lock used

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""

    rank86_prefix = "Week1_Rank86_SpeedyRecovery"
    rank86_sections = {
        "meta": {
            "title": "Speedy Recovery Message 2026: Get Well Soon Wishes",
            "slug": "speedy-recovery-message-get-well-soon-wishes-2026",
            "meta_desc": "Find speedy recovery message 2026 ideas, get well soon wishes, good health wishes, short texts, prayers, and warm notes for friends and family today with care.",
            "focus_kw": "speedy recovery message",
            "yoast_title": "Speedy Recovery Message 2026: Get Well Soon Wishes"
        },
        "intro": [
            "A speedy recovery message should feel calm, kind, and easy to receive. Whether you are texting a friend, writing to family, or sending a note with flowers or a gift, the right words can make a difficult day feel less lonely.",
            "TL;DR: keep the message short, avoid heavy advice, wish them comfort and strength, and personalize it with one detail about how you will support them."
        ],
        "sections": [
            {
                "h2": "Best Speedy Recovery Message Ideas",
                "lines": [
                    "Wishing you a smooth recovery and calmer days ahead. Take your time and know that you are cared for.",
                    "May each day bring a little more strength, comfort, and peace. Get well soon.",
                    "Sending warm wishes for your speedy recovery. Rest well and let your body heal gently.",
                    "I hope you feel better soon and return to your bright, usual self at your own pace.",
                    "May this recovery period be short, peaceful, and full of small signs of progress.",
                    "Thinking of you and wishing you steady healing, good rest, and better health every day.",
                    "Take one day at a time. You are stronger than this phase, and better days are coming.",
                    "Sending comfort, care, and positive thoughts for a quick and complete recovery.",
                    "May you regain your energy soon and feel surrounded by love while you heal.",
                    "Get well soon. I am cheering for your recovery and here whenever you need support."
                ]
            },
            {
                "h2": "Short Get Well Soon Wishes",
                "lines": [
                    "Get well soon and rest well.",
                    "Wishing you quick healing.",
                    "Feel better soon, we miss you.",
                    "Sending strength and comfort.",
                    "Take care and heal gently.",
                    "Hope today feels easier.",
                    "Praying for your good health.",
                    "Recover soon, one day at a time.",
                    "May your energy return soon.",
                    "Warm wishes for better days."
                ]
            },
            {
                "h2": "Good Health Wishes for Family",
                "lines": [
                    "Wishing you good health, peaceful rest, and a recovery that gets easier every day.",
                    "Family feels incomplete when you are unwell. Please rest and come back stronger soon.",
                    "May you feel cared for, protected, and surrounded by love while you heal.",
                    "Your health matters to all of us. Take your time and do not rush your recovery.",
                    "Sending you love, patience, and warm wishes for a smooth return to good health.",
                    "May every morning bring a little more comfort and every evening bring better rest.",
                    "We are all thinking of you and waiting to see your smile back in full strength.",
                    "Please focus on healing. Everything else can wait.",
                    "Wishing you relief from discomfort and many peaceful hours of rest.",
                    "May you recover fully and feel stronger than before."
                ]
            },
            {
                "h2": "Speedy Recovery Message for Friend",
                "lines": [
                    "My friend, I hope you recover quickly and feel like yourself again soon.",
                    "Rest properly, follow what your doctor says, and let us handle the worrying.",
                    "Sending you a big dose of friendship, comfort, and get well soon energy.",
                    "Your laugh is missed. Heal soon, but do not rush it.",
                    "May this be a short pause before you are back to your usual sparkle.",
                    "Thinking of you today and hoping your recovery feels lighter.",
                    "Get well soon, friend. I am only a call away if you need anything.",
                    "Take the rest seriously. We have many normal days to enjoy after this.",
                    "Wishing you strength, patience, and a quick comeback.",
                    "You are not alone in this. Heal slowly, steadily, and fully."
                ]
            },
            {
                "h2": "A Gentle Recovery Gift Idea",
                "lines": [
                    "A small keepsake can make a recovery note feel more personal, especially when the person cannot meet many visitors.",
                    "Choose light, comfortable jewellery that feels easy to wear once they are back to routine.",
                    "A pendant, bracelet, or ring can work when the message is about care, hope, and a fresh start.",
                    "Keep the note soft and avoid making the gift feel like pressure to be cheerful.",
                    "Do not include prices in the message. Let the thought lead.",
                    "A simple line such as, wear this when you feel ready, keeps the tone gentle.",
                    "Choose designs that suit everyday comfort rather than heavy occasion wear.",
                    "The best recovery gift feels calm, patient, and personal."
                ]
            },
            {
                "h2": "Speedy Recovery Message After Surgery",
                "lines": [
                    "Wishing you a safe and steady recovery after surgery. Rest well and give yourself time.",
                    "May every day after the procedure bring more comfort and strength.",
                    "I hope your healing is smooth and your energy returns little by little.",
                    "Please do not rush the process. Recovery deserves patience.",
                    "Sending warm thoughts as you rest, heal, and regain strength.",
                    "May your pain reduce, your rest improve, and your health grow stronger each day.",
                    "Thinking of you and hoping the coming days feel easier.",
                    "Get well soon. Let your body heal at the pace it needs.",
                    "Wishing you comfort, patience, and a complete recovery.",
                    "May this surgery become the start of better health ahead."
                ]
            },
            {
                "h2": "Prayer Messages for Speedy Recovery",
                "lines": [
                    "Praying for your quick recovery, renewed strength, and peaceful rest.",
                    "May God bless you with healing, patience, and better health each day.",
                    "Keeping you in my prayers and wishing you comfort during this recovery.",
                    "May you feel protected, loved, and guided toward complete healing.",
                    "Praying that your pain eases and your energy returns soon.",
                    "May every prayer bring you peace and every day bring progress.",
                    "Wishing you divine comfort and a speedy recovery.",
                    "May hope stay close to you while your body heals.",
                    "Praying for good reports, calm nights, and stronger mornings.",
                    "May you recover fully and feel blessed with health again."
                ]
            },
            {
                "h2": "Funny Speedy Recovery Messages",
                "lines": [
                    "Get well soon. Your bed has had enough of your company.",
                    "Recover quickly, we need your normal level of chaos back.",
                    "Please heal soon, group chats are too peaceful without you.",
                    "Take your medicines and stop negotiating with rest.",
                    "Wishing you a fast recovery and better snacks.",
                    "Come back soon, your jokes are still pending approval.",
                    "Rest now, because we are not letting you escape plans later.",
                    "Get well soon. Even your sofa wants a break.",
                    "Heal quickly, your dramatic comeback is due.",
                    "Sending soup, strength, and strict instructions to behave."
                ]
            },
            {
                "h2": "Professional Get Well Soon Message",
                "lines": [
                    "Wishing you a smooth and speedy recovery. Please take the time you need to rest.",
                    "We hope you feel better soon and return in good health when you are ready.",
                    "Sending warm wishes for your recovery and well-being.",
                    "Please focus on your health. Work can wait until you are fully better.",
                    "Wishing you comfort, rest, and a steady return to strength.",
                    "May your recovery be peaceful and complete.",
                    "Thinking of you and hoping each day brings improvement.",
                    "Please accept our best wishes for good health and quick healing.",
                    "We look forward to seeing you back when you are fully recovered.",
                    "Take care and wishing you better health soon."
                ]
            },
            {
                "h2": "Speedy Recovery Captions",
                "lines": [
                    "Healing, one quiet day at a time.",
                    "Sending comfort and better days.",
                    "Rest today, rise stronger soon.",
                    "Small progress still counts.",
                    "Good health is on its way.",
                    "Wrapped in care and hope.",
                    "Recovery mode with love.",
                    "Better mornings are coming.",
                    "Strength grows slowly too.",
                    "Get well soon, gentle heart."
                ]
            },
            {
                "h2": "What to Write in a Recovery Card",
                "lines": [
                    "Start with a simple wish for comfort and healing.",
                    "Add one personal line that shows you know what they are going through.",
                    "Offer practical help only if you can follow through.",
                    "Avoid comparing their situation with someone else's illness.",
                    "Keep the message hopeful without forcing positivity.",
                    "Use warm words such as rest, strength, comfort, healing, and care.",
                    "Close with a clear line of support.",
                    "If you are unsure, keep it short and sincere.",
                    "Do not give medical advice unless you are their doctor.",
                    "A kind card should feel easy to read, even on a hard day."
                ]
            },
            {
                "h2": "Speedy Recovery Message for WhatsApp",
                "lines": [
                    "Just checking in. Hope you are resting and feeling a little better today.",
                    "Sending you strength and good health. Get well soon.",
                    "Please take care and do not rush. I am here if you need anything.",
                    "Hope today is easier than yesterday and tomorrow feels better still.",
                    "Thinking of you. Rest well and recover soon.",
                    "May your health improve quickly and your days feel peaceful.",
                    "Get well soon. We are all waiting to see you happy and healthy again.",
                    "Sending warm wishes and lots of care your way.",
                    "Take medicines on time, rest properly, and heal well.",
                    "You have got this. Wishing you a smooth recovery."
                ]
            }
        ],
        "faqs": [
            ["What is a good speedy recovery message?", "A good speedy recovery message is short, warm, and supportive. Try: Wishing you comfort, steady healing, and better health every day. Rest well and know that you are cared for."],
            ["How do you say get well soon professionally?", "Use calm and respectful language. For example: Wishing you a smooth recovery. Please take the time you need to rest, and we look forward to seeing you back in good health."],
            ["What can I write in a recovery card?", "Write a simple wish for healing, one personal line, and a practical offer of support if appropriate. Avoid medical advice or pressure to feel positive."],
            ["What is a short get well soon wish?", "A short wish is: Get well soon and rest well. It is simple, kind, and works for WhatsApp, cards, flowers, or a quick check-in text."],
            ["Can I send a funny speedy recovery message?", "Yes, if the person enjoys humour and the illness is not too serious. Keep it light, never mocking, and add a caring line after the joke."],
            ["What should I avoid in get well soon wishes?", "Avoid giving medical advice, comparing illnesses, making the person feel guilty, or saying everything happens for a reason. Keep the message gentle and supportive."],
            ["How do I wish someone good health?", "Say something like: Wishing you good health, peaceful rest, and renewed strength every day. Keep the tone warm and focused on comfort."],
            ["Is it okay to send a gift with a speedy recovery message?", "Yes, if it suits the relationship. Keep the gift simple and the note pressure-free so the person feels cared for, not overwhelmed."]
        ]
    }
    rank86_config = {
        "rank": 86,
        "sections_json": f"output/{rank86_prefix}_sections.json",
        "output_prefix": rank86_prefix,
        "carousel_id": "bs-cf-speedyrecovery",
        "occasion_year": "Speedy Recovery 2026",
        "carousel_alt_prefix": "speedy recovery message 2026 gift idea",
        "gift_h2": "A Gentle Recovery Gift Idea",
        "gift_blurb": "If you are sending a recovery note with a keepsake, choose something calm, wearable, and personal. These six approved BlueStone designs fit a gentle get well soon gesture without making the article feel like a catalogue.",
        "conclusion_html": "A speedy recovery message does not need perfect words. Keep it gentle, wish them comfort, and offer support in a way that feels real.",
        "schema_keywords": ["speedy recovery message", "get well soon wishes", "good health wishes", "speedy recovery message 2026"],
        "type3_prompts_json": f"output/{rank86_prefix}_type3_prompts.json",
        "products": [
            product(rows, "The Melene Evil Eye Pendant", "Pendants"),
            product(rows, "The Elize Evil Eye Bracelet", "Bracelet"),
            product(rows, "The Haily Ring", "Rings"),
            product(rows, "The Aleena Huggie Earrings", "Earrings"),
            product(rows, "The Pear Evil Eye Toggle Bangle", "Bangles"),
            product(rows, "The Malocchio Charm Holder Bracelet", "Bracelet")
        ],
        "flatlay_insert_h2": "Speedy Recovery Message After Surgery",
        "lifestyle_insert_h2": "Prayer Messages for Speedy Recovery",
        "more_reads_html": "For more caring message ideas, read <a href=\"https://blog.bluestone.com/sorry-for-late-wishes-2026/\">sorry for late wishes 2026</a>, <a href=\"https://blog.bluestone.com/birthday-wishes-for-cousin-brother-sister-2026/\">birthday wishes for cousin 2026</a>, <a href=\"https://blog.bluestone.com/exam-quotes-wishes-for-students-2026/\">exam quotes for students 2026</a>, and <a href=\"https://blog.bluestone.com/shayari-on-teachers-in-hindi-2026/\">shayari on teachers in Hindi 2026</a>.",
        "how_to_html": "Keep recovery notes supportive and avoid medical advice. For serious symptoms or urgent concerns, official public health guidance such as <a href=\"https://www.who.int/health-topics\">WHO health topics</a> is a better starting point than social media posts.",
        "faq_h2": "Frequently Asked Questions about Speedy Recovery Messages",
        "min_lines": 110
    }
    rank86_checklist = """# Blog SEO + AEO/GEO Checklist v2, Rank 86

Article: Speedy Recovery Message 2026
Status: Draft assets prepared
Date: 2026-07-23

## A. Intent and Brief
- [x] Primary keyword: speedy recovery message
- [x] Supporting keywords mapped to H2s and FAQs
- [x] Action treated as New
- [x] Fresh slug: speedy-recovery-message-get-well-soon-wishes-2026
- [x] 2026 editorial freshness lock used

## F. Media and Links
- [x] Six Type 2 carousel products selected from ProductImages/seo images only
- [ ] WordPress post published
- [ ] Type 3 Higgsfield images generated and patched
- [ ] Live URL verified
"""

    write(rank85_prefix, rank85_sections, rank85_config, rank85_checklist)
    write(rank86_prefix, rank86_sections, rank86_config, rank86_checklist)


if __name__ == "__main__":
    main()
