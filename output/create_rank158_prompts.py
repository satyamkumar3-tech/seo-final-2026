#!/usr/bin/env python3
"""Generate Type 3 prompt manifest for Week 8 Rank 158: Party Wear Earrings."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

manifest = {
  "workflow": "Higgsfield CLI nano_banana_pro with local product reference images.",
  "wp_post_id": 38850,
  "slug": "party-wear-earrings-2026",
  "output_prefix": "Week8_Rank158_PartyWearEarrings",
  "flatlay_setting": "marble-vanity",
  "flatlay_insert_h2": "Gold Party Wear Earrings: Selecting 18K vs 22K Purity and Hallmarking",
  "lifestyle_insert_h2": "Earlobe Comfort, Weight Distribution, and Backing Security",
  "higgsfield": {
    "model": "nano_banana_pro",
    "aspect_ratio": "16:9",
    "resolution": "2k",
    "count": 1
  },
  "output": {
    "hero": "output/magnific_generated/party-wear-earrings-hero-2026.webp",
    "flatlay": "output/magnific_generated/party-wear-earrings-flatlay-2026.webp",
    "lifestyle": "output/magnific_generated/party-wear-earrings-lifestyle-2026.webp"
  },
  "slots": {
    "hero": {
      "slot": "hero",
      "product_name": "The Aleena Huggie Earrings",
      "code": "BIIP0279S08",
      "GenderTag": "Female",
      "pdp": "https://www.bluestone.com/earrings/the-aleena-huggie-earrings~16735.html",
      "dimensions": "product_height_mm=17.23, product_width_mm=9.5 (explicitly jewellery dimensions, not face or body measurements)",
      "local_reference_images": [
        "ProductImages/raw/Earrings/The Aleena Huggie Earrings/1_body_portrait.png",
        "ProductImages/raw/Earrings/The Aleena Huggie Earrings/2_front.png"
      ],
      "alt": "party wear earrings 2026 hero, The Aleena Huggie Earrings worn by a fair-skinned Indian woman for an evening party",
      "caption": "The Aleena Huggie Earrings as a radiant gold and diamond party wear design",
      "prompt": "Photoreal candid lifestyle portrait photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. The woman is the primary subject and remains candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear luminous fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Mid-shot candid portrait of an elegant fair-skinned Indian woman dressed in an exquisite black velvet evening gown in a softly lit luxury ballroom reception interior, turning gently with a warm natural smile. She is physically wearing The Aleena Huggie Earrings from reference images (@img1 body_image worn scale, @img2 design only) in her pierced earlobes. GENDER LOCK: Female adult woman only. The radiant diamond and gold huggie earrings hug the earlobe comfortably with soft natural contact shadows against skin at EXACT jewellery dimensions: product_height_mm=17.23 x product_width_mm=9.5 (these are jewellery dimensions, not face measurements). Keep the earring size on the woman like @img1 body_image (worn ear scale). Use @img2 only for the earring design. Do not make it bigger for visibility. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the woman; earrings are sharp and true with polished 18K yellow gold sculptural contours and shimmering pavé diamond accents. Bare neck, bare wrists, no other jewellery in frame. Safe margins, full face and ear clearly visible. Avoid: floating jewellery overlay, giant earring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted hands, extra fingers, extra earrings, product shot on plain background, cropped faces, cut-off heads, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
    },
    "flatlay": {
      "slot": "flatlay",
      "product_name": "The Vicky Hoop Earrings",
      "code": "BIIP0427H16",
      "GenderTag": "Female",
      "pdp": "https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html",
      "dimensions": "product_height_mm=14.75, product_width_mm=6.04 (explicitly jewellery dimensions)",
      "local_reference_images": [
        "ProductImages/raw/Earrings/The Vicky Hoop Earrings/2_front.png",
        "ProductImages/seo images/Earrings/The Vicky Hoop Earrings.png"
      ],
      "alt": "party wear earrings 2026 flatlay on marble vanity, The Vicky Hoop Earrings in fine gold",
      "caption": "party wear earrings 2026 styling: <a href=\"https://www.bluestone.com/earrings/the-vicky-hoop-earrings~35071.html\">The Vicky Hoop Earrings</a> in certified 18k fine gold",
      "prompt": "Photoreal high-end jewellery commercial flatlay, HD quality, no distortion of jewellery, identical scale and design (100% match to refs), physically accurate metal and stone detail, natural textures only, no stylization, no illustration. Controlled soft key light with gentle realistic shadows, proper shallow depth of field, balanced exposure with no blown whites and no HDR glare. Shot on DSLR, 16:9 full frame with safe margins. Top-down editorial jewellery flatlay. Flatlay setting ID: marble-vanity. Surface + props: soft white Italian marble vanity surface with subtle grey veining, a pale ivory silk ribbon loosely draped, a minimalist evening perfume bottle silhouette (no readable labels or text), a small polished brass trinket tray, and a pair of The Vicky Hoop Earrings from (@img1 front packshot, @img2 design reference) resting at EXACT jewellery dimensions: product_height_mm=14.75 x product_width_mm=6.04 (jewellery dimensions only). Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. HD hyperreal gold texture with soft specular highlights and authentic ribbed concentric contours. Props stay secondary; jewellery is the clear hero of the composition. No people, no hands, no skin. No floating overlays or cutouts. No readable text, logos, or brand marks on props. Safe margins, entire earrings visible in frame. Avoid: illustration, CGI look, cartoon, fantasy style, over-stylized, plastic glass, fake diamonds, artificial harsh lighting, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, blurry jewellery, distorted jewellery, warped metal, noise, low detail, AI artifacts, painting, digital art, unreal scale, oversized jewellery, floating overlays, cutouts, product diagrams, readable text, logos, people, hands, skin"
    },
    "lifestyle": {
      "slot": "lifestyle",
      "product_name": "The Asya Huggie Earrings",
      "code": "BISA0255D05",
      "GenderTag": "Female",
      "pdp": "https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html",
      "dimensions": "product_height_mm=19.77, product_width_mm=8.47 (explicitly jewellery dimensions, not face or body measurements)",
      "local_reference_images": [
        "ProductImages/raw/Earrings/The Asya Huggie Earrings/1_body_portrait.png",
        "ProductImages/raw/Earrings/The Asya Huggie Earrings/2_front.png"
      ],
      "alt": "party wear earrings 2026 lifestyle close-up, The Asya Huggie Earrings worn on earlobe for evening celebration",
      "caption": "party wear earrings 2026 comfort: <a href=\"https://www.bluestone.com/earrings/the-asya-huggie-earrings~13494.html\">The Asya Huggie Earrings</a> in certified gold",
      "prompt": "Photoreal candid lifestyle photograph with high-end fine jewellery commercial fidelity on the worn piece only. Natural skin texture, no illustration, no CGI. Controlled soft key light with gentle fill, realistic soft shadows, proper shallow depth of field (85mm lens), balanced exposure with no blown whites and no HDR glare. Shot on DSLR, HD quality, 16:9 full frame with safe margins. People are the primary subject and remain candid; the jewellery is an exquisite worn detail that is 100% identical to product refs. Casting (required): fair-skinned Indian woman only. Light wheatish to fair North Indian / urban Indian complexion, clear fair skin tones. Do not use deep brown, dark, or heavily tanned skin. Close-up side profile lifestyle portrait of an attractive fair-skinned Indian woman dressed in an elegant festive champagne silk saree in a luxury private dining lounge, her delicate hand gently adjusting her earring post. She is physically wearing The Asya Huggie Earrings from reference images (@img1 body_image worn scale, @img2 design only) in her earlobes. GENDER LOCK: Female adult woman only. The elongated drop huggie earrings hang gracefully with soft natural contact shadows against skin at EXACT jewellery dimensions: product_height_mm=19.77 x product_width_mm=8.47 (these are jewellery dimensions, not face measurements). Keep the earring size on the woman like @img1 body_image (worn ear scale). Use @img2 only for the earring design. Do not make it bigger for visibility. Visual style: subtle cinematic film grain, analog grain, Kodak Portra color science, gentle highlight halation, creamy bokeh, filmic tonal response with smooth highlight roll-off, editorial color grading, natural dynamic range, filmic contrast. Camera focuses naturally on the woman's ear and jawline; earrings are sharp and true with polished yellow gold links and brilliant diamond facets. Bare neck, bare wrists, no other jewellery in frame. Safe margins, full ear and side profile clearly in frame. Avoid: floating jewellery overlay, giant earring collage, product cutout over people, packshot composited on lifestyle photo, jewellery upscaled for visibility, graphic drawings, cutouts, product diagrams, split screen, illustration, CGI look, cartoon, fake diamonds, studio HDR glow, blown whites, overexposed highlights, washed-out lighting, unreal scale, oversized jewellery, distorted jewellery, warped metal, melted stones, wrong design, distorted hands, extra fingers, extra earrings, product shot on plain background, cropped faces, cut-off heads, readable text, logos, dark skin, deep brown skin, heavily tanned skin"
    }
  }
}

out_path = ROOT / "output/Week8_Rank158_PartyWearEarrings_type3_prompts.json"
out_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print(f"Manifest written to {out_path}")
