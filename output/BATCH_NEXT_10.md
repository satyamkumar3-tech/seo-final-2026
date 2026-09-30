# Batch next 10 blogs (Ranks 25–34)

## Important limitation

A plain terminal script **cannot** fully publish these blogs alone, because:

1. Each post needs original drafting (wishes / gift / education) to Master Prompt + Checklist quality  
2. Type 3 images need **Higgsfield Cursor MCP** (`nano_banana_pro`)

What the batch script **does** provide:

- Queue for Ranks 25–34 with live progress  
- Time estimates  
- A ready agent prompt for the next pending rank (`next-prompt`)  
- Status updates after each live URL ships  

## Terminal commands

```bash
cd "/Users/vikasindoria/Documents/Geo and Seo/article generation seo codex"

# One-time (or re-init)
python3 scripts/batch_blog_queue.py init --start 25 --count 10

# Snapshot
python3 scripts/batch_blog_queue.py status
python3 scripts/batch_blog_queue.py estimate

# Live progress window (leave this running)
python3 scripts/batch_blog_queue.py watch

# After each blog finishes (agent or you)
python3 scripts/batch_blog_queue.py mark --rank 25 --status done \
  --url "https://blog.bluestone.com/..." --wp-id 12345 \
  --type3-products "Hero: BIHS1145P21 The Valeria Rose Pendant | Flatlay: ... | Lifestyle: ..."
```

## How to run without retyping “next blog”

In Cursor chat, paste once:

```text
Process the festive batch queue end-to-end.
For each pending rank in article generation seo codex/output/batch_queue.json:
1. Run: python3 scripts/batch_blog_queue.py next-prompt
2. Execute that prompt fully (New publish + Type 3 + xlsx + mark done)
3. Immediately continue to the next pending rank until the queue is empty or I stop you.
Show live URL + Type 3 products after each rank.
```

Or say: **“Continue the batch queue”** after each pause.

## Time estimate (10 blogs)

| Pace | Total |
|------|--------|
| Optimistic (~35 min/blog) | **~5.5–6 hours** |
| Typical (~40–45 min/blog) | **~7 hours** |
| With Type 3 retries (~50 min) | **~8+ hours** |

Sequential only (Higgsfield + WP one blog at a time).
