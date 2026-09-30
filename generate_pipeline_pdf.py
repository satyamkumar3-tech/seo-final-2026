#!/usr/bin/env python3
"""
BlueStone SEO Generation Pipeline — Source of Truth PDF Generator
Run: python3 generate_pipeline_pdf.py
Output: docs/SEO_Pipeline_Source_of_Truth.pdf
"""

from pathlib import Path
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.platypus.flowables import BalancedColumns
from reportlab.lib.colors import HexColor

# ── Brand palette ──────────────────────────────────────────────────────────────
NAVY       = HexColor("#0D1B2A")   # deep header
INDIGO     = HexColor("#1A2F4E")   # section headers
GOLD       = HexColor("#C8922A")   # accent / highlight
GOLD_LIGHT = HexColor("#F5D87A")   # light accent
STEEL      = HexColor("#3D5A73")   # sub-section headers
SLATE      = HexColor("#4A5568")   # body text
CREAM      = HexColor("#FFFBF2")   # page background
PALE_GOLD  = HexColor("#FEF9EC")   # callout background
PALE_BLUE  = HexColor("#EEF4FB")   # table row alt
WHITE      = HexColor("#FFFFFF")
LIGHT_GREY = HexColor("#F7F8FA")
MID_GREY   = HexColor("#CBD5E0")
GREEN      = HexColor("#2D6A4F")
GREEN_BG   = HexColor("#D8F3DC")
RED_BG     = HexColor("#FFE5E5")
RED_FG     = HexColor("#9B1D1D")

ROOT = Path(__file__).resolve().parent
OUT  = ROOT / "docs" / "SEO_Pipeline_Source_of_Truth.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

# ── Styles ─────────────────────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()
    s = {}

    s["cover_title"] = ParagraphStyle(
        "cover_title",
        fontName="Helvetica-Bold",
        fontSize=28,
        textColor=WHITE,
        leading=36,
        spaceAfter=8,
        alignment=TA_CENTER,
    )
    s["cover_subtitle"] = ParagraphStyle(
        "cover_subtitle",
        fontName="Helvetica",
        fontSize=14,
        textColor=GOLD_LIGHT,
        leading=20,
        alignment=TA_CENTER,
    )
    s["cover_meta"] = ParagraphStyle(
        "cover_meta",
        fontName="Helvetica",
        fontSize=10,
        textColor=WHITE,
        leading=16,
        alignment=TA_CENTER,
    )
    s["h1"] = ParagraphStyle(
        "h1",
        fontName="Helvetica-Bold",
        fontSize=18,
        textColor=WHITE,
        leading=24,
        spaceBefore=4,
        spaceAfter=4,
        alignment=TA_LEFT,
    )
    s["h2"] = ParagraphStyle(
        "h2",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=INDIGO,
        leading=18,
        spaceBefore=14,
        spaceAfter=6,
    )
    s["h3"] = ParagraphStyle(
        "h3",
        fontName="Helvetica-Bold",
        fontSize=11,
        textColor=STEEL,
        leading=16,
        spaceBefore=10,
        spaceAfter=4,
    )
    s["body"] = ParagraphStyle(
        "body",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=SLATE,
        leading=15,
        spaceAfter=5,
        alignment=TA_JUSTIFY,
    )
    s["body_bold"] = ParagraphStyle(
        "body_bold",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=SLATE,
        leading=15,
        spaceAfter=4,
    )
    s["bullet"] = ParagraphStyle(
        "bullet",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=SLATE,
        leading=15,
        leftIndent=12,
        spaceAfter=3,
    )
    s["bullet_bold"] = ParagraphStyle(
        "bullet_bold",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=SLATE,
        leading=15,
        leftIndent=12,
        spaceAfter=3,
    )
    s["code"] = ParagraphStyle(
        "code",
        fontName="Courier",
        fontSize=8.5,
        textColor=INDIGO,
        leading=13,
        leftIndent=8,
        spaceAfter=2,
        backColor=PALE_BLUE,
    )
    s["caption"] = ParagraphStyle(
        "caption",
        fontName="Helvetica-Oblique",
        fontSize=8,
        textColor=STEEL,
        leading=12,
        alignment=TA_CENTER,
    )
    s["callout"] = ParagraphStyle(
        "callout",
        fontName="Helvetica",
        fontSize=9,
        textColor=INDIGO,
        leading=14,
        leftIndent=10,
        rightIndent=10,
        spaceAfter=4,
    )
    s["warning"] = ParagraphStyle(
        "warning",
        fontName="Helvetica-Bold",
        fontSize=9,
        textColor=RED_FG,
        leading=14,
        leftIndent=10,
        rightIndent=10,
        spaceAfter=4,
    )
    s["step_num"] = ParagraphStyle(
        "step_num",
        fontName="Helvetica-Bold",
        fontSize=9,
        textColor=WHITE,
        leading=12,
        alignment=TA_CENTER,
    )
    s["toc_item"] = ParagraphStyle(
        "toc_item",
        fontName="Helvetica",
        fontSize=10,
        textColor=INDIGO,
        leading=18,
        leftIndent=0,
    )
    s["toc_sub"] = ParagraphStyle(
        "toc_sub",
        fontName="Helvetica",
        fontSize=9,
        textColor=SLATE,
        leading=16,
        leftIndent=14,
    )
    return s

S = build_styles()

# ── Helper builders ────────────────────────────────────────────────────────────

def section_header(title: str) -> list:
    """Coloured full-width section header band."""
    tbl = Table([[Paragraph(title, S["h1"])]], colWidths=[170*mm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), INDIGO),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return [Spacer(1, 6*mm), tbl, Spacer(1, 4*mm)]


def sub_header(title: str) -> list:
    return [Paragraph(title, S["h2"])]


def sub_sub_header(title: str) -> list:
    return [Paragraph(title, S["h3"])]


def body(text: str) -> list:
    return [Paragraph(_esc(text), S["body"])]


def bullet(text: str, bold=False) -> list:
    st = S["bullet_bold"] if bold else S["bullet"]
    return [Paragraph(f"\u2022 &nbsp;{_esc(text)}", st)]


def code_line(text: str) -> list:
    return [Paragraph(_esc_code(text), S["code"])]


def hr() -> list:
    return [Spacer(1, 2*mm), HRFlowable(width="100%", thickness=0.5, color=MID_GREY), Spacer(1, 2*mm)]


def callout(text: str, warn=False) -> list:
    bg = RED_BG if warn else PALE_GOLD
    st = S["warning"] if warn else S["callout"]
    tbl = Table([[Paragraph(_esc_code(text), st)]], colWidths=[170*mm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
        ("BOX", (0,0), (-1,-1), 0.5, GOLD if not warn else RED_FG),
    ]))
    return [tbl, Spacer(1, 3*mm)]


def _esc(text: str) -> str:
    """Escape bare ampersands only — leaves <b>, <i>, <br/> etc. intact for ReportLab markup."""
    import re
    # Escape & only when not already part of an HTML entity (&amp; &lt; &gt; &nbsp; etc.)
    return re.sub(r'&(?!(?:[a-zA-Z]+|#\d+);)', '&amp;', text)


def _esc_code(text: str) -> str:
    """Full escape for literal/code text — escapes &, <, > so they render as plain characters."""
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;"))


def simple_table(headers: list, rows: list, col_widths=None) -> list:
    """Create a styled data table."""
    data = [headers] + rows
    if col_widths is None:
        col_widths = [170*mm / len(headers)] * len(headers)

    header_style = ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8.5,
                                  textColor=WHITE, leading=12)
    cell_style = ParagraphStyle("td", fontName="Helvetica", fontSize=8.5,
                                textColor=SLATE, leading=12)

    table_data = []
    for i, row in enumerate(data):
        if i == 0:
            table_data.append([Paragraph(_esc_code(str(c)), header_style) for c in row])
        else:
            table_data.append([Paragraph(_esc_code(str(c)), cell_style) for c in row])

    style = TableStyle([
        ("BACKGROUND", (0,0), (-1,0), INDIGO),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 7),
        ("RIGHTPADDING",  (0,0), (-1,-1), 7),
        ("GRID", (0,0), (-1,-1), 0.4, MID_GREY),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ])
    for i in range(1, len(table_data)):
        bg = PALE_BLUE if i % 2 == 0 else WHITE
        style.add("BACKGROUND", (0,i), (-1,i), bg)

    tbl = Table(table_data, colWidths=col_widths, repeatRows=1)
    tbl.setStyle(style)
    return [tbl, Spacer(1, 4*mm)]


def step_card(number: int, name: str, checkpoint: str, desc: str, details: list) -> list:
    """A styled pipeline step card."""
    num_cell = Paragraph(str(number), S["step_num"])
    name_para = Paragraph(f"<b>{name}</b>", ParagraphStyle("sc_name", fontName="Helvetica-Bold",
                           fontSize=10, textColor=INDIGO, leading=14))
    ckpt_para = Paragraph(f"<font color='#C8922A'>checkpoint:</font> <i>{checkpoint}</i>",
                          ParagraphStyle("ckpt", fontName="Helvetica", fontSize=8.5,
                                         textColor=STEEL, leading=12))
    desc_para = Paragraph(_esc(desc), S["body"])
    detail_paras = [Paragraph(f"• {_esc_code(d)}", S["bullet"]) for d in details]

    num_table = Table([[num_cell]], colWidths=[8*mm])
    num_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), GOLD),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROUNDEDCORNERS", [3]),
    ]))

    right_content = [name_para, ckpt_para, Spacer(1, 2), desc_para] + detail_paras
    right_table = Table([[c] for c in right_content], colWidths=[158*mm])
    right_table.setStyle(TableStyle([
        ("TOPPADDING",    (0,0), (-1,-1), 1),
        ("BOTTOMPADDING", (0,0), (-1,-1), 1),
        ("LEFTPADDING",   (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (-1,-1), 0),
    ]))

    outer = Table([[num_table, right_table]], colWidths=[12*mm, 158*mm])
    outer.setStyle(TableStyle([
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("BACKGROUND",    (0,0), (-1,-1), LIGHT_GREY),
        ("BOX",           (0,0), (-1,-1), 0.5, MID_GREY),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return [outer, Spacer(1, 3*mm)]


# ── Page template (header/footer) ─────────────────────────────────────────────

def on_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    # Footer
    canvas.setFillColor(INDIGO)
    canvas.rect(0, 0, w, 22, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(20, 7, "BlueStone SEO Generation Pipeline — Source of Truth")
    canvas.drawRightString(w - 20, 7, f"Page {doc.page}  |  v{datetime.now().strftime('%Y-%m-%d')}")
    # Top accent line
    canvas.setFillColor(GOLD)
    canvas.rect(0, h - 3, w, 3, fill=1, stroke=0)
    canvas.restoreState()


def on_first_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    # Full cover gradient background
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    # Gold accent band at top
    canvas.setFillColor(GOLD)
    canvas.rect(0, h - 6, w, 6, fill=1, stroke=0)
    # Side accent stripe
    canvas.setFillColor(GOLD)
    canvas.rect(0, 0, 6, h, fill=1, stroke=0)
    canvas.restoreState()


# ── Build document ─────────────────────────────────────────────────────────────

def build_pdf():
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=20*mm,
        rightMargin=20*mm,
        topMargin=25*mm,
        bottomMargin=20*mm,
    )

    story = []

    # ══════════════════════════════════════════════════════════════════════════
    # COVER PAGE
    # ══════════════════════════════════════════════════════════════════════════
    cover_spacer = Spacer(1, 60*mm)
    story.append(cover_spacer)

    cover_bg = Table([
        [Paragraph("🪙  BLUESTONE", S["cover_subtitle"])],
        [Paragraph("SEO Generation Pipeline", S["cover_title"])],
        [Paragraph("Source of Truth", S["cover_title"])],
        [Spacer(1, 6*mm)],
        [Paragraph("Complete workflow reference for the AI-powered blog article pipeline", S["cover_subtitle"])],
        [Spacer(1, 10*mm)],
        [Paragraph(f"Version: {datetime.now().strftime('%Y-%m-%d')}  |  Client: BlueStone (India)", S["cover_meta"])],
        [Paragraph("Website: blog.bluestone.com  |  Runner: AGY (Antigravity AI)", S["cover_meta"])],
    ], colWidths=[170*mm])
    cover_bg.setStyle(TableStyle([
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING",   (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (-1,-1), 0),
        ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ]))
    story.append(cover_bg)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # SECTION 0: WHAT IS THIS PIPELINE? (Beginner-friendly explanation)
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("What Is This Pipeline?  (Start Here)")

    story += body(
        "If you are reading this document for the first time, this section explains what the pipeline does, "
        "who is involved, and how the pieces fit together — in plain English, with no assumed knowledge."
    )

    # ── The Big Picture ──
    story += sub_header("The Big Picture")
    story += body(
        "BlueStone is an Indian fine jewellery brand (gold and diamonds). This pipeline automatically writes, "
        "publishes, and quality-checks SEO blog articles on <b>blog.bluestone.com</b>. Each article targets a "
        "specific keyword (e.g. 'gold ring designs for women 2026') and is designed to rank on Google India."
    )
    story += body(
        "The entire process — from picking the next keyword to publishing a fully-formatted WordPress post with "
        "images, a product carousel, SEO metadata, and schema markup — is handled by an <b>AI agent</b> (called AGY) "
        "that follows this pipeline's rules autonomously. A human only needs to start the command and review the output."
    )

    # ── Who Does What ──
    story += sub_header("Who Does What?")
    overview_rows = [
        ["You (the operator)", "Run the pipeline command in your terminal. Review the final report. Approve or fix any issues."],
        ["Python Orchestrator\n(article_pipeline.py)", "A script YOU run. It reads the keyword queue from an Excel file, builds a mega-prompt "
         "containing all context and rules, then launches the AI agent. After the agent finishes, it updates tracking files."],
        ["AI Agent (AGY)", "The brain. It receives the mega-prompt and autonomously executes all 16 steps: researching competitors, "
         "writing the article, building a product carousel, publishing to WordPress, generating AI images, running live QA, "
         "and writing the final report. It does NOT need human input during its run."],
        ["WordPress\n(blog.bluestone.com)", "The blog platform where articles are published. The agent talks to it via a REST API "
         "to create posts, upload images, set categories, and configure Yoast SEO."],
        ["Higgsfield AI", "An external AI image generation service. The agent uses its CLI to create lifestyle/editorial images "
         "(called 'Type 3' images) for the hero and article body."],
        ["Google / Semrush", "The agent scrapes Google India search results for the target keyword to understand what competitors "
         "are ranking for, then writes an article that covers the same topics AND fills gaps competitors missed."],
    ]
    story += simple_table(
        ["Actor", "What They Do"],
        overview_rows,
        col_widths=[42*mm, 128*mm],
    )

    # ── How One Article Gets Made (narrative) ──
    story += sub_header("How One Article Gets Made (The Journey)")
    story += body("Here is the lifecycle of a single article, from start to finish:")
    journey_steps = [
        "<b>1. You run the command:</b> <i>python3 -B scripts/article_pipeline.py produce --next ...</i>  "
        "This tells the orchestrator to pick the next unfinished keyword from the Excel queue.",
        "<b>2. The orchestrator reads the keyword queue</b> (SEO Strategy 2026.xlsx) and finds the next row "
        "marked 'Action = New'. It loads the keyword, volume, difficulty, suggested slug, and article engine.",
        "<b>3. It builds a massive prompt</b> containing: the target keyword data, all editorial rules, all SOPs, "
        "image generation instructions, WordPress config, and any pre-fetched SERP data for the keyword.",
        "<b>4. It launches the AI agent (AGY)</b> with that prompt. From this point, the agent works autonomously.",
        "<b>5. The agent reads all docs</b> loaded into its context and verifies Higgsfield AI is accessible.",
        "<b>6. Safety gates:</b> The agent checks if this keyword/slug already has a live post on BlueStone's blog. "
        "If a duplicate exists, it stops safely without creating anything.",
        "<b>7. SERP research:</b> The agent searches Google India for the keyword, reads the top 5 ranking pages, "
        "and writes a competitive brief identifying table-stakes topics, common FAQs, and content gaps.",
        "<b>8. Article planning:</b> The agent maps keywords to H2 headings, picks the right article engine "
        "(Gift Guide / Buying Guide / Design Listicle), and outlines the visual concept.",
        "<b>9. Drafting:</b> The agent writes the full article in WordPress Gutenberg HTML format — including "
        "introduction, body sections, product recommendations, a 6-product carousel, FAQ section, and JSON-LD schema.",
        "<b>10. Publishing:</b> The agent creates a new WordPress post via the REST API, uploads the hero image, "
        "sets Yoast SEO fields (focus keyword, meta title, meta description), and assigns categories.",
        "<b>11. Image generation:</b> The agent uses Higgsfield AI to generate 2-3 lifestyle images (hero + in-body), "
        "then uploads them to WordPress and patches the article to include them.",
        "<b>12. Live QA:</b> The agent fetches the live published URL and verifies everything: carousel works, "
        "images load, FAQs render, schema parses, word count is good, no broken links, no forbidden dashes.",
        "<b>13. Status update:</b> The agent updates the tracking CSV, product rotation file, and checkpoint.",
        "<b>14. Final report:</b> The agent prints a summary with the live URL, word count, products used, "
        "SERP insights, and any issues found.",
    ]
    for step_text in journey_steps:
        story += bullet(step_text)

    story.append(PageBreak())

    # ── VISUAL PIPELINE FLOWCHART ──
    story += sub_header("Visual Pipeline Flowchart")
    story += body(
        "The diagram below shows the end-to-end flow from your terminal command to a live published article. "
        "Read it top-to-bottom. Green boxes are inputs, blue boxes are agent actions, gold boxes are outputs."
    )

    # --- Build visual flowchart using styled tables ---

    FLOW_GREEN = HexColor("#D4EDDA")
    FLOW_GREEN_BORDER = HexColor("#28A745")
    FLOW_BLUE = HexColor("#D6EAF8")
    FLOW_BLUE_BORDER = HexColor("#2E86C1")
    FLOW_GOLD_BG = HexColor("#FFF3CD")
    FLOW_GOLD_BORDER = HexColor("#C8922A")
    FLOW_RED_BG = HexColor("#F8D7DA")
    FLOW_RED_BORDER = HexColor("#DC3545")
    FLOW_PURPLE_BG = HexColor("#E8DAEF")
    FLOW_PURPLE_BORDER = HexColor("#8E44AD")

    flow_cell = ParagraphStyle("flow_cell", fontName="Helvetica", fontSize=8.5,
                                textColor=SLATE, leading=12, alignment=TA_CENTER)
    flow_cell_bold = ParagraphStyle("flow_cell_bold", fontName="Helvetica-Bold", fontSize=9,
                                     textColor=INDIGO, leading=13, alignment=TA_CENTER)
    arrow_style = ParagraphStyle("arrow", fontName="Helvetica-Bold", fontSize=14,
                                  textColor=STEEL, leading=16, alignment=TA_CENTER)

    def flow_box(title, subtitle, bg, border, width=75*mm):
        """A single flowchart box."""
        content = []
        content.append(Paragraph(title, flow_cell_bold))
        if subtitle:
            content.append(Paragraph(subtitle, flow_cell))
        inner = Table([[c] for c in content], colWidths=[width - 4*mm])
        inner.setStyle(TableStyle([
            ("TOPPADDING", (0,0), (-1,-1), 2),
            ("BOTTOMPADDING", (0,0), (-1,-1), 2),
            ("LEFTPADDING", (0,0), (-1,-1), 3),
            ("RIGHTPADDING", (0,0), (-1,-1), 3),
        ]))
        outer = Table([[inner]], colWidths=[width])
        outer.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), bg),
            ("BOX", (0,0), (-1,-1), 1.5, border),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ("ROUNDEDCORNERS", [6]),
        ]))
        return outer

    def arrow_down():
        return Paragraph("▼", arrow_style)

    def flow_row_single(box):
        """Center a single box."""
        tbl = Table([[box]], colWidths=[170*mm])
        tbl.setStyle(TableStyle([
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("TOPPADDING", (0,0), (-1,-1), 0),
            ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ]))
        return tbl

    def flow_row_pair(box_left, box_right):
        """Two boxes side by side."""
        tbl = Table([[box_left, box_right]], colWidths=[85*mm, 85*mm])
        tbl.setStyle(TableStyle([
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("TOPPADDING", (0,0), (-1,-1), 0),
            ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ]))
        return tbl

    def flow_row_triple(box_left, box_mid, box_right):
        """Three boxes side by side."""
        tbl = Table([[box_left, box_mid, box_right]], colWidths=[57*mm, 56*mm, 57*mm])
        tbl.setStyle(TableStyle([
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("TOPPADDING", (0,0), (-1,-1), 0),
            ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ]))
        return tbl

    sp = Spacer(1, 2*mm)

    # Row 1: Inputs
    story.append(flow_row_triple(
        flow_box("📊 Excel Queue", "SEO Strategy 2026.xlsx", FLOW_GREEN, FLOW_GREEN_BORDER, 54*mm),
        flow_box("📦 Product CSV", "Seo Products - consolidated.csv", FLOW_GREEN, FLOW_GREEN_BORDER, 54*mm),
        flow_box("🖼️ Product Images", "ProductImages/seo images/", FLOW_GREEN, FLOW_GREEN_BORDER, 54*mm),
    ))
    story.append(sp)
    story.append(flow_row_single(arrow_down()))
    story.append(sp)

    # Row 2: Orchestrator
    story.append(flow_row_single(
        flow_box("⚙️ Python Orchestrator", "article_pipeline.py reads queue, builds mega-prompt, launches agent", FLOW_PURPLE_BG, FLOW_PURPLE_BORDER, 130*mm)
    ))
    story.append(sp)
    story.append(flow_row_single(arrow_down()))
    story.append(sp)

    # Row 3: Agent start
    story.append(flow_row_single(
        flow_box("🤖 AI Agent (AGY) Starts", "Receives mega-prompt with all rules, data, and context", FLOW_BLUE, FLOW_BLUE_BORDER, 130*mm)
    ))
    story.append(sp)
    story.append(flow_row_single(arrow_down()))
    story.append(sp)

    # Row 4: Safety gates
    story.append(flow_row_pair(
        flow_box("🛡️ Safety Gates", "Read docs, verify Higgsfield,\ncheck duplicate intent", FLOW_RED_BG, FLOW_RED_BORDER, 80*mm),
        flow_box("🔍 SERP Research", "Google top 5 scrape,\ncompetitive brief", FLOW_BLUE, FLOW_BLUE_BORDER, 80*mm),
    ))
    story.append(sp)
    story.append(flow_row_single(arrow_down()))
    story.append(sp)

    # Row 5: Content creation
    story.append(flow_row_pair(
        flow_box("📝 Keyword Map + Draft", "H2 spine, engine rules,\nfull Gutenberg HTML article", FLOW_BLUE, FLOW_BLUE_BORDER, 80*mm),
        flow_box("🎠 Product Carousel", "6 products from CSV,\n3D Coverflow HTML/CSS/JS", FLOW_BLUE, FLOW_BLUE_BORDER, 80*mm),
    ))
    story.append(sp)
    story.append(flow_row_single(arrow_down()))
    story.append(sp)

    # Row 6: Publishing
    story.append(flow_row_triple(
        flow_box("📤 WP Publish", "REST API → new post\n+ Yoast SEO", FLOW_BLUE, FLOW_BLUE_BORDER, 54*mm),
        flow_box("🎨 Higgsfield AI", "Type 3 images generated\n(hero + lifestyle)", FLOW_BLUE, FLOW_BLUE_BORDER, 54*mm),
        flow_box("🔧 Patch Media", "Upload images → WP,\nset og:image, links", FLOW_BLUE, FLOW_BLUE_BORDER, 54*mm),
    ))
    story.append(sp)
    story.append(flow_row_single(arrow_down()))
    story.append(sp)

    # Row 7: QA + Outputs
    story.append(flow_row_pair(
        flow_box("✅ Live QA", "DOM check, carousel, schema,\nword count, links, dashes", FLOW_BLUE, FLOW_BLUE_BORDER, 80*mm),
        flow_box("📋 Final Report", "Live URL, word count,\nSERP brief, products used", FLOW_BLUE, FLOW_BLUE_BORDER, 80*mm),
    ))
    story.append(sp)
    story.append(flow_row_single(arrow_down()))
    story.append(sp)

    # Row 8: Final outputs
    story.append(flow_row_triple(
        flow_box("🌐 Live Blog Post", "blog.bluestone.com/slug", FLOW_GOLD_BG, FLOW_GOLD_BORDER, 54*mm),
        flow_box("📊 Status CSV", "Week9_Blog_Queue_status.csv\nupdated", FLOW_GOLD_BG, FLOW_GOLD_BORDER, 54*mm),
        flow_box("💾 Checkpoint", "week9_rank{N}.json\nmarked complete", FLOW_GOLD_BG, FLOW_GOLD_BORDER, 54*mm),
    ))
    story.append(Spacer(1, 6*mm))

    # Legend
    legend_cell = ParagraphStyle("legend", fontName="Helvetica", fontSize=8, textColor=SLATE, leading=11)
    legend_data = [
        [Paragraph("🟢 <b>Green</b> = Inputs (files you provide)", legend_cell),
         Paragraph("🟣 <b>Purple</b> = Python orchestrator (runs on your machine)", legend_cell)],
        [Paragraph("🔵 <b>Blue</b> = AI agent actions (fully autonomous)", legend_cell),
         Paragraph("🟡 <b>Gold</b> = Final outputs (what you get)", legend_cell)],
        [Paragraph("🔴 <b>Red</b> = Safety gates (can halt the pipeline)", legend_cell),
         Paragraph("", legend_cell)],
    ]
    legend_tbl = Table(legend_data, colWidths=[85*mm, 85*mm])
    legend_tbl.setStyle(TableStyle([
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("BACKGROUND", (0,0), (-1,-1), LIGHT_GREY),
        ("BOX", (0,0), (-1,-1), 0.5, MID_GREY),
    ]))
    story.append(legend_tbl)

    story.append(PageBreak())

    # ── What Gets Updated After Each Article ──
    story += sub_header("What Gets Updated After Each Article?")
    story += body(
        "After the agent finishes and the article goes live, these files are updated to track progress:"
    )
    post_publish_rows = [
        ["output/Week9_Blog_Queue_status.csv", "Rank row upserted with: live URL, WP post ID, status, word count, notes",
         "Automatic (orchestrator)"],
        ["output/checkpoints/week9_rank{N}.json", "All 16 steps marked 'done' with timestamps. Status set to 'complete'",
         "Automatic (agent + orchestrator)"],
        ["output/product_rotation.json", "SKUs used in this article added/updated to prevent overuse in next articles",
         "Automatic (agent)"],
        ["SEO Strategy 2026.xlsx (Week 9 sheet)", "Target row updated with live URL, slug, and execution note",
         "Semi-automatic (when safe) or manual"],
        ["Manifest JSON (e.g. week9_69.json)", "Run entry finalized with timing, exit code, outcome, and log paths",
         "Automatic (orchestrator)"],
    ]
    story += simple_table(
        ["File", "What Gets Updated", "How"],
        post_publish_rows,
        col_widths=[55*mm, 75*mm, 40*mm],
    )

    # ── Quick Glossary ──
    story += sub_header("Quick Glossary")
    glossary_rows = [
        ["AGY", "Antigravity AI — the AI coding agent that executes the pipeline steps"],
        ["Orchestrator", "The Python script (article_pipeline.py) that you run. It prepares data and launches AGY"],
        ["Mega-prompt", "A very large text prompt built by the orchestrator containing all context, rules, and data the agent needs"],
        ["Checkpoint", "A JSON file tracking which of the 16 steps are done. Enables crash recovery — just rerun the command"],
        ["Type 1 image", "Raw studio jewellery photos from BlueStone. Used as reference only, never published directly"],
        ["Type 2 image", "Styled product shots on plinths/fabric. Used in the mid-article product carousel"],
        ["Type 3 image", "AI-generated lifestyle/editorial images via Higgsfield. Used as hero and in-body visuals"],
        ["Carousel", "A 3D Coverflow interactive HTML widget showing 6 products with Buy Now links mid-article"],
        ["SERP", "Search Engine Results Page — the Google results for a keyword. Agent scrapes top 5 to inform content"],
        ["Engine", "Article template type: Gift Guide, Buying Guide (education), or Design Listicle"],
        ["Rank", "The priority number of a keyword row in the Excel queue (Rank 1 = highest priority)"],
        ["PDP", "Product Detail Page — the BlueStone product page URL linked from carousel cards and images"],
        ["Yoast", "WordPress SEO plugin. The agent sets focus keyword, meta title, and meta description via its API"],
    ]
    story += simple_table(
        ["Term", "What It Means"],
        glossary_rows,
        col_widths=[30*mm, 140*mm],
    )

    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # TABLE OF CONTENTS
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("📋  Table of Contents")
    toc_items = [
        ("0.", "What Is This Pipeline? (Start Here)", [
            "The Big Picture",
            "Who Does What?",
            "How One Article Gets Made",
            "Visual Pipeline Flowchart",
            "What Gets Updated After Each Article",
            "Quick Glossary",
        ]),
        ("1.", "System Overview & Architecture", []),
        ("2.", "File & Directory Structure", []),
        ("3.", "The 16-Step Pipeline", [
            "Phase 1: Initialization & Safety Gates (Steps 1–4)",
            "Phase 2: SERP Research & Strategy (Steps 5–6)",
            "Phase 3: Content Architecture (Steps 7–8)",
            "Phase 4: Content Production (Steps 9–10)",
            "Phase 5: Publishing & Visual Production (Steps 11–13)",
            "Phase 6: Quality Assurance & Finalization (Steps 14–16)",
        ]),
        ("4.", "Content Engines (Gift Guide / Buying Guide / Design Listicle)", []),
        ("5.", "Image System (Types 1, 2, 3)", []),
        ("6.", "Carousel & Product Rules", []),
        ("7.", "WordPress Publishing & Yoast SEO", []),
        ("8.", "Checkpoint & Idempotency System", []),
        ("9.", "Mandatory Content Gates (Hard Rules)", []),
        ("10.", "CLI Reference & How to Run", []),
        ("11.", "Error Recovery Playbook", []),
        ("12.", "Monitoring & Status Tracking", []),
        ("13.", "Key Files Quick Reference", []),
    ]
    for num, title, subs in toc_items:
        story.append(Paragraph(f"<b>{num}</b> &nbsp; {title}", S["toc_item"]))
        for sub in subs:
            story.append(Paragraph(f"&nbsp;&nbsp;&nbsp; — &nbsp;{sub}", S["toc_sub"]))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 1. SYSTEM OVERVIEW
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("1.  System Overview & Architecture")
    story += body(
        "The BlueStone SEO Generation Pipeline is a fully-automated, AI-orchestrated system that produces "
        "complete, publication-ready SEO blog articles for blog.bluestone.com. Each article is generated "
        "end-to-end in a single AI agent session: from keyword research and competitor SERP analysis "
        "through drafting, product carousel assembly, WordPress publishing, Higgsfield AI image generation, "
        "live QA verification, and status tracking."
    )
    story += sub_header("Architecture at a Glance")
    story += simple_table(
        ["Layer", "Component", "Role"],
        [
            ["Input", "SEO Strategy 2026.xlsx (Week 9 sheet)", "Master keyword queue with rank, KD, volume, slug, theme"],
            ["Input", "Week9_Blog_Queue.csv", "CSV fallback if XLSX is unavailable"],
            ["Input", "Seo Products - consolidated.csv", "Product catalog with PDP URLs"],
            ["Input", "ProductImages/", "Raw (Type 1) & styled (Type 2) jewellery photos"],
            ["Orchestrator", "article_pipeline.py", "Python script that loads rows, builds prompts, launches AGY agent, finalizes checkpoints"],
            ["Orchestrator", "article_checkpoint.py", "Atomic JSON checkpoint manager (16 steps)"],
            ["Orchestrator", "serp_competitor_intel.py", "Pre-fetches Semrush SERP data per keyword"],
            ["AI Agent", "AGY (Antigravity)", "Executes all 16 steps: research → draft → publish → QA"],
            ["External", "WordPress REST API", "Publishes post, sets Yoast SEO fields, uploads media"],
            ["External", "Higgsfield CLI (nano_banana_pro)", "Generates Type 3 lifestyle/concept images"],
            ["External", "Google Search / Semrush", "SERP intelligence (top 5 competitor URLs)"],
            ["Output", "Published blog post", "Live article on blog.bluestone.com"],
            ["Output", "Week9_Blog_Queue_status.csv", "Terminal status tracker (rank, URL, WP post ID)"],
            ["Output", "Manifest JSON", "Full run audit trail with timing and outcomes"],
            ["Output", "Checkpoint JSON (per rank)", "Atomic step state for idempotent reruns"],
        ],
        col_widths=[28*mm, 58*mm, 84*mm],
    )

    story += sub_header("Design Principles")
    for p in [
        "<b>Single continuous agent session:</b> All 16 steps run in one AGY invocation. This preserves full context across steps (competitor research directly informs the draft; product selection informs image prompts).",
        "<b>Atomic idempotency:</b> Every step is checkpointed atomically. If the agent crashes, restarting the same command skips completed steps and resumes from the last pending one. WordPress post creation is strictly once.",
        "<b>SERP-first strategy:</b> The pipeline fetches and scrapes the top 5 Google India ranking pages BEFORE drafting. This ensures every article covers what Google currently rewards and differentiates on content gaps.",
        "<b>New posts only:</b> The pipeline only generates posts with Action=New. It never patches, optimizes, or deletes existing BlueStone blog posts.",
        "<b>Zero-price policy:</b> No prices appear in any article, carousel, or image. No competitor criticism. No fake statistics.",
    ]:
        story += bullet(p)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 2. FILE STRUCTURE
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("2.  File & Directory Structure")
    story += body("The workspace root is the folder <b>seo final 2026</b>. Every path below is relative to this root.")

    file_rows = [
        ["SEO Strategy 2026.xlsx", "Master strategy workbook — Week 9 sheet is the primary queue"],
        ["HANDOFF.md", "Project context, state handoff, quick-start instructions"],
        ["docs/PIPELINE_ARCHITECTURE.md", "Full architecture reference (this PDF is the definitive version)"],
        ["docs/SOP_ARTICLE_GENERATION.md", "Primary execution runbook (Step 0 → Step 10)"],
        ["docs/ARTICLE_WORKFLOW.md", "Canonical hard rules for article production"],
        ["docs/ARTICLE_ENGINES_PLAYBOOK.md", "Engine selection: Gift Guide / Buying Guide / Design Listicle"],
        ["docs/bluestone-blog-master-prompt-v5.md", "Master drafting prompt template"],
        ["docs/Blog-SEO-AEO-GEO-Checklist-v2.md", "Pre-publish QA checklist (mandatory)"],
        ["docs/HIGGSFIELD_IMAGE_GENERATION.md", "Higgsfield image SOP, prompts, Image SEO table"],
        ["cursor-rules/new-blogs-only.mdc", "Rule: only create new WP posts, never optimize old ones"],
        ["cursor-rules/carousel-seo-images.mdc", "Carousel image sourcing & conversion rules"],
        ["cursor-rules/type3-fair-skinned-indians.mdc", "Type 3 diversity / skin tone guideline"],
        ["cursor-rules/image-seo.mdc", "Image SEO: alts, filenames, WebP, media library titles"],
        ["cursor-rules/product-rotation-captions-education.mdc", "Product rotation and caption rules"],
        ["templates/eid_carousel_6_snippet.html", "Official 3D Coverflow carousel HTML/CSS/JS template"],
        ["scripts/article_pipeline.py", "Main orchestrator — current production pipeline"],
        ["scripts/article_checkpoint.py", "Atomic checkpoint manager (16 steps)"],
        ["scripts/week6_pipeline.py", "Shared utilities (common module)"],
        ["scripts/serp_competitor_intel.py", "Semrush SERP intelligence helper"],
        ["output/Week9_Blog_Queue.csv", "Week 9 queue CSV (fallback source)"],
        ["output/Week9_Blog_Queue_status.csv", "Terminal status tracker (rank → URL, WP post ID)"],
        ["output/product_rotation.json", "SKU rotation state (tracks which products used per rank)"],
        ["output/serp_cache/", "Cached Semrush SERP results per keyword"],
        ["output/checkpoints/", "Per-rank atomic checkpoint JSONs"],
        ["ProductImages/raw/", "Type 1: original studio jewellery photos (reference only)"],
        ["ProductImages/seo images/", "Type 2: styled product shots for carousel (960×535 WebP)"],
        ["Seo Products - consolidated.csv", "Product catalog with PDP URLs, SKU codes, categories"],
    ]
    story += simple_table(
        ["File / Directory", "Purpose"],
        file_rows,
        col_widths=[70*mm, 100*mm],
    )
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 3. 16-STEP PIPELINE
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("3.  The 16-Step Pipeline")
    story += body(
        "The pipeline orchestrator (article_pipeline.py) builds a single mega-prompt containing all context "
        "and rules, then launches the AGY AI agent. The agent executes all 16 steps synchronously within "
        "one session, marking each step in the checkpoint file as it goes."
    )

    # Pipeline flow visual table
    story += sub_header("Pipeline Flow Summary")
    phase_rows = [
        ["Phase 1", "Initialization & Safety", "Steps 1–4", "Read docs → Verify Higgsfield → Inspect row → Duplicate check"],
        ["Phase 2", "SERP Research", "Steps 5–6", "SERP intelligence (top 5 URLs) → Fact-check & compliance"],
        ["Phase 3", "Content Architecture", "Steps 7–8", "Keyword mapping & H2 spine → Article structure & visual concept"],
        ["Phase 4", "Content Production", "Steps 9–10", "Full article draft → Product curation & 3D carousel"],
        ["Phase 5", "Publishing & Visuals", "Steps 11–13", "WordPress publish → Higgsfield Type 3 generation → Media patching"],
        ["Phase 6", "QA & Finalization", "Steps 14–16", "Live QA verification → Status update → Final report"],
    ]
    story += simple_table(
        ["Phase", "Name", "Steps", "What Happens"],
        phase_rows,
        col_widths=[18*mm, 40*mm, 18*mm, 94*mm],
    )

    # ── PHASE 1 ──────────────────────────────────────────────────────────────
    story += sub_header("Phase 1: Initialization & Safety Gates")

    story += step_card(1, "Read Required Documents", "read_docs",
        "The agent reads all editorial guidelines, SOPs, and cursor rules into context before doing any task work.",
        [
            "HANDOFF.md — project state and active queue",
            "docs/SOP_ARTICLE_GENERATION.md — primary runbook",
            "docs/ARTICLE_WORKFLOW.md — canonical hard rules",
            "docs/ARTICLE_ENGINES_PLAYBOOK.md — engine selection",
            "docs/HIGGSFIELD_IMAGE_GENERATION.md — image SOP",
            "docs/Blog-SEO-AEO-GEO-Checklist-v2.md — QA checklist",
            "All 5 cursor-rules .mdc files",
        ])

    story += step_card(2, "Verify Higgsfield AI Status", "verify_higgsfield",
        "Before any image generation, the agent confirms Higgsfield credits, plan status, and CLI connectivity.",
        [
            "Runs: higgsfield account status --json (or MCP balance tool)",
            "Reports plan name and remaining credit balance",
            "Pipeline STOPS here if status fails — no proceeding to image generation",
            "On auth failure: user must re-login or reconnect the Higgsfield connector",
        ])

    story += step_card(3, "Inspect Target Row", "inspect_row",
        "Validates the target keyword row from the Week 9 workbook loaded by article_pipeline.py.",
        [
            "Data pre-loaded by orchestrator from SEO Strategy 2026.xlsx Week 9 sheet",
            "Validates: rank, primary keyword, slug, volume, KD, theme, engine, category fit",
            "Confirms Action = New (pipeline skips Done / Skip-Existing rows)",
            "Source: SEO Strategy 2026.xlsx Week 9 sheet OR Week9_Blog_Queue.csv fallback",
        ])

    story += step_card(4, "Duplicate & Intent Gate", "duplicate_check",
        "Checks if the target URL slug OR identical search intent already exists on blog.bluestone.com.",
        [
            "Queries WordPress REST API for the target slug",
            "Searches existing posts for overlapping search intent",
            "If duplicate found: pipeline HALTS safely — no new post, no media, checkpoint marked skipped_existing_intent",
            "Override available: --allow-existing-intent flag (requires --restart for audit trail)",
            "This is a hard safety gate — cannot be bypassed accidentally",
        ])

    # ── PHASE 2 ──────────────────────────────────────────────────────────────
    story += sub_header("Phase 2: SERP Research & Strategy")

    story += step_card(5, "SERP Intelligence", "serp_intelligence",
        "Searches Google India for the primary keyword, scrapes the top 5 organic URLs, and synthesizes a competitive brief. "
        "This step runs AFTER the duplicate check passes and BEFORE keyword mapping or drafting.",
        [
            "If Semrush data is cached in output/serp_cache/, pre-fetched URLs are used directly",
            "Otherwise: agent searches Google India and identifies top 5 organic results (excludes ads, featured snippets, PAA)",
            "For each of the 5 URLs: browses and reads full content, logs SERP_SCRAPED: position | url | domain | word_count | h2_count",
            "Extracts: page title, H2/H3 outline, key subtopics, FAQs answered, approximate word count",
            "Synthesizes SERP Competitive Brief containing:",
            "  a) Consensus topics (H2 themes in 3+ of top 5 pages — table stakes your article must cover)",
            "  b) Common FAQs (questions answered by 2+ competitors)",
            "  c) Content gaps (subtopics missing from all 5 pages — BlueStone differentiation opportunity)",
            "  d) Intent format (listicle / buying guide / long-form education / gift guide)",
            "  e) Average word count and depth benchmark",
            "Logs: SERP_BRIEF: <one-line summary of consensus topics and gaps>",
            "Uses brief directly to shape the H2 keyword map and article outline",
            "NEVER copies competitor wording — analysis only for topical coverage and differentiation",
        ])

    story += step_card(6, "Fact-Check & Compliance", "fact_check",
        "Verifies factual accuracy for buying and education topics. Browses authoritative sources when the keyword intent demands it.",
        [
            "Triggered for: GST rates, BIS hallmarking, gold purity, gem grading, legal/tax claims",
            "Sources: BIS website, official government notifications, authoritative jewellery industry bodies",
            "Hard rules enforced: no fake statistics, no prices, no competitor criticism, correct festival year",
            "For gift guides: fact-check is lighter (no regulatory compliance required)",
            "All cited facts logged in the Final Report",
        ])

    # ── PHASE 3 ──────────────────────────────────────────────────────────────
    story += sub_header("Phase 3: Content Architecture")

    story += step_card(7, "Keyword Mapping & H2 Spine", "keyword_map",
        "Maps the primary keyword plus all supporting keywords into a structured H2/H3 heading map and FAQ list.",
        [
            "Each H2 is labeled as: primary-backed / supporting-keyword-backed / competitor-structure-backed / serp-consensus-backed / intent-inferred",
            "Spine H2s (~70-80%): volume-backed primary and supporting keywords — placed higher in article",
            "Parity H2s (~20-30%): competitor structural buckets — placed lower, kept shorter",
            "Supporting keyword audit: irrelevant or polluted phrases explicitly REJECTED with reasons",
            "Engine selection applied: Gift Guide / Buying Guide / Design Listicle (from ARTICLE_ENGINES_PLAYBOOK.md)",
            "SERP brief consensus topics are mandatory inclusions in the H2 map",
        ])

    story += step_card(8, "Article Structure & Visual Concept", "structure_visuals",
        "Defines the complete article outline including visual layout, section ordering, and image placement plan.",
        [
            "Section ordering (MANDATORY): Intro → Body H2s → Carousel (mid-article) → More H2s → Related Guides → Conclusion → FAQs → JSON-LD",
            "Final Thoughts / Conclusion MUST appear BEFORE Frequently Asked Questions",
            "FAQs (5-7 visible Q&As) MUST be the final content section before JSON-LD schema",
            "Related Guides section (internal blog links) MUST appear between Conclusion and FAQs",
            "Visual plan: hero placement (featured image), in-body Type 3 image positions, carousel position",
        ])

    # ── PHASE 4 ──────────────────────────────────────────────────────────────
    story += sub_header("Phase 4: Content Production")

    story += step_card(9, "Full Article Draft", "draft",
        "Writes the complete Gutenberg HTML article following the Master Prompt v5 and all content rules.",
        [
            "Drafting guide: docs/bluestone-blog-master-prompt-v5.md",
            "Engine rules applied: Gift Guide / Buying Guide / Design Listicle structure and tone",
            "Gift guides: 5-6 named BlueStone recommendations with distinct gifting reasons, no prices",
            "Buying guides: explains calculations, buyer implications, regulatory context with citations",
            "Minimum internal links: 4+ internal BlueStone blog links + 1+ external authoritative link",
            "FAQs: 5-7 visible Q&A pairs in the HTML body (plus FAQPage JSON-LD schema)",
            "Author: Satyam (WP user ID 270271337) with byline 'By Satyam, BlueStone Editorial'",
            "ZERO em dashes, en dashes, or spaced hyphens anywhere in the article",
            "NO HTML tables — use structured bullet lists, cards, or styled PNG graphics instead",
            "NO duplicate sections — every H2 heading appears exactly once from intro to conclusion",
            "Strict Gutenberg block syntax with opening and closing comment tags on every block",
            "Every wp:paragraph block must explicitly enclose text in <p>...</p> tags",
        ])

    story += step_card(10, "Product Curation & 3D Coverflow Carousel", "product_media",
        "Selects 5-6 products from the catalog and builds the official 3D Coverflow carousel.",
        [
            "Product source: Seo Products - consolidated.csv (PDP links only, NO prices)",
            "SKU selection: 5-6 products matched to article intent, theme, and category",
            "Product rotation tracked in output/product_rotation.json (no SKU overuse)",
            "Carousel template: templates/eid_carousel_6_snippet.html (MUST use exactly this template)",
            "Carousel is a SINGLE unified wp:html block containing: <style> + <div class='bs-cf'> + <script>",
            "NEVER use unstyled wrappers (bs-cf-wrap, bs-cf-track) or split into multiple blocks",
            "Image source: Type 2 styled images from ProductImages/seo images/<Category>/<Name>.png",
            "Images converted to 960x535 WebP on stone plinths/draped fabric with warm lighting",
            "NEVER use plain white packshots for carousel cards",
            "Pre-flight check: EVERY carousel image URL verified to return HTTP 200 before insertion",
            "Every card includes: linked image (bs-cf-media) + product name + Buy now CTA (PDP URL)",
        ])

    story.append(PageBreak())

    # ── PHASE 5 ──────────────────────────────────────────────────────────────
    story += sub_header("Phase 5: Publishing & Visual Production")

    story += step_card(11, "WordPress Publish & Yoast SEO", "publish_wordpress",
        "Creates the new WordPress post via REST API with complete Gutenberg content, then configures Yoast SEO fields.",
        [
            "API auth: WP_USER + WP_APP_PASSWORD environment variables",
            "Base URL: https://blog.bluestone.com/wp-json/wp/v2/",
            "Post created with: Gutenberg HTML body, title, slug, categories, author ID 270271337",
            "WordPress creation is EXACTLY ONCE — reuses post if slug already exists from this run",
            "Never creates duplicate posts — stops safely if an untracked matching slug is found",
            "Yoast fields set: Focus Keyphrase, SEO Title (CTR-optimized), Meta Description (~155 chars)",
            "Featured image set as both featured_media and Yoast social image (og:image)",
            "Categories mapped by article intent — see WordPress Category Mapping table in Section 7",
        ])

    story += step_card(12, "Higgsfield AI Image Generation (Type 3)", "generate_type3",
        "Generates lifestyle and conceptual images using the Higgsfield CLI nano_banana_pro model.",
        [
            "Model: nano_banana_pro, aspect: 16:9, resolution: 2K, count: 1 per slot",
            "Slots: Hero image + 1-2 in-body lifestyle/conceptual images",
            "Style: analog grain, Kodak Portra color science, highlight halation, creamy bokeh, editorial color grading",
            "Max 2 concurrent generations — never exceed this limit",
            "On error: wait 45 seconds, then retry once. If still failing, step marked failed",
            "Extract image URL from result_url field in job JSON (NOT 'results' or 'output')",
            "Hero/lifestyle: image reference 1 = BP-PICS body_image, reference 2 = design angle",
            "If a SKU lacks body_image: select a different SKU — never generate people from packshots",
            "Product dimensions: product_height_mm and product_width_mm ONLY (not face/body measurements)",
            "FORBIDDEN in images: empty phones, screens, cards, boards, readable text, logos, product overlays",
            "Use physical props: flowers, diyas, ceramic cups, brass bowls, ribbons, wrapped gift boxes",
            "Jewellery material truth: BlueStone sells gold and diamond ONLY (no silver). Never describe gold/diamond SKUs as silver",
            "Output: WebP files with keyword-rich descriptive filenames",
        ])

    story += step_card(13, "Media Patching & Social Metadata", "patch_type3",
        "Uploads Type 3 images to WordPress, sets the featured hero, updates in-body image blocks, and configures social metadata.",
        [
            "Uploads all Type 3 WebP images to WordPress Media Library via REST API",
            "Sets hero as featured_media AND Yoast social image (og:image)",
            "Patches in-body image blocks to use the new uploaded media IDs",
            "Every product image in body is wrapped in a direct PDP hyperlink",
            "For in-body Type 3: sets linkDestination: custom with href to PDP URL",
            "Image SEO: unique keyword-led alt text, descriptive media library titles, sizeSlug: full only",
            "CLEAN image captions: standard <figcaption> without extra classes",
            "Verifies no duplicate hero image appears in the article body",
        ])

    # ── PHASE 6 ──────────────────────────────────────────────────────────────
    story += sub_header("Phase 6: Quality Assurance & Finalization")

    story += step_card(14, "Live QA Verification", "live_qa",
        "Fetches the live published URL and runs a comprehensive DOM and metadata verification pass.",
        [
            "Fetches the live published URL (cache-busted) and parses the HTML DOM",
            "CAROUSEL GATE: verifies .bs-cf, .bs-cf-stage, .bs-cf-card, .bs-cf-dots are present",
            "Verifies all 6 carousel card image URLs return HTTP 200 via HEAD requests",
            "If broken carousel detected: immediately replaces with eid_carousel_6_snippet.html template",
            "Single <h1> check (theme post title only — no injected content h1)",
            "Visible word count reported",
            "Heading counts: all planned H2s present in correct order",
            "All carousel Buy now links valid and pointing to correct PDPs",
            "5-7 FAQ questions and answers visible in the HTML body",
            "FAQPage schema parses cleanly; BlogPosting schema images array populated",
            "4+ internal links, 1+ external authoritative link",
            "og:image verified, canonical URL correct",
            "No forbidden dashes (em/en), no prices anywhere",
            "All images in WebP format with unique alt text and descriptive captions",
            "Author set to Satyam, categories correct",
            "Pass criteria: checkpoint detail result=passed",
        ])

    story += step_card(15, "Status Update", "update_status",
        "Updates all tracking files to record the completed rank.",
        [
            "Agent marks checkpoint update_status step done",
            "article_pipeline.py calls upsert_status_record() atomically with file-system locking",
            "output/Week9_Blog_Queue_status.csv updated (upsert by rank — never blind append)",
            "output/product_rotation.json updated (upsert by rank or SKU — never blind append)",
            "Status set to: published OR skipped_existing_intent",
            "Checkpoint status set to: complete with outcome and completed_at timestamp",
        ])

    story += step_card(16, "Final Report", "final_report",
        "Agent writes a comprehensive final report covering all key metrics and audit information for the run.",
        [
            "Live URL and WordPress post ID",
            "Article engine, author, categories",
            "Visible article word count",
            "Primary keyword and supplied volume/KD metrics",
            "Supporting keywords: which were used (with H2 placement) and which were rejected (with reasons)",
            "SERP intelligence: all URLs scraped (position, url, domain, word count, H2 count), consensus topics, content gaps, average competitor word count",
            "H2 keyword map with SERP-informed labels (which H2s added based on competitor analysis)",
            "Competitor URL analyzed and key findings",
            "Factual sources cited",
            "Carousel media IDs and Type 3 media IDs",
            "Product SKUs used and product rotation update",
            "Higgsfield: plan, starting balance, jobs run, retries, ending balance",
            "Duplicate and cannibalization check result",
            "Live og:image verification result",
        ])

    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 4. CONTENT ENGINES
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("4.  Content Engines (9 Reference Engines)")
    story += body(
        "The engine determines article structure, tone, visual approach, and product integration. "
        "Engine selection is <b>not a static lookup</b>. The pipeline uses a three-layer system: "
        "(1) the theme hint from the Excel queue, (2) SERP-driven validation during Step 5-7, and "
        "(3) dynamic engine composition for hybrid keywords. Reference: docs/ARTICLE_ENGINES_PLAYBOOK.md"
    )

    story += sub_header("Adaptive Engine Selection")
    story += body(
        "Instead of blindly mapping theme to engine, the agent <b>validates or overrides</b> the theme hint "
        "based on what Google is actually ranking. If the top 5 SERP results for 'pearl necklace set' are all "
        "design listicles but the theme says 'Education', the agent should write a design listicle."
    )
    story += simple_table(
        ["Layer", "What It Does", "When It Runs"],
        [
            ["1. Theme Hint", "Initial engine suggestion from the Excel queue 'theme' column", "At prompt build time (orchestrator)"],
            ["2. SERP Validation", "Agent scrapes top 5 Google results and checks if the dominant format matches the hint", "Step 5-7 (agent)"],
            ["3. Dynamic Composition", "For hybrid keywords, agent blends a primary engine (70-80%) with a secondary engine (20-30%)", "Step 7 (agent)"],
        ],
        col_widths=[35*mm, 85*mm, 50*mm],
    )

    story += sub_header("All 9 Reference Engines")
    story += simple_table(
        ["#", "Engine", "Triggered By", "Core Structure"],
        [
            ["1", "Gift Guide",
             "'gifts for sister', 'rakhi gifts', 'birthday gift for wife'",
             "Recipient segments, occasion guide, 5-6 named SKU recommendations with gifting reasons"],
            ["2", "Buying Guide / Education",
             "'how to check gold purity', '916 hallmark', 'GST on gold', 'bangle size'",
             "Technical explainer, step-by-step, regulatory context, buyer implications, fact-check gate"],
            ["3", "Design Listicle",
             "'gold ring designs', 'latest earrings', 'trendy necklace designs'",
             "Style categories, trend analysis, outfit pairing, 'best for' context mapping"],
            ["4", "Wishes and Quotes Compilation",
             "'happy diwali wishes', 'birthday wishes for crush', 'eid mubarak messages'",
             "120+ curated wish/quote lines by relationship and tone, soft jewellery gift tie-in section"],
            ["5", "Comparison / Versus",
             "'gold vs platinum', 'diamond vs moissanite', '22k vs 24k gold'",
             "Quick verdict, Option A/B deep-dives, head-to-head comparison (bullet lists, NOT tables)"],
            ["6", "Cultural Significance / Heritage",
             "'significance of mangalsutra', 'history of Polki', 'why do we wear toe rings'",
             "Historical origins, spiritual meaning, regional variations, modern interpretations"],
            ["7", "Care and Maintenance How-To",
             "'how to clean gold at home', 'how to store diamonds', 'jewellery polish tips'",
             "Materials list, numbered step-by-step, mistakes to avoid, when to seek professional help"],
            ["8", "Trend Report / Seasonal Forecast",
             "'jewellery trends 2027', 'summer jewellery trends', 'what is trending'",
             "Macro trends, individual trend deep-dives, what is fading, adoption advice"],
            ["9", "Regional / Bridal Collection",
             "'South Indian bridal jewellery', 'Bengali wedding jewellery', 'Maharashtrian'",
             "Essential pieces per tradition, styling guide, regional accuracy, modern adaptations"],
        ],
        col_widths=[6*mm, 36*mm, 58*mm, 70*mm],
    )

    story += sub_header("H2 Priority Weighting (All Engines)")
    story += simple_table(
        ["Priority", "Source", "Share", "Placement"],
        [
            ["Spine", "Volume-backed primary + supporting keywords from workbook row", "~70-80%", "Higher H2s + most FAQs"],
            ["Parity", "Competitor / SERP-consensus structural buckets", "~20-30%", "Lower H2s; keep shorter"],
            ["Never", "Soft parity buckets as separate URLs", "0%", "Stay on the single pillar URL"],
        ],
        col_widths=[20*mm, 90*mm, 20*mm, 40*mm],
    )

    story += callout(
        "ENGINE OVERRIDE RULE: If the SERP analysis in Step 5 contradicts the theme hint from the workbook, "
        "the agent MUST follow the SERP (Google is showing what users want). The override and reasoning "
        "must be logged in the Final Report."
    )
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 5. IMAGE SYSTEM
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("5.  Image System (Types 1, 2, 3)")
    story += simple_table(
        ["Type", "What It Is", "Source / Location", "Usage in Article"],
        [
            ["Type 1 — Raw",
             "Original studio jewellery photographs from BlueStone's photography sessions",
             "ProductImages/raw/<category>/",
             "Reference ONLY when writing Type 2/3 prompts. Never used directly in articles or carousel"],
            ["Type 2 — AI Product",
             "Styled product shots on plinths / draped fabric / warm-lit surfaces. 960×535 WebP",
             "ProductImages/seo images/<Category>/<Product Name>.png",
             "Mid-article 3D Coverflow carousel cards ONLY. Never as hero. Never plain white packshots"],
            ["Type 3 — AI Concept",
             "Lifestyle / atmosphere / editorial scenes generated by Higgsfield AI (nano_banana_pro, 16:9, 2K)",
             "Generated during Step 12 via Higgsfield CLI",
             "Hero (featured image) + 1-2 in-body editorial images. Never reuse hero in body"],
        ],
        col_widths=[22*mm, 50*mm, 48*mm, 50*mm],
    )

    story += sub_header("Type 3 Generation Style Lock")
    story += body("All Type 3 Higgsfield prompts MUST include this style language:")
    for style in [
        "Analog grain / subtle cinematic film grain",
        "Kodak Portra color science",
        "Highlight halation",
        "Creamy bokeh",
        "Filmic tonal response / highlight roll-off",
        "Editorial color grading",
        "Natural dynamic range / filmic contrast",
    ]:
        story += bullet(style)

    story += sub_header("Image SEO Requirements (Mandatory Every Publish)")
    story += simple_table(
        ["Requirement", "Rule"],
        [
            ["File format", "WebP only for all published images. Type 3 preferred WebP for LCP/hero"],
            ["Type 3 filename", "{occasion}-{hero|flatlay|lifestyle}-{year}.webp"],
            ["Type 2 filename", "{product-slug}-carousel.webp"],
            ["Alt text — hero", "Primary keyword + year + brief scene/product description"],
            ["Alt text — carousel", "{occasion/KW + year} gift idea: The {Product Name}"],
            ["Alt text — in-body Type 3", "Unique keyword-led description with product + scene + year"],
            ["Media library title", "Descriptive (NOT IMG_1234 or bare slug). E.g. 'Valeria Rose Pendant carousel — Eid 2027'"],
            ["Gutenberg sizeSlug", "Always 'full' — never 'large' with explicit width/height/loading attributes"],
            ["Captions", "Standard <figcaption>editorial caption</figcaption> — no extra classes"],
            ["Product image links", "Every product image in body wrapped in <a href='PDP URL'>"],
        ],
        col_widths=[50*mm, 120*mm],
    )

    story += callout(
        "⚠️  JEWELLERY MATERIAL TRUTH: BlueStone is a fine gold and diamond jeweller. It does NOT sell silver. "
        "Never recolor BlueStone SKUs in image prompts. Never describe authentic gold/diamond jewellery as silver.",
        warn=True
    )
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 6. CAROUSEL & PRODUCT RULES
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("6.  Carousel & Product Rules")

    story += sub_header("Official 3D Coverflow Carousel Specification")
    story += callout(
        "The mid-article carousel MUST strictly use the template from templates/eid_carousel_6_snippet.html. "
        "It MUST be a SINGLE unified wp:html block. No exceptions."
    )
    story += simple_table(
        ["Requirement", "Rule"],
        [
            ["Template source", "templates/eid_carousel_6_snippet.html — MUST use this template, not custom versions"],
            ["Block structure", "ONE wp:html block containing: <style> + <div class='bs-cf' id='bs-cf-{slug}'> + <script>"],
            ["CSS classes REQUIRED", ".bs-cf-stage, .bs-cf-card, .bs-cf-prev, .bs-cf-next, .bs-cf-dots, .bs-cf-cta, is-pos-0 through is-pos--1"],
            ["CSS values REQUIRED", ".bs-cf-stage { height: 360px }, margin: 1.75rem auto 1.25rem, .bs-cf-card { width: min(420px, 78vw) }"],
            ["NEVER use", "bs-cf-wrap, bs-cf-track, or any unstyled custom wrapper classes"],
            ["NEVER do", "Omit <style> or <script>, split into multiple blocks, wrap lines in single quotes"],
            ["Product count", "Exactly 6 products per carousel"],
            ["Image verification", "ALL 6 image URLs verified HTTP 200 before insertion — MANDATORY"],
            ["Card structure", "Each card: <a class='bs-cf-media' href='{PDP}'><img /></a> + name + <a class='bs-cf-cta' href='{PDP}'>Buy now</a>"],
            ["After carousel", "Follow immediately with ONLY a single 'Curated Design Highlights' paragraph. NEVER a repetitive product bullet list"],
            ["Carousel position", "Mid-article — NEVER the last block. Content continues after carousel"],
        ],
        col_widths=[45*mm, 125*mm],
    )

    story += sub_header("Product Selection Rules")
    for rule in [
        "Source: Seo Products - consolidated.csv — PDP links, categories, SKU codes",
        "Count: 5-6 products per article",
        "Match products to article intent, theme, and keyword category",
        "Track rotation in output/product_rotation.json — avoid reusing same SKUs too frequently",
        "NO prices anywhere — not in body text, carousel cards, captions, or FAQs",
        "Gift guides: named product recommendations in BODY (not just carousel) with gifting reasons",
        "Buying guides: product placement secondary and useful (educational context, not forced gifting)",
        "Design listicles: products as design references with 'best for' style/context mapping",
    ]:
        story += bullet(rule)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 7. WORDPRESS PUBLISHING
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("7.  WordPress Publishing & Yoast SEO")

    story += sub_header("API Configuration")
    story += simple_table(
        ["Parameter", "Value"],
        [
            ["Base URL", "https://blog.bluestone.com/wp-json/wp/v2/"],
            ["Authentication", "WP_USER + WP_APP_PASSWORD (environment variables — never commit to git)"],
            ["WP Username", "blogbluestone"],
            ["Author (Week 9)", "Satyam — WP user ID 270271337"],
            ["Author byline", "By Satyam, BlueStone Editorial"],
            ["BlogPosting schema author", "Satyam"],
            ["Theme", "Creatio — single template (wp_id 29900)"],
            ["Post title rendering", "Theme renders WP post title as <h1> above featured image"],
            ["H1 rule", "ONE h1 only — the theme post title. NEVER inject a duplicate h1 in content"],
        ],
        col_widths=[45*mm, 125*mm],
    )

    story += sub_header("WordPress Category Mapping")
    story += simple_table(
        ["Article Intent / Engine", "WordPress Category IDs"],
        [
            ["General gift guide", "Gift (554493424)"],
            ["Seasonal / festival gift guide", "Gift (554493424) + Festive Wishes (554493477)"],
            ["Wedding / couple jewellery", "Gift (554493424) + Wedding Jewellery (554493443)"],
            ["Gold buying / purity guide", "Gold (554493348) + Jewellery Problem and Solution (554493465)"],
            ["Design listicle / style discovery", "Jewellery Trends (554493317) or Jewellery and Lifestyle (554493425)"],
        ],
        col_widths=[80*mm, 90*mm],
    )

    story += sub_header("Yoast SEO Fields")
    story += simple_table(
        ["Field", "Value / Rule"],
        [
            ["_yoast_wpseo_focuskw", "Primary keyword from workbook row"],
            ["_yoast_wpseo_title", "CTR-optimized title with primary keyword — max 60 chars preferred"],
            ["_yoast_wpseo_metadesc", "Compelling 150-160 character description accurately summarizing article"],
            ["Featured image (og:image)", "Hero Type 3 image — set as both featured_media and Yoast social image"],
            ["Social image fallback", "If Yoast social-image field not exposed via REST: use authenticated editor UI for that field only"],
        ],
        col_widths=[60*mm, 110*mm],
    )

    story += sub_header("Strict Gutenberg Block Syntax Rules")
    story += callout(
        "Every WordPress block comment MUST be strictly formatted with opening and closing hyphens: "
        "<!-- wp:paragraph --> ... <!-- /wp:paragraph -->. "
        "NEVER emit: <!-- /wp:paragraph> (missing --) or <!-- /wp:paragraph) (parenthesis typo). "
        "Every wp:paragraph block MUST explicitly enclose text in <p>...</p> tags."
    )
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 8. CHECKPOINT SYSTEM
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("8.  Checkpoint & Idempotency System")
    story += body(
        "Each rank has an atomic JSON checkpoint at output/checkpoints/week9_rank{N}.json. "
        "Steps are marked atomically with file-system locking. If the agent crashes, restarting the same command "
        "skips completed steps and resumes from the last pending one."
    )

    story += sub_header("Step Names (Exact Order)")
    story += simple_table(
        ["#", "Step Name", "Checkpoint Key", "Phase"],
        [
            ["1", "Read Docs", "read_docs", "Phase 1"],
            ["2", "Verify Higgsfield", "verify_higgsfield", "Phase 1"],
            ["3", "Inspect Row", "inspect_row", "Phase 1"],
            ["4", "Duplicate Check", "duplicate_check", "Phase 1"],
            ["5", "SERP Intelligence", "serp_intelligence", "Phase 2"],
            ["6", "Fact Check", "fact_check", "Phase 2"],
            ["7", "Keyword Map", "keyword_map", "Phase 3"],
            ["8", "Structure & Visuals", "structure_visuals", "Phase 3"],
            ["9", "Draft Article", "draft", "Phase 4"],
            ["10", "Product & Carousel", "product_media", "Phase 4"],
            ["11", "Publish WordPress", "publish_wordpress", "Phase 5"],
            ["12", "Generate Type 3", "generate_type3", "Phase 5"],
            ["13", "Patch Media", "patch_type3", "Phase 5"],
            ["14", "Live QA", "live_qa", "Phase 6"],
            ["15", "Update Status", "update_status", "Phase 6"],
            ["16", "Final Report", "final_report", "Phase 6"],
        ],
        col_widths=[8*mm, 45*mm, 45*mm, 72*mm],
    )

    story += sub_header("Step Status Values")
    story += simple_table(
        ["Status", "Meaning"],
        [
            ["pending", "Step has not started yet"],
            ["running", "Step is currently in progress"],
            ["done", "Step completed successfully — artifact or external ID verified"],
            ["failed", "Step failed due to agent or script error"],
            ["skipped", "Step intentionally not applicable for this run"],
        ],
        col_widths=[25*mm, 145*mm],
    )

    story += sub_header("Checkpoint Commands")
    for cmd in [
        "# View checkpoint state",
        "python3 -B scripts/article_checkpoint.py show --path output/checkpoints/week9_rank{N}.json",
        "",
        "# Mark a step done",
        "python3 -B scripts/article_checkpoint.py mark --path <path> --step <step_name> --status done --detail key=value",
        "",
        "# Initialize checkpoint",
        "python3 -B scripts/article_checkpoint.py init --path <path> --rank <N> --slug <slug> --primary \"<keyword>\"",
    ]:
        story += code_line(cmd)

    story += sub_header("Pipeline Outcomes")
    story += simple_table(
        ["Outcome", "Checkpoint Status", "Meaning"],
        [
            ["published", "complete", "Post published, verified, and live QA passed"],
            ["skipped_existing_intent", "complete", "Duplicate intent detected — no post or media created"],
            ["incomplete", "incomplete", "Agent exited successfully but live QA did not pass"],
            ["failed", "failed", "Agent or script error caused step failure"],
        ],
        col_widths=[45*mm, 40*mm, 85*mm],
    )
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 9. MANDATORY CONTENT GATES
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("9.  Mandatory Content Gates (Hard Rules)")
    story += body(
        "These are non-negotiable rules enforced in the pipeline prompt. Violation causes QA failure "
        "or produces broken/non-compliant articles. Review these when making any workflow changes."
    )

    story += sub_header("Article Content Rules")
    for rule in [
        "Action must be New — skip Done and Skip-Existing rows without generating content",
        "Duplicate intent check MUST run before any research or drafting",
        "SERP intelligence (serp_intelligence step) runs AFTER duplicate check, BEFORE keyword mapping",
        "All 5 SERP URLs must be scraped and read in full — no skipping",
        "Competitor URL analyzed when present — never invent a competitor URL if blank",
        "Supporting keywords audited: irrelevant phrases explicitly REJECTED with reasons listed",
        "Every article uses the appropriate engine from ARTICLE_ENGINES_PLAYBOOK.md",
        "Gift guides: 5-6 named BlueStone product recommendations in the BODY (not just carousel)",
        "Buying guides: explain calculations, buyer implications, regulatory context clearly",
        "Factual topics (GST, hallmarking, purity, regulations): browse current authoritative sources, cite them",
        "NO prices anywhere in the article",
        "NO fake statistics",
        "NO unsupported legal or tax claims",
        "NO competitor criticism",
        "NO em dashes (—), en dashes (–), or spaced hyphens ( word - word )",
        "Author: Satyam (ID 270271337), byline: 'By Satyam, BlueStone Editorial'",
        "NO HTML tables — use structured bullet lists, cards, or styled PNG graphics instead",
        "Jewellery material: BlueStone sells gold and diamond ONLY — no silver",
        "EXACTLY ONCE content: no duplicate sections, no repeated H2s, no concatenated article halves",
        "Article depth preserved even when image generation runs in parallel",
        "120+ distinct list lines for quotes/captions/listicle articles (unless row specifies different format)",
    ]:
        story += bullet(rule)

    story += sub_header("Section Ordering Rules (MANDATORY)")
    story += callout(
        "1. Intro → 2. Body H2s → 3. Carousel (mid-article) → 4. More Body H2s → "
        "5. Related Guides section (4-5 internal links) → 6. Final Thoughts / Conclusion → "
        "7. Frequently Asked Questions (5-7 visible Q&As) → 8. JSON-LD schema\n\n"
        "Final Thoughts MUST appear BEFORE FAQs. FAQs MUST be the last content section before JSON-LD. "
        "Related Guides section MUST appear between Conclusion and FAQs."
    )

    story += sub_header("Synchronous Execution Gate")
    story += callout(
        "CRITICAL: The AI agent MUST execute ALL commands synchronously. "
        "NO background tasks, NO async delays. Every python script, curl call, Higgsfield generation, "
        "and WordPress upload runs in the foreground and blocks until full completion. "
        "The agent NEVER ends its turn while a task is running.",
        warn=True
    )
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 10. CLI REFERENCE
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("10.  CLI Reference & How to Run")

    story += sub_header("Standard Production Command")
    for line in [
        "python3 -B scripts/article_pipeline.py produce \\",
        "  --ranks 69 \\",
        "  --manifest output/week9_69.json \\",
        "  --timers \\",
        "  --approve-for-me",
    ]:
        story += code_line(line)

    story += sub_header("Auto-pick Next Unfinished Rank")
    for line in [
        "python3 -B scripts/article_pipeline.py produce \\",
        "  --next \\",
        "  --manifest output/week9_next.json \\",
        "  --timers --approve-for-me",
    ]:
        story += code_line(line)

    story += sub_header("All CLI Options")
    story += simple_table(
        ["Flag", "Purpose", "Notes"],
        [
            ["--ranks N or N-M", "Specific rank(s) to generate", "e.g. --ranks 69 or --ranks 69-73 or --ranks 69,72,75"],
            ["--next [COUNT]", "Auto-pick next N unfinished Action=New ranks", "Default COUNT=1 if omitted"],
            ["--manifest <path>", "Run manifest JSON path (audit trail)", "REQUIRED — used for status command too"],
            ["--timers", "Enable step-by-step timing display in terminal", "Recommended for monitoring"],
            ["--approve-for-me", "Auto-approve agent workspace writes", "Needed for non-interactive runs"],
            ["--dry-run", "Build prompt only — do not launch agent", "For prompt inspection and testing"],
            ["--verbose", "Stream full agent output to terminal", "Full log always saved regardless"],
            ["--restart", "Archive old checkpoint and restart selected ranks from step 1", "Requires explicit --ranks"],
            ["--allow-existing-intent", "Override duplicate-intent gate after documenting the conflict", "Requires --restart"],
            ["--force", "Rerun already-completed ranks", "Use for intentional controlled reruns only"],
            ["--runner agy", "Use AGY agent (default) or codex", "Default: agy"],
            ["--model <name>", "Specify AI model for AGY runner", "Optional"],
            ["--continue-on-error", "Continue to next rank even if current rank fails", "For batch runs"],
            ["--heartbeat-seconds N", "Seconds between progress updates (min 10)", "Default: 30"],
        ],
        col_widths=[45*mm, 65*mm, 60*mm],
    )

    story += sub_header("Status Command")
    for line in [
        "# Check run status",
        "python3 -B scripts/article_pipeline.py status --manifest output/week9_69.json",
        "",
        "# JSON output",
        "python3 -B scripts/article_pipeline.py status --manifest output/week9_69.json --json",
    ]:
        story += code_line(line)

    story += sub_header("Expected Terminal Output (with --timers)")
    for line in [
        "================================================================================",
        "Week 9 Rank 69: light earrings (Runner: agy)",
        "Engine: buying_guide",
        "================================================================================",
        "",
        "step 1: read_docs             | completed in 1m 12s",
        "step 2: verify_higgsfield     | completed in 21s",
        "step 3: inspect_row           | completed in 23s",
        "step 4: duplicate_check       | completed in 1m 0s",
        "step 5: serp_intelligence     | completed in 2m 30s",
        "step 6: fact_check            | completed in 13s",
        "step 7: keyword_map           | completed in 45s",
        "step 8: structure_visuals     | completed in 28s",
        "step 9: draft                 | completed in 8m 15s",
        "step 10: product_media        | completed in 3m 10s",
        "step 11: publish_wordpress    | completed in 2m 5s",
        "step 12: generate_type3       | completed in 5m 30s",
        "step 13: patch_type3          | completed in 1m 45s",
        "step 14: live_qa              | completed in 2m 0s",
        "step 15: update_status        | completed in 15s",
        "step 16: final_report         | completed in 24s",
    ]:
        story += code_line(line)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 11. ERROR RECOVERY
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("11.  Error Recovery Playbook")
    story += simple_table(
        ["Scenario", "Recovery Action", "Command / Notes"],
        [
            ["Agent crashes mid-step",
             "Rerun the same command — checkpoint skips all completed steps and resumes from last pending",
             "python3 -B scripts/article_pipeline.py produce --ranks N --manifest <same manifest> --timers --approve-for-me"],
            ["Want clean restart from step 1",
             "Archive old checkpoint and restart",
             "--restart flag (requires explicit --ranks). Old checkpoint archived to output/checkpoints/archive/"],
            ["Duplicate slug found in WordPress",
             "Agent stops safely. Reconcile manually: decide if existing post is the same intent or if new slug is needed",
             "May use --allow-existing-intent with --restart if user approves a differentiated rerun"],
            ["Higgsfield generation fails",
             "Agent waits 45 seconds and retries once automatically. If still failing, step is marked failed",
             "Rerun with same command — generate_type3 step will be retried from checkpoint"],
            ["Duplicate search intent detected",
             "Pipeline halts with skipped_existing_intent outcome. No post or media created",
             "Review the conflicting URL. If differentiation is possible, use --allow-existing-intent --restart"],
            ["Carousel is broken on live site",
             "Live QA step detects this and immediately replaces with eid_carousel_6_snippet.html template",
             "If QA detects unstyled bs-cf-wrap or broken images, carousel is patched before QA passes"],
            ["Incomplete checkpoint from previous run",
             "Rerun the command — checkpoint automatically resumes from last pending step",
             "Use --restart only if you want to wipe and start fresh from step 1"],
            ["Status CSV corrupted or headerless",
             "Pipeline auto-detects legacy format and migrates rows to new schema",
             "upsert_status_record() handles both legacy 8-column and current header formats"],
            ["Another pipeline instance is running",
             "File lock prevents concurrent runs. Wait for the running pipeline to finish",
             "Lock file: output/.locks/article_pipeline.lock"],
        ],
        col_widths=[42*mm, 60*mm, 68*mm],
    )
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 12. MONITORING & STATUS
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("12.  Monitoring & Status Tracking")

    story += sub_header("Status CSV — output/Week9_Blog_Queue_status.csv")
    story += simple_table(
        ["Column", "Description"],
        [
            ["rank", "Integer rank from Week 9 workbook"],
            ["primary", "Primary keyword"],
            ["slug", "Published URL slug"],
            ["blog_url", "Full published URL on blog.bluestone.com"],
            ["wp_post_id", "WordPress post ID"],
            ["status", "published | skipped_existing_intent | failed"],
            ["carousel_media", "WordPress media IDs for carousel images (JSON array)"],
            ["type3_media", "WordPress media IDs for Type 3 images (JSON array)"],
            ["lines", "Number of section lines in the draft"],
            ["visible_words", "Verified visible word count from live QA"],
            ["notes", "Run notes: engine, checkpointed components, QA result"],
        ],
        col_widths=[35*mm, 135*mm],
    )

    story += sub_header("Manifest JSON — output/week9_{ranks}.json")
    for item in [
        "Created per run — contains all run metadata, timing, exit codes, outcomes, per-rank details",
        "Fields: pipeline, created_at, workspace, week9_workbook, week9_csv, requested_ranks, runs[]",
        "Each run entry: rank, primary, slug, engine, status, started_at, finished_at, duration_seconds, exit_code, outcome, prompt_path, log_path, final_path, checkpoint_path",
    ]:
        story += bullet(item)

    story += sub_header("Checkpoint JSON — output/checkpoints/week9_rank{N}.json")
    for item in [
        "Created per rank — tracks per-step status, timestamps, and key artifacts",
        "Fields: pipeline, rank, slug, primary, created_at, status, outcome, steps{}",
        "Each step entry: status (pending/running/done/failed/skipped), started_at, finished_at, detail{}",
        "detail{} contains step-specific data: wp_post_id, live_url, media_ids, word_count, result, etc.",
        "Archive on restart: moved to output/checkpoints/archive/week9_rank{N}_{timestamp}.json",
    ]:
        story += bullet(item)

    story += sub_header("SERP Cache — output/serp_cache/")
    for item in [
        "Stores pre-fetched Semrush SERP data per keyword",
        "If cached data exists for the primary keyword, it is injected directly into the prompt",
        "If no cache: agent searches Google India live during Step 5",
        "Cache managed by scripts/serp_competitor_intel.py",
    ]:
        story += bullet(item)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # 13. KEY FILES QUICK REFERENCE
    # ══════════════════════════════════════════════════════════════════════════
    story += section_header("13.  Key Files Quick Reference")
    story += simple_table(
        ["File", "Purpose", "When to Read"],
        [
            ["HANDOFF.md", "Project context, current state, active queue", "Always first"],
            ["docs/SOP_ARTICLE_GENERATION.md", "Primary execution runbook Step 0 → Step 10", "Before any new run"],
            ["docs/ARTICLE_WORKFLOW.md", "Canonical hard rules: H1, images, carousel, dash rules", "When reviewing rules"],
            ["docs/ARTICLE_ENGINES_PLAYBOOK.md", "Engine selection (Gift/Buying/Design) and H2 strategy", "During keyword mapping"],
            ["docs/bluestone-blog-master-prompt-v5.md", "Master article drafting prompt template", "During draft step"],
            ["docs/Blog-SEO-AEO-GEO-Checklist-v2.md", "Pre-publish QA checklist (mandatory every publish)", "Before live QA"],
            ["docs/HIGGSFIELD_IMAGE_GENERATION.md", "Higgsfield SOP, prompt templates, Image SEO table", "During image generation"],
            ["docs/competitor-blog-analysis-SKILL.md", "Competitor analysis template and structure", "During fact-check"],
            ["cursor-rules/new-blogs-only.mdc", "Rule: new posts only, never optimize old posts", "If ever tempted to edit existing posts"],
            ["cursor-rules/carousel-seo-images.mdc", "Carousel image sourcing, conversion, pre-flight", "During carousel building"],
            ["cursor-rules/type3-fair-skinned-indians.mdc", "Type 3 diversity/representation guidelines", "During image prompt writing"],
            ["cursor-rules/image-seo.mdc", "Image SEO: alts, filenames, WebP, sizeSlug rules", "Before media upload"],
            ["cursor-rules/product-rotation-captions-education.mdc", "Product rotation and educational caption rules", "During product selection"],
            ["templates/eid_carousel_6_snippet.html", "Official 3D Coverflow carousel template (6 cards)", "During carousel assembly"],
            ["Seo Products - consolidated.csv", "Product catalog: name, SKU, category, PDP URL", "During product selection"],
            ["output/Week9_Blog_Queue_status.csv", "Terminal status tracker — which ranks are done", "Before selecting next rank"],
            ["output/product_rotation.json", "SKU rotation state — which products used per rank", "During product selection"],
            ["SEO_Pipeline_Source_of_Truth.pdf (this file)", "Complete pipeline documentation — source of truth", "Any time workflow questions arise"],
        ],
        col_widths=[55*mm, 65*mm, 50*mm],
    )

    story += [Spacer(1, 8*mm)]
    story += hr()
    footer_txt = (
        f"<b>BlueStone SEO Generation Pipeline — Source of Truth</b><br/>"
        f"Generated: {datetime.now().strftime('%B %d, %Y at %H:%M IST')}  |  Pipeline Version: Week 9 with SERP Intelligence<br/>"
        f"This document is the authoritative reference. Update this PDF whenever the workflow changes."
    )
    story.append(Paragraph(footer_txt, S["caption"]))

    doc.build(story, onFirstPage=on_first_page, onLaterPages=on_page)
    print(f"✅  PDF generated: {OUT}")
    return OUT


if __name__ == "__main__":
    build_pdf()
