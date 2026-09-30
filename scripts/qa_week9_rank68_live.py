#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive Live QA script for Week 9 Rank 68: green-emerald-ring-2026."""
import os
import sys
import json
import re
import urllib.request
import html as html_lib

LIVE_URL = "https://blog.bluestone.com/green-emerald-ring-2026/"
POST_ID = 40223

def head_status(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status
    except Exception as e:
        print(f"HEAD check failed for {url}: {e}")
        return None

def run_qa():
    print(f"=== LIVE QA AUDIT FOR: {LIVE_URL} ===")
    
    import time
    cb_val = int(time.time())
    req = urllib.request.Request(f"{LIVE_URL}?cb={cb_val}", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        status_code = resp.status
        html = resp.read().decode('utf-8')

    print(f"1. HTTP Status Code: {status_code} (PASS)")
    assert status_code == 200, f"Expected 200, got {status_code}"

    # 2. Canonical URL
    canonical_match = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    canonical = canonical_match.group(1) if canonical_match else "NOT FOUND"
    print(f"2. Canonical URL: {canonical}")
    assert canonical == LIVE_URL, f"Canonical mismatch: {canonical} vs {LIVE_URL}"

    # 3. Title Tag
    title_match = re.search(r'<title>([^<]+)</title>', html)
    raw_title = title_match.group(1) if title_match else "NOT FOUND"
    title = html_lib.unescape(raw_title)
    print(f"3. Page Title: {title}")
    assert "green emerald ring" in title.lower(), "Primary KW missing in title"

    # 4. Meta Description
    meta_desc_match = re.search(r'<meta name="description" content="([^"]+)"', html)
    raw_meta_desc = meta_desc_match.group(1) if meta_desc_match else "NOT FOUND"
    meta_desc = html_lib.unescape(raw_meta_desc)
    print(f"4. Meta Description: {meta_desc} (Length: {len(meta_desc)})")
    assert "green emerald ring" in meta_desc.lower(), "Primary KW missing in meta description"

    # 5. Author verification
    author_match = "author-satyam" in html or "author-270271337" in html or "By Satyam, BlueStone Editorial" in html
    print(f"5. Author Verification: {'PASS (Satyam)' if author_match else 'FAIL'}")
    assert author_match, "Author Satyam not verified in HTML"

    # 6. H1 Count
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, flags=re.DOTALL)
    print(f"6. H1 Count: {len(h1s)}")
    assert len(h1s) == 1, f"Expected exactly 1 H1, found {len(h1s)}"

    # 7. Headings Hierarchy
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, flags=re.DOTALL)
    print(f"7. H2 Count: {len(h2s)}")
    assert len(h2s) >= 8, f"Expected >= 8 H2s, found {len(h2s)}"
    for idx, h in enumerate(h2s):
        print(f"   H2 [{idx+1}]: {h.strip()}")

    # Verify Section Ordering: Conclusion must precede Related Guides and FAQs
    h2_titles = [h.strip() for h in h2s]
    conclusion_idx = -1
    related_idx = -1
    faq_idx = -1
    for idx, h in enumerate(h2_titles):
        if "final thoughts" in h.lower() or "conclusion" in h.lower():
            conclusion_idx = idx
        elif "more jewellery" in h.lower() or "more gold" in h.lower() or "related guides" in h.lower():
            related_idx = idx
        elif "frequently asked questions" in h.lower():
            faq_idx = idx
    print(f"   Ordering: Conclusion={conclusion_idx}, Related={related_idx}, FAQ={faq_idx}")
    assert conclusion_idx != -1 and related_idx != -1 and faq_idx != -1, "Missing one of: Conclusion, Related Guides, FAQs"
    assert conclusion_idx < related_idx < faq_idx, f"Section ordering violated! Expected Conclusion < Related < FAQ, got {conclusion_idx} < {related_idx} < {faq_idx}"
    print("   Section ordering verified: Final Thoughts -> More Guides -> FAQs (PASS)")

    # Extract article prose
    body_match = re.search(r'(By Satyam, BlueStone Editorial.*?Frequently Asked Questions About Green Emerald Rings.*?</script>)', html, flags=re.DOTALL)
    article_body = body_match.group(1) if body_match else html
    prose_body = re.sub(r'<style>.*?</style>', '', article_body, flags=re.DOTALL)
    prose_body = re.sub(r'<script.*?</script>', '', prose_body, flags=re.DOTALL)

    # 8. Dash and Price Violations in Article Prose
    print("8. Checking for prohibited patterns in article prose...")
    assert "—" not in prose_body, "Found forbidden em dash (—) in article prose"
    assert "–" not in prose_body, "Found forbidden en dash (–) in article prose"
    assert " - " not in prose_body, "Found spaced hyphen in article prose"
    
    price_patterns = re.findall(r'(?:₹|Rs\.?|INR)\s*\d+', prose_body)
    print(f"   Price mentions found in prose: {len(price_patterns)}")
    assert len(price_patterns) == 0, f"Found price mentions: {price_patterns}"

    # 9. Carousel 3D Coverflow DOM verification
    print("9. Verifying 3D Coverflow Carousel DOM structure...")
    assert 'class="bs-cf"' in html or 'class="bs-cf ' in html, "Missing .bs-cf class"
    assert 'class="bs-cf-stage"' in html, "Missing .bs-cf-stage container"
    assert 'class="bs-cf-card' in html, "Missing .bs-cf-card elements"
    assert 'class="bs-cf-dots"' in html, "Missing .bs-cf-dots navigation"
    assert 'bs-cf-wrap' not in html, "Found deprecated unstyled bs-cf-wrap class!"
    assert 'bs-cf-track' not in html, "Found deprecated unstyled bs-cf-track class!"

    # 10. Carousel Images Pre-flight (HTTP 200)
    carousel_imgs = re.findall(r'<div class="bs-cf-card[^>]*>.*?<img[^>]+src="([^"]+)".*?</div>', html, flags=re.DOTALL)
    print(f"10. Carousel Cards Found: {len(carousel_imgs)}")
    assert len(carousel_imgs) == 6, f"Expected 6 carousel images, found {len(carousel_imgs)}"
    for idx, img_url in enumerate(carousel_imgs):
        clean_url = img_url.replace('&amp;', '&')
        status = head_status(clean_url)
        print(f"    Card [{idx+1}]: {clean_url} -> 200: {status}")
        assert status == 200, f"Carousel card {idx+1} image failed 200: {clean_url}"

    # 11. OpenGraph Image & In-body images
    print("11. Verifying OpenGraph and In-body Type 3 images...")
    og_img_match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    og_img = og_img_match.group(1) if og_img_match else "NOT FOUND"
    print(f"    og:image: {og_img}")
    assert "green-emerald-ring-hero-2026" in og_img, f"og:image not expected hero: {og_img}"
    assert head_status(og_img) == 200, f"og:image failed 200: {og_img}"

    # Check in-body images
    body_imgs = re.findall(r'<figure class="wp-block-image[^"]*size-full"><a href="([^"]+)"><img[^>]+src="([^"]+)"', html)
    print(f"    In-body linked images found: {len(body_imgs)}")
    assert len(body_imgs) >= 2, f"Expected >= 2 in-body linked images, found {len(body_imgs)}"
    for link, src in body_imgs:
        clean_src = src.replace('&amp;', '&')
        status = head_status(clean_src)
        print(f"    In-body img: {clean_src} -> 200: {status} (links to: {link})")
        assert status == 200, f"In-body image failed 200: {clean_src}"

    # 12. Internal Links & Related Guides
    print("12. Verifying internal links...")
    internal_links = re.findall(r'href="(https://blog\.bluestone\.com/[^"]+)"', html)
    print(f"    Total internal blog links: {len(internal_links)}")
    assert len(internal_links) >= 4, f"Expected >= 4 internal blog links, found {len(internal_links)}"

    # 13. Visible FAQs
    print("13. Verifying visible FAQ section...")
    faq_qs = re.findall(r'<h3[^>]*>([A-Z][^<]*?\?)</h3>', html)
    print(f"    Visible FAQ questions found: {len(faq_qs)}")
    assert len(faq_qs) >= 5, f"Expected >= 5 FAQ questions, found {len(faq_qs)}"
    for idx, q in enumerate(faq_qs):
        print(f"    FAQ [{idx+1}]: {q}")

    # 14. JSON-LD Schemas
    print("14. Verifying JSON-LD schemas...")
    schemas = re.findall(r'<script type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>', html, flags=re.DOTALL)
    print(f"    JSON-LD blocks found: {len(schemas)}")
    assert len(schemas) >= 1, "No JSON-LD schemas found"
    schema_text = "\n".join(schemas)
    assert '"@type": "FAQPage"' in schema_text or '"@type":"FAQPage"' in schema_text, "FAQPage schema missing"
    assert '"@type": "BlogPosting"' in schema_text or '"@type":"BlogPosting"' in schema_text, "BlogPosting schema missing"
    assert '"image": [' in schema_text or '"image":[' in schema_text, "BlogPosting schema images array missing"

    # 15. Word Count
    clean_text = re.sub(r'<[^>]+>', ' ', html)
    clean_text = re.sub(r'\{[^}]+\}', ' ', clean_text)
    words = clean_text.split()
    print(f"15. Total visible words (approx): {len(words)}")
    assert len(words) >= 1200, f"Word count too low: {len(words)}"

    print("\nALL LIVE QA CHECKS PASSED PERFECTLY!")

if __name__ == "__main__":
    run_qa()
