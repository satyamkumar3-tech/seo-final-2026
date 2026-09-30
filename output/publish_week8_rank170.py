#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish script for Week 8 Rank 170: Real Diamond Rings Buying Guide 2026."""
import os
import sys
import json
import base64
import urllib.request
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TITLE = "Real Diamond Rings Buying Guide 2026: Authentication, 4Cs, Setting Security & Buyer Checklist"
SEO_TITLE = "Real Diamond Rings Buying Guide 2026: Authentication & 4Cs | BlueStone"
META_DESC = "Learn how to choose authentic real diamond rings in 2026. Explore verification tests, 4Cs grading, 18Kt vs 14Kt gold mountings, and certified designs for men and women."
SLUG = "real-diamond-rings-2026"
AUTHOR_ID = 270271337  # Satyam
CATEGORIES = [554493348, 554493465]  # Gold + Jewellery Problem & Solution
PRIMARY_KEYWORD = "real diamond rings"

def load_env():
    env_file = ROOT / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

load_env()
USER = os.environ.get("WP_USER", "")
PWD = os.environ.get("WP_APP_PASSWORD", "")
TOKEN = base64.b64encode(f"{USER}:{PWD}".encode()).decode() if USER and PWD else ""
AUTH_HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0",
    "Content-Type": "application/json"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"

def check_existing_post(slug: str):
    query = urllib.parse.urlencode({"slug": slug, "status": "publish,draft,pending,private,future"})
    req = urllib.request.Request(f"{WP_API}/posts?{query}", headers=AUTH_HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        posts = json.loads(resp.read().decode())
    return posts

def publish():
    existing = check_existing_post(SLUG)
    if existing:
        print(f"ERROR: Post already exists with slug '{SLUG}': ID={existing[0]['id']}, Link={existing[0]['link']}")
        out_info = {
            "post_id": existing[0]["id"],
            "slug": SLUG,
            "link": existing[0]["link"],
            "title": TITLE,
            "author": AUTHOR_ID,
            "categories": CATEGORIES,
            "primary_kw": PRIMARY_KEYWORD
        }
        with open(ROOT / "output/week8_rank170_wp_post.json", "w") as f:
            json.dump(out_info, f, indent=2)
        return out_info

    article_path = ROOT / "output/week8_rank170_article_content.html"
    if not article_path.exists():
        raise FileNotFoundError(f"Article HTML not found at {article_path}")

    full_content = article_path.read_text(encoding="utf-8")

    post_payload = {
        "title": TITLE,
        "slug": SLUG,
        "content": full_content,
        "author": AUTHOR_ID,
        "categories": CATEGORIES,
        "status": "publish",
        "meta": {
            "_yoast_wpseo_focuskw": PRIMARY_KEYWORD,
            "_yoast_wpseo_title": SEO_TITLE,
            "_yoast_wpseo_metadesc": META_DESC
        }
    }

    req = urllib.request.Request(
        f"{WP_API}/posts",
        data=json.dumps(post_payload).encode(),
        headers=AUTH_HEADERS,
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        created = json.loads(resp.read().decode())

    post_id = created["id"]
    post_link = created["link"]
    print(f"SUCCESS: Published post ID {post_id} at {post_link}")

    out_info = {
        "post_id": post_id,
        "slug": SLUG,
        "link": post_link,
        "title": TITLE,
        "author": AUTHOR_ID,
        "categories": CATEGORIES,
        "primary_kw": PRIMARY_KEYWORD
    }
    with open(ROOT / "output/week8_rank170_wp_post.json", "w") as f:
        json.dump(out_info, f, indent=2)
    return out_info

if __name__ == "__main__":
    publish()
