#!/usr/bin/env python3
"""Patch Type 3 WebP images into WordPress post 40310 for Ruby Earrings."""
import json, os, re, base64, urllib.request
from pathlib import Path
from PIL import Image

with open('.env') as f:
    env = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

wp_user = env['WP_USER'].strip('\"\'')
wp_pass = env['WP_APP_PASSWORD'].strip('\"\'')
auth_header = 'Basic ' + base64.b64encode((wp_user + ':' + wp_pass).encode()).decode()

headers = {'Authorization': auth_header, 'User-Agent': 'Mozilla/5.0'}
api_base = 'https://blog.bluestone.com/wp-json/wp/v2'
post_id = 40310

with open('output/Week9_Rank76_RubyEarrings_type3_prompts.json', encoding='utf-8') as f:
    manifest = json.load(f)

# 1. Prepare WebPs from raw PNGs
output_dir = Path('output/magnific_generated')
slots = ['hero', 'flatlay', 'lifestyle']
media_info = {}

for slot in slots:
    webp_path = Path(manifest['output'][slot])
    raw_path = webp_path.with_suffix('.raw.png')
    
    if not webp_path.exists():
        if not raw_path.exists():
            raise FileNotFoundError(f"Missing raw image for {slot}: {raw_path}")
        im = Image.open(raw_path).convert('RGB')
        if im.width > 1400:
            h = round(im.height * 1400 / im.width)
            im = im.resize((1400, h), Image.Resampling.LANCZOS)
        webp_path.parent.mkdir(parents=True, exist_ok=True)
        im.save(webp_path, 'WEBP', quality=82, method=6)
        print(f"Converted {raw_path} -> {webp_path}")
    else:
        print(f"Reusing existing {webp_path}")

    slot_cfg = manifest['slots'][slot]
    alt_text = slot_cfg['alt']
    title_text = f"Ruby earrings 2026 {slot.title()} \u2014 {slot_cfg['product_name']}"

    # Upload to WordPress
    upload_headers = dict(headers)
    upload_headers['Content-Disposition'] = f'attachment; filename=\"{webp_path.name}\"'
    upload_headers['Content-Type'] = 'image/webp'

    req = urllib.request.Request(f'{api_base}/media', data=webp_path.read_bytes(), headers=upload_headers, method='POST')
    with urllib.request.urlopen(req) as resp:
        m_data = json.loads(resp.read().decode())
        mid = m_data['id']
        msrc = m_data['source_url']

    # Update alt & title
    update_data = json.dumps({'alt_text': alt_text, 'title': title_text}).encode()
    req_update = urllib.request.Request(f'{api_base}/media/{mid}', data=update_data, headers={'Authorization': auth_header, 'Content-Type': 'application/json'}, method='POST')
    with urllib.request.urlopen(req_update) as resp:
        pass

    media_info[slot] = {
        'id': mid,
        'src': msrc,
        'alt': alt_text,
        'title': title_text,
        'pdp': slot_cfg['pdp'],
        'caption': slot_cfg.get('caption', '')
    }
    print(f"Uploaded {slot}: ID {mid} -> {msrc}")

with open('output/Week9_Rank76_type3_uploaded_media.json', 'w') as f:
    json.dump(media_info, f, indent=2)

# 2. Fetch current post content
req_post = urllib.request.Request(f'{api_base}/posts/{post_id}?context=edit', headers=headers)
with urllib.request.urlopen(req_post) as resp:
    curr_post = json.loads(resp.read().decode())

curr_content = curr_post['content']['raw']

# Build Gutenberg Image Block with Custom PDP Link & Clean Figcaption
def make_custom_image_block(mid, src, alt, pdp_url, caption):
    return (
        f'<!-- wp:image {{"id":{mid},"sizeSlug":"full","linkDestination":"custom"}} -->\n'
        f'<figure class="wp-block-image size-full">'
        f'<a href="{pdp_url}">'
        f'<img src="{src}" alt="{alt}" class="wp-image-{mid}"/>'
        f'</a>'
        f'<figcaption>{caption}</figcaption>'
        f'</figure>\n<!-- /wp:image -->'
    )

flatlay_block = make_custom_image_block(
    media_info['flatlay']['id'],
    media_info['flatlay']['src'],
    media_info['flatlay']['alt'],
    media_info['flatlay']['pdp'],
    media_info['flatlay']['caption']
)

lifestyle_block = make_custom_image_block(
    media_info['lifestyle']['id'],
    media_info['lifestyle']['src'],
    media_info['lifestyle']['alt'],
    media_info['lifestyle']['pdp'],
    media_info['lifestyle']['caption']
)

# 3. Replace placeholders precisely
if '<!-- TYPE3_FLATLAY_PLACEHOLDER -->' not in curr_content:
    raise ValueError("Missing TYPE3_FLATLAY_PLACEHOLDER in post content!")
if '<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->' not in curr_content:
    raise ValueError("Missing TYPE3_LIFESTYLE_PLACEHOLDER in post content!")

patched_content = curr_content.replace('<!-- TYPE3_FLATLAY_PLACEHOLDER -->', flatlay_block)
patched_content = patched_content.replace('<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->', lifestyle_block)

# 4. Update BlogPosting schema image array
image_array = [
    media_info['hero']['src'],
    media_info['flatlay']['src'],
    media_info['lifestyle']['src']
]

schema_img_pattern = r'\"@type\":\s*\"BlogPosting\",.*?(?=\"mainEntityOfPage\")'
# Let's inspect where BlogPosting schema is
img_json_str = json.dumps(image_array, indent=4)
patched_content = re.sub(
    r'(\"@type\":\s*\"BlogPosting\",\s*\n\s*\"headline\":[^\n]+,\s*\n\s*\"description\":[^\n]+,)',
    r'\1\n  "image": ' + json.dumps(image_array) + ',',
    patched_content
)

# 5. Push update to WordPress
patch_payload = {
    'featured_media': media_info['hero']['id'],
    'content': patched_content,
    'meta': {
        '_yoast_wpseo_opengraph-image': media_info['hero']['src'],
        '_yoast_wpseo_opengraph-image-id': media_info['hero']['id'],
        '_yoast_wpseo_twitter-image': media_info['hero']['src'],
        '_yoast_wpseo_twitter-image-id': media_info['hero']['id']
    }
}

req_update_post = urllib.request.Request(
    f'{api_base}/posts/{post_id}',
    data=json.dumps(patch_payload).encode('utf-8'),
    headers=headers,
    method='POST'
)

with urllib.request.urlopen(req_update_post) as resp:
    res = json.loads(resp.read().decode())
    print(f"SUCCESS: Post {post_id} updated with featured_media {res.get('featured_media')}")

