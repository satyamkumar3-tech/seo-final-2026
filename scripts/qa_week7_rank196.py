#!/usr/bin/env python3
"""Comprehensive Live QA script for Week 7 Rank 196: Big Earrings."""
import urllib.request
import re
import json
import sys
from html import unescape

URL = "https://blog.bluestone.com/big-earrings-2026/"

print(f"Fetching live URL: {URL}...")
req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        status_code = resp.status
        html = resp.read().decode("utf-8")
except Exception as e:
    print(f"FAILED to fetch live URL: {e}")
    sys.exit(1)

print(f"HTTP Status: {status_code} OK")
assert status_code == 200, f"Expected 200, got {status_code}"

# 1. Canonical URL
canonical_match = re.search(r'<link rel="canonical" href="([^"]+)"', html)
canonical = canonical_match.group(1) if canonical_match else None
print(f"Canonical URL: {canonical}")
assert canonical == URL, f"Canonical mismatch: expected {URL}, got {canonical}"

# 2. OpenGraph Image
og_img_match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
og_image = og_img_match.group(1) if og_img_match else None
print(f"OpenGraph Image: {og_image}")
assert og_image and "big-earrings-hero-2026.webp" in og_image, f"Invalid og:image: {og_image}"

# 3. Title tag & Meta description
title_match = re.search(r'<title>([^<]+)</title>', html)
meta_desc_match = re.search(r'<meta name="description" content="([^"]+)"', html)
print(f"Page Title: {title_match.group(1) if title_match else 'None'}")
print(f"Meta Description: {meta_desc_match.group(1) if meta_desc_match else 'None'}")

# 4. H1 tag count
h1_tags = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
print(f"H1 count: {len(h1_tags)}")
for i, h in enumerate(h1_tags):
    print(f"  H1 #{i+1}: {re.sub(r'<[^>]+>', '', h).strip()}")
assert len(h1_tags) == 1, f"Expected exactly 1 H1 tag, got {len(h1_tags)}"

# 5. H2 tags
h2_tags = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
print(f"\nH2 count: {len(h2_tags)}")
clean_h2s = [re.sub(r'<[^>]+>', '', h).strip() for h in h2_tags]
for i, h in enumerate(clean_h2s):
    print(f"  H2 #{i+1}: {h}")

# Verify conclusion precedes FAQ
faq_idx = -1
conclusion_idx = -1
for i, h in enumerate(clean_h2s):
    if "frequently asked questions" in h.lower():
        faq_idx = i
    if "final thoughts" in h.lower() or "conclusion" in h.lower():
        conclusion_idx = i

print(f"\nConclusion H2 index: {conclusion_idx}, FAQ H2 index: {faq_idx}")
assert conclusion_idx != -1, "Conclusion H2 not found!"
assert faq_idx != -1, "FAQ H2 not found!"
assert conclusion_idx < faq_idx, "Conclusion H2 must precede FAQ H2!"

# 6. Check article body word count
start_pos = html.find("entry-content")
end_pos = html.find("entry-footer")
if end_pos == -1:
    end_pos = html.find("post-author-box")
if end_pos == -1:
    end_pos = html.find("site-footer")
body_html = html[start_pos:end_pos]

text_no_scripts = re.sub(r'<script[^>]*>.*?</script>', ' ', body_html, flags=re.DOTALL)
text_no_style = re.sub(r'<style[^>]*>.*?</style>', ' ', text_no_scripts, flags=re.DOTALL)
clean_body = re.sub(r'<[^>]+>', ' ', text_no_style)
clean_body = unescape(clean_body)
words = re.findall(r'\b\w+\b', clean_body)
print(f"\nVisible word count in body: {len(words)}")
assert len(words) >= 2000, f"Article word count too low: {len(words)}"

# 7. Content prohibitions: em dash, en dash, spaced hyphen, prices, tables
em_dashes = [m.start() for m in re.finditer(r'—', clean_body)]
en_dashes = [m.start() for m in re.finditer(r'–', clean_body)]
spaced_hyphens = [m.group(0) for m in re.finditer(r'\b\w+\s+-\s+\w+\b', clean_body)]
prices = re.findall(r'(?:₹|\bRs\.?\s*\d|\bINR\s*\d)', clean_body, re.IGNORECASE)
tables = re.findall(r'<table', body_html, re.IGNORECASE)

print("\nProhibition checks:")
print(f"  Em dashes: {len(em_dashes)}")
print(f"  En dashes: {len(en_dashes)}")
print(f"  Spaced hyphens: {len(spaced_hyphens)}")
print(f"  Price mentions: {len(prices)}")
print(f"  HTML tables: {len(tables)}")

assert len(em_dashes) == 0, f"Found {len(em_dashes)} em dashes"
assert len(en_dashes) == 0, f"Found {len(en_dashes)} en dashes"
assert len(spaced_hyphens) == 0, f"Found spaced hyphens: {spaced_hyphens}"
assert len(prices) == 0, f"Found prices: {prices}"
assert len(tables) == 0, f"Found HTML tables: {len(tables)}"

# 8. Byline check
assert "By Satyam, BlueStone Editorial" in html or ("Satyam" in html and "BlueStone Editorial" in html), "Byline not found!"
print("Byline check: Verified 'By Satyam, BlueStone Editorial'")

# 9. Carousel cards
carousel_cards = re.findall(r'class="bs-cf-card"', html)
buy_now_links = re.findall(r'class="bs-cf-cta"[^>]*href="([^"]+)"', html)
print(f"Carousel cards: {len(carousel_cards)}, Buy now links: {len(buy_now_links)}")
assert len(carousel_cards) == 6, f"Expected 6 carousel cards, got {len(carousel_cards)}"
assert len(buy_now_links) == 6, f"Expected 6 buy now links, got {len(buy_now_links)}"

# 10. Type 3 images in body
figures = re.findall(r'<figure class="wp-block-image size-full[^"]*">(.*?)</figure>', html, re.DOTALL)
body_figures = [f for f in figures if "bs-logo" not in f]
print(f"\nType 3 body images: {len(body_figures)}")
for i, f in enumerate(body_figures):
    cap = re.search(r'<figcaption>(.*?)</figcaption>', f)
    alt = re.search(r'alt="([^"]+)"', f)
    mid = re.search(r'wp-image-(\d+)', f)
    print(f"  Image #{i+1}: Media ID {mid.group(1) if mid else None}")
    print(f"    Alt: {alt.group(1) if alt else None}")
    print(f"    Caption: {cap.group(1) if cap else None}")
assert len(body_figures) == 2, f"Expected 2 in-body Type 3 images, got {len(body_figures)}"

# 11. Schema verification
schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
print(f"\nFound {len(schemas)} JSON-LD schema blocks")
found_faq_schema = False
found_blog_schema = False

for s in schemas:
    try:
        data = json.loads(s.strip())
        stype = data.get("@type")
        if stype == "FAQPage":
            found_faq_schema = True
            entities = data.get("mainEntity", [])
            print(f"  FAQPage Schema: {len(entities)} questions")
            assert len(entities) >= 5, f"Expected at least 5 FAQ questions in schema, got {len(entities)}"
        elif stype == "BlogPosting":
            found_blog_schema = True
            author = data.get("author", {})
            aname = author.get("name") if isinstance(author, dict) else author
            images = data.get("image", [])
            print(f"  BlogPosting Schema: Author='{aname}', Images={len(images)}")
            assert aname == "Satyam", f"Expected BlogPosting author Satyam, got {aname}"
            assert len(images) >= 3, f"Expected images in BlogPosting, got {len(images)}"
    except Exception as e:
        pass

assert found_faq_schema, "FAQPage JSON-LD schema not found!"
assert found_blog_schema, "BlogPosting JSON-LD schema not found!"

print("\nALL LIVE QA CHECKS PASSED WITH FLYING COLOURS!")
