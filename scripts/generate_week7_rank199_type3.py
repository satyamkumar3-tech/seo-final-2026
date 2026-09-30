#!/usr/bin/env python3
"""Generate Type 3 images for Week 7 Rank 199: Gold Kanthi Chain Design."""
import os
import sys
import json
import time
import subprocess
import urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
HIGGSFIELD_BIN = Path.home() / ".local" / "bin" / "higgsfield"

MANIFEST_PATH = ROOT / "output/Week7_Rank199_GoldKanthi_type3_prompts.json"

MANIFEST_DATA = {
    "workflow": "Higgsfield CLI nano_banana_pro with local product reference images.",
    "wp_post_id": 36915,
    "slug": "gold-kanthi-chain-design-2026",
    "output_prefix": "Week7_Rank199_GoldKanthi",
    "flatlay_setting": "festive-mantel",
    "flatlay_insert_h2": "What Is a Gold Kanthi Chain? Origins, Significance, and Modern Revival",
    "lifestyle_insert_h2": "How to Style a Gold Kanthi Chain: Necklines, Outfits, and Layering",
    "higgsfield": {
        "model": "nano_banana_pro",
        "aspect_ratio": "16:9",
        "resolution": "2k",
        "count": 1
    },
    "output": {
        "hero": "output/magnific_generated/gold-kanthi-chain-design-hero-2026.webp",
        "flatlay": "output/magnific_generated/gold-kanthi-chain-design-flatlay-2026.webp",
        "lifestyle": "output/magnific_generated/gold-kanthi-chain-design-lifestyle-2026.webp"
    },
    "slots": {
        "hero": {
            "slot": "hero",
            "product_name": "The Thaloria Pendant",
            "code": "BISW1080P131",
            "GenderTag": "Female",
            "dimensions": "product_height_mm=36.91, product_width_mm=25.28 (explicitly jewellery dimensions, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Pendants/The Thaloria Pendant/1_body_portrait.png",
                "ProductImages/raw/Pendants/The Thaloria Pendant/2_front.png"
            ],
            "alt": "gold kanthi chain design 2026 hero, The Thaloria Pendant worn on an elegant necklace by a woman",
            "caption": "The Thaloria Pendant styled as a magnificent fine gold statement necklace",
            "prompt": "Photoreal candid lifestyle portrait photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. The woman is the primary subject and remains candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear luminous fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Mid-shot candid portrait of an elegant fair-skinned Indian woman dressed in modern festive raw silk attire in a warmly lit contemporary luxury interior. She is physically wearing The Thaloria Pendant from reference images (@img1 body_image worn scale, @img2 design only) on a delicate gold chain sitting gracefully along her collarbone. GENDER LOCK: Female adult woman only. The necklace hangs gracefully with soft natural contact shadows against skin at EXACT jewellery dimensions: product_height_mm=36.91 x product_width_mm=25.28 (these are jewellery dimensions, not face measurements). Keep the pendant size on the woman like @img1 body_image (worn neck scale). Use @img2 only for the pendant design. Do not make it bigger for visibility. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the woman; pendant is crisp and true with polished yellow gold contours and shimmering diamond accents. Bare wrists, bare ears, no other jewellery in frame. Safe margins, full face and neckline clearly visible. Avoid: floating jewellery overlay, giant pendant collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted hands, extra fingers, product shot on plain background, cropped faces, cut-off heads, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
        },
        "flatlay": {
            "slot": "flatlay",
            "product_name": "The Chevalier Gold Chain",
            "code": "BVEM0663C65",
            "GenderTag": "Male",
            "dimensions": "product_height_mm=5.11, product_width_mm=3.76 (explicitly jewellery dimensions)",
            "local_reference_images": [
                "ProductImages/raw/Chains/The Chevalier Gold Chain/1_front.png",
                "ProductImages/raw/Chains/The Chevalier Gold Chain/2_side_1.png",
                "ProductImages/raw/Chains/The Chevalier Gold Chain/0_primary.png"
            ],
            "alt": "gold kanthi chain design 2026 flatlay on festive mantel, The Chevalier Gold Chain",
            "caption": "The Chevalier Gold Chain arranged on a festive mantel highlighting refined link craftsmanship",
            "prompt": "Photoreal high-end jewellery commercial flatlay, HD quality, no distortion of jewellery, identical scale and design (100% match to refs), physically accurate metal detail, natural textures only, no stylization, no illustration. Controlled soft key light with gentle realistic shadows, proper shallow depth of field, balanced exposure with no blown whites and no HDR glare. Shot on DSLR, 16:9 full frame with safe margins. Top-down editorial jewellery flatlay. Flatlay setting ID: festive-mantel. Surface + props: warm polished dark walnut wood mantelpiece softly illuminated by warm ambient festive light, a delicate brass tray holding The Chevalier Gold Chain coiled gracefully from (@img1 front packshot, @img2 side view, @img3 primary design) at EXACT jewellery dimensions: product_height_mm=5.11 x product_width_mm=3.76 (jewellery dimensions only). Beside the tray sit subtle fresh marigold flower petals, a small unlit ornamental brass diya, folded raw silk fabric in rich maroon tones, and a small handcrafted ceramic bowl. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. HD hyperreal gold texture with soft specular highlights and authentic yellow gold lustre showing interlocking links of fine gold. Props stay secondary; chain is the clear hero of the composition. No people, no hands, no skin. No floating overlays or cutouts. No readable text, logos, or brand marks on props. Safe margins, entire piece visible in frame. Avoid: illustration, CGI look, cartoon, fantasy style, over-stylized, plastic glass, fake diamonds, artificial harsh lighting, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, blurry jewellery, distorted jewellery, warped metal, noise, low detail, AI artifacts, painting, digital art, unreal scale, oversized jewellery, floating overlays, cutouts, product diagrams, readable text, logos, people, hands, skin"
        },
        "lifestyle": {
            "slot": "lifestyle",
            "product_name": "The Sarvanya Pendant",
            "code": "BISW1080P132",
            "GenderTag": "Female",
            "dimensions": "product_height_mm=33.35, product_width_mm=23.79 (explicitly jewellery dimensions, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Pendants/The Sarvanya Pendant/1_body_portrait.png",
                "ProductImages/raw/Pendants/The Sarvanya Pendant/2_front.png"
            ],
            "alt": "gold kanthi chain design 2026 lifestyle close-up, The Sarvanya Pendant worn at a celebration",
            "caption": "The Sarvanya Pendant worn elegantly at the neckline for a festive family gathering",
            "prompt": "Photoreal candid lifestyle photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. People are the primary subject and remain candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Close-up portrait of an attractive fair-skinned Indian woman attending an intimate festive family dinner, warmly glowing ambient festive lanterns softly blurred in the background. She is physically wearing The Sarvanya Pendant from reference images (@img1 body_image worn scale, @img2 design only) resting cleanly on her upper chest along a fine gold chain. GENDER LOCK: Female adult woman only. The necklace rests gracefully with soft natural contact shadows against skin at EXACT jewellery dimensions: product_height_mm=33.35 x product_width_mm=23.79 (these are jewellery dimensions, not face measurements). Keep the pendant size on the woman like @img1 body_image (worn neck scale). Use @img2 only for the pendant design. Do not make it bigger for visibility. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the woman; pendant is sharp and true with polished yellow gold filigree and sparkling accents. Bare wrists, no other jewellery in frame. Safe margins, full face and neckline in frame. Avoid: floating jewellery overlay, giant pendant collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted hands, extra fingers, product shot on plain background, cropped faces, cut-off heads, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
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
    
    # Retry once on failure after 45s wait
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
        
    out_results_path = ROOT / "output/rank199_type3_results.json"
    with open(out_results_path, "w") as f:
        json.dump(results, f, indent=2)
    print("All 3 Type 3 images generated and saved successfully!")

if __name__ == "__main__":
    main()
