#!/usr/bin/env python3
"""Comprehensive Live QA audit for Week 7 Rank 156 using standard library."""
import urllib.request
import json
import re
from html import unescape

URL = "https://blog.bluestone.com/platinum-necklace-2026/"
POST_ID = 36380

print(f"=== Running Live QA for {URL} (Post ID: {POST_ID}) ===")

# 1. Fetch public HTML
req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
with urllib.request.urlopen(req, timeout=30) as resp:
    status_code = resp.status
    html = resp.read().decode("utf-8")

print(f"1. HTTP Status: {status_code} OK")
assert status_code == 200

# 2. Canonical & og:image
canonical_match = re.search(r'<link rel=["\']canonical["\'] href=["\']([^"\']+)["\']', html)
canonical_href = canonical_match.group(1) if canonical_match else None
print(f"2. Canonical URL: {canonical_href}")
assert canonical_href == URL

og_img_match = re.search(r'<meta property=["\']og:image["\'] content=["\']([^"\']+)["\']', html)
og_img_src = og_img_match.group(1) if og_img_match else None
print(f"3. Public og:image: {og_img_src}")
assert "platinum-necklace-hero-2026.webp" in (og_img_src or "")

# 3. Headings & Hierarchy
h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
print(f"4. H1 count: {len(h1s)}")
for h in h1s:
    clean_h1 = re.sub(r"<[^>]+>", "", h).strip()
    print(f"   H1: {clean_h1}")
assert len(h1s) == 1

h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
print(f"5. H2 count: {len(h2s)}")
h2_texts = [re.sub(r"<[^>]+>", "", h).strip() for h in h2s]
for idx, h2_t in enumerate(h2_texts):
    print(f"   H2 #{idx+1}: {h2_t}")

# Section ordering check: Final Thoughts must be BEFORE FAQs
final_thoughts_idx = -1
faq_idx = -1
for idx, h2_t in enumerate(h2_texts):
    if "final thoughts" in h2_t.lower() or "conclusion" in h2_t.lower():
        final_thoughts_idx = idx
    if "frequently asked questions" in h2_t.lower() or "faq" in h2_t.lower():
        faq_idx = idx

print(f"6. Section Ordering: Final Thoughts H2 #{final_thoughts_idx+1} < FAQs H2 #{faq_idx+1}")
assert final_thoughts_idx >= 0 and faq_idx >= 0
assert final_thoughts_idx < faq_idx, "Final Thoughts MUST precede FAQs!"

# 4. Word count & Visible Content
clean_text = re.sub(r"<style[\s\S]*?</style>", " ", html)
clean_text = re.sub(r"<script[\s\S]*?</script>", " ", clean_text)
clean_text = re.sub(r"<header[\s\S]*?</header>", " ", clean_text)
clean_text = re.sub(r"<footer[\s\S]*?</footer>", " ", clean_text)
clean_text = re.sub(r"<nav[\s\S]*?</nav>", " ", clean_text)
clean_text = re.sub(r"<[^>]+>", " ", clean_text)
clean_text = unescape(clean_text)

words = re.findall(r"\b\w+\b", clean_text)
print(f"7. Visible Word Count: {len(words)} words")
assert len(words) >= 2000

# 5. Prohibited Syntax Check
# Fetch post body specifically from REST API to verify prose
req_wp = urllib.request.Request(f"https://blog.bluestone.com/wp-json/wp/v2/posts/{POST_ID}", headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req_wp) as resp_wp:
    wp_post = json.loads(resp_wp.read().decode())

post_body_raw = wp_post["content"]["rendered"]
post_body_text = re.sub(r"<style[\s\S]*?</style>", " ", post_body_raw)
post_body_text = re.sub(r"<script[\s\S]*?</script>", " ", post_body_text)
post_body_text = re.sub(r"<[^>]+>", " ", post_body_text)
post_body_text = unescape(post_body_text)

em_dashes = len(re.findall(r"—", post_body_text))
en_dashes = len(re.findall(r"–", post_body_text))
spaced_hyphens = len(re.findall(r" - ", post_body_text))
prices = len(re.findall(r"₹|\bRs\.?\b|\bINR\b|\$\d+", post_body_text))

print(f"8. Prohibited Syntax in body: em dashes={em_dashes}, en dashes={en_dashes}, spaced hyphens={spaced_hyphens}, prices={prices}")
assert em_dashes == 0
assert en_dashes == 0
assert spaced_hyphens == 0
assert prices == 0

# 6. Carousel verification
has_carousel = "id=\"bs-cf-platinum-necklace\"" in html
cards = re.findall(r'class="bs-cf-card"', html)
print(f"9. Carousel Present: {has_carousel}, Card Count: {len(cards)}")
assert has_carousel
assert len(cards) == 6

# 7. FAQs visible in DOM
h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', html, re.DOTALL)
faq_questions = [re.sub(r"<[^>]+>", "", h).strip() for h in h3s if "?" in h]
print(f"10. Visible FAQ Questions count: {len(faq_questions)}")
for q in faq_questions:
    print(f"    FAQ Q: {q}")
assert len(faq_questions) >= 5

# 8. Schema verification
script_matches = re.findall(r'<script type=["\']application/ld\+json["\']>([\s\S]*?)</script>', html)
print(f"11. JSON-LD scripts count: {len(script_matches)}")
found_faq_schema = False
found_blog_schema = False
for s in script_matches:
    try:
        data = json.loads(s)
        if "@graph" in data:
            for item in data["@graph"]:
                if item.get("@type") == "FAQPage":
                    found_faq_schema = True
                    print(f"    Found FAQPage schema with {len(item.get('mainEntity', []))} questions")
                if item.get("@type") == "BlogPosting":
                    found_blog_schema = True
                    print(f"    Found BlogPosting schema with author: {item.get('author', {}).get('name')}")
                    print(f"    BlogPosting images: {item.get('image')}")
    except Exception as e:
        pass

assert found_faq_schema, "FAQPage schema missing!"
assert found_blog_schema, "BlogPosting schema missing!"

# 9. Verify Hero NOT duplicated in body
body_img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', post_body_raw)
duplicate_hero_in_body = [s for s in body_img_srcs if "platinum-necklace-hero" in s]
print(f"12. In-body duplicate hero count: {len(duplicate_hero_in_body)}")
assert len(duplicate_hero_in_body) == 0, "Hero image is duplicated inside the post body!"

print("\n=== ALL LIVE QA CHECKS PASSED PERFECTLY! ===")
