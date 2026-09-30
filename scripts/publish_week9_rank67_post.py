#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish Week 9 Rank 67 post to WordPress."""
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
HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0",
    "Content-Type": "application/json"
}

def api(method, path, data=None):
    url = f"{WP_URL}/wp-json/wp/v2/{path}"
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main():
    draft_file = ROOT / "output" / "Week9_Rank67_gold_hoop_earrings_draft.json"
    if not draft_file.exists():
        raise SystemExit(f"Draft file not found: {draft_file}")

    draft = json.loads(draft_file.read_text(encoding="utf-8"))

    title = draft["title"]
    slug = draft["slug"]
    focus_kw = draft["focus_keyphrase"]
    meta_desc = draft["meta_description"]
    author_id = draft["author_id"]
    categories = draft["categories"]
    content = draft["raw_content"]

    print(f"Checking for existing posts with slug: {slug}...")
    existing = api("GET", f"posts?slug={quote(slug)}&context=edit&status=any&per_page=10")
    if existing:
        post = existing[0]
        print(f"Found existing matching post ID {post['id']}: {post['link']}")
        post_id = post["id"]
        post_link = post["link"]
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
                "_yoast_wpseo_title": f"{title} | BlueStone",
                "_yoast_wpseo_metadesc": meta_desc
            }
        }
        res = api("POST", "posts", payload)
        post_id = res["id"]
        post_link = res["link"]
        print(f"Post created successfully! ID: {post_id}, Link: {post_link}")

    # Verify public link
    time.sleep(2)
    verify_req = urllib.request.Request(post_link, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(verify_req, timeout=30) as resp:
            print(f"Live post URL check status: {resp.status}")
    except urllib.error.HTTPError as e:
        print(f"Live post URL check HTTP {e.code}")

    # Save publish result
    result = {
        "post_id": post_id,
        "slug": slug,
        "link": post_link,
        "title": title,
        "author": author_id,
        "categories": categories,
        "published_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    res_path = ROOT / "output" / "Week9_Rank67_publish_result.json"
    res_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"Publish metadata saved to {res_path}")

if __name__ == "__main__":
    main()
