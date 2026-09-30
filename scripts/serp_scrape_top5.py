#!/usr/bin/env python3
"""Scrape top 5 organic ranking URLs for 'multicolor earrings'."""
import urllib.request
import re
from html.parser import HTMLParser

class SerpParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.h1s = []
        self.h2s = []
        self.h3s = []
        self.curr_tag = None
        self.curr_text = []
        self.title = ""
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in ["h1", "h2", "h3", "p", "li", "title"]:
            self.curr_tag = tag
            self.curr_text = []
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        tag = tag.lower()
        content = " ".join(self.curr_text).strip()
        if tag == "h1" and content:
            self.h1s.append(content)
        elif tag == "h2" and content:
            self.h2s.append(content)
        elif tag == "h3" and content:
            self.h3s.append(content)
        elif tag == "title":
            self.in_title = False
            self.title = content
        self.curr_tag = None

    def handle_data(self, data):
        data_clean = data.strip()
        if data_clean:
            self.text_parts.append(data_clean)
            if self.curr_tag:
                self.curr_text.append(data_clean)

urls = [
    ("1", "https://www.caratlane.com/jewellery/multicolored+stone+earrings.html", "caratlane.com"),
    ("2", "https://www.myntra.com/multicolor-earrings", "myntra.com"),
    ("3", "https://www.mirraw.com/women/jewellery/earrings/multicolor-earrings", "mirraw.com"),
    ("4", "https://www.voylla.com/collections/women-earrings", "voylla.com"),
    ("5", "https://www.kushals.com/collections/earrings", "kushals.com")
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

results = []
for pos, url, domain in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            parser = SerpParser()
            parser.feed(html)
            full_text = " ".join(parser.text_parts)
            word_count = len(full_text.split())
            h2_count = len(parser.h2s)
            results.append({
                "pos": pos,
                "url": url,
                "domain": domain,
                "word_count": word_count,
                "h2_count": h2_count,
                "title": parser.title,
                "h2s": parser.h2s,
                "h3s": parser.h3s[:10]
            })
            print(f"SERP_SCRAPED: {pos} | {url} | {domain} | {word_count} | {h2_count}")
    except Exception as e:
        print(f"Error scraping pos {pos} ({url}): {e}")

avg_words = sum(r["word_count"] for r in results) // len(results) if results else 0
print(f"\nTotal Scraped: {len(results)}")
print(f"Average Word Count: {avg_words}")

# Save results for synthesis
import json
with open("output/serp_rank80_analysis.json", "w", encoding="utf-8") as f:
    json.dump({"results": results, "avg_words": avg_words}, f, indent=2)
