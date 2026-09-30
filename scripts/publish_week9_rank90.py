#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish Week 9 Rank 90 post to WordPress (earring styles for guys)."""
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

slug = 'earring-styles-for-guys-2026'
title = 'How to Choose Earring Styles for Guys: The 2026 Buying Guide'
meta_desc = "Discover modern earring styles for guys in 2026. From subtle gold studs and huggies to diamond accents and ear placement rules, find your signature look."
author_id = 270271337
categories = [554493434, 554493467, 554493465] # Men's Jewellery, Mens Earrings, Jewellery Problem & Solution

# 1. Exact slug check before creating
req_check = urllib.request.Request(f'{api_base}/posts?slug={slug}&status=any', headers=headers)
with urllib.request.urlopen(req_check) as resp:
    existing = json.loads(resp.read().decode())
    if existing:
        print(f"Post with slug {slug} already exists! ID: {existing[0]['id']}")
        with open(ROOT / 'output/week9_rank90_published_post.json', 'w') as out_f:
            json.dump(existing[0], out_f, indent=2)
        sys.exit(0)

with open(ROOT / 'output/week9_rank90_draft.html', encoding='utf-8') as f:
    full_content = f.read()

with open(ROOT / 'output/week9_rank90_carousel_media.json', encoding='utf-8') as f:
    carousel_items = json.load(f)

# Initial post payload
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
        '_yoast_wpseo_focuskw': 'earring styles for guys',
        '_yoast_wpseo_title': 'Earring Styles for Guys: 2026 Guide to Studs, Hoops & Placement | BlueStone',
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
    with open(ROOT / 'output/week9_rank90_published_post.json', 'w') as out_f:
        json.dump(post_res, out_f, indent=2)
