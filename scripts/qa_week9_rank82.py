#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive Live QA script for Week 9 Rank 82: Rose Gold Bangle Buying Guide."""
import os
import sys
import re
import json
import urllib.request
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

URL = "https://blog.bluestone.com/rose-gold-bangle-2026/"
POST_ID = 40381
SLUG = "rose-gold-bangle-2026"

def run_qa():
    cache_url = f"{URL}?cache_bust={int(time.time())}"
    print(f"Fetching live page: {cache_url}...")
    req = urllib.request.Request(cache_url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})
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
    assert "rose-gold-bangle-hero-2026" in og_image, f"Hero og:image mismatch: {og_image}"

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
        clean_u = u.replace("&#038;", "&")
        h_req = urllib.request.Request(clean_u, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(h_req, timeout=15) as r:
            assert r.status == 200, f"Image {clean_u} returned {r.status}"
            print(f"   HTTP 200 OK: {clean_u.split('/')[-1]}")

    # 6. Type 3 in-body images
    flatlay_in_dom = "rose-gold-bangle-flatlay-2026" in html
    lifestyle_in_dom = "rose-gold-bangle-lifestyle-2026" in html
    print(f"6. Type 3 in-body images: Flatlay present={flatlay_in_dom}, Lifestyle present={lifestyle_in_dom}")
    assert flatlay_in_dom and lifestyle_in_dom, "Missing in-body Type 3 images"

    # Verify hero is NOT duplicated in body <img> tags
    entry_m = re.search(r'<div class="entry-content[^"]*"[^>]*>([\s\S]*?)(?:<footer|<nav|</article|<!-- \.entry-content)', html)
    body_content = entry_m.group(1) if entry_m else ""
    assert len(body_content) > 1000, "Could not extract article body"

    body_no_script = re.sub(r'<script[\s\S]*?</script>', '', body_content)
    body_no_script = re.sub(r'<style[\s\S]*?</style>', '', body_no_script)
    hero_in_body_img = any("rose-gold-bangle-hero-2026" in img for img in re.findall(r'<img[^>]+>', body_no_script))
    print(f"   Hero duplicate in body <img> check: {hero_in_body_img} (Must be False)")
    assert not hero_in_body_img, "Hero image must not be duplicated in body <img> tags"

    # 7. Word count and section ordering
    cleaned = re.sub(r'<style[\s\S]*?</style>', ' ', html)
    cleaned = re.sub(r'<script[\s\S]*?</script>', ' ', cleaned)
    cleaned_text = re.sub(r'<[^>]+>', ' ', cleaned)
    visible_words = len(re.findall(r'\b\w+\b', cleaned_text))
    print(f"7. Visible Word Count: {visible_words} words (Benchmark: >= 1800 words)")
    assert visible_words >= 1800, f"Word count too low: {visible_words}"

    # 8. FAQs count in visible HTML
    faq_questions = re.findall(r'<h3[^>]*>([^<]*\?)</h3>', html)
    print(f"8. Visible FAQ Questions ({len(faq_questions)} found):")
    for q in faq_questions:
        print(f"   - {q}")
    assert len(faq_questions) >= 5, f"Expected at least 5 FAQs, found {len(faq_questions)}"

    # 9. Section ordering: Final Thoughts before More Gold Buying Guides before FAQs
    final_thoughts_pos = html.find("Final Thoughts")
    related_guides_pos = html.find("More Gold &amp; Jewellery Buying Guides")
    if related_guides_pos == -1:
        related_guides_pos = html.find("More Gold & Jewellery Buying Guides")
    faq_heading_pos = html.find("Frequently Asked Questions")
    print(f"9. Section ordering: Final Thoughts pos={final_thoughts_pos}, Related Guides pos={related_guides_pos}, FAQs pos={faq_heading_pos}")
    assert final_thoughts_pos != -1, "Final thoughts heading missing"
    assert related_guides_pos != -1, "Related guides heading missing"
    assert faq_heading_pos != -1, "FAQs heading missing"
    assert final_thoughts_pos < related_guides_pos < faq_heading_pos, "Section order violation! Must be Final Thoughts -> Related Guides -> FAQs"

    # 10. Prohibited punctuation checks
    print("10. Checking prohibited dash patterns and price mentions...")
    assert "—" not in body_content, "Found em-dash in body!"
    assert "–" not in body_content, "Found en-dash in body!"
    spaced_hyphens = re.findall(r'\s+-\s+', body_no_script)
    assert not spaced_hyphens, f"Found spaced hyphens: {spaced_hyphens}"

    # Price mentions check
    price_patterns = re.findall(r'(?:Rs\.?|INR|₹)\s*\d+', body_no_script)
    print(f"    Price mentions: {price_patterns} (Must be empty)")
    assert not price_patterns, f"Found prohibited price patterns: {price_patterns}"

    # 11. Schema Verification
    print("11. Verifying Trailing JSON-LD Schema...")
    assert "application/ld+json" in html, "Missing JSON-LD schema in DOM"
    assert '"@type":"FAQPage"' in html or '"@type": "FAQPage"' in html, "Missing FAQPage schema"
    assert '"@type":"BlogPosting"' in html or '"@type": "BlogPosting"' in html, "Missing BlogPosting schema"
    assert "Satyam" in html, "Author Satyam missing from schema"

    # 12. Internal Links Count
    internal_links = re.findall(r'href="https://blog\.bluestone\.com/[^"]+"', body_no_script)
    print(f"12. Internal links in body: {len(internal_links)} found")
    assert len(internal_links) >= 4, f"Expected at least 4 internal links, found {len(internal_links)}"

    print("\n==========================================")
    print("ALL LIVE QA GATES PASSED PERFECTLY!")
    print("==========================================")

    qa_summary = {
        "status": "PASS",
        "live_url": URL,
        "wp_post_id": POST_ID,
        "canonical": canon_url,
        "og_image": og_image,
        "visible_words": visible_words,
        "carousel_cards": card_count,
        "faq_count": len(faq_questions),
        "flatlay_in_dom": flatlay_in_dom,
        "lifestyle_in_dom": lifestyle_in_dom,
        "hero_in_body": hero_in_body_img,
        "em_dash": False,
        "en_dash": False,
        "spaced_hyphens": False,
        "prices": False
    }

    with open(ROOT / "output/week9_rank82_live_qa.json", "w", encoding="utf-8") as out_f:
        json.dump(qa_summary, out_f, indent=2)

if __name__ == "__main__":
    run_qa()
