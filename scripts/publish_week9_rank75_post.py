#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish Week 9 Rank 75 post to WordPress."""
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
    draft_json_path = ROOT / "output" / "week9_rank75_draft.json"
    if not draft_json_path.exists():
        raise FileNotFoundError(f"Missing draft json at {draft_json_path}")

    with open(draft_json_path, "r", encoding="utf-8") as f:
        draft = json.load(f)

    slug = draft["slug"]
    title = draft["title"]
    content = draft["content"]
    focus_kw = draft["primary_kw"]
    meta_title = f"{title} | BlueStone"
    meta_desc = draft["meta_desc"]

    # Check if post already exists
    post_id, post_url = check_existing_post(slug)

    post_data = {
        "title": title,
        "slug": slug,
        "content": content,
        "status": "publish",
        "author": 270271337,  # Satyam
        "categories": [554493453, 554493465, 554493348],  # Pendant, Jewellery Problem & Solution, Gold
        "featured_media": 40293,  # Initial featured image (The Aagarna Pendant) until Type 3 hero is patched
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
            data=json.dumps(post_data).encode("utf-8"),
            headers=HEADERS,
            method="POST"
        )
    else:
        print(f"Creating new post for slug: {slug}...")
        req = urllib.request.Request(
            f"{WP_API}/posts",
            data=json.dumps(post_data).encode("utf-8"),
            headers=HEADERS,
            method="POST"
        )

    status, body = req_with_retry(req)
    res = json.loads(body.decode())
    new_post_id = res["id"]
    new_post_url = res["link"]

    print(f"\nSuccessfully published post!")
    print(f"Post ID: {new_post_id}")
    print(f"Live URL: {new_post_url}")

    pub_info = {
        "post_id": new_post_id,
        "post_url": new_post_url,
        "slug": slug,
        "title": title,
        "author": 270271337,
        "categories": [554493453, 554493465, 554493348],
        "published_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }

    out_path = ROOT / "output" / "week9_rank75_published_post.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(pub_info, f, indent=2)

    return pub_info

if __name__ == "__main__":
    main()
