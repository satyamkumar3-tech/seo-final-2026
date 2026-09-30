#!/usr/bin/env python3
"""Patch Type 3 images and metadata for Rank 156."""
import os
import json
import base64
import re
import urllib.request
from html import escape
from pathlib import Path

ROOT = Path(".")

# Load environment
env = {}
with open(ROOT / ".env") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip("\"'")

USER = env.get("WP_USER", "")
PWD = env.get("WP_APP_PASSWORD", "")
AUTH = base64.b64encode(f"{USER}:{PWD}".encode()).decode()
HEADERS = {"Authorization": f"Basic {AUTH}", "User-Agent": "BluestoneSEO/1.0"}
API = "https://blog.bluestone.com/wp-json/wp/v2"

POST_ID = 36380
MANIFEST_PATH = ROOT / "output/Week7_Rank156_platinum_necklace_type3_prompts.json"
manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

def upload_image(local_path: Path, alt: str, title: str):
    headers = dict(HEADERS)
    headers["Content-Disposition"] = f'attachment; filename="{local_path.name}"'
    headers["Content-Type"] = "image/webp"

    req = urllib.request.Request(f"{API}/media", data=local_path.read_bytes(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=60) as resp:
        media = json.loads(resp.read().decode("utf-8"))

    mid = media["id"]
    source_url = media.get("source_url") or media.get("guid", {}).get("rendered")

    # Update metadata
    req_meta = urllib.request.Request(
        f"{API}/media/{mid}",
        data=json.dumps({"alt_text": alt, "title": title}).encode("utf-8"),
        headers={**HEADERS, "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req_meta, timeout=60) as resp_meta:
        json.loads(resp_meta.read().decode("utf-8"))

    print(f"Uploaded Type 3 {local_path.name} -> ID: {mid} | URL: {source_url}")
    return mid, source_url

def main():
    hero_path = ROOT / manifest["output"]["hero"]
    flatlay_path = ROOT / manifest["output"]["flatlay"]
    lifestyle_path = ROOT / manifest["output"]["lifestyle"]

    hero_mid, hero_url = upload_image(
        hero_path,
        manifest["slots"]["hero"]["alt"],
        "Platinum Necklace 2026 - The Thaloria Pendant Hero"
    )
    flatlay_mid, flatlay_url = upload_image(
        flatlay_path,
        manifest["slots"]["flatlay"]["alt"],
        "Platinum Necklace 2026 - The Sarvanya Pendant Flatlay"
    )
    lifestyle_mid, lifestyle_url = upload_image(
        lifestyle_path,
        manifest["slots"]["lifestyle"]["alt"],
        "Platinum Necklace 2026 - The Thyvarne Pendant Lifestyle"
    )

    manifest["uploaded_media"] = {
        "hero": {"id": hero_mid, "url": hero_url},
        "flatlay": {"id": flatlay_mid, "url": flatlay_url},
        "lifestyle": {"id": lifestyle_mid, "url": lifestyle_url},
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Fetch current post content
    req = urllib.request.Request(f"{API}/posts/{POST_ID}?context=edit", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        post = json.loads(resp.read().decode("utf-8"))

    content = post["content"]["raw"]

    # 1. Remove in-body hero placeholder (Featured hero must not also appear in body)
    content = re.sub(
        r'<!-- wp:image \{.*?\} -->\s*<figure class="wp-block-image size-full"><img src="[^"]*platinum-necklace-hero-2026\.webp"[^>]*>.*?</figure>\s*<!-- /wp:image -->\n\n?',
        '',
        content
    )

    # 2. Replace flatlay placeholder with authentic Gutenberg block
    flatlay_block = (
        f'<!-- wp:image {{"id":{flatlay_mid},"sizeSlug":"full","linkDestination":"none"}} -->\n'
        f'<figure class="wp-block-image size-full"><img src="{flatlay_url}" alt="{manifest["slots"]["flatlay"]["alt"]}" class="wp-image-{flatlay_mid}"/>'
        f'<figcaption>{manifest["slots"]["flatlay"]["caption"]}</figcaption></figure>\n'
        f'<!-- /wp:image -->'
    )
    content = re.sub(
        r'<!-- wp:image \{.*?\} -->\s*<figure class="wp-block-image size-full"><img src="[^"]*platinum-necklace-flatlay-2026\.webp"[^>]*>.*?</figure>\s*<!-- /wp:image -->',
        flatlay_block,
        content
    )

    # 3. Replace lifestyle placeholder with authentic Gutenberg block
    lifestyle_block = (
        f'<!-- wp:image {{"id":{lifestyle_mid},"sizeSlug":"full","linkDestination":"none"}} -->\n'
        f'<figure class="wp-block-image size-full"><img src="{lifestyle_url}" alt="{manifest["slots"]["lifestyle"]["alt"]}" class="wp-image-{lifestyle_mid}"/>'
        f'<figcaption>{manifest["slots"]["lifestyle"]["caption"]}</figcaption></figure>\n'
        f'<!-- /wp:image -->'
    )
    content = re.sub(
        r'<!-- wp:image \{.*?\} -->\s*<figure class="wp-block-image size-full"><img src="[^"]*platinum-necklace-lifestyle-2026\.webp"[^>]*>.*?</figure>\s*<!-- /wp:image -->',
        lifestyle_block,
        content
    )

    # 4. Update Schema image URLs
    content = re.sub(
        r'"https://blog\.bluestone\.com/wp-content/uploads/2026/08/platinum-necklace-hero-2026\.webp"',
        f'"{hero_url}"',
        content
    )
    content = re.sub(
        r'"https://blog\.bluestone\.com/wp-content/uploads/2026/08/platinum-necklace-flatlay-2026\.webp"',
        f'"{flatlay_url}"',
        content
    )
    content = re.sub(
        r'"https://blog\.bluestone\.com/wp-content/uploads/2026/08/platinum-necklace-lifestyle-2026\.webp"',
        f'"{lifestyle_url}"',
        content
    )

    # Patch post
    patch_payload = {
        "featured_media": hero_mid,
        "content": content,
        "meta": {
            "_yoast_wpseo_opengraph-image": hero_url,
            "_yoast_wpseo_twitter-image": hero_url,
            "_yoast_wpseo_opengraph-image-id": hero_mid,
        }
    }

    req_patch = urllib.request.Request(
        f"{API}/posts/{POST_ID}",
        data=json.dumps(patch_payload).encode("utf-8"),
        headers={**HEADERS, "Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(req_patch, timeout=60) as resp_patch:
        patched_post = json.loads(resp_patch.read().decode("utf-8"))

    print(f"Successfully patched post {POST_ID}! Featured media set to {hero_mid}")

if __name__ == "__main__":
    main()
