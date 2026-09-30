import re
import json
import urllib.request
import urllib.parse
from html import unescape

url = "https://blog.bluestone.com/yellow-stone-ring-2026/?v=live_qa_full"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=30) as resp:
    html = resp.read().decode('utf-8')

print("Fetched live HTML length:", len(html))

results = {}

# 1. H1 check
h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
clean_h1s = [re.sub(r'<[^>]+>', '', h1).strip() for h1 in h1_matches]
results["h1_count"] = len(clean_h1s)
results["h1_text"] = clean_h1s[0] if clean_h1s else None

# 2. Canonical URL
canon_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', html, re.IGNORECASE)
results["canonical"] = canon_match.group(1) if canon_match else None

# 3. OG Image
og_img_match = re.search(r'<meta\s+property=["\']og:image["\']\s+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
results["og_image"] = og_img_match.group(1) if og_img_match else None

# 4. Author check
results["has_author_byline"] = "By Satyam, BlueStone Editorial" in html

# 5. Extract article body
m = re.search(r'<div class="entry-content[^\"]*">(.*?)</div><!-- .entry-content -->', html, re.DOTALL)
if not m:
    m = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
content = m.group(1) if m else html

# Dash checks in article body
results["body_em_dashes"] = content.count("—")
results["body_en_dashes"] = content.count("–")

body_text = re.sub(r'<script[^>]*>.*?</script>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
body_text = re.sub(r'<style[^>]*>.*?</style>', ' ', body_text, flags=re.DOTALL | re.IGNORECASE)
body_text = re.sub(r'<[^>]+>', ' ', body_text)
body_words = [w for w in body_text.split() if w]
results["visible_word_count"] = len(body_words)

results["has_spaced_hyphen_in_body"] = bool(re.search(r'\s+-\s+', body_text))

# 6. Price checks in body
price_matches = re.findall(r'(?:₹|Rs\.?|INR)\s*[\d,]+', body_text)
results["price_mentions"] = price_matches

# 7. HTML Tables check
results["has_table_tag"] = "<table" in content.lower()

# 8. 3D Coverflow Carousel check
results["has_bs_cf"] = "bs-cf" in html
results["has_bs_cf_stage"] = "bs-cf-stage" in html
results["has_bs_cf_card"] = "bs-cf-card" in html
results["has_bs_cf_dots"] = "bs-cf-dots" in html

m_cf = re.search(r'<div class="bs-cf".*?</div>\s*<script', html, re.DOTALL)
carousel_imgs = []
if m_cf:
    carousel_imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', m_cf.group(0))

results["carousel_card_count"] = len(carousel_imgs)
results["carousel_image_urls"] = carousel_imgs

carousel_img_statuses = []
for c_url in carousel_imgs:
    # normalize c_url
    clean_url = c_url.split('?')[0] if '?' in c_url else c_url
    head_req = urllib.request.Request(clean_url, headers=headers, method="HEAD")
    try:
        with urllib.request.urlopen(head_req, timeout=15) as head_resp:
            carousel_img_statuses.append((clean_url, head_resp.status))
    except Exception as e:
        carousel_img_statuses.append((clean_url, str(e)))
results["carousel_img_head_checks"] = carousel_img_statuses

# 9. In-body Type 3 images check
figures = re.findall(r'<figure class="wp-block-image[^"]*">(.*?)</figure>', content, re.DOTALL)
type3_figures = []
for f in figures:
    # check if has a link and img
    link_m = re.search(r'<a href="([^"]+)">', f)
    img_m = re.search(r'<img[^>]+src="([^"]+)"[^>]+alt="([^"]+)"', f)
    cap_m = re.search(r'<figcaption>(.*?)</figcaption>', f)
    if link_m and img_m:
        type3_figures.append({
            "pdp_url": link_m.group(1),
            "src": img_m.group(1),
            "alt": img_m.group(2),
            "caption": cap_m.group(1) if cap_m else None
        })
results["type3_in_body_images"] = type3_figures

# Verify HTTP 200 for Type 3 images
type3_head_statuses = []
for img in type3_figures:
    clean_src = img["src"].split('?')[0]
    head_req = urllib.request.Request(clean_src, headers=headers, method="HEAD")
    try:
        with urllib.request.urlopen(head_req, timeout=15) as head_resp:
            type3_head_statuses.append((clean_src, head_resp.status))
    except Exception as e:
        type3_head_statuses.append((clean_src, str(e)))
results["type3_img_head_checks"] = type3_head_statuses

# 10. FAQs check
faq_headings = re.findall(r'<h3[^>]*>(.*?\?)</h3>', html)
results["visible_faq_count"] = len(faq_headings)
results["faq_sample"] = faq_headings[:3]

# 11. Schema checks
schema_matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
schemas = []
for s in schema_matches:
    try:
        schemas.append(json.loads(s.strip()))
    except Exception:
        pass
results["schema_types"] = [s.get("@type") for s in schemas if isinstance(s, dict)]

# 12. Check section ordering
conclusion_idx = html.find("Final Thoughts")
related_idx = html.find("More Jewellery &#038; Buying Guides")
if related_idx == -1:
    related_idx = html.find("More Jewellery &amp; Buying Guides")
if related_idx == -1:
    related_idx = html.find("More Jewellery & Buying Guides")
faq_idx = html.find("Frequently Asked Questions About Yellow Stone Rings")

results["ordering_correct"] = (conclusion_idx != -1 and related_idx != -1 and faq_idx != -1 and conclusion_idx < related_idx < faq_idx)

# Print summary
print("\n--- LIVE QA AUDIT REPORT ---")
for k, v in results.items():
    if k in ["carousel_img_head_checks", "type3_img_head_checks", "type3_in_body_images", "carousel_image_urls"]:
        print(f"{k}:")
        if isinstance(v, list):
            for item in v:
                print(f"  - {item}")
        else:
            print(f"  {v}")
    else:
        print(f"{k}: {v}")

with open("output/Week9_Rank64_live_qa_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nSaved QA results to output/Week9_Rank64_live_qa_results.json")
