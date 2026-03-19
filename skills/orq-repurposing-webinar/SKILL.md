---
name: orq-repurposing-webinar
description: Orquestador de repurposing de webinar para Mateo Folador. Lanza 5 subagentes en paralelo para convertir una transcripción de webinar en semanas de contenido: posts de LinkedIn, emails de campaña, clips de video, mensajes de WhatsApp, y el artículo largo. Entrega el plan de publicación completo de 3 semanas.
user-invocable: true
---

# /orq-repurposing-webinar — Orquestador de Repurposing de Webinar

## Qué hace este agente

Procesa la transcripción de un webinar y lanza 5 subagentes en paralelo para generar 3 semanas de contenido simultáneamente.

**Diferencia con `/repurpose-webinar`:** El skill básico genera el contenido secuencialmente. Este orquestador lo hace todo en paralelo, en menos tiempo, con mayor especialización por canal.

**Cuándo activarlo:** 24–48 horas después del webinar (el contenido inmediato ya se manejó con `/orq-post-webinar`).

---

## Cómo activarlo

```
/orq-repurposing-webinar

Transcripción del webinar: [pegar aquí — puede ser parcial o resumen]
Tema: [título del webinar]
Fecha del webinar: [fecha]
Programa promovido: [Samurai 8 AI / Ventaja AI / otro]
¿Hay grabación disponible?: [Sí / No]
Highlights identificados: [los 3–5 momentos que más resonaron con la audiencia]
Preguntas del chat más frecuentes: [lista si están disponibles]
¿Mencionaste casos de éxito?: [Sí - cuáles / No]
Objetivo del repurposing: [más conversiones / más autoridad / más engagement / todo]
```

---

## Arquitectura de subagentes (ejecución paralela)

```
ORQUESTADOR REPURPOSING
├── [PARALELO] Subagente 1: LinkedIn Content Extractor
├── [PARALELO] Subagente 2: Email Campaign Writer
├── [PARALELO] Subagente 3: Video Clip Identifier
├── [PARALELO] Subagente 4: WhatsApp Content Adapter
└── [PARALELO] Subagente 5: Long-Form Article Writer
```

Después de los 5 anteriores:
```
└── [SECUENCIAL] Subagente 6: Publishing Calendar Builder
```

---

## Instrucciones del orquestador

### PASO 1 — Análisis de la transcripción

El orquestador lee la transcripción e identifica:
- El argumento central (la tesis del webinar en 1 oración)
- Los 10 mejores momentos candidatos a convertirse en contenido
- Las 5 mejores frases citables (quotables)
- Los momentos de storytelling (historias contadas)
- Los mitos desmontados (contenido contrarian)
- Las preguntas del chat que quedaron sin respuesta completa
- Los datos/estadísticas mencionados

### PASO 2 — Lanzar 5 subagentes en paralelo

**Subagente 1: LinkedIn Content Extractor**
```
Tarea: Extraer y escribir 12 posts de LinkedIn a partir del webinar
Input: Transcripción completa + highlights
Output: 12 posts completos con distribución de formatos:
- 3 posts de perspectiva/opinión (ángulo contrarian o insight profundo)
- 2 posts de tutorial/framework (los pasos accionables del webinar)
- 2 posts de storytelling (historias expandidas del webinar)
- 2 posts "pregunta del chat → respuesta completa" (1 pregunta = 1 post)
- 2 posts de caso de éxito (si los mencionó)
- 1 post de reflexión/cierre (lección central del webinar)

Para cada post:
- Texto completo listo para publicar
- Formato indicado (texto / carrusel / encuesta)
- Hook de la primera línea (el más potente posible)
- Semana de publicación recomendada (distribución en 3 semanas)
```

**Subagente 2: Email Campaign Writer**
```
Tarea: Generar la campaña de emails post-webinar para las 3 semanas siguientes
(Los emails de los primeros 7 días ya los generó /orq-post-webinar)
Input: Transcripción + tema + programa + casos de éxito mencionados
Output: 4 emails para semanas 2 y 3:

Email 4 (semana 2, día 10): "La pregunta que nadie hace sobre [TEMA]"
- Respuesta profunda a algo que no se cubrió en el webinar
- Desarrolla un punto secundario que quedó corto

Email 5 (semana 2, día 14): "El error más común que veo en [ICP]"
- Desmonta un mito relacionado con el tema del webinar
- CTA suave al programa

Email 6 (semana 3, día 17): Caso de éxito expandido
- Toma un caso mencionado en el webinar y lo desarrolla completo
- Incluye resultado + mecanismo + lección aplicable

Email 7 (semana 3, día 21): Cierre del tema + nuevo horizonte
- Cierre del arco narrativo de este webinar
- Teaser del siguiente webinar o tema
- CTA al programa si hay oferta activa

Para cada email:
- 3 opciones de asunto
- Preview text
- Cuerpo completo (300–500 palabras)
```

**Subagente 3: Video Clip Identifier**
```
Tarea: Identificar y describir los 6 mejores clips del webinar para edición
Input: Transcripción + highlights + si hay grabación disponible
Output para cada uno de los 6 clips:

Clip 1 — Hook de apertura (30–60 seg)
Clip 2 — El mito desmontado (60–90 seg)
Clip 3 — El framework central (2–4 min)
Clip 4 — Historia de cliente (1–3 min)
Clip 5 — La mejor pregunta del Q&A (60–90 seg)
Clip 6 — El cierre más potente (45–60 seg)

Para cada clip:
- Timecode aproximado en la transcripción
- Título del clip (el hook visual en pantalla)
- Por qué este clip funciona para redes sociales
- Plataformas recomendadas (YouTube / Reels / TikTok)
- Caption para publicar con el clip
- Texto para subtítulos automáticos (primeras 5–7 líneas)
```

**Subagente 4: WhatsApp Content Adapter**
```
Tarea: Adaptar el webinar en 10 mensajes de WhatsApp para las 3 semanas
Input: Highlights + preguntas del chat + casos de éxito
Output: 10 mensajes numerados por día de publicación:

Semana 2 (post-webinar):
- Día 8: Insight #2 más potente del webinar + pregunta de aplicación
- Día 10: Respuesta a la pregunta del chat más frecuente
- Día 12: Mini caso de éxito (3–4 líneas)
- Día 14: Recurso adicional relacionado con el tema

Semana 3:
- Día 15: "Lo que no alcancé a decir en el webinar..."
- Día 17: Framework del webinar en 3 bullets aplicables hoy
- Día 19: Testimonial/resultado de alguien que aplicó lo del webinar
- Día 21: Pregunta de diagnóstico al grupo

Semana 4 (cierre del tema):
- Día 22: Reflexión sobre el tema + teaser del próximo webinar
- Día 25: CTA final al programa si hay oferta activa

Formato: Máximo 8 líneas. Sin parrafadas. Conversacional.
```

**Subagente 5: Long-Form Article Writer**
```
Tarea: Escribir el artículo largo basado en el webinar
Output: Artículo de 900–1,200 palabras para LinkedIn Newsletter o blog

Estructura:
- Título (3 opciones — SEO + engagement)
- Introducción (150 palabras): Por qué este tema importa ahora
- Sección 1: El problema profundo (250 palabras con datos si hay)
- Sección 2: El framework de solución (300 palabras con los pasos)
- Sección 3: Caso de éxito real (200 palabras con estructura antes/después)
- Sección 4: Cómo implementarlo (200 palabras con acciones concretas)
- Cierre (100 palabras): Reflexión + CTA suave

Consideraciones:
- No debe sonar como "resumen del webinar" — debe funcionar como artículo independiente
- Incluir 2–3 frases muy citables (diseñadas para ser screenshoteable)
- Estructura visualmente escaneable (subtítulos, bullets donde corresponde)
```

### PASO 3 — Subagente 6 (secuencial): Publishing Calendar Builder

```
Tarea: Crear el calendario de publicación de 3 semanas con todo el contenido anterior
Input: Los 5 outputs anteriores
Output:
- Tabla de 3 semanas × 5 días × 3 canales (LinkedIn / WhatsApp / Email)
- Qué va en qué día y hora óptima
- Notas de coherencia (evitar publicar el mismo ángulo en 2 canales el mismo día)
- Checklist semanal de publicación
- Progresión narrativa (cómo la historia se desarrolla a lo largo de las 3 semanas)
```

---

## Entrega final del orquestador

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPURPOSING: [TEMA DEL WEBINAR]
Contenido para 3 semanas
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 LINKEDIN (12 posts)
Semana 1: Posts 1–4
Semana 2: Posts 5–8
Semana 3: Posts 9–12

📧 EMAILS (4 emails)
Email 4–7 con asuntos + cuerpo completo

🎬 CLIPS DE VIDEO (6 clips)
Descripción + timecode + captions

💬 WHATSAPP (10 mensajes)
Numerados con día de publicación

📝 ARTÍCULO LARGO
Completo, listo para publicar

📅 CALENDARIO DE 3 SEMANAS
Tabla con canal + día + hora + pieza
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total: ~35 piezas de contenido de 1 webinar
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
