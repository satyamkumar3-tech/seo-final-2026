#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive Live QA audit script for Week 9 Rank 52 (stone-stud-earrings-2026, Post 40055)."""

import urllib.request, json, re, sys
from html import unescape

URL = "https://blog.bluestone.com/stone-stud-earrings-2026/"
POST_ID = 40055

print(f"Fetching live page: {URL}...")
req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
with urllib.request.urlopen(req, timeout=30) as resp:
    html = resp.read().decode('utf-8')
    status_code = resp.status

print(f"HTTP Status: {status_code}")

checks = {}

# 1. Title & H1
h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.S)
clean_h1 = [re.sub(r'<[^>]+>', '', h).strip() for h in h1_matches]
checks["single_h1"] = len(h1_matches) == 1
checks["h1_text"] = clean_h1[0] if clean_h1 else ""
checks["primary_in_h1"] = "stone stud earrings" in checks["h1_text"].lower()

# 2. Carousel Gate
checks["has_bs_cf"] = 'class="bs-cf"' in html or "class='bs-cf'" in html or 'bs-cf' in html
checks["has_bs_cf_stage"] = 'bs-cf-stage' in html
checks["has_bs_cf_card"] = 'bs-cf-card' in html
checks["has_bs_cf_dots"] = 'bs-cf-dots' in html
checks["no_bs_cf_wrap"] = 'bs-cf-wrap' not in html

# Carousel card images preflight
carousel_images = re.findall(r'<div class="bs-cf-card[^"]*"[^>]*>.*?<img[^>]+src="([^"]+)".*?</div>', html, re.S)
checks["carousel_card_count"] = len(carousel_images)
carousel_200 = True
for img_url in carousel_images:
    head_req = urllib.request.Request(img_url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(head_req, timeout=10) as r:
            if r.status != 200:
                carousel_200 = False
                print(f"Broken carousel image: {img_url} ({r.status})")
    except Exception as e:
        carousel_200 = False
        print(f"Carousel image error: {img_url} ({e})")

checks["carousel_all_images_200"] = carousel_200 and len(carousel_images) == 6

# Buy now CTA links
buy_now_links = re.findall(r'href="([^"]+)"[^>]*>Buy now</a>', html)
checks["buy_now_count"] = len(buy_now_links)

# 3. Type 3 Images
checks["featured_media_present"] = 'wp-image-40056' in html or 'stone-stud-earrings-2026-hero.webp' in html

# Extract entry-content body
body_match = re.search(r'<div class=\"[^\"]*entry-content[^\"]*\"[^>]*>(.*?)</div>\s*<!-- \.entry-content', html, re.S)
if not body_match:
    body_match = re.search(r'<div class=\"[^\"]*entry-content[^\"]*\"[^>]*>(.*)', html, re.S)
body_html = body_match.group(1) if body_match else ""

checks["hero_not_in_body"] = 'stone-stud-earrings-2026-hero.webp' not in body_html
checks["flatlay_in_body"] = 'stone-stud-earrings-2026-flatlay.webp' in body_html
checks["lifestyle_in_body"] = 'stone-stud-earrings-2026-lifestyle.webp' in body_html

# Check product links on in-body Type 3 images
flatlay_pdp_linked = bool(re.search(r'<a href="https://www\.bluestone\.com/earrings/the-vicky-hoop-earrings~35071\.html"[^>]*>\s*<img[^>]+stone-stud-earrings-2026-flatlay\.webp', html))
lifestyle_pdp_linked = bool(re.search(r'<a href="https://www\.bluestone\.com/earrings/the-ursa-hoop-earrings~35069\.html"[^>]*>\s*<img[^>]+stone-stud-earrings-2026-lifestyle\.webp', html))
checks["flatlay_image_pdp_linked"] = flatlay_pdp_linked
checks["lifestyle_image_pdp_linked"] = lifestyle_pdp_linked

# 4. Word count & Section ordering
visible_text = re.sub(r'<(script|style)\b[^>]*>[\s\S]*?</\1>', ' ', html, flags=re.I)
visible_text = re.sub(r'<[^>]+>', ' ', visible_text)
words = [w for w in visible_text.split() if w.isalnum() or '-' in w]
checks["visible_word_count"] = len(words)

# Section ordering
final_pos = html.find("Final Thoughts: Investing in Timeless Stone Stud Earrings")
related_pos = html.find("More Jewellery &amp; Buying Guides")
if related_pos == -1:
    related_pos = html.find("More Jewellery & Buying Guides")
faq_pos = html.find("Frequently Asked Questions About Stone Stud Earrings")

checks["section_ordering_correct"] = (final_pos != -1 and related_pos != -1 and faq_pos != -1 and final_pos < related_pos < faq_pos)

# 5. Visible FAQ questions count
faq_h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', html)
faq_questions = [h for h in faq_h3s if any(q in h.lower() for q in ['stone stud', 'gold purity', 'screw back', 'billing', 'clean', 'wear'])]
checks["faq_question_count"] = len(faq_questions)

# 6. Author and Byline
checks["byline_present"] = "By Satyam, BlueStone Editorial" in html

# 7. Metadata & Schema
checks["canonical_url"] = re.search(r'<link rel=\"canonical\" href=\"([^\"]+)\"', html).group(1) if re.search(r'<link rel=\"canonical\" href=\"([^\"]+)\"', html) else ""
checks["has_faq_schema"] = '"@type": "FAQPage"' in html or '"@type":"FAQPage"' in html
checks["has_blog_schema"] = '"@type": "BlogPosting"' in html or '"@type":"BlogPosting"' in html

# 8. Dash and Price restrictions in article body
body_match = re.search(r'<div class=\"[^\"]*entry-content[^\"]*\"[^>]*>(.*?)</div>', html, re.S)
body_html = body_match.group(1) if body_match else html

# Strip script and style from body
clean_body = re.sub(r'<(script|style)\b[^>]*>[\s\S]*?</\1>', ' ', body_html, flags=re.I)
clean_body_text = re.sub(r'<[^>]+>', ' ', clean_body)

checks["no_em_dash"] = "\u2014" not in clean_body_text
checks["no_en_dash"] = "\u2013" not in clean_body_text
checks["no_spaced_hyphen"] = re.search(r'\s-\s', clean_body_text) is None
checks["no_prices"] = re.search(r'(?:₹|\bRs\.?\s*\d|\bINR\s*\d)', clean_body_text, re.I) is None
checks["no_html_tables"] = "<table" not in clean_body.lower()

# Print full QA report
print("\n" + "="*50)
print("LIVE QA RESULTS SUMMARY:")
print("="*50)
for k, v in checks.items():
    status = "PASS" if v is True or (isinstance(v, int) and v > 0) or (isinstance(v, str) and v) else "FAIL"
    print(f"[{status}] {k}: {v}")
print("="*50)

# Check for failures
failed = [k for k, v in checks.items() if v is False or v == ""]
if failed:
    print(f"FAILED CHECKS: {failed}")
    sys.exit(1)
else:
    print("ALL LIVE QA CHECKS PASSED PERFECTLY!")
