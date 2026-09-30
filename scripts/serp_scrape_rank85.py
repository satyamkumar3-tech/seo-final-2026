#!/usr/bin/env python3
"""SERP Intelligence Scraper and Synthesizer for Week 9 Rank 85 - stone necklace for women."""
import urllib.request
import re
import ssl
from html.parser import HTMLParser
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.h1s = []
        self.h2s = []
        self.h3s = []
        self.in_h1 = False
        self.in_h2 = False
        self.in_h3 = False
        self.in_title = False
        self.title = ""
        self.curr_h1 = []
        self.curr_h2 = []
        self.curr_h3 = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == "h1":
            self.in_h1 = True
            self.curr_h1 = []
        elif tag == "h2":
            self.in_h2 = True
            self.curr_h2 = []
        elif tag == "h3":
            self.in_h3 = True
            self.curr_h3 = []
        elif tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "h1":
            self.in_h1 = False
            t = " ".join(self.curr_h1).strip()
            if t:
                self.h1s.append(t)
        elif tag == "h2":
            self.in_h2 = False
            t = " ".join(self.curr_h2).strip()
            if t:
                self.h2s.append(t)
        elif tag == "h3":
            self.in_h3 = False
            t = " ".join(self.curr_h3).strip()
            if t:
                self.h3s.append(t)
        elif tag == "title":
            self.in_title = False

    def handle_data(self, data):
        data_clean = data.strip()
        if data_clean:
            self.text_parts.append(data_clean)
            if self.in_h1:
                self.curr_h1.append(data_clean)
            if self.in_h2:
                self.curr_h2.append(data_clean)
            if self.in_h3:
                self.curr_h3.append(data_clean)
            if self.in_title:
                self.title += " " + data_clean

urls = [
    ("1", "https://www.caratlane.com/jewellery/gemstone-necklaces.html", "caratlane.com"),
    ("2", "https://www.candere.com/jewellery/stone-necklace.html", "candere.com"),
    ("3", "https://www.candere.com/jewellery/gemstone-necklace.html", "candere.com"),
    ("4", "https://www.joyalukkas.in/jewellery/gemstone/necklaces", "joyalukkas.in"),
    ("5", "https://www.melorra.com/jewellery/stone-necklaces/", "melorra.com")
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

scraped_data = []

for pos, url, domain in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            parser = PageParser()
            parser.feed(html)
            
            full_text = " ".join(parser.text_parts)
            words = [w for w in full_text.split() if len(w) > 1]
            word_count = len(words)
            h2_count = len(parser.h2s)
            
            print(f"SERP_SCRAPED: {pos} | {url} | {domain} | {word_count} | {h2_count}")
            
            scraped_data.append({
                "pos": pos,
                "url": url,
                "domain": domain,
                "title": parser.title.strip(),
                "h1s": parser.h1s,
                "h2s": parser.h2s[:10],
                "h3s": parser.h3s[:10],
                "word_count": word_count,
                "h2_count": h2_count
            })
    except Exception as e:
        print(f"ERROR scraping {url}: {e}")

# Calculate averages
total_words = sum(d["word_count"] for d in scraped_data)
avg_word_count = total_words // len(scraped_data) if scraped_data else 0

output_file = ROOT / "output/week9_rank85_serp_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump({
        "scraped": scraped_data,
        "avg_word_count": avg_word_count,
        "urls_scraped": len(scraped_data)
    }, f, indent=2)

print(f"\nSCRAPE SUMMARY: Scraped {len(scraped_data)} URLs, Average word count: {avg_word_count}")
