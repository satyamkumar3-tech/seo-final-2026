#!/usr/bin/env python3
"""SERP Intelligence Scraper for Week 9 Rank 83 - White Stone Necklace Gold."""
import urllib.request
import re
from html.parser import HTMLParser
import json
from pathlib import Path

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
    ("1", "https://www.caratlane.com/jewellery/white+stone+necklace+sets.html", "caratlane.com"),
    ("2", "https://www.candere.com/jewellery/white-stone-necklace-gold.html", "candere.com"),
    ("3", "https://www.candere.com/jewellery/white-stone-necklace.html", "candere.com"),
    ("4", "https://www.myntra.com/white-stone-necklace", "myntra.com"),
    ("5", "https://www.melorra.com/jewellery/necklaces/", "melorra.com")
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

scraped_data = []

for pos, url, domain in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
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
                "word_count": word_count,
                "h1s": parser.h1s,
                "h2s": parser.h2s,
                "h3s": parser.h3s,
                "text_snippet": full_text[:1200]
            })
    except Exception as e:
        print(f"SERP_SCRAPED: {pos} | {url} | {domain} | ERR: {e}")

# Save raw output
out_path = Path("output/week9_rank83_serp_data.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(scraped_data, f, indent=2)

print(f"Saved raw scraped data to {out_path}")
