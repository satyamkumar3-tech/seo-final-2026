#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Complete all remaining steps for Week 8 Rank 168: Amethyst Rings Buying Guide 2026."""

import base64
import json
import os
import re
import urllib.request
from pathlib import Path

ROOT = Path("/Users/satyamkumar/Downloads/final seo generation context")
WORKSPACE = Path("/Users/satyamkumar/Downloads/seo final 2026")

# Load environment
env_path = ROOT / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

USER = os.environ.get("WP_USER", "blogbluestone")
PWD = os.environ.get("WP_APP_PASSWORD") or os.environ.get("WP_APP_PASS") or os.environ.get("WP_PASSWORD", "")
token = base64.b64encode(f"{USER}:{PWD}".encode()).decode()
headers = {"Authorization": f"Basic {token}", "User-Agent": "BluestoneSEO/1.0"}

TITLE = "Amethyst Rings Buying Guide 2026: Purple Gemstone Quality, Gold Purity, Designs & Everyday Care"
SLUG = "amethyst-rings-2026"
PRIMARY_KEYWORD = "amethyst rings"

manifest_path = ROOT / "output/Week8_Rank168_type3_manifest.json"
publish_info_path = ROOT / "output/Week8_Rank168_publish_info.json"
type3_media_path = ROOT / "output/Week8_Rank168_type3_media.json"

MANIFEST = json.loads(manifest_path.read_text(encoding="utf-8"))
publish_info = json.loads(publish_info_path.read_text(encoding="utf-8"))
post_id = publish_info["post_id"]

def upload_media(file_path: Path, title: str, alt: str):
    filename = file_path.name
    search_url = f"https://blog.bluestone.com/wp-json/wp/v2/media?search={filename}"
    req_search = urllib.request.Request(search_url, headers=headers)
    try:
        with urllib.request.urlopen(req_search, timeout=30) as resp:
            results = json.loads(resp.read().decode())
            for item in results:
                if filename in item.get("source_url", ""):
                    print(f"Found existing media for {filename}: ID {item['id']}")
                    return item["id"], item["source_url"]
    except Exception as e:
        print(f"Media search error for {filename}: {e}")

    with open(file_path, "rb") as f:
        file_data = f.read()

    h = dict(headers)
    h["Content-Type"] = "image/webp"
    h["Content-Disposition"] = f'attachment; filename="{filename}"'

    req_upload = urllib.request.Request(
        "https://blog.bluestone.com/wp-json/wp/v2/media",
        data=file_data,
        headers=h,
        method="POST"
    )
    with urllib.request.urlopen(req_upload, timeout=60) as resp:
        res = json.loads(resp.read().decode())
        media_id = res["id"]
        source_url = res["source_url"]
        print(f"Uploaded {filename} -> ID {media_id}")

    update_data = json.dumps({"title": title, "alt_text": alt}).encode("utf-8")
    h_update = dict(headers)
    h_update["Content-Type"] = "application/json"
    req_update = urllib.request.Request(
        f"https://blog.bluestone.com/wp-json/wp/v2/media/{media_id}",
        data=update_data,
        headers=h_update,
        method="POST"
    )
    try:
        with urllib.request.urlopen(req_update, timeout=30) as resp_up:
            pass
    except Exception as e:
        print(f"Failed to update metadata for ID {media_id}: {e}")

    return media_id, source_url

def main():
    print(f"--- Uploading Type 3 Media for {SLUG} (Post ID {post_id}) ---")

    slots = MANIFEST["slots"]
    uploaded = {}

    for slot_name in ["hero", "flatlay", "lifestyle"]:
        slot_info = slots[slot_name]
        webp_path = ROOT / slot_info["output_webp"]
        if not webp_path.exists():
            raise FileNotFoundError(f"WebP file not found: {webp_path}")

        m_id, m_url = upload_media(
            file_path=webp_path,
            title=slot_info["media_title"],
            alt=slot_info["alt"]
        )
        uploaded[slot_name] = {
            "id": m_id,
            "url": m_url,
            "alt": slot_info["alt"],
            "title": slot_info["media_title"],
            "caption": slot_info.get("caption", ""),
            "pdp_url": slot_info.get("pdp_url", "")
        }

    type3_media_path.write_text(json.dumps(uploaded, indent=2), encoding="utf-8")
    print(f"Saved Type 3 media info to {type3_media_path}")

    # Load article with carousel
    article_path = ROOT / "output/Week8_Rank168_AmethystRings_article_with_carousel.html"
    content = article_path.read_text(encoding="utf-8")

    # Format Gutenberg Block for Flatlay (custom PDP link + figure caption)
    flatlay_info = uploaded["flatlay"]
    flatlay_block = f"""<!-- wp:image {{"id":{flatlay_info['id']},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{flatlay_info['pdp_url']}"><img src="{flatlay_info['url']}" alt="{flatlay_info['alt']}" class="wp-image-{flatlay_info['id']}"/></a><figcaption>{flatlay_info['caption']}</figcaption></figure>
<!-- /wp:image -->"""

    # Format Gutenberg Block for Lifestyle (custom PDP link + figure caption)
    lifestyle_info = uploaded["lifestyle"]
    lifestyle_block = f"""<!-- wp:image {{"id":{lifestyle_info['id']},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{lifestyle_info['pdp_url']}"><img src="{lifestyle_info['url']}" alt="{lifestyle_info['alt']}" class="wp-image-{lifestyle_info['id']}"/></a><figcaption>{lifestyle_info['caption']}</figcaption></figure>
<!-- /wp:image -->"""

    content = content.replace("<!-- TYPE3_FLATLAY_PLACEHOLDER -->", flatlay_block)
    content = content.replace("<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->", lifestyle_block)

    # Update BlogPosting schema images
    hero_url = uploaded["hero"]["url"]
    flatlay_url = uploaded["flatlay"]["url"]
    lifestyle_url = uploaded["lifestyle"]["url"]

    # Replace the image array in the schema
    content = re.sub(
        r'"image":\s*\[\s*"[^"]*",\s*"[^"]*",\s*"[^"]*"\s*\]',
        f'"image": [\n        "{hero_url}",\n        "{flatlay_url}",\n        "{lifestyle_url}"\n      ]',
        content
    )

    # Save final patched article
    final_path = ROOT / "output/Week8_Rank168_AmethystRings_article_final.html"
    final_path.write_text(content, encoding="utf-8")
    print(f"Saved final article to {final_path}")

    # Patch WordPress Post
    hero_id = uploaded["hero"]["id"]
    print(f"Updating WordPress post {post_id} with featured_media {hero_id} and patched content...")

    patch_payload = {
        "featured_media": hero_id,
        "content": content,
        "meta": {
            "_yoast_wpseo_focuskw": PRIMARY_KEYWORD,
            "_yoast_wpseo_title": f"Amethyst Rings Buying Guide 2026: Purple Gemstone Quality & Care %%page%% %%sep%% %%sitename%%",
            "_yoast_wpseo_metadesc": (
                "Comprehensive 2026 buying guide to amethyst rings. "
                "Explore purple hue depth, 18Kt vs 14Kt gold settings, Mohs hardness, certified diamonds & BIS hallmarking."
            ),
            "_yoast_wpseo_canonical": f"https://blog.bluestone.com/{SLUG}/",
            "_yoast_wpseo_opengraph-image": hero_url,
            "_yoast_wpseo_opengraph-image-id": str(hero_id),
            "_yoast_wpseo_twitter-image": hero_url,
            "_yoast_wpseo_twitter-image-id": str(hero_id)
        }
    }

    h_patch = dict(headers)
    h_patch["Content-Type"] = "application/json"
    req_patch = urllib.request.Request(
        f"https://blog.bluestone.com/wp-json/wp/v2/posts/{post_id}",
        data=json.dumps(patch_payload).encode("utf-8"),
        headers=h_patch,
        method="POST"
    )

    with urllib.request.urlopen(req_patch, timeout=60) as resp:
        res_post = json.loads(resp.read().decode())
        print(f"Successfully updated post ID {res_post['id']} at {res_post.get('link')}")

    print("Type 3 images and social metadata successfully patched into WordPress!")

if __name__ == "__main__":
    main()
