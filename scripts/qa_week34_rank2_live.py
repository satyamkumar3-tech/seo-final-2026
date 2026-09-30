#!/usr/bin/env python3
"""Live QA for Week 3-4 Rank 2 post."""
from __future__ import annotations

import base64
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://blog.bluestone.com/wp-json/wp/v2"
SLUG = "diwali-quotes-for-instagram-2026"
POST_ID = 31824


def load_env() -> None:
    for raw in (ROOT / ".env").read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def api(path: str):
    token = base64.b64encode(f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD']}".encode()).decode()
    req = urllib.request.Request(
        f"{API}/{path}",
        headers={"Authorization": f"Basic {token}", "User-Agent": "BluestoneSEO/1.0"},
    )
    with urllib.request.urlopen(req, timeout=90) as response:
        return json.loads(response.read().decode())


def main() -> None:
    load_env()
    post = api(f"posts/{POST_ID}?context=edit")
    matches = api(f"posts?slug={SLUG}&status=publish,draft,pending,private,future&per_page=20")
    content = post["content"]["raw"]
    rendered = post["content"]["rendered"]
    image_blocks = re.findall(r"<!-- wp:image \{.*?\} -->\s*<figure.*?</figure>\s*<!-- /wp:image -->", content, flags=re.S)
    image_block_html = "\n".join(image_blocks)
    text = re.sub(r"<(script|style)\b[^>]*>[\s\S]*?</\1>", " ", rendered, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    checks = {
        "slug_count_one": len(matches) == 1 and matches[0]["id"] == POST_ID,
        "status_publish": post["status"] == "publish",
        "featured_media_set": bool(post["featured_media"]),
        "two_body_image_blocks": len(image_blocks) == 2,
        "hero_not_repeated_in_body": "diwali-quotes-for-instagram-hero-2026.webp" not in image_block_html,
        "flatlay_filename": "diwali-quotes-for-instagram-flatlay-2026.webp" in image_block_html,
        "lifestyle_filename": "diwali-quotes-for-instagram-lifestyle-2026.webp" in image_block_html,
        "captions_present": "Diwali quotes for Instagram 2026 flatlay" in content
        and "Diwali quotes for Instagram 2026 look" in content,
        "six_buy_now": content.count(">Buy now<") == 6,
        "faq_schema": '"@type": "FAQPage"' in content,
        "blog_schema": '"@type": "BlogPosting"' in content,
        "primary_kw_visible": "diwali quotes for instagram" in text.lower(),
        "no_em_dash": "\u2014" not in text,
        "no_en_dash": "\u2013" not in text,
        "no_spaced_hyphen": re.search(r"\s-\s", text) is None,
        "no_old_years": re.search(r"\b(2021|2022|2023|2024|2025)\b", text) is None,
        "no_old_url": "best-diwali-wishes-messages-quotes" not in content,
    }
    print(json.dumps(checks, indent=2))
    failed = [k for k, v in checks.items() if not v]
    if failed:
        raise SystemExit(f"FAILED: {failed}")
    print("PASS", post["link"], "featured_media", post["featured_media"])


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
