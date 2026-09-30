#!/usr/bin/env python3
"""Prepare Rank 99 product_media JSON after partial carousel upload timeout."""
from __future__ import annotations

import base64
import json
import os
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://blog.bluestone.com/wp-json/wp/v2"


def load_env() -> None:
    for raw_line in (ROOT / ".env").read_text().splitlines():
        line = raw_line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def api(method: str, path: str, data=None, raw_body=None, headers=None):
    token = base64.b64encode(f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD']}".encode()).decode()
    request_headers = {"Authorization": f"Basic {token}", "User-Agent": "BluestoneSEO/1.0"}
    if headers:
        request_headers.update(headers)
    body = raw_body
    if data is not None:
        request_headers["Content-Type"] = "application/json"
        body = json.dumps(data).encode()
    req = urllib.request.Request(f"{API}/{path}", data=body, headers=request_headers, method=method)
    with urllib.request.urlopen(req, timeout=180) as response:
        return json.loads(response.read().decode())


def upload_media(path: Path, alt: str, title: str) -> dict:
    headers = {
        "Content-Disposition": f'attachment; filename="{path.name}"',
        "Content-Type": "image/webp",
    }
    media = api("POST", "media", raw_body=path.read_bytes(), headers=headers)
    api("POST", f"media/{media['id']}", {"alt_text": alt, "title": title})
    return media


def main() -> None:
    load_env()
    cfg = json.loads((ROOT / "output/publish_configs/rank99.json").read_text())
    products = cfg["products"]
    assets = ROOT / f"output/{cfg['output_prefix']}_assets"
    existing = {
        "BIIP0550P16": (31526, "https://blog.bluestone.com/wp-content/uploads/2026/07/the-aagarna-pendant-carousel-16.webp"),
        "BENS0325O09": (31527, "https://blog.bluestone.com/wp-content/uploads/2026/07/the-tarentella-oval-bangle-carousel-7.webp"),
        "BIAR0097R04": (31528, "https://blog.bluestone.com/wp-content/uploads/2026/07/the-anya-ring-carousel-10.webp"),
    }
    product_media = []
    for product in products:
        name = product["name"]
        code = product["code"]
        filename = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower() + "-carousel.webp"
        webp = assets / filename
        alt = f"{cfg['carousel_alt_prefix']}: {name}"
        title = f"{name} carousel, {cfg['occasion_year']}"
        if code in existing:
            media_id, src = existing[code]
            api("POST", f"media/{media_id}", {"alt_text": alt, "title": title})
            print("reused", code, media_id, src)
        else:
            media = upload_media(webp, alt, title)
            media_id, src = media["id"], media["source_url"]
            print("uploaded", code, media_id, src)
        product_media.append({
            "code": code,
            "name": name,
            "url": product["url"],
            "id": media_id,
            "src": src,
            "alt": alt,
            "title": title,
        })
    out = ROOT / f"output/{cfg['output_prefix']}_product_media.json"
    out.write_text(json.dumps(product_media, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", out)


if __name__ == "__main__":
    main()
