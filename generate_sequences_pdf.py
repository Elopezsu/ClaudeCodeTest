from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.enums import TA_LEFT

OUTPUT = "/Users/eunicelopez/Desktop/ClaudeCodeTest/ValuSignal-Promo-Email-Sequences-Jun2026.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    rightMargin=0.9*inch,
    leftMargin=0.9*inch,
    topMargin=0.9*inch,
    bottomMargin=0.9*inch
)

styles = getSampleStyleSheet()

DARK    = colors.HexColor("#1a1a2e")
ACCENT  = colors.HexColor("#2563eb")
DARK2   = colors.HexColor("#0f172a")
MID     = colors.HexColor("#64748b")
WHITE   = colors.white

def s(name, **kw):
    base = dict(fontName="Helvetica", fontSize=9.5, textColor=DARK,
                leading=14, spaceAfter=6)
    base.update(kw)
    return ParagraphStyle(name, parent=styles["Normal"], **base)

title_style    = s("T",  fontName="Helvetica-Bold", fontSize=18, spaceAfter=4, leading=22)
sub_style      = s("S",  fontSize=10, textColor=MID, spaceAfter=14)
label_style    = s("L",  fontName="Helvetica-Bold", fontSize=10, textColor=ACCENT, spaceBefore=14, spaceAfter=2)
subject_style  = s("SB", fontName="Helvetica-Bold", fontSize=10, spaceAfter=8)
body_style     = s("B",  leftIndent=12)
note_style     = s("N",  fontName="Helvetica-Oblique", fontSize=8.5, textColor=MID, leftIndent=12)
sig_style      = s("SG", fontSize=9, textColor=MID, leftIndent=12)
seq_head_style = s("SH", fontName="Helvetica-Bold", fontSize=13, textColor=WHITE, spaceAfter=0)
meta_style     = s("M",  fontSize=9)

def banner(text, color=ACCENT):
    t = Table([[Paragraph(text, seq_head_style)]], colWidths=[6.6*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), color),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    return t

def hr():
    return HRFlowable(width="100%", thickness=0.5,
                      color=colors.HexColor("#e2e8f0"),
                      spaceAfter=8, spaceBefore=8)

def body(lines):
    return [Paragraph(l, body_style) for l in lines]

def sig(name="Deanne [Last Name]"):
    return Paragraph(
        f"{name}<br/>On behalf of Hansel Dobbs, MNAA, CDEI | ValuSignal 2026",
        sig_style)

story = []

# ── Title ──────────────────────────────────────────────────
story.append(Paragraph("ValuSignal 2026", title_style))
story.append(Paragraph("Promo Email Sequences · June 2026", sub_style))
story.append(Table([[
    Paragraph("Code: <b>EARLYBIRD</b>",       meta_style),
    Paragraph("Expires: <b>June 20, 2026</b>", meta_style),
    Paragraph("Price with code: <b>$187</b>",  meta_style),
]], colWidths=[2.2*inch]*3))
story.append(Spacer(1, 14))
story.append(hr())

# ── SEQUENCE 1 ─────────────────────────────────────────────
story.append(Spacer(1, 6))
story.append(banner("SEQUENCE 1 — Warm Leads  (~200 from Instantly)"))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "Sent from Deanne / Eunice personal inboxes · Reply-to: Hansel · NOT Instantly",
    note_style))

# S1 E1
story.append(Paragraph("EMAIL 1 — Day 0", label_style))
story.append(Paragraph("Subject: On behalf of Hansel Dobbs and ValuSignal 2026", subject_style))
story += body([
    "{{first_name}},",
    "You'd looked at ValuSignal 2026 earlier this year. Hansel flagged your name and asked us to reach out before September.",
    "Early bird closed June 15, but he wanted you to have code EARLYBIRD at checkout. It brings the ticket to $187 and it's valid for the next three days.",
    "September 18-19. Fully virtual, no flights, no hotels. Speakers include Kelly Davids (President, The Appraisal Foundation) and Tony Pistilli (Restb.ai, 30+ years in real estate valuation).",
    "Register at valusignal.com/register with code EARLYBIRD. Reply here with any questions and I'll make sure Hansel sees it.",
])
story.append(sig())
story.append(hr())

# S1 E2
story.append(Paragraph("EMAIL 2 — Day 3  ·  Blank subject (threads under Email 1)", label_style))
story += body([
    "{{first_name}},",
    "Today is the last day to use code EARLYBIRD. It expires tonight and brings the ticket to $187 at valusignal.com/register.",
    "Early bird closed June 15. This was the three-day extension Hansel held for people he'd already been talking with.",
    "Reply here if anything comes up.",
])
story.append(sig())
story.append(Spacer(1, 18))

# ── SEQUENCE 2 ─────────────────────────────────────────────
story.append(banner("SEQUENCE 2 — Cold Pipedrive Leads  (~870 contacts)", color=DARK2))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "Sent from Deanne / Eunice personal inboxes · 3 variants Email 1 · 1 shared Email 2",
    note_style))

# 1A
story.append(Paragraph("EMAIL 1A — Day 0  ·  Travel Cost Hook", label_style))
story.append(Paragraph("Subject: No travel required, {{first_name}}", subject_style))
story += body([
    "{{first_name}},",
    "The average appraiser spends more on flights and hotels to attend a national conference than the ticket itself costs.",
    "ValuSignal 2026 takes care of that. September 18-19, fully virtual, seventy-plus sessions on UAD 3.6 readiness, AI workflows, and adding work outside of AMC volume. Malinda Griffin, President of the National Association of Appraisers, is one of the speakers.",
    "Our founder, Hansel Dobbs, approved a promo code for a small group this week. Early bird closed June 15, but this brings the ticket to $187 for the next three days.",
    "Interested in the code?",
])
story.append(sig())
story.append(Paragraph('<i>reply "remove" and I\'ll update my list</i>', note_style))
story.append(hr())

# 1B
story.append(Paragraph("EMAIL 1B — Day 0  ·  UAD 3.6 Deadline Hook", label_style))
story.append(Paragraph("Subject: UAD 3.6, {{first_name}}", subject_style))
story += body([
    "{{first_name}},",
    "UAD 3.6 goes live November 2. Most appraisers I talk to are waiting to see how it plays out, which usually means scrambling when it does.",
    "ValuSignal 2026 is September 18-19, timed specifically so you're ready before it hits. It's 100% virtual, no travel costs, no time away from your desk. Jake Lew, whose firm was the first GSE-verified UAD 3.6 vendor, is one of the speakers.",
    "Our founder, Hansel Dobbs, approved a promo code for a small group this week. Early bird closed June 15, but this brings the ticket to $187 for the next three days.",
    "Interested in the code?",
])
story.append(sig())
story.append(Paragraph('<i>reply "remove" and I\'ll update my list</i>', note_style))
story.append(hr())

# 1C
story.append(Paragraph("EMAIL 1C — Day 0  ·  Contrast Hook", label_style))
story.append(Paragraph("Subject: {{first_name}}, quick question", subject_style))
story += body([
    "{{first_name}},",
    "Most appraisal conferences are built around travel. ValuSignal 2026 is not.",
    "September 18-19, fully virtual, no flights, no hotels, sessions on-demand for three months after the event. Seventy-plus sessions on UAD 3.6 readiness, AI in practice, and where the profession is headed. Kelly Davids, President of The Appraisal Foundation, is on the lineup.",
    "Our founder, Hansel Dobbs, approved a promo code for a small group this week. Early bird closed June 15, but this brings the ticket to $187 for the next three days.",
    "Interested in the code?",
])
story.append(sig())
story.append(Paragraph('<i>reply "remove" and I\'ll update my list</i>', note_style))
story.append(hr())

# E2
story.append(Paragraph("EMAIL 2 — Day 5  ·  Blank subject (threads under all variants)", label_style))
story += body([
    "{{first_name}},",
    "One thing I left out of my last note.",
    "The speaker lineup includes Kelly Davids (President, The Appraisal Foundation), Lisa Desmarais (VP of Appraisal Issues, 30+ years), Malinda Griffin (President, National Association of Appraisers), and Tony Pistilli (Restb.ai, 30+ years).",
    "This is the conversation happening at the top of the profession. UAD 3.6, AI in practice, how Fannie and Freddie are rethinking the appraisal process, and you don't need a plane ticket to be in the room.",
    "Hansel set aside code EARLYBIRD for the next three days. Early bird closed June 15, but it brings the ticket to $187.",
    "valusignal.com/register",
])
story.append(sig())

doc.build(story)
print("PDF saved to", OUTPUT)
