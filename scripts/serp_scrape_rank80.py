#!/usr/bin/env python3
"""SERP Intelligence Scraper for Week 9 Rank 80 - Multicolor Earrings."""
import urllib.request
import re
from html.parser import HTMLParser

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.h2s = []
        self.h3s = []
        self.in_h2 = False
        self.in_h3 = False
        self.in_title = False
        self.title = ""
        self.curr_h2 = []
        self.curr_h3 = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == "h2":
            self.in_h2 = True
            self.curr_h2 = []
        elif tag == "h3":
            self.in_h3 = True
            self.curr_h3 = []
        elif tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "h2":
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
        self.text_parts.append(data)
        if self.in_h2:
            self.curr_h2.append(data)
        if self.in_h3:
            self.curr_h3.append(data)
        if self.in_title:
            self.title += data

urls = [
    ("1", "https://www.caratlane.com/jewellery/multicolored+stone+earrings.html", "caratlane.com"),
    ("2", "https://www.myntra.com/multicolor-earrings", "myntra.com"),
    ("3", "https://www.mirraw.com/women/jewellery/earrings/multicolor-earrings", "mirraw.com"),
    ("4", "https://blingbag.co.in/collections/multi-colour-earrings", "blingbag.co.in"),
    ("5", "https://jewelzindia.in/collections/multi-colour-earrings", "jewelzindia.in"),
]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

results = []
total_words = 0

for pos, url, domain in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            parser = PageParser()
            parser.feed(html)
            clean_text = " ".join(parser.text_parts)
            clean_text = re.sub(r"\s+", " ", clean_text)
            words = len(clean_text.split())
            total_words += words
            h2_count = len(parser.h2s)
            results.append({
                "pos": pos,
                "url": url,
                "domain": domain,
                "words": words,
                "h2_count": h2_count,
                "title": parser.title.strip(),
                "h2s": parser.h2s,
                "h3s": parser.h3s
            })
            print(f"SERP_SCRAPED: {pos} | {url} | {domain} | {words} | {h2_count}")
    except Exception as e:
        print(f"Error scraping {url}: {e}")

avg_words = int(total_words / len(results)) if results else 0
print(f"\nAVERAGE_WORD_COUNT: {avg_words}")
print(f"TOTAL_URLS_SCRAPED: {len(results)}")
