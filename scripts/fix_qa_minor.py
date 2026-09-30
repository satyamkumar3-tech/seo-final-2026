import os
import json
import base64
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

env = {}
with open(ROOT / ".env") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            env[k.strip()] = v.strip().strip('\'\"')

token = base64.b64encode(f"{env['WP_USER']}:{env['WP_APP_PASSWORD']}".encode()).decode()
AUTH_HEADERS = {
    "Authorization": f"Basic {token}",
    "User-Agent": "BluestoneSEO/1.0",
    "Content-Type": "application/json"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"

# 1. Update media titles to remove em dashes
media_updates = [
    (40176, "Yellow Stone Ring 2026 Hero: The Gigi Ring"),
    (40177, "Yellow Stone Ring 2026 Flatlay: The Malibu Ring"),
    (40178, "Yellow Stone Ring 2026 Lifestyle: The Viperine Twist Ring")
]

for mid, clean_title in media_updates:
    req = urllib.request.Request(
        f"{WP_API}/media/{mid}",
        data=json.dumps({"title": clean_title}).encode(),
        headers=AUTH_HEADERS,
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        print(f"Updated title for media {mid}: {clean_title}")

# 2. Update post meta with opengraph-image-id
hero_url = "https://blog.bluestone.com/wp-content/uploads/2026/09/yellow-stone-ring-hero-2026.webp"
post_update = {
    "featured_media": 40176,
    "meta": {
        "_yoast_wpseo_focuskw": "yellow stone ring",
        "_yoast_wpseo_title": "Yellow Stone Ring Guide 2026: Types, Settings & Purity | BlueStone",
        "_yoast_wpseo_metadesc": "Complete 2026 buying guide to yellow stone rings. Compare yellow sapphire, citrine, and topaz, explore 14K vs 18K gold settings, BIS hallmarking, and daily care.",
        "_yoast_wpseo_opengraph-image": hero_url,
        "_yoast_wpseo_opengraph-image-id": 40176,
        "_yoast_wpseo_twitter-image": hero_url,
        "_yoast_wpseo_twitter-image-id": 40176
    }
}

p_req = urllib.request.Request(
    f"{WP_API}/posts/40175",
    data=json.dumps(post_update).encode(),
    headers=AUTH_HEADERS,
    method="POST"
)
with urllib.request.urlopen(p_req) as resp:
    res = json.loads(resp.read().decode())
    print("Post updated. Featured media:", res.get("featured_media"))
