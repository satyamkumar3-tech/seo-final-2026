#!/usr/bin/env python3
"""Generic Type 3 patch: upload hero/flatlay/lifestyle, set featured, insert before H2s, refresh schema."""
from __future__ import annotations

import base64
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_env():
    for line in (ROOT / ".env").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip("'\""))


def api(method, path, data=None, raw_body=None, headers=None):
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


def upload_media(path, alt, title):
    headers = {
        "Content-Disposition": f'attachment; filename="{path.name}"',
        "Content-Type": "image/webp",
    }
    media = api("POST", "media", raw_body=path.read_bytes(), headers=headers)
    api("POST", f"media/{media['id']}", {"alt_text": alt, "title": title})
    return media


def prepare_webp(path: Path) -> None:
    if path.exists():
        return
    raw = path.with_suffix(".raw.png")
    if not raw.exists():
        raise SystemExit(f"Missing {path} and source raw {raw}")
    from PIL import Image

    image = Image.open(raw).convert("RGB")
    if image.width > 1400:
        height = round(image.height * 1400 / image.width)
        image = image.resize((1400, height), Image.Resampling.LANCZOS)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "WEBP", quality=82, method=6)


def image_block(mid, src, alt, caption: str | None = None):
    clean_alt = re.sub(r"[^A-Za-z0-9\s,\.\-\'\!\(\)\?]", "", alt)
    clean_cap = ""
    if caption:
        clean_cap = re.sub(r"[^A-Za-z0-9\s,\.\-\'\!\(\)\?:]", "", caption).strip()
    figcaption = (
        f'<figcaption>{clean_cap}</figcaption>' if clean_cap else ""
    )
    return (
        f'<!-- wp:image {{"id":{mid},"sizeSlug":"full","linkDestination":"none"}} -->\n'
        f'<figure class="wp-block-image size-full">'
        f'<img src="{src}" alt="{clean_alt}" class="wp-image-{mid}"/>'
        f"{figcaption}"
        f"</figure>\n<!-- /wp:image -->"
    )


def find_h2_target(content_clean: str, heading: str) -> str:
    candidates = [
        f'<h2 class="wp-block-heading">{heading}</h2>',
        f'<h2 class="wp-block-heading">{heading.replace(chr(39), "&#x27;")}</h2>',
        f'<h2 class="wp-block-heading">{heading.replace(chr(39), "&#39;")}</h2>',
    ]
    for target in candidates:
        if target in content_clean:
            return target
    raise SystemExit(f"Could not find {heading!r} heading for image insertion.")


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: patch_week1_type3_generic.py path/to/type3_prompts.json")
    prompts_path = Path(sys.argv[1])
    if not prompts_path.is_absolute():
        prompts_path = ROOT / prompts_path
    prompts = json.loads(prompts_path.read_text(encoding="utf-8"))
    post_id = prompts.get("wp_post_id")
    if not post_id:
        raise SystemExit("Set wp_post_id in type3 prompts JSON first.")

    insert = json.loads((ROOT / prompts["insert_h2s_json"]).read_text(encoding="utf-8"))
    slug = insert["slug"]
    title = insert["title"]
    meta_desc = insert["meta_desc"]
    faqs = insert["faqs"]
    flatlay_h2 = insert["flatlay"]
    lifestyle_h2 = insert["lifestyle"]
    product_media = json.loads((ROOT / prompts["product_media_json"]).read_text(encoding="utf-8"))
    prefix = prompts.get("output_prefix") or slug
    media_checkpoint_path = ROOT / f"output/{prefix}_type3_media.json"

    load_env()
    print("Fetching post...")
    post = api("GET", f"posts/{post_id}?context=edit")
    content = post["content"]["raw"]

    print("Stripping ALL old wp:image blocks...")
    content_clean = re.sub(
        r"<!-- wp:image \{.*?\} -->\s*<figure.*?</figure>\s*<!-- /wp:image -->",
        "",
        content,
        flags=re.DOTALL,
    )
    content_clean = re.sub(
        r'<!-- wp:html -->\s*<script type="application/ld\+json" id="bs-faq-schema">.*?</script>\s*'
        r'<script type="application/ld\+json" id="bs-blogposting-schema">.*?</script>\s*<!-- /wp:html -->',
        "",
        content_clean,
        flags=re.DOTALL,
    ).strip()

    uploaded = (
        json.loads(media_checkpoint_path.read_text(encoding="utf-8"))
        if media_checkpoint_path.exists()
        else {}
    )
    featured_id = None
    for slot in ("hero", "flatlay", "lifestyle"):
        cfg = prompts["slots"][slot]
        src = ROOT / prompts["output"][slot]
        prepare_webp(src)
        alt = cfg["alt"]
        media_title = prompts.get("media_titles", {}).get(slot) or f"{insert['focus_kw']} {slot}"
        existing = uploaded.get(slot)
        if existing and existing.get("id") and existing.get("src"):
            try:
                api("GET", f"media/{existing['id']}?context=edit")
            except Exception:  # noqa: BLE001
                existing = None
        if existing:
            uploaded[slot] = {"id": existing["id"], "src": existing["src"], "alt": alt}
            print(f"Reusing {slot} media {existing['id']}")
        else:
            print(f"Uploading {slot}...")
            media = upload_media(src, alt, media_title)
            uploaded[slot] = {"id": media["id"], "src": media["source_url"], "alt": alt}
            media_checkpoint_path.write_text(
                json.dumps(uploaded, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
        if slot == "hero":
            featured_id = uploaded[slot]["id"]
        print(f"  {slot} -> {uploaded[slot]['id']}")

    def slot_caption(slot: str) -> str:
        cfg = prompts["slots"][slot]
        explicit = cfg.get("caption") or prompts.get("captions", {}).get(slot)
        if explicit:
            return explicit
        product_name = (cfg.get("product") or {}).get("name") or ""
        occasion = prompts.get("caption_occasion") or insert.get("focus_kw") or "Festive"
        year = prompts.get("caption_year") or "2026"
        if product_name:
            return f"{occasion} {year} vibe: {product_name}"
        return f"{occasion} {year} moment"

    flatlay_target = find_h2_target(content_clean, flatlay_h2)
    content_clean = content_clean.replace(
        flatlay_target,
        f"{image_block(uploaded['flatlay']['id'], uploaded['flatlay']['src'], uploaded['flatlay']['alt'], slot_caption('flatlay'))}\n\n{flatlay_target}",
        1,
    )
    lifestyle_target = find_h2_target(content_clean, lifestyle_h2)
    content_clean = content_clean.replace(
        lifestyle_target,
        f"{image_block(uploaded['lifestyle']['id'], uploaded['lifestyle']['src'], uploaded['lifestyle']['alt'], slot_caption('lifestyle'))}\n\n{lifestyle_target}",
        1,
    )

    faq_schema = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for q, a in faqs
    ]
    faq_page = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_schema}
    all_images = [
        uploaded["hero"]["src"],
        uploaded["flatlay"]["src"],
        uploaded["lifestyle"]["src"],
    ] + [p["src"] for p in product_media]
    blog_posting = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": meta_desc,
        "datePublished": post["date"][:10],
        "dateModified": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "author": {"@type": "Person", "name": "Satyam"},
        "publisher": {"@type": "Organization", "name": "BlueStone", "url": "https://www.bluestone.com/"},
        "image": all_images,
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"https://blog.bluestone.com/{slug}/"},
        "keywords": prompts.get("schema_keywords") or [insert["focus_kw"]],
    }
    schema_block = (
        "\n\n<!-- wp:html -->\n"
        f'<script type="application/ld+json" id="bs-faq-schema">{json.dumps(faq_page, ensure_ascii=False)}</script>\n'
        f'<script type="application/ld+json" id="bs-blogposting-schema">{json.dumps(blog_posting, ensure_ascii=False)}</script>\n'
        "<!-- /wp:html -->\n"
    )
    final_content = content_clean + schema_block
    img_blocks = re.findall(r"<!-- wp:image", final_content)
    print(f"  Image blocks in content: {len(img_blocks)} (expected: 2)")
    assert len(img_blocks) == 2, f"Expected 2 image blocks, found {len(img_blocks)}"

    updated = api(
        "POST",
        f"posts/{post_id}",
        {
            "content": final_content,
            "featured_media": featured_id,
            "author": 270271337,
            "categories": prompts.get("categories") or post.get("categories") or [],
            "meta": {
                "_yoast_wpseo_opengraph-image": uploaded["hero"]["src"],
                "_yoast_wpseo_twitter-image": uploaded["hero"]["src"],
            },
        },
    )
    print(f"Post updated! URL: {updated['link']}")
    (ROOT / f"output/{prefix}_article.html").write_text(final_content, encoding="utf-8")
    media_checkpoint_path.write_text(
        json.dumps(uploaded, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
