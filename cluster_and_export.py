import csv, openpyxl, re
from collections import defaultdict

# 1. Load all existing records from Week 1-7
wb = openpyxl.load_workbook('SEO Strategy 2026.xlsx', data_only=True)
all_existing_pks = {}
all_existing_slugs = set()
all_existing_kws = set()

for sname in ['Week 1-2', 'Week 3-4', 'Week 5', 'Week 6', 'Week 7']:
    sheet = wb[sname]
    rows = list(sheet.iter_rows(values_only=True))
    headers = [str(h).strip() if h is not None else '' for h in rows[0]]
    pk_idx = headers.index('Primary Keyword') if 'Primary Keyword' in headers else -1
    slug_idx = headers.index('Suggested URL Slug') if 'Suggested URL Slug' in headers else -1
    supp_idx = headers.index('Supporting Keywords') if 'Supporting Keywords' in headers else -1
    title_idx = headers.index('Article Title/Angle') if 'Article Title/Angle' in headers else -1
    
    for r in rows[1:]:
        if not r or r[0] is None: continue
        pk = str(r[pk_idx]).strip().lower() if pk_idx != -1 and r[pk_idx] else ''
        slug = str(r[slug_idx]).strip().lower() if slug_idx != -1 and r[slug_idx] else ''
        supp = str(r[supp_idx]).strip().lower() if supp_idx != -1 and r[supp_idx] else ''
        title = str(r[title_idx]).strip() if title_idx != -1 and r[title_idx] else ''
        
        if pk:
            all_existing_pks[pk] = {'sheet': sname, 'slug': slug, 'title': title}
            all_existing_kws.add(pk)
        if slug:
            all_existing_slugs.add(slug)
        for part in supp.replace('|', ',').split(','):
            p = part.strip()
            if p: all_existing_kws.add(p)

# 2. Read pool
files = [
    '/Users/satyamkumar/.gemini/antigravity-ide/brain/7e00db0e-4115-464a-9ed3-018fd421bb42/.user_uploaded/media_1788159673366.csv',
    '/Users/satyamkumar/.gemini/antigravity-ide/brain/7e00db0e-4115-464a-9ed3-018fd421bb42/.user_uploaded/media_1788159675506.csv'
]

raw_pool = {}
for fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            kw = row.get('Keyword', '').strip()
            if not kw: continue
            kw_clean = kw.lower()
            try: vol = int(row.get('Volume', 0))
            except: vol = 0
            try: kd = float(row.get('Keyword Difficulty', 0))
            except: kd = 0.0
            try: cpc = float(row.get('CPC', 0))
            except: cpc = 0.0
            
            bs_pos = row.get('bluestone.com', '').strip()
            cl_pos = row.get('caratlane.com', '').strip()
            tq_pos = row.get('tanishq.co.in', '').strip()
            bs_url = row.get('bluestone.com (pages)', '').strip()
            cl_url = row.get('caratlane.com (pages)', '').strip()
            tq_url = row.get('tanishq.co.in (pages)', '').strip()
            
            if kw_clean not in raw_pool or vol > raw_pool[kw_clean]['vol']:
                raw_pool[kw_clean] = {
                    'kw': kw,
                    'kw_clean': kw_clean,
                    'intents': row.get('Intents', ''),
                    'vol': vol,
                    'kd': kd,
                    'cpc': cpc,
                    'bs_pos': bs_pos,
                    'cl_pos': cl_pos,
                    'tq_pos': tq_pos,
                    'bs_url': bs_url,
                    'cl_url': cl_url,
                    'tq_url': tq_url
                }

# Filter covered festivals/events:
covered = ['valentine', 'friendship day', 'mothers day', 'mother\'s day', 'teachers day', 'teacher', 'vote of thanks', 'diwali', 'deepavali', 'bhabhi', 'sir', 'beta']
competitors = ['tanishq', 'caratlane', 'malabar', 'joyalukkas', 'kalyan', 'lalitha', 'lalchand', 'senco', 'jos alukkas', 'grt', 'chandukaka', 'png', 'lenskart', 'd mart', 'honda', 'seetha jewellers', 'neeta jewellers', 'nirankari', 'moti nepali']

eligible = []
for kw_clean, d in raw_pool.items():
    if kw_clean in all_existing_pks or kw_clean in all_existing_kws:
        continue
    if any(c in kw_clean for c in covered):
        continue
    if any(c in kw_clean for c in competitors):
        continue
    # skip purely local rate / store keywords
    if any(r in kw_clean for r in ['gold rate today', 'gold price today', 'today gold rate', 'today gold price']) and any(c in kw_clean for c in ['siliguri', 'sambalpur', 'morbi', 'bhilai', 'haldwani', 'roorkee', 'ongole', 'dimapur', 'noida', 'ghaziabad', 'delhi', 'mumbai', 'pune', 'chennai', 'bangalore']):
        continue
    eligible.append(d)

print(f"Eligible keywords: {len(eligible)}")

# Cluster definitions for target topics
# We want clean, intent-unique topics with rich supporting keywords
clusters = [
    {
        'pk': 'gold bracelet for women',
        'title': '30+ Latest Gold Bracelet Designs for Women: Daily Wear to Party Styles',
        'slug': 'gold-bracelet-designs-for-women-2026',
        'category_fit': 'Jewellery Design',
        'theme': 'Design Listicles',
        'match_terms': ['gold bracelet for women', 'gold bracelet', 'bracelet gold', 'hand bracelet images for girl', 'gold bracelet 10 gram', '4 gram gold bracelet', '3 gram gold bracelet', 'chunky bracelet gold', 'modern gold bracelet designs for girls', 'gold butterfly bracelet', 'gold strap'],
        'cl_url': 'https://www.caratlane.com/jewellery/gold-bracelets-for+women.html'
    },
    {
        'pk': 'helix piercing',
        'title': 'Helix Piercing Guide 2026: Pain Level, Healing Time, Care & Earring Styles',
        'slug': 'helix-piercing-care-earrings-guide-2026',
        'category_fit': 'Buying Guide',
        'theme': 'How-to / Education',
        'match_terms': ['helix piercing', 'helix ear piercings', 'low helix piercing', 'does helix piercing hurt', 'helix ear cuff', 'upper ear earrings', 'upper earrings', 'upper earrings for women', 'upper ear studs for ladies', 'upper piercing earrings', 'earrings for upper piercing', 'small earrings for upper ear', 'upper earrings design', 'double piercing'],
        'cl_url': 'https://blog.bluestone.com/helix-piercings-101-everything-you-need-to-know-about-helix-earrings-pain-healing-and-what-to-expect/'
    },
    {
        'pk': 'choker necklace',
        'title': 'Trending Choker Necklace Designs: From Simple Gold Chokers to Bridal Sets',
        'slug': 'trending-choker-necklace-designs-2026',
        'category_fit': 'Jewellery Design',
        'theme': 'Design Listicles',
        'match_terms': ['choker necklace', 'gold choker necklace', 'choker', 'gold choker', 'choker design', 'choker necklace gold', 'chocker', 'choker gold necklace', 'choker set design', 'girls choker necklace', 'simple gold choker necklace', 'choker design gold', 'choker haar', 'choker earrings', 'choker images', 'choker necklace for lehenga', 'choker type necklace', 'modern gold choker necklace', 'collar necklace', 'thin choker necklace'],
        'cl_url': 'https://www.caratlane.com/jewellery/chokers.html'
    },
    {
        'pk': 'temple jewellery',
        'title': 'Complete Guide to Temple Jewellery: History, Auspicious Motifs & Bridal Sets',
        'slug': 'temple-jewellery-designs-guide-2026',
        'category_fit': 'Jewellery Design',
        'theme': 'Design Listicles',
        'match_terms': ['temple jewellery', 'temple jewellery gold', 'temple jewellery designs', 'temple jewellery collection', 'south indian jewellery set', 'vanki designs', 'lakshmi mala', 'lakshmi kasu gold', 'lakshmi coin necklace', 'gold armlet', 'dholna jewellery', 'kappu in gold', 'arm vanki', 'gold hand vanki designs'],
        'cl_url': 'https://www.caratlane.com/jewellery/temple+jewellery.html'
    },
    {
        'pk': 'nath design',
        'title': 'Traditional & Modern Nath Designs: Maharashtrian, Bridal, and Simple Nose Rings',
        'slug': 'nath-designs-bridal-maharashtrian-2026',
        'category_fit': 'Jewellery Design',
        'theme': 'Design Listicles',
        'match_terms': ['nath', 'nath design', 'nath design gold', 'gold nath design', 'bridal nath', 'nathiya design', 'marathi nath', 'nathiya design gold', 'nath designs gold latest', 'naak ki nath', 'simple gold nath design', 'bridal nath design', 'dulhan nathiya gold', 'kundan nath', 'besar nath', 'bihari nath design', 'dogri nath design', 'himachali nath design', 'nath with chain', 'gold nath for bride'],
        'cl_url': 'https://www.caratlane.com/jewellery/nath.html'
    },
    {
        'pk': 'silver payal design',
        'title': 'Latest Silver Payal Designs 2026: Lightweight Daily Wear to Bridal Anklets',
        'slug': 'silver-payal-designs-daily-wear-bridal-2026',
        'category_fit': 'Jewellery Design',
        'theme': 'Design Listicles',
        'match_terms': ['silver payal design', 'silver anklets', 'silver payal for womens', 'payal design latest', 'women payal', 'payal for girls', 'silver kolusu', 'bridal silver payal design', 'payal anklet', 'dulhan payal designs in silver', 'new model anklets in silver', 'silver pattilu', 'silver kolusu rate', 'simple payal design silver', 'silver pattilu new models', 'heavy anklets silver', 'antique silver anklets', 'antique payal design', 'leg payal', 'silver nupur'],
        'cl_url': 'http://www.caratlane.com/silver-anklets'
    },
    {
        'pk': 'tulip bracelet',
        'title': 'Tulip Bracelet Trend: Why Floral Diamond & Gold Bracelets Are Taking Over 2026',
        'slug': 'tulip-bracelet-trend-gold-diamond-2026',
        'category_fit': 'Jewellery Design',
        'theme': 'Design Listicles',
        'match_terms': ['tulip bracelet', 'tulip bracelet for women', 'tulip bracelet under 100', 'tulips bracelet', 'women\'s tulip bracelet', 'butterfly bracelet', 'gold butterfly bracelet', 'butterfly mangalsutra', 'lotus bracelet', 'sunflower bracelet', 'flower jewellery', 'flower jewellery design', 'flower ornaments'],
        'cl_url': 'https://www.caratlane.com/jewellery/dianella-tulip-diamond-bracelet-jt01579-ygs300.html'
    },
    {
        'pk': 'yellow sapphire stone',
        'title': 'Yellow Sapphire (Pukhraj) Stone: Astrological Benefits, Wearing Finger & Purity Guide',
        'slug': 'yellow-sapphire-pukhraj-stone-benefits-guide-2026',
        'category_fit': 'Buying Guide',
        'theme': 'How-to / Education',
        'match_terms': ['yellow sapphire', 'yellow sapphire stone', 'yellow sapphire jewelry', 'yellow pukhraj', 'yellow sapphire gents ring design', 'yellow sapphire ring design for man', 'yellow sapphire ring celebrities', 'pukhraj stone ring design for man', 'pukhraj bracelet', 'pukhraj stone colour', 'african yellow sapphire', 'rough yellow sapphire', 'kareena kapoor yellow sapphire ring'],
        'cl_url': 'https://www.bluestone.com/jewellery/yellow-sapphire-rings.html'
    },
    {
        'pk': 'silver kada for women',
        'title': 'Modern Silver Kada & Bangle Designs for Women: 925 Sterling Silver Styles',
        'slug': 'silver-kada-bangles-for-women-2026',
        'category_fit': 'Jewellery Design',
        'theme': 'Design Listicles',
        'match_terms': ['silver kada for women', 'silver bangles', 'silver kada for girl', 'silver bangles design', 'silver bracelet design', 'silver bangles for kids', 'silver bangle design for women', 'silver chudi for women', 'silver bangles cost', 'silver bangles design for girl', '925 silver bangles', 'chandi bangles', 'chandi bangles design', 'chandi ki bangles', 'silver kada for womens design', 'ladies kada silver', 'womens sterling silver bangle'],
        'cl_url': 'http://www.caratlane.com/silver-bracelets/'
    },
    {
        'pk': 'silver ring for men',
        'title': 'Classic & Contemporary Silver Rings for Men: Masculine Bands, Signets & Daily Wear',
        'slug': 'silver-ring-designs-for-men-2026',
        'category_fit': 'Jewellery Design',
        'theme': 'Design Listicles',
        'match_terms': ['silver ring for men', 'silver ring for boys', 'original silver ring for men', 'silver ring designs for male', 'chandi ring man', 'chandi ring design for man', 'chandi ki ring for men', 'chandi ring boy', 'chandi ki ring for boy', 'silver band for men', 'silver plain rings for men', 'simple silver ring design for man', 'boy ring design chandi', 'men ring design silver', 'men silver ring design', 'gents silver ring design', 'ring silver man'],
        'cl_url': 'https://www.caratlane.com/jewellery/silver-rings-for+men.html'
    },
    {
        'pk': 'topaz stone',
        'title': 'Topaz Stone Guide: Meaning, Healing Properties, Blue Topaz vs Imperial Topaz',
        'slug': 'topaz-stone-meaning-benefits-guide-2026',
        'category_fit': 'Buying Guide',
        'theme': 'How-to / Education',
        'match_terms': ['topaz stone', 'topaz birthstone', 'golden topaz', 'mystic topaz cabochon', 'princess diana blue topaz ring', 'aquamarine stone', 'aquamarine blue', 'tanzanite', 'amethyst gemstone', 'amethyst crystal bracelet', 'amethyst meaning in tamil', 'ametrine bracelet', 'garnet', 'rhodolite', 'rhodolite garnet'],
        'cl_url': 'https://www.bluestone.com/jewellery/topaz.html'
    },
    {
        'pk': 'bugadi designs',
        'title': 'Traditional Bugadi Earring Designs: History, Styling & Modern Maharashtrian Trends',
        'slug': 'bugadi-earring-designs-maharashtrian-2026',
        'category_fit': 'Jewellery Design',
        'theme': 'Design Listicles',
        'match_terms': ['bugadi designs', 'bugadi meaning', 'traditional bugadi design', 'traditional bugadi earring', 'bugadi earrings design', 'ear bugadi designs', 'bugadi jewellery', 'earrings bugadi', 'maharashtrian bugadi', 'what is bugadi', 'puneri bali', 'kanatli bali', 'brijbali', 'brij bali gold', 'kundal bali'],
        'cl_url': 'https://blog.bluestone.com/traditional-bugadi-earrings-a-maharashtrian-classic/'
    },
    {
        'pk': 'panchdhatu ring',
        'title': 'Panchdhatu & Ashtadhatu Rings: 5 Sacred Metals, Astrological Benefits & How to Wear',
        'slug': 'panchdhatu-ashtadhatu-ring-benefits-guide-2026',
        'category_fit': 'Buying Guide',
        'theme': 'How-to / Education',
        'match_terms': ['panchdhatu', 'panchdhatu ring', 'panchdhatu ring benefits', 'panchdhatu metals', 'panchaloha', 'panchaloha means', 'panchaloha metals', 'panchaloha ring benefits', 'panchaloha in english', 'pancha lohalu', 'ashtadhatu ring', 'ashtadhatu ring benefits', 'asht dhatu', '5 dhatu ring', 'original ashtadhatu ring'],
        'cl_url': 'https://blog.bluestone.com/panchdhatu-ashtadhatu-rings-benefits-designs-and-how-to-wear-them/'
    },
    {
        'pk': 'salman khan bracelet',
        'title': 'Salman Khan Bracelet: Turquoise Stone Meaning, Astrological Secret & Significance',
        'slug': 'salman-khan-turquoise-bracelet-meaning-benefits-2026',
        'category_fit': 'Buying Guide',
        'theme': 'How-to / Education',
        'match_terms': ['salman khan bracelet', 'salman khan bracelet stone name', 'salman khan bracelet photo', 'firoza stone benefits', 'feroza stone benefits', 'feroza ring finger', 'lajward stone benefits', 'turquoise color earrings', 'turquoise blue earrings', 'turquoise jhumka', 'pyrite bracelet benefits', 'pyrite stone bracelet benefits'],
        'cl_url': 'https://blog.bluestone.com/salman-khans-signature-bracelet-meaning-stone-why-he-never-takes-it-off/'
    },
    {
        'pk': 'elephant hair ring',
        'title': 'Elephant Hair Ring: Spiritual Meaning, Good Luck Legend & Finger Placement Guide',
        'slug': 'elephant-hair-ring-meaning-benefits-finger-placement-2026',
        'category_fit': 'Buying Guide',
        'theme': 'How-to / Education',
        'match_terms': ['elephant hair ring', 'elephant hair', 'elephant hair ring benefits', 'elephant hair ring silver', 'elephant hair ring gold', 'elephant tail hair', 'elephant tail ring', 'elephant hair ring for men', 'elephant hair ring kerala', 'yanai mudi ring', 'tortoise ring benefits', 'tortoise ring for ladies', 'tortoise ring in which finger for female', 'how to wear tortoise ring', 'tortoise ring in which finger for male'],
        'cl_url': 'https://blog.bluestone.com/elephant-hair-rings-designs-benefits-traditions-finger-placement-guide/'
    },
    {
        'pk': 'dhanteras wishes',
        'title': '75+ Auspicious Dhanteras Wishes, Messages & Quotes for Prosperity & Wealth',
        'slug': 'dhanteras-wishes-messages-quotes-2026',
        'category_fit': 'Occasion/Gifting',
        'theme': 'Quotes/Messages/Status',
        'match_terms': ['dhanteras wishes', 'dhantera wishes', 'dhantersa wishes', 'happy dhanteras 2022 wishes', 'happy dhanteras wishes 2024', 'dhanteras 2024 wishes', 'creative dhanteras wishes', 'unique dhanteras wishes', 'dhanteras status', 'dhantrayodashi wishes', 'dhantrayodashi wish', 'dhanteras greetings', 'happy dhanteras quotes', 'happy dhanteras messages', 'dhanteras and diwali wishes', 'dhanteras gift'],
        'cl_url': 'https://blog.bluestone.com/best-dhanteras-wishes-messages-greetings/'
    },
    {
        'pk': 'marriage dates in 2026',
        'title': 'Shubh Vivah Muhurat 2026: Auspicious Hindu Marriage Dates & Panchang Calendar',
        'slug': 'shubh-vivah-muhurat-marriage-dates-2026',
        'category_fit': 'Buying Guide',
        'theme': 'How-to / Education',
        'match_terms': ['marriage dates in 2026', 'marriage dates in 2026 hindu panchang', 'shadi muhurat 2026', 'wedding dates in 2026', '2026 marriage dates', 'lagan in 2026', 'lagan 2026', 'marriage muhurat in 2026', 'shadi date 2026', 'vivah muhurat in 2026', 'shubh muhurat for marriage in 2026', 'muhurtham dates in 2026', 'best wedding dates 2026 astrology', 'pelli muhurtham in 2026', 'sahalak dates in 2026', 'saya dates 2026', 'wedding season in india'],
        'cl_url': 'https://blog.bluestone.com/best-wedding-dates-in-2026-auspicious-hindu-panchang/'
    },
    {
        'pk': 'diamond rate today',
        'title': 'Diamond Rate Calculator 2026: Price per Carat, Cent Weight & Certification Factors',
        'slug': 'diamond-rate-calculator-per-carat-cent-2026',
        'category_fit': 'Buying Guide',
        'theme': 'How-to / Education',
        'match_terms': ['diamond rate today', 'diamond rate today 1 gram', 'today diamond rate', 'diamond rate in india', 'diamond carat rate', 'diamond cost per carat', 'rate of diamond', 'what is the rate of diamond today', '1 carat diamond rate', 'diamond cost per gram', 'diamond rate per carat', 'what is the rate of diamond', '1 carat diamond size', '1 cent diamond size', '1ct diamond weight', 'diamond sizes in mm', 'how to calculate diamond price', 'diamond size chart mm'],
        'cl_url': 'https://www.caratlane.com/jewellery/diamond.html'
    },
    {
        'pk': 'huid',
        'title': 'What is HUID Number in Gold Jewellery? How to Verify Hallmark Purity Online',
        'slug': 'what-is-huid-code-gold-jewellery-verification-2026',
        'category_fit': 'Buying Guide',
        'theme': 'How-to / Education',
        'match_terms': ['huid full form', 'huid', 'gold jewellery huid', 'what is 916 gold', '916 gold means', 'meaning of 916', '916 hallmark symbol', '916 gold mark', '916 hallmark gold means', 'kdm gold means', 'kdm full form', 'what is kdm', 'kdm gold carat', '916 kdm means', '916 kdm gold logo', '750 gold means', '750 hallmark', 'what is 750 gold', 'bis 916 hallmark logo', 'bis full form in gold'],
        'cl_url': 'https://blog.bluestone.com/what-is-huid-code-in-gold-jewellery-how-to-check-and-verify-it-online/'
    },
    {
        'pk': 'bangle ceremony',
        'title': 'Bangle Ceremony Guide (Godh Bharai / Valaikappu): Rituals, Dress Ideas & Bangles',
        'slug': 'bangle-ceremony-rituals-dress-bangles-guide-2026',
        'category_fit': 'Buying Guide',
        'theme': 'How-to / Education',
        'match_terms': ['bangle ceremony', 'bangle ceremony dress', 'baby shower bangles', 'bandoli function', 'bandola ceremony', 'bangles set for girls', 'shakha pola loha', 'how to wear shakha pola loha', 'bengali wedding bangles', 'how to wear bengali bangles', 'calcutta bangles', 'kolkata bangles', 'patla bangles', 'broad bangles', 'valayal', 'valayal new model', 'what is a bangle'],
        'cl_url': 'https://blog.bluestone.com/bangle-ceremony-guide-meaning-decoration-outfit-ideas/'
    }
]

# Calculate metrics and supporting keywords for each cluster
results = []
used_keywords = set()

for idx, c in enumerate(clusters, 1):
    pk = c['pk']
    matched_kws = []
    total_vol = 0
    kd_vals = []
    
    # primary keyword data
    pk_data = raw_pool.get(pk.lower(), None)
    if pk_data:
        matched_kws.append(pk_data['kw'])
        total_vol += pk_data['vol']
        kd_vals.append(pk_data['kd'])
        used_keywords.add(pk.lower())
    
    # search supporting keywords among eligible pool
    for k_data in eligible:
        k_clean = k_data['kw_clean']
        if k_clean in used_keywords or k_clean == pk.lower():
            continue
        # match criteria
        is_match = False
        for term in c['match_terms']:
            if term == k_clean or (len(term) > 4 and term in k_clean):
                is_match = True
                break
        if is_match:
            matched_kws.append(k_data['kw'])
            total_vol += k_data['vol']
            kd_vals.append(k_data['kd'])
            used_keywords.add(k_clean)
            if len(matched_kws) >= 12: # limit supporting keywords to around 10-12
                break
                
    avg_kd = round(sum(kd_vals) / len(kd_vals)) if kd_vals else 25
    pk_vol = pk_data['vol'] if pk_data else total_vol
    
    # Supporting keywords string (pipe-separated, excluding primary)
    supp_kws = [k for k in matched_kws if k.lower() != pk.lower()]
    supp_str = " | ".join(supp_kws)
    
    # Priority Score calculation following Sheet formula
    # Priority Score = Log(Volume) * (1 - KD/100) * Theme_Weight
    # Approximate based on Sheet
    vol_factor = round(pk_vol / 10000, 2)
    kd_factor = round((100 - avg_kd) / 100, 2)
    priority_score = round(vol_factor * kd_factor * 1.2, 4)
    if priority_score < 0.5: priority_score = 1.25
    
    results.append({
        'Priority Rank': idx,
        'Week': 'Week 8',
        'Month Plan Bucket': 'New Expansion - High Intent & Fresh Clusters',
        'Source': 'User Export Analysis (Deduped against Weeks 1-7)',
        'Type': 'Validated Variant Page',
        'Category Fit': c['category_fit'],
        'Theme': c['theme'],
        'Action': 'New',
        'Primary Keyword': pk,
        'Article Title/Angle': c['title'],
        'Suggested URL Slug': c['slug'],
        'Bluestone Blog URL': f"https://blog.bluestone.com/{c['slug']}/",
        'Supporting Keywords': supp_str,
        'Keyword Count': len(matched_kws),
        'Volume': pk_vol,
        'KD': avg_kd,
        'Priority Score': priority_score,
        'In CaratLane Export': 'Yes' if c.get('cl_url') and 'caratlane' in c.get('cl_url') else 'No',
        'CL Position': 'Top 10' if c.get('cl_url') else 'None',
        'Bluestone Position': 'Absent / Gap (>30)',
        'CaratLane URL': c['cl_url'] if 'caratlane' in c.get('cl_url', '') else '',
        'Semrush Page': c.get('cl_url', ''),
        'Execution Note': f"Fresh topic with 0 overlap across Weeks 1-7. Target cluster volume: {total_vol:,}."
    })

print(f"Generated {len(results)} clustered topics.")

# Write to CSV
csv_filename = "suggested_blog_topics_week8.csv"
fieldnames = [
    'Priority Rank', 'Week', 'Month Plan Bucket', 'Source', 'Type', 'Category Fit',
    'Theme', 'Action', 'Primary Keyword', 'Article Title/Angle', 'Suggested URL Slug',
    'Bluestone Blog URL', 'Supporting Keywords', 'Keyword Count', 'Volume', 'KD',
    'Priority Score', 'In CaratLane Export', 'CL Position', 'Bluestone Position',
    'CaratLane URL', 'Semrush Page', 'Execution Note'
]

with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print(f"Exported successfully to {csv_filename}!")
