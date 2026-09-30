#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create Type 3 prompts manifest for Week 9 Rank 90: earring styles for guys."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

manifest = {
    "workflow": "Higgsfield CLI nano_banana_pro with local product reference images",
    "higgsfield": {
        "model": "nano_banana_pro",
        "theme_anchor": "Hyper-realistic commercial lifestyle photography, cinematic 35mm film still, Kodak Portra 400 color science, highlight halation, creamy bokeh, filmic tonal response, natural dynamic range, filmic contrast, subtle analog grain. Fair-skinned Indian subject, light wheatish complexion.",
        "negative_prompt": "dark skin, deep brown skin, heavily tanned skin, female model, woman, feminine styling, duplicate jewellery, floating packshot, cartoon, illustration, 3d render, cgi, blurry, bad anatomy, distorted hands, text, logo, watermark, readable text, phone screen, laptop screen"
    },
    "slots": {
        "hero": {
            "product_name": "The Skein Hoop Earrings",
            "code": "BINK0363H03",
            "pdp": "https://www.bluestone.com/earrings/the-skein-hoop-earrings~27215.html",
            "product_dimensions": "17.95mm height by 6.16mm width (jewellery dimensions only, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Earrings/The Skein Hoop Earrings/1_body_portrait.png",
                "ProductImages/raw/Earrings/The Skein Hoop Earrings/0_primary.png"
            ],
            "prompt": "Hyper-realistic commercial lifestyle photography, cinematic 35mm film still, Kodak Portra 400 color science, highlight halation, creamy bokeh, subtle analog grain. Candid portrait of a confident, handsome fair-skinned North Indian young man in his late twenties with a clean light wheatish complexion, well-groomed stubble beard, and sharp stylish jawline. He is seated near a large sunlit loft window, physically wearing The Skein Hoop Earrings from @img2 on his earlobe at true worn scale matching @img1 body_image (product_height_mm=17.95 and product_width_mm=6.16; these are jewellery dimensions only, not face or body measurements). The textured 18Kt yellow gold hoop earring fits comfortably and securely in his lower earlobe, catching the warm directional morning sunlight with soft golden specular reflections. He wears a relaxed charcoal-grey textured linen overshirt over an off-white crewneck. Softly blurred in the background is a modern architectural loft interior; zero phones, zero screens, zero readable text. Visual style: subtle cinematic film grain / analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Avoid: woman, female, dark skin, deep brown skin, heavily tanned skin, duplicate jewellery, floating packshot, cartoon, 3d render, blurry, distorted hands, text, watermark, phone screen, laptop.",
            "alt": "earring styles for guys 2026 hero: stylish fair-skinned Indian man wearing a minimalist 18K gold hoop earring"
        },
        "flatlay": {
            "product_name": "The Ursa Hoop Earrings",
            "code": "BISP0427H21",
            "pdp": "https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html",
            "product_dimensions": "16.14mm height by 10.07mm width (jewellery dimensions only)",
            "setting": "study-desk",
            "local_reference_images": [
                "ProductImages/raw/Earrings/The Ursa Hoop Earrings/0_primary.png",
                "ProductImages/raw/Earrings/The Ursa Hoop Earrings/2_front.png",
                "ProductImages/raw/Earrings/The Ursa Hoop Earrings/1_body_portrait.png"
            ],
            "prompt": "Top-down commercial fine jewellery flatlay photography, 50mm macro lens, f/4 aperture, sharp focus on jewellery with gentle natural falloff. Flatlay setting: study-desk. Arranged on a rich dark walnut wood desk surface in soft diffused morning daylight: @img1, authentic fine 18Kt yellow gold hoop earrings with distinct ribbed facets, accompanied by design details from @img2 and @img3, resting centered at true life scale (16.14mm height by 10.07mm width). Beside the gold earrings are authentic tactile masculine study and grooming props: a handcrafted tan saddle-leather valet tray, an antique miniature brass loupe with clear glass lens, an unlabelled dark leather notebook with closed spine turned away, and a stainless steel vintage watch case softly out of focus. Soft directional morning window illumination, delicate organic shadows. Visual style: subtle cinematic film grain / analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. No people, no hands, no readable text, no cards, no screens, no logos. Avoid: floating packshot, cartoon, 3d render, CGI, plastic textures, blurry, artificial lighting, text, watermark, numbers, phone screen.",
            "alt": "earring styles for guys 2026 flatlay: The Ursa Hoop Earrings on masculine study desk with leather valet tray and brass loupe",
            "caption": "The <a href=\"https://www.bluestone.com/earrings/the-ursa-hoop-earrings~35069.html\">Ursa Hoop Earrings</a> in solid 18Kt gold featuring bold sculpted ridges designed for distinctive masculine edge"
        },
        "lifestyle": {
            "product_name": "The Asya Huggie Earrings",
            "code": "BISA0255D05",
            "pdp": "https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html",
            "product_dimensions": "19.77mm height by 8.47mm width (jewellery dimensions only, not face or body measurements)",
            "local_reference_images": [
                "ProductImages/raw/Earrings/The Asya Huggie Earrings/1_body_portrait.png",
                "ProductImages/raw/Earrings/The Asya Huggie Earrings/0_primary.png"
            ],
            "prompt": "Hyper-realistic candid lifestyle action photograph, 35mm film still, Kodak Portra 400 color science, creamy bokeh, natural dynamic range, highlight halation, subtle film grain. A refined fair-skinned North Indian young man with a delicate light wheatish complexion, sharp jawline, and modern styled haircut is captured in an elegant candid close-up, gently adjusting The Asya Huggie Earrings from @img2 on his earlobe with masculine fingertips at exact worn scale matching @img1 body_image (product_height_mm=19.77 and product_width_mm=8.47; jewellery dimensions only). The polished 18Kt yellow gold and natural diamond huggie earring catches radiant warm indoor light, fitting flush and securely against his earlobe. He wears a crisp tailored white Oxford shirt with open collar. Elegant ambient background with warm wooden accents in soft focus, zero phone screens, no readable text. Visual style: subtle cinematic film grain / analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Avoid: woman, female, dark skin, deep brown skin, heavily tanned skin, duplicate jewellery, floating packshot, cartoon, 3d render, blurry, distorted hands, text, watermark, phone screen.",
            "alt": "earring styles for guys 2026 lifestyle: fair-skinned Indian man adjusting refined diamond huggie earring on earlobe",
            "caption": "The <a href=\"https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html\">Asya Huggie Earrings</a> in 18Kt gold and natural diamonds delivering flush earlobe comfort and refined sparkle"
        }
    },
    "output": {
        "hero": "output/earring-styles-for-guys-hero-2026.webp",
        "flatlay": "output/earring-styles-for-guys-flatlay-2026.webp",
        "lifestyle": "output/earring-styles-for-guys-lifestyle-2026.webp"
    }
}

manifest_path = ROOT / "output/Week9_Rank90_EarringStylesGuys_type3_prompts.json"
manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print(f"Manifest written to {manifest_path}")
