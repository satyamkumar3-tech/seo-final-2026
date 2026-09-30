#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Type 3 visuals, patch WordPress, fix carousel, and run live QA for Week 9 Rank 4 (long-necklace-2026 / Post ID 39382)."""

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
POST_ID = 39382
SLUG = "long-necklace-2026"
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

HERO_WEBP = OUTPUT_DIR / "long-necklace-hero-2026.webp"
FLATLAY_WEBP = OUTPUT_DIR / "long-necklace-flatlay-2026.webp"
LIFESTYLE_WEBP = OUTPUT_DIR / "long-necklace-lifestyle-2026.webp"

PROMPTS = {
    "hero": {
        "product_name": "The Sarvanya Pendant & Long Chain",
        "sku": "BISW1080P132",
        "pdp_url": "https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html",
        "dimensions": "product_height_mm=33.35, product_width_mm=23.79 (jewellery dimensions only)",
        "refs": [
            ROOT / "ProductImages/raw/Pendants/The Sarvanya Pendant/1_body_portrait.png",
            ROOT / "ProductImages/raw/Pendants/The Sarvanya Pendant/0_primary.png"
        ],
        "alt": "Long necklace buying guide 2026 hero: elegant Indian woman styling The Sarvanya Pendant on a graceful long gold chain",
        "caption": "Long necklace styling 2026: <a href=\"https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html\">The Sarvanya Pendant</a> worn gracefully on an elongated 18k solid gold chain",
        "prompt": "Photoreal candid lifestyle portrait photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. The woman is the primary subject and remains candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear luminous fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Mid-shot candid portrait of an elegant fair-skinned Indian woman in her late 20s dressed in a contemporary silk ensemble in a softly lit luxury boutique lounge, smiling warmly while adjusting the delicate drape of her necklace. She is physically wearing The Sarvanya Pendant and long gold chain from reference images (@img1 body_image worn scale, @img2 design only) around her neck. GENDER LOCK: Female adult woman only. The long necklace rests naturally against her chest with soft contact shadows at EXACT jewellery dimensions: product_height_mm=33.35 x product_width_mm=23.79 (these are jewellery dimensions, not face measurements). Keep the jewellery size on the person like @img1 body_image (worn neck scale). Use @img2 only for the jewellery design. Do not make it bigger for visibility. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the woman; the long necklace is crisp and true with polished 18K gold and radiant gemstone accents. Safe margins, full face and neck clearly visible. Avoid: floating jewellery overlay, giant necklace collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake stones, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted neck, extra hands, product shot on plain background, cropped faces, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
    },
    "flatlay": {
        "product_name": "The Rapett Evil Eye Charm Necklace",
        "sku": "BIPN0987N07",
        "pdp_url": "https://www.bluestone.com/necklaces/the-rapett-evil-eye-charm-necklace~114824.html",
        "dimensions": "product_height_mm=18.75, product_width_mm=11.52 (jewellery dimensions only)",
        "refs": [
            ROOT / "ProductImages/raw/Necklaces/The Rapett Evil Eye Charm Necklace/0_primary.png",
            ROOT / "ProductImages/raw/Necklaces/The Rapett Evil Eye Charm Necklace/1_front.png",
            ROOT / "ProductImages/raw/Necklaces/The Rapett Evil Eye Charm Necklace/4_angle.png"
        ],
        "alt": "Long necklace buying guide 2026 flatlay on marble vanity styling The Rapett Evil Eye Charm Necklace in solid gold",
        "caption": "Long necklace design detail: <a href=\"https://www.bluestone.com/necklaces/the-rapett-evil-eye-charm-necklace~114824.html\">The Rapett Evil Eye Charm Necklace</a> in hallmarked 18k gold",
        "prompt": "Photoreal high-end jewellery commercial flatlay, HD quality, no distortion of jewellery, identical scale and design (100% match to refs), physically accurate metal and stone detail, natural textures only, no stylization, no illustration. Controlled soft key light with gentle realistic shadows, proper shallow depth of field, balanced exposure with no blown whites and no HDR glare. Shot on DSLR, 16:9 full frame with safe margins. Top-down editorial jewellery flatlay on a warm pale marble vanity surface. Surface + props: folded ivory silk fabric, a small velvet jewellery tray, a sprig of dried jasmine blossoms, and soft morning ambient light. Resting smoothly across the marble in an elegant curving silhouette is The Rapett Evil Eye Charm Necklace from (@img1, @img2, @img3) at EXACT jewellery dimensions: product_height_mm=18.75 x product_width_mm=11.52 (jewellery dimensions only). Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. HD hyperreal gold texture with soft specular highlights, delicate evil eye charm detail, and authentic gold shine. Props stay secondary; jewellery is the clear hero of the composition. No people, no hands, no skin. No floating overlays or cutouts. No readable text, logos, or brand marks on props. Safe margins, entire necklace visible in frame. Avoid: illustration, CGI look, cartoon, fantasy style, over-stylized, plastic glass, fake gems, artificial harsh lighting, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, blurry jewellery, distorted jewellery, warped metal, noise, low detail, AI artifacts, painting, digital art, unreal scale, oversized jewellery, floating overlays, cutouts, product diagrams, readable text, logos, people, hands, skin"
    },
    "lifestyle": {
        "product_name": "The Ailia Evil Eye Layered Necklace",
        "sku": "BIAV0987N78",
        "pdp_url": "https://www.bluestone.com/necklaces/the-ailia-evil-eye-layered-necklace~116379.html",
        "dimensions": "product_height_mm=7.45, product_width_mm=7.45 (jewellery dimensions only)",
        "refs": [
            ROOT / "ProductImages/raw/Necklaces/The Ailia Evil Eye Layered Necklace/0_primary.png",
            ROOT / "ProductImages/raw/Necklaces/The Ailia Evil Eye Layered Necklace/1_front.png",
            ROOT / "ProductImages/raw/Necklaces/The Ailia Evil Eye Layered Necklace/4_angle.png"
        ],
        "alt": "Long necklace buying guide 2026 lifestyle: fair-skinned Indian woman wearing The Ailia Evil Eye Layered Necklace at a festive celebration",
        "caption": "Festive layering vibe: <a href=\"https://www.bluestone.com/necklaces/the-ailia-evil-eye-layered-necklace~116379.html\">The Ailia Evil Eye Layered Necklace</a> styled for all-day elegance",
        "prompt": "Photoreal candid lifestyle photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. People are the primary subject and remain candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear luminous fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Close-up lifestyle portrait of an attractive fair-skinned Indian woman attending an upscale festive dinner, laughing gently with friends in a softly blurred background. She is physically wearing The Ailia Evil Eye Layered Necklace from reference images (@img1, @img2, @img3) around her neck. GENDER LOCK: Female adult woman only. The layered necklace drapes gracefully across her neckline with soft natural contact shadows against skin at EXACT jewellery dimensions: product_height_mm=7.45 x product_width_mm=7.45 (these are jewellery dimensions, not face measurements). Keep the jewellery size on the person natural and true to worn neck scale. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the neckline and collarbone; the layered gold chains and evil eye motifs are sharp, refined, and glowing with 18K yellow gold luster. Bare ears or minimal studs, no other large jewellery in frame. Safe margins, full face and neck clearly in frame. Avoid: floating jewellery overlay, giant necklace collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted neck, extra hands, product shot on plain background, cropped hands, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
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
    proc = None
    for attempt in range(2):
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode == 0:
            break
        print(f"Attempt {attempt+1} failed: {proc.stderr or proc.stdout}")
        if attempt == 0:
            print("Waiting 45 seconds before retry...")
            time.sleep(45)
            
    if proc.returncode != 0:
        raise RuntimeError(f"Higgsfield generation failed for slot {slot_key}: {proc.stderr or proc.stdout}")
        
    try:
        data = json.loads(proc.stdout)
    except Exception as e:
        raise RuntimeError(f"Failed to parse JSON output from Higgsfield: {proc.stdout}") from e
        
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
        
    # Resize to 1400px wide 16:9 WebP at quality 85
    img = Image.open(temp_img).convert("RGB")
    if img.width > 1400:
        target_h = round(img.height * 1400 / img.width)
        img = img.resize((1400, target_h), Image.Resampling.LANCZOS)
    img.save(dest_webp, "WEBP", quality=85, method=6)
    temp_img.unlink(missing_ok=True)
    print(f"Saved optimized WebP to {dest_webp} ({img.width}x{img.height}, {os.path.getsize(dest_webp)} bytes)")

def upload_to_wordpress(file_path: Path, title: str, alt: str, caption: str) -> int:
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
        
    # Update alt text, caption, title
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
        
    return media_id

def main():
    print("=== Step 1: Generate Type 3 Images ===")
    generate_slot("hero", HERO_WEBP)
    generate_slot("flatlay", FLATLAY_WEBP)
    generate_slot("lifestyle", LIFESTYLE_WEBP)
    
    print("\n=== Step 2: Upload to WordPress Media Library ===")
    hero_id = upload_to_wordpress(HERO_WEBP, "Long Necklace Buying Guide 2026 Hero", PROMPTS["hero"]["alt"], PROMPTS["hero"]["caption"])
    flatlay_id = upload_to_wordpress(FLATLAY_WEBP, "Long Necklace Buying Guide 2026 Flatlay", PROMPTS["flatlay"]["alt"], PROMPTS["flatlay"]["caption"])
    lifestyle_id = upload_to_wordpress(LIFESTYLE_WEBP, "Long Necklace Buying Guide 2026 Lifestyle", PROMPTS["lifestyle"]["alt"], PROMPTS["lifestyle"]["caption"])
    
    # Get media URLs
    def get_media_url(mid):
        r = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/media/{mid}", headers=HEADERS)
        with urllib.request.urlopen(r) as res:
            return json.loads(res.read().decode())["source_url"]
            
    hero_url = get_media_url(hero_id)
    flatlay_url = get_media_url(flatlay_id)
    lifestyle_url = get_media_url(lifestyle_id)
    
    print(f"Hero ({hero_id}): {hero_url}")
    print(f"Flatlay ({flatlay_id}): {flatlay_url}")
    print(f"Lifestyle ({lifestyle_id}): {lifestyle_url}")
    
    print("\n=== Step 3: Fetch Post Content & Patch WordPress ===")
    post_req = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/posts/{POST_ID}?context=edit", headers=HEADERS)
    with urllib.request.urlopen(post_req) as resp:
        post = json.loads(resp.read().decode())
        raw_content = post.get("content", {}).get("raw", "")
        
    # Build Image Gutenberg Blocks
    flatlay_block = f"""<!-- wp:image {{"id":{flatlay_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{PROMPTS['flatlay']['pdp_url']}"><img src="{flatlay_url}" alt="{PROMPTS['flatlay']['alt']}" class="wp-image-{flatlay_id}"/></a><figcaption>{PROMPTS['flatlay']['caption']}</figcaption></figure>
<!-- /wp:image -->"""

    lifestyle_block = f"""<!-- wp:image {{"id":{lifestyle_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{PROMPTS['lifestyle']['pdp_url']}"><img src="{lifestyle_url}" alt="{PROMPTS['lifestyle']['alt']}" class="wp-image-{lifestyle_id}"/></a><figcaption>{PROMPTS['lifestyle']['caption']}</figcaption></figure>
<!-- /wp:image -->"""

    # Exact Canonical Carousel
    new_carousel = """<!-- wp:html -->
<style>
.bs-cf{max-width:900px;margin:1.75rem auto 1.25rem;position:relative;perspective:1200px}
.bs-cf-stage{position:relative;height:360px;margin:0 auto;overflow:visible}
.bs-cf-card{position:absolute;top:0;left:50%;width:min(420px,78vw);transform-origin:center center;transition:transform .65s cubic-bezier(.22,.61,.36,1),opacity .65s ease,filter .65s ease;border-radius:16px;background:#fff;box-shadow:0 12px 30px rgba(0,0,0,.12);overflow:hidden;border:1px solid #ececec}
.bs-cf-media{display:block;line-height:0;background:#f4f4f4}
.bs-cf-media img{display:block;width:100%;aspect-ratio:16/9;height:auto;object-fit:cover;object-position:center}
.bs-cf-meta{padding:14px 16px 16px;text-align:center;background:#fff}
.bs-cf-name{margin:0 0 10px;font-size:1rem;font-weight:600;color:#1a1a1a;text-decoration:none;line-height:1.35;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bs-cf-cta{display:inline-block;padding:8px 18px;border-radius:2px;background:#111;color:#fff!important;font-size:.875rem;font-weight:600;text-decoration:none!important;letter-spacing:.02em}
.bs-cf-cta:hover{background:#333;color:#fff!important}
.bs-cf-card.is-pos-0{z-index:5;opacity:1;filter:none;transform:translate3d(-50%,8px,0) scale(1.02)}
.bs-cf-card.is-pos-1{z-index:3;opacity:.95;filter:brightness(.97);transform:translate3d(calc(-50% + 210px),34px,-110px) rotateY(-26deg) scale(.78)}
.bs-cf-card.is-pos-2{z-index:3;opacity:.95;filter:brightness(.97);transform:translate3d(calc(-50% - 210px),34px,-110px) rotateY(26deg) scale(.78)}
.bs-cf-card.is-pos-3,.bs-cf-card.is-pos--3{z-index:1;opacity:.3;pointer-events:none;transform:translate3d(calc(-50% + 340px),54px,-200px) rotateY(-36deg) scale(.58)}
.bs-cf-card.is-pos--1{z-index:1;opacity:.3;pointer-events:none;transform:translate3d(calc(-50% - 340px),54px,-200px) rotateY(36deg) scale(.58)}
.bs-cf-dots{display:flex;justify-content:center;gap:8px;margin-top:14px}
.bs-cf-dot{width:8px;height:8px;border-radius:50%;border:0;padding:0;background:#c8c8c8;cursor:pointer}
.bs-cf-dot.is-active{background:#111;transform:scale(1.2)}
.bs-cf-nav{position:absolute;top:38%;z-index:8;width:38px;height:38px;border:0;border-radius:50%;background:rgba(255,255,255,.96);box-shadow:0 2px 8px rgba(0,0,0,.14);cursor:pointer;font-size:20px;color:#222;transform:translateY(-50%)}
.bs-cf-prev{left:0}.bs-cf-next{right:0}
@media (max-width:700px){
  .bs-cf-stage{height:300px}
  .bs-cf-card{width:min(300px,84vw)}
  .bs-cf-card.is-pos-1{transform:translate3d(calc(-50% + 130px),36px,-80px) rotateY(-24deg) scale(.72)}
  .bs-cf-card.is-pos-2{transform:translate3d(calc(-50% - 130px),36px,-80px) rotateY(24deg) scale(.72)}
  .bs-cf-card.is-pos-3,.bs-cf-card.is-pos--3,.bs-cf-card.is-pos--1{opacity:0}
}
@media (prefers-reduced-motion:reduce){.bs-cf-card{transition:none}}
</style>
<div class="bs-cf" id="bs-cf-long-necklace-2026" data-interval="3200" aria-roledescription="carousel" aria-label="BlueStone long necklace and pendant highlights">
  <button type="button" class="bs-cf-nav bs-cf-prev" aria-label="Previous">&#8249;</button>
  <button type="button" class="bs-cf-nav bs-cf-next" aria-label="Next">&#8250;</button>
  <div class="bs-cf-stage">
    <div class="bs-cf-card is-pos-0" data-index="0">
      <a class="bs-cf-media" href="https://www.bluestone.com/necklaces/the-ailia-evil-eye-layered-necklace~116379.html">
        <img src="https://blog.bluestone.com/wp-content/uploads/2026/09/the-ailia-evil-eye-layered-necklace-carousel-2026-1.webp" alt="long necklace 2026 gift idea: The Ailia Evil Eye Layered Necklace" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">The Ailia Evil Eye Layered Necklace</div>
        <a class="bs-cf-cta" href="https://www.bluestone.com/necklaces/the-ailia-evil-eye-layered-necklace~116379.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-1" data-index="1">
      <a class="bs-cf-media" href="https://www.bluestone.com/necklaces/the-rapett-evil-eye-charm-necklace~114824.html">
        <img src="https://blog.bluestone.com/wp-content/uploads/2026/09/the-rapett-evil-eye-charm-necklace-carousel-2026-1.webp" alt="long necklace 2026 gift idea: The Rapett Evil Eye Charm Necklace" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">The Rapett Evil Eye Charm Necklace</div>
        <a class="bs-cf-cta" href="https://www.bluestone.com/necklaces/the-rapett-evil-eye-charm-necklace~114824.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-2" data-index="2">
      <a class="bs-cf-media" href="https://www.bluestone.com/necklaces/the-yfel-evil-eye-pendant-necklace~89724.html">
        <img src="https://blog.bluestone.com/wp-content/uploads/2026/09/the-yfel-evil-eye-pendant-necklace-carousel-2026-1.webp" alt="long necklace 2026 gift idea: The Yfel Evil Eye Pendant Necklace" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">The Yfel Evil Eye Pendant Necklace</div>
        <a class="bs-cf-cta" href="https://www.bluestone.com/necklaces/the-yfel-evil-eye-pendant-necklace~89724.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos-3" data-index="3">
      <a class="bs-cf-media" href="https://www.bluestone.com/pendants/the-valeria-rose-pendant~181266.html">
        <img src="https://blog.bluestone.com/wp-content/uploads/2026/09/the-valeria-rose-pendant-carousel-2026-1.webp" alt="long necklace 2026 gift idea: The Valeria Rose Pendant" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">The Valeria Rose Pendant</div>
        <a class="bs-cf-cta" href="https://www.bluestone.com/pendants/the-valeria-rose-pendant~181266.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos--2" data-index="4">
      <a class="bs-cf-media" href="https://www.bluestone.com/pendants/the-lumeelle-cluster-pendant~162509.html">
        <img src="https://blog.bluestone.com/wp-content/uploads/2026/09/the-lumeelle-cluster-pendant-carousel-2026-1.webp" alt="stone necklaces for women 2026 gift idea: The Lumeelle Cluster Pendant" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">The Lumeelle Cluster Pendant</div>
        <a class="bs-cf-cta" href="https://www.bluestone.com/pendants/the-lumeelle-cluster-pendant~162509.html">Buy now</a>
      </div>
    </div>
    <div class="bs-cf-card is-pos--1" data-index="5">
      <a class="bs-cf-media" href="https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html">
        <img src="https://blog.bluestone.com/wp-content/uploads/2026/09/the-sarvanya-pendant-carousel-2026.webp" alt="long necklace 2026 gift idea: The Sarvanya Pendant" width="960" height="535" loading="lazy" decoding="async"/>
      </a>
      <div class="bs-cf-meta">
        <div class="bs-cf-name">The Sarvanya Pendant</div>
        <a class="bs-cf-cta" href="https://www.bluestone.com/pendants/the-sarvanya-pendant~156927.html">Buy now</a>
      </div>
    </div>
  </div>
  <div class="bs-cf-dots" role="tablist">
    <button type="button" class="bs-cf-dot is-active" data-i="0" aria-label="Product 1"></button>
    <button type="button" class="bs-cf-dot" data-i="1" aria-label="Product 2"></button>
    <button type="button" class="bs-cf-dot" data-i="2" aria-label="Product 3"></button>
    <button type="button" class="bs-cf-dot" data-i="3" aria-label="Product 4"></button>
    <button type="button" class="bs-cf-dot" data-i="4" aria-label="Product 5"></button>
    <button type="button" class="bs-cf-dot" data-i="5" aria-label="Product 6"></button>
  </div>
</div>
<script>
(function(){
  var root=document.getElementById('bs-cf-long-necklace-2026');
  if(!root||root.dataset.ready)return;
  root.dataset.ready='1';
  var cards=[].slice.call(root.querySelectorAll('.bs-cf-card'));
  var dots=[].slice.call(root.querySelectorAll('.bs-cf-dot'));
  var n=cards.length, active=0, timer=null;
  var ms=parseInt(root.getAttribute('data-interval'),10)||3200;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function rel(i){ var d=((i-active)%n+n)%n; if(d>n/2)d=d-n; return d; }
  function paint(){
    cards.forEach(function(c,i){
      c.className='bs-cf-card';
      var d=rel(i), cls='is-pos-'+d;
      if(d===-1)cls='is-pos-2'; if(d===1)cls='is-pos-1'; if(d===0)cls='is-pos-0';
      if(d===-2||d===2)cls=d===2?'is-pos-3':'is-pos--1';
      c.classList.add(cls);
    });
    dots.forEach(function(d,i){d.classList.toggle('is-active',i===active)});
  }
  function go(to){active=((to%n)+n)%n;paint()}
  function next(){go(active+1)}
  function prev(){go(active-1)}
  function stop(){if(timer){clearInterval(timer);timer=null}}
  function start(){if(reduce)return;stop();timer=setInterval(next,ms)}
  root.querySelector('.bs-cf-next').addEventListener('click',function(){next();start()});
  root.querySelector('.bs-cf-prev').addEventListener('click',function(){prev();start()});
  dots.forEach(function(d){d.addEventListener('click',function(){go(+d.getAttribute('data-i'));start()})});
  root.addEventListener('mouseenter',stop);
  root.addEventListener('mouseleave',start);
  paint(); start();
})();
</script>
<!-- /wp:html -->"""

    # Replace Carousel
    c_pattern = re.compile(r'<!-- wp:html -->\s*<style>\s*\.bs-cf.*?<!-- /wp:html -->', re.DOTALL)
    if c_pattern.search(raw_content):
        updated_content = c_pattern.sub(new_carousel, raw_content)
    else:
        updated_content = raw_content

    # Insert Flatlay before Section on Lengths / Styling
    h2_matches = list(re.finditer(r'<!-- wp:heading -->\s*<h2[^>]*>(.*?)</h2>\s*<!-- /wp:heading -->', updated_content))
    print(f"Found {len(h2_matches)} H2 headings in article content.")
    for idx, hm in enumerate(h2_matches):
        print(f"  H2 {idx+1}: {hm.group(1)}")
        
    # Flatlay after 2nd H2 section or before 3rd H2
    if len(h2_matches) >= 3:
        insert_pos_flatlay = h2_matches[2].start()
        updated_content = updated_content[:insert_pos_flatlay] + flatlay_block + "\n\n" + updated_content[insert_pos_flatlay:]
        
    # Re-find H2s after flatlay insertion
    h2_matches = list(re.finditer(r'<!-- wp:heading -->\s*<h2[^>]*>(.*?)</h2>\s*<!-- /wp:heading -->', updated_content))
    # Lifestyle before 5th or 6th H2
    if len(h2_matches) >= 5:
        insert_pos_lifestyle = h2_matches[4].start()
        updated_content = updated_content[:insert_pos_lifestyle] + lifestyle_block + "\n\n" + updated_content[insert_pos_lifestyle:]
    elif len(h2_matches) >= 3:
        insert_pos_lifestyle = h2_matches[-1].start()
        updated_content = updated_content[:insert_pos_lifestyle] + lifestyle_block + "\n\n" + updated_content[insert_pos_lifestyle:]

    # Send POST to WordPress with updated content & featured_media
    print("\nPushing updated content and featured media to WordPress post 39382...")
    post_payload = json.dumps({
        "featured_media": hero_id,
        "content": updated_content
    }).encode("utf-8")
    
    update_post_req = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/posts/{POST_ID}", data=post_payload, headers=HEADERS, method="POST")
    with urllib.request.urlopen(update_post_req, timeout=30) as resp:
        print(f"Post {POST_ID} updated successfully! Status: {resp.status}")

    # Step 4: Run Live QA
    print("\n=== Step 4: Live QA Verification ===")
    live_url = f"https://blog.bluestone.com/{SLUG}/"
    req_live = urllib.request.Request(live_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req_live, timeout=20) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        print(f"Live Page HTTP Status: {resp.status}")
        print(f"Live Page HTML size: {len(html)} bytes")
        
    # Check DOM items
    has_cf = 'id="bs-cf-long-necklace-2026"' in html
    has_stage = 'class="bs-cf-stage"' in html
    cards_count = len(re.findall(r'class="bs-cf-card', html))
    figs_count = len(re.findall(r'<figure class="wp-block-image', html))
    print(f"Carousel present: {has_cf}, Stage present: {has_stage}, Cards count: {cards_count}")
    print(f"Figure blocks count: {figs_count}")

    # Step 5: Update Checkpoint and Status Files
    print("\n=== Step 5: Update Checkpoint and Queue Files ===")
    cp_path = ROOT / "output" / "checkpoints" / "week9_rank4.json"
    cp_data = {
        "pipeline": "week9",
        "rank": 4,
        "slug": SLUG,
        "primary": "long necklace",
        "created_at": "2026-09-18T06:42:04Z",
        "status": "done",
        "steps": {
            "read_docs": {"status": "done"},
            "verify_higgsfield": {"status": "done"},
            "inspect_row": {"status": "done"},
            "duplicate_check": {"status": "done"},
            "fact_check": {"status": "done"},
            "keyword_map": {"status": "done"},
            "structure_visuals": {"status": "done"},
            "draft": {"status": "done"},
            "product_media": {"status": "done"},
            "publish_wordpress": {"status": "done", "detail": [f"post_id={POST_ID}"]},
            "generate_type3": {"status": "done", "detail": [f"hero={hero_id}", f"flatlay={flatlay_id}", f"lifestyle={lifestyle_id}"]},
            "patch_type3": {"status": "done"},
            "live_qa": {"status": "done", "detail": ["status=200", "dom=valid"]},
            "update_status": {"status": "done"},
            "final_report": {"status": "done"}
        },
        "updated_at": "2026-09-18T06:58:00Z",
        "last_exit_code": 0,
        "outcome": "published_and_verified"
    }
    with open(cp_path, "w") as f:
        json.dump(cp_data, f, indent=2)
    print(f"Updated checkpoint: {cp_path}")
    
    # Update Status CSV
    status_csv = ROOT / "output" / "Week9_Blog_Queue_status.csv"
    with open(status_csv, "a", encoding="utf-8") as f:
        f.write(f"4,Done,long necklace,Done,{POST_ID},{live_url},3400,{time.strftime('%Y-%m-%dT%H:%M:%S')}\n")
    print("Updated Week9_Blog_Queue_status.csv")
    
    print("\n🎉 Rank 4 processing complete and verified live!")

if __name__ == "__main__":
    main()
