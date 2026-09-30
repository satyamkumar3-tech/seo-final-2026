import urllib.request, re, json

url = 'https://blog.bluestone.com/womens-gold-necklace-design-2026/?v=1'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
with urllib.request.urlopen(req, timeout=30) as resp:
    html = resp.read().decode('utf-8')

print('--- LIVE QA AUDIT ---')

# 1. H1 count
h1_matches = re.findall(r'<h1\b[^>]*>(.*?)</h1>', html, re.I | re.DOTALL)
print(f'H1 count: {len(h1_matches)}')
for h in h1_matches:
    print('  H1 text:', re.sub(r'<[^>]+>', '', h).strip())
assert len(h1_matches) == 1, 'Expected exactly 1 H1'

# 2. Canonical
canonical_match = re.search(r'<link\s+rel=[\'"]canonical[\'"]\s+href=[\'"](.*?)[\'"]', html, re.I)
canonical = canonical_match.group(1) if canonical_match else None
print('Canonical URL:', canonical)
assert canonical and 'womens-gold-necklace-design-2026' in canonical, 'Canonical mismatch'

# 3. OG Image
og_match = re.search(r'<meta\s+property=[\'"]og:image[\'"]\s+content=[\'"](.*?)[\'"]', html, re.I)
og_img = og_match.group(1) if og_match else None
print('OG Image:', og_img)
assert og_img and 'womens-gold-necklace-design-hero-2026.webp' in og_img, 'OG Image mismatch'

# 4. H2 tags
h2_matches = re.findall(r'<h2\b[^>]*>(.*?)</h2>', html, re.I | re.DOTALL)
print(f'H2 count: {len(h2_matches)}')
for h in h2_matches:
    print('  H2:', re.sub(r'<[^>]+>', '', h).strip())

# 5. Buy now links
buy_links = re.findall(r'>Buy now<', html)
print(f'Buy now links count: {len(buy_links)}')
assert len(buy_links) == 6, f'Expected 6 Buy now links, found {len(buy_links)}'

# 6. Visible word count
body_html = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', html, flags=re.I | re.DOTALL)
text_clean = re.sub(r'<[^>]+>', ' ', body_html)
words = re.findall(r'\b\w+\b', text_clean)
print(f'Total page word count: {len(words)}')
assert len(words) >= 1500, 'Word count too low'

# 7. Prohibitions
assert '—' not in text_clean, 'Em dash found'
assert '–' not in text_clean, 'En dash found'
assert not re.search(r'\b\w+\s+-\s+\w+\b', text_clean), 'Spaced hyphen found'
assert not re.search(r'(?:₹|\bRs\.?\s*\d|\bINR\s*\d)', text_clean, re.I), 'Price pattern found'

# 8. Schema verification
json_ld_blocks = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"][^>]*>(.*?)</script>', html, re.I | re.DOTALL)
print(f'JSON-LD scripts found: {len(json_ld_blocks)}')
faq_found = False
blog_found = False
for block in json_ld_blocks:
    try:
        data = json.loads(block.strip())
        if data.get('@type') == 'FAQPage':
            faq_found = True
            print(f'  FAQPage questions: {len(data.get("mainEntity", []))}')
        if data.get('@type') == 'BlogPosting':
            blog_found = True
            print(f'  BlogPosting headline: {data.get("headline")}')
            print(f'  BlogPosting author: {data.get("author")}')
            print(f'  BlogPosting images count: {len(data.get("image", []))}')
    except Exception as e:
        pass

assert faq_found, 'FAQPage schema not found'
assert blog_found, 'BlogPosting schema not found'

print('ALL QA CHECKS PASSED PERFECTLY!')
