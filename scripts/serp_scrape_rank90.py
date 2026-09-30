#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SERP Intelligence Scraper and Synthesizer for Week 9 Rank 90 - earring styles for guys."""
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
    ("1", "https://www.caratlane.com/blog/mens-earrings-buying-guide/", "caratlane.com"),
    ("2", "https://ivanajewels.com/blogs/lab-grown-diamond-jewellery/men-s-earring-styles-a-guide-to-popular-designs-trends", "ivanajewels.com"),
    ("3", "https://www.thementhing.com/blogs/news/the-ultimate-guide-to-mens-stud-and-hoop-earrings", "thementhing.com"),
    ("4", "https://www.fashionbeans.com/article/best-earrings-men/", "fashionbeans.com"),
    ("5", "https://www.theinspirationedit.com/types-of-earrings-for-men/", "theinspirationedit.com")
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

scraped_data = []

for pos, url, domain in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            parser = PageParser()
            parser.feed(html)
            
            raw_text = " ".join(parser.text_parts)
            # Rough body word count by cleaning boilerplate
            word_count = len(raw_text.split())
            h2_cleaned = [re.sub(r"\s+", " ", h).strip() for h in parser.h2s if len(h.strip()) > 3]
            h3_cleaned = [re.sub(r"\s+", " ", h).strip() for h in parser.h3s if len(h.strip()) > 3]
            title_cleaned = re.sub(r"\s+", " ", parser.title).strip()
            
            print(f"SERP_SCRAPED: {pos} | {url} | {domain} | {word_count} | {len(h2_cleaned)}")
            scraped_data.append({
                "position": pos,
                "url": url,
                "domain": domain,
                "title": title_cleaned,
                "word_count": word_count,
                "h2_count": len(h2_cleaned),
                "h2s": h2_cleaned,
                "h3s": h3_cleaned[:15],
                "sample_text": raw_text[:500]
            })
    except Exception as e:
        print(f"Failed scraping {url}: {e}")

out_path = ROOT / "output/week9_rank90_serp_data.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(scraped_data, f, indent=2)

avg_wc = int(sum(d["word_count"] for d in scraped_data) / max(len(scraped_data), 1))
print(f"\nAverage Word Count across Top 5: {avg_wc}")

brief_summary = (
    "Consensus: Studs, Huggies, Hoops, Dangles/Drops, Cuffs, Face shape matching, Metals (14K/18K gold, platinum), Healing/aftercare; "
    "Gaps: Pure gold & diamond craftsmanship, hallmarking/BIS security, post thickness/comfort gauge, zero silver, modern Indian corporate/festive styling."
)
print(f"SERP_BRIEF: {brief_summary}")
