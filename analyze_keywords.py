import sys, csv, openpyxl, re
from collections import defaultdict

# 1. Load existing topics
wb = openpyxl.load_workbook('SEO Strategy 2026.xlsx', data_only=True)
existing_records = []
all_existing_pks = set()
all_existing_slugs = set()
all_existing_kws = set()

for sname in ['Week 1-2', 'Week 3-4', 'Week 5', 'Week 6', 'Week 7']:
    sheet = wb[sname]
    rows = list(sheet.iter_rows(values_only=True))
    headers = [str(h).strip() if h is not None else '' for h in rows[0]]
    
    pk_idx = headers.index('Primary Keyword') if 'Primary Keyword' in headers else -1
    title_idx = headers.index('Article Title/Angle') if 'Article Title/Angle' in headers else -1
    slug_idx = headers.index('Suggested URL Slug') if 'Suggested URL Slug' in headers else -1
    supp_idx = headers.index('Supporting Keywords') if 'Supporting Keywords' in headers else -1
    theme_idx = headers.index('Theme') if 'Theme' in headers else -1
    cat_idx = headers.index('Category Fit') if 'Category Fit' in headers else -1
    
    for r in rows[1:]:
        if not r or r[0] is None: continue
        pk = str(r[pk_idx]).strip().lower() if pk_idx != -1 and r[pk_idx] else ''
        title = str(r[title_idx]).strip() if title_idx != -1 and r[title_idx] else ''
        slug = str(r[slug_idx]).strip().lower() if slug_idx != -1 and r[slug_idx] else ''
        supp = str(r[supp_idx]).strip().lower() if supp_idx != -1 and r[supp_idx] else ''
        theme = str(r[theme_idx]).strip() if theme_idx != -1 and r[theme_idx] else ''
        cat = str(r[cat_idx]).strip() if cat_idx != -1 and r[cat_idx] else ''
        
        if pk:
            all_existing_pks.add(pk)
            all_existing_kws.add(pk)
        if slug:
            all_existing_slugs.add(slug)
            
        supp_list = [p.strip() for p in re.split(r'\||,', supp) if p.strip()]
        for p in supp_list:
            all_existing_kws.add(p)
            
        existing_records.append({
            'sheet': sname,
            'pk': pk,
            'title': title,
            'slug': slug,
            'theme': theme,
            'cat': cat,
            'supp': supp_list
        })

print(f"Loaded {len(existing_records)} existing rows across Week 1-7.")
print(f"Unique existing primary keywords: {len(all_existing_pks)}")
print(f"Unique existing total keywords (PK + supporting): {len(all_existing_kws)}")

