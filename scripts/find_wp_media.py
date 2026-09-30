#!/usr/bin/env python3
"""Read-only WordPress media search by term."""
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
    for raw in (ROOT / ".env").read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: find_wp_media.py search-term [search-term...]")
    load_env()
    token = base64.b64encode(f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD']}".encode()).decode()
    headers = {"Authorization": f"Basic {token}", "User-Agent": "BluestoneSEO/1.0"}
    out = {}
    for term in sys.argv[1:]:
        query = urllib.parse.urlencode({"search": term, "per_page": 20, "orderby": "date", "order": "desc"})
        req = urllib.request.Request(f"{API}/media?{query}", headers=headers)
        with urllib.request.urlopen(req, timeout=60) as response:
            media = json.loads(response.read().decode())
        out[term] = [
            {
                "id": item["id"],
                "date": item["date"],
                "slug": item["slug"],
                "title": item["title"]["rendered"],
                "source_url": item["source_url"],
                "alt_text": item.get("alt_text", ""),
            }
            for item in media
        ]
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
