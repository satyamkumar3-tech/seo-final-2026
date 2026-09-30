#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish Week 9 Rank 88 post to WordPress (panna stone ring)."""
import json
import os
import sys
import base64
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Load environment
for ep in [ROOT / ".env", Path("/Users/satyamkumar/Downloads/seo final 2026/.env")]:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

wp_user = os.environ.get("WP_USER", "blogbluestone")
wp_pass = os.environ.get("WP_APP_PASSWORD") or os.environ.get("WP_APP_PASS") or os.environ.get("WP_PASSWORD", "")
auth_header = 'Basic ' + base64.b64encode((wp_user + ':' + wp_pass).encode()).decode()

headers = {
    'Authorization': auth_header,
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
}
api_base = 'https://blog.bluestone.com/wp-json/wp/v2'

slug = 'panna-stone-ring-2026'
title = 'How to Choose and Style a Panna Stone Ring: The Definitive 2026 Buying Guide'
meta_desc = "Discover how to choose the perfect panna stone ring in 2026. Explore emerald 4Cs, men's designs, gold settings, BIS hallmarking, and astrological rules."
author_id = 270271337
categories = [554493348, 554493465] # Gold (554493348), Jewellery Problem & Solution (554493465)

# 1. Exact slug check before creating
req_check = urllib.request.Request(f'{api_base}/posts?slug={slug}&status=any', headers=headers)
with urllib.request.urlopen(req_check) as resp:
    existing = json.loads(resp.read().decode())
    if existing:
        print(f"Post with slug {slug} already exists! ID: {existing[0]['id']}")
        with open(ROOT / 'output/week9_rank88_published_post.json', 'w') as out_f:
            json.dump(existing[0], out_f, indent=2)
        sys.exit(0)

with open(ROOT / 'output/Week9_Rank88_Panna_Stone_Ring_Draft.html', encoding='utf-8') as f:
    body_content = f.read()

with open(ROOT / 'output/week9_rank88_carousel_media.json', encoding='utf-8') as f:
    carousel_items = json.load(f)

# Trailing JSON-LD Schema
schema_json = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "BlogPosting",
            "@id": f"https://blog.bluestone.com/{slug}/#blogposting",
            "mainEntityOfPage": f"https://blog.bluestone.com/{slug}/",
            "headline": title,
            "description": meta_desc,
            "author": {
                "@type": "Person",
                "name": "Satyam",
                "jobTitle": "BlueStone Editorial"
            },
            "publisher": {
                "@type": "Organization",
                "name": "BlueStone",
                "url": "https://blog.bluestone.com"
            },
            "datePublished": "2026-09-28T17:00:00+05:30",
            "dateModified": "2026-09-28T17:00:00+05:30"
        },
        {
            "@type": "FAQPage",
            "@id": f"https://blog.bluestone.com/{slug}/#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "Which finger should a panna stone ring be worn on according to Vedic tradition?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "In Vedic astrology, a panna stone ring is traditionally worn on the little finger (Kanishtika) of the working or dominant hand. The little finger aligns directly with the mount of Mercury (Budha) at the base of the palm. In certain individual horoscopes, an astrologer may suggest the ring finger, but the little finger remains the standard, universal placement."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Can a panna stone ring be worn every day without risking damage?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Yes, a panna stone ring can be worn daily provided it is set in a protective mount, such as a secure bezel or low-profile multi-prong setting in sturdy 14K or 18K gold. Because natural emeralds have a hardness of 7.5 to 8 on the Mohs scale with internal inclusions, avoid wearing the ring during heavy physical labour, gym workouts, or when handling harsh chemicals and cleaning agents."
                    }
                },
                {
                    "@type": "Question",
                    "name": "What features define an ideal panna stone ring design for man?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "An ideal panna stone ring design for man features a broad gold shank (typically 4.0 mm to 8.0 mm wide), a substantial metal profile, and protective flush, signet, or bezel settings. These architectural choices shield the emerald's delicate corners from daily impact while offering a confident, sophisticated look that pairs seamlessly with both western formal wear and traditional Indian attire."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Why are inclusions or gardens normal in natural panna stones?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Natural emeralds form under intense hydrothermal conditions where beryllium meets chromium deep in the earth's crust. This turbulent crystallization creates microscopic two-phase fluid bubbles, healing fissures, and mineral crystals known as a jardin (garden). These inclusions are natural proof of authenticity, distinguishing genuine mined gemstones from synthetic glass or laboratory imitations."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How is the price of a panna stone ring calculated in an authentic Indian jewellery invoice?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "An honest jewellery invoice calculates the total price by deducting the gemstone weight in carats from the gross ring weight to arrive at the net gold weight. The prevailing gold rate is applied strictly to the net gold weight, while the panna stone, making charges, and statutory 3% GST are billed as separate, transparent line items."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How do I clean and care for my panna stone ring at home?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Clean your panna stone ring at home using lukewarm water, a few drops of mild dish soap, and an extra-soft toothbrush to gently loosen dirt beneath the mount. Rinse thoroughly with clean water and dry with a soft microfibre cloth. Never use ultrasonic cleaners or boiling steam, as high vibrations and intense heat will strip the natural cedarwood oils from the gemstone fissures."
                    }
                }
            ]
        }
    ]
}

schema_block = f"""<!-- wp:html -->
<script type="application/ld+json">
{json.dumps(schema_json, indent=2, ensure_ascii=False)}
</script>
<!-- /wp:html -->"""

full_content = body_content.strip() + "\n\n" + schema_block

# Create WordPress post
post_payload = {
    'title': title,
    'slug': slug,
    'status': 'publish',
    'author': author_id,
    'categories': categories,
    'excerpt': meta_desc,
    'content': full_content,
    'featured_media': carousel_items[0]['media_id'],
    'meta': {
        '_yoast_wpseo_focuskw': 'panna stone ring',
        '_yoast_wpseo_title': "Panna Stone Ring Buying Guide 2026: Design, Quality & Settings",
        '_yoast_wpseo_metadesc': meta_desc
    }
}

req_create = urllib.request.Request(
    f'{api_base}/posts',
    data=json.dumps(post_payload).encode('utf-8'),
    headers=headers,
    method='POST'
)

with urllib.request.urlopen(req_create) as resp:
    post_res = json.loads(resp.read().decode())
    post_id = post_res['id']
    post_url = post_res['link']
    print(f"Successfully published post! ID: {post_id}")
    print(f"Live URL: {post_url}")
    with open(ROOT / 'output/week9_rank88_published_post.json', 'w') as out_f:
        json.dump(post_res, out_f, indent=2)

