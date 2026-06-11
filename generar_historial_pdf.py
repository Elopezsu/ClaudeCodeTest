from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = "/Users/eunicelopez/Desktop/Historial-Salud-2026-Eunice.pdf"

AZUL      = colors.HexColor("#2C5F8A")
AZUL_CLARO= colors.HexColor("#EBF2F9")
GRIS      = colors.HexColor("#F5F5F5")
ROJO      = colors.HexColor("#C0392B")
VERDE     = colors.HexColor("#1E7E34")
TEXTO     = colors.HexColor("#222222")

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2.2*cm, bottomMargin=2.2*cm
)

base = getSampleStyleSheet()

def S(name, **kw):
    s = ParagraphStyle(name, **kw)
    return s

titulo    = S("titulo",    fontSize=18, textColor=AZUL,  fontName="Helvetica-Bold",
               spaceAfter=4,  alignment=TA_CENTER)
subtitulo = S("subtitulo", fontSize=10, textColor=TEXTO, fontName="Helvetica",
               spaceAfter=2,  alignment=TA_CENTER)
fecha_doc = S("fecha_doc", fontSize=8,  textColor=colors.grey, fontName="Helvetica-Oblique",
               spaceAfter=14, alignment=TA_CENTER)

h1        = S("h1", fontSize=13, textColor=colors.white, fontName="Helvetica-Bold",
               spaceBefore=12, spaceAfter=6, leftIndent=0,
               backColor=AZUL, borderPadding=(5,8,5,8))
h2        = S("h2", fontSize=11, textColor=AZUL, fontName="Helvetica-Bold",
               spaceBefore=10, spaceAfter=4, leftIndent=0,
               borderPadding=(0,0,2,0))
h3        = S("h3", fontSize=10, textColor=AZUL, fontName="Helvetica-Bold",
               spaceBefore=6, spaceAfter=3)

normal    = S("normal", fontSize=9, textColor=TEXTO, fontName="Helvetica",
               spaceAfter=3, leading=13)
negrita   = S("negrita", fontSize=9, textColor=TEXTO, fontName="Helvetica-Bold",
               spaceAfter=3, leading=13)
bullet    = S("bullet", fontSize=9, textColor=TEXTO, fontName="Helvetica",
               spaceAfter=2, leading=13, leftIndent=12, bulletIndent=0)
italica   = S("italica", fontSize=9, textColor=TEXTO, fontName="Helvetica-Oblique",
               spaceAfter=3, leading=13, leftIndent=12)
alerta    = S("alerta", fontSize=9, textColor=ROJO, fontName="Helvetica-Bold",
               spaceAfter=3, leading=13)
bien      = S("bien", fontSize=9, textColor=VERDE, fontName="Helvetica-Bold",
               spaceAfter=3, leading=13)

def tabla(data, col_widths, header_bg=AZUL):
    style = TableStyle([
        ("BACKGROUND",   (0,0), (-1,0),  header_bg),
        ("TEXTCOLOR",    (0,0), (-1,0),  colors.white),
        ("FONTNAME",     (0,0), (-1,0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,-1), 8),
        ("FONTNAME",     (0,1), (-1,-1), "Helvetica"),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [colors.white, GRIS]),
        ("GRID",         (0,0), (-1,-1), 0.4, colors.HexColor("#CCCCCC")),
        ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING",  (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
        ("WORDWRAP",     (0,0), (-1,-1), True),
    ])
    t = Table(data, colWidths=col_widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(style)
    return t

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CCCCCC"),
                      spaceAfter=6, spaceBefore=2)

def sp(h=6):
    return Spacer(1, h)

# ─── CONTENIDO ────────────────────────────────────────────────────────────────
story = []

# ENCABEZADO
story += [
    Paragraph("HISTORIAL DE SALUD 2026", titulo),
    Paragraph("Eunice Estela López Suárez", subtitulo),
    Paragraph("CC 1140836476  |  35 años  |  Medellín, Colombia", subtitulo),
    Paragraph("Documento actualizado: 11 de junio de 2026", fecha_doc),
    hr(),
]

# ── ANTECEDENTES ──────────────────────────────────────────────────────────────
story += [
    Paragraph("ANTECEDENTES QUIRÚRGICOS", h1), sp(2),
    Paragraph("• Hernioplastia umbilical", bullet),
    Paragraph("• Cirugía láser ocular", bullet),
    Paragraph("• Tubectomía (2023)", bullet),
    Paragraph("• Legrado uterino (2017)", bullet),
    Paragraph("• Fractura de tibia y peroné derecho (niñez)", bullet),
    Paragraph("• Bursitis patelar izquierda a los 22 años (peso muerto mal ejecutado)", bullet),
    sp(4),
    Paragraph("<b>Ciclos menstruales:</b> 4 días / cada 28 días. Eumenorrea. Menarquia a los 9 años.", normal),
    sp(4),
]

# ── DICIEMBRE 2025 ────────────────────────────────────────────────────────────
story += [
    Paragraph("DICIEMBRE 2025 — Antecedente imagenológico", h1), sp(2),
    Paragraph("26 de diciembre — RX panorámica miembros inferiores (Osteomedical)", h3),
    Paragraph(
        "Radiografía panorámica de miembros inferiores que confirmó <b>lateralización bilateral de rótulas</b>. "
        "Este hallazgo fue el punto de partida para buscar evaluación especializada de fisiatra.", normal),
    sp(4),
]

# ── ENERO 2026 ────────────────────────────────────────────────────────────────
story += [Paragraph("ENERO 2026", h1), sp(2)]

story += [
    Paragraph("6 de enero — Fisiatra Dra. María Victoria Morales Vergara (Bioforma S.A.)", h2),
    Paragraph("Primera consulta por dolor crónico en rodillas y columna.", negrita),
    Paragraph(
        "Eunice consultó por dolor en rodillas con crepitación (varios años) y dolor dorso-lumbar. "
        "Antecedente: fractura de tibia y peroné en niñez; bursitis patelar izquierda a los 22 años.", normal),
    Paragraph("<b>Radiografías tomadas en consulta:</b>", normal),
    Paragraph("• <b>Columna total:</b> leve escoliosis postural sin componente rotacional", bullet),
    Paragraph("• <b>Rodillas:</b> lateralización bilateral de rótulas + agudización de espinas tibiales", bullet),
    Paragraph(
        "Examen físico: inflamación tendones pata de ganso, puntos de contractura en temporales, ATM y esplenios "
        "(bruxismo), dolor sacroilíacas. Sin trastorno de movilidad.", normal),
    Paragraph("<b>Diagnóstico:</b> M624 Contractura muscular + M545 Lumbago no especificado", normal),
    Paragraph("<b>Plan:</b> Terapia física orofacial y cervical (5 sesiones) + Colchicina 0.5mg / 10 días", normal),
    sp(6),
]

story += [
    Paragraph("6 de enero — Wellness EpixLife", h2),
    Paragraph(
        "Evaluación de bienestar complementaria. Necesidades identificadas: antioxidantes (selenio, alfa-lipoico, "
        "sulforafano, polifenoles), minerales (cromo, molibdeno, silicio, selenio) y aminoácidos (valina, alanina, "
        "isoleucina, triptófano). Sistemas prioritarios: inmune e intestinal.", normal),
    Paragraph(
        "<b>Alimentos a evitar 90 días:</b> cerdo, centeno, sandía, mora roja, aceite de girasol, cacahuetes, "
        "brotes de soja, grosellas.", normal),
    sp(6),
]

story += [
    Paragraph("23 de enero — Ginecología Dra. Deymi Katiuska Nuñez Ávila (Virgen de Coromoto)", h2),
    Paragraph("Consulta de chequeo general ginecológico.", negrita),
    Paragraph(
        "Ecografía transvaginal: <b>miomatosis uterina múltiple FIGO 5-6</b> — mioma cara anterior ~32mm, "
        "fondo uterino ~77mm. Útero 138cc. No descarta endometriosis ni EPI. Primer hallazgo formal de los miomas.", normal),
    Paragraph("<b>Laboratorios:</b>", normal),
    tabla(
        [["Examen","Resultado","Estado"],
         ["FSH","1.0 mUI/mL","BAJO (rango luteínica 1.79–5.12)"],
         ["LH","1.28 mUI/mL","Límite inferior"],
         ["TSH","1.34 µUI/mL","Normal"],
         ["VIH 1 y 2","Negativo","—"],
         ["Hepatitis B Ag HBs","Negativo","—"],
         ["VDRL","No reactivo","—"]],
        [5.5*cm, 4*cm, 7*cm]
    ),
    sp(6),
]

story += [
    Paragraph("26 de enero — Citología cervicouterina (Citofemme IPS)", h2),
    Paragraph(
        "<b>Negativa para lesión intraepitelial y malignidad</b> (Sistema Bethesda 2001). "
        "VPH no detectable (dic 2024). Exudado inflamatorio leve. Cuello sano.", normal),
    Paragraph(
        "<b>Creatinina en suero: 0.91 mg/dL</b> — marcada con asterisco por estar sobre el rango femenino "
        "(0.46–0.83 mg/dL). Requiere monitoreo.", alerta),
    sp(4),
]

# ── FEBRERO 2026 ──────────────────────────────────────────────────────────────
story += [Paragraph("FEBRERO 2026", h1), sp(2)]

story += [
    Paragraph("13 de febrero — TAC abdomen y pelvis con contraste (Ginecología)", h2),
    Paragraph("Ordenado por la Dra. Nuñez para dimensionar la miomatosis. Resultados:", normal),
    Paragraph("• <b>Mioma exofítico en fundus anterior: 87mm</b> — el más grande y de mayor relevancia clínica", bullet),
    Paragraph("• Miomas intramurales adicionales de hasta 29mm", bullet),
    Paragraph("• <b>Colelitiasis</b> (cálculos en vesícula) sin signos de colecistitis activa", bullet),
    Paragraph("• Ovarios de aspecto normal", bullet),
    Paragraph(
        "<b>Nota:</b> Este TAC es la imagen de referencia más reciente. A junio 2026 han pasado 4 meses sin "
        "imagen de control — eco transvaginal de seguimiento PENDIENTE Y URGENTE.", alerta),
    sp(6),
]

story += [
    Paragraph("19 de febrero — Seguimiento Fisiatra Dra. María Victoria Morales", h2),
    Paragraph("Evolución positiva: contracturas cervicales y dorsales desaparecidas. Solo quedan puntos gatillo "
              "en temporales, ATM y maseteros lado derecho (zona del bruxismo). Mejoró el sueño. "
              "Practicando consciencia de relajación orofacial.", normal),
    Paragraph("<b>Indicación:</b> Continuar hábitos. Revisión en 2 meses.", normal),
    sp(4),
]

# ── JUNIO 2026 ────────────────────────────────────────────────────────────────
story += [Paragraph("JUNIO 2026", h1), sp(2)]

story += [
    Paragraph("3 de junio — YOU Regenerative Medicine — Dra. Luisa María Mejía Arboleda (El Poblado)", h2),
    Paragraph("Consulta integral de medicina funcional — la más completa hasta la fecha.", negrita),
    Paragraph("<b>Síntomas activos al consultar:</b>", normal),
    Paragraph("• Dolor cervical y bruxismo, dorsal, lumbar, rodillas", bullet),
    Paragraph("• Distensión abdominal con gases y granos", bullet),
    Paragraph("• Spotting ~7 días antes del período", bullet),
    Paragraph("• Dispareunia y nicturia", bullet),
    Paragraph("• Caída de cabello (atribuida inicialmente al cloro de la piscina)", bullet),
    Paragraph("<b>Estilo de vida:</b> Dieta vegana ~7 meses. Fuerza 3x/sem (redujo de 5–6). "
              "Suspendió natación por caída de cabello. Duerme 8pm, despierta 3am productiva.", normal),
    Paragraph("<b>Hallazgo clave al examen:</b> Respuesta pupilar fluctuante — posible alteración del "
              "sistema nervioso autónomo y baja tolerancia al estrés.", alerta),
    Paragraph("<b>Diagnóstico:</b> R53X Malestar y fatiga + R522 Otro dolor crónico", normal),
    sp(4),
    Paragraph("<b>Fórmula médica (04/06/2026):</b>", normal),
    tabla(
        [["#","Suplemento","Indicación"],
         ["1","Proteína vegana aislada arveja+arroz 25–30g/día","Meta 115g proteína/día"],
         ["2","Complejo B metilado (Homocysteine Nutrients)","Mañana"],
         ["3","Vitamina D3 + K2","Almuerzo — 12 semanas"],
         ["4","Omega 3 vegano algas DHA+EPA 500–1000mg","Almuerzo"],
         ["5","Magnesio glicinato 300mg","Noche"],
         ["6","Glicina 3g","Noche (junto con magnesio)"],
         ["7","Creatina monohidratada 3g","Con proteína o almuerzo"],
         ["8","Probiótico (Probiessens o Plucbiotic)","90 días"],
         ["9","P-Cide Nutrabiotics 4–8 gotas","Mañana y noche — 2 botellas"],
         ["10","Vitamina C 500mg","Desayuno/almuerzo — 8 semanas"]],
        [1*cm, 8*cm, 7.5*cm]
    ),
    sp(4),
    Paragraph("<b>Suspender:</b> tierra de diatomeas, cromo picolinato (hasta HbA1c/HOMA-IR), "
              "extracto semilla de uva, aceite de orégano (mientras dure P-Cide).", normal),
    Paragraph("También se entregó cotización para células mesenquimales de cordón umbilical "
              "(25–50M) en cada rodilla como opción regenerativa articular. Control en 4–8 semanas.", normal),
    sp(6),
]

story += [
    Paragraph("9 de junio — Clínica Metco — InBody 270 + Nutricionista", h2),
    Paragraph("Consulta por peso estancado. Mismo día: medición de composición corporal.", negrita),
    sp(2),
    Paragraph("<b>InBody 270 — Composición corporal:</b>", normal),
    tabla(
        [["Parámetro","Valor","Estado"],
         ["Peso","83.8 kg","Alto (+8.3 kg del ideal 75.5 kg)"],
         ["Masa muscular","32.2 kg","Normal"],
         ["Masa grasa","25.7 kg","Alto"],
         ["% Grasa corporal","30.7%","ALTO"],
         ["Relación cintura-cadera","0.98","ALTO (normal mujer <0.85)"],
         ["Grasa visceral","Nivel 10","Límite"],
         ["Metabolismo basal","1,914 kcal","—"],
         ["Score InBody","80/100","Bueno"]],
        [6.5*cm, 4*cm, 6*cm]
    ),
    sp(4),
    Paragraph("<b>Nutricionista:</b> Propuso quemadores (termogénicos), faja y masajes de mesoterapia "
              "(advirtió que dolerían). <b>Eunice rechazó ese enfoque.</b> Lo que sí adoptó: aumentar "
              "ingesta calórica, especialmente proteína, para romper el estancamiento — recomendación "
              "que coincidió con la meta de 115g/día de la Dra. Mejia en YOU.", normal),
    sp(6),
]

story += [
    Paragraph("11 de junio — Laboratorio POCTLAB — Panel de sangre en ayunas", h2),
    tabla(
        [["Examen","Resultado","Rango","Estado"],
         ["Glucosa","74.9 mg/dL","70–100","Normal"],
         ["Insulina","4.93 µUI/mL","1.9–23","Normal"],
         ["HOMA-IR (calculado)","0.91","<2.0 normal","ÓPTIMO — sin resistencia insulínica"],
         ["T4 libre","0.96 ng/dL","0.61–1.12","Normal"],
         ["T3 libre","3.05 pg/mL","2.5–3.9","Normal"],
         ["Vitamina D 25-OH","27.75 ng/mL *","30–100","INSUFICIENTE"],
         ["Ferritina","78.60 ng/mL","11–306.8","Normal (límite inferior funcional)"],
         ["Vitamina B12","195.4 pg/mL","180–914","Suficiente pero límite para vegana"]],
        [5*cm, 3.5*cm, 3*cm, 5*cm]
    ),
    sp(4),
    Paragraph("<b>Interpretación:</b>", normal),
    Paragraph("• <b>Resistencia insulínica descartada</b> — HOMA-IR 0.91 es óptimo. "
              "El origen hormonal de los miomas se debe confirmar con estradiol + progesterona día 21.", bullet),
    Paragraph("• <b>Tiroides normal en toda la cadena</b> — TSH + T4 libre + T3 libre correctos. "
              "Falta Anti-TPO para descartar Hashimoto.", bullet),
    Paragraph("• <b>Vitamina D insuficiente</b> — 27.75 ng/mL. Óptimo funcional: 60–80 ng/mL. "
              "Hay evidencia de que la vitamina D inhibe crecimiento de fibromas. D3+K2 ya recetada.", bullet),
    Paragraph("• <b>B12 en zona de alerta</b> — 195.4 pg/mL. Óptimo funcional para vegana: >300. "
              "Reservas hepáticas en descenso sostenido.", bullet),
    Paragraph("• <b>Ferritina normal</b> — descarta anemia ferropénica como causa de caída de cabello.", bullet),
    Paragraph("• <b>Caída de cabello:</b> causas activas = Vit D insuficiente + B12 límite + "
              "estrés crónico (telogen effluvium). Zinc aún sin medir.", bullet),
    sp(6),
]

# ── DIMENSIÓN EMOCIONAL ───────────────────────────────────────────────────────
story += [
    Paragraph("DIMENSIÓN EMOCIONAL Y TERAPÉUTICA (2026)", h1), sp(2),
    Paragraph("• <b>Terapia con Ester</b> — proceso de varios años, en curso", bullet),
    Paragraph("• <b>Formación en constelaciones familiares</b> — 2026, impacto significativo reportado", bullet),
    Paragraph("• <b>Biodescodificación</b> — sesión realizada en 2026", bullet),
    Paragraph("<b>Audio de Ester (03/06/2026):</b>", normal),
    Paragraph(
        '"La escoliosis es carga y desesperanza. En la contracción el cuerpo se desartícula. '
        'Cada día: respira y mándale a los huesos. Yoga y meditación."', italica),
    Paragraph(
        "La conexión mente-cuerpo ha sido confirmada de forma independiente por la fisiatra, la médica funcional, "
        "la terapeuta y la biodescodificación: el sistema nervioso autónomo en hiperactivación crónica "
        "amplifica la inflamación sistémica y contribuye al cuadro completo.", normal),
    sp(6),
]

# ── PROTOCOLO ACTIVO ──────────────────────────────────────────────────────────
story += [
    Paragraph("PROTOCOLO ACTIVO — iniciado 10 de junio de 2026", h1), sp(2),
    Paragraph("<b>Respiración diafragmática diaria:</b> 10 minutos cada mañana antes de revisar el celular.", normal),
    Paragraph("Técnica: inhala 4s → retén 4s → exhala 6s. Activa el nervio vago para regular el sistema nervioso simpático.", normal),
    sp(6),
]

# ── COTIZACIÓN YOU ────────────────────────────────────────────────────────────
story += [
    Paragraph("COTIZACIÓN PENDIENTE — YOU Regenerative Medicine (rodillas)", h1), sp(2),
    tabla(
        [["Plan","Precio","Incluye"],
         ["Essential Recovery","$14,700,000 COP",
          "25M células madre por rodilla + ortopedista + seguimiento 6 meses"],
         ["Advanced Regeneration","$24,390,000 COP",
          "Sueroterapia desinflamatoria (3 sesiones) + 50M células madre + exosomas + ortopedista + seguimiento 6 meses"],
         ["Signature Regeneration ★","$26,150,000 COP",
          "Todo lo anterior + 8 sesiones cámara hiperbárica O2 100%"]],
        [4.5*cm, 4*cm, 8*cm]
    ),
    sp(4),
    Paragraph("Decisión pendiente hasta después de la cita con el endocrinólogo. "
              "<b>Antes de iniciar cualquier terapia IV deben ser informados de los fibromas activos</b> "
              "para ajustar el protocolo.", alerta),
    sp(6),
]

# ── PRÓXIMOS PASOS ────────────────────────────────────────────────────────────
story += [
    Paragraph("ESTADO ACTUAL Y PRÓXIMOS PASOS — JUNIO 2026", h1), sp(2),

    Paragraph("Resuelto hasta ahora", h3),
    Paragraph("✓ Sin resistencia insulínica (HOMA-IR 0.91)", bullet),
    Paragraph("✓ Tiroides funciona correctamente en toda la cadena", bullet),
    Paragraph("✓ Citología negativa, VPH negativo", bullet),
    Paragraph("✓ Contracturas musculares en gran parte resueltas", bullet),
    Paragraph("✓ Caída de cabello: descartada anemia ferropénica", bullet),
    sp(4),

    Paragraph("Pendiente urgente", h3),
    Paragraph("1. <b>Eco transvaginal de control</b> — última imagen del fibroma de 87mm fue febrero 2026", bullet),
    Paragraph("2. <b>Endocrinólogo</b> — llevar historial completo + todos los labs", bullet),
    sp(4),

    Paragraph("Documentos para el endocrinólogo", h3),
    Paragraph("• TAC feb/2026 (mioma 87mm)", bullet),
    Paragraph("• Labs ene/2026 (FSH 1.0, TSH 1.34, creatinina 0.91)", bullet),
    Paragraph("• Labs jun/2026 (panel completo con HOMA-IR)", bullet),
    Paragraph("• Fórmula médica Dra. Mejia jun/2026", bullet),
    Paragraph("• InBody 270 del 09/06/2026", bullet),
    sp(4),

    Paragraph("Preguntas clave para el endocrinólogo", h3),
    Paragraph("1. HOMA-IR 0.91 descarta resistencia insulínica — ¿cuál es la vía hormonal de los miomas? "
              "Pedir <b>estradiol + progesterona en día 21 del ciclo</b>", bullet),
    Paragraph("2. Vitamina D 27.75 con fibromas activos — ¿qué dosis de D3 para llegar a 60–80 ng/mL?", bullet),
    Paragraph("3. B12 195.4 siendo vegana — ¿metilcobalamina sublingual o inyectable adicional?", bullet),
    Paragraph("4. <b>Anti-TPO</b> para descartar Hashimoto autoinmune", bullet),
    Paragraph("5. ¿El fibroma de 87mm tiene componente hormonal tratable sin cirugía?", bullet),
    sp(4),

    Paragraph("Labs pendientes — próximo mes", h3),
    tabla(
        [["Examen","Por qué"],
         ["Anti-TPO","Descartar Hashimoto autoinmune"],
         ["Estradiol + Progesterona (día 21)","Confirmar dominancia estrogénica — driver de miomas"],
         ["Zinc","Caída de cabello + recuperación muscular"],
         ["Folato","Complementa perfil B12"],
         ["Homocisteína","Riesgo cardiovascular + metilación"],
         ["HbA1c","Promedio glucosa últimos 3 meses"]],
        [5*cm, 11.5*cm]
    ),
]

# ── BUILD ──────────────────────────────────────────────────────────────────────
doc.build(story)
print(f"PDF generado: {OUTPUT}")
