#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create Type 3 prompt manifest for Week 9 Rank 78: Indian Gold Earrings Designs Hoops."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILMIC_STYLE = "Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast."

NEGATIVE_PEOPLE = "dark skin, deep brown skin, heavily tanned skin, floating jewellery overlay, giant earring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake stones, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted ears, multiple ears, extra ears, product shot on plain background, cropped faces, readable text, logos, empty screens, phones"

NEGATIVE_PRODUCT = "floating cutout, 3D render, cartoon, plastic, blurry, oversaturated, harsh flash, empty screens, readable text, logos, hands, people, dark moody shadows, clutter, readable certificates"

CASTING_WOMAN = "Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear luminous fair skin tones. Do not use deep brown, dark, or heavily tanned skin."

prompts_data = {
    "rank": 78,
    "slug": "indian-gold-earrings-designs-hoops-2026",
    "topic": "indian-gold-earrings-designs-hoops",
    "wp_post_id": 40336,
    "workflow": "Higgsfield CLI nano_banana_pro with raw product references",
    "flatlay_setting": "windowsill-daylight",
    "higgsfield": {
        "model": "nano_banana_pro",
        "aspect_ratio": "16:9",
        "resolution": "2k"
    },
    "output": {
        "hero": "output/magnific_generated/indian-gold-earrings-designs-hoops-hero-2026.webp",
        "flatlay": "output/magnific_generated/indian-gold-earrings-designs-hoops-flatlay-2026.webp",
        "lifestyle": "output/magnific_generated/indian-gold-earrings-designs-hoops-lifestyle-2026.webp"
    },
    "slots": {
        "hero": {
            "product_name": "The Vicky Hoop Earrings",
            "code": "BIIP0427H16",
            "gender": "Female",
            "pdp": "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html",
            "dimensions": "product_height_mm=14.75, product_width_mm=6.04 (jewellery dimensions only)",
            "alt": "indian gold earrings designs hoops 2026 hero: elegant fair-skinned Indian woman wearing The Vicky Hoop Earrings in warm morning daylight",
            "caption": "The Vicky Hoop Earrings showcasing classic gold hoop contours and refined earlobe ergonomics",
            "local_reference_images": [
                "ProductImages/raw/Earrings/The Vicky Hoop Earrings/1_body_portrait.png",
                "ProductImages/raw/Earrings/The Vicky Hoop Earrings/2_front.png"
            ],
            "prompt": f"Photoreal candid lifestyle portrait photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft morning window light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. The woman is the primary subject and remains candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. {CASTING_WOMAN} Mid-shot portrait of a graceful, elegant fair-skinned Indian woman in her late 20s dressed in a soft cream raw-silk kurta with subtle golden embroidery, seated in a sunlit living space. Her head is angled slightly to the side with hair gracefully swept behind her ear, clearly revealing The Vicky Hoop Earrings worn on her earlobe. She is physically wearing The Vicky Hoop Earrings from reference images (@img1 body_image worn scale, @img2 design only). GENDER LOCK: adult woman only. The polished gold hoops fit her earlobe naturally with realistic soft contact shadows at EXACT jewellery dimensions: product_height_mm=14.75 x product_width_mm=6.04 (these are jewellery dimensions, not body measurements). Keep the jewellery size on the person like @img1 body_image (worn ear scale). Use @img2 only for the jewellery design. Do not make it bigger for visibility. {FILMIC_STYLE} Camera focuses naturally on the woman; the gold hoop is crisp and true with warm 18K yellow gold luster. Safe margins. Avoid: {NEGATIVE_PEOPLE}"
        },
        "flatlay": {
            "product_name": "The Faliha Purse Hoop Earrings",
            "code": "BIJP0686H03",
            "gender": "Female",
            "pdp": "https://www.bluestone.com/earrings/the-faliha-purse-hoop-earrings~73262.html",
            "dimensions": "product_height_mm=13.86, product_width_mm=13.12 (jewellery dimensions only)",
            "alt": "indian gold earrings designs hoops 2026 flatlay: The Faliha Purse Hoop Earrings on a sunny oak windowsill with ceramic dish and brass loupe",
            "caption": "The <a href=\"https://www.bluestone.com/earrings/the-faliha-purse-hoop-earrings~73262.html\">Faliha Purse Hoop Earrings</a> showcase an intricate purse-silhouette gold bali with delicate floral motifs for festive elegance",
            "local_reference_images": [
                "ProductImages/raw/Earrings/The Faliha Purse Hoop Earrings/2_front.png",
                "ProductImages/raw/Earrings/The Faliha Purse Hoop Earrings/4_back.png",
                "ProductImages/raw/Earrings/The Faliha Purse Hoop Earrings/6_angle.png"
            ],
            "prompt": f"High-end editorial fine jewellery flatlay still-life photograph. Crisp commercial catalogue macro sharpness on product only. Balanced studio lighting with soft diffused side window light and realistic contact shadows. 16:9 full frame composition with generous negative space. The jewellery is the undisputed hero, physically resting on the textured surface in true dimensions. Setting: windowsill-daylight. Top-down view of a lime-washed oak windowsill bathed in soft morning daylight. In the center rests a pair of The Faliha Purse Hoop Earrings from reference images (@img1, @img2, @img3) resting inside a handmade matte cream ceramic jewellery dish, exact jewellery dimensions product_height_mm=13.86 x product_width_mm=13.12 (jewellery dimensions only). Thoughtfully arranged nearby on the wood are a folded ivory raw silk ribbon, a delicate stem of dried baby's breath, and a vintage jeweller brass loupe. No readable text, no phones, no cards, no screens. {FILMIC_STYLE} Avoid: {NEGATIVE_PRODUCT}"
        },
        "lifestyle": {
            "product_name": "The Ursa Hoop Earrings",
            "code": "BISP0427H21",
            "gender": "Female",
            "pdp": "https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html",
            "dimensions": "product_height_mm=16.14, product_width_mm=10.07 (jewellery dimensions only)",
            "alt": "indian gold earrings designs hoops 2026 lifestyle: fair-skinned Indian professional woman wearing The Ursa Hoop Earrings with chic workwear",
            "caption": "The <a href=\"https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html\">Ursa Hoop Earrings</a> blend structured oval geometry with lightweight gold crafting for effortless daily styling",
            "local_reference_images": [
                "ProductImages/raw/Earrings/The Ursa Hoop Earrings/1_body_portrait.png",
                "ProductImages/raw/Earrings/The Ursa Hoop Earrings/2_front.png"
            ],
            "prompt": f"Photoreal candid lifestyle portrait photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft morning window light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites. Shot on DSLR, HD quality, 16:9 full frame with safe margins. The woman is the primary subject and remains candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. {CASTING_WOMAN} Candid portrait of a chic, professional fair-skinned Indian woman in her early 30s dressed in a tailored pastel peach blazer over a silk camisole in an airy contemporary office studio. She is smiling warmly while adjusting her hair lightly behind her ear, clearly showcasing The Ursa Hoop Earrings on her earlobe. She is physically wearing The Ursa Hoop Earrings from reference images (@img1 body_image worn scale, @img2 design only). GENDER LOCK: adult woman only. The structured gold hoops fit her earlobe naturally with soft realistic contact shadows at EXACT jewellery dimensions: product_height_mm=16.14 x product_width_mm=10.07 (these are jewellery dimensions, not body measurements). Keep the jewellery size on the person like @img1 body_image (worn ear scale). Use @img2 only for the jewellery design. Do not make it bigger for visibility. {FILMIC_STYLE} Camera focuses naturally on the woman; the earrings are crisp with authentic 18K gold luster and subtle diamond pave lines. Safe margins. Avoid: {NEGATIVE_PEOPLE}"
        }
    }
}

manifest_file = ROOT / "output" / "Week9_Rank78_IndianGoldHoops_type3_prompts.json"
with open(manifest_file, "w", encoding="utf-8") as f:
    json.dump(prompts_data, f, indent=2, ensure_ascii=False)

print(f"Created {manifest_file.name} successfully.")
