#!/usr/bin/env python3
"""Comprehensive Live QA script for Week 8 Rank 26: Unique Gold Earrings Design."""
import os
import re
import sys
import json
import urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL = "https://blog.bluestone.com/unique-gold-earrings-design-2026/"
POST_ID = 37280

def run_qa():
    print(f"Fetching live URL: {URL} ...")
    req = urllib.request.Request(URL + "?v=live_qa_final", headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        status_code = resp.status
        html = resp.read().decode('utf-8')
        
    assert status_code == 200, f"Expected 200, got {status_code}"
    
    checks = []
    
    # 1. H1 check
    h1_matches = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.DOTALL | re.IGNORECASE)
    h1_clean = [re.sub(r'<[^>]+>', '', h).strip() for h in h1_matches]
    checks.append({
        "check": "Single H1 heading",
        "pass": len(h1_matches) == 1,
        "detail": f"Found {len(h1_matches)} H1(s): {h1_clean}"
    })
    
    # 2. H2 count & map
    h2_matches = [re.sub(r'<[^>]+>', '', h).strip() for h in re.findall(r"<h2[^>]*>(.*?)</h2>", html, re.DOTALL | re.IGNORECASE)]
    checks.append({
        "check": "H2 headings present",
        "pass": len(h2_matches) >= 8,
        "detail": f"Found {len(h2_matches)} H2s: {h2_matches}"
    })
    
    # Verify section ordering: Conclusion before FAQ
    faq_idx = -1
    conclusion_idx = -1
    for i, h in enumerate(h2_matches):
        if "frequently asked questions" in h.lower():
            faq_idx = i
        if "final thoughts" in h.lower() or "conclusion" in h.lower():
            conclusion_idx = i
            
    checks.append({
        "check": "Section Ordering (Conclusion before FAQ)",
        "pass": conclusion_idx != -1 and faq_idx != -1 and conclusion_idx < faq_idx,
        "detail": f"Conclusion index: {conclusion_idx}, FAQ index: {faq_idx}"
    })
    
    # 3. Canonical URL
    can_match = re.search(r'<link[^>]+rel=[\'"]canonical[\'"][^>]+href=[\'"]([^\'"]+)[\'"]', html, re.IGNORECASE)
    can_url = can_match.group(1) if can_match else ""
    checks.append({
        "check": "Canonical URL",
        "pass": can_url == URL,
        "detail": f"Canonical: {can_url}"
    })
    
    # 4. OpenGraph Image
    og_match = re.search(r'<meta[^>]+property=[\'"]og:image[\'"][^>]+content=[\'"]([^\'"]+)[\'"]', html, re.IGNORECASE)
    og_url = og_match.group(1) if og_match else ""
    checks.append({
        "check": "OG Image",
        "pass": bool(og_url and "unique-gold-earrings-design-hero-2026.webp" in og_url),
        "detail": f"og:image: {og_url}"
    })
    
    # 5. Body Word Count & Prohibited characters inside entry-content
    start_pos = html.find("entry-content")
    end_pos = html.find("<footer")
    if end_pos == -1:
        end_pos = len(html)
    body_html = html[start_pos:end_pos]
    
    text_no_scripts = re.sub(r'<script[^>]*>.*?</script>', ' ', body_html, flags=re.DOTALL)
    text_no_style = re.sub(r'<style[^>]*>.*?</style>', ' ', text_no_scripts, flags=re.DOTALL)
    clean_body = re.sub(r'<[^>]+>', ' ', text_no_style)
    clean_body = unescape(clean_body)
    words = re.findall(r'\b\w+\b', clean_body)
    
    checks.append({
        "check": "Visible Word Count (>=2000)",
        "pass": len(words) >= 2000,
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
    
    # 6. No HTML tables
    tables = re.findall(r"<table", body_html, re.IGNORECASE)
    checks.append({
        "check": "No HTML tables in body",
        "pass": len(tables) == 0,
        "detail": f"Found {len(tables)} tables"
    })
    
    # 7. No prices
    prices = re.findall(r'(?:₹|\bRs\.?\s*\d|\bINR\s*\d|\bUSD\s*\d|\$\s*\d)', clean_body, re.IGNORECASE)
    checks.append({
        "check": "No price figures",
        "pass": len(prices) == 0,
        "detail": f"Price mentions found: {len(prices)}"
    })
    
    # 8. Carousel cards
    cards = re.findall(r'class=[\'"][^\'"]*bs-cf-card[^\'"]*[\'"]', body_html)
    checks.append({
        "check": "Carousel 6 product cards",
        "pass": len(cards) == 6,
        "detail": f"Found {len(cards)} carousel cards"
    })
    
    # 9. In-body Type 3 images
    has_flatlay = "unique-gold-earrings-design-flatlay-2026.webp" in body_html
    has_lifestyle = "unique-gold-earrings-design-lifestyle-2026.webp" in body_html
    checks.append({
        "check": "In-body Type 3 images (flatlay + lifestyle)",
        "pass": has_flatlay and has_lifestyle,
        "detail": f"Flatlay present: {has_flatlay}, Lifestyle present: {has_lifestyle}"
    })
    
    # 10. FAQ visibility
    faq_h2 = any("Frequently Asked Questions" in h for h in h2_matches)
    checks.append({
        "check": "Visible FAQ section",
        "pass": faq_h2,
        "detail": f"FAQ heading present: {faq_h2}"
    })
    
    # 11. Schema tags
    has_faq_schema = '"@type": "FAQPage"' in html or '"@type":"FAQPage"' in html
    has_blog_schema = '"@type": "BlogPosting"' in html or '"@type":"BlogPosting"' in html
    checks.append({
        "check": "JSON-LD Schemas (FAQPage & BlogPosting)",
        "pass": has_faq_schema and has_blog_schema,
        "detail": f"FAQPage schema: {has_faq_schema}, BlogPosting schema: {has_blog_schema}"
    })
    
    # 12. Internal links
    links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', body_html)
    internal_links = [l for l in links if "blog.bluestone.com" in l and "unique-gold-earrings-design-2026" not in l]
    checks.append({
        "check": "Internal links (>=4)",
        "pass": len(internal_links) >= 4,
        "detail": f"Internal links: {len(internal_links)} ({internal_links})"
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
        print("ALL 12 LIVE QA GATES PASSED PERFECTLY!")
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
    with open(ROOT / "output/Week8_Rank26_UniqueGoldEarrings_qa_results.json", "w") as f:
        json.dump(qa_artifact, f, indent=2)
    return qa_artifact

if __name__ == "__main__":
    run_qa()
