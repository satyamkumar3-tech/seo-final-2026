#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish Week 9 Rank 85 post to WordPress (stone necklace for women)."""
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

slug = 'stone-necklace-for-women-2026'
title = 'How to Choose and Style a Stone Necklace for Women: An Expert Buying Guide (2026)'
meta_desc = "Looking for the perfect stone necklace for women in 2026? Discover gemstone varieties, 18K vs 14K gold settings, net weight billing, length styling, and care tips."
author_id = 270271337
categories = [554493424, 554493465] # Gift (554493424), Jewellery Problem & Solution (554493465)

# 1. Exact slug check before creating
req_check = urllib.request.Request(f'{api_base}/posts?slug={slug}&status=any', headers=headers)
with urllib.request.urlopen(req_check) as resp:
    existing = json.loads(resp.read().decode())
    if existing:
        print(f"Post with slug {slug} already exists! ID: {existing[0]['id']}")
        with open(ROOT / 'output/week9_rank85_published_post.json', 'w') as out_f:
            json.dump(existing[0], out_f, indent=2)
        sys.exit(0)

with open(ROOT / 'output/week9_rank85_draft.html', encoding='utf-8') as f:
    body_content = f.read()

with open(ROOT / 'output/week9_rank85_carousel_media.json', encoding='utf-8') as f:
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
            "datePublished": "2026-09-28T10:30:00+05:30",
            "dateModified": "2026-09-28T10:30:00+05:30"
        },
        {
            "@type": "FAQPage",
            "@id": f"https://blog.bluestone.com/{slug}/#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "Which stone necklace is best for daily wear?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "For daily wear, stone necklaces crafted with durable minerals like rubies, sapphires (Mohs hardness 9), and diamonds set in 14K or 18K gold bezel settings are ideal. Bezel settings encase the gemstone perimeter smoothly, preventing snagging against clothing and providing unmatched stone security during active daily routines."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Why is 18K or 14K gold preferred over 22K for stone necklaces?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "22K gold contains 91.6% pure gold, making it relatively soft and malleable. Under the mechanical stress of daily wear, 22K gold prongs can bend or loosen, risking gemstone loss. 18K (75% gold) and 14K (58.5% gold) are alloyed with stronger metals like silver and copper, providing the high tensile rigidity necessary to grip gemstones permanently."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How does net weight billing work when buying a stone necklace?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Under Indian consumer protection and BIS guidelines, reputable jewellers must weigh the entire piece (gross weight) and deduct the exact weight of the gemstones to determine net gold weight. The gold price must be calculated solely on the net gold weight, while gemstones are billed separately based on their individual carat weight and quality."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How do I choose the right necklace length for my neckline?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Match your necklace length to the silhouette of your clothing. An 18-inch princess length necklace is universally flattering and sits gracefully below the collarbone for V-necks and collared shirts. A 14 to 16-inch choker is sensational with off-shoulder and sweetheart necklines, while 20 to 24-inch matinee chains elongate high-neck tops, sweaters, and traditional sarees."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Can I clean my stone necklace in an ultrasonic cleaner at home?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Ultrasonic cleaning is safe for hard, untreated gemstones like diamonds and unheated sapphires, but should never be used on emeralds, pearls, opals, or heavily included gemstones. Ultrasonic vibrations can shatter delicate fractures or strip natural protective oils from emeralds. Clean your jewellery safely at home using lukewarm water, mild soap, and a soft baby toothbrush."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How can I verify that the gemstones and gold in my necklace are authentic?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Verify gold authenticity by inspecting the mandatory BIS hallmarking triangle logo and the laser-etched 6-character Hallmark Unique Identification (HUID) code using the government BIS CARE mobile app. For gemstones, verify authenticity through independent gemmological laboratory certificates (such as IGI or SGL) provided with your BlueStone purchase."
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
        '_yoast_wpseo_focuskw': 'stone necklace for women',
        '_yoast_wpseo_title': f"Stone Necklace for Women: Expert Buying & Styling Guide (2026) | BlueStone",
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
    with open(ROOT / 'output/week9_rank85_published_post.json', 'w') as out_f:
        json.dump(post_res, out_f, indent=2)
