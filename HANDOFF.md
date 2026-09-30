# Final SEO Generation Context — Handoff

**Updated:** 2026-09-29  
**Workspace:** Open folder `seo final 2026` as Cursor / Codex / AGY root  
**Active queue:** **Week 9.** All previous weeks (1–8) are complete or paused. Do not read Week 6 or Week 7 queue rows, status files, or checkpoints.  

### Week 9 pipeline (active)

- Start Week 9 work through `scripts/article_pipeline.py`; it reads the full `Week 9` worksheet and maintains `output/checkpoints/week9_rank{rank}.json`.
- Use `--next` to select the first unfinished row whose Action is `New`. Completed, Done, and Skip-Existing rows are not regenerated.
- Week 9 has its own manifest, lock, checkpoint namespace, and status file: `output/Week9_Blog_Queue_status.csv`.
- The ARTICLE_ENGINES_PLAYBOOK.md engines (Gift Guide / Buying Guide / Design Listicle) remain reusable article-engine references. Do not read Week 6 queue data.
- Current next command: `python3 -B scripts/article_pipeline.py produce --next --manifest output/article_pipeline.json --timers --approve-for-me`.

---

## STEP 0 — Higgsfield status (do this first)

Before competitor analysis or Type 3:

1. Confirm **Higgsfield** is connected in this client.
2. Preferred MCP path: call MCP tool **`balance`**. Current working fallback: CLI `higgsfield account status --json`.
3. Report **credits + plan** in your reply.
4. If you get `session expired` / auth failure: ask the user to **remove and re-add** the Higgsfield connector or rerun `higgsfield auth login`, complete login, then retry status/balance until it succeeds.
5. **Do not** start Type 3 generation until balance/status works.

Type 3 model: `nano_banana_pro`, aspect `16:9`, resolution `2k`, `count: 1` per slot (hero / flatlay / lifestyle). Run **maximum 2 simultaneous generations**. If a Higgsfield queue/generation error occurs, wait **40-50 seconds** before the second try.

---

## Policy (mandatory)

**New blogs only.** Ignore sheet `Action = Optimize`.

- Always create a **new** WP post with a fresh slug (`scripts/publish_week1_generic.py` + `output/publish_configs/rankXX.json`).
- Do **not** patch old BlueStone URLs for remaining queue rows (old URL = reference only).
- See `.cursor/rules/new-blogs-only.mdc` (also mirrored in `cursor-rules/`).

### Body image hard gate (hero + lifestyle)

- `@img1` = raw / CDN **`BP-PICS` body_image** (or `1_body_portrait`)
- `@img2` = front / design only
- If **no body_image** for a SKU → **skip that SKU** and pick another with a body shot
- Never generate people hero/lifestyle from packshots alone
- Flatlay may use 3–4 packshot angles

### Guide-only keyword / competitor / length gates

- Week 6 uses a separate cluster playbook: read `docs/ARTICLE_ENGINES_PLAYBOOK.md` and choose the article engine from CSV `theme` before drafting.
- Competitor pass is required **only when the sheet row provides a competitor/CaratLane URL**. If the URL is blank, do **not** manually invent or search one unless the user asks; log: `No competitor URL in row, proceeded per guide from keyword cluster/Semrush page/supporting KWs`.
- Supporting keywords must be mapped visibly into H2s, body, FAQ, and schema where natural. Do not publish until this is checked.
- Full article length is mandatory even when generating in parallel. For captions/quotes/listicles, target **120+ list lines** unless the guide row clearly requires a different format.
- “Copy-ready lines” phrasing is allowed only for true quotes/captions/messages/wishes articles. For gift guides, buying guides, and education/how-to posts, use section-specific explanatory leads or omit the lead; never use the copy-ready fallback.
- Gift-guide articles must recommend named BlueStone products in the body, not only in the carousel. Add a “recommended gifts” section with 5–6 linked SKUs, each mapped to a gift reason such as romantic pendant, first Karwa Chauth ring, easy earrings, traditional bangle, luxury keepsake, or everyday bracelet. No prices.
- Type 3 prompts must keep the current style language: subtle cinematic film grain / analog grain, Kodak Portra color science, highlight halation, creamy bokeh, filmic tonal response / highlight roll-off, editorial color grading, natural dynamic range / filmic contrast.
- Type 3 prompts must avoid empty phones/screens/cards/boards/placards/readable text. Use physical props instead: flowers, diyas, ceramic cups, brass bowls, ribbons, folded fabric, wrapped gift boxes, trays, and closed books turned away or blurred.
- Product dimensions are jewellery dimensions only. Never write `face_height_mm` / `face_width_mm`; use `product_height_mm` / `product_width_mm`, and state these are not face/body measurements.

---

## Recently completed (do not redo)

| Rank | URL | Type3 (flatlay setting) |
|------|-----|-------------------------|
| Week 6 Rank 4 | Skipped: existing intent at https://blog.bluestone.com/best-gift-for-sister-on-raksha-bandhan-2026/ (WP 32319) | No new media created |
| Week 6 Rank 3 | https://blog.bluestone.com/bangle-size-2026/ | Luvee / Tetyana / Muricelle (`desk-kraft`) |
| Week 6 Rank 2 | https://blog.bluestone.com/how-to-check-gold-purity-2026/ | Luvee / Tetyana / Muricelle (`study-desk`) |
| Week 6 Rank 1 | https://blog.bluestone.com/karwa-chauth-gift-for-wife-2026/ | Teshvarya / Ebony / Faliha (`festive-mantel`) |
| Week 3-4 Rank 106 | https://blog.bluestone.com/bestie-captions-for-instagram-2026/ | Lumeelle / Rafia / Asya (`cafe-tray`) |
| Week 3-4 Rank 105 | https://blog.bluestone.com/farewell-message-for-seniors-2026/ | Aagarna / Quinn / Nettile (`gift-wrapping-station`) |
| Week 3-4 Rank 104 | https://blog.bluestone.com/good-times-caption-2026/ | Sarvanya / Haily / Vicky (`linen-bedside`) |
| Week 3-4 Rank 103 | https://blog.bluestone.com/student-success-motivational-quotes-2026/ | Thaloria / Anya / Ursa (`study-desk`) |
| Week 3-4 Rank 102 | https://blog.bluestone.com/busy-people-quotes-2026/ | Protecteur / Muricelle / Skein (`cafe-tray`) |
| Week 3-4 Rank 101 | https://blog.bluestone.com/unity-quotes-2026/ | Ixea / Channing / Kricia (`windowsill-daylight`) |
| Week 1-2 Rank 101 | https://blog.bluestone.com/birthday-wishes-for-bhabhi-2026/ | Existing published post 31028 verified 2026-07-30 |
| Week 1-2 Rank 102 | https://blog.bluestone.com/diwali-banner-2026/ | Existing published post 31064 verified 2026-07-30 |
| Week 1-2 Rank 103 | https://blog.bluestone.com/birthday-wishes-2026/ | Existing published post 31092 verified 2026-07-30 |
| Week 1-2 Rank 104 | https://blog.bluestone.com/congratulations-wishes-2026/ | Existing published post 31110 verified 2026-07-30 |
| Week 1-2 Rank 105 | https://blog.bluestone.com/friendship-day-shayari-2026/ | Existing published post 31164 verified 2026-07-30 |

Track rotation: `output/product_rotation.json`.

---

## Handoff prompt for a new LLM session

Copy and paste this at the start of a new LLM session to hand off the pipeline:

```
Workspace root: seo final 2026

STEP 0 — VERIFY HIGGSFIELD FIRST:
1. Call Higgsfield MCP tool `balance`, or CLI `higgsfield account status --json`.
2. Report credits + plan.
3. If session expired: ask user to remove/re-add connector or rerun `higgsfield auth login`.
4. Do not start Type 3 generation until balance/status succeeds.

Read these fully before doing any task work:
- HANDOFF.md
- docs/SOP_ARTICLE_GENERATION.md
- docs/ARTICLE_WORKFLOW.md
- docs/ARTICLE_ENGINES_PLAYBOOK.md
- docs/HIGGSFIELD_IMAGE_GENERATION.md
- docs/Blog-SEO-AEO-GEO-Checklist-v2.md
- cursor-rules/new-blogs-only.mdc
- cursor-rules/carousel-seo-images.mdc
- cursor-rules/type3-fair-skinned-indians.mdc
- cursor-rules/image-seo.mdc
- cursor-rules/product-rotation-captions-education.mdc

Active pipeline: Week 9
Orchestrator: scripts/article_pipeline.py
Status file: output/Week9_Blog_Queue_status.csv
Checkpoints: output/checkpoints/week9_rank{N}.json
Author: Satyam (WP ID 270271337)
Byline: By Satyam, BlueStone Editorial

To run next unfinished rank:
  python3 -B scripts/article_pipeline.py produce --next --manifest output/article_pipeline.json --timers --approve-for-me

To run a specific rank:
  python3 -B scripts/article_pipeline.py produce --ranks N --manifest output/week9_N.json --timers --approve-for-me

Env: .env with WP_USER + WP_APP_PASSWORD
Execute end-to-end and report the live URL when done.
```

---

## WordPress API

| Item | Value |
|------|-------|
| API base | `https://blog.bluestone.com/wp-json/wp/v2/` |
| Author | **Satyam** — `270271337` |
| On-page byline | `By Satyam, BlueStone Editorial` |
| BlogPosting schema author | `Satyam` |
| Categories | Configurable per post. Use `docs/ARTICLE_ENGINES_PLAYBOOK.md` category mapping for all weeks. |
| Auth | `WP_USER` + `WP_APP_PASSWORD` in `.env` |

---

## Scripts

| Flow | Script |
|------|--------|
| Week 9 orchestration (produce) | `scripts/article_pipeline.py produce --ranks N --manifest output/week9_N.json --timers --approve-for-me` |
| Week 9 orchestration (auto-next) | `scripts/article_pipeline.py produce --next --manifest output/article_pipeline.json --timers --approve-for-me` |
| Status check | `scripts/article_pipeline.py status --manifest output/week9_N.json` |
| Checkpoint inspect | `scripts/article_checkpoint.py show --path output/checkpoints/week9_rankN.json` |
| Checkpoint mark | `scripts/article_checkpoint.py mark --path output/checkpoints/week9_rankN.json --step <step> --status done` |

### Week 9 run safety

- Start Week 9 work through `scripts/article_pipeline.py`; it maintains `output/checkpoints/week9_rank{rank}.json`.
- A completed rank, a non-New row, or a terminal status row is skipped unless `--force` is deliberately supplied.
- `--next` selects the next unfinished `Action = New` rank from the full Week 9 worksheet.
- An explicitly approved clean rerun uses `--ranks N --restart`; the old checkpoint is moved into `output/checkpoints/archive/` for audit instead of being deleted.
- `--allow-existing-intent` is a one-off user-approved exception for a differently slugged semantic conflict. It requires `--restart`, preserves the older article, and never permits an exact target-slug duplicate.
- Only one Week 9 production runner may use this workspace at a time. The lock prevents simultaneous article jobs from colliding in WordPress, status, or product rotation.
- Production agents must not modify shared helper scripts. The wrapper keeps terminal output concise while timestamped logs retain full details.

### Week 6 run safety

- Start Week 6 work through `scripts/week6_pipeline.py`; it maintains `output/checkpoints/week6_rank{rank}.json`.
- A published/completed rank is skipped unless `--force` is deliberately supplied.
- Only one Week 6 production runner may use this workspace at a time. The workspace lock prevents two agents from editing shared scripts or status files concurrently.
- Production agents must not modify shared helper scripts. Missing pipeline capability is a blocker to report, not a reason to rewrite shared code mid-article.
- Publishing reuses a trusted matching WordPress post ID, refuses an untracked duplicate slug, reuses carousel media checkpoints, reuses completed Higgsfield jobs, and reuses uploaded Type 3 media.
- The terminal shows concise progress and the final URL. Full raw Codex output remains available in the timestamped `.log`; use `--verbose` only for diagnosis.

---

## Image SEO (mandatory)

Canonical: `docs/HIGGSFIELD_IMAGE_GENERATION.md` → **Image SEO**

- WebP only; unique KW-led alts; WP media titles on upload
- Carousel alt: `{KW/occasion + year} gift idea: {Exact Product Name}`
- Type 3 filenames: `{occasion}-{hero|flatlay|lifestyle}-{year}.webp`
- Gutenberg: `sizeSlug: full` only; figcaptions on flatlay + lifestyle
- Featured hero must not also appear in body

---

## After each publish

1. Update `SEO Strategy 2026.xlsx` → active week sheet → Bluestone Blog URL + Execution Note  
2. Update `output/product_rotation.json` (Type 3 trio + flatlay setting)  
3. Proceed to the next unfinished NEW rank
