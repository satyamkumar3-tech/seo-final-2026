#!/usr/bin/env python3
"""Upload remaining Rank 2 carousel media and create a reusable product media manifest."""
from __future__ import annotations

import base64
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
API = "https://blog.bluestone.com/wp-json/wp/v2"
CONFIG = ROOT / "output/publish_configs/week34_rank2.json"
OUT = ROOT / "output/Week34_Rank2_DiwaliInstagramCaptions_product_media_preuploaded.json"

SEEDED = {
    "BIHS1145P21": {
        "id": 31817,
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/07/the-valeria-rose-pendant-carousel-29.webp",
    },
    "BISM0003O14": {
        "id": 31818,
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/07/the-muricelle-bangle-carousel-21.webp",
    },
    "BIPN0880H218": {
        "id": 31819,
        "src": "https://blog.bluestone.com/wp-content/uploads/2026/07/the-nettile-huggie-earrings-carousel-10.webp",
    },
}


def load_env() -> None:
    for raw in (ROOT / ".env").read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def api(method: str, path: str, data=None, raw_body=None, headers=None):
    token = base64.b64encode(f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD']}".encode()).decode()
    req_headers = {"Authorization": f"Basic {token}", "User-Agent": "BluestoneSEO/1.0"}
    if headers:
        req_headers.update(headers)
    if data is not None:
        req_headers["Content-Type"] = "application/json"
        body = json.dumps(data).encode()
    else:
        body = raw_body
    req = urllib.request.Request(f"{API}/{path}", data=body, headers=req_headers, method=method)
    with urllib.request.urlopen(req, timeout=180) as response:
        return json.loads(response.read().decode())


def to_webp(src: Path, dest: Path) -> None:
    image = Image.open(src).convert("RGB")
    target_w, target_h = 960, 535
    image.thumbnail((target_w, target_h), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (target_w, target_h), (245, 243, 240))
    canvas.paste(image, ((target_w - image.width) // 2, (target_h - image.height) // 2))
    dest.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dest, "WEBP", quality=82, method=6)


def upload_media(path: Path, alt: str, title: str):
    media = api(
        "POST",
        "media",
        raw_body=path.read_bytes(),
        headers={"Content-Disposition": f'attachment; filename="{path.name}"', "Content-Type": "image/webp"},
    )
    last_error = None
    for _ in range(2):
        try:
            api("POST", f"media/{media['id']}", {"alt_text": alt, "title": title})
            return media
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(10)
    print(json.dumps({"uploaded_id_before_metadata_error": media["id"], "source_url": media["source_url"]}))
    raise last_error


def main() -> None:
    load_env()
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    assets = ROOT / f"output/{cfg['output_prefix']}_assets"
    existing = {}
    if OUT.exists():
        for item in json.loads(OUT.read_text(encoding="utf-8")):
            existing[item["code"]] = item

    product_media = []
    for product in cfg["products"]:
        code = product["code"]
        alt = f"{cfg['carousel_alt_prefix']}: {product['name']}"
        title = f"{product['name']} carousel, {cfg['occasion_year']}"
        if code in existing:
            item = existing[code]
        elif code in SEEDED:
            item = {
                "code": code,
                "name": product["name"],
                "url": product["url"],
                "id": SEEDED[code]["id"],
                "src": SEEDED[code]["src"],
                "alt": alt,
                "title": title,
            }
        else:
            src = ROOT / product["png"]
            filename = re.sub(r"[^A-Za-z0-9]+", "-", product["name"]).strip("-").lower() + "-carousel.webp"
            webp = assets / filename
            if not webp.exists():
                to_webp(src, webp)
            media = upload_media(webp, alt, title)
            item = {
                "code": code,
                "name": product["name"],
                "url": product["url"],
                "id": media["id"],
                "src": media["source_url"],
                "alt": alt,
                "title": title,
            }
        product_media.append(item)
        OUT.write_text(json.dumps(product_media, indent=2) + "\n", encoding="utf-8")
        print("ready", code, item["id"], item["src"])

    cfg["preuploaded_product_media_json"] = str(OUT.relative_to(ROOT))
    CONFIG.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")
    print("wrote", OUT.relative_to(ROOT))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
