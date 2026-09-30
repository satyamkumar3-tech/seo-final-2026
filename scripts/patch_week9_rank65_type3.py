#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch Week 9 Rank 65 WordPress post with Type 3 images and social metadata."""
import os
import sys
import time
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

# Load env
env = {}
for ep in [ROOT / ".env", Path("/Users/satyamkumar/Downloads/seo final 2026/.env")]:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                env[k.strip()] = v.strip().strip('\'\"')

user = env.get("WP_USER", "blogbluestone")
pwd = env.get("WP_APP_PASSWORD") or env.get("WP_APP_PASS") or env.get("WP_PASSWORD", "")
token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
AUTH_HEADERS = {
    "Authorization": f"Basic {token}",
    "User-Agent": "BluestoneSEO/1.0"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"

POST_ID = 40188

def req_with_retry(req, max_retries=5, initial_delay=3):
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return resp.status, resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"HTTP 429 received. Waiting {delay}s before retry (attempt {attempt+1}/{max_retries})...")
                time.sleep(delay)
                delay *= 2
            else:
                print(f"HTTP error {e.code}: {e.reason}")
                raise e
    raise Exception("Max retries exceeded for request")

def prepare_webp(raw_path: Path, webp_path: Path, max_width=1400, quality=82):
    webp_path.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(raw_path) as img:
        img = img.convert("RGB")
        if img.width > max_width:
            h = round(img.height * max_width / img.width)
            img = img.resize((max_width, h), Image.Resampling.LANCZOS)
        img.save(webp_path, "WEBP", quality=quality, method=6)
    print(f"Prepared WebP: {raw_path.name} -> {webp_path.name} ({webp_path.stat().st_size} bytes)")

def upload_media(path: Path, alt: str, title: str):
    headers = dict(AUTH_HEADERS)
    headers["Content-Disposition"] = f'attachment; filename="{path.name}"'
    headers["Content-Type"] = "image/webp"
    
    req = urllib.request.Request(f"{WP_API}/media", data=path.read_bytes(), headers=headers, method="POST")
    _, body = req_with_retry(req)
    media = json.loads(body.decode())
    mid = media["id"]
    src_url = media["source_url"]
    print(f"Uploaded {path.name} -> Media ID: {mid}, URL: {src_url}")
    
    time.sleep(1)
    update_data = json.dumps({"alt_text": alt, "title": title}).encode()
    u_headers = dict(AUTH_HEADERS)
    u_headers["Content-Type"] = "application/json"
    u_req = urllib.request.Request(f"{WP_API}/media/{mid}", data=update_data, headers=u_headers, method="POST")
    req_with_retry(u_req)
    print(f"Updated metadata for media ID {mid}")
    return mid, src_url

def build_custom_image_block(mid: int, src: str, alt: str, pdp_url: str, caption_html: str):
    return f"""<!-- wp:image {{"id":{mid},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{pdp_url}"><img src="{src}" alt="{alt}" class="wp-image-{mid}"/></a><figcaption>{caption_html}</figcaption></figure>
<!-- /wp:image -->"""

def main():
    manifest_path = ROOT / "output/Week9_Rank65_BlueStoneRingMen_type3_prompts.json"
    with open(manifest_path) as f:
        manifest = json.load(f)

    slots = manifest["slots"]
    outputs = manifest["output"]

    # Check raw files exist
    uploaded_type3 = {}
    for slot_name, out_path_str in outputs.items():
        webp_path = ROOT / out_path_str
        raw_path = webp_path.with_suffix(".raw.png")
        if not raw_path.exists():
            raise FileNotFoundError(f"Missing raw image for slot {slot_name}: {raw_path}")
        
        prepare_webp(raw_path, webp_path)
        
        cfg = slots[slot_name]
        alt = cfg["alt"]
        title = f"Blue Stone Ring for Men 2026 {slot_name.title()} — {cfg['product_name']}"
        
        time.sleep(1)
        mid, src_url = upload_media(webp_path, alt, title)
        uploaded_type3[slot_name] = {
            "media_id": mid,
            "src": src_url,
            "alt": alt,
            "caption": cfg["caption"],
            "pdp": cfg["pdp"],
            "product_name": cfg["product_name"]
        }

    # Save uploaded Type 3 media info
    media_json_path = ROOT / "output/Week9_Rank65_type3_media.json"
    with open(media_json_path, "w") as f:
        json.dump(uploaded_type3, f, indent=2)
    print(f"Saved Type 3 media info to {media_json_path}")

    # Fetch current post
    get_req = urllib.request.Request(f"{WP_API}/posts/{POST_ID}", headers=AUTH_HEADERS)
    _, body = req_with_retry(get_req)
    post_data = json.loads(body.decode())
    content = post_data["content"]["raw"] if "raw" in post_data["content"] else post_data["content"]["rendered"]

    # Build image blocks
    flatlay_data = uploaded_type3["flatlay"]
    flatlay_caption_html = f'<a href="{flatlay_data["pdp"]}">{flatlay_data["product_name"]}</a> styled on a ceramic cafe tray with brass loupe'
    flatlay_block = build_custom_image_block(
        flatlay_data["media_id"],
        flatlay_data["src"],
        flatlay_data["alt"],
        flatlay_data["pdp"],
        flatlay_caption_html
    )

    lifestyle_data = uploaded_type3["lifestyle"]
    lifestyle_caption_html = f'<a href="{lifestyle_data["pdp"]}">{lifestyle_data["product_name"]}</a> worn as a distinguished everyday men\'s band'
    lifestyle_block = build_custom_image_block(
        lifestyle_data["media_id"],
        lifestyle_data["src"],
        lifestyle_data["alt"],
        lifestyle_data["pdp"],
        lifestyle_caption_html
    )

    # Replace placeholder blocks precisely
    # Find flatlay placeholder
    import re
    flatlay_pattern = r'<!-- wp:image \{"id":0,"sizeSlug":"full","linkDestination":"custom"\} -->\s*<figure class="wp-block-image size-full"><a href="https://www\.bluestone\.com/rings/the-ebony-ring~9686\.html">.*?<!-- /wp:image -->'
    lifestyle_pattern = r'<!-- wp:image \{"id":0,"sizeSlug":"full","linkDestination":"custom"\} -->\s*<figure class="wp-block-image size-full"><a href="https://www\.bluestone\.com/rings/the-jasper-band-for-him~93964\.html">.*?<!-- /wp:image -->'

    if re.search(flatlay_pattern, content, flags=re.DOTALL):
        content = re.sub(flatlay_pattern, flatlay_block, content, count=1, flags=re.DOTALL)
        print("Replaced flatlay placeholder with authentic Type 3 block.")
    else:
        print("Warning: Flatlay placeholder pattern not found!")

    if re.search(lifestyle_pattern, content, flags=re.DOTALL):
        content = re.sub(lifestyle_pattern, lifestyle_block, content, count=1, flags=re.DOTALL)
        print("Replaced lifestyle placeholder with authentic Type 3 block.")
    else:
        print("Warning: Lifestyle placeholder pattern not found!")

    # Update BlogPosting schema images
    hero_src = uploaded_type3["hero"]["src"]
    flatlay_src = uploaded_type3["flatlay"]["src"]
    lifestyle_src = uploaded_type3["lifestyle"]["src"]

    # Inject images array into BlogPosting schema
    img_array_str = f'"image": [\n    "{hero_src}",\n    "{flatlay_src}",\n    "{lifestyle_src}"\n  ],'
    if '"image": [' not in content and '"@type": "BlogPosting"' in content:
        content = content.replace('"@type": "BlogPosting",', f'"@type": "BlogPosting",\n  {img_array_str}')

    # Update WordPress post with featured media and updated content
    update_payload = {
        "featured_media": uploaded_type3["hero"]["media_id"],
        "content": content,
        "meta": {
            "_yoast_wpseo_focuskw": "blue stone ring for men",
            "_yoast_wpseo_title": "Blue Stone Ring for Men Buying Guide 2026 | BlueStone",
            "_yoast_wpseo_metadesc": "Explore our 2026 buying guide for blue stone rings for men. Learn about blue sapphire and topaz, 18K gold settings, bezel security, sizing, and daily care.",
            "_yoast_wpseo_opengraph-image": hero_src,
            "_yoast_wpseo_twitter-image": hero_src
        }
    }

    time.sleep(1)
    patch_req = urllib.request.Request(
        f"{WP_API}/posts/{POST_ID}",
        data=json.dumps(update_payload).encode(),
        headers={**AUTH_HEADERS, "Content-Type": "application/json"},
        method="POST"
    )
    _, patch_body = req_with_retry(patch_req)
    patched_post = json.loads(patch_body.decode())

    print(f"SUCCESS: Post {POST_ID} patched with Type 3 images!")
    print(f"Featured Media ID: {patched_post.get('featured_media')}")
    print(f"Live URL: {patched_post.get('link')}")

if __name__ == "__main__":
    main()
