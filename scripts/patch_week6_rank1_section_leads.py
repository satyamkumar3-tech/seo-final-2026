#!/usr/bin/env python3
import base64
import json
import os
import pathlib
import sys
from typing import Optional
import urllib.request

POST_ID = 34778
ARTICLE = pathlib.Path("output/Week6_Rank1_KarwaChauthGiftWife_article.html")
API = "https://blog.bluestone.com/wp-json/wp/v2"


def load_env(path: pathlib.Path = pathlib.Path(".env")) -> None:
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def api(method: str, path: str, payload: Optional[dict] = None) -> dict:
    token = base64.b64encode(f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD']}".encode()).decode()
    headers = {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json",
    }
    data = None if payload is None else json.dumps(payload).encode()
    req = urllib.request.Request(f"{API}/{path}", data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode())


def main() -> int:
    load_env()
    missing = [name for name in ("WP_USER", "WP_APP_PASSWORD") if not os.environ.get(name)]
    if missing:
        print(f"Missing required env: {', '.join(missing)}", file=sys.stderr)
        return 2

    content = ARTICLE.read_text()
    bad = "Copy ready lines for karwa chauth gift for wife"
    if bad.lower() in content.lower():
        print("Refusing to publish: bad fallback phrase still exists locally.", file=sys.stderr)
        return 3

    updated = api("POST", f"posts/{POST_ID}", {"content": content})
    print(json.dumps({"id": updated["id"], "link": updated["link"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
