#!/usr/bin/env python3
"""Generate Type 3 images for Week 8 Rank 19: Engagement Rings for Couples."""
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

MANIFEST_PATH = ROOT / "output/Week8_Rank19_EngagementRingsCouples_type3_prompts.json"

MANIFEST_DATA = {
    "workflow": "Higgsfield CLI nano_banana_pro with local product reference images.",
    "wp_post_id": 37205,
    "slug": "engagement-rings-for-couples-2026",
    "output_prefix": "Week8_Rank19_EngagementRingsCouples",
    "flatlay_setting": "marble-vanity",
    "flatlay_insert_h2": "Top Gold Engagement Ring Designs for Couples: Styles, Textures & Motifs",
    "lifestyle_insert_h2": "Precious Metal Selection: 18K vs. 14K Gold & Dual-Tone Combinations",
    "higgsfield": {
        "model": "nano_banana_pro",
        "aspect_ratio": "16:9",
        "resolution": "2k",
        "count": 1
    },
    "output": {
        "hero": "output/magnific_generated/engagement-rings-for-couples-hero-2026.webp",
        "flatlay": "output/magnific_generated/engagement-rings-for-couples-flatlay-2026.webp",
        "lifestyle": "output/magnific_generated/engagement-rings-for-couples-lifestyle-2026.webp"
    },
    "slots": {
        "hero": {
            "slot": "hero",
            "product_name": "The Liza Ring",
            "code": "BIAR0097R07",
            "GenderTag": "Female",
            "dimensions": "product_height_mm=21.56, product_width_mm=7.91 (explicitly jewellery dimensions, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Rings/The Liza ring/1_body_portrait.png",
                "ProductImages/raw/Rings/The Liza ring/0_primary.png"
            ],
            "alt": "engagement rings for couples 2026 hero with The Liza Ring",
            "caption": "The Liza Ring celebrating an engagement milestone with timeless diamond solitaire elegance",
            "prompt": "Photoreal candid lifestyle portrait photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. People are the primary subject and remain candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian couple only. Light wheatish to fair North Indian / urban Indian complexion, clear luminous fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Mid-shot candid portrait of an attractive fair-skinned Indian couple celebrating their engagement in a softly lit, warm contemporary home setting. The woman rests her left hand gently against her partner's shoulder, smiling warmly. She is physically wearing The Liza Ring from reference images (@img1 body_image worn scale, @img2 design only) on her ring finger. GENDER LOCK: Female adult woman only. The ring rests naturally on her finger with soft contact shadows at EXACT jewellery dimensions: product_height_mm=21.56 x product_width_mm=7.91 (these are jewellery dimensions, not face measurements). Keep the jewellery size on the person like @img1 body_image (worn finger scale). Use @img2 only for the jewellery design. Do not make it bigger for visibility. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the couple; the engagement ring is sharp and true with polished yellow gold band and a sparkling four-prong natural diamond solitaire. Bare neck, bare wrists, no other jewellery in frame. Safe margins, full faces and hands clearly visible. Avoid: floating jewellery overlay, giant ring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted hands, extra fingers, extra rings, product shot on plain background, cropped faces, cut-off heads, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
        },
        "flatlay": {
            "slot": "flatlay",
            "product_name": "The Interlink Band Ring",
            "code": "BISV0910R24",
            "GenderTag": "Male",
            "dimensions": "product_height_mm=25.41, product_width_mm=9.49 (explicitly jewellery dimensions, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Rings/The Interlink Band Ring/0_primary.png",
                "ProductImages/raw/Rings/The Interlink Band Ring/2_front.png",
                "ProductImages/raw/Rings/The Interlink Band Ring/4_close_up.png"
            ],
            "alt": "couple engagement gold rings design 2026 marble vanity flatlay with The Interlink Band Ring",
            "caption": "The Interlink Band Ring styled on a marble vanity as a modern gold couple engagement ring design",
            "prompt": "Photoreal high-end jewellery commercial flatlay, HD quality, no distortion of jewellery, identical scale and design (100% match to refs), physically accurate metal and stone detail, natural textures only, no stylization, no illustration. Controlled soft key light with gentle realistic shadows, proper shallow depth of field, balanced exposure with no blown whites and no HDR glare. Shot on DSLR, 16:9 full frame with safe margins. Top-down editorial jewellery flatlay. Flatlay setting ID: marble-vanity. Surface + props: pale warm marble vanity surface, folded champagne silk ribbon, a small unbranded velvet ring box, two delicate dried eucalyptus sprigs, and a soft ambient glow. Resting on the marble surface is The Interlink Band Ring from (@img1, @img2, @img3) at EXACT jewellery dimensions: product_height_mm=25.41 x product_width_mm=9.49 (jewellery dimensions only). Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. HD hyperreal yellow gold texture with soft specular highlights, polished interlinking architecture, clean beveled edges, and authentic precious metal luster. Props stay secondary; jewellery is the clear hero of the composition. No people, no hands, no skin. No floating overlays or cutouts. No readable text, logos, or brand marks on props. Safe margins, entire ring visible in frame. Avoid: illustration, CGI look, cartoon, fantasy style, over-stylized, plastic glass, fake diamonds, artificial harsh lighting, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, blurry jewellery, distorted jewellery, warped metal, noise, low detail, AI artifacts, painting, digital art, unreal scale, oversized jewellery, floating overlays, cutouts, product diagrams, readable text, logos, people, hands, skin"
        },
        "lifestyle": {
            "slot": "lifestyle",
            "product_name": "The Jasper Band For Him",
            "code": "BISL0851R28",
            "GenderTag": "Male",
            "dimensions": "product_height_mm=24.11, product_width_mm=11.92 (explicitly jewellery dimensions, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Rings/The Jasper Band For Him/1_body_portrait.png",
                "ProductImages/raw/Rings/The Jasper Band For Him/0_primary.png"
            ],
            "alt": "engagement rings gold for couple 2026 lifestyle with The Jasper Band For Him",
            "caption": "The Jasper Band For Him worn as a refined 18K gold couple engagement band",
            "prompt": "Photoreal candid lifestyle photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. People are the primary subject and remain candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian man only. Light wheatish to fair North Indian / urban Indian complexion, clear fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Close-up lifestyle portrait of a well-groomed fair-skinned Indian man in a smart linen shirt at an engagement celebration, holding a fine porcelain cup with his left hand naturally positioned in the foreground, softly blurred warm restaurant background. He is physically wearing The Jasper Band For Him from reference images (@img1 body_image worn scale, @img2 design only) on his ring finger. GENDER LOCK: Male adult man only. The ring rests naturally on his finger with soft natural contact shadows against skin at EXACT jewellery dimensions: product_height_mm=24.11 x product_width_mm=11.92 (these are jewellery dimensions, not face measurements). Keep the jewellery size on the person like @img1 body_image (worn finger scale). Use @img2 only for the jewellery design. Do not make it bigger for visibility. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the hand and ring; the polished gold band and beveled edges are sharp and true with authentic 18K yellow gold warmth. Bare wrists, no other jewellery in frame. Safe margins, full hand and fingers clearly in frame. Avoid: floating jewellery overlay, giant ring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted hands, extra fingers, extra rings, product shot on plain background, cropped hands, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
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
        
    out_results_path = ROOT / "output/rank19_type3_results.json"
    with open(out_results_path, "w") as f:
        json.dump(results, f, indent=2)
    print("All 3 Type 3 images generated and saved successfully!")

if __name__ == "__main__":
    main()
