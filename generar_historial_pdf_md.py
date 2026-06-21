#!/usr/bin/env python3
"""Genera el PDF del historial de salud parseando directamente el Markdown,
para que el PDF siempre refleje la última versión del .md."""
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_CENTER

SRC = "/Users/eunicelopez/Desktop/ClaudeCodeTest/Historial-Salud-2026-Eunice.md"
OUTPUT = "/Users/eunicelopez/Desktop/Historial-Salud-2026-Eunice.pdf"

AZUL   = colors.HexColor("#2C5F8A")
AZULBG = colors.HexColor("#EBF2F9")
GRIS   = colors.HexColor("#F5F5F5")
ROJO   = colors.HexColor("#C0392B")
TEXTO  = colors.HexColor("#222222")

doc = SimpleDocTemplate(OUTPUT, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm,
                        topMargin=2*cm, bottomMargin=2*cm)


def S(name, **kw):
    return ParagraphStyle(name, **kw)


titulo = S("titulo", fontSize=17, textColor=AZUL, fontName="Helvetica-Bold",
           spaceAfter=4, alignment=TA_CENTER)
sub    = S("sub", fontSize=9, textColor=TEXTO, fontName="Helvetica",
           spaceAfter=2, alignment=TA_CENTER)
fecha  = S("fecha", fontSize=8, textColor=colors.grey, fontName="Helvetica-Oblique",
           spaceAfter=10, alignment=TA_CENTER)
h1 = S("h1", fontSize=12, textColor=colors.white, fontName="Helvetica-Bold",
       spaceBefore=12, spaceAfter=6, backColor=AZUL, borderPadding=(5,8,5,8))
h2 = S("h2", fontSize=10.5, textColor=AZUL, fontName="Helvetica-Bold",
       spaceBefore=9, spaceAfter=4)
normal = S("normal", fontSize=9, textColor=TEXTO, fontName="Helvetica",
           spaceAfter=3, leading=13)
bullet = S("bullet", fontSize=9, textColor=TEXTO, fontName="Helvetica",
           spaceAfter=2, leading=13, leftIndent=12, bulletIndent=2)
quote  = S("quote", fontSize=9, textColor=ROJO, fontName="Helvetica-Oblique",
           spaceAfter=4, leading=13, leftIndent=10, backColor=colors.HexColor("#FBEDEC"),
           borderPadding=(5,6,5,6))
cell   = S("cell", fontSize=8, textColor=TEXTO, fontName="Helvetica", leading=11)
cellb  = S("cellb", fontSize=8, textColor=colors.white, fontName="Helvetica-Bold", leading=11)


def inline(t):
    """Convierte **negrita**, *itálica* y emojis básicos a markup de reportlab."""
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    return t


with open(SRC, encoding="utf-8") as f:
    lines = f.read().split("\n")

story = []
i = 0
n = len(lines)
# Encabezado (primeras líneas)
while i < n:
    ln = lines[i].rstrip()
    if ln.startswith("# "):
        story.append(Paragraph(inline(ln[2:]), titulo))
    elif ln.startswith("**CC"):
        story.append(Paragraph(inline(ln.replace("**", "")), sub))
    elif ln.startswith("*Documento"):
        story.append(Paragraph(ln.strip("*"), fecha))
        i += 1
        break
    i += 1

while i < n:
    ln = lines[i].rstrip()
    if not ln.strip() or ln.strip() == "---":
        i += 1
        continue
    if ln.startswith("## "):
        story.append(Paragraph(inline(ln[3:]), h1))
    elif ln.startswith("### "):
        story.append(Paragraph(inline(ln[4:]), h2))
    elif ln.startswith("> "):
        story.append(Paragraph(inline(ln[2:]), quote))
    elif ln.lstrip().startswith(("- ", "* ")):
        txt = ln.lstrip()[2:]
        story.append(Paragraph(inline(txt), bullet, bulletText="•"))
    elif re.match(r"^\s*\d+\.\s", ln):
        num, txt = re.match(r"^\s*(\d+)\.\s(.*)", ln).groups()
        story.append(Paragraph(inline(txt), bullet, bulletText=f"{num}."))
    elif ln.lstrip().startswith("|"):
        # recolectar bloque de tabla
        rows = []
        while i < n and lines[i].lstrip().startswith("|"):
            rows.append(lines[i].strip())
            i += 1
        i -= 1
        parsed = []
        for r_idx, row in enumerate(rows):
            cells = [c.strip() for c in row.strip("|").split("|")]
            if all(re.fullmatch(r":?-+:?", c.strip()) for c in cells):
                continue  # separador
            parsed.append(cells)
        if parsed:
            ncol = len(parsed[0])
            data = []
            for r_idx, cells in enumerate(parsed):
                cells = (cells + [""] * ncol)[:ncol]
                sty = cellb if r_idx == 0 else cell
                data.append([Paragraph(inline(c), sty) for c in cells])
            tbl = Table(data, repeatRows=1, hAlign="LEFT")
            tbl.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), AZUL),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, GRIS]),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]))
            story.append(Spacer(1, 2))
            story.append(tbl)
            story.append(Spacer(1, 4))
    else:
        story.append(Paragraph(inline(ln), normal))
    i += 1

doc.build(story)
print("PDF generado:", OUTPUT)
