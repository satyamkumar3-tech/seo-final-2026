#!/usr/bin/env python3
"""Fix quote errors and clean Gutenberg block syntax for post 37764 (Bow Earrings Buying Guide 2026)."""
import os
import re
import json
import base64
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Load local environment
def load_env():
    env_file = ROOT / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

load_env()
USER = os.environ.get("WP_USER", "")
PWD = os.environ.get("WP_APP_PASSWORD", "")
TOKEN = base64.b64encode(f"{USER}:{PWD}".encode()).decode() if USER and PWD else ""
AUTH_HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0",
    "Content-Type": "application/json"
}
WP_API = "https://blog.bluestone.com/wp-json/wp/v2"
POST_ID = 37764

def fetch_post(post_id):
    req = urllib.request.Request(f"{WP_API}/posts/{post_id}?context=edit", headers=AUTH_HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())

def update_post(post_id, content):
    data = json.dumps({"content": content}).encode()
    req = urllib.request.Request(f"{WP_API}/posts/{post_id}", data=data, headers=AUTH_HEADERS, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())

def clean_content(raw_text):
    lines = raw_text.split("\n")
    cleaned_lines = []
    
    for line in lines:
        l = line
        # Strip leading escape and quote if present
        if l.startswith("\\'"):
            l = l[2:]
        elif l.startswith("'"):
            l = l[1:]
        # Strip trailing quote if present
        if l.endswith("'"):
            l = l[:-1]
        cleaned_lines.append(l)
        
    cleaned_text = "\n".join(cleaned_lines)
    return cleaned_text

def main():
    post = fetch_post(POST_ID)
    title = post.get("title", {}).get("raw", "")
    content = post.get("content", {}).get("raw", "")
    print(f"Fetched post ID {POST_ID}: {title}")
    print(f"Original raw length: {len(content)} chars")
    
    cleaned_text = clean_content(content)
    print(f"Cleaned raw length: {len(cleaned_text)} chars")
    
    # Audit Gutenberg blocks
    p_open = len(re.findall(r"<!-- wp:paragraph.*?-->", cleaned_text))
    p_close = len(re.findall(r"<!-- /wp:paragraph -->", cleaned_text))
    h_open = len(re.findall(r"<!-- wp:heading.*?-->", cleaned_text))
    h_close = len(re.findall(r"<!-- /wp:heading -->", cleaned_text))
    l_open = len(re.findall(r"<!-- wp:list.*?-->", cleaned_text))
    l_close = len(re.findall(r"<!-- /wp:list -->", cleaned_text))
    img_open = len(re.findall(r"<!-- wp:image.*?-->", cleaned_text))
    img_close = len(re.findall(r"<!-- /wp:image -->", cleaned_text))
    html_open = len(re.findall(r"<!-- wp:html -->", cleaned_text))
    html_close = len(re.findall(r"<!-- /wp:html -->", cleaned_text))
    
    print(f"Paragraph blocks: {p_open} open, {p_close} close")
    print(f"Heading blocks: {h_open} open, {h_close} close")
    print(f"List blocks: {l_open} open, {l_close} close")
    print(f"Image blocks: {img_open} open, {img_close} close")
    print(f"HTML blocks: {html_open} open, {html_close} close")
    
    assert p_open == p_close, "Mismatched paragraph blocks!"
    assert h_open == h_close, "Mismatched heading blocks!"
    assert l_open == l_close, "Mismatched list blocks!"
    assert img_open == img_close, "Mismatched image blocks!"
    assert html_open == html_close, "Mismatched HTML blocks!"
    
    updated = update_post(POST_ID, cleaned_text)
    print(f"SUCCESS: Post {POST_ID} updated successfully!")
    print(f"Live URL: {updated.get('link')}")

if __name__ == "__main__":
    main()
