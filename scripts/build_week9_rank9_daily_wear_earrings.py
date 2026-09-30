#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Type 3 images, upload carousel assets, patch content & featured image, and live QA Rank 9 (daily-wear-earrings-2026, Post ID 39421)."""

import os, sys, json, time, re, subprocess, urllib.request, base64
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

# Load .env
env_paths = [ROOT / '.env', Path('/Users/satyamkumar/Downloads/seo final 2026/.env')]
for ep in env_paths:
    if ep.exists():
        for line in ep.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

WP_USER = os.environ.get('WP_USER', 'blogbluestone')
WP_PASS = os.environ.get('WP_APP_PASSWORD') or os.environ.get('WP_APP_PASS') or os.environ.get('WP_PASSWORD', '')
WP_URL = os.environ.get('WP_URL', 'https://blog.bluestone.com')
POST_ID = 39421
SLUG = "daily-wear-earrings-2026"
PRIMARY = "daily wear earrings"
TOKEN = base64.b64encode(f"{WP_USER}:{WP_PASS}".encode()).decode()
HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "BluestoneSEO/1.0",
    "Content-Type": "application/json"
}

HIGGSFIELD_BIN = Path.home() / ".local" / "bin" / "higgsfield"
if not HIGGSFIELD_BIN.exists():
    HIGGSFIELD_BIN = Path("/usr/local/bin/higgsfield")

OUTPUT_DIR = ROOT / "output" / "magnific_generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

HERO_WEBP = OUTPUT_DIR / "daily-wear-earrings-hero-2026.webp"
FLATLAY_WEBP = OUTPUT_DIR / "daily-wear-earrings-flatlay-2026.webp"
LIFESTYLE_WEBP = OUTPUT_DIR / "daily-wear-earrings-lifestyle-2026.webp"

PROMPTS = {
    "hero": {
        "product_name": "The Aleena Huggie Earrings",
        "sku": "BIIP0279S08",
        "pdp_url": "https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html",
        "refs": [
            ROOT / "ProductImages/raw/Earrings/The Aleena Huggie Earrings/1_body_portrait.png",
            ROOT / "ProductImages/raw/Earrings/The Aleena Huggie Earrings/0_primary.png"
        ],
        "alt": "Daily wear earrings buying guide 2026 hero: fair-skinned Indian woman wearing The Aleena Huggie Earrings in 18k solid gold",
        "caption": "Everyday earring comfort: <a href=\"https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html\">The Aleena Huggie Earrings</a> in lightweight 18k gold",
        "prompt": "Photoreal candid lifestyle portrait photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. The woman is the primary subject and remains candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear luminous fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Close-up side portrait of an elegant fair-skinned Indian woman softly brushing her hair behind her ear in a bright sunlit apartment. She is physically wearing The Aleena Huggie Earrings from reference images (@img1 body_image worn scale, @img2 design only) securely on her primary earlobe. GENDER LOCK: Female adult woman only. The huggie earring rests naturally on her earlobe with soft contact shadows at EXACT jewellery dimensions (jewellery dimensions, not face measurements). Keep the earring size on the ear like @img1 body_image (worn ear scale). Use @img2 only for the jewellery design. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the earlobe and cheekbone; the gold huggie is crisp, sharp, and true to real 18K yellow gold finish. Bare neck, no extra earrings. Safe margins, ear and side profile clearly in frame. Avoid: floating jewellery overlay, giant earring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted ear, extra ears, product shot on plain background, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
    },
    "flatlay": {
        "product_name": "The Vicky Hoop Earrings",
        "sku": "BIIP0427H16",
        "pdp_url": "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html",
        "refs": [
            ROOT / "ProductImages/raw/Earrings/The Vicky Hoop Earrings/0_primary.png",
            ROOT / "ProductImages/raw/Earrings/The Vicky Hoop Earrings/2_front.png",
            ROOT / "ProductImages/raw/Earrings/The Vicky Hoop Earrings/4_close_up.png"
        ],
        "alt": "Daily wear earrings buying guide 2026 flatlay on beige ceramic tray showing The Vicky Hoop Earrings and silk ribbon",
        "caption": "Effortless everyday loops: <a href=\"https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html\">The Vicky Hoop Earrings</a> featuring secure click-top closures",
        "prompt": "Photoreal high-end jewellery commercial flatlay, HD quality, no distortion of jewellery, identical scale and design (100% match to refs), physically accurate metal and stone detail, natural textures only, no stylization, no illustration. Controlled soft key light with gentle realistic shadows, proper shallow depth of field, balanced exposure with no blown whites and no HDR glare. Shot on DSLR, 16:9 full frame with safe margins. Top-down editorial jewellery flatlay on a warm neutral travertine tray. Surface + props: folded off-white linen, a small ceramic ring dish, a soft cream silk ribbon, and gentle window daylight. Arranged neatly on the tray is The Vicky Hoop Earrings from (@img1, @img2, @img3). Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. HD hyperreal gold texture with soft specular highlights and authentic 18K gold luster. Props stay secondary; jewellery is the clear hero of the composition. No people, no hands, no skin. No floating overlays or cutouts. No readable text, logos, or brand marks on props. Safe margins, entire earrings visible in frame. Avoid: illustration, CGI look, cartoon, fantasy style, over-stylized, plastic glass, fake gems, artificial harsh lighting, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, blurry jewellery, distorted jewellery, warped metal, noise, low detail, AI artifacts, painting, digital art, unreal scale, oversized jewellery, floating overlays, cutouts, product diagrams, readable text, logos, people, hands, skin"
    },
    "lifestyle": {
        "product_name": "The Ursa Hoop Earrings",
        "sku": "BISP0427H21",
        "pdp_url": "https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html",
        "refs": [
            ROOT / "ProductImages/raw/Earrings/The Ursa Hoop Earrings/1_body_portrait.png",
            ROOT / "ProductImages/raw/Earrings/The Ursa Hoop Earrings/0_primary.png"
        ],
        "alt": "Daily wear earrings buying guide 2026 lifestyle: fair-skinned Indian professional wearing The Ursa Hoop Earrings in an executive boardroom",
        "caption": "Contemporary hoops: <a href=\"https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html\">The Ursa Hoop Earrings</a> crafted for all-day earlobe comfort",
        "prompt": "Photoreal candid lifestyle photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. People are the primary subject and remain candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear luminous fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Close-up candid portrait of an attractive fair-skinned Indian woman laughing gently during a coffee break, natural loose wavy hair framing her face. She is physically wearing The Ursa Hoop Earrings from reference images (@img1 body_image worn scale, @img2 design only) on her earlobes. GENDER LOCK: Female adult woman only. The hoop earring hangs comfortably on her lobe with natural contact shadows against skin. Keep the jewellery size on the person natural and true to worn ear scale. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the ear and jawline; the gold hoop is sharp, crisp, and gleaming with authentic 18K yellow gold warmth. Safe margins, full ear and side profile clearly in frame. Avoid: floating jewellery overlay, giant earring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted ear, extra ears, product shot on plain background, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
    }
}

def generate_slot(slot_key: str, dest_webp: Path):
    if dest_webp.exists() and dest_webp.stat().st_size > 10000:
        print(f"[{slot_key}] Image already exists: {dest_webp}")
        return
    
    cfg = PROMPTS[slot_key]
    print(f"\n--- Generating {slot_key} image via Higgsfield CLI ---")
    cmd = [
        str(HIGGSFIELD_BIN), "generate", "create", "nano_banana_pro",
        "--prompt", cfg["prompt"],
        "--aspect_ratio", "16:9",
        "--resolution", "2k",
    ]
    for r in cfg["refs"]:
        if r.exists():
            cmd.extend(["--image", str(r)])
            
    cmd.extend(["--wait", "--wait-timeout", "10m", "--wait-interval", "5s", "--json"])
    
    print("Executing Higgsfield command...")
    start_t = time.time()
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"Attempt 1 failed: {proc.stderr or proc.stdout}. Retrying in 45s...")
        time.sleep(45)
        proc = subprocess.run(cmd, capture_output=True, text=True)
        
    if proc.returncode != 0:
        raise RuntimeError(f"Higgsfield generation failed for slot {slot_key}: {proc.stderr or proc.stdout}")
        
    data = json.loads(proc.stdout)
    job = data[0] if isinstance(data, list) else data
    result_url = job.get("result_url")
    job_id = job.get("id", "unknown")
    if not result_url:
        raise RuntimeError(f"No result_url returned in job: {job}")
        
    print(f"Slot '{slot_key}' finished in {time.time() - start_t:.1f}s, Job ID: {job_id}")
    print(f"Downloading from {result_url}...")
    
    temp_img = OUTPUT_DIR / f"temp_{slot_key}.png"
    req = urllib.request.Request(result_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        temp_img.write_bytes(resp.read())
        
    img = Image.open(temp_img).convert("RGB")
    if img.width > 1400:
        target_h = round(img.height * 1400 / img.width)
        img = img.resize((1400, target_h), Image.Resampling.LANCZOS)
    img.save(dest_webp, "WEBP", quality=85, method=6)
    temp_img.unlink(missing_ok=True)
    print(f"Saved optimized WebP to {dest_webp} ({img.width}x{img.height}, {os.path.getsize(dest_webp)} bytes)")

def upload_to_wordpress(file_path: Path, title: str, alt: str, caption: str) -> tuple:
    print(f"\nUploading {file_path.name} to WordPress...")
    filename = file_path.name
    with open(file_path, "rb") as f:
        img_data = f.read()
        
    upload_url = f"{WP_URL}/wp-json/wp/v2/media"
    req = urllib.request.Request(upload_url, data=img_data, headers={
        "Authorization": f"Basic {TOKEN}",
        "User-Agent": "BluestoneSEO/1.0",
        "Content-Disposition": f'attachment; filename="{filename}"',
        "Content-Type": "image/webp"
    }, method="POST")
    
    with urllib.request.urlopen(req, timeout=45) as resp:
        media_item = json.loads(resp.read().decode())
        media_id = media_item["id"]
        source_url = media_item["source_url"]
        print(f"Uploaded Media ID: {media_id}, URL: {source_url}")
        
    update_url = f"{WP_URL}/wp-json/wp/v2/media/{media_id}"
    patch_payload = json.dumps({
        "title": title,
        "alt_text": alt,
        "caption": caption,
        "description": alt
    }).encode("utf-8")
    
    update_req = urllib.request.Request(update_url, data=patch_payload, headers=HEADERS, method="POST")
    with urllib.request.urlopen(update_req, timeout=30) as resp:
        print(f"Updated metadata for Media ID {media_id}")
        
    return media_id, source_url

def prepare_carousel_images():
    carousel_products = [
        ("The Aleena Huggie Earrings", "BIIP0279S08", "https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html", ROOT / "ProductImages/raw/Earrings/The Aleena Huggie Earrings/0_primary.png"),
        ("The Vicky Hoop Earrings", "BIIP0427H16", "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html", ROOT / "ProductImages/raw/Earrings/The Vicky Hoop Earrings/0_primary.png"),
        ("The Ursa Hoop Earrings", "BISP0427H21", "https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html", ROOT / "ProductImages/raw/Earrings/The Ursa Hoop Earrings/0_primary.png"),
        ("The Rohal Huggie Earrings", "BIPM0001H28", "https://www.bluestone.com/earrings/the-rohal-huggie-earrings~21864.html", ROOT / "ProductImages/raw/Earrings/The Rohal Huggie Earrings/0_primary.png"),
        ("The Asya Huggie Earrings", "BISA0255D05", "https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html", ROOT / "ProductImages/raw/Earrings/The Asya Huggie Earrings/0_primary.png"),
        ("The Skein Hoop Earrings", "BINK0363H03", "https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html", ROOT / "ProductImages/raw/Earrings/The Skein Hoop Earrings/0_primary.png")
    ]
    
    uploaded_carousel = []
    for name, sku, url, img_path in carousel_products:
        slug_name = re.sub(r'[^a-zA-Z0-9]+', '-', name.lower()).strip('-')
        webp_file = OUTPUT_DIR / f"{slug_name}-carousel-2026.webp"
        if not webp_file.exists():
            img = Image.open(img_path).convert("RGB")
            target_w, target_h = 960, 535
            bg = Image.new("RGB", (target_w, target_h), (255, 255, 255))
            img.thumbnail((700, 480), Image.Resampling.LANCZOS)
            offset = ((target_w - img.width) // 2, (target_h - img.height) // 2)
            bg.paste(img, offset)
            bg.save(webp_file, "WEBP", quality=90, method=6)
            
        m_id, s_url = upload_to_wordpress(
            webp_file,
            f"{name} Carousel 2026",
            f"Daily wear earrings 2026: {name} from BlueStone",
            f"<a href=\"{url}\">{name}</a>"
        )
        uploaded_carousel.append({
            "name": name,
            "sku": sku,
            "url": url,
            "media_url": s_url
        })
        
    return uploaded_carousel

def build_article_content(carousel_items, flatlay_id, flatlay_url, lifestyle_id, lifestyle_url):
    c = carousel_items
    carousel_html = f"""<!-- wp:html -->
<style>
.bs-cf{{max-width:900px;margin:1.75rem auto 1.25rem;position:relative;perspective:1200px}}
.bs-cf-stage{{position:relative;height:360px;margin:0 auto;overflow:visible}}
.bs-cf-card{{position:absolute;top:0;left:50%;width:min(420px,78vw);transform-origin:center center;transition:transform .65s cubic-bezier(.22,.61,.36,1),opacity .65s ease,filter .65s ease;border-radius:16px;background:#fff;box-shadow:0 12px 30px rgba(0,0,0,.12);overflow:hidden;border:1px solid #ececec}}
.bs-cf-media{{display:block;line-height:0;background:#f4f4f4}}
.bs-cf-media img{{display:block;width:100%;aspect-ratio:16/9;height:auto;object-fit:cover;object-position:center}}
.bs-cf-meta{{padding:14px 16px 16px;text-align:center;background:#fff}}
.bs-cf-name{{margin:0 0 10px;font-size:1rem;font-weight:600;color:#1a1a1a;text-decoration:none;line-height:1.35;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.bs-cf-cta{{display:inline-block;padding:8px 18px;border-radius:2px;background:#111;color:#fff!important;font-size:.875rem;font-weight:600;text-decoration:none!important;letter-spacing:.02em}}
.bs-cf-cta:hover{{background:#333;color:#fff!important}}
.bs-cf-card.is-pos-0{{z-index:5;opacity:1;filter:none;transform:translate3d(-50%,8px,0) scale(1.02)}}
.bs-cf-card.is-pos-1{{z-index:3;opacity:.95;filter:brightness(.97);transform:translate3d(calc(-50% + 210px),34px,-110px) rotateY(-26deg) scale(.78)}}
.bs-cf-card.is-pos-2{{z-index:3;opacity:.95;filter:brightness(.97);transform:translate3d(calc(-50% - 210px),34px,-110px) rotateY(26deg) scale(.78)}}
.bs-cf-card.is-pos-3,.bs-cf-card.is-pos--3{{z-index:1;opacity:.3;pointer-events:none;transform:translate3d(calc(-50% + 340px),54px,-200px) rotateY(-36deg) scale(.58)}}
.bs-cf-card.is-pos--1{{z-index:1;opacity:.3;pointer-events:none;transform:translate3d(calc(-50% - 340px),54px,-200px) rotateY(36deg) scale(.58)}}
.bs-cf-dots{{display:flex;justify-content:center;gap:8px;margin-top:14px}}
.bs-cf-dot{{width:8px;height:8px;border-radius:50%;border:0;padding:0;background:#c8c8c8;cursor:pointer}}
.bs-cf-dot.is-active{{background:#111;transform:scale(1.2)}}
.bs-cf-nav{{position:absolute;top:38%;z-index:8;width:38px;height:38px;border:0;border-radius:50%;background:rgba(255,255,255,.96);box-shadow:0 2px 8px rgba(0,0,0,.14);cursor:pointer;font-size:20px;color:#222;transform:translateY(-50%)}}
.bs-cf-prev{{left:0}}.bs-cf-next{{right:0}}
@media (max-width:700px){{
  .bs-cf-stage{{height:300px}}
  .bs-cf-card{{width:min(300px,84vw)}}
  .bs-cf-card.is-pos-1{{transform:translate3d(calc(-50% + 130px),36px,-80px) rotateY(-24deg) scale(.72)}}
  .bs-cf-card.is-pos-2{{transform:translate3d(calc(-50% - 130px),36px,-80px) rotateY(24deg) scale(.72)}}
  .bs-cf-card.is-pos-3,.bs-cf-card.is-pos--3,.bs-cf-card.is-pos--1{{opacity:0}}
}}
@media (prefers-reduced-motion:reduce){{.bs-cf-card{{transition:none}}}}
</style>
<div class="bs-cf" id="bs-cf-daily-wear-earrings-2026" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone Daily Wear Earrings Collection">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
    <div class="bs-cf-card is-pos-0" data-index="0">
      <a class="bs-cf-media" href="{c[0]['url']}">
        <img src="{c[0]['media_url']}" alt="Daily wear earrings 2026: {c[0]['name']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{c[0]['name']}</div>
        <a class="bs-cf-cta" href="{c[0]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-1" data-index="1">
      <a class="bs-cf-media" href="{c[1]['url']}">
        <img src="{c[1]['media_url']}" alt="Daily wear earrings 2026: {c[1]['name']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{c[1]['name']}</div>
        <a class="bs-cf-cta" href="{c[1]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-2" data-index="2">
      <a class="bs-cf-media" href="{c[2]['url']}">
        <img src="{c[2]['media_url']}" alt="Daily wear earrings 2026: {c[2]['name']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{c[2]['name']}</div>
        <a class="bs-cf-cta" href="{c[2]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-3" data-index="3">
      <a class="bs-cf-media" href="{c[3]['url']}">
        <img src="{c[3]['media_url']}" alt="Daily wear earrings 2026: {c[3]['name']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{c[3]['name']}</div>
        <a class="bs-cf-cta" href="{c[3]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos--2" data-index="4">
      <a class="bs-cf-media" href="{c[4]['url']}">
        <img src="{c[4]['media_url']}" alt="Daily wear earrings 2026: {c[4]['name']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{c[4]['name']}</div>
        <a class="bs-cf-cta" href="{c[4]['url']}">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos--1" data-index="5">
      <a class="bs-cf-media" href="{c[5]['url']}">
        <img src="{c[5]['media_url']}" alt="Daily wear earrings 2026: {c[5]['name']}" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">{c[5]['name']}</div>
        <a class="bs-cf-cta" href="{c[5]['url']}">Buy now</a>
      </div>
    </div>
  </div>
  <div class="bs-cf-dots">
    <button type="button" class="bs-cf-dot is-active" data-dot="0" aria-label="Go to slide 1"></button>
    <button type="button" class="bs-cf-dot" data-dot="1" aria-label="Go to slide 2"></button>
    <button type="button" class="bs-cf-dot" data-dot="2" aria-label="Go to slide 3"></button>
    <button type="button" class="bs-cf-dot" data-dot="3" aria-label="Go to slide 4"></button>
    <button type="button" class="bs-cf-dot" data-dot="4" aria-label="Go to slide 5"></button>
    <button type="button" class="bs-cf-dot" data-dot="5" aria-label="Go to slide 6"></button>
  </div>
</div>
<script>
(function(){{
  var root=document.getElementById("bs-cf-daily-wear-earrings-2026");
  if(!root)return;
  var cards=Array.prototype.slice.call(root.querySelectorAll(".bs-cf-card"));
  var dots=Array.prototype.slice.call(root.querySelectorAll(".bs-cf-dot"));
  var prevBtn=root.querySelector(".bs-cf-prev");
  var nextBtn=root.querySelector(".bs-cf-next");
  var total=cards.length;
  var current=0;
  var timer=null;
  var interval=parseInt(root.getAttribute("data-interval")||"3200",10);
  var classNames=["is-pos-0","is-pos-1","is-pos-2","is-pos-3","is-pos--2","is-pos--1"];
  function update(){{
    cards.forEach(function(card,i){{
      classNames.forEach(function(cls){{card.classList.remove(cls);}});
      var rel=(i-current+total)%total;
      if(rel===0)card.classList.add("is-pos-0");
      else if(rel===1)card.classList.add("is-pos-1");
      else if(rel===2)card.classList.add("is-pos-2");
      else if(rel===3)card.classList.add("is-pos-3");
      else if(rel===total-2)card.classList.add("is-pos--2");
      else if(rel===total-1)card.classList.add("is-pos--1");
    }});
    dots.forEach(function(dot,i){{
      dot.classList.toggle("is-active",i===current);
    }});
  }}
  function next(){{current=(current+1)%total;update();}}
  function prev(){{current=(current-1+total)%total;update();}}
  function start(){{stop();timer=setInterval(next,interval);}}
  function stop(){{if(timer){{clearInterval(timer);timer=null;}}}}
  if(nextBtn)nextBtn.addEventListener("click",function(){{next();start();}});
  if(prevBtn)prevBtn.addEventListener("click",function(){{prev();start();}});
  dots.forEach(function(dot,i){{
    dot.addEventListener("click",function(){{current=i;update();start();}});
  }});
  root.addEventListener("mouseenter",stop);
  root.addEventListener("mouseleave",start);
  update();
  start();
}})();
</script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p><strong>Curated Design Highlights:</strong> Explore signature everyday earring designs engineered for 24/7 comfort: <a href="{c[0]['url']}">{c[0]['name']}</a> with snag-free huggie ergonomics, <a href="{c[1]['url']}">{c[1]['name']}</a> offering featherlight hoop silhouettes, <a href="{c[2]['url']}">{c[2]['name']}</a> with contemporary rounded contours, <a href="{c[3]['url']}">{c[3]['name']}</a> featuring secure latch-backs, <a href="{c[4]['url']}">{c[4]['name']}</a> crafted with diamond-accented grace, and <a href="{c[5]['url']}">{c[5]['name']}</a> for textured modern minimalism.</p>
<!-- /wp:paragraph -->"""

    # In-body images
    flatlay_block = f"""<!-- wp:image {{"id":{flatlay_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{PROMPTS['flatlay']['pdp_url']}"><img src="{flatlay_url}" alt="{PROMPTS['flatlay']['alt']}" class="wp-image-{flatlay_id}"/></a><figcaption>{PROMPTS['flatlay']['caption']}</figcaption></figure>
<!-- /wp:image -->"""

    lifestyle_block = f"""<!-- wp:image {{"id":{lifestyle_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{PROMPTS['lifestyle']['pdp_url']}"><img src="{lifestyle_url}" alt="{PROMPTS['lifestyle']['alt']}" class="wp-image-{lifestyle_id}"/></a><figcaption>{PROMPTS['lifestyle']['caption']}</figcaption></figure>
<!-- /wp:image -->"""

    # Fetch existing content
    req = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/posts/{POST_ID}", headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        post = json.loads(resp.read().decode('utf-8'))
        content = post['content']['raw'] if 'raw' in post['content'] else post['content']['rendered']

    # Clean any previous broken carousels or image placeholders
    content = re.sub(r'<!-- wp:html -->\s*<style>[\s\S]*?<!-- /wp:html -->', '', content)
    content = re.sub(r'<!-- wp:image[\s\S]*?<!-- /wp:image -->', '', content)
    
    # Insert Carousel after first H2 section
    h2_matches = list(re.finditer(r'<!-- wp:heading {"level":2} -->', content))
    if len(h2_matches) >= 2:
        idx = h2_matches[1].start()
        content = content[:idx] + carousel_html + "\n\n" + content[idx:]
    elif len(h2_matches) >= 1:
        idx = h2_matches[0].end()
        p_end = content.find('<!-- /wp:paragraph -->', idx)
        if p_end != -1:
            idx = p_end + len('<!-- /wp:paragraph -->')
        content = content[:idx] + "\n\n" + carousel_html + "\n\n" + content[idx:]
    else:
        content = carousel_html + "\n\n" + content

    # Place Flatlay and Lifestyle images
    h2_matches = list(re.finditer(r'<!-- wp:heading {"level":2} -->', content))
    if len(h2_matches) >= 5:
        f_idx = h2_matches[2].start()
        content = content[:f_idx] + flatlay_block + "\n\n" + content[f_idx:]
        
        h2_matches = list(re.finditer(r'<!-- wp:heading {"level":2} -->', content))
        l_idx = h2_matches[4].start()
        content = content[:l_idx] + lifestyle_block + "\n\n" + content[l_idx:]
    elif len(h2_matches) >= 3:
        f_idx = h2_matches[1].start()
        content = content[:f_idx] + flatlay_block + "\n\n" + content[f_idx:]
        h2_matches = list(re.finditer(r'<!-- wp:heading {"level":2} -->', content))
        l_idx = h2_matches[2].start()
        content = content[:l_idx] + lifestyle_block + "\n\n" + content[l_idx:]

    return content

def main():
    print(f"=== Starting Build & Fix for Rank 9 ({SLUG} - Post ID {POST_ID}) ===")
    
    # 1. Generate Type 3 Images
    generate_slot("hero", HERO_WEBP)
    generate_slot("flatlay", FLATLAY_WEBP)
    generate_slot("lifestyle", LIFESTYLE_WEBP)
    
    # 2. Upload Type 3 Images to WordPress
    hero_id, hero_url = upload_to_wordpress(
        HERO_WEBP,
        "Daily Wear Earrings Buying Guide 2026 Hero",
        PROMPTS["hero"]["alt"],
        PROMPTS["hero"]["caption"]
    )
    flatlay_id, flatlay_url = upload_to_wordpress(
        FLATLAY_WEBP,
        "Daily Wear Earrings Buying Guide 2026 Flatlay",
        PROMPTS["flatlay"]["alt"],
        PROMPTS["flatlay"]["caption"]
    )
    lifestyle_id, lifestyle_url = upload_to_wordpress(
        LIFESTYLE_WEBP,
        "Daily Wear Earrings Buying Guide 2026 Lifestyle",
        PROMPTS["lifestyle"]["alt"],
        PROMPTS["lifestyle"]["caption"]
    )
    
    # 3. Prepare & Upload Carousel Images
    carousel_items = prepare_carousel_images()
    
    # 4. Build Full Article HTML
    updated_content = build_article_content(carousel_items, flatlay_id, flatlay_url, lifestyle_id, lifestyle_url)
    
    # 5. Patch WordPress Post
    print(f"\nPatching WordPress Post ID {POST_ID}...")
    patch_payload = {
        "featured_media": hero_id,
        "content": updated_content,
        "meta": {
            "_yoast_wpseo_opengraph-image": hero_url,
            "_yoast_wpseo_twitter-image": hero_url
        }
    }
    
    patch_req = urllib.request.Request(
        f"{WP_URL}/wp-json/wp/v2/posts/{POST_ID}",
        data=json.dumps(patch_payload).encode('utf-8'),
        headers=HEADERS,
        method="POST"
    )
    with urllib.request.urlopen(patch_req, timeout=45) as resp:
        updated_post = json.loads(resp.read().decode('utf-8'))
        print(f"Successfully updated Post {POST_ID}! Live URL: {updated_post['link']}")
        print(f"Featured Media ID: {updated_post['featured_media']}")

    # 6. Live QA Check
    print("\n--- Running Live QA Check ---")
    live_req = urllib.request.Request(updated_post['link'], headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(live_req, timeout=30) as resp:
        html = resp.read().decode('utf-8')
        has_carousel = 'class="bs-cf"' in html
        has_hero_og = hero_url in html or f"wp-image-{hero_id}" in html or 'og:image' in html
        word_count = len(re.findall(r'\b\w+\b', re.sub(r'<[^>]+>', ' ', html)))
        print(f"Live QA: Status {resp.status} | Carousel in DOM: {has_carousel} | Words: {word_count}")

if __name__ == "__main__":
    main()
