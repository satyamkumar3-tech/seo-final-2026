#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Type 3 images via Higgsfield CLI, upload to WordPress, and patch Post 40055."""

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
POST_ID = 40055
SLUG = "stone-stud-earrings-2026"
PRIMARY = "stone stud earrings"
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

HERO_WEBP = OUTPUT_DIR / f"{SLUG}-hero.webp"
FLATLAY_WEBP = OUTPUT_DIR / f"{SLUG}-flatlay.webp"
LIFESTYLE_WEBP = OUTPUT_DIR / f"{SLUG}-lifestyle.webp"

PROMPTS = {
    "hero": {
        "product_name": "The Aleena Huggie Earrings",
        "sku": "BIIP0279S08",
        "pdp_url": "https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html",
        "refs": [
            ROOT / "ProductImages/raw/Earrings/The Aleena Huggie Earrings/1_body_portrait.png",
            ROOT / "ProductImages/raw/Earrings/The Aleena Huggie Earrings/0_primary.png"
        ],
        "alt": "Stone stud earrings buying guide 2026 hero: fair-skinned Indian woman wearing The Aleena Huggie Earrings in 18k solid gold",
        "title": "Stone stud earrings buying guide 2026 hero: The Aleena Huggie Earrings in 18k gold",
        "caption": "Effortless everyday sparkle: The Aleena Huggie Earrings in 18k solid gold",
        "prompt": "Photoreal candid lifestyle portrait photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. The woman is the primary subject and remains candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear luminous fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Close-up side portrait of an elegant fair-skinned Indian woman softly tucking her dark hair behind her ear in a bright sunlit apartment. She is physically wearing The Aleena Huggie Earrings from reference images (@img1 body_image worn scale, @img2 design only) securely on her primary earlobe. GENDER LOCK: Female adult woman only. The stone stud huggie rests naturally on her earlobe with soft contact shadows at EXACT jewellery dimensions (product_height_mm 17.23, product_width_mm 9.5; jewellery dimensions, not face measurements). Keep the earring size on the ear like @img1 body_image (worn ear scale). Use @img2 only for the jewellery design. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the earlobe and cheekbone; the gold and diamond stones are crisp, sharp, and true to real 18K yellow gold finish. Safe margins, ear and side profile clearly in frame. Avoid: floating jewellery overlay, giant earring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted ear, extra ears, product shot on plain background, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
    },
    "flatlay": {
        "product_name": "The Vicky Hoop Earrings",
        "sku": "BIIP0427H16",
        "pdp_url": "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html",
        "refs": [
            ROOT / "ProductImages/raw/Earrings/The Vicky Hoop Earrings/0_primary.png",
            ROOT / "ProductImages/raw/Earrings/The Vicky Hoop Earrings/2_front.png",
            ROOT / "ProductImages/raw/Earrings/The Vicky Hoop Earrings/5_close_up.png"
        ],
        "alt": "Stone stud earrings buying guide 2026 flatlay showing The Vicky Hoop Earrings on travertine tray with jeweller loupe",
        "title": "Stone stud earrings buying guide 2026 flatlay: The Vicky Hoop Earrings",
        "caption": "Fine gemstone earrings: <a href=\"https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html\">The Vicky Hoop Earrings</a> featuring brilliant stones and secure closures",
        "prompt": "Photoreal high-end fine jewellery commercial flatlay, HD quality, no distortion of jewellery, identical scale and design (100% match to refs), physically accurate metal and stone detail, natural textures only, no stylization, no illustration. Controlled soft key light with gentle realistic shadows, proper shallow depth of field, balanced exposure with no blown whites and no HDR glare. Shot on DSLR, 16:9 full frame with safe margins. Top-down editorial jewellery flatlay on a warm neutral travertine tray on a study desk. Surface + props: a jeweller's brass loupe, a brass millimeter gauge, neatly folded off-white linen cloth, a soft cream silk ribbon, and gentle window daylight. Arranged neatly on the tray is The Vicky Hoop Earrings from (@img1, @img2, @img3). Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. HD hyperreal gold texture with soft specular highlights and authentic 18K gold luster. Props stay secondary; jewellery is the clear hero of the composition. No people, no hands, no skin. No floating overlays or cutouts. No readable text, logos, or brand marks on props. Safe margins, entire earrings visible in frame. Avoid: illustration, CGI look, cartoon, fantasy style, over-stylized, plastic glass, fake gems, artificial harsh lighting, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, blurry jewellery, distorted jewellery, warped metal, noise, low detail, AI artifacts, painting, digital art, unreal scale, oversized jewellery, floating overlays, cutouts, product diagrams, readable text, logos, people, hands, skin"
    },
    "lifestyle": {
        "product_name": "The Ursa Hoop Earrings",
        "sku": "BISP0427H21",
        "pdp_url": "https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html",
        "refs": [
            ROOT / "ProductImages/raw/Earrings/The Ursa Hoop Earrings/1_body_portrait.png",
            ROOT / "ProductImages/raw/Earrings/The Ursa Hoop Earrings/0_primary.png"
        ],
        "alt": "Stone stud earrings buying guide 2026 lifestyle: fair-skinned Indian professional woman wearing The Ursa Hoop Earrings",
        "title": "Stone stud earrings buying guide 2026 lifestyle: The Ursa Hoop Earrings in 18k gold",
        "caption": "Contemporary gold studs: <a href=\"https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html\">The Ursa Hoop Earrings</a> crafted for all-day comfort and sparkle",
        "prompt": "Photoreal candid lifestyle photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. People are the primary subject and remain candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear luminous fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Close-up candid portrait of an attractive fair-skinned Indian professional woman smiling gently during a creative architectural consultation, natural hair tucked neatly behind her ear. She is physically wearing The Ursa Hoop Earrings from reference images (@img1 body_image worn scale, @img2 design only) on her earlobes. GENDER LOCK: Female adult woman only. The stone stud hoop hangs comfortably on her lobe with natural contact shadows against skin at EXACT jewellery dimensions (product_height_mm 16.14, product_width_mm 10.07; jewellery dimensions, not face measurements). Keep the jewellery size on the person natural and true to worn ear scale. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the ear and jawline; the gold is sharp, crisp, and gleaming with authentic 18K yellow gold warmth. Safe margins, full ear and side profile clearly in frame. Avoid: floating jewellery overlay, giant earring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted ear, extra ears, product shot on plain background, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
    }
}

job_history = {}

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
    
    print("Executing Higgsfield command synchronously...")
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
    job_history[slot_key] = {"job_id": job_id, "result_url": result_url}
    
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
    with urllib.request.urlopen(req, timeout=120) as resp:
        res = json.loads(resp.read().decode())
        media_id = res["id"]
        source_url = res["source_url"]
        
    # Update alt, title, and caption
    update_data = json.dumps({
        "title": title,
        "alt_text": alt,
        "caption": caption
    }).encode()
    req = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/media/{media_id}", data=update_data, headers=HEADERS, method="POST")
    with urllib.request.urlopen(req, timeout=60) as resp:
        pass
        
    print(f"Uploaded Media ID: {media_id} -> {source_url}")
    return media_id, source_url

def main():
    print("=== Step 12: Generating Type 3 Images ===")
    generate_slot("hero", HERO_WEBP)
    generate_slot("flatlay", FLATLAY_WEBP)
    generate_slot("lifestyle", LIFESTYLE_WEBP)
    
    print("\nAll 3 Type 3 images generated successfully!")
    
    # Save job history
    (ROOT / "output" / "week9_rank52_higgsfield_jobs.json").write_text(json.dumps(job_history, indent=2))
    
    print("\n=== Step 13: Uploading Images and Patching WordPress ===")
    
    hero_cfg = PROMPTS["hero"]
    hero_id, hero_url = upload_to_wordpress(HERO_WEBP, hero_cfg["title"], hero_cfg["alt"], hero_cfg["caption"])
    
    flatlay_cfg = PROMPTS["flatlay"]
    flatlay_id, flatlay_url = upload_to_wordpress(FLATLAY_WEBP, flatlay_cfg["title"], flatlay_cfg["alt"], flatlay_cfg["caption"])
    
    lifestyle_cfg = PROMPTS["lifestyle"]
    lifestyle_id, lifestyle_url = upload_to_wordpress(LIFESTYLE_WEBP, lifestyle_cfg["title"], lifestyle_cfg["alt"], lifestyle_cfg["caption"])
    
    # Fetch current post
    print(f"\nFetching Post {POST_ID} content from WordPress...")
    req = urllib.request.Request(f"{WP_URL}/wp-json/wp/v2/posts/{POST_ID}?context=edit", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        post = json.loads(resp.read().decode())
        content = post["content"]["raw"]
        
    # Build Gutenberg blocks for flatlay and lifestyle
    flatlay_block = f"""<!-- wp:image {{"id":{flatlay_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{flatlay_cfg['pdp_url']}"><img src="{flatlay_url}" alt="{flatlay_cfg['alt']}" class="wp-image-{flatlay_id}"/></a><figcaption>{flatlay_cfg['caption']}</figcaption></figure>
<!-- /wp:image -->"""

    lifestyle_block = f"""<!-- wp:image {{"id":{lifestyle_id},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{lifestyle_cfg['pdp_url']}"><img src="{lifestyle_url}" alt="{lifestyle_cfg['alt']}" class="wp-image-{lifestyle_id}"/></a><figcaption>{lifestyle_cfg['caption']}</figcaption></figure>
<!-- /wp:image -->"""

    # Replace placeholders
    if "<!-- TYPE3_FLATLAY_PLACEHOLDER -->" in content:
        content = content.replace("<!-- TYPE3_FLATLAY_PLACEHOLDER -->", flatlay_block)
        print("Replaced FLATLAY placeholder successfully")
    else:
        print("WARNING: Flatlay placeholder not found!")
        
    if "<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->" in content:
        content = content.replace("<!-- TYPE3_LIFESTYLE_PLACEHOLDER -->", lifestyle_block)
        print("Replaced LIFESTYLE placeholder successfully")
    else:
        print("WARNING: Lifestyle placeholder not found!")
        
    # Patch post with featured media and updated content
    patch_payload = {
        "content": content,
        "featured_media": hero_id,
        "meta": {
            "_yoast_wpseo_opengraph-image": hero_url,
            "_yoast_wpseo_opengraph-image-id": hero_id,
            "_yoast_wpseo_twitter-image": hero_url,
            "_yoast_wpseo_twitter-image-id": hero_id,
        }
    }
    
    print(f"\nPatching Post {POST_ID} in WordPress...")
    req = urllib.request.Request(
        f"{WP_URL}/wp-json/wp/v2/posts/{POST_ID}",
        data=json.dumps(patch_payload).encode(),
        headers=HEADERS,
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        updated_post = json.loads(resp.read().decode())
        print(f"Successfully patched Post {updated_post['id']}!")
        print(f"Featured Media ID: {updated_post.get('featured_media')}")
        print(f"Link: {updated_post.get('link')}")
        
    # Record media manifest
    media_manifest = {
        "post_id": POST_ID,
        "slug": SLUG,
        "hero": {"id": hero_id, "url": hero_url, "product": hero_cfg["product_name"], "sku": hero_cfg["sku"]},
        "flatlay": {"id": flatlay_id, "url": flatlay_url, "product": flatlay_cfg["product_name"], "sku": flatlay_cfg["sku"]},
        "lifestyle": {"id": lifestyle_id, "url": lifestyle_url, "product": lifestyle_cfg["product_name"], "sku": lifestyle_cfg["sku"]}
    }
    (ROOT / "output" / "week9_rank52_media_manifest.json").write_text(json.dumps(media_manifest, indent=2))
    print(f"Recorded media manifest to output/week9_rank52_media_manifest.json")

if __name__ == "__main__":
    main()
