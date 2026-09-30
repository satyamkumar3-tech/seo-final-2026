#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish Week 9 Rank 71 post to WordPress."""
import os
import sys
import json
import base64
import urllib.request
import urllib.error
import time
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]

# Load environment
for ep in [ROOT / ".env", Path("/Users/satyamkumar/Downloads/seo final 2026/.env")]:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

WP_USER = os.environ.get("WP_USER", "blogbluestone")
WP_PASS = os.environ.get("WP_APP_PASSWORD") or os.environ.get("WP_APP_PASS") or os.environ.get("WP_PASSWORD", "")
WP_URL = os.environ.get("WP_URL", "https://blog.bluestone.com")
TOKEN = base64.b64encode(f"{WP_USER}:{WP_PASS}".encode()).decode()
WP_API = f"{WP_URL}/wp-json/wp/v2"

HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0",
    "Content-Type": "application/json"
}

def req_with_retry(req, max_retries=5, initial_delay=3):
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return resp.status, resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"HTTP 429 received. Waiting {delay}s before retry (attempt {attempt+1}/{max_retries})...")
                time.sleep(delay)
                delay *= 2
            else:
                print(f"HTTP error {e.code}: {e.reason}")
                raise e
    raise Exception("Max retries exceeded for request")

def check_existing_post(slug: str):
    url = f"{WP_API}/posts?slug={quote(slug)}&status=any"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        status, body = req_with_retry(req)
        posts = json.loads(body.decode())
        if posts:
            p = posts[0]
            return p["id"], p["link"]
    except Exception as e:
        print(f"Error checking existing slug: {e}")
    return None, None

def main():
    draft_file = ROOT / "output" / "week9_rank71_draft.json"
    if not draft_file.exists():
        raise FileNotFoundError(f"Missing draft file at {draft_file}")

    with open(draft_file, "r", encoding="utf-8") as f:
        draft = json.load(f)

    slug = draft["slug"]
    title = draft["title"]
    content = draft["content"]
    focus_kw = draft["focus_kw"]
    meta_title = draft["meta_title"]
    meta_desc = draft["meta_desc"]

    # Check if post already exists
    post_id, post_url = check_existing_post(slug)

    post_data = {
        "title": title,
        "slug": slug,
        "content": content,
        "status": "publish",
        "author": 270271337,  # Satyam
        "categories": [554493348, 554493465],  # Gold, Jewellery Problem & Solution
        "meta": {
            "_yoast_wpseo_focuskw": focus_kw,
            "_yoast_wpseo_title": meta_title,
            "_yoast_wpseo_metadesc": meta_desc
        }
    }

    if post_id:
        print(f"Post already exists with ID: {post_id}. Updating post...")
        req = urllib.request.Request(
            f"{WP_API}/posts/{post_id}",
            data=json.dumps(post_data).encode(),
            headers=HEADERS,
            method="POST"
        )
    else:
        print(f"Creating new post for slug: {slug}...")
        req = urllib.request.Request(
            f"{WP_API}/posts",
            data=json.dumps(post_data).encode(),
            headers=HEADERS,
            method="POST"
        )

    status, body = req_with_retry(req)
    res = json.loads(body.decode())
    published_id = res["id"]
    published_url = res["link"]

    print(f"\nSuccessfully published post!")
    print(f"Post ID: {published_id}")
    print(f"Live URL: {published_url}")

    out_record = {
        "post_id": published_id,
        "url": published_url,
        "slug": slug,
        "title": title,
        "author_id": 270271337,
        "author_name": "Satyam",
        "categories": [554493348, 554493465],
        "word_count": draft["word_count"],
        "published_at": res.get("date_gmt", "")
    }

    out_file = ROOT / "output" / "week9_rank71_post_published.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(out_record, f, indent=2)

    print(f"Saved publication record to {out_file}")
    return out_record

if __name__ == "__main__":
    main()
