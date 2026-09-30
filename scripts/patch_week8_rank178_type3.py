#!/usr/bin/env python3
"""Upload Type 3 images and patch WordPress Post 39077 for Week 8 Rank 178."""
import os
import re
import sys
import json
import base64
import urllib.request
from pathlib import Path

ROOT = Path("/Users/satyamkumar/Downloads/seo final 2026")
POST_ID = 39077
SLUG = "finger-rings-for-girls-2026"

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
TOKEN = base64.b64encode(f"{USER}:{PWD}".encode()).decode()
AUTH_HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"


def upload_media(path: Path, alt: str, title: str):
    filename = path.name
    # Check if existing
    search_url = f"{WP_API}/media?search={filename}&per_page=10"
    req_s = urllib.request.Request(search_url, headers=AUTH_HEADERS)
    try:
        with urllib.request.urlopen(req_s, timeout=20) as resp:
            data = json.loads(resp.read().decode())
            for item in data:
                if filename in item.get("source_url", ""):
                    print(f"  Found existing media for {filename}: ID {item['id']}")
                    return item
    except Exception as e:
        print(f"  Search error: {e}")

    headers = dict(AUTH_HEADERS)
    headers["Content-Disposition"] = f'attachment; filename="{filename}"'
    headers["Content-Type"] = "image/webp"

    req = urllib.request.Request(f"{WP_API}/media", data=path.read_bytes(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=120) as resp:
        media = json.loads(resp.read().decode())
    mid = media["id"]

    update_headers = dict(AUTH_HEADERS)
    update_headers["Content-Type"] = "application/json"
    update_data = json.dumps({"alt_text": alt, "title": title}).encode()
    req_u = urllib.request.Request(f"{WP_API}/media/{mid}", data=update_data, headers=update_headers, method="POST")
    with urllib.request.urlopen(req_u, timeout=120) as resp_u:
        media_u = json.loads(resp_u.read().decode())
    s_url = media_u.get("source_url")
    print(f"Uploaded {path.name} -> ID {mid} ({s_url})")
    return media_u


def patch_post():
    manifest_path = ROOT / "output/Week8_Rank178_FingerRingsForGirls_type3_prompts.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    slots = manifest["slots"]
    outputs = manifest["output"]

    hero_path = ROOT / outputs["hero"]
    flatlay_path = ROOT / outputs["flatlay"]
    lifestyle_path = ROOT / outputs["lifestyle"]

    assert hero_path.exists(), f"Hero image missing at {hero_path}"
    assert flatlay_path.exists(), f"Flatlay image missing at {flatlay_path}"
    assert lifestyle_path.exists(), f"Lifestyle image missing at {lifestyle_path}"

    print("Uploading Type 3 images to WordPress...")
    hero_media = upload_media(hero_path, slots["hero"]["alt"], "Finger Rings for Girls Buying Guide 2026 Hero with The Anya Ring")
    flatlay_media = upload_media(flatlay_path, slots["flatlay"]["alt"], "Finger Rings for Girls Buying Guide 2026 Flatlay with The Quinn Ring")
    lifestyle_media = upload_media(lifestyle_path, slots["lifestyle"]["alt"], "Finger Rings for Girls Buying Guide 2026 Lifestyle with The Rafia Ring")

    hero_id = hero_media["id"]
    hero_url = hero_media["source_url"]
    flatlay_id = flatlay_media["id"]
    flatlay_url = flatlay_media["source_url"]
    lifestyle_id = lifestyle_media["id"]
    lifestyle_url = lifestyle_media["source_url"]

    type3_media_info = {
        "hero": {"id": hero_id, "url": hero_url, "alt": slots["hero"]["alt"], "title": "Finger Rings for Girls Buying Guide 2026 Hero with The Anya Ring"},
        "flatlay": {"id": flatlay_id, "url": flatlay_url, "alt": slots["flatlay"]["alt"], "title": "Finger Rings for Girls Buying Guide 2026 Flatlay with The Quinn Ring"},
        "lifestyle": {"id": lifestyle_id, "url": lifestyle_url, "alt": slots["lifestyle"]["alt"], "title": "Finger Rings for Girls Buying Guide 2026 Lifestyle with The Rafia Ring"}
    }
    with open(ROOT / "output/Week8_Rank178_FingerRingsForGirls_type3_media.json", "w", encoding="utf-8") as f:
        json.dump(type3_media_info, f, indent=2)
    print("Saved Type 3 media info to output/Week8_Rank178_FingerRingsForGirls_type3_media.json")

    # Fetch current post content
    req = urllib.request.Request(
        f"{WP_API}/posts/{POST_ID}?context=edit",
        headers=AUTH_HEADERS
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        post_data = json.loads(resp.read().decode())

    raw_content = post_data["content"]["raw"]

    # PDP URLs
    quinn_pdp = "https://www.bluestone.com/rings/the-quinn-ring~57845.html"
    rafia_pdp = "https://www.bluestone.com/rings/the-rafia-ring~53638.html"

    # Prepare Gutenberg image blocks with product links and clean captions
    flatlay_block = f"""<!-- wp:image {{"id":{flatlay_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{quinn_pdp}"><img src="{flatlay_url}" alt="{slots['flatlay']['alt']}" class="wp-image-{flatlay_id}"/></a><figcaption><a href="{quinn_pdp}">The Quinn Ring</a> styled on an Italian marble vanity alongside fine jewellery keepsakes</figcaption></figure>
<!-- /wp:image -->"""

    lifestyle_block = f"""<!-- wp:image {{"id":{lifestyle_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{rafia_pdp}"><img src="{lifestyle_url}" alt="{slots['lifestyle']['alt']}" class="wp-image-{lifestyle_id}"/></a><figcaption><a href="{rafia_pdp}">The Rafia Ring</a> highlighting graceful floral openwork and ergonomic comfort fit</figcaption></figure>
<!-- /wp:image -->"""

    assert "<!-- TYPE3_FLATLAY_IMAGE_PLACEHOLDER -->" in raw_content, "Flatlay placeholder missing"
    assert "<!-- TYPE3_LIFESTYLE_IMAGE_PLACEHOLDER -->" in raw_content, "Lifestyle placeholder missing"

    updated_content = raw_content.replace("<!-- TYPE3_FLATLAY_IMAGE_PLACEHOLDER -->", flatlay_block, 1)
    updated_content = updated_content.replace("<!-- TYPE3_LIFESTYLE_IMAGE_PLACEHOLDER -->", lifestyle_block, 1)

    # Add images array to schema
    schema_image_insert = f""""image": [
                  "{hero_url}",
                  "{flatlay_url}",
                  "{lifestyle_url}"
                ],"""
    updated_content = updated_content.replace('"articleSection": "Jewellery Education",', f'{schema_image_insert}\n                "articleSection": "Jewellery Education",', 1)

    # Verify no unclosed comments or malformed tags
    assert "<!-- /wp:paragraph>" not in updated_content
    assert "<!-- /wp:heading>" not in updated_content
    assert "—" not in updated_content
    assert "–" not in updated_content

    # Save final patched article
    with open(ROOT / "output/week8_rank178_article_content_final.html", "w", encoding="utf-8") as f:
        f.write(updated_content)
    print("Saved final patched article to output/week8_rank178_article_content_final.html")

    # Update WordPress Post
    patch_payload = {
        "content": updated_content,
        "featured_media": hero_id,
        "meta": {
            "_yoast_wpseo_opengraph-image": hero_url,
            "_yoast_wpseo_opengraph-image-id": str(hero_id),
            "_yoast_wpseo_twitter-image": hero_url,
            "_yoast_wpseo_twitter-image-id": str(hero_id)
        }
    }
    update_headers = dict(AUTH_HEADERS)
    update_headers["Content-Type"] = "application/json"
    req_update = urllib.request.Request(
        f"{WP_API}/posts/{POST_ID}",
        data=json.dumps(patch_payload).encode("utf-8"),
        headers=update_headers,
        method="POST"
    )
    with urllib.request.urlopen(req_update, timeout=120) as resp_up:
        res_post = json.loads(resp_up.read().decode())
    print(f"Successfully patched Post {POST_ID}! Status: {res_post['status']}, Featured Media: {res_post['featured_media']}")


if __name__ == "__main__":
    patch_post()
