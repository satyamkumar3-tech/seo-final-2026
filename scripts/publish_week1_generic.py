#!/usr/bin/env python3
"""Generic New-publish for Week 1 ranks driven by a config JSON + sections JSON."""
from __future__ import annotations

import base64
import json
import os
import re
import sys
import urllib.request
from urllib.parse import quote
from datetime import datetime, timezone
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT_FESTIVE = 554493477
CAT_QUOTES = 554493415
CAT_GIFT = 554493424
CAT_JEWELLERY_LIFESTYLE = 554493425
CAT_JEWELLERY_PROBLEM_SOLUTION = 554493465
CAT_JEWELLERY_TRENDS = 554493317
CAT_GOLD = 554493348
CAT_WEDDING_JEWELLERY = 554493443
CAT_KIDS_JEWELLERY = 554493433
CAT_MENS_JEWELLERY = 554493434
LOCAL_ONLY = os.environ.get("BS_LOCAL", "").lower() in ("1", "true", "yes")


def load_local_env():
    env_path = ROOT / ".env"
    if env_path.exists():
        for raw_line in env_path.read_text().splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_local_env()
USER = os.environ.get("WP_USER", "")
PWD = os.environ.get("WP_APP_PASSWORD", "")
TOKEN = base64.b64encode(f"{USER}:{PWD}".encode()).decode() if USER and PWD else ""
AUTH = {"Authorization": f"Basic {TOKEN}", "User-Agent": "BluestoneSEO/1.0"} if TOKEN else {}
API = "https://blog.bluestone.com/wp-json/wp/v2"


def api(method, path, data=None, raw_body=None, headers=None):
    request_headers = dict(AUTH)
    if headers:
        request_headers.update(headers)
    if data is not None:
        request_headers["Content-Type"] = "application/json"
        body = json.dumps(data).encode()
    else:
        body = raw_body
    req = urllib.request.Request(f"{API}/{path}", data=body, headers=request_headers, method=method)
    with urllib.request.urlopen(req, timeout=180) as response:
        return json.loads(response.read().decode())


def to_carousel_webp(src: Path, dest: Path):
    from PIL import Image

    image = Image.open(src).convert("RGB")
    target_w, target_h = 960, 535
    image.thumbnail((target_w, target_h), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (target_w, target_h), (245, 243, 240))
    canvas.paste(image, ((target_w - image.width) // 2, (target_h - image.height) // 2))
    dest.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dest, "WEBP", quality=82, method=6)


def upload_media(path: Path, alt: str, title: str):
    headers = {
        "Content-Disposition": f'attachment; filename="{path.name}"',
        "Content-Type": "image/webp",
    }
    media = api("POST", "media", raw_body=path.read_bytes(), headers=headers)
    api("POST", f"media/{media['id']}", {"alt_text": alt, "title": title})
    return media


def h2(text):
    return f'<!-- wp:heading -->\n<h2 class="wp-block-heading">{escape(text)}</h2>\n<!-- /wp:heading -->'


def h3(text):
    return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{escape(text)}</h3>\n<!-- /wp:heading -->'


def para(text):
    return f'<!-- wp:paragraph -->\n<p>{text}</p>\n<!-- /wp:paragraph -->'


def list_block(items, ordered=True):
    tag = "ol" if ordered else "ul"
    attrs = ' {"ordered":true}' if ordered else ""
    lines = [f"<!-- wp:list{attrs} -->", f'<{tag} class="wp-block-list">']
    lines.extend(f"<li>{escape(item)}</li>" for item in items)
    lines.extend([f"</{tag}>", "<!-- /wp:list -->"])
    return "\n".join(lines)


def normalize_sections(raw):
    """Return list of {key,h2,lines}."""
    out = []
    if isinstance(raw, list):
        for i, block in enumerate(raw):
            out.append(
                {
                    "key": f"sec_{i}",
                    "h2": block["h2"],
                    "lines": block["lines"],
                }
            )
        return out
    for key, block in raw.items():
        if isinstance(block, list):
            out.append({"key": key, "h2": key.replace("_", " ").title(), "lines": block})
        else:
            out.append({"key": key, "h2": block["h2"], "lines": block["lines"]})
    return out


def build_carousel(product_media, carousel_id, aria_label):
    cards = []
    dots = []
    for index, product in enumerate(product_media):
        cards.append(
            f'    <div class="bs-cf-card" data-i="{index}">\n'
            f'      <a class="bs-cf-media" href="{product["url"]}">\n'
            f'        <img src="{product["src"]}" alt="{escape(product["alt"])}" width="960" height="535" loading="lazy" decoding="async"/>\n'
            f"      </a>\n"
            f'      <div class="bs-cf-meta">\n'
            f'        <p class="bs-cf-name">{escape(product["name"])}</p>\n'
            f'        <a class="bs-cf-cta" href="{product["url"]}">Buy now</a>\n'
            f"      </div>\n"
            f"    </div>"
        )
        active = " is-active" if index == 0 else ""
        dots.append(
            f'    <button type="button" class="bs-cf-dot{active}" data-i="{index}" aria-label="Product {index + 1}"></button>'
        )
    template = (ROOT / "templates/eid_carousel_6_snippet.html").read_text()
    style = template.split("<style>", 1)[1].split("</style>", 1)[0]
    script = template.split("<script>", 1)[1].split("</script>", 1)[0]
    script = script.replace("bs-cf-eid", carousel_id)
    return (
        "<!-- wp:html -->\n<style>\n"
        + style
        + f'\n</style>\n<div class="bs-cf" id="{carousel_id}" data-interval="3200" aria-roledescription="carousel" aria-label="{escape(aria_label)}">\n'
        + '  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>\n'
        + '  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>\n'
        + '  <div class="bs-cf-stage">\n'
        + "\n".join(cards)
        + '\n  </div>\n  <div class="bs-cf-dots" role="tablist">\n'
        + "\n".join(dots)
        + "\n  </div>\n</div>\n<script>\n"
        + script
        + "\n</script>\n<!-- /wp:html -->"
    )


def build_faqs(faqs, faq_h2):
    html = [h2(faq_h2)]
    schema = []
    for question, answer in faqs:
        html.append(h3(question))
        html.append(para(escape(answer)))
        schema.append(
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {"@type": "Answer", "text": answer},
            }
        )
    return "\n\n".join(html), schema


def build_product_recommendations(cfg):
    recs = cfg.get("product_recommendations") or []
    if not recs:
        return []
    blocks = [h2(cfg.get("product_recommendations_h2") or "Recommended BlueStone Jewellery Gifts")]
    intro = cfg.get("product_recommendations_intro")
    if intro:
        blocks.append(para(escape(intro)))
    for rec in recs:
        name = rec["name"]
        url = rec["url"]
        best_for = rec.get("best_for") or "a thoughtful jewellery gift"
        why = rec.get("why") or ""
        tip = rec.get("tip") or ""
        blocks.append(h3(f"{name}: {best_for}"))
        body = f'<a href="{escape(url, quote=True)}">{escape(name)}</a>'
        if why:
            body += f" {escape(why)}"
        blocks.append(para(body))
        if tip:
            blocks.append(para(f"<em>Gifting tip:</em> {escape(tip)}"))
    return blocks


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: publish_week1_generic.py path/to/publish_config.json")
    cfg_path = Path(sys.argv[1])
    if not cfg_path.is_absolute():
        cfg_path = ROOT / cfg_path
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))

    content_data = json.loads((ROOT / cfg["sections_json"]).read_text(encoding="utf-8"))
    meta = content_data["meta"]
    title = meta["title"]
    slug = meta["slug"]
    meta_desc = meta["meta_desc"]
    focus_kw = meta["focus_kw"]
    yoast_title = meta["yoast_title"]
    live_url = f"https://blog.bluestone.com/{slug}/"
    intros = content_data.get("intro") or []
    sections = normalize_sections(content_data["sections"])
    faqs = content_data["faqs"]
    flatlay_h2 = cfg["flatlay_insert_h2"]
    lifestyle_h2 = cfg["lifestyle_insert_h2"]
    carousel_id = cfg["carousel_id"]
    occasion_year = cfg["occasion_year"]
    gift_blurb = cfg["gift_blurb"]
    more_reads = cfg["more_reads_html"]
    conclusion = cfg["conclusion_html"]
    alt_prefix = cfg["carousel_alt_prefix"]
    keywords = cfg["schema_keywords"]
    faq_h2 = cfg.get("faq_h2") or f"Frequently Asked Questions about {focus_kw.title()}"
    output_prefix = cfg["output_prefix"]
    min_lines = cfg.get("min_lines", 100)
    categories = cfg.get("categories") or [CAT_FESTIVE, CAT_QUOTES]
    prompts_path = ROOT / cfg.get("type3_prompts_json", f"output/{output_prefix}_type3_prompts.json")
    prompts_manifest = json.loads(prompts_path.read_text(encoding="utf-8")) if prompts_path.exists() else {}
    tracked_post = None
    if not LOCAL_ONLY:
        tracked_post_id = prompts_manifest.get("wp_post_id")
        if tracked_post_id:
            tracked_post = api("GET", f"posts/{tracked_post_id}?context=edit")
            if tracked_post.get("slug") != slug:
                raise SystemExit(
                    f"Tracked WordPress post {tracked_post_id} has slug {tracked_post.get('slug')!r}, "
                    f"expected {slug!r}; refusing to overwrite it."
                )
        else:
            existing_posts = api(
                "GET",
                f"posts?slug={quote(slug)}&context=edit&status=any&per_page=10",
            )
            if existing_posts:
                existing = existing_posts[0]
                raise SystemExit(
                    f"Existing WordPress slug detected: post {existing['id']} {existing.get('link')}. "
                    "Record and verify that post ID in the Type 3 manifest before resuming; "
                    "a second post will not be created."
                )

    products = []
    for p in cfg["products"]:
        products.append(
            {
                "code": p["code"],
                "name": p["name"],
                "url": p["url"],
                "png": ROOT / p["png"],
            }
        )

    assert 150 <= len(meta_desc) <= 160, len(meta_desc)
    assert len(yoast_title) <= 60, len(yoast_title)

    assets = ROOT / f"output/{output_prefix}_assets"
    assets.mkdir(parents=True, exist_ok=True)
    product_media = []
    product_media_path = ROOT / f"output/{output_prefix}_product_media.json"
    preuploaded_path = cfg.get("preuploaded_product_media_json")
    if preuploaded_path:
        product_media = json.loads((ROOT / preuploaded_path).read_text(encoding="utf-8"))
        print("using preuploaded product media", preuploaded_path)
    elif product_media_path.exists():
        saved_media = json.loads(product_media_path.read_text(encoding="utf-8"))
        expected_codes = [product["code"] for product in products]
        saved_codes = [item.get("code") for item in saved_media]
        if (
            saved_codes != expected_codes[: len(saved_codes)]
            or len(saved_codes) > len(expected_codes)
            or (not LOCAL_ONLY and any(not item.get("id") for item in saved_media))
        ):
            raise SystemExit(
                f"Existing product media checkpoint does not match the requested products: {product_media_path}"
            )
        product_media = saved_media
        print(
            "reusing product media checkpoint",
            product_media_path.relative_to(ROOT),
            f"({len(product_media)}/{len(products)})",
        )
    if not preuploaded_path:
        for product in products[len(product_media) :]:
            if not product["png"].exists():
                raise SystemExit(f"Missing approved Type 2 image: {product['png']}")
            filename = re.sub(r"[^A-Za-z0-9]+", "-", product["name"]).strip("-").lower() + "-carousel.webp"
            webp = assets / filename
            to_carousel_webp(product["png"], webp)
            alt = f"{alt_prefix}: {product['name']}"
            media_title = f"{product['name']} carousel, {occasion_year}"
            if LOCAL_ONLY:
                media = {"id": None, "source_url": str(webp.relative_to(ROOT))}
            else:
                media = upload_media(webp, alt, media_title)
            product_media.append(
                {
                    "code": product["code"],
                    "name": product["name"],
                    "url": product["url"],
                    "id": media["id"],
                    "src": media["source_url"],
                    "alt": alt,
                    "title": media_title,
                }
            )
            product_media_path.write_text(
                json.dumps(product_media, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            print("prepared product", product["code"], media.get("id"), media["source_url"])

    carousel = build_carousel(
        product_media,
        carousel_id,
        cfg.get("carousel_aria_label") or f"BlueStone {occasion_year} gift ideas",
    )
    faq_html, faq_schema = build_faqs(faqs, faq_h2)

    # Insert gift carousel after first ~3 sections, before flatlay/lifestyle targets
    section_blocks = []
    for sec in sections:
        ordered = "caption" not in sec["key"].lower() and "status" not in sec["key"].lower() and "short" not in sec["h2"].lower()
        # captions/status often unordered
        use_ol = not any(x in sec["h2"].lower() for x in ("caption", "status", "one liner", "one-line"))
        section_blocks.append((sec["h2"], sec["lines"], use_ol))

    # Find insert indices by H2 match
    flatlay_idx = next(i for i, (h, _, _) in enumerate(section_blocks) if h == flatlay_h2)
    lifestyle_idx = next(i for i, (h, _, _) in enumerate(section_blocks) if h == lifestyle_h2)
    gift_before = min(flatlay_idx, 3)  # gift block before flatlay section

    parts = [
        '<!-- wp:html -->\n<style>\n.bs-eeat{margin:0 auto 1.25rem;max-width:720px;text-align:center;font-size:.95rem;color:#444;line-height:1.5}\n.bs-eeat strong{color:#111}\n.entry-content img,.wp-block-image img{max-width:100%;height:auto}\n</style>\n<!-- /wp:html -->',
        '<!-- wp:paragraph {"align":"center"} -->\n<p class="has-text-align-center bs-eeat">By <strong>Vikas</strong>, BlueStone Editorial</p>\n<!-- /wp:paragraph -->',
    ]
    for i, intro in enumerate(intros):
        if i == 0 and focus_kw.lower() not in intro.lower():
            parts.append(para(f"Looking for <strong>{escape(focus_kw)}</strong>? {escape(intro)}"))
        else:
            parts.append(para(escape(intro)))

    content_mode = (cfg.get("content_mode") or "listicle").lower()
    article_engine = (cfg.get("article_engine") or cfg.get("theme") or content_mode).lower().replace(" ", "_")

    def education_section_html(heading: str, lines: list[str], use_ol: bool) -> list[str]:
        """Turn bullet source lines into paragraphs + a short takeaway list."""
        blocks = []
        lead = cfg.get("section_leads", {}).get(heading)
        if lead:
            blocks.append(para(lead))
        section_html = cfg.get("section_html", {}).get(heading)
        if section_html:
            blocks.append(section_html)
        # First 2 to 3 lines become prose paragraphs; remaining become compact takeaways (max 6).
        prose_n = min(3, max(1, len(lines) // 3)) if len(lines) > 4 else min(2, len(lines))
        prose_lines = lines[:prose_n]
        takeaway_lines = lines[prose_n : prose_n + 6]
        for line in prose_lines:
            text = line.strip()
            # Soft-strip leading labels like "Fact:" if present
            text = re.sub(r"^(Fact|Note|Point|Tip|Line)\s*:\s*", "", text, flags=re.I)
            if text and not text.endswith((".", "!", "?")):
                text = text + "."
            blocks.append(para(escape(text)))
        if takeaway_lines:
            blocks.append(para("Keep these quick takeaways handy:"))
            blocks.append(list_block(takeaway_lines, ordered=use_ol))
        elif len(lines) <= prose_n:
            pass
        return blocks

    def default_listicle_lead(heading: str) -> str | None:
        """Only use copy-ready phrasing for true copy/paste intent.

        Gift guides and buying/education articles can also be rendered as
        listicles, but they should not say "copy ready lines" unless the
        article is actually a quotes/captions/messages piece.
        """
        text = f"{focus_kw} {heading}".lower()
        copy_terms = (
            "wish",
            "wishes",
            "message",
            "messages",
            "quote",
            "quotes",
            "caption",
            "captions",
            "shayari",
            "status",
            "comment",
            "comments",
            "one liner",
            "one-liner",
        )
        shopping_terms = (
            "gift",
            "gifts",
            "jewellery",
            "jewelry",
            "buy",
            "buying",
            "guide",
            "check",
            "purity",
            "choose",
        )
        if any(term in text for term in copy_terms) and not any(term in text for term in shopping_terms):
            return f"Copy-ready lines for {escape(focus_kw)}."
        return None

    for i, (h, lines, use_ol) in enumerate(section_blocks):
        if i == gift_before:
            parts.append(h2(cfg["gift_h2"]))
            parts.append(para(gift_blurb))
            parts.append(carousel)
            parts.extend(build_product_recommendations(cfg))
        parts.append(h2(h))
        if content_mode == "education":
            parts.extend(education_section_html(h, lines, use_ol))
        else:
            lead = cfg.get("section_leads", {}).get(h) or default_listicle_lead(h)
            if lead:
                parts.append(para(lead))
            parts.append(list_block(lines, ordered=use_ol))

    tail_defaults = {
        "gift_guide": (
            "How to Choose the Right Gift",
            f"Start with the recipient's style, then choose a piece they can wear beyond {escape(occasion_year)}. If sizing is uncertain, prefer earrings, pendants, or bracelets before fitted rings and bangles.",
        ),
        "gift_guides": (
            "How to Choose the Right Gift",
            f"Start with the recipient's style, then choose a piece they can wear beyond {escape(occasion_year)}. If sizing is uncertain, prefer earrings, pendants, or bracelets before fitted rings and bangles.",
        ),
        "buying_guide": (
            "How to Use This Guide Before Buying",
            "Use the checklist first, compare the jewellery details carefully, and ask for professional confirmation when purity, hallmarking, tax, or sizing affects the purchase decision.",
        ),
        "how-to_/_education": (
            "How to Use This Guide Before Buying",
            "Use the checklist first, compare the jewellery details carefully, and ask for professional confirmation when purity, hallmarking, tax, or sizing affects the purchase decision.",
        ),
        "education": (
            "How to Use This Guide Before Buying",
            "Use the checklist first, compare the jewellery details carefully, and ask for professional confirmation when purity, hallmarking, tax, or sizing affects the purchase decision.",
        ),
        "design_listicle": (
            "How to Choose the Right Design",
            "Match the design to the wearer, outfit, comfort level, and occasion. A good jewellery design should look beautiful in photos and still feel wearable in real life.",
        ),
        "design_listicles": (
            "How to Choose the Right Design",
            "Match the design to the wearer, outfit, comfort level, and occasion. A good jewellery design should look beautiful in photos and still feel wearable in real life.",
        ),
        "jewellery_design": (
            "How to Choose the Right Design",
            "Match the design to the wearer, outfit, comfort level, and occasion. A good jewellery design should look beautiful in photos and still feel wearable in real life.",
        ),
    }
    default_tail_h2, default_tail_html = tail_defaults.get(
        article_engine,
        (
            "How to Pick the Right Message",
            f"Choose a short line for chats, a longer note for cards, and a caption for photos. Personalize with a name, keep the tone honest, and use {escape(occasion_year)} wording before you send.",
        ),
    )
    parts.append(h2(cfg.get("tail_h2") or cfg.get("how_to_h2") or default_tail_h2))
    parts.append(para(cfg.get("how_to_html") or cfg.get("tail_html") or default_tail_html))
    parts.append(h2(cfg.get("more_reads_h2") or "More Festive and Occasion Reads"))
    parts.append(para(more_reads))
    parts.append(faq_html)
    parts.append(h2("Conclusion"))
    parts.append(para(conclusion))

    content = "\n\n".join(parts)
    images = [p["src"] for p in product_media]
    faq_page = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_schema}
    blog_posting = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": meta_desc,
        "datePublished": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "dateModified": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "author": {"@type": "Person", "name": "Vikas"},
        "publisher": {"@type": "Organization", "name": "BlueStone", "url": "https://www.bluestone.com/"},
        "image": images,
        "mainEntityOfPage": {"@type": "WebPage", "@id": live_url},
        "keywords": keywords,
    }
    content += (
        "\n\n<!-- wp:html -->\n"
        f'<script type="application/ld+json" id="bs-faq-schema">{json.dumps(faq_page, ensure_ascii=False)}</script>\n'
        f'<script type="application/ld+json" id="bs-blogposting-schema">{json.dumps(blog_posting, ensure_ascii=False)}</script>\n'
        "<!-- /wp:html -->\n"
    )

    article_content = content.split('<script type="application/ld+json" id="bs-faq-schema">', 1)[0]
    visible = re.sub(r"<(style|script)\b[^>]*>[\s\S]*?</\1>", " ", article_content, flags=re.I)
    visible = re.sub(r"<[^>]+>", " ", visible)
    body_no_links = re.sub(r"<a\b[^>]*>[\s\S]*?</a>", " ", article_content, flags=re.I)
    body_no_links = re.sub(r"<(style|script)\b[^>]*>[\s\S]*?</\1>", " ", body_no_links, flags=re.I)
    body_no_links = re.sub(r"<[^>]+>", " ", body_no_links)
    total_lines = sum(len(s["lines"]) for s in sections)
    rules = {
        "no_em_dash": "\u2014" not in visible,
        "no_en_dash": "\u2013" not in visible,
        "no_spaced_hyphen": re.search(r"\s-\s", visible) is None,
        "no_prices": not re.search(r"(?:₹|\bRs\.?\s*\d|\bINR\s*\d)", visible, re.I),
        "carousel_mid_article": content.index(carousel_id) < content.index("Frequently Asked Questions"),
        "six_buy_links": content.count(">Buy now<") == 6,
        "faq_schema": '"@type": "FAQPage"' in content,
        "blog_schema": '"@type": "BlogPosting"' in content,
        "no_content_h1": "<h1" not in content.lower(),
        "primary_kw": focus_kw.lower() in visible.lower(),
        "no_old_years_body": not re.search(r"\b(2021|2022|2023|2024|2025)\b", body_no_links),
        "meta_title_len": len(yoast_title) <= 60,
        "meta_desc_len": 150 <= len(meta_desc) <= 160,
        "hundred_plus_lines": total_lines >= min_lines,
        "flatlay_h2_present": flatlay_h2 in visible,
        "lifestyle_h2_present": lifestyle_h2 in visible,
        "no_malformed_wp_comments": re.search(r"<!--\s*\/?[a-z0-9\:\-\_]+(?!-->)>", content) is None,
        "no_html_tables": "<table" not in content.lower(),
        "all_faqs_in_body": all(q in visible for q, _ in faqs),
        "no_duplicate_h2s": len(re.findall(r"<h2\b[^>]*>(.*?)</h2>", content, re.I)) == len(set(re.findall(r"<h2\b[^>]*>(.*?)</h2>", content, re.I))),
    }
    if "gift" in article_engine:
        rules["gift_recommendations_present"] = len(cfg.get("product_recommendations") or []) >= 5
    if "education" in article_engine or "buying" in article_engine:
        rules["no_message_tail_for_education"] = "How to Pick the Right Message" not in visible
    if "design" in article_engine:
        rules["no_message_tail_for_design"] = "How to Pick the Right Message" not in visible
    failed = [name for name, passed in rules.items() if not passed]
    if failed:
        raise SystemExit(f"Content validation failed: {failed}")

    (ROOT / f"output/{output_prefix}_article.html").write_text(content, encoding="utf-8")
    product_media_path.write_text(
        json.dumps(product_media, indent=2), encoding="utf-8"
    )
    # export insert H2s for patch scripts
    (ROOT / f"output/{output_prefix}_insert_h2s.json").write_text(
        json.dumps({"flatlay": flatlay_h2, "lifestyle": lifestyle_h2, "slug": slug, "title": title, "meta_desc": meta_desc, "focus_kw": focus_kw, "faqs": faqs}, indent=2),
        encoding="utf-8",
    )
    print("local_validation", rules)

    if LOCAL_ONLY:
        print("LOCAL_ONLY: skipped WordPress publish")
        return

    post_payload = {
        "title": title,
        "slug": slug,
        "status": "publish",
        "author": 270271337,
        "categories": categories,
        "content": content,
        "excerpt": meta_desc,
        "meta": {
            "_yoast_wpseo_focuskw": focus_kw,
            "_yoast_wpseo_title": yoast_title,
            "_yoast_wpseo_metadesc": meta_desc,
        },
    }
    if tracked_post:
        post = api("POST", f"posts/{tracked_post['id']}", post_payload)
        print("updated existing tracked post", post["id"], post["link"])
    else:
        post = api("POST", "posts", post_payload)
        print("published new post", post["id"], post["link"])

    if prompts_path.exists():
        manifest = json.loads(prompts_path.read_text(encoding="utf-8"))
        manifest["wp_post_id"] = post["id"]
        prompts_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    else:
        prompts_path.write_text(
            json.dumps({"wp_post_id": post["id"], "slug": slug, "output_prefix": output_prefix}, indent=2) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
