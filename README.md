# Final SEO Generation Context

Self-contained handoff pack for BlueStone festive SEO blogs + Type 2/Type 3 images.

**Open this folder as the Cursor / Codex workspace root.**

Total size ~780MB (mostly `ProductImages/`).

---

## 1. First message to the new LLM (copy-paste)

```
Workspace root is: final seo generation context

STEP 0 — VERIFY HIGGSFIELD MCP (required before any Type 3 work):
1. Confirm the Higgsfield MCP connector is connected in this client.
2. Call the Higgsfield MCP tool `balance`.
3. Report credits + plan.
4. If balance fails with session expired: remove and re-add the Higgsfield connector, login, then retry balance until it succeeds.
5. Do not generate Type 3 images until balance succeeds.

Then read fully:
- HANDOFF.md
- docs/SOP_ARTICLE_GENERATION.md
- docs/ARTICLE_WORKFLOW.md
- docs/HIGGSFIELD_IMAGE_GENERATION.md (Image SEO + body_image hard gate)
- docs/Blog-SEO-AEO-GEO-Checklist-v2.md
- cursor-rules/new-blogs-only.mdc
- cursor-rules/carousel-seo-images.mdc
- cursor-rules/type3-fair-skinned-indians.mdc
- cursor-rules/image-seo.mdc
- cursor-rules/product-rotation-captions-education.mdc

Hard Type 3 rule: hero + lifestyle MUST use @img1 = raw/BP-PICS body_image + @img2 = design. If body_image is missing for a SKU, SKIP that SKU and pick another. Never generate people shots from packshots alone.

Next: SEO Strategy 2026.xlsx → Week 1-2 → next unfinished NEW rank after 69 (start Rank 70 as NEW if Optimize, or Rank 71). Follow HANDOFF.md.
```

---

## 2. Setup checklist

| Step | Action |
|------|--------|
| 1 | Open **this folder** as workspace root |
| 2 | Connect **Higgsfield MCP** → run `balance` (must succeed) |
| 3 | Copy `.env.example` → `.env` and add `WP_USER` + `WP_APP_PASSWORD` |
| 4 | (Cursor) Copy `cursor-rules/*.mdc` into `.cursor/rules/` if auto-rules do not load from `cursor-rules/` |
| 5 | Confirm `ProductImages/seo images/` and `ProductImages/raw/` exist |
| 6 | Read `HANDOFF.md` and continue the queue |

---

## 3. Folder map

| Path | Purpose |
|------|---------|
| `HANDOFF.md` | Queue state + opening prompt |
| `docs/` | SOP, workflow, Higgsfield Type 3, checklist, master prompt |
| `KnowledgeBase/` | Writing + Product guides (canonical copies) |
| `cursor-rules/` | Always-on Cursor rules (body_image gate, NEW blogs, carousel SEO) |
| `SEO Strategy 2026.xlsx` | Week 1-2 execution queue |
| `Seo Products - consolidated.csv` | Canonical SKUs + GenderTag + mm sizes |
| `ProductImages/raw/` | Multi-angle + body portraits for Type 3 refs |
| `ProductImages/seo images/` | Type 2 carousel source PNGs only |
| `scripts/` | `publish_week1_generic.py`, `patch_week1_type3_generic.py`, etc. |
| `templates/` | Type 3 prompt templates |
| `output/product_rotation.json` | Recent Type 3 trios + flatlay settings |
| `output/publish_configs/` | Rank publish JSON configs |
| `image-generation-handoff/` | Extra Type 3 / Magnific notes |
| `references/` | Worked examples |

---

## 4. What was intentionally left out

- Live `.env` secrets (use `.env.example` → create your own `.env`)
- Generated Type 3 WebPs (`magnific_generated/`) — regenerate via Higgsfield
- Full git history
- `google_product_feed.csv` (optional bulk feed; not required for the blog queue)

---

## 5. Policy snapshot

- **NEW blogs only** — ignore sheet `Action = Optimize`; create a fresh slug
- Carousel = `ProductImages/seo images/` only → WebP
- Type 3 = Higgsfield `nano_banana_pro`, 16:9, 2k, count 1 × 3 slots
- Body image hard gate for hero + lifestyle (see rules above)
- Author Vikas `270271338`; categories Festive + Quotes
