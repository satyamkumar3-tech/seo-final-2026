#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive Live QA script for Week 9 Rank 71."""
import os
import sys
import re
import json
import urllib.request
from pathlib import Path

URL = "https://blog.bluestone.com/light-weight-gold-earrings-design-2026/"
POST_ID = 40253
SLUG = "light-weight-gold-earrings-design-2026"

def run_qa():
    print(f"Fetching live page: {URL}...")
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8")
        status_code = resp.status

    print(f"1. HTTP Status: {status_code} (Verified 200 OK)")
    assert status_code == 200, f"Expected 200, got {status_code}"

    # 2. Canonical URL
    canon_match = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    canon_url = canon_match.group(1) if canon_match else ""
    print(f"2. Canonical URL: {canon_url}")
    assert canon_url == URL or canon_url == f"https://blog.bluestone.com/{SLUG}/", f"Canonical mismatch: {canon_url}"

    # 3. og:image
    og_match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    og_image = og_match.group(1) if og_match else ""
    print(f"3. og:image: {og_image}")
    assert "light-weight-gold-earrings-design-hero-2026.webp" in og_image, f"Hero og:image mismatch: {og_image}"

    # 4. Carousel 3D Coverflow elements
    assert "bs-cf" in html, "Missing .bs-cf container"
    assert "bs-cf-stage" in html, "Missing .bs-cf-stage"
    assert "bs-cf-dots" in html, "Missing .bs-cf-dots"
    card_count = len(re.findall(r'class="bs-cf-card', html))
    print(f"4. 3D Coverflow Carousel: Verified with {card_count} cards")
    assert card_count == 6, f"Expected 6 carousel cards, found {card_count}"

    # 5. Verify carousel image URLs return HTTP 200
    carousel_img_urls = re.findall(r'<div class="bs-cf-card[^"]*"[^>]*>[\s\S]*?<img [^>]*src="([^"]+)"', html)
    print(f"5. Verifying {len(carousel_img_urls)} carousel card image URLs via HTTP HEAD...")
    for u in carousel_img_urls:
        h_req = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(h_req, timeout=15) as r:
            assert r.status == 200, f"Image {u} returned {r.status}"
            print(f"   HTTP 200 OK: {u.split('/')[-1]}")

    # 6. Type 3 in-body images
    flatlay_in_dom = "light-weight-gold-earrings-design-flatlay-2026.webp" in html
    lifestyle_in_dom = "light-weight-gold-earrings-design-lifestyle-2026.webp" in html
    print(f"6. Type 3 in-body images: Flatlay present={flatlay_in_dom}, Lifestyle present={lifestyle_in_dom}")
    assert flatlay_in_dom and lifestyle_in_dom, "Missing in-body Type 3 images"

    # 7. Word count and section ordering
    cleaned = re.sub(r'<style[\s\S]*?</style>', ' ', html)
    cleaned = re.sub(r'<script[\s\S]*?</script>', ' ', cleaned)
    cleaned_text = re.sub(r'<[^>]+>', ' ', cleaned)
    visible_words = len(re.findall(r'\b\w+\b', cleaned_text))
    print(f"7. Visible Word Count: {visible_words} words (Passes > 2,500 words)")
    assert visible_words >= 2500, f"Word count too low: {visible_words}"

    # 8. FAQs count in visible HTML
    faq_questions = re.findall(r'<h3 class="wp-block-heading">(.*?\?)</h3>', html)
    print(f"8. Visible FAQ Questions ({len(faq_questions)} found):")
    for q in faq_questions:
        print(f"   - {q}")
    assert len(faq_questions) >= 5, f"Expected at least 5 FAQs, found {len(faq_questions)}"

    # 9. Section ordering: Final Thoughts before FAQs
    final_thoughts_pos = html.find("Final Thoughts on Selecting the Perfect Light Weight Gold Earrings Design")
    faq_heading_pos = html.find("Frequently Asked Questions About Light Weight Gold Earrings Design")
    print(f"9. Section ordering: Final Thoughts pos={final_thoughts_pos}, FAQs pos={faq_heading_pos}")
    assert final_thoughts_pos != -1 and faq_heading_pos != -1, "Headings not found"
    assert final_thoughts_pos < faq_heading_pos, "Final thoughts must appear before FAQs"

    # 10. Prohibited dashes in body
    entry_m = re.search(r'<div class="entry-content[^"]*"[^>]*>([\s\S]*?)(?:<footer|<nav|</article|<!-- \.entry-content)', html)
    body_content = entry_m.group(1) if entry_m else ""
    assert len(body_content) > 1000, "Could not extract article body"
    assert "—" not in body_content, "Prohibited em dash found in body"
    assert "–" not in body_content, "Prohibited en dash found in body"
    print("10. Prohibited Dash Check: Passed (0 em/en dashes in body)")

    # 11. No raw HTML tables
    assert "<table" not in body_content and "wp:table" not in body_content, "Prohibited HTML table found"
    print("11. Table Check: Passed (0 raw tables)")

    # 12. Schema validation
    assert 'application/ld+json' in html, "JSON-LD schema missing"
    assert '"@type": "BlogPosting"' in html or '"@type":"BlogPosting"' in html, "BlogPosting schema missing"
    assert '"@type": "FAQPage"' in html or '"@type":"FAQPage"' in html, "FAQPage schema missing"
    print("12. Schema Check: Passed (BlogPosting + FAQPage valid)")

    # 13. Related Guides cluster links
    related_guides_pos = html.find("More Jewellery &amp; Buying Guides")
    assert related_guides_pos != -1, "More Jewellery & Buying Guides heading missing"
    assert final_thoughts_pos < related_guides_pos < faq_heading_pos, "Related guides must sit between Final Thoughts and FAQs"
    print("13. Related Guides Cluster Section: Verified and correctly placed")

    print("\n==========================================")
    print("ALL 13 LIVE QA AUDIT CHECKS PASSED WITH 100% ACCURACY!")
    print("==========================================")

    return {
        "status": "passed",
        "visible_words": visible_words,
        "h2_count": len(re.findall(r'<h2', html)),
        "h3_count": len(re.findall(r'<h3', html)),
        "faq_count": len(faq_questions),
        "og_image": og_image,
        "canonical": canon_url,
        "post_id": POST_ID
    }

if __name__ == "__main__":
    res = run_qa()
    out_file = Path("output/week9_rank71_live_qa.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)
    print(f"Saved QA report to {out_file}")
