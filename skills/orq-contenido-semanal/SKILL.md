---
name: orq-contenido-semanal
description: Orquestador de contenido semanal para Mateo Folador. Lanza 6 subagentes en paralelo para generar simultáneamente posts de LinkedIn, mensajes de WhatsApp, email, brief de video, historias de Instagram, y el calendario de publicación. Entrega todo el contenido de la semana en una sola ejecución.
user-invocable: true
---

# /orq-contenido-semanal — Orquestador de Contenido Semanal

## Qué hace este agente

Coordina 6 subagentes especializados que trabajan en paralelo para entregar el pack de contenido completo de la semana en el menor tiempo posible.

**Tiempo estimado:** 3–5 minutos (vs. 30–45 min si se hiciera secuencialmente)

---

## Cómo activarlo

```
/orq-contenido-semanal

Semana del: [fecha]
Tema central: [ej. "Automatización de ventas con IA"]
¿Hay webinar?: [Sí - fecha/hora / No]
¿Lanzamiento activo?: [Sí - programa + precio / No]
Caso de éxito disponible: [nombre + resultado / ninguno]
Novedad del ecosistema: [herramienta nueva / logro / hito / ninguna]
Tono de la semana: [más educativo / más vendedor / equilibrado]
```

---

## Arquitectura de subagentes (ejecución paralela)

```
ORQUESTADOR SEMANAL
├── [PARALELO] Subagente 1: LinkedIn Posts Generator
├── [PARALELO] Subagente 2: WhatsApp Community Writer
├── [PARALELO] Subagente 3: Email Semanal Writer
├── [PARALELO] Subagente 4: Video Brief Creator
├── [PARALELO] Subagente 5: Instagram Stories Writer
└── [SECUENCIAL] Subagente 6: Calendar Assembler (espera los 5 anteriores)
```

---

## Instrucciones del orquestador

Al recibir el input del usuario, el orquestador:

### PASO 1 — Análisis de contexto

Antes de lanzar subagentes, el orquestador procesa:
- El tema central y lo descompone en 5 ángulos distintos (uno por canal)
- El balance 70/30 (valor vs. negocio) según si hay lanzamiento activo
- Qué tipo de contenido va a qué canal según la audiencia de cada uno
- El tono apropiado para la semana

**Distribución de ángulos:**
- LinkedIn: Perspectiva de industria / autoridad / casos / tendencias
- WhatsApp: Conversacional / tips rápidos / engagement / comunidad
- Email: Profundidad + relación 1:1 / storytelling extendido
- Video: Educación visual / tutorial / proceso en pantalla
- Instagram: Behind the scenes / lifestyle de trabajo / prueba social

### PASO 2 — Lanzar 5 subagentes en paralelo

El orquestador invoca simultáneamente:

**Subagente 1: LinkedIn Posts Generator**
```
Tarea: Generar 5 posts de LinkedIn para la semana del [FECHA]
Tema central: [TEMA]
Distribución: 1 post perspectiva provocadora (lunes), 1 tutorial/framework (martes),
1 storytelling/caso (miércoles), 1 contenido de negocio (jueves), 1 reflexión (viernes)
¿Webinar?: [SÍ/NO + DETALLES]
¿Lanzamiento?: [SÍ/NO + DETALLES]
Tono: Directo, basado en prueba. Sin motivacional genérico.
Contexto de marca: Mateo Folador / Samurai 8 AI / Ventaja AI
Output: 5 posts completos con formato, emojis y hashtags
```

**Subagente 2: WhatsApp Community Writer**
```
Tarea: Generar 7 mensajes de WhatsApp para la comunidad de ~14K personas
Tema central: [TEMA]
¿Hay webinar esta semana?: [SÍ/NO + DETALLES]
¿Lanzamiento activo?: [SÍ/NO]
Tono: Conversacional, cercano, sin parrafadas. Máximo 8 líneas por mensaje.
Distribución: Lunes (arrancada), Martes (tip), Miércoles (caso/historia),
Jueves (webinar reminder o engagement), Viernes (cierre de semana),
Sábado (negocio si hay lanzamiento), Domingo (preparación mental)
Output: 7 mensajes numerados y listos para copiar/pegar
```

**Subagente 3: Email Semanal Writer**
```
Tarea: Generar el email semanal para la lista
Tema central: [TEMA]
¿Caso de éxito disponible?: [SÍ/NO + DETALLES]
¿CTA principal?: [webinar / programa / descarga / ninguno]
Estructura: Hook + cuerpo (valor) + CTA + P.D.
Longitud: 300–500 palabras
Output: 3 opciones de asunto + preview text + email completo
```

**Subagente 4: Video Brief Creator**
```
Tarea: Crear el brief de video para la semana
Tema: [TEMA]
Plataformas: YouTube (8–15 min) + versión corta para Reels/TikTok (60–90 seg)
Output: Título (3 opciones) + concepto de thumbnail + estructura del guion
+ hook completo (primeros 30 segundos palabra por palabra)
+ CTA del final
```

**Subagente 5: Instagram Stories Writer**
```
Tarea: Crear 3 historias de Instagram para la semana
Historia 1 (lunes): Pregunta de engagement
Historia 2 (miércoles): Tip visual con instrucción de diseño
Historia 3 (viernes): Behind the scenes + CTA si hay webinar/lanzamiento
Output: Copy de cada historia + instrucción visual (color, texto en pantalla, sticker sugerido)
```

### PASO 3 — Lanzar Subagente 6 con outputs de los 5 anteriores

**Subagente 6: Calendar Assembler**
```
Tarea: Integrar todos los outputs anteriores en un calendario semanal
Input: Los 5 outputs de los subagentes anteriores
Output: Tabla de calendario con: canal | día | hora óptima | pieza de contenido | notas
+ checklist de publicación diaria
+ notas de coherencia (asegura que el mismo tema no se repite igual en 2 canales el mismo día)
```

### PASO 4 — Entrega final del orquestador

El orquestador consolida todos los outputs y los entrega en este orden:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PACK DE CONTENIDO — Semana del [FECHA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 CALENDARIO DE LA SEMANA
[tabla de 5 días × 5 canales]

📌 LINKEDIN (5 posts)
[Post Lunes]
[Post Martes]
[Post Miércoles]
[Post Jueves]
[Post Viernes]

💬 WHATSAPP (7 mensajes)
[Mensaje 1–7]

📧 EMAIL
Asunto A: / Asunto B: / Asunto C:
Preview:
[Cuerpo completo]

🎬 VIDEO BRIEF
[Título + estructura + hook completo]

📲 HISTORIAS INSTAGRAM
[Historia 1–3 con instrucciones visuales]

✅ CHECKLIST DE PUBLICACIÓN
[Por día]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Garantías de calidad del orquestador

Antes de entregar, el orquestador verifica:
- ¿El tema central es consistente en todos los canales sin ser repetitivo?
- ¿La distribución 70/30 valor/negocio está respetada?
- ¿Ninguna pieza suena igual a la anterior? (variedad de ángulos)
- ¿Los CTAs son coherentes con lo que hay disponible esta semana?
- ¿El tono de cada canal está calibrado correctamente?

---

## Contexto de marca (compartido con todos los subagentes)

- **Voz de Mateo:** Directo, específico, basado en prueba. Nunca motivacional vacío.
- **Audiencia:** Consultores, coaches, agencias, founders de LATAM en LinkedIn. Comunidad amplia en WhatsApp.
- **Evitar:** Emojis excesivos, frases de gurú, estadísticas sin fuente, "cambia tu vida"
- **Programas activos:** Samurai 8 AI ($3K–$10K) | Ventaja AI ($500–$2K) | Ventas 10X
- **Diferenciador:** IA aplicada a operaciones y ventas reales, no IA genérica
