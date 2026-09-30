#!/usr/bin/env python3
"""Live QA for Week 3-4 Rank 4 and Rank 5 posts."""
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
POSTS = [
    {
        "name": "rank4",
        "slug": "emotional-friendship-day-quotes-2026",
        "post_id": 32312,
        "primary_kw": "emotional friendship day quotes",
        "hero": "emotional-friendship-day-quotes-hero-2026.webp",
        "flatlay": "emotional-friendship-day-quotes-flatlay-2026.webp",
        "lifestyle": "emotional-friendship-day-quotes-lifestyle-2026.webp",
        "caption_a": "Friendship Day quotes 2026 vibe",
        "caption_b": "Friendship Day quotes 2026 look",
        "old_url_part": "happy-fathers-day-wishes-quotes-and-messages-for-every-dad",
    },
    {
        "name": "rank5",
        "slug": "best-gift-for-sister-on-raksha-bandhan-2026",
        "post_id": 32319,
        "primary_kw": "best gift for sister on raksha bandhan",
        "hero": "best-gift-for-sister-on-raksha-bandhan-hero-2026.webp",
        "flatlay": "best-gift-for-sister-on-raksha-bandhan-flatlay-2026.webp",
        "lifestyle": "best-gift-for-sister-on-raksha-bandhan-lifestyle-2026.webp",
        "caption_a": "Rakhi gift for sister 2026 vibe",
        "caption_b": "Rakhi gift for sister 2026 look",
        "old_url_part": "why-rakhi-gifts-arent-just-for-sisters-unique-raksha-bandhan-gift-ideas-for-brothers",
    },
]


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


def check_post(cfg: dict[str, object]) -> dict[str, bool]:
    post = api(f"posts/{cfg['post_id']}?context=edit")
    matches = api(f"posts?slug={cfg['slug']}&status=publish,draft,pending,private,future&per_page=20")
    content = post["content"]["raw"]
    rendered = post["content"]["rendered"]
    image_blocks = re.findall(r"<!-- wp:image \{.*?\} -->\s*<figure.*?</figure>\s*<!-- /wp:image -->", content, flags=re.S)
    image_block_html = "\n".join(image_blocks)
    text = re.sub(r"<(script|style)\b[^>]*>[\s\S]*?</\1>", " ", rendered, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return {
        "slug_count_one": len(matches) == 1 and matches[0]["id"] == cfg["post_id"],
        "status_publish": post["status"] == "publish",
        "featured_media_set": bool(post["featured_media"]),
        "two_body_image_blocks": len(image_blocks) == 2,
        "hero_not_repeated_in_body": str(cfg["hero"]) not in image_block_html,
        "flatlay_filename": str(cfg["flatlay"]) in image_block_html,
        "lifestyle_filename": str(cfg["lifestyle"]) in image_block_html,
        "captions_present": str(cfg["caption_a"]) in content and str(cfg["caption_b"]) in content,
        "six_buy_now": content.count(">Buy now<") == 6,
        "faq_schema": '"@type": "FAQPage"' in content,
        "blog_schema": '"@type": "BlogPosting"' in content,
        "primary_kw_visible": str(cfg["primary_kw"]).lower() in text.lower(),
        "no_em_dash": "\u2014" not in text,
        "no_en_dash": "\u2013" not in text,
        "no_spaced_hyphen": re.search(r"\s-\s", text) is None,
        "no_old_years": re.search(r"\b(2021|2022|2023|2024|2025)\b", text) is None,
        "no_old_url": str(cfg["old_url_part"]) not in content,
    }


def main() -> None:
    load_env()
    all_results = {}
    failed = {}
    for cfg in POSTS:
        checks = check_post(cfg)
        all_results[str(cfg["name"])] = checks
        bad = [k for k, v in checks.items() if not v]
        if bad:
            failed[str(cfg["name"])] = bad
    print(json.dumps(all_results, indent=2))
    if failed:
        raise SystemExit(f"FAILED: {failed}")
    print("PASS", [f"https://blog.bluestone.com/{p['slug']}/" for p in POSTS])


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
