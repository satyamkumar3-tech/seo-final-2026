#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish Week 9 Rank 79 to WordPress."""
import json
import os
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

with open(ROOT / 'output/Week9_Rank79_draft.json', encoding='utf-8') as f:
    draft = json.load(f)

slug = draft['slug']

# 1. Exact slug check before creating
req_check = urllib.request.Request(f'{api_base}/posts?slug={slug}', headers=headers)
with urllib.request.urlopen(req_check) as resp:
    existing = json.loads(resp.read().decode())
    if existing:
        print(f"Post with slug {slug} already exists! ID: {existing[0]['id']}")
        with open(ROOT / 'output/week9_rank79_published_post.json', 'w') as out_f:
            json.dump(existing[0], out_f, indent=2)
        exit(0)

# 2. Create post
post_payload = {
    'title': draft['title'],
    'slug': slug,
    'status': 'publish',
    'author': draft['author_id'],
    'categories': draft['categories'],
    'excerpt': draft['meta_desc'],
    'content': draft['content'],
    'featured_media': 40341,  # Initial featured media (The Ailia Evil Eye Layered Necklace)
    'meta': {
        '_yoast_wpseo_focuskw': draft['primary_kw'],
        '_yoast_wpseo_title': f"{draft['meta_title']} | BlueStone",
        '_yoast_wpseo_metadesc': draft['meta_desc']
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
    with open(ROOT / 'output/week9_rank79_published_post.json', 'w') as out_f:
        json.dump(post_res, out_f, indent=2)
