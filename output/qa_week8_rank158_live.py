#!/usr/bin/env python3
"""Comprehensive Live QA script for Week 8 Rank 158: Party Wear Earrings Buying Guide 2026."""
import os
import re
import sys
import json
import urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL = "https://blog.bluestone.com/party-wear-earrings-2026/"
POST_ID = 38850

def verify_http_200(img_url: str) -> bool:
    try:
        req = urllib.request.Request(img_url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"HEAD failed for {img_url}: {e}")
        return False

def run_qa():
    print(f"Fetching live URL: {URL} ...")
    req = urllib.request.Request(URL + "?v=live_qa_final", headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        status_code = resp.status
        html = resp.read().decode("utf-8")
        
    assert status_code == 200, f"Expected 200, got {status_code}"
    
    checks = []
    
    # 1. H1 check
    h1_matches = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.DOTALL | re.IGNORECASE)
    h1_clean = [re.sub(r"<[^>]+>", "", h).strip() for h in h1_matches]
    checks.append({
        "check": "Single H1 heading",
        "pass": len(h1_matches) == 1,
        "detail": f"Found {len(h1_matches)} H1(s): {h1_clean}"
    })
    
    # 2. H2 count & map
    h2_matches = [re.sub(r"<[^>]+>", "", h).strip() for h in re.findall(r"<h2[^>]*>(.*?)</h2>", html, re.DOTALL | re.IGNORECASE)]
    checks.append({
        "check": "H2 headings present (>=8)",
        "pass": len(h2_matches) >= 8,
        "detail": f"Found {len(h2_matches)} H2s: {h2_matches}"
    })
    
    # 3. Verify section ordering: Conclusion before Related before FAQ
    faq_idx = -1
    conclusion_idx = -1
    related_idx = -1
    for i, h in enumerate(h2_matches):
        if "frequently asked questions" in h.lower():
            faq_idx = i
        if "final thoughts" in h.lower() or "conclusion" in h.lower():
            conclusion_idx = i
        if "more jewellery" in h.lower() or "buying guides" in h.lower():
            related_idx = i
            
    checks.append({
        "check": "Section Ordering (Conclusion before Related before FAQ)",
        "pass": conclusion_idx != -1 and faq_idx != -1 and conclusion_idx < related_idx < faq_idx,
        "detail": f"Conclusion index: {conclusion_idx}, Related index: {related_idx}, FAQ index: {faq_idx}"
    })
    
    # 4. Canonical URL
    can_match = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']', html, re.IGNORECASE)
    can_url = can_match.group(1) if can_match else ""
    checks.append({
        "check": "Canonical URL matches live slug",
        "pass": can_url == URL,
        "detail": f"Canonical: {can_url}"
    })
    
    # 5. OpenGraph Image
    og_match = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
    og_url = og_match.group(1) if og_match else ""
    checks.append({
        "check": "OG Image matches hero image",
        "pass": bool(og_url and "party-wear-earrings-hero-2026.webp" in og_url),
        "detail": f"og:image: {og_url}"
    })
    
    # 6. Body Word Count & Prohibited characters inside entry-content
    start_pos = html.find("entry-content")
    end_pos = html.find("<footer", start_pos)
    if end_pos == -1:
        end_pos = len(html)
    body_html = html[start_pos:end_pos]
    
    text_no_scripts = re.sub(r"<script[^>]*>.*?</script>", " ", body_html, flags=re.DOTALL)
    text_no_style = re.sub(r"<style[^>]*>.*?</style>", " ", text_no_scripts, flags=re.DOTALL)
    clean_body = re.sub(r"<[^>]+>", " ", text_no_style)
    clean_body = unescape(clean_body)
    words = re.findall(r'\b\w+\b', clean_body)
    
    checks.append({
        "check": "Visible Word Count (>=1500)",
        "pass": len(words) >= 1500,
        "detail": f"Total visible word count in body: {len(words)} words"
    })
    
    em_dashes = [m.start() for m in re.finditer(r'—', clean_body)]
    en_dashes = [m.start() for m in re.finditer(r'–', clean_body)]
    spaced_hyphens = [m.group(0) for m in re.finditer(r'\b\w+\s+-\s+\w+\b', clean_body)]
    checks.append({
        "check": "No prohibited dashes in body (em/en/spaced)",
        "pass": len(em_dashes) == 0 and len(en_dashes) == 0 and len(spaced_hyphens) == 0,
        "detail": f"em_dashes: {len(em_dashes)}, en_dashes: {len(en_dashes)}, spaced_hyphens: {len(spaced_hyphens)}"
    })
    
    # 7. No HTML tables
    tables = re.findall(r"<table", body_html, re.IGNORECASE)
    checks.append({
        "check": "No HTML tables in body",
        "pass": len(tables) == 0,
        "detail": f"Found {len(tables)} tables"
    })
    
    # 8. No prices
    prices = re.findall(r"(?:₹| Rs\.?\s*\d| INR\s*\d| USD\s*\d|\$\s*\d)", clean_body, re.IGNORECASE)
    checks.append({
        "check": "No price figures",
        "pass": len(prices) == 0,
        "detail": f"Price mentions found: {len(prices)}"
    })
    
    # 9. Carousel 3D Coverflow elements & cards
    has_bs_cf = ".bs-cf" in body_html or 'class="bs-cf"' in body_html
    has_bs_cf_stage = "bs-cf-stage" in body_html
    has_bs_cf_dots = "bs-cf-dots" in body_html
    cards = re.findall(r'class=["\'][^"\']*bs-cf-card[^"\']*["\']', body_html)
    checks.append({
        "check": "Carousel 3D Coverflow Container & 6 product cards",
        "pass": has_bs_cf and has_bs_cf_stage and has_bs_cf_dots and len(cards) == 6,
        "detail": f"bs-cf: {has_bs_cf}, stage: {has_bs_cf_stage}, dots: {has_bs_cf_dots}, cards: {len(cards)}"
    })
    
    # 10. Carousel media HTTP 200 check
    card_img_urls = [u.replace("&#038;", "&") for u in re.findall(r'class=["\'][^"\']*bs-cf-media[^"\']*["\'][^>]*>.*?<img[^>]+src=["\']([^"\']+)["\']', body_html, re.DOTALL)]
    card_urls_ok = len(card_img_urls) == 6 and all(verify_http_200(u) for u in card_img_urls)
    checks.append({
        "check": "Carousel all 6 card images return HTTP 200",
        "pass": card_urls_ok,
        "detail": f"Found {len(card_img_urls)} image URLs, all HTTP 200: {card_urls_ok}"
    })
    
    # 11. In-body Type 3 images
    has_flatlay = "party-wear-earrings-flatlay-2026.webp" in body_html
    has_lifestyle = "party-wear-earrings-lifestyle-2026.webp" in body_html
    checks.append({
        "check": "In-body Type 3 images (flatlay + lifestyle)",
        "pass": has_flatlay and has_lifestyle,
        "detail": f"Flatlay present: {has_flatlay}, Lifestyle present: {has_lifestyle}"
    })
    
    # 12. Visible FAQ section
    faq_h2 = any("Frequently Asked Questions" in h for h in h2_matches)
    checks.append({
        "check": "Visible FAQ section",
        "pass": faq_h2,
        "detail": f"FAQ heading present: {faq_h2}"
    })
    
    # 13. Schema tags
    has_faq_schema = '"@type": "FAQPage"' in html or '"@type":"FAQPage"' in html
    has_blog_schema = '"@type": "BlogPosting"' in html or '"@type":"BlogPosting"' in html
    has_schema_images = "party-wear-earrings-hero-2026.webp" in html and "party-wear-earrings-flatlay-2026.webp" in html
    checks.append({
        "check": "JSON-LD Schemas (FAQPage & BlogPosting with images)",
        "pass": has_faq_schema and has_blog_schema and has_schema_images,
        "detail": f"FAQPage schema: {has_faq_schema}, BlogPosting schema: {has_blog_schema}, Schema images: {has_schema_images}"
    })
    
    # 14. Internal links
    links = re.findall(r'href=["\']([^"\']+)["\']', body_html)
    internal_links = [l for l in links if "blog.bluestone.com" in l and "party-wear-earrings-2026" not in l]
    checks.append({
        "check": "Internal links (>=4)",
        "pass": len(internal_links) >= 4,
        "detail": f"Internal links: {len(internal_links)} ({internal_links})"
    })
    
    # 15. Author Satyam & Byline
    has_byline = "By Satyam, BlueStone Editorial" in html
    checks.append({
        "check": "Author Byline (By Satyam, BlueStone Editorial)",
        "pass": has_byline,
        "detail": f"Byline present: {has_byline}"
    })
    
    print("\n================== LIVE QA AUDIT RESULTS ==================")
    all_passed = True
    for c in checks:
        status_str = "PASS" if c["pass"] else "FAIL"
        if not c["pass"]:
            all_passed = False
        print(f"[{status_str}] {c['check']}: {c['detail']}")
        
    print("===========================================================")
    if all_passed:
        print("ALL 15 LIVE QA GATES PASSED PERFECTLY!")
    else:
        print("SOME QA CHECKS FAILED - REVIEW ABOVE.")
        sys.exit(1)
        
    qa_artifact = {
        "url": URL,
        "post_id": POST_ID,
        "word_count": len(words),
        "h1": h1_clean[0] if h1_clean else "",
        "og_image": og_url,
        "checks": checks,
        "all_passed": all_passed
    }
    with open(ROOT / "output/Week8_Rank158_PartyWearEarrings_qa_results.json", "w", encoding="utf-8") as f:
        json.dump(qa_artifact, f, indent=2)
    return qa_artifact

if __name__ == "__main__":
    run_qa()
