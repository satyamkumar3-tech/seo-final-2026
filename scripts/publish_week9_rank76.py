#!/usr/bin/env python3
"""Publish Week 9 Rank 76 to WordPress."""
import json, os, base64, urllib.request

with open('.env') as f:
    env = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

wp_user = env['WP_USER'].strip('\"\'')
wp_pass = env['WP_APP_PASSWORD'].strip('\"\'')
auth_header = 'Basic ' + base64.b64encode((wp_user + ':' + wp_pass).encode()).decode()

headers = {
    'Authorization': auth_header,
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}
api_base = 'https://blog.bluestone.com/wp-json/wp/v2'

with open('output/week9_rank76_draft.json', encoding='utf-8') as f:
    draft = json.load(f)

slug = draft['slug']

# 1. Exact slug check before creating
req_check = urllib.request.Request(f'{api_base}/posts?slug={slug}', headers=headers)
with urllib.request.urlopen(req_check) as resp:
    existing = json.loads(resp.read().decode())
    if existing:
        print(f"Post with slug {slug} already exists! ID: {existing[0]['id']}")
        with open('output/week9_rank76_published_post.json', 'w') as out_f:
            json.dump(existing[0], out_f, indent=2)
        exit(0)

# 2. Create post
post_payload = {
    'title': draft['title'],
    'slug': slug,
    'status': 'publish',
    'author': draft['author_id'],
    'categories': draft['categories'],
    'excerpt': draft['meta_desc'],
    'content': draft['content'],
    'meta': {
        '_yoast_wpseo_focuskw': draft['focus_kw'],
        '_yoast_wpseo_title': draft['yoast_title'],
        '_yoast_wpseo_metadesc': draft['meta_desc']
    }
}

req_create = urllib.request.Request(
    f'{api_base}/posts',
    data=json.dumps(post_payload).encode('utf-8'),
    headers=headers,
    method='POST'
)

with urllib.request.urlopen(req_create) as resp:
    post_res = json.loads(resp.read().decode())
    post_id = post_res['id']
    post_url = post_res['link']
    print(f"SUCCESS: Post created with ID {post_id} at {post_url}")
    with open('output/week9_rank76_published_post.json', 'w') as out_f:
        json.dump(post_res, out_f, indent=2)

