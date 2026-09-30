#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload Type 3 images and patch WordPress post 40286 for Week 9 Rank 74."""
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
POST_ID = 40286

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
    manifest_path = ROOT / "output" / "Week9_Rank74_NeelamStoneRing_type3_prompts.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    hero_info = manifest["slots"]["hero"]
    flatlay_info = manifest["slots"]["flatlay"]
    lifestyle_info = manifest["slots"]["lifestyle"]

    hero_webp = ROOT / manifest["output"]["hero"]
    flatlay_webp = ROOT / manifest["output"]["flatlay"]
    lifestyle_webp = ROOT / manifest["output"]["lifestyle"]

    if not hero_webp.exists() or not flatlay_webp.exists() or not lifestyle_webp.exists():
        raise FileNotFoundError("One or more Type 3 WebP images are missing. Ensure generation is complete.")

    print("Uploading Type 3 images to WordPress media library...")
    h_id, h_src = upload_image(hero_webp, hero_info["alt"], f"{hero_info['product_name']} hero: Neelam Stone Ring 2026")
    f_id, f_src = upload_image(flatlay_webp, flatlay_info["alt"], f"{flatlay_info['product_name']} flatlay: Neelam Stone Ring 2026")
    l_id, l_src = upload_image(lifestyle_webp, lifestyle_info["alt"], f"{lifestyle_info['product_name']} lifestyle: Neelam Stone Ring 2026")

    type3_uploaded = {
        "hero": {"media_id": h_id, "src": h_src, "alt": hero_info["alt"], "pdp": hero_info["pdp"], "name": hero_info["product_name"]},
        "flatlay": {"media_id": f_id, "src": f_src, "alt": flatlay_info["alt"], "pdp": flatlay_info["pdp"], "name": flatlay_info["product_name"]},
        "lifestyle": {"media_id": l_id, "src": l_src, "alt": lifestyle_info["alt"], "pdp": lifestyle_info["pdp"], "name": lifestyle_info["product_name"]}
    }

    uploaded_record_path = ROOT / "output" / "Week9_Rank74_type3_uploaded_media.json"
    uploaded_record_path.write_text(json.dumps(type3_uploaded, indent=2), encoding="utf-8")

    # Fetch post content
    req = urllib.request.Request(f"{WP_API}/posts/{POST_ID}?context=edit", headers=AUTH_HEADERS)
    with urllib.request.urlopen(req, timeout=120) as resp:
        post_data = json.loads(resp.read().decode())

    content = post_data["content"]["raw"]

    # 1. Replace flatlay placeholder
    flatlay_block = f"""<!-- wp:image {{"id":{f_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{flatlay_info['pdp']}"><img src="{f_src}" alt="{flatlay_info['alt']}" class="wp-image-{f_id}"/></a><figcaption>The <a href="{flatlay_info['pdp']}">{flatlay_info['product_name']}</a> showcased as a masterclass in precious gemstone setting and hallmarked gold craftsmanship</figcaption></figure>
<!-- /wp:image -->"""

    flatlay_pattern = r'<!-- wp:image [^>]*-->\s*<figure[^>]*><a[^>]*><img[^>]*PLACEHOLDER_TYPE3_FLATLAY[^>]*></a><figcaption>[^<]*</figcaption></figure>\s*<!-- /wp:image -->'
    if re.search(flatlay_pattern, content):
        content = re.sub(flatlay_pattern, flatlay_block, content)
        print("Flatlay placeholder replaced successfully!")
    else:
        print("WARNING: Flatlay regex pattern not found, trying string replace...")
        content = content.replace('PLACEHOLDER_TYPE3_FLATLAY', f_src)

    # 2. Replace lifestyle placeholder
    lifestyle_block = f"""<!-- wp:image {{"id":{l_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{lifestyle_info['pdp']}"><img src="{l_src}" alt="{lifestyle_info['alt']}" class="wp-image-{l_id}"/></a><figcaption>The <a href="{lifestyle_info['pdp']}">{lifestyle_info['product_name']}</a> demonstrating refined everyday proportion and contemporary gold styling</figcaption></figure>
<!-- /wp:image -->"""

    lifestyle_pattern = r'<!-- wp:image [^>]*-->\s*<figure[^>]*><a[^>]*><img[^>]*PLACEHOLDER_TYPE3_LIFESTYLE[^>]*></a><figcaption>[^<]*</figcaption></figure>\s*<!-- /wp:image -->'
    if re.search(lifestyle_pattern, content):
        content = re.sub(lifestyle_pattern, lifestyle_block, content)
        print("Lifestyle placeholder replaced successfully!")
    else:
        print("WARNING: Lifestyle regex pattern not found, trying string replace...")
        content = content.replace('PLACEHOLDER_TYPE3_LIFESTYLE', l_src)

    # 3. Inject image array in BlogPosting schema
    img_array_str = f'"image": [\n    "{h_src}",\n    "{f_src}",\n    "{l_src}"\n  ],'
    if '"image": [' not in content and '"@type": "BlogPosting"' in content:
        content = content.replace('"@type": "BlogPosting",', f'"@type": "BlogPosting",\n  {img_array_str}')
        print("BlogPosting schema image array injected!")

    update_payload = {
        "featured_media": h_id,
        "content": content,
        "meta": {
            "_yoast_wpseo_focuskw": "neelam stone ring",
            "_yoast_wpseo_title": "Neelam Stone Ring Buying Guide 2026: Quality, Gold Settings & Designs",
            "_yoast_wpseo_metadesc": "Learn how to choose an authentic neelam stone ring in 2026. Explore blue sapphire 4Cs, BIS 14K vs 18K gold settings, neelam stone ring design styles, and care tips.",
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

    print(f"\nSuccessfully patched WordPress post {POST_ID}!")
    print(f"Live URL: {updated_post['link']}")
    print(f"Featured Media ID: {updated_post.get('featured_media')}")

if __name__ == "__main__":
    main()
