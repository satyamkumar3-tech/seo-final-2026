#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive Live QA script for Week 9 Rank 61: women-chain-2026."""
import os, sys, json, re, urllib.request
from urllib.parse import urlparse

LIVE_URL = "https://blog.bluestone.com/women-chain-2026/"
POST_ID = 40148

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
    
    # 1. Fetch live HTML
    req = urllib.request.Request(LIVE_URL, headers={"User-Agent": "Mozilla/5.0"})
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
    title = title_match.group(1) if title_match else "NOT FOUND"
    print(f"3. Page Title: {title}")
    assert "women chain" in title.lower(), "Primary KW missing in title"

    # 4. Meta Description
    meta_desc_match = re.search(r'<meta name="description" content="([^"]+)"', html)
    meta_desc = meta_desc_match.group(1) if meta_desc_match else "NOT FOUND"
    print(f"4. Meta Description: {meta_desc} (Length: {len(meta_desc)})")
    assert "women chain" in meta_desc.lower(), "Primary KW missing in meta description"

    # 5. Author verification
    author_match = re.search(r'author-(?:satyam|270271337)', html) or "By Satyam, BlueStone Editorial" in html
    print(f"5. Author Verification: {'PASS (Satyam)' if author_match else 'FAIL'}")
    assert author_match, "Author Satyam not verified in HTML"

    # 6. H1 Count
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, flags=re.DOTALL)
    print(f"6. H1 Count: {len(h1s)}")
    assert len(h1s) == 1, f"Expected exactly 1 H1, found {len(h1s)}"

    # 7. Headings Hierarchy
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, flags=re.DOTALL)
    clean_h2s = [re.sub(r'<[^>]+>', '', h).strip() for h in h2s]
    print(f"7. H2 Count: {len(clean_h2s)}")
    for i, h in enumerate(clean_h2s, 1):
        print(f"    {i}. {h}")
    assert len(clean_h2s) >= 8, f"Expected at least 8 H2s, found {len(clean_h2s)}"

    # 8. Word Count
    text_content = re.sub(r'<style>.*?</style>', '', html, flags=re.DOTALL)
    text_content = re.sub(r'<script.*?</script>', '', text_content, flags=re.DOTALL)
    text_content = re.sub(r'<[^>]+>', ' ', text_content)
    words = [w for w in text_content.split() if w]
    print(f"8. Total Page Word Count: ~{len(words)} words (PASS)")
    assert len(words) >= 1500, f"Expected at least 1500 words, found {len(words)}"

    # 9. Prohibited Characters in Article Body
    body_match = re.search(r'(<h2 class="wp-block-heading">Understanding Women Chain Designs.*?Frequently Asked Questions About Women Chain Selection.*?</script>)', html, flags=re.DOTALL)
    article_body = body_match.group(1) if body_match else html
    prose_body = re.sub(r'<style>.*?</style>', '', article_body, flags=re.DOTALL)
    prose_body = re.sub(r'<script.*?</script>', '', prose_body, flags=re.DOTALL)

    em_dashes = '—' in prose_body
    en_dashes = '–' in prose_body
    spaced_hyphens = bool(re.search(r'\s-\s', prose_body))
    print(f"9. Prohibited Characters in Body: Em-dash: {em_dashes}, En-dash: {en_dashes}, Spaced hyphen: {spaced_hyphens} (PASS)")
    assert not em_dashes, "Found prohibited em-dash in body"
    assert not en_dashes, "Found prohibited en-dash in body"
    assert not spaced_hyphens, "Found prohibited spaced hyphen in body prose"

    # 10. No HTML Tables
    has_table = '<table' in html.lower() or 'wp-block-table' in html.lower()
    print(f"10. HTML Table check: {'PASS (No tables)' if not has_table else 'FAIL'}")
    assert not has_table, "Found prohibited HTML table"

    # 11. 3D Coverflow Carousel Elements
    has_bs_cf = 'class="bs-cf"' in html
    has_stage = 'class="bs-cf-stage"' in html
    has_card = 'class="bs-cf-card' in html
    has_dots = 'class="bs-cf-dots"' in html
    print(f"11. Carousel Elements: bs-cf={has_bs_cf}, stage={has_stage}, card={has_card}, dots={has_dots}")
    assert has_bs_cf and has_stage and has_card and has_dots, "Missing 3D coverflow carousel elements!"

    # 12. Carousel Image URLs HTTP 200
    carousel_imgs = re.findall(r'<div class="bs-cf-card[^"]*"[^>]*>.*?<img[^>]+src="([^"]+)"', html, flags=re.DOTALL)
    print(f"12. Carousel Images Found: {len(carousel_imgs)}")
    assert len(carousel_imgs) == 6, f"Expected 6 carousel images, found {len(carousel_imgs)}"
    for idx, c_url in enumerate(carousel_imgs, 1):
        st = head_status(c_url)
        print(f"    Image {idx}: {c_url} -> HTTP {st}")
        assert st == 200, f"Carousel image {c_url} returned {st}"

    # 13. OpenGraph / Twitter Image
    og_img_match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    og_img = og_img_match.group(1) if og_img_match else "NOT FOUND"
    print(f"13. og:image: {og_img}")
    assert head_status(og_img) == 200, f"og:image {og_img} is not HTTP 200"

    # 14. Schema JSON-LD Validation
    schemas = re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', html, flags=re.DOTALL)
    print(f"14. JSON-LD Schemas Found: {len(schemas)}")
    has_faq = False
    has_blogposting = False
    for s in schemas:
        try:
            sd = json.loads(s)
            graph = sd.get("@graph", [sd])
            for item in graph:
                if item.get("@type") == "FAQPage":
                    has_faq = True
                    q_count = len(item.get("mainEntity", []))
                    print(f"    FAQPage Schema: {q_count} questions (PASS)")
                if item.get("@type") == "BlogPosting":
                    has_blogposting = True
                    print(f"    BlogPosting Schema: Author={item.get('author')}, Images={item.get('image')} (PASS)")
        except Exception as e:
            pass
    assert has_faq, "FAQPage schema missing"
    assert has_blogposting, "BlogPosting schema missing"

    # 15. Section Ordering: Conclusion before FAQ
    conclusion_pos = html.find("Finding Your Signature Women Chain")
    related_guides_pos = html.find("More Jewellery &#038; Buying Guides")
    if related_guides_pos == -1:
        related_guides_pos = html.find("More Jewellery & Buying Guides")
    if related_guides_pos == -1:
        related_guides_pos = html.find("More Jewellery")
    faq_pos = html.find("Frequently Asked Questions About Women Chain Selection")
    print(f"15. Section Positions: Conclusion={conclusion_pos}, Related Guides={related_guides_pos}, FAQ={faq_pos}")
    assert conclusion_pos != -1, "Conclusion heading not found"
    assert related_guides_pos != -1, "Related Guides heading not found"
    assert faq_pos != -1, "FAQ heading not found"
    assert conclusion_pos < related_guides_pos < faq_pos, "Section order violation: Expected Conclusion < Related Guides < FAQ"

    # 16. Internal Cluster Links in Related Guides
    internal_links = [
        "how-to-check-gold-purity-2026",
        "gst-on-gold-jewellery-in-india-what-youre-actually-paying-in-tax",
        "is-buying-gold-jewellery-online-safe-in-india-the-honest-answer",
        "916-hallmark-gold-2026",
        "daily-wear-modern-gold-bangles-design-2026"
    ]
    for il in internal_links:
        assert il in html, f"Missing internal cluster link: {il}"
    print(f"16. Internal Cluster Links: All 5 verified (PASS)")

    # 17. In-body Type 3 Images and Captions
    figures = re.findall(r'<figure class="wp-block-image size-full">(.*?)</figure>', html, flags=re.DOTALL)
    print(f"17. In-body Type 3 Images with PDP links & captions: {len(figures)}")
    assert len(figures) == 2, f"Expected 2 in-body Type 3 images (flatlay & lifestyle), found {len(figures)}"
    for idx, fig in enumerate(figures, 1):
        a_href_match = re.search(r'<a href="([^"]+)">', fig)
        img_src_match = re.search(r'<img[^>]+src="([^"]+)"', fig)
        figcaption_match = re.search(r'<figcaption>(.*?)</figcaption>', fig, flags=re.DOTALL)
        
        assert a_href_match, f"Missing PDP link in figure {idx}"
        assert img_src_match, f"Missing img src in figure {idx}"
        assert figcaption_match, f"Missing figcaption in figure {idx}"
        
        pdp = a_href_match.group(1)
        src = img_src_match.group(1).replace('&#038;', '&')
        caption = re.sub(r'<[^>]+>', '', figcaption_match.group(1)).strip()
        
        st = head_status(src)
        print(f"    In-body {idx}: {src} -> HTTP {st} (PDP: {pdp})")
        assert st == 200, f"In-body image {src} returned {st}"
        assert pdp.startswith("https://www.bluestone.com/"), f"Invalid PDP link: {pdp}"
        assert len(caption) > 10, f"Caption too short: {caption}"

    print("\nALL 17 LIVE QA CHECKS PASSED PERFECTLY!")

if __name__ == "__main__":
    run_qa()
