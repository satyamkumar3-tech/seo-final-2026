#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload Type 3 images and patch WordPress post 40201 for Week 9 Rank 66."""
import os, sys, json, base64, urllib.request, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Load .env
for ep in [ROOT / ".env", Path("/Users/satyamkumar/Downloads/seo final 2026/.env")]:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('\'\"'))

user = os.environ.get("WP_USER", "blogbluestone")
pwd = os.environ.get("WP_APP_PASSWORD") or os.environ.get("WP_APP_PASS") or os.environ.get("WP_PASSWORD", "")
token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
AUTH_HEADERS = {
    "Authorization": f"Basic {token}",
    "User-Agent": "BluestoneSEO/1.0"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"
POST_ID = 40201

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
    return mid, src_url

def main():
    # Load manifest and media info
    manifest_path = ROOT / "output" / "Week9_Rank66_GarbaJewellery_type3_prompts.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    hero_info = manifest["slots"]["hero"]
    flatlay_info = manifest["slots"]["flatlay"]
    lifestyle_info = manifest["slots"]["lifestyle"]

    hero_webp = ROOT / manifest["output"]["hero"]
    flatlay_webp = ROOT / manifest["output"]["flatlay"]
    lifestyle_webp = ROOT / manifest["output"]["lifestyle"]

    print("Uploading Type 3 images to WordPress media library...")
    h_id, h_src = upload_image(hero_webp, hero_info["alt"], "The Skein Hoop Earrings: Garba Jewellery 2026 Hero")
    f_id, f_src = upload_image(flatlay_webp, flatlay_info["alt"], "The Channing Bangle: Garba Jewellery 2026 Flatlay")
    l_id, l_src = upload_image(lifestyle_webp, lifestyle_info["alt"], "The Lumeelle Cluster Pendant: Garba Jewellery 2026 Lifestyle")

    type3_uploaded = {
        "hero": {"media_id": h_id, "src": h_src, "alt": hero_info["alt"], "pdp": hero_info["pdp"], "name": hero_info["product_name"]},
        "flatlay": {"media_id": f_id, "src": f_src, "alt": flatlay_info["alt"], "pdp": flatlay_info["pdp"], "name": flatlay_info["product_name"]},
        "lifestyle": {"media_id": l_id, "src": l_src, "alt": lifestyle_info["alt"], "pdp": lifestyle_info["pdp"], "name": lifestyle_info["product_name"]}
    }

    uploaded_record_path = ROOT / "output" / "Week9_Rank66_type3_uploaded_media.json"
    uploaded_record_path.write_text(json.dumps(type3_uploaded, indent=2), encoding="utf-8")

    # Fetch post content
    req = urllib.request.Request(f"{WP_API}/posts/{POST_ID}?context=edit", headers=AUTH_HEADERS)
    with urllib.request.urlopen(req, timeout=120) as resp:
        post_data = json.loads(resp.read().decode())

    content = post_data["content"]["raw"]

    # Precise Gutenberg blocks
    flatlay_block = f"""<!-- wp:image {{"id":{f_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{flatlay_info['pdp']}"><img src="{f_src}" alt="{flatlay_info['alt']}" class="wp-image-{f_id}"/></a><figcaption><a href="{flatlay_info['pdp']}">{flatlay_info['product_name']}</a> styled on a festive mantel with marigold petals and traditional brass dandiya</figcaption></figure>
<!-- /wp:image -->"""

    lifestyle_block = f"""<!-- wp:image {{"id":{l_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{lifestyle_info['pdp']}"><img src="{l_src}" alt="{lifestyle_info['alt']}" class="wp-image-{l_id}"/></a><figcaption><a href="{lifestyle_info['pdp']}">{lifestyle_info['product_name']}</a> worn as a vibrant floral centerpiece for festive Navratri evenings</figcaption></figure>
<!-- /wp:image -->"""

    if "<!-- TYPE3_FLATLAY_PLACEHOLDER -->" in content:
        content = content.replace("<!-- TYPE3_FLATLAY_PLACEHOLDER -->", flatlay_block)
        print("Flatlay placeholder replaced successfully!")
    else:
        print("WARNING: Flatlay placeholder not found in content!")

    if "<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->" in content:
        content = content.replace("<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->", lifestyle_block)
        print("Lifestyle placeholder replaced successfully!")
    else:
        print("WARNING: Lifestyle placeholder not found in content!")

    # Inject image array in BlogPosting schema
    img_array_str = f'"image": [\n    "{h_src}",\n    "{f_src}",\n    "{l_src}"\n  ],'
    if '"image": [' not in content and '"@type": "BlogPosting"' in content:
        content = content.replace('"@type": "BlogPosting",', f'"@type": "BlogPosting",\n  {img_array_str}')
        print("BlogPosting schema image array injected!")

    update_payload = {
        "featured_media": h_id,
        "content": content,
        "meta": {
            "_yoast_wpseo_focuskw": "garba jewellery",
            "_yoast_wpseo_title": "How to Choose and Style Garba Jewellery in 2026: An Expert Buyer's Guide | BlueStone",
            "_yoast_wpseo_metadesc": "Master how to choose dance-proof garba jewellery in 2026. Discover lightweight gold hoops, secure clasps, gemstone jewelry pairings, and sweat-safe care tips.",
            "_yoast_wpseo_opengraph-image": h_src,
            "_yoast_wpseo_twitter-image": h_src
        }
    }

    update_req = urllib.request.Request(
        f"{WP_API}/posts/{POST_ID}",
        data=json.dumps(update_payload).encode(),
        headers={**AUTH_HEADERS, "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(update_req, timeout=120) as resp:
        res = json.loads(resp.read().decode())
        print(f"SUCCESS: Post {POST_ID} updated! Featured Media: {res.get('featured_media')}")

if __name__ == "__main__":
    main()
