import json
import re
from html.parser import HTMLParser
from urllib.parse import urlparse

class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip_depth = 0
        self.text = []
        self.h2_text = []
        self.caption_text = []
        self.current_h2 = None
        self.current_caption = None
        self.links = []
        self.images = []
        self.carousel_cards = 0

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag in {"style", "script"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        classes = set(attr.get("class", "").split())
        if tag == "h2":
            self.current_h2 = []
        if tag == "figcaption":
            self.current_caption = []
        if tag == "a":
            self.links.append(attr.get("href", ""))
        if tag == "img":
            self.images.append(attr)
        if tag == "div" and "bs-cf-card" in classes:
            self.carousel_cards += 1

    def handle_endtag(self, tag):
        if tag in {"style", "script"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == "h2" and self.current_h2 is not None:
            self.h2_text.append(" ".join(self.current_h2).strip())
            self.current_h2 = None
        if tag == "figcaption" and self.current_caption is not None:
            self.caption_text.append(" ".join(self.current_caption).strip())
            self.current_caption = None

    def handle_data(self, data):
        if self.skip_depth:
            return
        clean = " ".join(data.split())
        if not clean:
            return
        self.text.append(clean)
        if self.current_h2 is not None:
            self.current_h2.append(clean)
        if self.current_caption is not None:
            self.current_caption.append(clean)


html = open("/tmp/week6_rank5_live.html", encoding="utf-8").read()
post = json.load(open("/tmp/week6_rank5_post.json", encoding="utf-8"))
rendered_html = post["content"]["rendered"]
parser = ArticleParser()
parser.feed(rendered_html)
visible_text = " ".join(parser.text)
visible_words = re.findall(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)*", visible_text)
headings_1 = re.findall(r"<h1\b[^>]*>(.*?)</h1>", html, re.I | re.S)
links = parser.links
internal_links = [
    url
    for url in links
    if urlparse(url).netloc == "blog.bluestone.com"
    and "wedding-gifts-for-girls-2026" not in url
]
external_links = [
    url
    for url in links
    if urlparse(url).netloc and urlparse(url).netloc != "blog.bluestone.com"
]

faq_match = re.search(r'<script type="application/ld\+json" id="bs-faq-schema">(.*?)</script>', rendered_html, re.S)
blog_match = re.search(r'<script type="application/ld\+json" id="bs-blogposting-schema">(.*?)</script>', rendered_html, re.S)
faq_schema = json.loads(faq_match.group(1))
blog_schema = json.loads(blog_match.group(1))
hero_media = json.load(open("/tmp/week6_rank5_media_hero.json", encoding="utf-8"))
body_media = json.load(open("/tmp/week6_rank5_media_body.json", encoding="utf-8"))

images = parser.images
result = {
    "visible_words": len(visible_words),
    "h1_count": len(headings_1),
    "h1_text": [re.sub(r"<[^>]+>", " ", heading).strip() for heading in headings_1],
    "h2_count": len(parser.h2_text),
    "h2_text": parser.h2_text,
    "carousel_cards": parser.carousel_cards,
    "buy_links": len(re.findall(r">\s*Buy now\s*<", rendered_html, re.I)),
    "faq_schema_count": len(faq_schema["mainEntity"]),
    "blog_schema_images": len(blog_schema["image"]),
    "internal_links": len(set(internal_links)),
    "external_links": len(set(external_links)),
    "body_images": len(images),
    "webp_body_images": sum(".webp" in image.get("src", "") for image in images),
    "alts_unique": len({image.get("alt", "") for image in images}) == len(images),
    "empty_alts": sum(not image.get("alt") for image in images),
    "hero_in_body": any(image.get("src") == hero_media["source_url"] for image in images),
    "featured_media": post["featured_media"],
    "author": post["author"],
    "categories": post["categories"],
    "status": post["status"],
    "slug": post["slug"],
    "em_dash": visible_text.count(chr(8212)),
    "en_dash": visible_text.count(chr(8211)),
    "spaced_hyphen": len(re.findall(r"\s-\s", visible_text)),
    "price_patterns": len(re.findall(r"₹|\bRs\.?\s*\d|\bINR\s*\d", visible_text, re.I)),
    "body_captions": parser.caption_text,
    "hero_media": hero_media,
    "body_media": body_media,
}

print(json.dumps(result, indent=2, ensure_ascii=False))
