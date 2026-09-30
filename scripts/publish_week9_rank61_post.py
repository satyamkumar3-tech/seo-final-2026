#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish Week 9 Rank 61 post to WordPress."""
import os, sys, json, base64, urllib.request
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]

# Load .env
env_paths = [ROOT / '.env', Path('/Users/satyamkumar/Downloads/seo final 2026/.env')]
for ep in env_paths:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

WP_USER = os.environ.get('WP_USER', 'blogbluestone')
WP_PASS = os.environ.get('WP_APP_PASSWORD') or os.environ.get('WP_APP_PASS') or os.environ.get('WP_PASSWORD', '')
WP_URL = os.environ.get('WP_URL', 'https://blog.bluestone.com')
TOKEN = base64.b64encode(f"{WP_USER}:{WP_PASS}".encode()).decode()
HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0",
    "Content-Type": "application/json"
}

def api(method, path, data=None):
    url = f"{WP_URL}/wp-json/wp/v2/{path}"
    body = json.dumps(data).encode('utf-8') if data else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode('utf-8'))

# Read draft content
draft_file = ROOT / "output" / "week9_rank61_draft.html"
if not draft_file.exists():
    raise SystemExit(f"Draft file not found: {draft_file}")

content = draft_file.read_text(encoding='utf-8')

meta_file = ROOT / "output" / "week9_rank61_meta.json"
meta = json.loads(meta_file.read_text(encoding='utf-8'))

title = meta["title"]
slug = meta["slug"]
focus_kw = meta["focus_kw"]
meta_desc = meta["meta_desc"]
author_id = meta["author_id"]
categories = meta["categories"]

print(f"Checking for existing posts with slug: {slug}...")
existing = api("GET", f"posts?slug={quote(slug)}&context=edit&status=any&per_page=10")
if existing:
    post = existing[0]
    print(f"Found existing matching post ID {post['id']}: {post['link']}")
else:
    print("No existing post found. Creating NEW WordPress post...")
    payload = {
        "title": title,
        "slug": slug,
        "status": "publish",
        "author": author_id,
        "categories": categories,
        "content": content,
        "excerpt": meta_desc,
        "meta": {
            "_yoast_wpseo_focuskw": focus_kw,
            "_yoast_wpseo_title": title,
            "_yoast_wpseo_metadesc": meta_desc,
        }
    }
    post = api("POST", "posts", payload)
    print(f"Created post ID {post['id']} successfully: {post['link']}")

# Record post details
result = {
    "post_id": post["id"],
    "slug": slug,
    "link": post["link"],
    "title": title,
    "status": post["status"],
    "author": post["author"],
    "categories": post["categories"]
}

post_record_path = ROOT / "output" / "week9_rank61_post_info.json"
post_record_path.write_text(json.dumps(result, indent=2), encoding='utf-8')
print(f"Recorded post info to: {post_record_path}")
