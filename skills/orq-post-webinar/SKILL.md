---
name: orq-post-webinar
description: Orquestador post-webinar para Mateo Folador. Lanza 5 subagentes en paralelo inmediatamente después de cada webinar para procesar la segmentación de asistentes, generar los emails de seguimiento, crear los mensajes para setters, producir el contenido de repurposing, y preparar los mensajes de WhatsApp. Todo listo en minutos.
user-invocable: true
---

# /orq-post-webinar — Orquestador Post-Webinar

## Qué hace este agente

Activa el sistema completo de seguimiento post-webinar en paralelo:
- Segmenta a los asistentes en Champions / Explorers / No-Survey / No-Show
- Genera emails de seguimiento personalizados por segmento
- Prepara los mensajes de los setters con contexto de cada prospecto
- Crea el contenido inmediato de repurposing del webinar
- Prepara los mensajes de WhatsApp para la comunidad

**Cuándo activarlo:** Dentro de los primeros 30 minutos después de terminar el webinar.

---

## Cómo activarlo

```
/orq-post-webinar

Tema del webinar: [título]
Fecha y hora: [fecha + hora]
Total registrados: [número]
Total asistentes: [número]
Total respondieron encuesta: [número]
Programa promovido: [Samurai 8 AI / Ventaja AI / otro]
Precio del programa: [monto]
¿Hay oferta de tiempo limitado?: [Sí - fecha vencimiento / No]
Highlights del webinar: [2–3 momentos clave, preguntas frecuentes del chat]
Lista de Champions identificados: [nombres + emails + señales de compra, si están disponibles]
```

---

## Arquitectura de subagentes (ejecución paralela)

```
ORQUESTADOR POST-WEBINAR
├── [PARALELO] Subagente 1: Segmentation Analyzer
├── [PARALELO] Subagente 2: Email Sequence Writer (por segmento)
├── [PARALELO] Subagente 3: Setter Briefing Generator
├── [PARALELO] Subagente 4: WhatsApp Community Messenger
└── [PARALELO] Subagente 5: Repurposing Quick Hits
```

---

## Instrucciones del orquestador

### PASO 1 — Análisis inicial

El orquestador procesa los datos del webinar y determina:
- Ratio de conversión: registrados → asistentes → encuesta → Champions
- Perfil del segmento más valioso esta semana
- Urgencia del seguimiento (¿hay oferta con fecha límite?)
- Qué información tienen los setters y qué necesitan

### PASO 2 — Lanzar 5 subagentes en paralelo

**Subagente 1: Segmentation Analyzer**
```
Tarea: Crear el protocolo de segmentación para este webinar específico
Input: Datos del webinar + lista de asistentes si está disponible
Output:
- Criterios de clasificación Champions / Explorers / No-Survey / No-Show
- Template de encuesta de seguimiento (si no se usó durante el webinar)
- Prioridad de contacto: ¿a quién llama el setter primero?
- Estimado de conversión esperada por segmento basado en el webinar
- Checklist para el setter antes de cada llamada
```

**Subagente 2: Email Sequence Writer**
```
Tarea: Generar la secuencia completa de emails post-webinar por segmento
Programa: [PROGRAMA] | Precio: [PRECIO] | Oferta: [SÍ/NO + FECHA]
Output para cada segmento:

CHAMPIONS (asistieron + encuesta + señales de compra):
- Email 1 (enviar en los próximos 60 min): Gracias + resumen + CTA directo al programa
- Email 2 (día 2): La pregunta más frecuente del webinar + respuesta profunda + CTA
- Email 3 (día 5): Caso de éxito + urgencia si hay oferta + último CTA

EXPLORERS (asistieron + encuesta sin señales claras):
- Email 1 (hoy): Gracias + resumen + recurso gratuito adicional
- Email 2 (día 3): Contenido de valor relacionado al tema + CTA suave
- Email 3 (día 7): Pregunta de diagnóstico + invitación a llamada exploratoria

NO-SURVEY (asistieron pero no respondieron encuesta):
- Email único: Resumen del webinar + enlace a encuesta pendiente + CTA

NO-SHOW (se registraron pero no asistieron):
- Email 1 (hoy): "Te lo perdiste" + resumen + link a grabación si aplica
- Email 2 (día 4): El punto más valioso del webinar + CTA
```

**Subagente 3: Setter Briefing Generator**
```
Tarea: Preparar el briefing completo para que los setters hagan las llamadas
Output:
- Brief por cada Champion identificado (si hay datos disponibles):
  * Nombre + cargo + industria
  * Lo que escribió en el chat o respondió en la encuesta
  * Señales de compra observadas
  * Ángulo de apertura de la llamada (personalizado)
  * Objeción más probable basada en su perfil
- Template de primer mensaje por WhatsApp/DM para contactar Champions
- Template de primer mensaje para Explorers
- Script de apertura de llamada (primeros 2 minutos)
- Recordatorio: preguntas de diagnóstico a hacer antes de presentar el precio
```

**Subagente 4: WhatsApp Community Messenger**
```
Tarea: Generar los mensajes para la comunidad en las próximas 48 horas
Output:
- Mensaje 1 (misma noche del webinar): Agradecimiento + highlight + pregunta de engagement
- Mensaje 2 (al día siguiente, mañana): El insight más potente del webinar + aplicación
- Mensaje 3 (pasado mañana): Pregunta frecuente del chat + respuesta completa
- Mensaje 4 (día 4): Recordatorio del programa si hay oferta activa
Tono: Cercano, como si Mateo le escribiera a un amigo. Sin formal ni corporativo.
```

**Subagente 5: Repurposing Quick Hits**
```
Tarea: Identificar y generar los 3 piezas de contenido de mayor valor inmediato del webinar
Input: Highlights del webinar proporcionados
Output:
- Post de LinkedIn para publicar mañana (usa el momento más potente del webinar)
- Quote visual (texto para diseñar como imagen): la frase más citeable
- Thread de Twitter/X (si aplica): los 5 puntos clave en formato hilo
Nota: El repurposing completo se hace con /repurpose-webinar. Esto es solo lo inmediato (24–48h).
```

### PASO 3 — Entrega final del orquestador

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-WEBINAR: [TEMA] — [FECHA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 RESUMEN DE SEGMENTACIÓN
[Criterios + estimados + prioridades]

📧 SECUENCIAS DE EMAIL
Champions: [Emails 1, 2, 3]
Explorers: [Emails 1, 2, 3]
No-Survey: [Email único]
No-Show: [Emails 1, 2]

📞 BRIEFING PARA SETTERS
[Por cada Champion + templates de contacto inicial]

💬 MENSAJES WHATSAPP (4 días)
[Mensajes 1–4 listos para copiar/pegar]

⚡ CONTENIDO INMEDIATO
[Post LinkedIn mañana + Quote visual + Thread]

🗓️ TIMELINE DE ACCIONES
Hoy (próximas 2 horas): [lista]
Mañana: [lista]
Días 2–3: [lista]
Días 4–7: [lista]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Timeline del orquestador post-webinar

| Tiempo | Acción |
|---|---|
| 0–30 min post-webinar | Activar `/orq-post-webinar` con los datos del webinar |
| 30–60 min | Revisar outputs y aprobar/ajustar emails de Champions |
| 60 min post-webinar | Enviar Email 1 a todos los segmentos |
| Misma noche | Publicar mensaje en WhatsApp comunidad |
| Día siguiente (9am) | Setters inician contacto con Champions |
| Día 2 | Post de LinkedIn del webinar |
| Día 3 | Email 2 a Champions + Explorers |

---

## Métricas que debe rastrear el orquestador

Al finalizar el ciclo (7 días post-webinar), el orquestador genera un reporte con:
- Champions contactados / llamadas agendadas / cierres
- Open rate de cada secuencia de email (si hay integración con la plataforma)
- Engagement en WhatsApp (respuestas / reacciones)
- Comparativa con webinar anterior
