---
name: orq-caso-de-exito
description: Orquestador constructor de casos de éxito para Mateo Folador / Samurai 8 AI. Lanza 4 subagentes en paralelo para transformar el resultado de un cliente en: activos de contenido multipropósito, documento de caso de estudio, kit completo de ventas, y campaña de difusión. Convierte cada resultado en una máquina de prueba social.
user-invocable: true
---

# /orq-caso-de-exito — Orquestador Constructor de Caso de Éxito

## Qué hace este agente

Cuando un cliente de Samurai 8 AI / Ventaja AI logra un resultado notable, este orquestador lo convierte en el activo de prueba social más valioso del negocio — simultáneamente en 4 dimensiones.

**Cuándo activarlo:**
- Cliente alcanza su milestone de 30 / 60 / 90 días
- Cliente comparte un resultado inesperadamente bueno
- Cliente deja un testimonial voluntario
- Mateo/equipo identifica un resultado que vale la pena documentar

---

## Cómo activarlo

```
/orq-caso-de-exito

Nombre del cliente: [nombre o seudónimo si no autoriza]
Cargo/Industria: [cargo + sector]
Programa: [Samurai 8 AI / Ventaja AI / Ventas 10X]
Situación ANTES: [qué le pasaba, en sus palabras si es posible]
Qué implementó en el programa: [módulos, herramientas, cambios]
Resultado concreto: [número + tiempo + qué cambió]
Quote del cliente: [frase textual si existe]
¿Autoriza uso de nombre y foto?: [Sí / Solo nombre / Solo iniciales / Seudónimo]
¿Hay captura de pantalla o evidencia?: [Sí - describir / No]
¿El cliente puede hacer una llamada de 15 min para grabar testimonio?: [Sí / No / Preguntar]
ICP más parecido a este cliente: [perfil de la audiencia que más se va a identificar]
```

---

## Arquitectura de subagentes (ejecución paralela)

```
ORQUESTADOR CASO DE ÉXITO
├── [PARALELO] Subagente 1: Content Assets Creator
├── [PARALELO] Subagente 2: Case Study Document Builder
├── [PARALELO] Subagente 3: Sales Kit Generator
└── [PARALELO] Subagente 4: Distribution Campaign Planner
```

---

## Instrucciones del orquestador

### PASO 1 — Evaluación del caso

El orquestador determina:
- Potencia del caso (1–5): ¿Qué tan sorprendente es el resultado?
- Transferibilidad: ¿Cuántos ICPs pueden identificarse con este caso?
- Privacidad: Qué nivel de información puede compartirse
- Formatos prioritarios según el potencial del caso
- Qué hace único este caso vs. los que ya existen en el portfolio

### PASO 2 — Lanzar 4 subagentes en paralelo

**Subagente 1: Content Assets Creator**
```
Tarea: Generar todos los activos de contenido directo del caso
Output:

1. POST DE LINKEDIN (storytelling largo, 300–500 palabras):
   - Hook con el resultado (sin contexto — genera curiosidad)
   - Quién era antes
   - El momento decisivo
   - Qué hizo (sin revelar todo el método)
   - El resultado concreto
   - La lección aplicable
   - CTA suave + pregunta de engagement

2. VERSIÓN CORTA PARA WHATSAPP (máx 8 líneas):
   - Resultado → antes → cómo → qué aprender
   - Pregunta de engagement al final

3. VERSIÓN PARA HISTORIAS DE INSTAGRAM (3 slides):
   - Slide 1: El resultado (número grande, impactante)
   - Slide 2: El antes/después en 2–3 bullets
   - Slide 3: CTA o reflexión

4. THREAD DE TWITTER/X (8–10 tweets):
   - Tweet 1: El resultado como hook
   - Tweets 2–7: El proceso desglosado
   - Tweet 8: La lección
   - Tweet 9: CTA

5. QUOTE VISUAL (para diseño):
   - La frase más citeable del caso en 1–2 líneas
   - Atribución: "— [NOMBRE], [CARGO]"
   - Fondo recomendado y jerarquía tipográfica
```

**Subagente 2: Case Study Document Builder**
```
Tarea: Construir el documento de caso de estudio completo
Output: Documento de 600–800 palabras (PDF/Notion)

Estructura:
PORTADA:
- Título: [RESULTADO EN BOLD] — El caso de [NOMBRE/INDUSTRIA]
- Tagline: "De [ANTES] a [DESPUÉS] en [TIEMPO] con [PROGRAMA]"

RESUMEN EJECUTIVO (100 palabras):
- Quién es el cliente, cuál era el problema, cuál fue el resultado

EL CONTEXTO (150 palabras):
- Situación del cliente antes con detalle suficiente para que el lector se identifique
- Los intentos anteriores que no funcionaron

EL PROCESO (200 palabras):
- Qué módulos del programa usó
- Cuál fue el primer cambio implementado
- Los obstáculos encontrados y cómo los superó
- El sistema que construyó (sin revelar el método completo — genera curiosidad sobre el programa)

EL RESULTADO (100 palabras):
- Números exactos + tiempo
- Resultado secundario inesperado (si existe)
- Cómo describe el cliente su situación ahora

QUÉ APRENDEMOS (100 palabras):
- 3 lecciones transferibles para el lector
- Cómo aplica esto a su situación

EL CLIENTE EN SUS PALABRAS:
- Quote completo (1–3 párrafos)

PRÓXIMOS PASOS PARA EL LECTOR:
- CTA al programa con 1 enlace

NOTAS LEGALES/PRIVACIDAD:
- Nivel de autorización del cliente
```

**Subagente 3: Sales Kit Generator**
```
Tarea: Transformar el caso en herramientas directas de ventas
Output:

1. QUOTE DE SETTER (para usar en llamadas de ventas):
   Una sola oración, poderosa, para decir verbalmente:
   "[NOMBRE] pasó de [ANTES] a [DESPUÉS] en [TIEMPO] — [DETALLE SORPRESA]."

2. MINI-DECK SLIDE (descripción para diseñar):
   - Slide del caso para usar en presentaciones o pantallas compartidas en Zoom
   - Layout: nombre + cargo + resultado + quote + foto si hay autorización

3. TESTIMONIAL ESTRUCTURADO PARA LANDING PAGE:
   - Versión larga (150 palabras): para landing pages de venta
   - Versión media (50 palabras): para secciones de testimonios
   - Versión corta (15 palabras): para headlines y banners

4. RESPUESTA TEMPLATE PARA OBJECIÓN:
   - Objeción que este caso refuta directamente
   - Cómo mencionar el caso en la llamada cuando surge esa objeción
   - Template: "Déjame contarte de [NOMBRE]. Estaba exactamente en tu situación: [ANTES]. En [TIEMPO], [RESULTADO]. ¿Qué te parece eso?"

5. EMAIL DE PROSPECCIÓN (para DMs o outbound):
   - Template de mensaje frío basado en el caso
   - Para enviar a prospectos con perfil similar al del cliente exitoso
```

**Subagente 4: Distribution Campaign Planner**
```
Tarea: Planear la distribución estratégica del caso en los próximos 30 días
Output:

PLAN DE DISTRIBUCIÓN (30 días):

Semana 1 — Lanzamiento del caso:
- Día 1: Post de LinkedIn (storytelling largo)
- Día 2: Mensaje WhatsApp a la comunidad
- Día 3: Historias de Instagram
- Día 5: Thread de Twitter/X
- Día 7: Email a la lista con el caso completo

Semana 2 — Amplificación:
- Post de LinkedIn desde el ángulo de la lección (no del caso)
- WhatsApp: mini-tip relacionado con el método del caso
- Solicitar al cliente que comparta el post si autorizó nombre

Semana 3 — Activación de ventas:
- Usar el caso en el próximo webinar (guion de 2 min preparado)
- Incluir el case study en el doc de oferta actualizado (/oferta-samurai)
- Usar el quote del setter en la próxima llamada de ventas

Semana 4 — Evergreen:
- Actualizar landing page con el nuevo testimonial
- Agregar el caso al banco de casos de éxito del programa
- Evaluar si el cliente puede hacer un video testimonial de 60 segundos

BANCOS A ACTUALIZAR:
- [ ] Landing page del programa
- [ ] Documento de oferta (oferta-samurai)
- [ ] Presentación de ventas (setter deck)
- [ ] Email automático de nurture
- [ ] Onboarding de nuevos clientes (como ejemplo inspiracional)
```

### PASO 3 — Entrega final del orquestador

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CASO DE ÉXITO: [NOMBRE/SEUDÓNIMO]
[RESULTADO EN 1 LÍNEA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📱 ACTIVOS DE CONTENIDO
[Post LinkedIn + WhatsApp + Historias + Thread + Quote visual]

📄 CASO DE ESTUDIO COMPLETO
[Documento de 600–800 palabras listo para PDF/Notion]

💼 KIT DE VENTAS
[Quote setter + Slide + Testimoniales x3 + Respuesta objeción + Email frío]

📅 PLAN DE DISTRIBUCIÓN 30 DÍAS
[Calendario + bancos a actualizar]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Principios del orquestador

- **Un caso bien documentado vale más que 10 posts de opinión** — es la prueba más poderosa que existe
- **Nunca exagerar un resultado** — la especificidad y honestidad hacen el caso creíble
- **El cliente es el héroe, no el programa** — el programa es el vehículo, no el protagonista
- **Distribuir en momentos distintos** — no saturar todos los canales el mismo día con el mismo caso
- **Construir el banco de casos** — cada caso es un activo permanente que se reutiliza en ventas durante meses o años
