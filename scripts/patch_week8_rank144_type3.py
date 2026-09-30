#!/usr/bin/env python3
"""Upload Type 3 images and patch WordPress Post 38716 for Week 8 Rank 144."""
import os
import re
import sys
import json
import base64
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

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
POST_ID = 38716

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
    manifest_path = ROOT / "output/Week8_Rank144_PurpleEarrings_type3_prompts.json"
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
    hero_media = upload_media(hero_path, slots["hero"]["alt"], "Purple Earrings Buying Guide 2026 Hero with The Aleena Huggie Earrings")
    flatlay_media = upload_media(flatlay_path, slots["flatlay"]["alt"], "Purple Earrings Buying Guide 2026 Flatlay with The Nettile Huggie Earrings")
    lifestyle_media = upload_media(lifestyle_path, slots["lifestyle"]["alt"], "Purple Earrings Buying Guide 2026 Lifestyle with The Vicky Hoop Earrings")
    
    hero_id = hero_media["id"]
    hero_url = hero_media["source_url"]
    flatlay_id = flatlay_media["id"]
    flatlay_url = flatlay_media["source_url"]
    lifestyle_id = lifestyle_media["id"]
    lifestyle_url = lifestyle_media["source_url"]
    
    type3_media_info = {
        "hero": {"id": hero_id, "url": hero_url, "alt": slots["hero"]["alt"], "title": "Purple Earrings Buying Guide 2026 Hero with The Aleena Huggie Earrings"},
        "flatlay": {"id": flatlay_id, "url": flatlay_url, "alt": slots["flatlay"]["alt"], "title": "Purple Earrings Buying Guide 2026 Flatlay with The Nettile Huggie Earrings"},
        "lifestyle": {"id": lifestyle_id, "url": lifestyle_url, "alt": slots["lifestyle"]["alt"], "title": "Purple Earrings Buying Guide 2026 Lifestyle with The Vicky Hoop Earrings"}
    }
    with open(ROOT / "output/Week8_Rank144_PurpleEarrings_type3_media.json", "w", encoding="utf-8") as f:
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
    nettile_pdp = "https://www.bluestone.com/earrings/the-nettile-huggie-earrings~108215.html"
    vicky_pdp = "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html"
    
    # Prepare Gutenberg image blocks with product links and clean captions
    flatlay_block = f"""<!-- wp:image {{"id":{flatlay_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{nettile_pdp}"><img src="{flatlay_url}" alt="{slots['flatlay']['alt']}" class="wp-image-{flatlay_id}"/></a><figcaption><a href="{nettile_pdp}">The Nettile Huggie Earrings</a> styled on a sunlit windowsill highlighting pavé diamond settings</figcaption></figure>
<!-- /wp:image -->"""

    lifestyle_block = f"""<!-- wp:image {{"id":{lifestyle_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{vicky_pdp}"><img src="{lifestyle_url}" alt="{slots['lifestyle']['alt']}" class="wp-image-{lifestyle_id}"/></a><figcaption><a href="{vicky_pdp}">The Vicky Hoop Earrings</a> worn for sophisticated everyday styling in 18Kt gold</figcaption></figure>
<!-- /wp:image -->"""

    assert "<!-- TYPE3_FLATLAY_PLACEHOLDER -->" in raw_content, "Flatlay placeholder missing"
    assert "<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->" in raw_content, "Lifestyle placeholder missing"
    
    updated_content = raw_content.replace("<!-- TYPE3_FLATLAY_PLACEHOLDER -->", flatlay_block, 1)
    updated_content = updated_content.replace("<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->", lifestyle_block, 1)
    
    # Update BlogPosting schema images cleanly
    kw_target = '"keywords": "purple earrings, purple and gold earrings, purple earrings india, purple gold earrings, amethyst earrings, tanzanite earrings 2026"'
    images_json = json.dumps([hero_url, flatlay_url, lifestyle_url])
    kw_replacement = f'{kw_target},\n      "image": {images_json}'
    assert kw_target in updated_content, "Keywords line missing in schema"
    updated_content = updated_content.replace(kw_target, kw_replacement, 1)
    
    # Verify no duplicate sections
    h2_titles = re.findall(r"<h2[^>]*>(.*?)</h2>", updated_content)
    assert len(h2_titles) == len(set(h2_titles)), f"Duplicate H2 detected: {h2_titles}"
    
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
