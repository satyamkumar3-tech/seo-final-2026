#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload Type 3 images and patch WordPress Post 40162 for Week 9 Rank 63."""
import os, sys, json, base64, urllib.request, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POST_ID = 40162
SLUG = "mens-gold-band-rings-2026"

# Load environment
env_paths = [ROOT / '.env', Path('/Users/satyamkumar/Downloads/seo final 2026/.env')]
for ep in env_paths:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

WP_USER = os.environ.get('WP_USER', 'blogbluestone')
WP_PASS = os.environ.get('WP_APP_PASSWORD') or os.environ.get('WP_APP_PASS') or os.environ.get('WP_PASSWORD', '')
WP_URL = os.environ.get('WP_URL', 'https://blog.bluestone.com')
TOKEN = base64.b64encode(f"{WP_USER}:{WP_PASS}".encode()).decode()
AUTH_HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0"
}

def upload_media(path: Path, alt: str, title: str):
    filename = path.name
    # Search existing media
    search_url = f"{WP_URL}/wp-json/wp/v2/media?search={filename}&per_page=10"
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

    req = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/media", data=path.read_bytes(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=120) as resp:
        media = json.loads(resp.read().decode())
    mid = media["id"]

    update_headers = dict(AUTH_HEADERS)
    update_headers["Content-Type"] = "application/json"
    update_data = json.dumps({"alt_text": alt, "title": title}).encode()
    req_u = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/media/{mid}", data=update_data, headers=update_headers, method="POST")
    with urllib.request.urlopen(req_u, timeout=60) as resp_u:
        media_u = json.loads(resp_u.read().decode())
    s_url = media_u.get("source_url")
    print(f"Uploaded {path.name} -> ID {mid} ({s_url})")
    return media_u

def patch_post():
    manifest_path = ROOT / "output" / "Week9_Rank63_MensGoldBands_type3_prompts.json"
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))

    slots = manifest["slots"]
    outputs = manifest["output"]

    hero_path = ROOT / outputs["hero"]
    flatlay_path = ROOT / outputs["flatlay"]
    lifestyle_path = ROOT / outputs["lifestyle"]

    assert hero_path.exists(), f"Hero image missing at {hero_path}"
    assert flatlay_path.exists(), f"Flatlay image missing at {flatlay_path}"
    assert lifestyle_path.exists(), f"Lifestyle image missing at {lifestyle_path}"

    print("Uploading Type 3 images to WordPress...")
    hero_media = upload_media(hero_path, slots["hero"]["alt"], "Men's Gold Band Rings 2026 Hero featuring The Jasper Band For Him")
    flatlay_media = upload_media(flatlay_path, slots["flatlay"]["alt"], "Men's Gold Band Rings 2026 Study Desk Flatlay with The Le Sommet Ring")
    lifestyle_media = upload_media(lifestyle_path, slots["lifestyle"]["alt"], "Men's Gold Band Rings 2026 Lifestyle Action with The Interlink Band Ring")

    hero_id = hero_media["id"]
    hero_url = hero_media["source_url"]
    flatlay_id = flatlay_media["id"]
    flatlay_url = flatlay_media["source_url"]
    lifestyle_id = lifestyle_media["id"]
    lifestyle_url = lifestyle_media["source_url"]

    # Save media manifest
    media_manifest = {
        "post_id": POST_ID,
        "slug": SLUG,
        "hero": {
            "id": hero_id,
            "url": hero_url,
            "product": slots["hero"]["product_name"],
            "sku": slots["hero"]["code"],
            "alt": slots["hero"]["alt"]
        },
        "flatlay": {
            "id": flatlay_id,
            "url": flatlay_url,
            "product": slots["flatlay"]["product_name"],
            "sku": slots["flatlay"]["code"],
            "alt": slots["flatlay"]["alt"]
        },
        "lifestyle": {
            "id": lifestyle_id,
            "url": lifestyle_url,
            "product": slots["lifestyle"]["product_name"],
            "sku": slots["lifestyle"]["code"],
            "alt": slots["lifestyle"]["alt"]
        }
    }
    manifest_out = ROOT / "output" / "week9_rank63_media_manifest.json"
    manifest_out.write_text(json.dumps(media_manifest, indent=2), encoding='utf-8')
    print(f"Saved media manifest to: {manifest_out}")

    # Fetch current post
    print(f"Fetching current post {POST_ID}...")
    req = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/posts/{POST_ID}?context=edit", headers=AUTH_HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        post_data = json.loads(resp.read().decode())

    content = post_data["content"]["raw"]

    # Build image blocks with custom links to PDPs
    flatlay_pdp = slots["flatlay"]["pdp"]
    flatlay_caption = slots["flatlay"]["caption"]
    flatlay_block = f"""<!-- wp:image {{"id":{flatlay_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{flatlay_pdp}"><img src="{flatlay_url}" alt="{slots['flatlay']['alt']}" class="wp-image-{flatlay_id}"/></a><figcaption><a href="{flatlay_pdp}">{flatlay_caption}</a></figcaption></figure>
<!-- /wp:image -->"""

    lifestyle_pdp = slots["lifestyle"]["pdp"]
    lifestyle_caption = slots["lifestyle"]["caption"]
    lifestyle_block = f"""<!-- wp:image {{"id":{lifestyle_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{lifestyle_pdp}"><img src="{lifestyle_url}" alt="{slots['lifestyle']['alt']}" class="wp-image-{lifestyle_id}"/></a><figcaption><a href="{lifestyle_pdp}">{lifestyle_caption}</a></figcaption></figure>
<!-- /wp:image -->"""

    # Replace placeholders
    if "<!-- TYPE3_FLATLAY_PLACEHOLDER -->" in content:
        content = content.replace("<!-- TYPE3_FLATLAY_PLACEHOLDER -->", flatlay_block)
        print("Replaced flatlay placeholder successfully.")
    else:
        print("Warning: TYPE3_FLATLAY_PLACEHOLDER not found in content!")

    if "<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->" in content:
        content = content.replace("<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->", lifestyle_block)
        print("Replaced lifestyle placeholder successfully.")
    else:
        print("Warning: TYPE3_LIFESTYLE_PLACEHOLDER not found in content!")

    # Update trailing schema images
    schema_pattern = r'("headline":\s*"[^"]+",)'
    if re.search(schema_pattern, content):
        img_schema = f'\\1\n      "image": [\n        "{hero_url}",\n        "{flatlay_url}",\n        "{lifestyle_url}"\n      ],'
        content = re.sub(schema_pattern, img_schema, content, count=1)
        print("Added images to BlogPosting schema.")

    # Patch post via API
    patch_payload = {
        "featured_media": hero_id,
        "content": content,
        "meta": {
            "_yoast_wpseo_opengraph-image": hero_url,
            "_yoast_wpseo_twitter-image": hero_url
        }
    }

    req_patch = urllib.request.Request(
        f"{WP_URL}/wp-json/wp/v2/posts/{POST_ID}",
        data=json.dumps(patch_payload).encode('utf-8'),
        headers={**AUTH_HEADERS, "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req_patch, timeout=60) as resp:
        updated_post = json.loads(resp.read().decode())
        print(f"Patched post {POST_ID} successfully!")
        print(f"Featured media: {updated_post.get('featured_media')}")

if __name__ == "__main__":
    patch_post()
