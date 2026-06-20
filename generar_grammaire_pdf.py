#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera un PDF bonito y fácil de leer del cuaderno Grammaire Active.
Parsea el markdown Grammaire-Active-Frances-Eunice.md y lo renderiza con reportlab:
 - cada unidad en su propia página
 - tablas de conjugación a color
 - cajas de colores para tips (verde), advertencias (rojo) e info (azul)
"""
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

SRC = "/Users/eunicelopez/Desktop/ClaudeCodeTest/Grammaire-Active-Frances-Eunice.md"
OUTPUT = "/Users/eunicelopez/Desktop/Grammaire-Active-Frances-Eunice.pdf"

# Paleta: azul francés + acentos
AZUL      = colors.HexColor("#1F4E79")
AZUL_MED  = colors.HexColor("#2E6CA4")
AZUL_CLARO= colors.HexColor("#EAF1F8")
ROJO      = colors.HexColor("#C0392B")
ROJO_CLARO= colors.HexColor("#FBEAE8")
VERDE     = colors.HexColor("#1E7E34")
VERDE_CLARO=colors.HexColor("#E8F5EC")
AMBAR     = colors.HexColor("#B7791F")
AMBAR_CLARO=colors.HexColor("#FDF6E3")
GRIS      = colors.HexColor("#F4F6F8")
TEXTO     = colors.HexColor("#222222")

USABLE_W = A4[0] - 4*cm

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=1.8*cm, bottomMargin=1.8*cm,
    title="Grammaire Active - Francais A1-B1",
    author="Eunice Lopez",
)

def S(name, **kw):
    return ParagraphStyle(name, **kw)

titulo   = S("titulo", fontSize=24, textColor=AZUL, fontName="Helvetica-Bold",
             spaceAfter=4, alignment=TA_CENTER, leading=28)
subtit   = S("subtit", fontSize=12, textColor=AZUL_MED, fontName="Helvetica-Oblique",
             spaceAfter=14, alignment=TA_CENTER, leading=16)
h1       = S("h1", fontSize=15, textColor=colors.white, fontName="Helvetica-Bold",
             spaceBefore=2, spaceAfter=10, backColor=AZUL,
             borderPadding=(7,8,7,8), leading=19)
h2       = S("h2", fontSize=12, textColor=AZUL, fontName="Helvetica-Bold",
             spaceBefore=10, spaceAfter=5, leading=15)
h3       = S("h3", fontSize=10.5, textColor=AZUL_MED, fontName="Helvetica-Bold",
             spaceBefore=7, spaceAfter=3, leading=13)
normal   = S("normal", fontSize=9.5, textColor=TEXTO, fontName="Helvetica",
             spaceAfter=4, leading=14)
bullet   = S("bullet", fontSize=9.5, textColor=TEXTO, fontName="Helvetica",
             spaceAfter=2, leading=14, leftIndent=14, bulletIndent=2)
celda    = S("celda", fontSize=8, textColor=TEXTO, fontName="Helvetica", leading=10)
celda_h  = S("celda_h", fontSize=8, textColor=colors.white, fontName="Helvetica-Bold", leading=10)
celda_c1 = S("celda_c1", fontSize=8, textColor=AZUL, fontName="Helvetica-Bold", leading=10)
# Cajas (callouts)
caja_txt = S("caja_txt", fontSize=9, textColor=TEXTO, fontName="Helvetica", leading=13)

EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF"
    "\U00002190-\U000021FF\U00002B00-\U00002BFF️‍]", flags=re.UNICODE)

def strip_emoji(s):
    return EMOJI.sub("", s).strip()

def inline(text):
    """Convierte markdown inline a markup de reportlab."""
    text = strip_emoji(text)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"~~(.+?)~~", r'<font color="#C0392B"><strike>\1</strike></font>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`(.+?)`", r'<font face="Courier"><b>\1</b></font>', text)
    return text.strip()

def caja(lines, kind):
    bg, bd = {"warn": (ROJO_CLARO, ROJO), "tip": (VERDE_CLARO, VERDE),
              "info": (AZUL_CLARO, AZUL_MED)}[kind]
    flowed = [Paragraph(inline(l), caja_txt) for l in lines if l.strip()]
    t = Table([[flowed]], colWidths=[USABLE_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("LINEBEFORE", (0,0), (-1,-1), 3, bd),
        ("BOX", (0,0), (-1,-1), 0.5, bd),
        ("LEFTPADDING", (0,0), (-1,-1), 9),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    return t

def make_table(rows):
    header, body = rows[0], rows[1:]
    ncol = len(header)
    # ancho por columna segun contenido
    maxlen = [max(len(strip_emoji(r[i])) if i < len(r) else 0 for r in rows) for i in range(ncol)]
    total = sum(maxlen) or 1
    widths = [max(1.4*cm, USABLE_W*(m/total)) for m in maxlen]
    scale = USABLE_W/sum(widths)
    widths = [w*scale for w in widths]
    data = []
    data.append([Paragraph(inline(c), celda_h) for c in header])
    for r in body:
        cells = []
        for i in range(ncol):
            raw = r[i] if i < len(r) else ""
            st = celda_c1 if i == 0 else celda
            cells.append(Paragraph(inline(raw), st))
        data.append(cells)
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), AZUL_MED),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, GRIS]),
        ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#C7D2DD")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 4),
        ("RIGHTPADDING", (0,0), (-1,-1), 4),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ]))
    return t

def parse_table_row(line):
    parts = line.strip().strip("|").split("|")
    return [p.strip() for p in parts]

# ---------- Parser principal ----------
with open(SRC, encoding="utf-8") as f:
    lines = f.readlines()

story = []
i = 0
first_h1 = True
n = len(lines)

def flush_quote(buf):
    if not buf:
        return
    joined = " ".join(buf)
    kind = "info"
    if "⚠️" in joined or "OJO" in joined or "Trampa" in joined or "trampa" in joined:
        kind = "warn"
    elif "💡" in joined or "Truco" in joined or "Astuce" in joined or "Regla de oro" in joined or "regla" in joined.lower():
        kind = "tip"
    story.append(caja(buf, kind))
    story.append(Spacer(1, 5))

while i < n:
    raw = lines[i].rstrip("\n")
    line = raw.strip()

    # separadores
    if line in ("---", "***", "___"):
        i += 1
        continue

    # blockquote (posible multilinea)
    if line.startswith(">"):
        buf = []
        while i < n and lines[i].strip().startswith(">"):
            buf.append(lines[i].strip()[1:].strip())
            i += 1
        flush_quote(buf)
        continue

    # tabla markdown
    if line.startswith("|") and i+1 < n and re.match(r"^\|[\s:|-]+\|?$", lines[i+1].strip()):
        rows = [parse_table_row(line)]
        i += 2  # saltar header + separador
        while i < n and lines[i].strip().startswith("|"):
            rows.append(parse_table_row(lines[i].strip()))
            i += 1
        story.append(make_table(rows))
        story.append(Spacer(1, 6))
        continue

    # headings
    if line.startswith("# "):
        txt = strip_emoji(line[2:])
        if first_h1:
            story.append(Paragraph(inline(line[2:]), titulo))
            first_h1 = False
        else:
            story.append(PageBreak())
            story.append(Paragraph(inline(line[2:]), h1))
        i += 1
        continue
    if line.startswith("## "):
        story.append(Paragraph(inline(line[3:]), h2))
        i += 1
        continue
    if line.startswith("### "):
        # subtitulo del doc (justo despues del titulo) vs h3 normal
        if len(story) <= 1:
            story.append(Paragraph(inline(line[4:]), subtit))
        else:
            story.append(Paragraph(inline(line[4:]), h3))
        i += 1
        continue

    # listas
    m = re.match(r"^(\d+)\.\s+(.*)", line)
    if m:
        story.append(Paragraph(inline(m.group(2)), bullet, bulletText=m.group(1)+"."))
        i += 1
        continue
    if line.startswith("- ") or line.startswith("* "):
        story.append(Paragraph(inline(line[2:]), bullet, bulletText="•"))
        i += 1
        continue

    # vacio
    if not line:
        i += 1
        continue

    # parrafo normal
    story.append(Paragraph(inline(line), normal))
    i += 1

# pie de pagina con numeros
def footer(canvas, d):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.grey)
    canvas.drawCentredString(A4[0]/2, 1*cm,
        f"Grammaire Active · Français A1–B1 · Eunice López — page {d.page}")
    canvas.restoreState()

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("PDF generado:", OUTPUT)
