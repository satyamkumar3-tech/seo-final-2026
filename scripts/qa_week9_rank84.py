#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive Live QA script for Week 9 Rank 84 (baby wearing earrings)."""
import urllib.request
import urllib.error
import json
import re
import sys
import time

URL = "https://blog.bluestone.com/baby-wearing-earrings-2026/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_with_retry(url, method="GET", max_retries=5, delay=3):
    req = urllib.request.Request(url, headers=headers, method=method)
    for attempt in range(1, max_retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read() if method == "GET" else b""
                return resp.status, data.decode("utf-8", errors="ignore")
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < max_retries:
                print(f"HTTP 429 on attempt {attempt}, waiting {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                raise
        except Exception as e:
            if attempt < max_retries:
                time.sleep(delay)
                delay *= 2
            else:
                raise

print(f"Fetching live URL: {URL}...")
status_code, html = fetch_with_retry(URL)
print(f"HTTP Status: {status_code}")
assert status_code == 200, f"Expected 200, got {status_code}"

# 1. Canonical URL
m_canonical = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', html)
canonical = m_canonical.group(1) if m_canonical else "NOT FOUND"
print(f"Canonical URL: {canonical}")
assert canonical == URL, f"Expected {URL}, got {canonical}"

# 2. og:image
m_og_img = re.search(r'<meta\s+property=["\']og:image["\']\s+content=["\']([^"\']+)["\']', html)
og_image = m_og_img.group(1) if m_og_img else "NOT FOUND"
print(f"og:image: {og_image}")
assert "baby-wearing-earrings-hero-2026" in og_image, f"Unexpected og:image: {og_image}"

# Verify og:image returns 200
status, _ = fetch_with_retry(og_image, method="HEAD")
print(f"og:image HTTP Status: {status}")
assert status == 200

# 3. Headings
h1_tags = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.DOTALL)
print(f"H1 count: {len(h1_tags)}")
for h in h1_tags:
    print(f"  H1: {re.sub(r'<[^>]+>', '', h).strip()}")
assert len(h1_tags) == 1, f"Expected exactly 1 H1, got {len(h1_tags)}"

h2_tags = re.findall(r'<h2[^>]*class=["\'][^"\']*wp-block-heading[^"\']*["\'][^>]*>(.*?)</h2>', html, re.I | re.DOTALL)
if not h2_tags:
    h2_tags = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.I | re.DOTALL)
print(f"H2 count: {len(h2_tags)}")
for i, h in enumerate(h2_tags):
    clean_h = re.sub(r'<[^>]+>', '', h).strip()
    print(f"  H2 {i+1}: {clean_h}")

# Verify no duplicate H2s in body
body_h2s = [re.sub(r'<[^>]+>', '', h).strip() for h in h2_tags if "Discover more" not in h]
assert len(body_h2s) == len(set(body_h2s)), "Duplicate H2 headings detected!"

# 4. 3D Coverflow Carousel Gate
has_bs_cf = ".bs-cf" in html or 'class="bs-cf"' in html
has_stage = "bs-cf-stage" in html
has_cards = "bs-cf-card" in html
has_dots = "bs-cf-dots" in html
print(f"Carousel elements: bs-cf={has_bs_cf}, stage={has_stage}, cards={has_cards}, dots={has_dots}")
assert has_bs_cf and has_stage and has_cards and has_dots, "Carousel gate failed!"

# Verify all 6 carousel images return 200
carousel_imgs = re.findall(r'<img[^>]+src=["\']([^"\']*-carousel-2026\.webp[^"\']*)["\']', html)
print(f"Found {len(carousel_imgs)} carousel image URLs in DOM:")
assert len(carousel_imgs) == 6, f"Expected 6 carousel images, got {len(carousel_imgs)}"
for c_url in carousel_imgs:
    # clean entities for URL verification
    c_url_clean = c_url.replace("&#038;", "&")
    c_status, _ = fetch_with_retry(c_url_clean, method="HEAD")
    print(f"  {c_url_clean[:80]}... -> HTTP {c_status}")
    assert c_status == 200

# 5. In-body Type 3 Images (Flatlay and Lifestyle)
flatlay_imgs = re.findall(r'<img[^>]+src=["\']([^"\']*baby-wearing-earrings-flatlay-2026\.webp[^"\']*)["\']', html)
lifestyle_imgs = re.findall(r'<img[^>]+src=["\']([^"\']*baby-wearing-earrings-lifestyle-2026\.webp[^"\']*)["\']', html)
print(f"Flatlay in DOM: {len(flatlay_imgs)}, Lifestyle in DOM: {len(lifestyle_imgs)}")
assert len(flatlay_imgs) == 1, "Expected exactly 1 flatlay image in body!"
assert len(lifestyle_imgs) == 1, "Expected exactly 1 lifestyle image in body!"

# 6. Section Ordering: Conclusion BEFORE Related Guides, and Related Guides BEFORE FAQs
conclusion_pos = html.find("Final Thoughts")
related_pos = html.find("More Jewellery")
faq_pos = html.find("Frequently Asked Questions")
print(f"Section order positions: Conclusion={conclusion_pos}, Related={related_pos}, FAQs={faq_pos}")
assert conclusion_pos < related_pos < faq_pos, "Invalid section ordering! Expected Conclusion -> Related -> FAQs"

# 7. FAQs rendered in live DOM
faq_qs = [
    "What is the best age for a baby wearing earrings for the first time?",
    "Which gold purity is best and safest for infant earrings?",
    "Why are light weight earrings essential for babies?",
    "Are screw-back earrings safe for babies to sleep in?",
    "Can a baby wear small hoops or dangling earrings?",
    "How should I clean my baby's ears after getting them pierced?"
]
for q in faq_qs:
    assert q in html, f"Missing FAQ question in HTML: {q}"
print("All 6 FAQ questions confirmed in live DOM!")

# 8. Schema verification
m_schemas = re.findall(r'<script\s+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(m_schemas)} JSON-LD schema blocks.")
schema_valid = False
for s in m_schemas:
    if "BlogPosting" in s and "FAQPage" in s:
        try:
            parsed = json.loads(s.strip())
            print("Successfully parsed Article + FAQPage JSON-LD schema!")
            schema_valid = True
            break
        except Exception as e:
            print(f"JSON parse error: {e}")
assert schema_valid, "Could not find valid BlogPosting + FAQPage JSON-LD schema!"

# 9. Clean prose checks (no em dash, no en dash, no spaced hyphen, no price symbol in article text)
m_content = re.search(r'<div class=["\'][^"\']*entry-content[^"\']*["\'][^>]*>(.*?)</div>\s*<!-- \.entry-content -->', html, re.DOTALL)
if not m_content:
    m_content = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)

article_html = m_content.group(1) if m_content else html
article_text = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', article_html, flags=re.DOTALL)
clean_text = re.sub(r'<[^>]+>', ' ', article_text)

assert "—" not in clean_text, "Found em dash in article body!"
assert "–" not in clean_text, "Found en dash in article body!"
assert " - " not in clean_text, "Found spaced hyphen in article body!"
assert "₹" not in clean_text, "Found rupee symbol in article body!"

words = re.findall(r'\b[a-zA-Z0-9_-]+\b', clean_text)
print(f"Visible word count: {len(words)}")
assert len(words) > 1500, f"Expected >1500 words, got {len(words)}"

print("\nALL LIVE QA CHECKS PASSED PERFECTLY!")
