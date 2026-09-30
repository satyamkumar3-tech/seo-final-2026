#!/usr/bin/env python3
"""Build rank-specific content JSON/configs for Rank 85 and Rank 86."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write_json(path: str, data: dict) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(target)


rank85_sections = {
    "meta": {
        "title": "Humanity Quotes 2026: Kindness, Compassion and Goodness",
        "slug": "humanity-quotes-2026",
        "meta_desc": "Explore humanity quotes 2026 on kindness, compassion, goodness, helping others, unity and hope for captions, speeches, status and thoughtful messages today.",
        "focus_kw": "humanity quotes",
        "yoast_title": "Humanity Quotes 2026: Kindness and Hope",
    },
    "intro": [
        "Humanity quotes are short lines about kindness, compassion, dignity, and the simple choice to care for another person. In 2026, they work beautifully for captions, school speeches, status updates, morning messages, and thoughtful notes.",
        "TL;DR: choose a short quote for status, a deeper line for speeches, and a hopeful quote when someone needs encouragement. The best humanity quote sounds clear, warm, and useful in real life.",
        "A good line about humanity should not feel ornamental. It should make the reader pause, soften, and do one decent thing."
    ],
    "sections": [
        {
            "key": "short_humanity_quotes",
            "h2": "Short Humanity Quotes",
            "lines": [
                "Humanity begins where indifference ends.",
                "A kind heart is still the strongest language.",
                "Be human first, everything else can wait.",
                "Goodness is quiet, but it changes rooms.",
                "The world improves when someone chooses care.",
                "A little compassion can carry a tired person.",
                "Humanity is the habit of seeing another life clearly.",
                "Kindness is never small to the person receiving it.",
                "Real strength protects, it does not humiliate.",
                "Hope grows when people help each other.",
                "The simplest act of humanity is to notice.",
                "A better world starts with a softer response."
            ],
        },
        {
            "key": "kindness_compassion",
            "h2": "Humanity Quotes on Kindness and Compassion",
            "lines": [
                "Kindness is not weakness. It is courage with a gentle voice.",
                "Compassion asks us to help before we judge.",
                "The most human thing we can do is make someone feel less alone.",
                "A compassionate heart listens even when it cannot solve everything.",
                "Kindness is the bridge between strangers.",
                "When you cannot fix the whole world, repair one moment.",
                "Compassion turns ordinary people into safe places.",
                "Humanity grows when comfort is shared, not hoarded.",
                "A kind word can become the beginning of someone's strength.",
                "To care is to say that another person's pain matters.",
                "Kindness is love made practical.",
                "Compassion is the art of standing beside someone without noise."
            ],
        },
        {
            "key": "goodness_values",
            "h2": "Humanity Quotes About Goodness",
            "lines": [
                "Goodness is doing the right thing when applause is absent.",
                "A good person leaves people lighter than they found them.",
                "Goodness does not need grand stages. It needs honest choices.",
                "Humanity is measured in how we treat people who can give us nothing.",
                "The best kind of goodness is steady, not seasonal.",
                "Do good quietly, but do it often.",
                "A good heart is a daily discipline.",
                "Goodness is not perfection. It is the willingness to keep choosing better.",
                "The world remembers sincere goodness longer than loud success.",
                "A humane life is built from small honest acts.",
                "Goodness becomes powerful when it is repeated.",
                "The finest legacy is how safe people felt around you."
            ],
        },
        {
            "key": "humanity_status",
            "h2": "Humanity Quotes for Status",
            "lines": [
                "Stay kind. The world is already hard enough.",
                "Choose humanity, especially when it is inconvenient.",
                "Soft hearts can still build strong worlds.",
                "Be the reason someone trusts goodness again.",
                "Kindness looks good on every soul.",
                "Humanity is my favourite form of strength.",
                "Less ego, more empathy.",
                "Care is never outdated.",
                "Help quietly. Love honestly. Live gently.",
                "The real glow is a good heart.",
                "Make kindness your default setting.",
                "Humanity is a daily decision."
            ],
        },
        {
            "key": "helping_others",
            "h2": "Quotes About Helping Others",
            "lines": [
                "Helping someone is a reminder that we belong to each other.",
                "A hand held at the right time can feel like hope.",
                "You may not change the whole road, but you can light one step.",
                "Help is most beautiful when it protects dignity.",
                "The smallest support can become someone's turning point.",
                "When you lift another person, your own heart rises too.",
                "Service is love without a speech.",
                "The best help arrives with respect, not superiority.",
                "A humane world is built by people who do not look away.",
                "Sometimes kindness is simply showing up.",
                "Helping others is how hope becomes visible.",
                "A generous act can outlive the day it was done."
            ],
        },
        {
            "key": "unity_peace",
            "h2": "Humanity Quotes on Unity and Peace",
            "lines": [
                "Unity starts when we listen to understand, not to win.",
                "Peace is built by people who refuse to dehumanize others.",
                "We are different stories sharing the same sky.",
                "Humanity is bigger than every label we create.",
                "A peaceful heart does not need to defeat everyone.",
                "The world heals faster when dignity is mutual.",
                "Unity is not sameness. It is respect across difference.",
                "Peace begins in the words we choose today.",
                "A humane society protects the vulnerable first.",
                "The strongest communities are stitched with empathy.",
                "Humanity asks us to widen the circle.",
                "Respect is the first language of peace."
            ],
        },
        {
            "key": "caption_quotes",
            "h2": "Humanity Quotes for Captions",
            "lines": [
                "A little more kindness, a little less noise.",
                "Trying to leave people better than I found them.",
                "Humanity is the real aesthetic.",
                "Choose compassion, then choose it again.",
                "Small acts, honest heart, better world.",
                "A good heart never goes out of style.",
                "Softness with boundaries, kindness with courage.",
                "Making room for hope.",
                "The world needs more decent moments.",
                "Be kind in ways people can feel.",
                "Empathy is quiet magic.",
                "Let goodness be the caption."
            ],
        },
        {
            "key": "speech_quotes",
            "h2": "Humanity Quotes for Speeches and Essays",
            "lines": [
                "Humanity is not an idea reserved for books. It is tested in everyday choices.",
                "A society becomes truly strong when it protects people with the least power.",
                "The purpose of progress is incomplete if it leaves compassion behind.",
                "Technology may connect us, but humanity teaches us how to care once connected.",
                "The future deserves intelligence with empathy and ambition with conscience.",
                "Humanity is the courage to see pain and still choose action.",
                "Our greatest achievement is not only what we build, but how gently we treat one another while building it.",
                "A humane world begins when respect becomes ordinary.",
                "Compassion is not extra. It is the foundation of civil life.",
                "If we want a better tomorrow, kindness must become a public habit.",
                "Humanity gives success a soul.",
                "The finest education is incomplete without empathy."
            ],
        },
    ],
    "section_leads": {
        "Short Humanity Quotes": "Use these lines when you need a quick quote that is easy to remember and easy to share.",
        "Humanity Quotes on Kindness and Compassion": "These quotes are warmer and more reflective, useful for messages, posts, and personal notes.",
        "Humanity Quotes About Goodness": "Goodness quotes work well when you want the line to feel value-led without sounding preachy.",
        "Humanity Quotes for Status": "Keep status lines short, clear, and emotionally clean.",
        "Quotes About Helping Others": "Use these when the focus is service, support, or being present for someone.",
        "Humanity Quotes on Unity and Peace": "These lines fit speeches, classroom activities, and community posts.",
        "Humanity Quotes for Captions": "These captions are short enough for Instagram, LinkedIn, WhatsApp, and story posts.",
        "Humanity Quotes for Speeches and Essays": "These longer lines can open or close a speech, school essay, or reflection note."
    },
    "faqs": [
        ["What are humanity quotes?", "Humanity quotes are short lines about kindness, compassion, dignity, empathy, and helping others. They are often used in captions, school speeches, essays, status updates, and thoughtful messages because they express human values in a simple way."],
        ["What is the best short humanity quote?", "A strong short humanity quote is: Humanity begins where indifference ends. It is brief, clear, and meaningful because it reminds readers that being human is an active choice, not just an identity."],
        ["Can I use humanity quotes for Instagram captions?", "Yes, humanity quotes work well for Instagram captions when they are short and natural. Choose lines about kindness, empathy, or hope, then pair them with a photo that feels sincere rather than overly staged."],
        ["What are good humanity quotes for students?", "Good humanity quotes for students should be simple and value-focused. Try lines about helping others, respecting differences, and choosing kindness. They work well for assemblies, essays, classroom boards, and school speeches."],
        ["How do I write my own humanity quote?", "To write your own humanity quote, choose one value such as kindness or dignity, then connect it to a daily action. Keep it under 20 words if it is for status, or make it slightly longer for speeches and essays."]
    ]
}

rank85_config = {
    "rank": 85,
    "sections_json": "output/Week1_Rank85_HumanityQuotes_sections.json",
    "output_prefix": "Week1_Rank85_HumanityQuotes",
    "carousel_id": "bs-cf-humanityquotes",
    "occasion_year": "Humanity Quotes 2026",
    "carousel_alt_prefix": "humanity quotes 2026 gift idea",
    "gift_h2": "A Thoughtful Keepsake for Someone Kind",
    "gift_blurb": "If a quote reminds you of someone who has shown kindness, a quiet keepsake can make the message more personal. These six approved BlueStone designs stay soft and thoughtful, with no prices in the article.",
    "conclusion_html": "Humanity quotes work best when they lead to a real gesture. Share one line, then follow it with patience, help, or a kinder response in the next conversation.",
    "schema_keywords": ["humanity quotes", "kindness quotes", "compassion quotes", "goodness quotes", "humanity status"],
    "type3_prompts_json": "output/Week1_Rank85_HumanityQuotes_type3_prompts.json",
    "products": [
        {"code": "BISW1080P132", "name": "The Sarvanya Pendant", "url": "https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html", "png": "ProductImages/seo images/Pendants/The Sarvanya Pendant.png"},
        {"code": "BIIP0550P16", "name": "The Aagarna Pendant", "url": "https://www.bluestone.com/pendants/the-aagarna-pendant~54965.html", "png": "ProductImages/seo images/Pendants/The Aagarna Pendant.png"},
        {"code": "BIIP0279S08", "name": "The Aleena Huggie Earrings", "url": "https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html", "png": "ProductImages/seo images/Earrings/The Aleena Huggie Earrings.png"},
        {"code": "BIMG0635V45", "name": "The Shining Star Bracelet", "url": "https://www.bluestone.com/bracelets/the-shining-star-bracelet~63731.html", "png": "ProductImages/seo images/Bracelet/The Shining Star Bracelet.png"},
        {"code": "BIAV0865V24", "name": "The Pervinca Charm Holder Bracelet", "url": "https://www.bluestone.com/bracelets/the-pervinca-charm-holder-bracelet~103133.html", "png": "ProductImages/seo images/Bracelet/The Pervinca Charm Holder Bracelet.png"},
        {"code": "BIAR0097R16", "name": "The Quinn Ring", "url": "https://www.bluestone.com/rings/the-quinn-ring~57845.html", "png": "ProductImages/seo images/Rings/The Quinn Ring.png"}
    ],
    "flatlay_insert_h2": "Humanity Quotes About Goodness",
    "lifestyle_insert_h2": "Quotes About Helping Others",
    "more_reads_html": "Read more thoughtful lines in <a href=\"https://blog.bluestone.com/exam-quotes-wishes-for-students-2026/\">exam quotes for students 2026</a>, <a href=\"https://blog.bluestone.com/shayari-for-teachers-in-english-2026/\">shayari for teachers in English 2026</a>, <a href=\"https://blog.bluestone.com/raksha-bandhan-quotes-wishes-in-hindi-2026/\">Raksha Bandhan quotes in Hindi 2026</a>, and <a href=\"https://blog.bluestone.com/birthday-wishes-for-cousin-brother-sister-2026/\">birthday wishes for cousin 2026</a>. For a broader reference, see <a href=\"https://en.wikipedia.org/wiki/Humanity_(virtue)\">humanity as a virtue</a>.",
    "how_to_html": "Pick a humanity quote by matching the situation. Use a short line for status, a warm line for captions, and a deeper line for speeches or essays. Avoid using a quote to sound impressive if a simple kind action would say more.",
    "faq_h2": "Frequently Asked Questions about Humanity Quotes",
    "min_lines": 90
}

rank86_sections = {
    "meta": {
        "title": "Speedy Recovery Message 2026: Get Well Soon Wishes",
        "slug": "speedy-recovery-message-2026",
        "meta_desc": "Find speedy recovery message 2026 ideas with get well soon wishes, good health wishes, short texts, prayers and warm lines for friends and family today now.",
        "focus_kw": "speedy recovery message",
        "yoast_title": "Speedy Recovery Message 2026"
    },
    "intro": [
        "A speedy recovery message should be gentle, hopeful, and easy for the person to receive. In 2026, the best get well soon wishes sound caring without making the illness the whole conversation.",
        "TL;DR: keep it short for WhatsApp, warmer for family, and practical for colleagues. Wish them rest, strength, comfort, and good health without giving medical advice.",
        "When someone is unwell, a small message can make the day feel less lonely. Use the lines below as they are, or add the person's name for a softer touch."
    ],
    "sections": [
        {
            "key": "short_speedy_recovery",
            "h2": "Short Speedy Recovery Messages",
            "lines": [
                "Wishing you a speedy recovery and a calmer, healthier week ahead.",
                "Get well soon. Rest well and take one gentle day at a time.",
                "Sending you strength, comfort, and warm wishes for a quick recovery.",
                "Hope you feel better soon and return to your cheerful self.",
                "Take care, rest fully, and let your body heal at its own pace.",
                "Wishing you good health, peace, and steady improvement every day.",
                "Get well soon. You are in my thoughts today.",
                "May each day bring more comfort and more strength.",
                "Rest, recover, and know that you are cared for.",
                "Sending a little hope your way for a speedy recovery."
            ]
        },
        {
            "key": "get_well_soon",
            "h2": "Get Well Soon Wishes",
            "lines": [
                "Get well soon. I hope your recovery is smooth, peaceful, and full of small signs of progress.",
                "Wishing you better health with every passing day. Please take the rest you need.",
                "May this phase pass quickly and leave you feeling stronger than before.",
                "Get well soon. Your energy and smile are missed more than you know.",
                "I hope today feels a little easier and tomorrow feels even better.",
                "Wishing you comfort, patience, and a steady return to good health.",
                "Take your time to heal. Everything else can wait.",
                "May you feel surrounded by care, warmth, and hope while you recover.",
                "Get well soon. I am cheering for your strength and healing.",
                "Sending you calm thoughts and a heart full of good wishes."
            ]
        },
        {
            "key": "good_health_wishes",
            "h2": "Good Health Wishes",
            "lines": [
                "Wishing you good health, deep rest, and many brighter mornings ahead.",
                "May your body regain strength and your mind stay peaceful through recovery.",
                "Good health is the sweetest blessing, and I hope it returns to you quickly.",
                "May every day bring you more energy, comfort, and confidence.",
                "Wishing you a healthy heart, a calm mind, and a strong recovery.",
                "May your health improve steadily and your spirit stay hopeful.",
                "I hope wellness finds its way back to you soon.",
                "Wishing you healing, patience, and the comfort of people who care.",
                "May this recovery bring you rest, renewal, and good health.",
                "Here is to better days, stronger steps, and peaceful healing."
            ]
        },
        {
            "key": "family_recovery",
            "h2": "Speedy Recovery Messages for Family",
            "lines": [
                "Get well soon. The house feels incomplete until you are smiling freely again.",
                "We are all thinking of you and waiting for the day you feel stronger.",
                "Please rest without worrying about anything. Your health comes first.",
                "Sending you family love, warm food vibes, and endless prayers for healing.",
                "May you recover soon and return to the little routines we all miss.",
                "You are deeply loved. Take every bit of time you need to heal.",
                "Wishing you comfort today and better health tomorrow.",
                "Get well soon. We are right here with you through this recovery.",
                "Your strength inspires us, but please be gentle with yourself now.",
                "May every prayer become a step toward your recovery."
            ]
        },
        {
            "key": "friend_recovery",
            "h2": "Speedy Recovery Messages for Friends",
            "lines": [
                "Get well soon, my friend. I miss your jokes, your energy, and your usual spark.",
                "Rest properly now so we can celebrate your comeback soon.",
                "Sending you healing wishes, silly distractions, and lots of care.",
                "You have handled tougher days. This one will pass too.",
                "Get well soon. I am only one call away if you need anything.",
                "Wishing you comfort, strength, and a quick return to your bright self.",
                "Take it slow, heal well, and let people show up for you.",
                "Hope you feel better soon. Our plans can wait until you are fully ready.",
                "Sending a soft reminder that you are loved and missed.",
                "May recovery be kinder and quicker than expected."
            ]
        },
        {
            "key": "professional_recovery",
            "h2": "Professional Get Well Soon Messages",
            "lines": [
                "Wishing you a smooth recovery and good health in the days ahead.",
                "Please take the time you need to rest and recover fully.",
                "Sending warm wishes for your health, comfort, and steady recovery.",
                "We hope you feel better soon and return when you are ready.",
                "Wishing you strength and a peaceful recovery period.",
                "Get well soon. Your wellbeing matters most right now.",
                "May each day bring renewed energy and better health.",
                "Take care and please do not rush your recovery.",
                "Wishing you comfort, rest, and a quick return to good health.",
                "Sending sincere wishes for a full and speedy recovery."
            ]
        },
        {
            "key": "prayer_recovery",
            "h2": "Prayerful Speedy Recovery Messages",
            "lines": [
                "May you be blessed with strength, patience, and complete healing.",
                "Praying for your comfort today and your good health very soon.",
                "May every prayer bring you peace and every day bring progress.",
                "Wishing you divine comfort, renewed strength, and a gentle recovery.",
                "May you feel protected, supported, and steadily healed.",
                "Praying that this difficult phase passes quickly and safely.",
                "May hope stay close to you while your body recovers.",
                "Sending prayers for better health and a peaceful heart.",
                "May you be surrounded by care and guided toward complete wellness.",
                "Wishing you healing blessings and brighter days ahead."
            ]
        },
        {
            "key": "what_not_to_write",
            "h2": "What Not to Write in a Recovery Message",
            "lines": [
                "Do not ask for private medical details unless the person offers them.",
                "Do not compare their illness with someone else's story.",
                "Avoid dramatic lines that make the person more anxious.",
                "Do not give medical advice unless you are their doctor.",
                "Avoid jokes unless you know they will enjoy the tone.",
                "Do not pressure them to reply quickly.",
                "Avoid making the message about your inconvenience.",
                "Do not use false urgency or miracle claims.",
                "Keep the message supportive, not investigative.",
                "When unsure, write less and write kindly."
            ]
        }
    ],
    "section_leads": {
        "Short Speedy Recovery Messages": "Use these when you want a clean WhatsApp or SMS line.",
        "Get Well Soon Wishes": "These wishes are warm without becoming too heavy.",
        "Good Health Wishes": "Good health wishes work for family, friends, colleagues, and elders.",
        "Speedy Recovery Messages for Family": "Family messages can be more affectionate and personal.",
        "Speedy Recovery Messages for Friends": "Friendship recovery wishes can be a little warmer and more casual.",
        "Professional Get Well Soon Messages": "Keep workplace messages respectful, brief, and pressure-free.",
        "Prayerful Speedy Recovery Messages": "Use these only when prayerful language fits the relationship.",
        "What Not to Write in a Recovery Message": "A thoughtful recovery message should reduce stress, not add to it."
    },
    "faqs": [
        ["What is a good speedy recovery message?", "A good speedy recovery message is short, hopeful, and gentle. You can write: Wishing you a speedy recovery and a calmer, healthier week ahead. It shows care without asking for private medical details."],
        ["What can I say instead of get well soon?", "Instead of get well soon, you can say: Wishing you comfort and steady healing, or I hope each day brings more strength. These lines feel warmer and less routine while keeping the message simple."],
        ["How do I send good health wishes professionally?", "For a professional note, keep it respectful and pressure-free. Write: Wishing you a smooth recovery and good health in the days ahead. Please take the time you need to rest and recover fully."],
        ["Can I send a speedy recovery message on WhatsApp?", "Yes, WhatsApp is fine for a speedy recovery message. Keep it brief, avoid medical questions, and do not expect an immediate reply. A simple line of care can still feel meaningful."],
        ["What should I avoid in a recovery message?", "Avoid asking for private details, giving medical advice, comparing illnesses, or making dramatic claims. The best recovery messages offer comfort, patience, and practical care without adding pressure."]
    ]
}

rank86_config = {
    "rank": 86,
    "sections_json": "output/Week1_Rank86_SpeedyRecovery_sections.json",
    "output_prefix": "Week1_Rank86_SpeedyRecovery",
    "carousel_id": "bs-cf-speedyrecovery",
    "occasion_year": "Speedy Recovery 2026",
    "carousel_alt_prefix": "speedy recovery message 2026 gift idea",
    "gift_h2": "A Gentle Get Well Soon Gift Idea",
    "gift_blurb": "A recovery message is enough on its own, but a small keepsake can feel comforting when the relationship is close. These six approved BlueStone pieces lean protective and thoughtful, with no prices shown.",
    "conclusion_html": "A speedy recovery message does not need to be long. Send one honest line, give the person space to rest, and follow up with real care if they need support.",
    "schema_keywords": ["speedy recovery message", "get well soon wishes", "good health wishes", "speedy recovery wishes"],
    "type3_prompts_json": "output/Week1_Rank86_SpeedyRecovery_type3_prompts.json",
    "products": [
        {"code": "BIPO0783P12", "name": "The Melene Evil Eye Pendant", "url": "https://www.bluestone.com/pendants/the-melene-evil-eye-pendant~82769.html", "png": "ProductImages/seo images/Pendants/The Melene Evil Eye Pendant.png"},
        {"code": "BIPO0783P11", "name": "The Ixea Evil Eye Pendant", "url": "https://www.bluestone.com/pendants/the-ixea-evil-eye-pendant~82777.html", "png": "ProductImages/seo images/Pendants/The Ixea Evil Eye Pendant.png"},
        {"code": "BISE0987P01", "name": "The Protecteur Evil Eye Pendant", "url": "https://www.bluestone.com/pendants/the-protecteur-evil-eye-pendant~114379.html", "png": "ProductImages/seo images/Pendants/The Protecteur Evil Eye Pendant.png"},
        {"code": "BIMG0635V45", "name": "The Shining Star Bracelet", "url": "https://www.bluestone.com/bracelets/the-shining-star-bracelet~63731.html", "png": "ProductImages/seo images/Bracelet/The Shining Star Bracelet.png"},
        {"code": "BIAV1005V201", "name": "The Novare Evil Eye Kids Nazariya Bracelet", "url": "https://www.bluestone.com/kids+bracelets/the-novare-evil-eye-kids-nazariya-bracelet~173235.html", "png": "ProductImages/seo images/Kids Bracelets/The Novare Evil Eye Kids Nazariya Bracelet.png"},
        {"code": "BIEK1005V227", "name": "The Winkoo Kids Evil Eye Bracelet", "url": "https://www.bluestone.com/kids+bracelets/the-winkoo-kids-evil-eye-bracelet~181193.html", "png": "ProductImages/seo images/Kids Bracelets/The Winkoo Kids Evil Eye Bracelet.png"}
    ],
    "flatlay_insert_h2": "Good Health Wishes",
    "lifestyle_insert_h2": "Speedy Recovery Messages for Friends",
    "more_reads_html": "For more message ideas, read <a href=\"https://blog.bluestone.com/humanity-quotes-2026/\">humanity quotes 2026</a>, <a href=\"https://blog.bluestone.com/exam-quotes-wishes-for-students-2026/\">exam quotes for students 2026</a>, <a href=\"https://blog.bluestone.com/sorry-for-late-wishes-2026/\">sorry for late wishes 2026</a>, and <a href=\"https://blog.bluestone.com/birthday-wishes-for-cousin-brother-sister-2026/\">birthday wishes for cousin 2026</a>. For general health information, use official guidance from <a href=\"https://www.who.int/health-topics\">the World Health Organization</a>.",
    "how_to_html": "Match the recovery message to the relationship. Keep it short for colleagues, warmer for friends, and more affectionate for family. Avoid medical advice, private questions, or pressure to respond.",
    "faq_h2": "Frequently Asked Questions about Speedy Recovery Messages",
    "min_lines": 80
}


def main() -> None:
    write_json("output/Week1_Rank85_HumanityQuotes_sections.json", rank85_sections)
    write_json("output/publish_configs/rank85.json", rank85_config)
    write_json("output/Week1_Rank86_SpeedyRecovery_sections.json", rank86_sections)
    write_json("output/publish_configs/rank86.json", rank86_config)


if __name__ == "__main__":
    main()
