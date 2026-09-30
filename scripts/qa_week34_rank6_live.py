#!/usr/bin/env python3
"""Live QA for Week 3-4 Rank 6 post."""
from __future__ import annotations

import base64
import json
import os
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://blog.bluestone.com/wp-json/wp/v2"
CFG = {
    "slug": "happy-womens-day-wishes-quotes-2027",
    "post_id": 32352,
    "primary_kw": "happy womens day wishes quotes",
    "hero": "happy-womens-day-wishes-quotes-hero-2027.webp",
    "flatlay": "happy-womens-day-wishes-quotes-flatlay-2027.webp",
    "lifestyle": "happy-womens-day-wishes-quotes-lifestyle-2027.webp",
    "caption_a": "Womens Day wishes 2027 vibe",
    "caption_b": "Womens Day wishes 2027 look",
    "old_url_part": "happy-womens-day-quotes-wishes-and-messages-to-celebrate-strength-and-empowerment",
}


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
    post = api(f"posts/{CFG['post_id']}?context=edit")
    matches = api(f"posts?slug={CFG['slug']}&status=publish,draft,pending,private,future&per_page=20")
    content = post["content"]["raw"]
    rendered = post["content"]["rendered"]
    image_blocks = re.findall(r"<!-- wp:image \{.*?\} -->\s*<figure.*?</figure>\s*<!-- /wp:image -->", content, flags=re.S)
    image_block_html = "\n".join(image_blocks)
    text = re.sub(r"<(script|style)\b[^>]*>[\s\S]*?</\1>", " ", rendered, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    checks = {
        "slug_count_one": len(matches) == 1 and matches[0]["id"] == CFG["post_id"],
        "status_publish": post["status"] == "publish",
        "featured_media_set": bool(post["featured_media"]),
        "two_body_image_blocks": len(image_blocks) == 2,
        "hero_not_repeated_in_body": CFG["hero"] not in image_block_html,
        "flatlay_filename": CFG["flatlay"] in image_block_html,
        "lifestyle_filename": CFG["lifestyle"] in image_block_html,
        "captions_present": CFG["caption_a"] in content and CFG["caption_b"] in content,
        "six_buy_now": content.count(">Buy now<") == 6,
        "faq_schema": '"@type": "FAQPage"' in content,
        "blog_schema": '"@type": "BlogPosting"' in content,
        "primary_kw_visible": CFG["primary_kw"].lower() in text.lower(),
        "no_em_dash": "\u2014" not in text,
        "no_en_dash": "\u2013" not in text,
        "no_spaced_hyphen": re.search(r"\s-\s", text) is None,
        "no_old_years": re.search(r"\b(2021|2022|2023|2024|2025|2026)\b", text) is None,
        "no_old_url": CFG["old_url_part"] not in content,
    }
    print(json.dumps(checks, indent=2))
    failed = [key for key, passed in checks.items() if not passed]
    if failed:
        raise SystemExit(f"FAILED: {failed}")
    print(f"PASS https://blog.bluestone.com/{CFG['slug']}/")


if __name__ == "__main__":
    main()
