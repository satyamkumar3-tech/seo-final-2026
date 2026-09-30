#!/usr/bin/env python3
"""Regenerate Type 3 AI images for Week 7 Ranks 184, 185, and 186 using Higgsfield CLI and patch WordPress."""
from __future__ import annotations

import base64
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output"


def load_env():
    for line in (ROOT / ".env").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip("'\""))


def api(method: str, path: str, data=None, raw_body=None, headers=None):
    token = base64.b64encode(f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD']}".encode()).decode()
    h = {"Authorization": f"Basic {token}", "User-Agent": "BluestoneSEO/1.0"}
    if headers:
        h.update(headers)
    body = json.dumps(data).encode() if data is not None else raw_body
    if data is not None:
        h["Content-Type"] = "application/json"
    req = urllib.request.Request(
        f"https://blog.bluestone.com/wp-json/wp/v2/{path}", data=body, headers=h, method=method
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.loads(r.read().decode())


def upload_media(path: Path, alt: str, title: str) -> dict:
    headers = {
        "Content-Disposition": f'attachment; filename="{path.name}"',
        "Content-Type": "image/webp",
    }
    media = api("POST", "media", raw_body=path.read_bytes(), headers=headers)
    api("POST", f"media/{media['id']}", {"alt_text": alt, "title": title})
    return media


def generate_higgsfield_image(prompt: str, output_path: Path, ref_images: list[Path] | None = None) -> Path:
    print(f"  [Higgsfield] Generating: {output_path.name}...")
    cmd = [
        str(Path.home() / ".local" / "bin" / "higgsfield"),
        "generate",
        "create",
        "nano_banana_pro",
        "--prompt",
        prompt,
        "--aspect_ratio",
        "16:9",
        "--resolution",
        "2k",
    ]
    if ref_images:
        for ref in ref_images:
            if ref.exists():
                cmd += ["--image", str(ref)]
    cmd += ["--wait", "--wait-timeout", "10m", "--wait-interval", "5s", "--json"]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"Higgsfield generation failed: {proc.stderr or proc.stdout}")

    data = json.loads(proc.stdout)
    job = data[0] if isinstance(data, list) else data
    result_url = job.get("result_url")
    if not result_url:
        raise RuntimeError(f"No result_url returned in job: {job}")

    raw_path = output_path.with_suffix(".raw.png")
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(result_url, timeout=180) as response:
        raw_path.write_bytes(response.read())

    # Convert to 1400px 16:9 WebP
    img = Image.open(raw_path).convert("RGB")
    if img.width > 1400:
        target_h = round(img.height * 1400 / img.width)
        img = img.resize((1400, target_h), Image.Resampling.LANCZOS)
    img.save(output_path, "WEBP", quality=82, method=6)
    print(f"  [Saved WebP] {output_path} ({img.width}x{img.height})")
    return output_path


CONFIGS = {
    184: {
        "slug": "black-beads-gold-chain-2026",
        "post_id": 36719,
        "assets_dir": OUTPUT_DIR / "Week7_Rank184_Type3_Assets",
        "images": {
            "hero": {
                "filename": "black-beads-gold-chain-hero-2026.webp",
                "alt": "black beads gold chain 2026 trending design, The Yeijah Mangaslsutra Necklace worn by fair-skinned Indian woman",
                "title": "Black Beads Gold Chain 2026 Hero",
                "prompt": "Editorial close-up portrait of an elegant fair-skinned Indian woman wearing a delicate 18K yellow gold black beads chain necklace (The Yeijah Mangalsutra), wearing high-end pastel cream saree, warm morning studio sunlight, cinematic highlight halation, creamy bokeh, natural skin texture, Kodak Portra color grading, photorealistic 8k, authentic jewellery craftsmanship.",
                "ref_sku": "BIMA1081C01",
            },
            "flatlay": {
                "filename": "black-beads-gold-chain-flatlay-2026.webp",
                "alt": "black beads gold chain 2026 flatlay design, The Casma Mangalsutra",
                "title": "Black Beads Gold Chain 2026 Flatlay",
                "caption": "Black beads gold chain 2026 vibe: The Casma Mangalsutra",
                "prompt": "Top-down luxury flatlay of an authentic 18K gold black beads necklace (The Casma Mangalsutra) gracefully arranged on a natural light oak desk with warm kraft paper journal, brass stationery, soft natural daylight casting subtle diagonal shadows, ultra-detailed gold polishing and black spinel bead facets, 8k commercial photography.",
                "ref_sku": "BIMA0780C53",
            },
            "lifestyle": {
                "filename": "black-beads-gold-chain-lifestyle-2026.webp",
                "alt": "black beads gold chain 2026 styling lifestyle, The Yosni Mangalsutra",
                "title": "Black Beads Gold Chain 2026 Lifestyle",
                "caption": "Black beads gold chain 2026 styling: The Yosni Mangalsutra",
                "prompt": "Editorial lifestyle portrait of an elegant fair-skinned Indian woman wearing a sophisticated modern black beads gold chain (The Yosni Mangalsutra), wearing emerald raw silk attire, looking gently off-camera with a graceful smile, warm ambient lighting, filmic depth of field, 8k photorealistic.",
                "ref_sku": "BIMA0780C29",
            },
        },
    },
    185: {
        "slug": "infinity-ring-2026",
        "post_id": 36730,
        "assets_dir": OUTPUT_DIR / "Week7_Rank185_Type3_Assets",
        "images": {
            "hero": {
                "filename": "infinity-ring-hero-2026.webp",
                "alt": "infinity ring 2026 trending design, The Viperine Twist Ring worn by fair-skinned Indian woman",
                "title": "Infinity Ring 2026 Hero",
                "prompt": "Editorial closeup of a manicured hand with fair-skinned tone wearing a sparkling 18K yellow gold and diamond infinity twist ring (The Viperine Twist Ring), resting gracefully near collarbone against champagne silk fabric, warm directional glow, creamy bokeh, hyper-detailed diamond micro-prong sparkle, Kodak Portra 400 filmic contrast, 8k.",
                "ref_sku": "BIJP0993R123",
            },
            "flatlay": {
                "filename": "infinity-ring-flatlay-2026.webp",
                "alt": "infinity ring 2026 flatlay design, The Luvee Highway Ring",
                "title": "Infinity Ring 2026 Flatlay",
                "caption": "Infinity ring 2026 vibe: The Luvee Highway Ring",
                "prompt": "Luxury overhead flatlay of a modern gold infinity ring (The Luvee Highway Ring) placed inside a soft ceramic dish on white Calacatta marble vanity, with blush silk ribbon and crystal perfume bottle silhouette, soft morning window light, high-end fine jewellery photoshoot, 8k.",
                "ref_sku": "BIKR0993R117",
            },
            "lifestyle": {
                "filename": "infinity-ring-lifestyle-2026.webp",
                "alt": "infinity ring 2026 styling lifestyle, The Quinn Ring",
                "title": "Infinity Ring 2026 Lifestyle",
                "caption": "Infinity ring 2026 styling: The Quinn Ring",
                "prompt": "Candid editorial portrait of a fair-skinned Indian woman wearing an elegant gold infinity band (The Quinn Ring) on her hand while holding a fine porcelain coffee cup in a sunlit modern interior, tailored neutral blazer, natural skin glow, creamy depth of field, 8k.",
                "ref_sku": "BIAR0097R16",
            },
        },
    },
    186: {
        "slug": "pearl-chain-2026",
        "post_id": 36741,
        "assets_dir": OUTPUT_DIR / "Week7_Rank186_Type3_Assets",
        "images": {
            "hero": {
                "filename": "pearl-chain-hero-2026.webp",
                "alt": "pearl chain 2026 trending design, The Thaloria Pendant worn on neck by fair-skinned Indian woman",
                "title": "Pearl Chain 2026 Hero",
                "prompt": "Close-up editorial portrait of an elegant fair-skinned Indian woman wearing a fine yellow gold pearl pendant chain (The Thaloria Pendant), soft ivory silk blouse, warm golden hour window light, creamy background blur, iridescent pearl luster and gleaming yellow gold chain links, 8k cinema quality.",
                "ref_sku": "BISW1080P131",
            },
            "flatlay": {
                "filename": "pearl-chain-flatlay-2026.webp",
                "alt": "pearl chain 2026 flatlay design, The Tetyana Gold Chain",
                "title": "Pearl Chain 2026 Flatlay",
                "caption": "Pearl chain 2026 vibe: The Tetyana Gold Chain",
                "prompt": "Overhead fine jewellery still life of an authentic gold pearl chain (The Tetyana Gold Chain) laid delicately across a sage green velvet tray on Italian marble, surrounded by natural freshwater seed pearls, soft diffused morning studio lighting, 8k photorealistic.",
                "ref_sku": "BVEM0663C88",
            },
            "lifestyle": {
                "filename": "pearl-chain-lifestyle-2026.webp",
                "alt": "pearl chain 2026 styling lifestyle, The Lumeelle Cluster Pendant",
                "title": "Pearl Chain 2026 Lifestyle",
                "caption": "Pearl chain 2026 styling: The Lumeelle Cluster Pendant",
                "prompt": "Editorial fashion portrait of a stylish fair-skinned Indian woman in a tailored cream linen blazer delicately adjusting her gold pearl station necklace (The Lumeelle Cluster Pendant), warm diffused sunlight, natural candid expression, filmic tonal response, 8k.",
                "ref_sku": "BISW1080P133",
            },
        },
    },
}


def patch_post_with_new_images(rank: int, media_ids: dict[str, dict]):
    cfg = CONFIGS[rank]
    post_id = cfg["post_id"]
    print(f"\n[Patching Post {post_id}] {cfg['slug']}...")

    post = api("GET", f"posts/{post_id}?context=edit")
    content = post["content"]["raw"]

    hero_media = media_ids["hero"]
    flatlay_media = media_ids["flatlay"]
    lifestyle_media = media_ids["lifestyle"]

    # Replace existing image blocks or update IDs/URLs
    for slot_name, media_info in [("flatlay", flatlay_media), ("lifestyle", lifestyle_media)]:
        old_pattern = rf'<!-- wp:image \{{"id":\d+,"sizeSlug":"full","linkDestination":"none"\}} -->\s*<figure class="wp-block-image size-full"><img src="[^"]*?{slot_name}[^"]*?" alt="[^"]*?" class="wp-image-\d+"[^>]*?/>(?:\s*<figcaption>.*?</figcaption>)?\s*</figure>\s*<!-- /wp:image -->'
        caption_html = f"<figcaption>{cfg['images'][slot_name].get('caption', '')}</figcaption>" if cfg['images'][slot_name].get('caption') else ""
        new_block = (
            f'<!-- wp:image {{"id":{media_info["id"]},"sizeSlug":"full","linkDestination":"none"}} -->\n'
            f'<figure class="wp-block-image size-full"><img src="{media_info["source_url"]}" alt="{media_info["alt_text"]}" class="wp-image-{media_info["id"]}"/>'
            f'{caption_html}</figure>\n<!-- /wp:image -->'
        )
        if re.search(old_pattern, content):
            content = re.sub(old_pattern, new_block, content, count=1)
        else:
            print(f"  Note: Could not match exact old {slot_name} block regex, will preserve structure.")

    # Update featured media and Yoast metadata
    update_data = {
        "featured_media": hero_media["id"],
        "content": content,
        "meta": {
            "_yoast_wpseo_opengraph-image": hero_media["source_url"],
            "_yoast_wpseo_opengraph-image-id": hero_media["id"],
            "_yoast_wpseo_twitter-image": hero_media["source_url"],
            "_yoast_wpseo_twitter-image-id": hero_media["id"],
        },
    }
    res = api("POST", f"posts/{post_id}", data=update_data)
    print(f"  [Updated WP Post] Post ID: {res['id']} | Featured Media: {res.get('featured_media')}")


def process_rank(rank: int):
    print(f"\n========================================================")
    print(f"PROCESSING WEEK 7 RANK {rank}: {CONFIGS[rank]['slug']}")
    print(f"========================================================")
    cfg = CONFIGS[rank]
    cfg["assets_dir"].mkdir(parents=True, exist_ok=True)
    media_ids = {}

    for slot, item in cfg["images"].items():
        out_file = cfg["assets_dir"] / item["filename"]
        # Find reference SKU image if available
        ref_images = []
        sku_dir = ROOT / "ProductImages" / item.get("ref_sku", "")
        if sku_dir.exists():
            for p in sku_dir.glob("*.png"):
                ref_images.append(p)
            for p in sku_dir.glob("*.jpg"):
                ref_images.append(p)

        generate_higgsfield_image(item["prompt"], out_file, ref_images)
        media = upload_media(out_file, item["alt"], item["title"])
        media_ids[slot] = media
        print(f"  [Uploaded] {slot} -> WP Media ID: {media['id']} ({media['source_url']})")

    patch_post_with_new_images(rank, media_ids)
    print(f"[Done Rank {rank}] https://blog.bluestone.com/{cfg['slug']}/")


def main():
    load_env()
    ranks = [int(r) for r in sys.argv[1:] if r.isdigit()] if len(sys.argv) > 1 else [184, 185, 186]
    for r in ranks:
        if r in CONFIGS:
            process_rank(r)
        else:
            print(f"Unknown rank: {r}")


if __name__ == "__main__":
    main()
