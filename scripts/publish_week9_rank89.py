#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish Week 9 Rank 89 post to WordPress (daily wear gold earrings for women)."""
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

slug = 'daily-wear-gold-earrings-for-women-2026'
title = 'How to Choose Daily Wear Gold Earrings for Women: The 2026 Buying Guide'
meta_desc = "Discover how to choose daily wear gold earrings for women in 2026. Explore lightweight designs, 14K vs 18K gold, secure screw backs, and earlobe comfort tips."
author_id = 270271337
categories = [554493348, 554493465] # Gold (554493348), Jewellery Problem & Solution (554493465)

# 1. Exact slug check before creating
req_check = urllib.request.Request(f'{api_base}/posts?slug={slug}&status=any', headers=headers)
with urllib.request.urlopen(req_check) as resp:
    existing = json.loads(resp.read().decode())
    if existing:
        print(f"Post with slug {slug} already exists! ID: {existing[0]['id']}")
        with open(ROOT / 'output/week9_rank89_published_post.json', 'w') as out_f:
            json.dump(existing[0], out_f, indent=2)
        sys.exit(0)

with open(ROOT / 'output/week9_rank89_draft.html', encoding='utf-8') as f:
    full_content = f.read()

with open(ROOT / 'output/week9_rank89_carousel_media.json', encoding='utf-8') as f:
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
        '_yoast_wpseo_focuskw': 'daily wear gold earrings for women',
        '_yoast_wpseo_title': 'Daily Wear Gold Earrings for Women: 2026 Buying Guide | BlueStone',
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
    with open(ROOT / 'output/week9_rank89_published_post.json', 'w') as out_f:
        json.dump(post_res, out_f, indent=2)
