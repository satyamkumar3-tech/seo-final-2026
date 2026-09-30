#!/usr/bin/env python3
"""Comprehensive Live QA script for Week 8 Rank 178: Finger Rings for Girls 2026."""
import os
import re
import sys
import json
import urllib.request
import urllib.error
from html import unescape
from pathlib import Path

ROOT = Path("/Users/satyamkumar/Downloads/seo final 2026")
URL = "https://blog.bluestone.com/finger-rings-for-girls-2026/"
POST_ID = 39077


def verify_http_200(img_url: str) -> bool:
    try:
        req = urllib.request.Request(img_url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except Exception as e:
        try:
            req_get = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req_get, timeout=15) as resp_get:
                return resp_get.status == 200
        except Exception as e2:
            print(f"HTTP check failed for {img_url}: {e2}")
            return False


def run_qa():
    print(f"Fetching live URL: {URL} ...")
    req = urllib.request.Request(URL + "?v=live_qa_final", headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        status_code = resp.status
        html = resp.read().decode("utf-8")

    assert status_code == 200, f"Expected 200, got {status_code}"

    # Extract true entry content boundaries
    idx = html.find("entry-content wp-block-post-content")
    if idx != -1:
        end_idx = html.find('class="robots-nocontent sd-block sd-social', idx)
        if end_idx != -1:
            body_html = html[idx:end_idx]
        else:
            body_html = html[idx:]
    else:
        body_match = re.search(r'<div class="entry-content[^"]*">(.*?)</div>\s*<!-- \.entry-content -->', html, re.DOTALL)
        body_html = body_match.group(1) if body_match else html

    clean_text = re.sub(r"<style[\s\S]*?</style>", " ", body_html)
    clean_text = re.sub(r"<script[\s\S]*?</script>", " ", clean_text)
    clean_text = re.sub(r"<[^>]+>", " ", clean_text)
    clean_text_unescaped = unescape(clean_text)

    checks = []

    # 1. H1 check
    h1_matches = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.DOTALL | re.IGNORECASE)
    h1_clean = [re.sub(r"<[^>]+>", "", h).strip() for h in h1_matches]
    h1_ok = len(h1_matches) == 1
    checks.append({
        "check": "Single H1 heading",
        "pass": h1_ok,
        "detail": f"Found {len(h1_matches)} H1(s): {h1_clean}"
    })

    # 2. H2 count & map
    h2_matches = [unescape(re.sub(r"<[^>]+>", "", h)).strip() for h in re.findall(r"<h2[^>]*>(.*?)</h2>", html, re.DOTALL | re.IGNORECASE)]
    h2_ok = len(h2_matches) >= 8
    checks.append({
        "check": "H2 headings present",
        "pass": h2_ok,
        "detail": f"Found {len(h2_matches)} H2s: {h2_matches}"
    })

    # 3. Verify section ordering: Conclusion before Related Guides, and Related Guides before FAQ
    faq_idx = -1
    conclusion_idx = -1
    related_idx = -1
    for i, h in enumerate(h2_matches):
        hl = h.lower()
        if "frequently asked questions" in hl:
            faq_idx = i
        if "final thoughts" in hl or "conclusion" in hl:
            conclusion_idx = i
        if "more jewellery & buying guides" in hl or "more gold buying guides" in hl:
            related_idx = i

    order_ok = (conclusion_idx != -1 and related_idx != -1 and faq_idx != -1 and conclusion_idx < related_idx < faq_idx)
    checks.append({
        "check": "Section ordering (Conclusion < Related Guides < FAQ)",
        "pass": order_ok,
        "detail": f"Conclusion idx: {conclusion_idx}, Related idx: {related_idx}, FAQ idx: {faq_idx}"
    })

    # 4. Canonical URL
    canonical_match = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    canonical_url = canonical_match.group(1) if canonical_match else ""
    canonical_ok = canonical_url.rstrip("/") == URL.rstrip("/")
    checks.append({
        "check": "Canonical URL exact match",
        "pass": canonical_ok,
        "detail": f"Found canonical: {canonical_url}"
    })

    # 5. Public og:image
    og_img_match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    og_img_url = og_img_match.group(1) if og_img_match else ""
    og_200 = verify_http_200(og_img_url) if og_img_url else False
    checks.append({
        "check": "Public og:image returns HTTP 200",
        "pass": og_200,
        "detail": f"og:image URL: {og_img_url} (HTTP 200: {og_200})"
    })

    # 6. Word count
    words = len(re.findall(r"\b[A-Za-z0-9_]+\b", clean_text))
    word_count_ok = words >= 3000
    checks.append({
        "check": "Visible article word count >= 3,000",
        "pass": word_count_ok,
        "detail": f"Visible words: {words}"
    })

    # 7. 3D Coverflow Carousel DOM check
    cf_container = ".bs-cf" in html
    cf_stage = ".bs-cf-stage" in html
    cf_cards = ".bs-cf-card" in html
    cf_dots = ".bs-cf-dots" in html
    carousel_dom_ok = cf_container and cf_stage and cf_cards and cf_dots
    checks.append({
        "check": "3D Coverflow Carousel DOM markup",
        "pass": carousel_dom_ok,
        "detail": f"Has .bs-cf: {cf_container}, .bs-cf-stage: {cf_stage}, .bs-cf-card: {cf_cards}, .bs-cf-dots: {cf_dots}"
    })

    # 8. Carousel Card Images HTTP 200 pre-flight check
    stage_match = re.search(r'<div class="bs-cf-stage">([\s\S]*?)</div>\s*<div class="bs-cf-dots"', html)
    carousel_img_matches = re.findall(r'<img [^>]*src=[\"\']([^\"\']+)[\"\']', stage_match.group(1)) if stage_match else []
    carousel_imgs_200 = True
    c_img_details = []
    for c_url in carousel_img_matches:
        is_ok = verify_http_200(c_url)
        c_img_details.append(f"{c_url} -> {is_ok}")
        if not is_ok:
            carousel_imgs_200 = False
    checks.append({
        "check": "All carousel card images HTTP 200",
        "pass": carousel_imgs_200 and len(carousel_img_matches) == 6,
        "detail": f"Checked {len(carousel_img_matches)} images: {c_img_details}"
    })

    # 9. Type 3 In-Body Images check (flatlay & lifestyle present, hero not in body prose as img)
    flatlay_in_body = "finger-rings-for-girls-flatlay-2026.webp" in body_html
    lifestyle_in_body = "finger-rings-for-girls-lifestyle-2026.webp" in body_html
    hero_img_in_body = bool(re.search(r'<img[^>]*src=[\"\'][^\"\']*finger-rings-for-girls-hero-2026\.webp', body_html))
    type3_placement_ok = flatlay_in_body and lifestyle_in_body and not hero_img_in_body
    checks.append({
        "check": "Type 3 in-body placement (flatlay & lifestyle present, hero not in body prose)",
        "pass": type3_placement_ok,
        "detail": f"Flatlay in body: {flatlay_in_body}, Lifestyle in body: {lifestyle_in_body}, Hero img in body: {hero_img_in_body}"
    })

    # 10. Clean Figcaption Check
    figcaptions = re.findall(r"<figcaption>(.*?)</figcaption>", body_html, re.DOTALL)
    clean_captions_ok = len(figcaptions) >= 2
    checks.append({
        "check": "Clean editorial figcaptions present",
        "pass": clean_captions_ok,
        "detail": f"Found {len(figcaptions)} figcaption(s): {figcaptions}"
    })

    # 11. Visible FAQ Q&As in DOM
    faq_q_count = len(re.findall(r"<strong>Q\d+:", html))
    faq_ok = 5 <= faq_q_count <= 10
    checks.append({
        "check": "Visible FAQ Q&A pairs (5 to 10)",
        "pass": faq_ok,
        "detail": f"Found {faq_q_count} visible FAQ questions in DOM"
    })

    # 12. Schema validation (BlogPosting & FAQPage)
    has_blogposting = '"@type": "BlogPosting"' in html or '"@type":"BlogPosting"' in html
    has_faqpage = '"@type": "FAQPage"' in html or '"@type":"FAQPage"' in html
    schema_ok = has_blogposting and has_faqpage
    checks.append({
        "check": "JSON-LD Schemas (BlogPosting & FAQPage)",
        "pass": schema_ok,
        "detail": f"BlogPosting: {has_blogposting}, FAQPage: {has_faqpage}"
    })

    # 13. Author & Byline
    has_byline = "Satyam, BlueStone Editorial" in html
    checks.append({
        "check": "Author on-page byline",
        "pass": has_byline,
        "detail": f"Byline present: {has_byline}"
    })

    # 14. Prohibited characters check (in body HTML)
    em_dash_count = body_html.count("—")
    en_dash_count = body_html.count("–")
    spaced_hyphens = len(re.findall(r"\s-\s", clean_text))
    price_symbols = len(re.findall(r"₹\s*\d+|Rs\.?\s*\d+", clean_text))
    has_raw_table = "<table" in body_html or "<!-- wp:table" in body_html
    prohibited_ok = (em_dash_count == 0 and en_dash_count == 0 and spaced_hyphens == 0 and price_symbols == 0 and not has_raw_table)
    checks.append({
        "check": "Zero prohibited characters in body (no em/en dashes, no spaced hyphens, no prices, no tables)",
        "pass": prohibited_ok,
        "detail": f"Em dashes: {em_dash_count}, En dashes: {en_dash_count}, Spaced hyphens: {spaced_hyphens}, Prices: {price_symbols}, Tables: {has_raw_table}"
    })

    # 15. Dedicated Related Guides Section (Internal Blog Cluster Links)
    cluster_links = [
        "how-to-check-gold-purity-2026",
        "gst-on-gold-jewellery-in-india-what-youre-actually-paying-in-tax",
        "is-buying-gold-jewellery-online-safe-in-india-the-honest-answer",
        "stackable-rings-2026",
        "hand-bracelet-for-girls-2026"
    ]
    matched_links = [cl for cl in cluster_links if cl in html]
    cluster_ok = len(matched_links) >= 4
    checks.append({
        "check": "Internal Blog Cluster Links (>=4 guides)",
        "pass": cluster_ok,
        "detail": f"Found {len(matched_links)} cluster links: {matched_links}"
    })

    all_passed = all(c["pass"] for c in checks)
    print("\n================ LIVE QA REPORT ================")
    for c in checks:
        status_sym = "PASS" if c["pass"] else "FAIL"
        print(f"[{status_sym}] {c['check']}: {c['detail']}")
    print(f"OVERALL STATUS: {'PASS' if all_passed else 'FAIL'}")
    print("================================================\n")

    report_path = ROOT / "output/Week8_Rank178_FingerRingsForGirls_live_qa_report.json"
    report_data = {
        "url": URL,
        "post_id": POST_ID,
        "overall_status": "PASS" if all_passed else "FAIL",
        "visible_word_count": words,
        "checks": checks
    }
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2)
    print(f"Saved full Live QA report to {report_path}")

    return all_passed


if __name__ == "__main__":
    passed = run_qa()
    if not passed:
        sys.exit(1)
