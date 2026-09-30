#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive Live QA script for Week 9 Rank 89 (daily wear gold earrings for women)."""
import urllib.request
import urllib.error
import json
import re
import sys
import time

URL = "https://blog.bluestone.com/daily-wear-gold-earrings-for-women-2026/"
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
assert "daily-wear-gold-earrings-for-women-hero-2026" in og_image, f"Unexpected og:image: {og_image}"

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

# Load carousel items from JSON to check URLs
with open("output/week9_rank89_carousel_media.json", encoding="utf-8") as f:
    carousel_items = json.load(f)

print(f"Checking {len(carousel_items)} carousel image URLs:")
for item in carousel_items:
    c_url = item["image_url"]
    c_status, _ = fetch_with_retry(c_url, method="HEAD")
    print(f"  {item['name']} ({c_url}) -> HTTP {c_status}")
    assert c_status == 200

# 5. In-body Type 3 Images (Flatlay and Lifestyle)
flatlay_imgs = re.findall(r'<img[^>]+src=["\']([^"\']*daily-wear-gold-earrings-for-women-flatlay-2026\.webp[^"\']*)["\']', html)
lifestyle_imgs = re.findall(r'<img[^>]+src=["\']([^"\']*daily-wear-gold-earrings-for-women-lifestyle-2026\.webp[^"\']*)["\']', html)
print(f"Flatlay in DOM: {len(flatlay_imgs)}, Lifestyle in DOM: {len(lifestyle_imgs)}")
assert len(flatlay_imgs) == 1, "Expected exactly 1 flatlay image in body!"
assert len(lifestyle_imgs) == 1, "Expected exactly 1 lifestyle image in body!"

# 6. Section Ordering: Conclusion BEFORE Related Guides, and Related Guides BEFORE FAQs
conclusion_pos = html.find("Final Thoughts: Investing in Timeless Daily Comfort")
related_pos = html.find("More Jewellery")
faq_pos = html.find("Frequently Asked Questions About Daily Wear Gold Earrings for Women")
print(f"Section order positions: Conclusion={conclusion_pos}, Related={related_pos}, FAQs={faq_pos}")
assert conclusion_pos != -1 and related_pos != -1 and faq_pos != -1, "Missing section headings!"
assert conclusion_pos < related_pos < faq_pos, "Invalid section ordering! Expected Conclusion -> Related -> FAQs"

# 7. FAQs rendered in live DOM
faq_qs = [
    "What type of earrings are best for daily use?",
    "Can I wear gold earrings daily without taking them off?",
    "Is 18K or 22K gold better for daily wear earrings?",
    "What is the ideal weight for light weight daily wear gold earrings?",
    "Which earring back is safest for everyday wear?",
    "How do I clean daily wear gold earrings at home?"
]
for q in faq_qs:
    assert q in html, f"Missing FAQ question in HTML: {q}"
print("All 6 FAQ questions confirmed in live DOM!")

# 8. Schema verification
m_schemas = re.findall(r'<script\s+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(m_schemas)} JSON-LD schema blocks.")
has_faq = False
has_blog = False
for s in m_schemas:
    try:
        parsed = json.loads(s.strip())
        t = parsed.get("@type", "")
        if t == "FAQPage" or any(x.get("@type") == "FAQPage" for x in parsed.get("@graph", [])):
            has_faq = True
            print("Successfully verified FAQPage JSON-LD schema!")
        if t == "BlogPosting" or any(x.get("@type") == "BlogPosting" for x in parsed.get("@graph", [])):
            has_blog = True
            print("Successfully verified BlogPosting JSON-LD schema!")
    except Exception as e:
        print(f"JSON parse error: {e}")
assert has_faq and has_blog, f"Schema verification failed: has_faq={has_faq}, has_blog={has_blog}"

# 9. Clean prose checks (no em dash, no en dash, no spaced hyphen, no price symbol in article text)
m_content = re.search(r'<div class=["\'][^"\']*entry-content[^"\']*["\'][^>]*>(.*?)</div>\s*<!-- \.entry-content -->', html, re.DOTALL)
if not m_content:
    m_content = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
article_body = m_content.group(1) if m_content else html

# Remove style and script blocks before text checks
clean_body = re.sub(r'<(style|script)[^>]*>.*?</\1>', '', article_body, flags=re.DOTALL)
clean_body_text = re.sub(r'<[^>]+>', ' ', clean_body)

# Word count
words = [w for w in clean_body_text.split() if len(w) > 1]
print(f"Visible Word Count: {len(words)}")
assert len(words) >= 2000, f"Word count too low: {len(words)}"

# Check dashes
assert "—" not in clean_body_text, "Em dash found in body text!"
assert "–" not in clean_body_text, "En dash found in body text!"
assert " - " not in clean_body_text, "Spaced hyphen found in body text!"

# Check prices
price_matches = re.findall(r'(?:₹|Rs\.?|INR)\s*\d+', clean_body_text)
print(f"Price mentions found: {price_matches}")
assert len(price_matches) == 0, f"Prohibited price mentions found: {price_matches}"

# 10. Internal Links check
links = re.findall(r'href=["\'](https://blog\.bluestone\.com/[^"\']+)["\']', clean_body)
print(f"Total internal blog links in body: {len(links)}")
for l in links:
    print(f"  Link: {l}")
assert len(links) >= 4, f"Expected at least 4 internal links, got {len(links)}"

print("\n==========================================")
print("ALL LIVE QA CHECKS PASSED PERFECTLY!")
print("==========================================")
