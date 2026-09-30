# Cursor rules

These five `.mdc` files are also installed under `.cursor/rules/` in this pack.

If the new Cursor workspace does not auto-load rules, copy:

```bash
mkdir -p .cursor/rules
cp cursor-rules/*.mdc .cursor/rules/
```

Files:

- `new-blogs-only.mdc` — always NEW publish; ignore Optimize
- `carousel-seo-images.mdc` — Type 2 from `ProductImages/seo images/` only
- `image-seo.mdc` — WebP, alts, titles, Type 3 credits + **body_image hard gate**
- `product-rotation-captions-education.mdc` — rotation, captions, education prose, **skip SKU if no body_image**
- `type3-fair-skinned-indians.mdc` — casting lock for people shots
