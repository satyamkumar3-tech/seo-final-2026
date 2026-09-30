#!/usr/bin/env python3
"""Comprehensive Live QA script for Week 9 Rank 76: Ruby Earrings."""
import urllib.request, re, json

url = "https://blog.bluestone.com/ruby-earrings-2026/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode("utf-8", errors="ignore")

results = {}

# 1. H1 count
h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
results["h1_count"] = len(h1s)
results["h1_text"] = [re.sub(r'<[^>]+>', '', h).strip() for h in h1s]

# 2. Canonical
m_canon = re.search(r'<link rel=\"canonical\" href=\"([^\"]+)\"', html)
results["canonical"] = m_canon.group(1) if m_canon else None

# 3. OG Image
m_og = re.search(r'<meta property=\"og:image\" content=\"([^\"]+)\"', html)
results["og_image"] = m_og.group(1) if m_og else None
if results["og_image"]:
    head_req = urllib.request.Request(results["og_image"], headers=headers, method="HEAD")
    with urllib.request.urlopen(head_req, timeout=10) as head_resp:
        results["og_image_status"] = head_resp.status
else:
    results["og_image_status"] = None

# 4. H2 headings
h2s = re.findall(r'<h2[^>]*class=\"[^\"]*wp-block-heading[^\"]*\"[^>]*>(.*?)</h2>', html, re.DOTALL | re.IGNORECASE)
if not h2s:
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL | re.IGNORECASE)
results["h2_count"] = len(h2s)
results["h2_list"] = [re.sub(r'<[^>]+>', '', h).strip() for h in h2s]

# 5. Visible word count
# Extract main content between article tags
m_article = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
article_html = m_article.group(1) if m_article else html

no_s = re.sub(r'<script[^>]*>.*?</script>', ' ', article_html, flags=re.DOTALL | re.IGNORECASE)
no_st = re.sub(r'<style[^>]*>.*?</style>', ' ', no_s, flags=re.DOTALL | re.IGNORECASE)
text = re.sub(r'<[^>]+>', ' ', no_st)
words = re.findall(r'\b\w+\b', text)
results["visible_word_count"] = len(words)

# 6. Carousel verification
results["has_bs_cf"] = "bs-cf" in html
results["has_bs_cf_stage"] = "bs-cf-stage" in html
results["has_bs_cf_card"] = "bs-cf-card" in html
results["has_bs_cf_dots"] = "bs-cf-dots" in html

card_imgs = re.findall(r'<div class=\"bs-cf-card[^\"]*\".*?<img src=\"([^\"]+)\"', html, re.DOTALL)
results["carousel_card_count"] = len(card_imgs)
results["carousel_img_urls"] = card_imgs
carousel_statuses = []
for c_url in card_imgs:
    try:
        h_req = urllib.request.Request(c_url, headers=headers, method="HEAD")
        with urllib.request.urlopen(h_req, timeout=10) as c_resp:
            carousel_statuses.append(c_resp.status)
    except Exception as e:
        carousel_statuses.append(str(e))
results["carousel_http_statuses"] = carousel_statuses

# 7. Type 3 in-body images
img_figures = re.findall(r'<figure class=\"[^\"]*wp-block-image[^\"]*\">(.*?)</figure>', article_html, re.DOTALL | re.IGNORECASE)
results["in_body_image_count"] = len(img_figures)
in_body_details = []
for fig in img_figures:
    src = re.search(r'src=\"([^\"]+)\"', fig)
    alt = re.search(r'alt=\"([^\"]+)\"', fig)
    link = re.search(r'<a href=\"([^\"]+)\"', fig)
    cap = re.search(r'<figcaption>(.*?)</figcaption>', fig, re.DOTALL)
    in_body_details.append({
        "src": src.group(1) if src else None,
        "alt": alt.group(1) if alt else None,
        "link": link.group(1) if link else None,
        "caption": cap.group(1).strip() if cap else None
    })
results["in_body_images"] = in_body_details

# 8. Check for dashes in article text
results["em_dashes"] = text.count("—")
results["en_dashes"] = text.count("–")
results["spaced_hyphens"] = len(re.findall(r'\b\w+\s+-\s+\w+\b', text))

# 9. Check for prices
results["price_symbols"] = len(re.findall(r'₹|\bRs\.?\s*\d+', text))

# 10. Check tables
results["has_table"] = "<table" in article_html or "wp-block-table" in article_html

# 11. FAQs count
faq_headings = [h for h in re.findall(r'<h3[^>]*>(.*?)</h3>', article_html, re.DOTALL | re.IGNORECASE) if '?' in h]
results["faq_count"] = len(faq_headings)
results["faq_questions"] = [re.sub(r'<[^>]+>', '', h).strip() for h in faq_headings]

# 12. Author & byline
results["has_satyam_byline"] = "By Satyam, BlueStone Editorial" in article_html or "Satyam" in html

# 13. Schemas
results["has_faq_schema"] = '"@type": "FAQPage"' in html or '"@type":"FAQPage"' in html
results["has_blogposting_schema"] = '"@type": "BlogPosting"' in html or '"@type":"BlogPosting"' in html

print(json.dumps(results, indent=2))
