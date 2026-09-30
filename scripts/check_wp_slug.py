#!/usr/bin/env python3
"""Read-only WordPress slug check."""
from __future__ import annotations

import base64
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://blog.bluestone.com/wp-json/wp/v2"


def load_env() -> None:
    env_path = ROOT / ".env"
    for raw in env_path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: check_wp_slug.py slug")
    slug = sys.argv[1]
    load_env()
    token = base64.b64encode(f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD']}".encode()).decode()
    query = urllib.parse.urlencode(
        {"slug": slug, "status": "publish,draft,pending,private,future", "per_page": 20}
    )
    req = urllib.request.Request(
        f"{API}/posts?{query}",
        headers={"Authorization": f"Basic {token}", "User-Agent": "BluestoneSEO/1.0"},
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        posts = json.loads(response.read().decode())
    print(json.dumps({"count": len(posts), "ids": [p["id"] for p in posts], "links": [p["link"] for p in posts]}, indent=2))


if __name__ == "__main__":
    main()
