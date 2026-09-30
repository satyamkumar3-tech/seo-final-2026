#!/usr/bin/env python3
"""Live QA for Week 3-4 Rank 11 through Rank 15 posts."""
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
MANIFESTS = [
    "output/Week34_Rank11_FriendshipDayMsg_type3_prompts.json",
    "output/Week34_Rank12_DevDiwaliWishes_type3_prompts.json",
    "output/Week34_Rank13_DiwaliWhatsapp_type3_prompts.json",
    "output/Week34_Rank14_RakhiGreetingCard_type3_prompts.json",
    "output/Week34_Rank15_NationalBestFriendsDay_type3_prompts.json",
]
OLD_OPTIMIZE_URLS = {
    "happy-dev-diwali-wishes-in-english-2026": "happy-fathers-day-wishes-quotes-and-messages-for-every-dad",
    "national-best-friends-day-wishes-2026": "happy-international-mens-day-best-quotes-wishes-messages",
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


def visible_text(rendered: str) -> str:
    text = re.sub(r"<(script|style)\b[^>]*>[\s\S]*?</\1>", " ", rendered, flags=re.I)
    return re.sub(r"<[^>]+>", " ", text)


def body_without_links(raw_content: str) -> str:
    body = re.sub(r"<a\b[^>]*>[\s\S]*?</a>", " ", raw_content, flags=re.I)
    body = re.sub(r"<(script|style)\b[^>]*>[\s\S]*?</\1>", " ", body, flags=re.I)
    return re.sub(r"<[^>]+>", " ", body)


def check_manifest(path: str) -> dict[str, bool]:
    manifest = json.loads((ROOT / path).read_text(encoding="utf-8"))
    post_id = manifest["wp_post_id"]
    slug = manifest["slug"]
    post = api(f"posts/{post_id}?context=edit")
    matches = api(f"posts?slug={slug}&status=publish,draft,pending,private,future&per_page=20")
    content = post["content"]["raw"]
    rendered = post["content"]["rendered"]
    image_blocks = re.findall(
        r"<!-- wp:image \{.*?\} -->\s*<figure.*?</figure>\s*<!-- /wp:image -->",
        content,
        flags=re.S,
    )
    image_block_html = "\n".join(image_blocks)
    text = visible_text(rendered)
    no_link_text = body_without_links(content)
    flatlay_file = Path(manifest["output"]["flatlay"]).name
    lifestyle_file = Path(manifest["output"]["lifestyle"]).name
    hero_file = Path(manifest["output"]["hero"]).name
    old_part = OLD_OPTIMIZE_URLS.get(slug)
    return {
        "slug_count_one": len(matches) == 1 and matches[0]["id"] == post_id,
        "status_publish": post["status"] == "publish",
        "featured_media_set": bool(post["featured_media"]),
        "two_body_image_blocks": len(image_blocks) == 2,
        "hero_not_repeated_in_body": hero_file not in image_block_html,
        "flatlay_filename": flatlay_file in image_block_html,
        "lifestyle_filename": lifestyle_file in image_block_html,
        "captions_present": manifest["slots"]["flatlay"]["caption"] in content and manifest["slots"]["lifestyle"]["caption"] in content,
        "six_buy_now": content.count(">Buy now<") == 6,
        "faq_schema": '"@type": "FAQPage"' in content,
        "blog_schema": '"@type": "BlogPosting"' in content,
        "primary_kw_visible": manifest["primary_kw"].lower() in text.lower(),
        "no_em_dash": "\u2014" not in text,
        "no_en_dash": "\u2013" not in text,
        "no_spaced_hyphen": re.search(r"\s-\s", text) is None,
        "no_old_years": re.search(r"\b(2021|2022|2023|2024|2025)\b", no_link_text) is None,
        "old_optimize_url_not_reused": (not old_part) or (old_part not in post["link"] and old_part not in content),
    }


def main() -> None:
    load_env()
    all_results = {}
    failed = {}
    for path in MANIFESTS:
        manifest = json.loads((ROOT / path).read_text(encoding="utf-8"))
        checks = check_manifest(path)
        all_results[manifest["slug"]] = checks
        bad = [key for key, ok in checks.items() if not ok]
        if bad:
            failed[manifest["slug"]] = bad
    print(json.dumps(all_results, indent=2))
    if failed:
        raise SystemExit(f"FAILED: {failed}")
    print("PASS", [f"https://blog.bluestone.com/{json.loads((ROOT / p).read_text())['slug']}/" for p in MANIFESTS])


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
