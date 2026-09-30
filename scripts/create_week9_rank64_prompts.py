import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

manifest = {
    "workflow": "Higgsfield CLI nano_banana_pro with local product reference images",
    "higgsfield": {
        "model": "nano_banana_pro",
        "aspect_ratio": "16:9",
        "resolution": "2k",
        "count": 1
    },
    "flatlay_setting": "windowsill-daylight",
    "slots": {
        "hero": {
            "slot": "hero",
            "product_name": "The Gigi Ring",
            "code": "BINS0639R18",
            "GenderTag": "Female",
            "pdp": "https://www.bluestone.com/rings/the-gigi-ring~64382.html",
            "dimensions": "product_height_mm=23, product_width_mm=16.12 (explicitly jewellery dimensions, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Rings/The Gigi Ring/1_body_portrait.png",
                "ProductImages/raw/Rings/The Gigi Ring/0_primary.png"
            ],
            "alt": "Yellow stone ring 2026 hero lifestyle featuring The Gigi Ring worn by an Indian woman",
            "caption": "The Gigi Ring worn with contemporary elegance, showcasing radiant yellow gemstone brilliance",
            "prompt": "Photoreal candid lifestyle photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. People are the primary subject and remain candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Mid-shot candid portrait of an elegant, graceful fair-skinned Indian woman in her late 20s wearing a pastel ivory silk kurti in a sun-drenched modern Indian living room during golden hour. Her hand rests gently near her collarbone as she smiles softly, fingers relaxed and clearly visible in the frame. She is physically wearing The Gigi Ring from reference images (@img1 body_image worn scale, @img2 design only) on her ring finger. GENDER LOCK: Female adult woman only. The ring rests naturally on her finger with authentic soft contact shadows against skin at EXACT jewellery dimensions: product_height_mm=23 x product_width_mm=16.12 (these are jewellery dimensions, not face or body measurements). Keep the jewellery size on the person like @img1 body_image (worn finger scale). Use @img2 only for the jewellery design. Do not make it bigger for visibility. Visual style: subtle cinematic film grain / analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the woman and her hand; the geometric yellow gold band with sparkling yellow stone accents is sharp, true, and refined in authentic 18K yellow gold warmth. This is the single and only piece of jewellery in the entire image. Bare ears, bare neck, bare wrists, no other rings. Safe margins, full face, shoulder, and hand clearly visible. CRITICAL anti-collage: the jewellery is physically attached to the finger, never a floating cutout, never a giant product diagram composited over the photo, never a packshot overlay. 16:9 landscape. Avoid: floating jewellery overlay, giant ring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted hands, extra fingers, extra rings, extra bracelets, product shot on plain background, cropped hands, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
        },
        "flatlay": {
            "slot": "flatlay",
            "product_name": "The Malibu Ring",
            "code": "BIPM0017R18",
            "GenderTag": "Female",
            "pdp": "https://www.bluestone.com/rings/the-malibu-ring~7642.html",
            "dimensions": "product_height_mm=21.59, product_width_mm=8.32 (explicitly jewellery dimensions, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Rings/The Malibu Ring/0_primary.png",
                "ProductImages/raw/Rings/The Malibu Ring/2_front.png",
                "ProductImages/raw/Rings/The Malibu Ring/5_close_up.png"
            ],
            "alt": "Yellow stone ring 2026 windowsill daylight flatlay featuring The Malibu Ring",
            "caption": "The Malibu Ring resting on a sunlit windowsill, highlighting 18K yellow gold prong craftsmanship",
            "prompt": "Photoreal high-end jewellery commercial flatlay, HD quality, no distortion of jewellery, identical scale and design (100% match to refs), physically accurate metal and stone detail, natural textures only, no stylization, no illustration. Controlled soft key light with gentle realistic shadows, proper shallow depth of field, balanced exposure with no blown whites and no HDR glare. Shot on DSLR, 16:9 full frame with safe margins. Top-down editorial jewellery flatlay. Flatlay setting ID: windowsill-daylight. Surface + props: painted eggshell white wooden windowsill, soft morning daylight filtering through a sheer textured ivory linen curtain blurred in the background, a small textured ceramic ring dish, an antique brass jeweller loupe resting nearby, and delicate dried golden botanicals. The identical The Malibu Ring from (@img1, @img2, @img3) rests cleanly on the windowsill surface at EXACT jewellery dimensions: product_height_mm=21.59 x product_width_mm=8.32 (these are jewellery dimensions, not face or body measurements). Visual style: subtle cinematic film grain / analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. HD hyperreal yellow gold texture with soft specular highlights, polished prong architecture holding the luminous yellow gemstone, and authentic precious metal luster. Props stay secondary; jewellery is the clear subject. No people, no hands, no skin. No floating overlays or cutouts. No readable text, logos, or brand marks on props. Avoid: illustration, CGI look, cartoon, fantasy style, over-stylized, plastic glass, fake diamonds, artificial harsh lighting, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, blurry jewellery, distorted jewellery, warped metal, noise, low detail, AI artifacts, painting, digital art, unreal scale, oversized jewellery, floating overlays, cutouts, product diagrams, readable text, logos, people, hands, skin"
        },
        "lifestyle": {
            "slot": "lifestyle",
            "product_name": "The Viperine Twist Ring",
            "code": "BIJP0993R123",
            "GenderTag": "Female",
            "pdp": "https://www.bluestone.com/rings/the-viperine-twist-ring~131093.html",
            "dimensions": "product_height_mm=22.21, product_width_mm=9.68 (explicitly jewellery dimensions, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Rings/The Viperine Twist Ring/1_body_portrait.png",
                "ProductImages/raw/Rings/The Viperine Twist Ring/0_primary.png"
            ],
            "alt": "Yellow stone ring 2026 lifestyle action close-up featuring The Viperine Twist Ring",
            "caption": "The Viperine Twist Ring in daily motion, displaying bypass band architecture and golden sparkle",
            "prompt": "Photoreal candid lifestyle photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. People are the primary subject and remain candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Close-up candid lifestyle photograph of a fair-skinned Indian woman's well-manicured hand resting gracefully beside a fine bone china cup on a light natural oak tea table in a sunlit breakfast nook. Her fingers are relaxed with the ring finger positioned sharply in the focal plane. She is physically wearing The Viperine Twist Ring from reference images (@img1 body_image worn scale, @img2 design only) on her ring finger. GENDER LOCK: Female adult woman only. The ring rests naturally on her finger with realistic contact shadows against skin at EXACT jewellery dimensions: product_height_mm=22.21 x product_width_mm=9.68 (these are jewellery dimensions, not face or body measurements). Keep the jewellery size on the person like @img1 body_image (worn finger scale). Use @img2 only for the jewellery design. Do not make it bigger for visibility. Visual style: subtle cinematic film grain / analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses sharply on the hand and ring; the bypass twisted yellow gold band and prong-set yellow stone are sharp and true with authentic 18K gold luster. Bare wrists, bare arms, no other rings or jewellery in frame. Safe margins, full hand and fingers clearly in frame. CRITICAL anti-collage: the jewellery is physically attached to the finger, never a floating cutout, never a giant product diagram composited over the photo, never a packshot overlay. 16:9 landscape. Avoid: floating jewellery overlay, giant ring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted hands, extra fingers, extra rings, extra bracelets, product shot on plain background, cropped hands, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
        }
    },
    "output": {
        "hero": "output/magnific_generated/yellow-stone-ring-hero-2026.webp",
        "flatlay": "output/magnific_generated/yellow-stone-ring-flatlay-2026.webp",
        "lifestyle": "output/magnific_generated/yellow-stone-ring-lifestyle-2026.webp"
    }
}

manifest_path = ROOT / "output/Week9_Rank64_YellowStoneRing_type3_prompts.json"
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)

print(f"Manifest written to {manifest_path}")
