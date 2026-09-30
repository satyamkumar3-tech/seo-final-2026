#!/usr/bin/env python3
"""Generate Type 3 images for Week 8 Rank 1: Diamond Rings."""
import os
import sys
import json
import time
import subprocess
import urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
HIGGSFIELD_BIN = Path("/Users/satyamkumar/.local/bin/higgsfield")
if not HIGGSFIELD_BIN.exists():
    HIGGSFIELD_BIN = Path.home() / ".local" / "bin" / "higgsfield"

MANIFEST_PATH = ROOT / "output/Week8_Rank1_DiamondRings_type3_prompts.json"

MANIFEST_DATA = {
    "workflow": "Higgsfield CLI nano_banana_pro with local product reference images.",
    "wp_post_id": 36937,
    "slug": "diamond-rings-2026",
    "output_prefix": "Week8_Rank1_DiamondRings",
    "flatlay_setting": "marble-vanity",
    "flatlay_insert_h2": "The Best Diamond Ring Designs in 2026",
    "lifestyle_insert_h2": "Choosing the Best Diamond Rings for Women Across Different Occasions",
    "higgsfield": {
        "model": "nano_banana_pro",
        "aspect_ratio": "16:9",
        "resolution": "2k",
        "count": 1
    },
    "output": {
        "hero": "output/magnific_generated/diamond-rings-hero-2026.webp",
        "flatlay": "output/magnific_generated/diamond-rings-flatlay-2026.webp",
        "lifestyle": "output/magnific_generated/diamond-rings-lifestyle-2026.webp"
    },
    "slots": {
        "hero": {
            "slot": "hero",
            "product_name": "The Rafia Ring",
            "code": "BIAB0503R03",
            "GenderTag": "Female",
            "dimensions": "product_height_mm=20.92, product_width_mm=9.23 (explicitly jewellery dimensions, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Rings/The Rafia Ring/1_body_portrait.png",
                "ProductImages/raw/Rings/The Rafia Ring/0_primary.png"
            ],
            "alt": "diamond rings 2026 hero with The Rafia Ring",
            "caption": "The Rafia Ring in a warm lifestyle setting capturing radiant diamond brilliance",
            "prompt": "Photoreal candid lifestyle portrait photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. The woman is the primary subject and remains candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear luminous fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Mid-shot candid portrait of an elegant fair-skinned Indian woman dressed in modern silk attire in a softly lit luxury home setting, gently resting her hand near her chin while smiling warmly. She is physically wearing The Rafia Ring from reference images (@img1 body_image worn scale, @img2 design only) on her ring finger. GENDER LOCK: Female adult woman only. The ring rests naturally on her finger with soft contact shadows at EXACT jewellery dimensions: product_height_mm=20.92 x product_width_mm=9.23 (these are jewellery dimensions, not face measurements). Keep the jewellery size on the person like @img1 body_image (worn finger scale). Use @img2 only for the jewellery design. Do not make it bigger for visibility. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the woman; the ring is crisp and true with polished 18K yellow gold band and sparkling organic floral diamond array. Bare neck, bare wrists, no other jewellery in frame. Safe margins, full face and hands clearly visible. Avoid: floating jewellery overlay, giant ring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted hands, extra fingers, extra rings, product shot on plain background, cropped faces, cut-off heads, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
        },
        "flatlay": {
            "slot": "flatlay",
            "product_name": "The Malibu Ring",
            "code": "BIPM0017R18",
            "GenderTag": "Female",
            "dimensions": "product_height_mm=21.59, product_width_mm=8.32 (explicitly jewellery dimensions, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Rings/The Malibu Ring/0_primary.png",
                "ProductImages/raw/Rings/The Malibu Ring/2_front.png",
                "ProductImages/raw/Rings/The Malibu Ring/4_back.png",
                "ProductImages/raw/Rings/The Malibu Ring/6_angle.png"
            ],
            "alt": "best diamond ring designs 2026 marble vanity flatlay with The Malibu Ring",
            "caption": "The Malibu Ring styled on a marble vanity as an exquisite diamond statement design",
            "prompt": "Photoreal high-end jewellery commercial flatlay, HD quality, no distortion of jewellery, identical scale and design (100% match to refs), physically accurate metal and stone detail, natural textures only, no stylization, no illustration. Controlled soft key light with gentle realistic shadows, proper shallow depth of field, balanced exposure with no blown whites and no HDR glare. Shot on DSLR, 16:9 full frame with safe margins. Top-down editorial jewellery flatlay. Flatlay setting ID: marble-vanity. Surface + props: pale warm marble vanity surface, folded ivory silk ribbon, a small unbranded velvet jewellery box, three delicate scattered pale rose petals, and a soft fabric edge in the background. Resting on the marble surface is The Malibu Ring from (@img1, @img2, @img3, @img4) at EXACT jewellery dimensions: product_height_mm=21.59 x product_width_mm=8.32 (jewellery dimensions only). Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. HD hyperreal white metal texture with soft specular highlights, dense rows of round diamonds, flowing interwoven ribbons, and authentic diamond brilliance. Props stay secondary; jewellery is the clear hero of the composition. No people, no hands, no skin. No floating overlays or cutouts. No readable text, logos, or brand marks on props. Safe margins, entire ring visible in frame. Avoid: illustration, CGI look, cartoon, fantasy style, over-stylized, plastic glass, fake diamonds, artificial harsh lighting, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, blurry jewellery, distorted jewellery, warped metal, noise, low detail, AI artifacts, painting, digital art, unreal scale, oversized jewellery, floating overlays, cutouts, product diagrams, readable text, logos, people, hands, skin"
        },
        "lifestyle": {
            "slot": "lifestyle",
            "product_name": "The Ebony Ring",
            "code": "BIIP0090R24",
            "GenderTag": "Female",
            "dimensions": "product_height_mm=20.56, product_width_mm=18.35 (explicitly jewellery dimensions, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Rings/The Ebony Ring/1_body_portrait.png",
                "ProductImages/raw/Rings/The Ebony Ring/0_primary.png"
            ],
            "alt": "best diamond rings for women 2026 lifestyle with The Ebony Ring",
            "caption": "The Ebony Ring worn as a statement floral cluster diamond ring for special occasions",
            "prompt": "Photoreal candid lifestyle photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. People are the primary subject and remain candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Close-up lifestyle portrait of an attractive fair-skinned Indian woman during a celebration, holding a fine porcelain teacup with her hand gracefully turned towards the camera, softly blurred background. She is physically wearing The Ebony Ring from reference images (@img1 body_image worn scale, @img2 design only) on her finger. GENDER LOCK: Female adult woman only. The ring rests naturally on her finger with soft natural contact shadows against skin at EXACT jewellery dimensions: product_height_mm=20.56 x product_width_mm=18.35 (these are jewellery dimensions, not face measurements). Keep the jewellery size on the person like @img1 body_image (worn finger scale). Use @img2 only for the jewellery design. Do not make it bigger for visibility. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the hand and ring; the floral cluster diamond petals are sharp and true with polished yellow gold mountings and dazzling natural diamond sparkle. Bare wrists, no other jewellery in frame. Safe margins, full hand and fingers clearly in frame. Avoid: floating jewellery overlay, giant ring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted hands, extra fingers, extra rings, product shot on plain background, cropped hands, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
        }
    }
}

def write_manifest():
    with open(MANIFEST_PATH, "w") as f:
        json.dump(MANIFEST_DATA, f, indent=2)
    print(f"Saved Type 3 prompts manifest to {MANIFEST_PATH}")

def run_higgsfield_generation(slot_key: str):
    slot_info = MANIFEST_DATA["slots"][slot_key]
    out_rel = MANIFEST_DATA["output"][slot_key]
    dest_path = ROOT / out_rel
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    prompt = slot_info["prompt"]
    ref_paths = [ROOT / r for r in slot_info["local_reference_images"]]
    
    cmd = [
        str(HIGGSFIELD_BIN),
        "generate",
        "create",
        "nano_banana_pro",
        "--prompt", prompt,
        "--aspect_ratio", "16:9",
        "--resolution", "2k",
    ]
    for r in ref_paths:
        if r.exists():
            cmd += ["--image", str(r)]
            
    cmd += ["--wait", "--wait-timeout", "10m", "--wait-interval", "5s", "--json"]
    
    print(f"Starting Higgsfield CLI generation for slot '{slot_key}'...")
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
    
    raw_path = dest_path.with_suffix(".raw.png")
    req = urllib.request.Request(result_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        raw_path.write_bytes(resp.read())
        
    # Resize to 1400px wide 16:9 WebP at quality 82
    img = Image.open(raw_path).convert("RGB")
    if img.width > 1400:
        target_h = round(img.height * 1400 / img.width)
        img = img.resize((1400, target_h), Image.Resampling.LANCZOS)
    img.save(dest_path, "WEBP", quality=82, method=6)
    print(f"Saved optimized WebP to {dest_path} ({img.width}x{img.height}, {os.path.getsize(dest_path)} bytes)")
    
    return {
        "slot": slot_key,
        "job_id": job_id,
        "result_url": result_url,
        "path": str(dest_path),
        "alt": slot_info["alt"],
        "caption": slot_info.get("caption", "")
    }

def main():
    write_manifest()
    results = {}
    for slot in ["hero", "flatlay", "lifestyle"]:
        res = run_higgsfield_generation(slot)
        results[slot] = res
        time.sleep(2)
        
    out_results_path = ROOT / "output/rank1_type3_results.json"
    with open(out_results_path, "w") as f:
        json.dump(results, f, indent=2)
    print("All 3 Type 3 images generated and saved successfully!")

if __name__ == "__main__":
    main()
