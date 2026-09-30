#!/usr/bin/env python3
"""Upload Type 3 images and patch WordPress Post 37205."""
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
POST_ID = 37205

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
    manifest_path = ROOT / "output/Week8_Rank19_EngagementRingsCouples_type3_prompts.json"
    with open(manifest_path) as f:
        manifest = json.load(f)
        
    slots = manifest["slots"]
    hero_path = ROOT / manifest["output"]["hero"]
    flatlay_path = ROOT / manifest["output"]["flatlay"]
    lifestyle_path = ROOT / manifest["output"]["lifestyle"]
    
    for p in [hero_path, flatlay_path, lifestyle_path]:
        if not p.exists():
            raise FileNotFoundError(f"Missing required Type 3 image: {p}")
            
    print("Uploading Type 3 media to WordPress...")
    hero_media = upload_media(hero_path, slots["hero"]["alt"], "Engagement Rings for Couples 2026 Hero with The Liza Ring")
    flatlay_media = upload_media(flatlay_path, slots["flatlay"]["alt"], "Couple Engagement Gold Rings Design 2026 Flatlay with The Interlink Band Ring")
    lifestyle_media = upload_media(lifestyle_path, slots["lifestyle"]["alt"], "Engagement Rings Gold for Couple 2026 Lifestyle with The Jasper Band For Him")
    
    hero_id = hero_media["id"]
    hero_url = hero_media["source_url"]
    flatlay_id = flatlay_media["id"]
    flatlay_url = flatlay_media["source_url"]
    lifestyle_id = lifestyle_media["id"]
    lifestyle_url = lifestyle_media["source_url"]
    
    type3_media_info = {
        "hero": {"id": hero_id, "url": hero_url, "alt": slots["hero"]["alt"], "title": "Engagement Rings for Couples 2026 Hero with The Liza Ring"},
        "flatlay": {"id": flatlay_id, "url": flatlay_url, "alt": slots["flatlay"]["alt"], "title": "Couple Engagement Gold Rings Design 2026 Flatlay with The Interlink Band Ring"},
        "lifestyle": {"id": lifestyle_id, "url": lifestyle_url, "alt": slots["lifestyle"]["alt"], "title": "Engagement Rings Gold for Couple 2026 Lifestyle with The Jasper Band For Him"}
    }
    with open(ROOT / "output/Week8_Rank19_EngagementRingsCouples_type3_media.json", "w") as f:
        json.dump(type3_media_info, f, indent=2)
    
    # Fetch current post content
    req = urllib.request.Request(
        f"{WP_API}/posts/{POST_ID}?context=edit",
        headers=AUTH_HEADERS
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        post_data = json.loads(resp.read().decode())
        
    raw_content = post_data["content"]["raw"]
    
    # PDP URLs
    interlink_pdp = "https://www.bluestone.com/rings/the-interlink-band-ring~108785.html"
    jasper_pdp = "https://www.bluestone.com/rings/the-jasper-band-for-him~93964.html"
    
    # Prepare Gutenberg image blocks
    flatlay_block = f"""<!-- wp:image {{"id":{flatlay_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{interlink_pdp}"><img src="{flatlay_url}" alt="{slots['flatlay']['alt']}" class="wp-image-{flatlay_id}"/></a><figcaption><a href="{interlink_pdp}">The Interlink Band Ring</a> styled on a marble vanity as a modern gold couple engagement ring design</figcaption></figure>
<!-- /wp:image -->"""

    lifestyle_block = f"""<!-- wp:image {{"id":{lifestyle_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{jasper_pdp}"><img src="{lifestyle_url}" alt="{slots['lifestyle']['alt']}" class="wp-image-{lifestyle_id}"/></a><figcaption><a href="{jasper_pdp}">The Jasper Band For Him</a> worn as a refined 18K gold couple engagement band</figcaption></figure>
<!-- /wp:image -->"""

    assert "<!-- TYPE3_FLATLAY_PLACEHOLDER -->" in raw_content, "Flatlay placeholder missing"
    assert "<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->" in raw_content, "Lifestyle placeholder missing"
    
    updated_content = raw_content.replace("<!-- TYPE3_FLATLAY_PLACEHOLDER -->", flatlay_block)
    updated_content = updated_content.replace("<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->", lifestyle_block)
    
    # Ensure BlogPosting schema has updated image array
    image_array = [hero_url, flatlay_url, lifestyle_url]
    
    patch_payload = {
        "featured_media": hero_id,
        "content": updated_content,
        "meta": {
            "_yoast_wpseo_opengraph-image": hero_url,
            "_yoast_wpseo_opengraph-image-id": hero_id,
            "_yoast_wpseo_twitter-image": hero_url,
            "_yoast_wpseo_twitter-image-id": hero_id
        }
    }
    
    req_patch = urllib.request.Request(
        f"{WP_API}/posts/{POST_ID}",
        data=json.dumps(patch_payload).encode(),
        headers={**AUTH_HEADERS, "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req_patch, timeout=120) as resp:
        patched = json.loads(resp.read().decode())
        
    print(f"SUCCESS: Patched Post {POST_ID} with featured media {hero_id} and in-body images {flatlay_id}, {lifestyle_id}")
    return {
        "hero_media_id": hero_id,
        "flatlay_media_id": flatlay_id,
        "lifestyle_media_id": lifestyle_id,
        "hero_url": hero_url,
        "flatlay_url": flatlay_url,
        "lifestyle_url": lifestyle_url
    }

if __name__ == "__main__":
    patch_post()
