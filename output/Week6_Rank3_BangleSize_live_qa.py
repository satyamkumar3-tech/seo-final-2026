#!/usr/bin/env python3
import copy
import json
import re
from pathlib import Path

from lxml import html

live_path = Path("/tmp/week6-rank3-live.html")
post_path = Path("/tmp/week6-rank3-post.json")
raw = live_path.read_text(encoding="utf-8")
doc = html.fromstring(raw)
post = json.loads(post_path.read_text(encoding="utf-8"))

entries = doc.xpath(
    '//*[contains(concat(" ", normalize-space(@class), " "), " wp-block-post-content ")]'
)
if not entries:
    entries = doc.xpath(
        '//*[contains(concat(" ", normalize-space(@class), " "), " entry-content ")]'
    )
if not entries:
    raise SystemExit("Could not locate post content container")
entry = entries[0]
clean = copy.deepcopy(entry)
for node in clean.xpath(".//script|.//style"):
    parent = node.getparent()
    if parent is not None:
        parent.remove(node)
visible = " ".join(clean.text_content().split())

schemas = {}
for schema_id in ("bs-faq-schema", "bs-blogposting-schema"):
    nodes = entry.xpath(f'.//script[@id="{schema_id}"]')
    schemas[schema_id] = json.loads(nodes[0].text) if nodes else None

h1s = [" ".join(node.text_content().split()) for node in doc.xpath("//h1")]
h2s = [" ".join(node.text_content().split()) for node in entry.xpath(".//h2")]
images = [
    {"src": node.get("src") or "", "alt": node.get("alt") or "", "class": node.get("class") or ""}
    for node in entry.xpath(".//img")
]
captions = [
    " ".join(node.text_content().split())
    for node in entry.xpath(
        './/figure[contains(concat(" ", normalize-space(@class), " "), " wp-block-image ")]/figcaption'
    )
]
links = [node.get("href") or "" for node in entry.xpath(".//a")]
faq_schema = schemas["bs-faq-schema"] or {}
blog_schema = schemas["bs-blogposting-schema"] or {}
dom_nodes = list(doc.iter())
h1_nodes = doc.xpath("//h1")
hero_nodes = doc.xpath('//img[contains(@src,"bangle-size-hero-2026.webp")]')

results = {
    "http_content_bytes": len(raw),
    "status": post.get("status"),
    "post_id": post.get("id"),
    "slug": post.get("slug"),
    "author": post.get("author"),
    "categories": post.get("categories"),
    "featured_media": post.get("featured_media"),
    "h1_count": len(h1s),
    "h1": h1s,
    "h1_before_featured": bool(h1_nodes and hero_nodes and dom_nodes.index(h1_nodes[0]) < dom_nodes.index(hero_nodes[0])),
    "h2_count": len(h2s),
    "h2s": h2s,
    "visible_words": len(re.findall(r"[A-Za-z0-9%']+", visible)),
    "carousel_cards": len(
        entry.xpath(
            './/*[contains(concat(" ", normalize-space(@class), " "), " bs-cf-card ")]'
        )
    ),
    "buy_links": len(entry.xpath('.//a[normalize-space(text())="Buy now"]')),
    "carousel_before_faq": raw.find("bs-cf-banglesize") < raw.find("Frequently Asked Questions"),
    "body_image_ids": [
        css_class
        for image in images
        for css_class in image["class"].split()
        if css_class.startswith("wp-image-")
    ],
    "body_webp": all(image["src"].split("?")[0].endswith(".webp") for image in images),
    "body_alts": [image["alt"] for image in images],
    "figcaptions": captions,
    "faq_schema_count": len(faq_schema.get("mainEntity", [])),
    "blog_schema_images": len(blog_schema.get("image", [])),
    "blog_schema_url": blog_schema.get("mainEntityOfPage", {}).get("@id"),
    "internal_blog_links": len([url for url in links if url.startswith("https://blog.bluestone.com/")]),
    "factual_source_links": len([
        url for url in links
        if "climg6.bluestone.com" in url or "gjsci.org" in url
    ]),
    "product_links": len([url for url in links if url.startswith("https://www.bluestone.com/")]),
    "forbidden": {
        "em": visible.count("—"),
        "en": visible.count("–"),
        "spaced_hyphen": bool(re.search(r"\s-\s", visible)),
        "prices": bool(re.search(r"(?:₹|\bRs\.?\s*\d|\bINR\s*\d)", visible, re.I)),
        "old_years": bool(re.search(r"\b(2021|2022|2023|2024|2025)\b", visible)),
    },
    "canonical": (doc.xpath('//link[@rel="canonical"]/@href') or [None])[0],
    "meta_desc": (doc.xpath('//meta[@name="description"]/@content') or [None])[0],
}

expected_h2s = [
    "Bangle size chart in mm, cm and inches",
    "How to measure bangle size using a bangle you own",
    "How to measure your hand for bangle size at home",
    "Bangle designs to compare before choosing a size",
    "Closed, openable and adjustable bangle sizing explained",
    "How should a correctly sized bangle fit?",
    "Common bangle size mistakes and how to fix them",
    "Choosing a size for wide, oval and stackable bangles",
    "Bangle size buying checklist for online orders",
    "When to visit a BlueStone store for a fitting",
    "Fact sources for this bangle size guide",
    "How to use this bangle size guide before buying",
    "More bangle guides from BlueStone",
    "Frequently Asked Questions about Bangle Size",
    "Conclusion",
]
checks = {
    "published": results["status"] == "publish",
    "post_id": results["post_id"] == 34822,
    "author_vikas": results["author"] == 270271338,
    "categories": set(results["categories"] or []) == {554493412, 554493465},
    "featured_hero": results["featured_media"] == 34823,
    "one_h1": results["h1_count"] == 1,
    "h1_title": results["h1"] == ["Bangle Size Chart 2026: How to Measure the Right Fit"],
    "h1_above_featured": results["h1_before_featured"],
    "all_h2s": results["h2s"] == expected_h2s,
    "full_length": results["visible_words"] >= 2000,
    "carousel_six": results["carousel_cards"] == 6 and results["buy_links"] == 6,
    "carousel_mid_article": results["carousel_before_faq"],
    "two_body_type3": set(results["body_image_ids"]) == {"wp-image-34824", "wp-image-34825"},
    "featured_not_in_body": "wp-image-34823" not in results["body_image_ids"],
    "webp": results["body_webp"],
    "unique_alts": len(results["body_alts"]) == len(set(results["body_alts"])),
    "editorial_captions": results["figcaptions"] == [
        "The Skein Bangle being checked over the widest part of the hand for a comfortable fit",
        "The Channing Bangle beside simple tools used to confirm bangle size and inner diameter",
    ],
    "faq_schema": results["faq_schema_count"] == 8,
    "blog_schema": results["blog_schema_images"] == 9,
    "schema_url": results["blog_schema_url"] == "https://blog.bluestone.com/bangle-size-2026/",
    "internal_links": results["internal_blog_links"] >= 4,
    "factual_sources": results["factual_source_links"] >= 2,
    "product_links": results["product_links"] >= 6,
    "no_forbidden_text": results["forbidden"] == {
        "em": 0,
        "en": 0,
        "spaced_hyphen": False,
        "prices": False,
        "old_years": False,
    },
    "canonical": results["canonical"] == "https://blog.bluestone.com/bangle-size-2026/",
    "meta_desc": bool(results["meta_desc"]) and 150 <= len(results["meta_desc"]) <= 160,
}

print(json.dumps({"results": results, "checks": checks}, indent=2, ensure_ascii=False))
failed = [name for name, passed in checks.items() if not passed]
if failed:
    raise SystemExit(f"LIVE_QA_FAILED: {failed}")
print("LIVE_QA_PASSED")
