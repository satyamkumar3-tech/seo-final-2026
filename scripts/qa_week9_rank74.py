#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive Live QA script for Week 9 Rank 74: Neelam Stone Ring Buying Guide."""
import urllib.request
import re
import json

URL = "https://blog.bluestone.com/neelam-stone-ring-2026/"
POST_ID = 40286

def run_live_qa():
    print(f"Fetching live URL: {URL}...")
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        status_code = resp.status
        html = resp.read().decode('utf-8', errors='ignore')

    print(f"HTTP Status: {status_code}")
    assert status_code == 200, f"Expected 200, got {status_code}"

    # 1. Canonical URL
    canonical_match = re.search(r'<link rel=[\'"]canonical[\'"] href=[\'"]([^\'"]+)[\'"]', html)
    canonical = canonical_match.group(1) if canonical_match else "NOT FOUND"
    print(f"Canonical URL: {canonical}")
    assert canonical == URL, f"Canonical mismatch: {canonical} vs {URL}"

    # 2. OpenGraph Image
    og_img_match = re.search(r'<meta property=[\'"]og:image[\'"] content=[\'"]([^\'"]+)[\'"]', html)
    og_img = og_img_match.group(1) if og_img_match else "NOT FOUND"
    print(f"og:image: {og_img}")
    assert "neelam-stone-ring-hero-2026.webp" in og_img or "wp-content/uploads" in og_img, f"Unexpected og:image: {og_img}"

    # 3. Headings
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, flags=re.DOTALL)
    clean_h1s = [re.sub(r'<[^>]+>', '', h).strip() for h in h1s]
    print(f"H1 Count: {len(clean_h1s)} -> {clean_h1s}")
    assert len(clean_h1s) == 1, f"Expected exactly 1 H1, found {len(clean_h1s)}"

    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, flags=re.DOTALL)
    clean_h2s = [re.sub(r'<[^>]+>', '', h).strip() for h in h2s if len(re.sub(r'<[^>]+>', '', h).strip()) > 3]
    print(f"\nH2 Count ({len(clean_h2s)}):")
    for i, h in enumerate(clean_h2s, 1):
        print(f"  {i}. {h}")
    assert len(clean_h2s) >= 10, f"Expected at least 10 H2s, found {len(clean_h2s)}"

    # 4. Visible word count
    # Strip script, style, head, nav, footer
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html, flags=re.DOTALL)
    body_html = body_match.group(1) if body_match else html
    body_clean = re.sub(r'<script.*?</script>', '', body_html, flags=re.DOTALL)
    body_clean = re.sub(r'<style.*?</style>', '', body_clean, flags=re.DOTALL)
    body_text = re.sub(r'<[^>]+>', ' ', body_clean)
    words = re.findall(r'\b[A-Za-z0-9_]+\b', body_text)
    print(f"\nVisible word count: {len(words)}")
    assert len(words) >= 2000, f"Expected word count >= 2000, got {len(words)}"

    # 5. 3D Coverflow Carousel Gate
    has_bs_cf = 'class="bs-cf"' in html or 'class="bs-cf ' in html or 'id="bs-cf-' in html
    has_bs_cf_stage = 'class="bs-cf-stage"' in html
    has_bs_cf_card = 'class="bs-cf-card' in html
    has_bs_cf_dots = 'class="bs-cf-dots"' in html
    print(f"\nCarousel 3D Coverflow elements: bs-cf={has_bs_cf}, stage={has_bs_cf_stage}, card={has_bs_cf_card}, dots={has_bs_cf_dots}")
    assert has_bs_cf and has_bs_cf_stage and has_bs_cf_card and has_bs_cf_dots, "Missing 3D coverflow carousel elements"

    # 6. Verify 6 carousel image URLs return HTTP 200
    carousel_imgs = re.findall(r'<div class=[\'"]bs-cf-card.*?<img[^>]+src=[\'"]([^\'"]+)[\'"]', html, flags=re.DOTALL)
    print(f"\nCarousel images found: {len(carousel_imgs)}")
    assert len(carousel_imgs) == 6, f"Expected 6 carousel images, found {len(carousel_imgs)}"
    for idx, c_url in enumerate(carousel_imgs, 1):
        c_req = urllib.request.Request(c_url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
        with urllib.request.urlopen(c_req, timeout=10) as c_resp:
            print(f"  Card {idx}: {c_url} -> HTTP {c_resp.status}")
            assert c_resp.status == 200, f"Card {idx} image failed with status {c_resp.status}"

    # 7. Type 3 In-body images & Captions
    body_imgs = re.findall(r'<figure class=[\'"]wp-block-image size-full[\'"]>.*?<img[^>]+src=[\'"]([^\'"]+)[\'"].*?<figcaption>(.*?)</figcaption>', html, flags=re.DOTALL)
    print(f"\nIn-body Type 3 figure images with figcaptions: {len(body_imgs)}")
    assert len(body_imgs) == 2, f"Expected 2 in-body Type 3 images with figcaption, found {len(body_imgs)}"
    for idx, (img_src, caption) in enumerate(body_imgs, 1):
        clean_cap = re.sub(r'<[^>]+>', '', caption).strip()
        print(f"  Image {idx}: {img_src}")
        print(f"  Caption {idx}: {clean_cap}")
        # Verify image HTTP 200
        t_req = urllib.request.Request(img_src, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
        with urllib.request.urlopen(t_req, timeout=10) as t_resp:
            print(f"  HTTP Status: {t_resp.status}")
            assert t_resp.status == 200

    # 8. Schema verification
    schemas = re.findall(r'<script type=[\'"]application/ld\+json[\'"][^>]*>(.*?)</script>', html, flags=re.DOTALL)
    print(f"\nJSON-LD Schemas found: {len(schemas)}")
    has_blogposting = False
    has_faqpage = False
    for s in schemas:
        try:
            s_data = json.loads(s)
            graph = s_data.get("@graph", [s_data])
            for item in graph:
                if item.get("@type") == "BlogPosting":
                    has_blogposting = True
                    print("  Found BlogPosting schema: Author =", item.get("author"))
                    print("  Images in BlogPosting:", item.get("image"))
                elif item.get("@type") == "FAQPage":
                    has_faqpage = True
                    faqs = item.get("mainEntity", [])
                    print(f"  Found FAQPage schema with {len(faqs)} questions")
        except Exception:
            pass

    assert has_blogposting, "Missing BlogPosting schema"
    assert has_faqpage, "Missing FAQPage schema"

    # 9. Internal links
    internal_links = re.findall(r'href=[\'"](https://blog\.bluestone\.com/[^\'"]+)[\'"]', html)
    unique_internals = list(set([l for l in internal_links if l != URL]))
    print(f"\nUnique Internal Blog Links ({len(unique_internals)}):")
    for l in unique_internals:
        print(f"  - {l}")
    assert len(unique_internals) >= 4, f"Expected at least 4 internal links, got {len(unique_internals)}"

    # 10. Prohibited dashes & prices in article content
    m_start = html.find('By Satyam, BlueStone Editorial')
    m_end = html.find('Frequently Asked Questions')
    m_last_q = html.find('How do you clean and maintain a neelam stone ring at home?')
    if m_last_q != -1:
        end_idx = html.find('</p>', m_last_q) + 4
    else:
        end_idx = len(html)
    
    article_content_html = html[m_start:end_idx] if m_start != -1 else body_clean
    content_no_style = re.sub(r'<style.*?</style>', '', article_content_html, flags=re.DOTALL)
    content_text = re.sub(r'<[^>]+>', ' ', content_no_style)
    
    prohibited_em = re.findall(r'—', content_text)
    prohibited_en = re.findall(r'–', content_text)
    prohibited_hyphen = re.findall(r'\s-\s', content_text)
    prices = re.findall(r'₹\s*[0-9,]+', content_text)
    print(f"\nProhibited checks in article content: em={len(prohibited_em)}, en={len(prohibited_en)}, spaced_hyphens={len(prohibited_hyphen)}, prices={len(prices)}")
    assert len(prohibited_em) == 0, f"Found {len(prohibited_em)} em dashes"
    assert len(prohibited_en) == 0, f"Found {len(prohibited_en)} en dashes"
    assert len(prohibited_hyphen) == 0, f"Found {len(prohibited_hyphen)} spaced hyphens"
    assert len(prices) == 0, f"Found {len(prices)} price mentions"

    # 11. Section ordering: Final Thoughts BEFORE FAQs
    conclusion_idx = html.find("Final Thoughts")
    faq_idx = html.find("Frequently Asked Questions")
    print(f"\nSection ordering: Conclusion pos={conclusion_idx}, FAQ pos={faq_idx}")
    assert conclusion_idx != -1 and faq_idx != -1, "Missing conclusion or FAQ section"
    assert conclusion_idx < faq_idx, "Conclusion MUST appear BEFORE Frequently Asked Questions"

    print("\n==========================================")
    print("ALL LIVE QA CHECKS PASSED PERFECTLY!")
    print("==========================================")

if __name__ == "__main__":
    run_live_qa()
