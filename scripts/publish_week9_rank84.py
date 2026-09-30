#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish Week 9 Rank 84 post to WordPress."""
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

slug = 'baby-wearing-earrings-2026'
title = 'Baby Wearing Earrings: Complete Safety, Gold Purity, and Style Guide (2026)'
meta_desc = "Planning for your baby wearing earrings in 2026? Learn paediatric readiness, safe gold purity, light weight earrings, screw-back closures, and aftercare tips."
author_id = 270271337
categories = [554493433, 554493465] # Kids Jewellery (554493433), Jewellery Problem & Solution (554493465)

# 1. Exact slug check before creating
req_check = urllib.request.Request(f'{api_base}/posts?slug={slug}', headers=headers)
with urllib.request.urlopen(req_check) as resp:
    existing = json.loads(resp.read().decode())
    if existing:
        print(f"Post with slug {slug} already exists! ID: {existing[0]['id']}")
        with open(ROOT / 'output/week9_rank84_published_post.json', 'w') as out_f:
            json.dump(existing[0], out_f, indent=2)
        sys.exit(0)

with open(ROOT / 'output/week9_rank84_draft.html', encoding='utf-8') as f:
    body_content = f.read()

with open(ROOT / 'output/week9_rank84_carousel_media.json', encoding='utf-8') as f:
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
            "datePublished": "2026-09-27T10:30:00+05:30",
            "dateModified": "2026-09-27T10:30:00+05:30"
        },
        {
            "@type": "FAQPage",
            "@id": f"https://blog.bluestone.com/{slug}/#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "What is the best age for a baby wearing earrings for the first time?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Paediatricians generally recommend waiting until the infant is at least two to three months of age and has received their initial DTaP and tetanus vaccinations. Waiting until this stage ensures that the baby's immune system has begun developing, reducing the risk of systemic infection following the piercing."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Which gold purity is best and safest for infant earrings?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Solid 14kt (58.5% pure gold) and 18kt (75% pure gold) are the safest options for infants. They are hypoallergenic, resistant to corrosion, and durable enough to maintain secure screw-lock threads. Avoid 22kt gold for daily infant wear because its extreme softness bends easily under gentle pressure, and strictly avoid gold-plated items that expose sensitive skin to irritating base metals."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Why are light weight earrings essential for babies?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "An infant's earlobes are made of delicate skin and soft adipose tissue. Light weight earrings weighing under 1.0 to 1.5 grams per pair ensure that the lobe does not stretch, tear, or become inflamed under excess gravitational load, allowing the piercing channel to heal symmetrically and comfortably."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Are screw-back earrings safe for babies to sleep in?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Yes, safety screw-back earrings with rounded, dome-shaped caps are specifically engineered for sleeping and daily wear. The closed cap completely encloses the sharp point of the earring post, preventing it from poking into the baby's neck, scalp, or mastoid area during naps or nighttime sleep."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Can a baby wear small hoops or dangling earrings?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "No, babies and toddlers under three years of age should never wear dangling earrings, chandeliers, or loose hoops. These styles can easily snag on swaddling blankets, clothing, or parents' knitwear, or be pulled by curious little hands, risking painful lobe tears and dangerous choking hazards. Stick to petite, smooth stud earrings with secure screw backs."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How should I clean my baby's ears after getting them pierced?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Clean the piercing twice daily using a sterile 0.9% saline solution applied gently with sterile medical gauze. Clean both the front of the earlobe around the stud and behind the lobe around the screw backing. Gently rotate the stud half a turn while cleaning to prevent the skin from adhering, and always pat the area completely dry after baths to prevent moisture accumulation."
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
        '_yoast_wpseo_focuskw': 'baby wearing earrings',
        '_yoast_wpseo_title': f"Baby Wearing Earrings: Complete Safety & Gold Guide (2026) | BlueStone",
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
    print(f"SUCCESS: Post created with ID {post_id} at {post_url}")
    with open(ROOT / 'output/week9_rank84_published_post.json', 'w') as out_f:
        json.dump(post_res, out_f, indent=2)
