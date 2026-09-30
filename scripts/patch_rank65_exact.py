#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch exact Gutenberg image blocks into post 40188."""
import os, sys, json, base64, urllib.request, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

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
POST_ID = 40188

# Load media info
media_info = json.loads((ROOT / "output/Week9_Rank65_type3_media.json").read_text())
hero = media_info["hero"]
flatlay = media_info["flatlay"]
lifestyle = media_info["lifestyle"]

# Get post
req = urllib.request.Request(f"{WP_API}/posts/{POST_ID}?context=edit", headers=AUTH_HEADERS)
with urllib.request.urlopen(req) as resp:
    post_data = json.loads(resp.read().decode())

content = post_data["content"]["raw"]

# Precise flatlay block
flatlay_block = f"""<!-- wp:image {{"id":{flatlay['media_id']},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{flatlay['pdp']}"><img src="{flatlay['src']}" alt="{flatlay['alt']}" class="wp-image-{flatlay['media_id']}"/></a><figcaption><a href="{flatlay['pdp']}">{flatlay['product_name']}</a> styled on a ceramic cafe tray with brass loupe</figcaption></figure>
<!-- /wp:image -->"""

# Precise lifestyle block
lifestyle_block = f"""<!-- wp:image {{"id":{lifestyle['media_id']},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{lifestyle['pdp']}"><img src="{lifestyle['src']}" alt="{lifestyle['alt']}" class="wp-image-{lifestyle['media_id']}"/></a><figcaption><a href="{lifestyle['pdp']}">{lifestyle['product_name']}</a> worn as a distinguished everyday men's band</figcaption></figure>
<!-- /wp:image -->"""

import re
# Match the figure containing placeholder-flatlay
flatlay_regex = r'<figure class="wp-block-image size-full"><a href="https://www\.bluestone\.com/rings/the-ebony-ring~9686\.html"><img [^>]*?placeholder-flatlay\.webp[^>]*?/></a><figcaption>.*?</figcaption></figure>'
lifestyle_regex = r'<figure class="wp-block-image size-full"><a href="https://www\.bluestone\.com/rings/the-jasper-band-for-him~93964\.html"><img [^>]*?placeholder-lifestyle\.webp[^>]*?/></a><figcaption>.*?</figcaption></figure>'

if re.search(flatlay_regex, content):
    content = re.sub(flatlay_regex, flatlay_block, content, count=1)
    print("Flatlay placeholder replaced successfully!")
else:
    print("ERROR: Flatlay placeholder regex did not match!")

if re.search(lifestyle_regex, content):
    content = re.sub(lifestyle_regex, lifestyle_block, content, count=1)
    print("Lifestyle placeholder replaced successfully!")
else:
    print("ERROR: Lifestyle placeholder regex did not match!")

# Inject BlogPosting schema images array
h_src = hero['src']
f_src = flatlay['src']
l_src = lifestyle['src']
img_array_str = f'"image": [\n    "{h_src}",\n    "{f_src}",\n    "{l_src}"\n  ],'
if '"image": [' not in content and '"@type": "BlogPosting"' in content:
    content = content.replace('"@type": "BlogPosting",', f'"@type": "BlogPosting",\n  {img_array_str}')
    print("BlogPosting schema image array injected!")

update_payload = {
    "featured_media": hero["media_id"],
    "content": content,
    "meta": {
        "_yoast_wpseo_focuskw": "blue stone ring for men",
        "_yoast_wpseo_title": "Blue Stone Ring for Men Buying Guide 2026 | BlueStone",
        "_yoast_wpseo_metadesc": "Explore our 2026 buying guide for blue stone rings for men. Learn about blue sapphire and topaz, 18K gold settings, bezel security, sizing, and daily care.",
        "_yoast_wpseo_opengraph-image": hero["src"],
        "_yoast_wpseo_twitter-image": hero["src"]
    }
}

update_req = urllib.request.Request(
    f"{WP_API}/posts/{POST_ID}",
    data=json.dumps(update_payload).encode(),
    headers={**AUTH_HEADERS, "Content-Type": "application/json"},
    method="POST"
)
with urllib.request.urlopen(update_req) as resp:
    res = json.loads(resp.read().decode())
    print(f"SUCCESS: Post {POST_ID} updated! Featured Media: {res.get('featured_media')}")
