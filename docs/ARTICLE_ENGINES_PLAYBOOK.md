# Article Engines Playbook

**Version:** 2026-09-29  
**Scope:** All weeks — reusable engine reference for every article in the pipeline  
**Author:** Satyam (WP ID 270271337)

---

## How Engine Selection Works

Engine selection is **not a static lookup**. The pipeline uses a three-layer system:

### Layer 1: Theme Hint (from the Excel queue)
The `theme` column in `SEO Strategy 2026.xlsx` provides a starting hint:
- `Gift Guides` → starts with Engine 1
- `How-to / Education` → starts with Engine 2
- `Design Listicles` → starts with Engine 3
- `Wishes - Festival Day` / `Wishes - Occasion/People` → starts with Engine 4
- `Quotes/Messages/Status` → starts with Engine 5
- `Other` → agent decides based on SERP analysis

### Layer 2: SERP-Driven Validation (during Step 5–7)
After the agent scrapes the top 5 Google India results (Step 5: SERP Intelligence), it **validates or overrides** the theme hint:
- If Google's top 5 are all listicles but the theme says "Education" → agent should use Design Listicle structure
- If the SERP shows comparison content dominates → agent should use Comparison engine
- The agent logs its engine decision with reasoning in the H2 keyword map (Step 7)

### Layer 3: Dynamic Engine Composition (for hybrid keywords)
Some keywords need **elements from multiple engines**. The agent may compose a custom blend:
- Primary engine: determines H2 spine and tone
- Secondary engine: contributes product integration style or specific sections
- Example: "best gold rings for engagement 2027" → Design Listicle (primary) + Gift Guide (secondary: gifting context + recipient awareness)

The agent MUST log which engine(s) it used and why in the Final Report (Step 16).

---

## Universal Rules (All Engines)

- Treat every row as **NEW** unless explicitly instructed otherwise.
- Before drafting, create an H2 keyword map. Label each H2 as one of:
  - `primary-backed`: contains the primary keyword or a close variant
  - `supporting-keyword-backed`: comes from a supplied keyword export with volume/KD
  - `competitor-structure-backed`: comes from a competitor URL structure analysis
  - `serp-consensus-backed`: appears in 3+ of the top 5 SERP pages (table stakes)
  - `intent-inferred`: natural subtopic inferred from intent, without confirmed volume/KD
- Do not claim an H2 has good volume or low KD unless it is backed by sheet data or a keyword export. Intent-inferred H2s are useful for topical coverage but must be reported as inferred.
- No prices, no fake discounts, no fake stats, no competitor criticism.
- For current factual topics (GST, hallmarking, purity rules, buying dates), verify facts from reliable/current sources before publishing.
- Check for near-duplicate intent before publishing.
- Do not use "copy-ready lines" language except for true wishes, messages, quotes, captions, comments, status, or shayari intent (Engines 4 and 5).

## Checkpoint and exactly-once rules

- Use `scripts/article_pipeline.py` for production. Each rank has an atomic step ledger at `output/checkpoints/`.
- Before every major step, verify the checkpoint and recorded external artifact. Skip a `done` step unless the user explicitly requests replacement work.
- WordPress publication must reuse a trusted matching post ID. If an untracked post already owns the intended slug, stop for reconciliation.
- Reuse saved carousel media IDs, Higgsfield job IDs/files, and Type 3 WordPress media IDs. Regenerate or re-upload only a slot explicitly rejected during QA.
- Update the status CSV by rank and product rotation by SKU; do not blindly append duplicate records.

## WordPress category mapping

Set `categories` in the publish config based on article intent:

| Article Intent | Recommended WP Categories |
|---|---|
| General gift guide | `Gift` 554493424 |
| Seasonal/festival gift guide | `Gift` 554493424 + `Festive Wishes` 554493477 |
| Wedding / bride / couple jewellery | `Gift` 554493424 + `Wedding Jewellery` 554493443 |
| Gold buying or purity guide | `Gold` 554493348 + `Jewellery Problem & Solution` 554493465 |
| Jewellery sizing / measurement guide | `Jewellery Problem & Solution` 554493465 + relevant product category |
| Design listicle / style discovery | `Jewellery Trends` 554493317 or `Jewellery & Lifestyle` 554493425 |
| Wishes / quotes / messages | `Quotes & Wishes` 554493415 + occasion-specific category if applicable |
| Cultural significance / heritage | `Jewellery & Lifestyle` 554493425 |
| Care / maintenance | `Jewellery Problem & Solution` 554493465 |
| Comparison / versus | `Gold` 554493348 or `Jewellery Problem & Solution` 554493465 (based on topic) |
| Trend report / forecast | `Jewellery Trends` 554493317 |
| Regional / bridal | `Wedding Jewellery` 554493443 + regional category if available |
| Kids jewellery | `Kids Jewellery` 554493433 |
| Men's jewellery | `Men's Jewellery` 554493434 |

---

## Engine 1: Gift Guide

**Trigger:** `theme = Gift Guides` or keyword contains gifting intent ("gifts for sister", "birthday gift for wife", "rakhi gifts")

### Content structure

1. Intro that identifies recipient, occasion, and buying intent.
2. TL;DR with quick gift direction.
3. Gift decision framework: recipient style, occasion, relationship, budget sensitivity without mentioning prices.
4. Mid-article BlueStone carousel with 5–6 approved SKUs.
5. Editorial product recommendation section with 5–6 named BlueStone SKUs.
6. Each product recommendation must include:
   - product name linked to PDP
   - best-for use case
   - why it works as a gift
   - short gifting tip
7. Occasion/recipient sections (e.g. sister, bride, parents, couple, best friend, mother).
8. Last-minute or safe-choice guidance where useful.
9. FAQs mapped to primary keyword plus natural supporting phrases.
10. Conclusion with a soft buying nudge, not a hard sale.

### Product logic

- Match product category to recipient and occasion:
  - wife / girlfriend / bride: pendants, rings, earrings, bracelets, bangles
  - sister / best friend / teenage girl: earrings, bracelets, rings, charms, light pendants
  - mother / parents: bangles, pendants, earrings, chains, classic designs
  - father / husband / brother: chains, bracelets, men-suitable rings where available
  - couple / wedding: complementary jewellery ideas, bride/groom-aware options
- No prices. Use "budget-friendly", "premium", or "keepsake" as qualitative guidance only.

### Visual logic

- Hero/lifestyle: gifting moment, recipient wearing jewellery, wrapped box, flowers, diyas, festive fabric.
- Flatlay: jewellery with physical props, not blank cards or screens.
- Body_image gate: `@img1` body image + `@img2` design reference. Skip a SKU if no body image exists.
- Image captions should be editorial and product-specific.

---

## Engine 2: Buying Guide / Education

**Trigger:** `theme = How-to / Education` or `category_fit = Buying Guide` or keyword contains educational intent ("how to check gold purity", "bangle size", "GST on gold")

### Content structure

1. Direct answer in the intro.
2. Plain-language explanation of the concept.
3. Step-by-step process or checklist.
4. Tables where useful (purity percentages, measurement steps, size conversion, buyer checklist) — rendered as structured bullet lists, NOT HTML tables.
5. Common mistakes and how to avoid them.
6. When to visit a store, jeweller, or certified professional.
7. Soft BlueStone product or category mention only when useful.
8. FAQs focused on practical buyer questions.
9. Conclusion summarizing the safest action.

### Fact-check gate

Before publishing, verify current facts when the topic touches:
- GST / tax rates
- hallmarking or purity standards (BIS)
- gold buying dates / auspicious days
- measurement charts
- government or BIS rules
- finance-like claims

### Visual logic

- Hero/lifestyle: hands checking jewellery, hallmark loupe, weighing scale, ring sizer, bangle sizer, ruler, clean jewellery counter.
- Product may be present, but the visual should feel educational, not romantic gifting.

---

## Engine 3: Design Listicle

**Trigger:** `theme = Design Listicles` or `category_fit = Jewellery Design` or keyword is design discovery ("gold ring designs", "latest earrings", "trendy necklace designs")

### Content structure

1. Intro that defines the design/search intent.
2. Design categories or style buckets.
3. Who each design suits.
4. Outfit/occasion pairing.
5. Metal, motif, gemstone, and comfort guidance where relevant.
6. Named BlueStone examples where useful.
7. Care/styling tips.
8. FAQs.

### Product logic

- Editorial, not purely promotional.
- Use "best for" mappings: saree styling, daily wear, festive statement, office wear, minimal look, kids-safe styling.
- Avoid forcing a gift framing when the keyword is design discovery.

### Visual logic

- Hero/lifestyle: model wearing the design type, outfit pairing, close-up styling.
- Flatlay: design variations, fabric background, jewellery tray, macro details.

---

## Engine 4: Wishes & Quotes Compilation

**Trigger:** `theme = Wishes - Festival Day` or `Wishes - Occasion/People` or `Quotes/Messages/Status` or keyword contains wishes/quotes intent ("happy diwali wishes", "eid mubarak messages", "birthday wishes for crush")

### Content structure

1. Short intro (2–3 paragraphs) establishing the occasion, its emotional significance, and the role of heartfelt messages.
2. **120+ curated wish/quote/message lines** organized into clearly labeled H2 sections by:
   - Relationship/recipient (for family, for friends, for spouse, for colleagues)
   - Tone (formal, funny/humorous, emotional/heartfelt, short/WhatsApp-ready)
   - Format (one-liners, longer paragraphs, shayari/poetry, image captions, Instagram/status)
3. Each H2 section contains 10–20 wish lines. Lines should feel natural, warm, and culturally appropriate.
4. **Jewellery gift tie-in section** (1 H2, placed mid-to-late article): 3–5 BlueStone product suggestions framed as "pair your wishes with a meaningful gift." This is a soft CTA — the article is content-first, product-secondary.
5. Mid-article carousel with 5–6 gift-appropriate SKUs (if the occasion supports gifting).
6. FAQs: "When is [festival] 2027?", "How to write [occasion] wishes?", "What gift goes with [occasion] wishes?"
7. Conclusion: warm sign-off encouraging readers to share wishes and consider a thoughtful gift.

### Content quality rules

- Wishes must be **original or editorially curated** — not generic placeholder text.
- Mix emotional depth with brevity. Not every line should be 3 sentences; include short punchy lines too.
- For festivals: include culturally accurate references (specific rituals, foods, traditions).
- For occasion/people: include relationship-specific warmth (not just "Happy Birthday [Name]" templates).
- Shayari/Hindi wishes: include only when the keyword or search intent explicitly demands it. Transliterate in Roman script with meaning if needed.
- **No jewellery in the wish lines themselves** — jewellery appears only in the dedicated gift tie-in section.

### Visual logic

- Hero: festive scene, cultural motifs, celebration moments, warm lighting, traditional decorations.
- In-body: occasion-specific imagery (diyas for Diwali, crescent for Eid, rakhi threads for Raksha Bandhan).
- Product images only in the gift tie-in section and carousel, not interspersed with wish lines.

### When NOT to use this engine

- If the keyword is "best [occasion] gifts" → use Gift Guide (Engine 1) instead.
- If the keyword is "[occasion] jewellery designs" → use Design Listicle (Engine 3) instead.
- The distinguishing signal is: does the user want **text to copy-paste and send**, or do they want **products to buy**?

---

## Engine 5: Comparison / Versus

**Trigger:** keyword contains "vs", "versus", "difference between", "which is better", or SERP analysis shows top results are comparison-format content

### Content structure

1. Intro: state both options clearly, acknowledge why the comparison matters to a buyer.
2. **Quick verdict** (1 paragraph): for readers who want the answer immediately.
3. **Option A deep-dive** (2–3 H2s): what it is, key properties, pros, ideal buyer profile.
4. **Option B deep-dive** (2–3 H2s): same structure.
5. **Head-to-head comparison** (1 H2): structured bullet list comparing on 5–8 dimensions (e.g. durability, price range, resale value, cultural significance, skin compatibility, maintenance).
   - Do NOT use HTML tables. Use paired bullet lists: "**Durability:** Gold — excellent long-term. Platinum — superior scratch resistance."
6. **Which should you choose?** (1 H2): decision framework based on buyer persona (daily wearer vs. investor vs. gift buyer vs. bride).
7. BlueStone product tie-in: 2–3 relevant SKUs that exemplify the winning choice, with PDP links.
8. FAQs: practical comparison questions.
9. Conclusion: nuanced recommendation, not a hard "X is better."

### Fact-check gate

Comparison articles are **high-risk for factual errors**. Mandatory verification for:
- Purity percentages, karat equivalences
- Tax treatment differences (GST on gold vs. diamonds vs. platinum)
- Hallmarking requirements by metal type
- Resale value claims (must be qualified, not absolute)
- Hardness/durability claims (use Mohs scale or Vickers where applicable)

### Visual logic

- Hero: side-by-side visual of both options (e.g. gold ring next to platinum ring on a neutral surface).
- In-body: close-up comparison shots showing texture, color, and finish differences.
- No misleading color grading that makes one option look superior.

---

## Engine 6: Cultural Significance / Heritage

**Trigger:** keyword contains "significance of", "meaning of", "history of", "why do we wear", "tradition of", or SERP intent is cultural/informational

### Content structure

1. Intro: state the cultural/spiritual significance directly.
2. **Historical origins** (1–2 H2s): trace the tradition through Indian history, mythology, or regional customs.
3. **Cultural and spiritual meaning** (1–2 H2s): symbolism, rituals, religious context, family traditions.
4. **Regional variations** (1 H2): how the tradition differs across Indian states/communities (South Indian, Bengali, Maharashtrian, Rajasthani, etc.).
5. **Modern interpretations** (1 H2): how contemporary jewellery design honors the tradition while evolving.
6. BlueStone product tie-in: 3–4 products that embody the tradition, with cultural context for each.
7. Carousel: products that represent the tradition across different styles/budgets.
8. FAQs: "What is the significance of [item]?", "Can [item] be worn daily?", "Which [metal/stone] is traditional for [item]?"
9. Conclusion: cultural appreciation and continuity message.

### Content quality rules

- **Cultural accuracy is paramount.** Verify religious and cultural claims. Do not generalize across faiths/regions without qualification.
- Cite historical or scriptural references when making significance claims.
- Be respectful and inclusive — present traditions without judgment.
- Avoid cultural appropriation framing; present from an Indian cultural context.

### Visual logic

- Hero: traditional setting with the jewellery piece in cultural context (temple, pooja thali, bridal preparation).
- In-body: regional styling variations, traditional wearing methods.

---

## Engine 7: Care & Maintenance How-To

**Trigger:** keyword contains "how to clean", "how to store", "how to maintain", "care tips", "polish", or practical maintenance intent

### Content structure

1. Intro: state the care problem directly and why it matters for jewellery longevity.
2. **What you'll need** (1 H2): materials/tools list in bullet format (e.g. soft cloth, mild soap, lukewarm water, soft toothbrush).
3. **Step-by-step process** (1–2 H2s): numbered steps with clear instructions. Each step should be 1–2 sentences.
4. **What NOT to do** (1 H2): common mistakes that damage jewellery (harsh chemicals, ultrasonic cleaners on certain stones, hot water on certain metals).
5. **Storage tips** (1 H2): proper storage to prevent tarnishing, scratching, or tangling.
6. **When to get professional help** (1 H2): signs that home care isn't enough and you should visit a jeweller.
7. Soft BlueStone product mention: only if relevant (e.g. "BlueStone's [product] features a protective rhodium coating that simplifies daily care").
8. FAQs: practical care questions.
9. Conclusion: maintenance schedule recommendation (daily, weekly, monthly).

### Visual logic

- Hero: hands gently cleaning or polishing jewellery, natural light, clean workspace.
- In-body: before/after if applicable, tools laid out, storage solutions.
- Educational feel — NOT glamour/lifestyle.

---

## Engine 8: Trend Report / Seasonal Forecast

**Trigger:** keyword contains "trends", "forecast", "what's trending", "latest [year]", or SERP shows trend-report format dominates

### Content structure

1. Intro: set the trend landscape for the season/year.
2. **Trend overview** (1 H2): macro trends in Indian jewellery (minimalism, statement pieces, lab-grown diamonds, vintage revival, etc.).
3. **Individual trend deep-dives** (3–6 H2s, one per trend): what the trend is, why it's popular, who it suits, how to style it.
4. **BlueStone's take** (1 H2): 4–5 products that align with the trends, with editorial "this is trending because" context.
5. Carousel: trend-aligned products.
6. **What's fading** (1 H2): trends that are losing momentum (handled respectfully — "evolving into" not "dying").
7. **How to adopt trends wisely** (1 H2): investment vs. experimental pieces, layering, mixing trends.
8. FAQs: "What jewellery is trending in [year]?", "Is [trend] still in?", "How to style [trend]?"
9. Conclusion: trend forecast summary for the next 6–12 months.

### Content quality rules

- Reference real fashion/jewellery trends from runway shows, celebrity styling, or social media signals.
- Do not fabricate trends. If citing a trend, it should be verifiable.
- Date-stamp the forecast clearly (e.g. "Trends for Late 2026 – Early 2027").

### Visual logic

- Hero: styled trend showcase, editorial fashion photography feel.
- In-body: individual trend illustrations with model/styling context.

---

## Engine 9: Regional / Bridal Collection

**Trigger:** keyword contains regional identifiers ("South Indian", "Bengali", "Maharashtrian", "Rajasthani", "Kerala") combined with jewellery/bridal intent, or SERP shows regional bridal content dominates

### Content structure

1. Intro: the regional bridal jewellery tradition and its cultural importance.
2. **Essential pieces** (2–3 H2s): the must-have jewellery for this regional bridal look (e.g. South Indian: temple jewellery, waistband, jhumkas, mango mala; Bengali: choker, shakha-pola, nolok).
3. **Styling guide** (1–2 H2s): how each piece is worn, layering order, outfit pairing (saree/lehenga type, fabric, colors).
4. **Modern adaptations** (1 H2): contemporary takes on traditional designs for modern brides.
5. BlueStone products: 4–6 SKUs mapped to the essential pieces, with "this works for [regional tradition] because" context.
6. Carousel: bridal collection products.
7. **Budget planning** (1 H2): qualitative tiers (minimal/essential vs. full traditional vs. luxury statement) — NO prices.
8. FAQs: "What jewellery does a [regional] bride wear?", "How many pieces are needed?", "Can I mix traditional and modern?"
9. Conclusion: celebrating the tradition while embracing personal style.

### Content quality rules

- **Regional accuracy is critical.** Get the specific piece names, wearing traditions, and cultural context right.
- Consult regional wedding customs — don't generalize "Indian bridal" when the keyword is region-specific.
- Include regional language terms for jewellery pieces (e.g. "kamarbandh" not just "waist chain") with English explanations.

### Visual logic

- Hero: bride in full regional attire with traditional jewellery styling.
- In-body: individual piece close-ups, regional outfit pairing, layering demonstrations.

---

## Engine Selection Decision Tree

When the agent reaches Step 7 (Keyword Mapping), it should follow this decision process:

```
1. Read the theme hint from the workbook row
2. Scrape top 5 SERP results (already done in Step 5)
3. Classify the dominant SERP format:
   - Are 3+ results wishes/quotes compilations? → Engine 4 or 5
   - Are 3+ results comparison articles? → Engine 5
   - Are 3+ results listicles? → Engine 3
   - Are 3+ results step-by-step guides? → Engine 7
   - Are 3+ results cultural/significance articles? → Engine 6
   - Are 3+ results trend roundups? → Engine 8
   - Are 3+ results gift recommendations? → Engine 1
   - Are 3+ results educational buying guides? → Engine 2
   - Mixed format? → Use theme hint as primary, blend secondary

4. If SERP format contradicts the theme hint:
   - Log the conflict
   - Follow the SERP (Google is showing what users want)
   - Note the override in the Final Report

5. For hybrid keywords, compose:
   - Primary engine: determines H2 spine and tone (70-80%)
   - Secondary engine: contributes specific sections (20-30%)
```

---

## Status reporting (all engines)

For every completed article, report:

- rank and primary keyword
- live URL and WP post ID
- **engine(s) used and selection reasoning** (theme hint vs. SERP override vs. hybrid composition)
- supporting phrases used
- H2 keyword map (with source labels: primary-backed, supporting, competitor, serp-consensus, intent-inferred)
- competitor URL status
- article length in visible words
- carousel media IDs
- Type 3 media IDs
- product SKUs used
- factual verification note, if applicable
- duplicate/cannibalization note
