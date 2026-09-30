#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload Type 3 images and patch WordPress post 40437 for Week 9 Rank 86 (modern vanki ring designs)."""
import os
import sys
import json
import base64
import urllib.request
import time
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Load environment
for ep in [ROOT / ".env", Path("/Users/satyamkumar/Downloads/seo final 2026/.env")]:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip("'\""))

user = os.environ.get("WP_USER", "blogbluestone")
pwd = os.environ.get("WP_APP_PASSWORD") or os.environ.get("WP_APP_PASS") or os.environ.get("WP_PASSWORD", "")
token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
AUTH_HEADERS = {
    "Authorization": f"Basic {token}",
    "User-Agent": "BluestoneSEO/1.0"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"
POST_ID = 40437

def verify_http_200(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "BluestoneSEO/1.0"}, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"Verification failed for {url}: {e}")
        return False

def upload_image(path: Path, alt: str, title: str):
    headers = dict(AUTH_HEADERS)
    headers["Content-Disposition"] = f'attachment; filename="{path.name}"'
    headers["Content-Type"] = "image/webp"

    req = urllib.request.Request(f"{WP_API}/media", data=path.read_bytes(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=120) as resp:
        media = json.loads(resp.read().decode())
    mid = media["id"]
    src_url = media["source_url"]
    print(f"Uploaded {path.name} -> ID: {mid}, URL: {src_url}")

    # Update metadata
    time.sleep(0.5)
    update_data = json.dumps({"alt_text": alt, "title": title}).encode()
    u_headers = dict(AUTH_HEADERS)
    u_headers["Content-Type"] = "application/json"
    u_req = urllib.request.Request(f"{WP_API}/media/{mid}", data=update_data, headers=u_headers, method="POST")
    with urllib.request.urlopen(u_req, timeout=120) as resp:
        pass
    print(f"Updated metadata for media ID {mid}")

    # Pre-flight check
    time.sleep(0.5)
    if not verify_http_200(src_url):
        raise RuntimeError(f"HTTP 200 verification failed for {src_url}")
    print(f"Verified {src_url} -> HTTP 200 OK")
    return mid, src_url

def main():
    manifest_path = ROOT / "output/Week9_Rank86_ModernVankiRingDesigns_type3_prompts.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    hero_info = manifest["slots"]["hero"]
    flatlay_info = manifest["slots"]["flatlay"]
    lifestyle_info = manifest["slots"]["lifestyle"]

    hero_webp = ROOT / manifest["output"]["hero"]
    flatlay_webp = ROOT / manifest["output"]["flatlay"]
    lifestyle_webp = ROOT / manifest["output"]["lifestyle"]

    print("Uploading Type 3 images to WordPress media library...")
    h_id, h_src = upload_image(hero_webp, hero_info["alt"], f"{hero_info['product_name']} hero: Modern Vanki Ring Designs Guide 2026")
    f_id, f_src = upload_image(flatlay_webp, flatlay_info["alt"], f"{flatlay_info['product_name']} flatlay: Modern Vanki Ring Designs Guide 2026")
    l_id, l_src = upload_image(lifestyle_webp, lifestyle_info["alt"], f"{lifestyle_info['product_name']} lifestyle: Modern Vanki Ring Designs Guide 2026")

    type3_uploaded = {
        "hero": {"media_id": h_id, "src": h_src, "alt": hero_info["alt"], "pdp": hero_info["pdp"], "name": hero_info["product_name"]},
        "flatlay": {"media_id": f_id, "src": f_src, "alt": flatlay_info["alt"], "pdp": flatlay_info["pdp"], "name": flatlay_info["product_name"]},
        "lifestyle": {"media_id": l_id, "src": l_src, "alt": lifestyle_info["alt"], "pdp": lifestyle_info["pdp"], "name": lifestyle_info["product_name"]}
    }

    uploaded_record_path = ROOT / "output/Week9_Rank86_type3_uploaded_media.json"
    uploaded_record_path.write_text(json.dumps(type3_uploaded, indent=2), encoding="utf-8")

    # Fetch post content
    req = urllib.request.Request(f"{WP_API}/posts/{POST_ID}?context=edit", headers=AUTH_HEADERS)
    with urllib.request.urlopen(req, timeout=120) as resp:
        post_data = json.loads(resp.read().decode())

    content = post_data["content"]["raw"]

    # 1. Replace flatlay placeholder
    old_flatlay_target = 'PLACEHOLDER_TYPE3_FLATLAY"'
    new_flatlay_replacement = f'{f_src}" class="wp-image-{f_id}"'
    if old_flatlay_target in content:
        content = content.replace(old_flatlay_target, new_flatlay_replacement)
        content = content.replace('<!-- wp:image {"sizeSlug":"full","linkDestination":"custom"} -->', f'<!-- wp:image {{"id":{f_id},"sizeSlug":"full","linkDestination":"custom"}} -->', 1)
        print("Flatlay placeholder replaced successfully!")
    else:
        print("WARNING: Flatlay placeholder not found in content!")

    # 2. Replace lifestyle placeholder
    old_lifestyle_target = 'PLACEHOLDER_TYPE3_LIFESTYLE"'
    new_lifestyle_replacement = f'{l_src}" class="wp-image-{l_id}"'
    if old_lifestyle_target in content:
        content = content.replace(old_lifestyle_target, new_lifestyle_replacement)
        # Replace the next image block comment
        content = content.replace('<!-- wp:image {"sizeSlug":"full","linkDestination":"custom"} -->', f'<!-- wp:image {{"id":{l_id},"sizeSlug":"full","linkDestination":"custom"}} -->', 1)
        print("Lifestyle placeholder replaced successfully!")
    else:
        print("WARNING: Lifestyle placeholder not found in content!")

    # 3. Add images into BlogPosting schema
    img_json_str = f'"image": [\n        "{h_src}",\n        "{f_src}",\n        "{l_src}"\n      ],\n      "headline"'
    content = content.replace('"headline"', img_json_str, 1)
    print("Injected image array into BlogPosting schema!")

    # Verify no unclosed comments
    if "<!--" in content and "-->" in content:
        open_count = content.count("<!--")
        close_count = content.count("-->")
        print(f"Comment audit: open <!-- = {open_count}, close --> = {close_count}")
        if open_count != close_count:
            raise ValueError(f"Mismatched HTML comments: {open_count} open vs {close_count} close!")

    update_payload = {
        "featured_media": h_id,
        "content": content,
        "meta": {
            "_yoast_wpseo_focuskw": "modern vanki ring designs",
            "_yoast_wpseo_title": "Modern Vanki Ring Designs: 2026 Buying & Styling Guide | BlueStone",
            "_yoast_wpseo_metadesc": "Discover modern vanki ring designs in 2026. Explore traditional symbolism, lightweight daily gold engineering, 18K vs 14K gold, styling tips, and sizing advice.",
            "_yoast_wpseo_opengraph-image": h_src,
            "_yoast_wpseo_opengraph-image-id": h_id,
            "_yoast_wpseo_twitter-image": h_src,
            "_yoast_wpseo_twitter-image-id": h_id
        }
    }

    update_req = urllib.request.Request(
        f"{WP_API}/posts/{POST_ID}",
        data=json.dumps(update_payload).encode(),
        headers={**AUTH_HEADERS, "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(update_req, timeout=120) as resp:
        updated_post = json.loads(resp.read().decode())
    print(f"Successfully patched post {POST_ID}!")
    print(f"Featured media: {updated_post['featured_media']}")

if __name__ == "__main__":
    main()
