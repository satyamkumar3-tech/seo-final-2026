#!/usr/bin/env python3
"""Upload Type 3 images and patch WordPress Post 36882."""
import os
import re
import sys
import json
import base64
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Load local environment
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
    "User-Agent": "BluestoneSEO/1.0"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"
POST_ID = 36882

def upload_media(path: Path, alt: str, title: str):
    headers = dict(AUTH_HEADERS)
    headers["Content-Disposition"] = f'attachment; filename="{path.name}"'
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
    manifest_path = ROOT / "output/Week7_Rank196_BigEarrings_type3_prompts.json"
    with open(manifest_path) as f:
        manifest = json.load(f)
        
    slots = manifest["slots"]
    hero_path = ROOT / manifest["output"]["hero"]
    flatlay_path = ROOT / manifest["output"]["flatlay"]
    lifestyle_path = ROOT / manifest["output"]["lifestyle"]
    
    print("Uploading Type 3 media to WordPress...")
    hero_media = upload_media(hero_path, slots["hero"]["alt"], "The Asya Huggie Earrings - Big Statement Earrings in 18K Yellow Gold with Diamonds")
    flatlay_media = upload_media(flatlay_path, slots["flatlay"]["alt"], "The Skein Hoop Earrings - Big Gold Statement Hoops Flatlay on Cafe Tray")
    lifestyle_media = upload_media(lifestyle_path, slots["lifestyle"]["alt"], "The Faliha Purse Hoop Earrings - Statement Fine Gold Earrings Worn for Evening")
    
    hero_id = hero_media["id"]
    hero_url = hero_media["source_url"]
    flatlay_id = flatlay_media["id"]
    flatlay_url = flatlay_media["source_url"]
    lifestyle_id = lifestyle_media["id"]
    lifestyle_url = lifestyle_media["source_url"]
    
    # Fetch current post content
    req = urllib.request.Request(
        f"{WP_API}/posts/{POST_ID}?context=edit",
        headers=AUTH_HEADERS
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        post_data = json.loads(resp.read().decode())
        
    raw_content = post_data["content"]["raw"]
    
    # Prepare Gutenberg image blocks
    flatlay_block = f"""<!-- wp:image {{"id":{flatlay_id},"sizeSlug":"full","linkDestination":"none"}} -->
<figure class="wp-block-image size-full"><img src="{flatlay_url}" alt="{slots['flatlay']['alt']}" class="wp-image-{flatlay_id}"/><figcaption>{slots['flatlay']['caption']}</figcaption></figure>
<!-- /wp:image -->"""

    lifestyle_block = f"""<!-- wp:image {{"id":{lifestyle_id},"sizeSlug":"full","linkDestination":"none"}} -->
<figure class="wp-block-image size-full"><img src="{lifestyle_url}" alt="{slots['lifestyle']['alt']}" class="wp-image-{lifestyle_id}"/><figcaption>{slots['lifestyle']['caption']}</figcaption></figure>
<!-- /wp:image -->"""

    assert "<!-- TYPE3_FLATLAY_PLACEHOLDER -->" in raw_content, "Flatlay placeholder missing"
    assert "<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->" in raw_content, "Lifestyle placeholder missing"
    
    patched_content = raw_content.replace("<!-- TYPE3_FLATLAY_PLACEHOLDER -->", flatlay_block)
    patched_content = patched_content.replace("<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->", lifestyle_block)
    
    # Update BlogPosting schema images
    # Collect all image URLs: hero + carousel + flatlay + lifestyle
    with open(ROOT / "output/carousel_webp/rank196/media_ids.json") as f:
        car_media = json.load(f)
    all_images = [hero_url] + [m["src"] for m in car_media] + [flatlay_url, lifestyle_url]
    
    # Update schema in patched content
    image_json_str = json.dumps(all_images)
    patched_content = re.sub(
        r'("headline": "Trending Big Earrings in 2026: 15 Statement Gold, Diamond & Heritage Styles for Women",\s*"description": ".*?",)',
        r'\1\n        "image": ' + image_json_str + ',',
        patched_content
    )
    
    # Update post
    update_payload = {
        "featured_media": hero_id,
        "content": patched_content,
        "meta": {
            "_yoast_wpseo_opengraph-image": hero_url,
            "_yoast_wpseo_twitter-image": hero_url,
            "_yoast_wpseo_opengraph-image-id": hero_id,
            "_yoast_wpseo_twitter-image-id": hero_id
        }
    }
    
    headers = dict(AUTH_HEADERS)
    headers["Content-Type"] = "application/json"
    req_update = urllib.request.Request(
        f"{WP_API}/posts/{POST_ID}",
        data=json.dumps(update_payload).encode(),
        headers=headers,
        method="POST"
    )
    with urllib.request.urlopen(req_update, timeout=120) as resp:
        updated_post = json.loads(resp.read().decode())
        
    print(f"Successfully patched Post {POST_ID}!")
    print(f"Featured media ID: {updated_post.get('featured_media')}")
    
    patch_info = {
        "post_id": POST_ID,
        "hero_media_id": hero_id,
        "hero_url": hero_url,
        "flatlay_media_id": flatlay_id,
        "flatlay_url": flatlay_url,
        "lifestyle_media_id": lifestyle_id,
        "lifestyle_url": lifestyle_url,
    }
    with open(ROOT / "output/rank196_patch_info.json", "w") as f:
        json.dump(patch_info, f, indent=2)
    return patch_info

if __name__ == "__main__":
    patch_post()
