#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create Type 3 prompt manifest for Week 9 Rank 77: Blue Sapphire Ring for Men."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILMIC_STYLE = "Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast."

NEGATIVE_PEOPLE = "dark skin, deep brown skin, heavily tanned skin, floating jewellery overlay, giant ring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake stones, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted fingers, extra fingers, extra hands, product shot on plain background, cropped faces, readable text, logos"

NEGATIVE_PRODUCT = "floating cutout, 3D render, cartoon, plastic, blurry, oversaturated, harsh flash, empty screens, readable text, logos, hands, people, dark moody shadows, clutter"

CASTING_MAN = "Casting (required): fair-skinned Indian man only. Light wheatish to fair North Indian / urban Indian complexion, clear luminous fair skin tones. Do not use deep brown, dark, or heavily tanned skin."

prompts_data = {
    "rank": 77,
    "slug": "blue-sapphire-ring-for-men-2026",
    "topic": "blue-sapphire-ring-for-men",
    "wp_post_id": 40325,
    "workflow": "Higgsfield CLI nano_banana_pro with raw product references",
    "flatlay_setting": "linen-bedside",
    "higgsfield": {
        "model": "nano_banana_pro",
        "aspect_ratio": "16:9",
        "resolution": "2k"
    },
    "output": {
        "hero": "output/magnific_generated/blue-sapphire-ring-for-men-hero-2026.webp",
        "flatlay": "output/magnific_generated/blue-sapphire-ring-for-men-flatlay-2026.webp",
        "lifestyle": "output/magnific_generated/blue-sapphire-ring-for-men-lifestyle-2026.webp"
    },
    "slots": {
        "hero": {
            "product_name": "The Jasper Band For Him",
            "code": "BISL0851R28",
            "gender": "Male",
            "pdp": "https://www.bluestone.com/rings/the-jasper-band-for-him~93964.html",
            "dimensions": "product_height_mm=24.11, product_width_mm=11.92 (jewellery dimensions only)",
            "alt": "Blue sapphire ring for men 2026 hero: distinguished fair-skinned Indian gentleman wearing The Jasper Band For Him in solid gold",
            "caption": "The Jasper Band For Him as a commanding men's ring design reflecting sophisticated masculine luxury",
            "local_reference_images": [
                "ProductImages/raw/Rings/The Jasper Band For Him/1_body_portrait.png",
                "ProductImages/raw/Rings/The Jasper Band For Him/2_front.png"
            ],
            "prompt": f"Photoreal candid lifestyle portrait photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. The man is the primary subject and remains candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. {CASTING_MAN} Mid-shot candid portrait of a distinguished, handsome fair-skinned Indian gentleman in his early 30s dressed in a bespoke charcoal-grey wool tailored blazer over a crisp open-collar white shirt, seated in a warm luxury lounge. His right hand rests naturally on a dark polished mahogany side table, physically wearing The Jasper Band For Him from reference images (@img1 body_image worn scale, @img2 design only) on his middle finger. GENDER LOCK: adult man only. The solid precious gold band fits his masculine hand naturally with realistic contact shadows at EXACT jewellery dimensions: product_height_mm=24.11 x product_width_mm=11.92 (these are jewellery dimensions, not body measurements). Keep the jewellery size on the person like @img1 body_image (worn finger scale). Use @img2 only for the jewellery design. Do not make it bigger for visibility. {FILMIC_STYLE} Camera focuses naturally on the gentleman; the ring is crisp and true with authentic gold luster, zero distortion. Safe margins. Avoid: {NEGATIVE_PEOPLE}"
        },
        "flatlay": {
            "product_name": "The Le Sommet Ring",
            "code": "BISE0932R181",
            "gender": "Female",
            "pdp": "https://www.bluestone.com/rings/the-le-sommet-ring~105031.html",
            "dimensions": "product_height_mm=21.93, product_width_mm=7.95 (jewellery dimensions only)",
            "alt": "Blue sapphire ring for men 2026 flatlay: The Le Sommet Ring on a textured linen bedside table beside brass cufflinks and wooden valet box",
            "caption": "The <a href=\"https://www.bluestone.com/rings/the-le-sommet-ring~105031.html\">Le Sommet Ring</a> showcases architectural precision and exquisite stone setting security for daily wear",
            "local_reference_images": [
                "ProductImages/raw/Rings/The Le Sommet Ring/0_primary.png",
                "ProductImages/raw/Rings/The Le Sommet Ring/2_front.png",
                "ProductImages/raw/Rings/The Le Sommet Ring/6_angle.png"
            ],
            "prompt": f"High-end editorial fine jewellery flatlay still-life photograph. Crisp commercial catalogue macro sharpness on product only. Balanced studio lighting with soft diffused side window light and realistic contact shadows. 16:9 full frame composition with generous negative space. The jewellery is the undisputed hero, physically resting on the textured surface in true dimensions. Setting: linen-bedside. Top-down view of a refined gentleman's dressing valet table draped in natural woven oatmeal linen. In the center rests The Le Sommet Ring from reference images (@img1, @img2, @img3) in solid gold with precision-crafted geometry, exact jewellery dimensions product_height_mm=21.93 x product_width_mm=7.95 (jewellery dimensions only). Thoughtfully arranged nearby are a pair of vintage engine-turned brass cufflinks, an open small dark walnut valet ring box with black velvet lining, and an antique brass loupe. No readable text, no phones, no cards, no screens. {FILMIC_STYLE} Avoid: {NEGATIVE_PRODUCT}"
        },
        "lifestyle": {
            "product_name": "The Interlink Band Ring",
            "code": "BISV0910R24",
            "gender": "Male",
            "pdp": "https://www.bluestone.com/rings/the-interlink-band-ring~108785.html",
            "dimensions": "product_height_mm=25.41, product_width_mm=9.49 (jewellery dimensions only)",
            "alt": "Blue sapphire ring for men 2026 lifestyle: fair-skinned Indian professional gentleman wearing The Interlink Band Ring in tailored office styling",
            "caption": "The <a href=\"https://www.bluestone.com/rings/the-interlink-band-ring~108785.html\">Interlink Band Ring</a> combines interlocking masculine geometry with comfortable daily wear ergonomics",
            "local_reference_images": [
                "ProductImages/raw/Rings/The Interlink Band Ring/1_body_portrait.png",
                "ProductImages/raw/Rings/The Interlink Band Ring/2_front.png"
            ],
            "prompt": f"Photoreal candid lifestyle portrait photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft morning window light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites. Shot on DSLR, HD quality, 16:9 full frame with safe margins. The man is the primary subject and remains candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. {CASTING_MAN} Candid portrait of a sharp, stylish fair-skinned Indian executive in his early 30s in a contemporary creative boardroom. He wears a tailored navy-blue blazer over a fine white dress shirt with cuffs lightly visible. He is smiling warmly while clasping a ceramic coffee mug, clearly displaying The Interlink Band Ring on his ring finger. He is physically wearing The Interlink Band Ring from reference images (@img1 body_image worn scale, @img2 design only). GENDER LOCK: adult man only. The modern interlocking gold band fits his hand naturally with soft realistic contact shadows at EXACT jewellery dimensions: product_height_mm=25.41 x product_width_mm=9.49 (these are jewellery dimensions, not body measurements). Keep the jewellery size on the person like @img1 body_image (worn finger scale). Use @img2 only for the jewellery design. Do not make it bigger for visibility. {FILMIC_STYLE} Camera focuses naturally on the gentleman; the gold ring is crisp and true with polished 18K yellow gold finish. Safe margins. Avoid: {NEGATIVE_PEOPLE}"
        }
    }
}

manifest_file = ROOT / "output" / "Week9_Rank77_BlueSapphireRingMen_type3_prompts.json"
with open(manifest_file, "w", encoding="utf-8") as f:
    json.dump(prompts_data, f, indent=2, ensure_ascii=False)

print(f"Created {manifest_file.name} successfully.")
