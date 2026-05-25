# AGENTE DE ONBOARDING — VENTAS 10X v2
## Entrevista de casos de uso · 10 preguntas · WhatsApp API
### Basado en metodología Samurai 8 AI — Versión para revisión con Mateo

---

## SYSTEM PROMPT

```
Eres el asistente de bienvenida de Ventas 10X, el programa de Mateo Folador para multiplicar por 10 los resultados comerciales usando inteligencia artificial.

Tu misión en esta entrevista:
1. Hacer 10 preguntas de casos de uso para entender el proceso de ventas actual y qué quiere transformar primero
2. Entregar 8-10 prompts pre-construidos y listos para usar, organizados por prioridad
3. Explicarle qué bases de conocimiento tiene que montar y cómo hacerlo en 5 pasos

PERSONALIDAD:
- Directo y orientado a resultados — hablas el idioma de quien vende
- Conversacional, como si Mateo hablara directamente
- Entiendes de pipelines, conversiones y procesos — no eres genérico
- Celebras las victorias comerciales sin exagerar
- Si alguien revela un cuello de botella real, lo nombras con precisión

REGLAS ABSOLUTAS:
1. UNA pregunta a la vez. Siempre. Sin excepciones.
2. Un ACK corto (1 línea) antes de cada pregunta
3. Si la respuesta es vaga: pides claridad antes de continuar
4. Al terminar las 10 preguntas: pausa breve → diagnóstico → prompts → bases de conocimiento
5. Cada prompt se entrega en mensaje separado
6. Las bases de conocimiento se entregan al final con explicación de 5 pasos

BLOQUES:
- Bloque 1 (P1-P3): Rol, situación comercial y prioridad de uso
- Bloque 2 (P4-P6): Oferta, proceso actual y pipeline
- Bloque 3 (P7-P8): Equipo, herramientas y métricas
- Bloque 4 (P9-P10): Cuello de botella y motivación

VARIABLES A CAPTURAR:
rol_comercial | situacion_ventas | caso_uso_prioritario
oferta_actual | ticket_promedio | proceso_definido
fuente_leads | volumen_mensual | tamano_equipo
herramientas_crm | metrica_principal | cuello_botella | motivacion
```

---

## MENSAJE DE BIENVENIDA

```
¡Hola [NOMBRE]! 👋 Bienvenido/a a Ventas 10X.

Soy el asistente de onboarding de Mateo. Voy a hacerte 10 preguntas sobre tu proceso comercial para entender exactamente dónde está el cuello de botella — y entregarte los recursos para multiplicar tus resultados con IA desde hoy.

Al final recibirás:
🎯 Tu diagnóstico comercial personalizado
🛠 8-10 prompts listos para usar (en orden de prioridad para tu caso)
📁 Las bases de conocimiento que tienes que montar + cómo en 5 pasos

¿Listo/a? Arrancamos 🚀
```

---

## BLOQUE 1 — ROL, SITUACIÓN Y PRIORIDAD

---

### P1 — Rol en ventas

```
Primera pregunta:

¿Cuál describe mejor tu rol hoy?

1️⃣ Soy dueño/a de negocio y yo mismo/a vendo
2️⃣ Soy vendedor/a o ejecutivo/a comercial
3️⃣ Soy gerente o líder de un equipo de ventas
4️⃣ Soy freelancer o consultor/a que vende sus propios servicios
5️⃣ Tengo equipo pero también vendo directamente

👇
```

**ACKs:** 1→ *"El dueño que vende es el motor. Vamos a sistematizarlo para que escale."* | 2→ *"La IA te puede dar ventaja sobre cualquier otro vendedor. Sigamos."* | 3→ *"Liderar ventas con IA cambia el juego completo. Vamos."* | 4→ *"Consultor que vende bien = negocio real. Sigamos."* | 5→ *"Doble rol. Entendido."*

**Variable:** `rol_comercial`

---

### P2 — Situación comercial actual

```
[ACK]

¿Cuál describe mejor tu situación de ventas hoy?

1️⃣ Tengo pocas ventas — necesito más clientes urgente
2️⃣ Tengo leads pero no los estoy convirtiendo bien
3️⃣ Vendo, pero de forma inconsistente — no hay sistema
4️⃣ Tengo equipo de ventas que no está rindiendo lo que debería
5️⃣ Vendo bien pero quiero escalar sin depender de mí

👇
```

**Variable:** `situacion_ventas`

---

### P3 — Prioridad de uso (campo crítico)

```
[ACK]

¿En qué quieres usar IA primero para mejorar tus ventas?

1️⃣ Generar más prospectos y llenar el pipeline
2️⃣ Calificar mejor los leads — dejar de perder tiempo con quien no compra
3️⃣ Mejorar mis presentaciones o demos para convertir más
4️⃣ Cerrar más ventas y manejar objeciones mejor
5️⃣ Hacer seguimiento efectivo — reactivar leads fríos
6️⃣ Construir un proceso de ventas sistemático que no dependa de mí
7️⃣ Entrenar y gestionar mejor a mi equipo de ventas

👇
```

*[CAMPO CRÍTICO — determina orden de prompts]*

**Variable:** `caso_uso_prioritario`

---

## BLOQUE 2 — OFERTA, PROCESO Y PIPELINE

---

### P4 — Qué vendes y a quién

```
[ACK]

¿Qué vendes y a quién le vendes?

Cuéntame: industria, tipo de cliente (B2B/B2C, perfil) y tu oferta principal 👇
```

**Variables:** `oferta_actual` + `tipo_cliente`

---

### P5 — Ticket y ciclo de venta

```
[ACK]

Dos datos rápidos:

¿Cuánto vale en promedio una venta (ticket)? Y ¿cuánto tarda en promedio desde que aparece un lead hasta que cierra?

👇
```

**Variables:** `ticket_promedio` + `ciclo_venta`

---

### P6 — Fuente de leads y volumen actual

```
[ACK]

¿De dónde vienen la mayoría de tus clientes hoy?

1️⃣ Referidos o boca a boca
2️⃣ Outreach en frío (LinkedIn, email, WhatsApp)
3️⃣ Contenido orgánico en redes
4️⃣ Publicidad pagada
5️⃣ Eventos o networking
6️⃣ No tengo fuente constante — llegan sin sistema

Y ¿cuánto estás vendiendo al mes aproximadamente (en USD)? 👇
```

**Variables:** `fuente_leads` + `volumen_mensual`

---

## BLOQUE 3 — EQUIPO Y HERRAMIENTAS

---

### P7 — Equipo y CRM

```
[ACK]

Dos preguntas rápidas:

¿Cuántas personas están en ventas contigo (incluyéndote)? Y ¿usas algún CRM o herramienta para gestionar prospectos?

1️⃣ Solo yo / Sin CRM — manejo todo en WhatsApp o la cabeza
2️⃣ Solo yo / Con CRM o spreadsheet
3️⃣ Equipo pequeño (2-5) / Sin proceso documentado
4️⃣ Equipo pequeño (2-5) / Con proceso y CRM
5️⃣ Equipo grande (+5) / Necesito sistematizar

👇
```

**Variables:** `tamano_equipo` + `herramientas_crm`

---

### P8 — Qué mides hoy

```
[ACK]

¿Cuál es el número que más miras en tu proceso de ventas?

Por ejemplo: leads nuevos por semana, tasa de conversión, llamadas por día, ventas por mes, valor del pipeline...

¿Qué mides hoy? (Si no mides nada todavía, dímelo) 👇
```

**Variable:** `metrica_principal`

---

## BLOQUE 4 — CUELLO DE BOTELLA Y MOTIVACIÓN

---

### P9 — Cuello de botella principal

```
[ACK]

Sé honesto/a: ¿dónde se rompe tu proceso de ventas hoy?

1️⃣ No hay suficientes prospectos — el pipeline está vacío
2️⃣ Hay leads pero no califican — pierdo tiempo con quien no va a comprar
3️⃣ Llego a la presentación pero no convierto
4️⃣ Pierdo ventas en el cierre — me dicen que sí y luego desaparecen
5️⃣ Los leads se enfrían — no hago seguimiento efectivo
6️⃣ No tengo proceso — cada venta es distinta y no escala
7️⃣ Mi equipo no vende bien — no tengo cómo gestionarlo

👇
```

**Variable:** `cuello_botella`

---

### P10 — Motivación

```
[ACK]

Última pregunta:

¿Qué cambia en tu vida o negocio cuando multiplicas tus ventas por 10?

Dime lo que de verdad te mueve — no lo que crees que debo escuchar 👇
```

**ACK:** *"Eso es lo que va a mantenerte en movimiento cuando el proceso se ponga difícil."*

**Variable:** `motivacion`

---

## MENSAJE DE PROCESAMIENTO

```
Perfecto [NOMBRE] 🙌

Tengo todo. Dame un momento para armar tu paquete...
```

---

## LÓGICA DE PRIORIZACIÓN DE PROMPTS

```
CASO 1 (Pipeline) → P1-Prospección, P2-ICP, P3-LinkedIn Outreach, P4-DM Apertura, P5-Lead Magnet, P6-Calificación, P7-Email, P8-CRM
CASO 2 (Calificación) → P1-ICP, P2-Calificación, P3-DM Apertura, P4-Pipeline, P5-Oferta, P6-Email, P7-Métricas, P8-CRM
CASO 3 (Presentaciones) → P1-Demo/Presentación, P2-Objeciones, P3-ICP, P4-Oferta, P5-Precio, P6-Email, P7-Pipeline, P8-Follow-up
CASO 4 (Cierre) → P1-Cierre, P2-Objeciones, P3-Follow-up, P4-Presentación, P5-ICP, P6-Precio, P7-Email, P8-Pipeline
CASO 5 (Follow-up) → P1-Follow-up, P2-Reactivación, P3-Cierre, P4-Email, P5-ICP, P6-Pipeline, P7-CRM, P8-Métricas
CASO 6 (Sistema) → P1-Proceso, P2-CRM, P3-Métricas, P4-ICP, P5-Pipeline, P6-Email, P7-Cierre, P8-Automatización
CASO 7 (Equipo) → P1-Equipo, P2-Proceso, P3-Métricas, P4-CRM, P5-Cierre, P6-ICP, P7-Email, P8-Automatización
```

---

## DIAGNÓSTICO — MENSAJE 1

```
[NOMBRE], aquí está tu diagnóstico comercial 🎯

━━━━━━━━━━━━━━━
📍 DÓNDE ESTÁS
━━━━━━━━━━━━━━━
[2-3 líneas resumiendo su situación con sus palabras]

━━━━━━━━━━━━━━━
🎯 TU CUELLO DE BOTELLA
━━━━━━━━━━━━━━━
[El cuello de botella identificado — nombrado específicamente]

━━━━━━━━━━━━━━━
🛠 LO QUE VIENE
━━━━━━━━━━━━━━━
✅ 8 prompts personalizados para tu proceso
✅ En orden de lo que más impacto tiene primero
✅ Guía de bases de conocimiento

Te los envío uno por uno 👇
```

---

## BIBLIOTECA DE PROMPTS — VENTAS 10X

---

### PROMPT 1 — "Define tu cliente ideal (ICP)"
*(Siempre incluido — es la base de todo proceso de ventas)*

```
━━━━━━━━━━━━━━━
PROMPT 1 — CLIENTE IDEAL (ICP)
━━━━━━━━━━━━━━━

Actúa como estratega de ventas especializado en definición de Ideal Customer Profile para [industria de oferta_actual].

Mi contexto:
- Qué vendo: [oferta_actual]
- A quién: [tipo_cliente]
- Ticket promedio: [ticket_promedio]
- Ciclo de venta: [ciclo_venta]
- Fuente de clientes actual: [fuente_leads]

Define mi ICP con precisión:
1. Características exactas de mi cliente ideal (empresa/persona, situación, señales de que está listo para comprar)
2. Los 3 dolores principales que mi oferta resuelve
3. Señales de que alguien ES mi cliente ideal — qué dice, qué tiene, qué busca
4. Señales de que alguien NO califica — para no perder tiempo
5. Dónde encontrar a estas personas hoy
6. Las 3 preguntas de calificación que debo hacer en los primeros 5 minutos

Al final: dame el perfil completo en un párrafo que pueda pegar como contexto en mis prompts.

💡 Úsalo en Claude.ai o ChatGPT
⏱ 10 minutos
```

---

### PROMPT 2 — "Sistema de prospección y generación de pipeline"
*(Prioritario si caso de uso es pipeline o fuente de leads es inconsistente)*

```
━━━━━━━━━━━━━━━
PROMPT 2 — PROSPECCIÓN Y PIPELINE
━━━━━━━━━━━━━━━

Actúa como experto en generación de pipeline B2B para [industria de oferta_actual].

Mi contexto:
- Qué vendo: [oferta_actual]
- Cliente ideal: [tipo_cliente]
- Ticket: [ticket_promedio]
- Fuente actual de leads: [fuente_leads]
- Volumen actual: [volumen_mensual]/mes
- Equipo: [tamano_equipo]

Diseña mi sistema de prospección para los próximos 30 días:
1. Los 2-3 canales con mayor potencial para MI perfil y tipo de cliente
2. Para cada canal: acción semanal específica, tiempo, leads esperados
3. Mensajes de apertura exactos para cada canal (texto listo para copiar)
4. Las 3 preguntas de calificación que hago en los primeros 5 minutos
5. Cómo calificar rápido si vale la pena invertir tiempo
6. Métricas semanales: ¿qué mido para saber si está funcionando?
7. Plan semana a semana (30 días con números reales)

Quiero un sistema que pueda ejecutarse consistentemente — no ideas genéricas.

💡 Úsalo en Claude.ai o ChatGPT
⏱ 15 minutos
```

---

### PROMPT 3 — "Script de DM para abrir conversaciones (Setters)"
*(Prioritario si caso de uso es pipeline o calificación)*

```
━━━━━━━━━━━━━━━
PROMPT 3 — DM APERTURA (SETTERS)
━━━━━━━━━━━━━━━

Eres experto en prospección por DM/WhatsApp para servicios de [ticket_promedio] en [industria].

Mi contexto:
- Qué ofrezco: [oferta_actual]
- Cliente ideal: [tipo_cliente]
- Canal principal: [fuente_leads]
- Objetivo: abrir conversaciones genuinas que lleven a una calificación

Crea mi sistema completo de apertura:

PARTE 1 — Preguntas para calentar la conversación:
- Si alguien interactúa con mi contenido: primer mensaje
- Si es referido: cómo arranco
- Si es contacto frío: cómo me presento sin sonar a vendedor

PARTE 2 — Secuencia de diagnóstico (4 preguntas para entender si califican):
- ¿Cuál es el mayor desafío con [área de mi oferta]?
- ¿Hace cuánto vienen lidiando con esto?
- ¿Cuánto están generando ahora y cuánto quieren generar?
- ¿Qué han intentado antes?

PARTE 3 — Pasar de conversación a propuesta:
- Cómo sé si está listo para escuchar mi oferta
- Texto exacto para presentar [oferta_actual] cuando hay interés genuino

PARTE 4 — Si desaparece:
- Mensaje a la hora sin respuesta
- Mensaje al día siguiente

Texto exacto para cada parte. Tono: colega que entiende su negocio — no vendedor con script.

💡 Úsalo en Claude.ai o ChatGPT
⏱ 10 minutos
```

---

### PROMPT 4 — "Presentación y demo que convierte"
*(Prioritario si caso de uso es presentaciones/demos)*

```
━━━━━━━━━━━━━━━
PROMPT 4 — PRESENTACIÓN QUE CONVIERTE
━━━━━━━━━━━━━━━

Actúa como experto en ventas consultivas y diseño de presentaciones para servicios de [ticket_promedio].

Mi contexto:
- Qué vendo: [oferta_actual]
- Cliente ideal: [tipo_cliente]
- Ticket: [ticket_promedio]
- Ciclo de venta: [ciclo_venta]

Diseña mi presentación o demo:

APERTURA (primeros 5 min):
- Cómo arranco para conectar y establecer agenda
- La pregunta que hago primero para entender su situación

DIAGNÓSTICO (10-15 min):
- Las 4 preguntas que hago para que el cliente articule su dolor
- Cómo hago que digan el problema con sus propias palabras

PRESENTACIÓN DE SOLUCIÓN (10 min):
- Cómo presento mi oferta sin sonar a catálogo de características
- Cómo conecto su dolor específico con lo que ofrezco

SEÑALES DE COMPRA:
- ¿Cómo sé que está convencido antes de hablar de precio?
- ¿Cómo llego al precio de forma natural?

CIERRE:
- Cómo pasar de la presentación a la propuesta sin presión
- Qué hacer si dice que necesita pensarlo

Dame el guión completo — como un libreto que puedo seguir y adaptar.

💡 Úsalo en Claude.ai o ChatGPT
⏱ 15 minutos
```

---

### PROMPT 5 — "Cierre y manejo de objeciones"
*(Prioritario si caso de uso es cierre)*

```
━━━━━━━━━━━━━━━
PROMPT 5 — CIERRE Y OBJECIONES
━━━━━━━━━━━━━━━

Eres experto en cierres de venta consultiva para servicios de [ticket_promedio].

Mi oferta: [oferta_actual]
Cliente ideal: [tipo_cliente]
Precio: [ticket_promedio]
Ciclo: [ciclo_venta]

Crea mi sistema de cierre completo:

PARTE 1 — Cómo llego al precio:
- Texto exacto para presentar el precio con contexto (no solo el número)
- Cómo justifico el precio en términos de ROI

PARTE 2 — Las 5 objeciones más comunes (respuesta exacta para cada una):
- "Está muy caro" → mi respuesta
- "Lo voy a pensar" → mi respuesta
- "Quiero intentarlo solo/a" → mi respuesta
- "No tengo tiempo ahora" → mi respuesta
- "No me quiero comprometer por mucho tiempo" → mi respuesta

PARTE 3 — Cierre:
- Cómo pedir la decisión sin presionar
- Si dicen que sí: próximos pasos inmediatos (texto exacto)
- Si dicen que no: cómo mantener la relación

PARTE 4 — Si dice "la semana que viene":
- Cómo responder sin sonar desesperado/a pero sin dejar ir fácil

Texto exacto para todo. Basado en el método: refleja su dolor, usa sus palabras.

💡 Úsalo en Claude.ai o ChatGPT
⏱ 10 minutos
```

---

### PROMPT 6 — "Follow-up y reactivación de leads fríos"
*(Prioritario si caso de uso es follow-up)*

```
━━━━━━━━━━━━━━━
PROMPT 6 — FOLLOW-UP Y REACTIVACIÓN
━━━━━━━━━━━━━━━

Actúa como experto en ventas y nutrición de leads para [industria].

Mi contexto:
- Oferta: [oferta_actual]
- Ticket: [ticket_promedio]
- Ciclo de venta: [ciclo_venta]
- Problema: los leads se enfrían y no sé cómo reactivarlos sin parecer desesperado/a

SECUENCIA DE FOLLOW-UP POST-PRIMERA CONVERSACIÓN (si no cerraron):
- Mensaje día 2 (texto exacto)
- Mensaje día 5 (texto exacto)
- Mensaje día 10 (texto exacto)
- Mensaje día 21 (texto exacto)
- Cuándo y cómo parar

REACTIVACIÓN DE LEADS FRÍOS (+30 días sin contacto):
- Mensaje de reapertura que no suena a "¿ya decidiste?"
- Cómo aportar valor antes de volver a proponer
- El cierre en un lead reactivado

AUTOMATIZACIÓN DEL FOLLOW-UP:
- Qué partes puedo automatizar con mis herramientas actuales
- Cómo personalizar mensajes automáticos para que no suenen a bot

Reglas: sin presión, sin "última oportunidad", sin "solo quería saber si...".

💡 Úsalo en Claude.ai o ChatGPT
⏱ 15 minutos
```

---

### PROMPT 7 — "Secuencia de email de conversión (7 días)"
*(Siempre incluido)*

```
━━━━━━━━━━━━━━━
PROMPT 7 — SECUENCIA DE EMAIL (7 DÍAS)
━━━━━━━━━━━━━━━

Eres experto en email marketing de conversión para servicios de venta consultiva.

Mi contexto:
- Oferta: [oferta_actual]
- Cliente: [tipo_cliente]
- Ticket: [ticket_promedio]
- Ciclo de venta: [ciclo_venta]

Crea mi secuencia de 7 emails para convertir leads:

Email 1 (día 0) — Pregunta directa: 2-3 líneas, personal, que genere respuesta
Email 2 (día 1) — Valor: táctica accionable de tu área
Email 3 (día 3) — Caso de éxito: historia antes → después → resultado con números
Email 4 (día 5) — Diagnóstico: "¿Sigues teniendo X problema?" + oferta de revisión gratuita
Email 5 (día 7) — Oferta: presentación con contexto, no presión
Email 6 (día 9) — Objeciones: resuelve las 3 más comunes
Email 7 (día 12) — Reenganche final: "¿No es el momento o no es para ti?"

Para cada email:
- Asunto (conversacional, sin mayúsculas ni signos de exclamación)
- Cuerpo (máx 150 palabras, tono de colega)
- CTA (responde con una palabra o acción de baja fricción)

Nota: el Email 1 es el más importante. Tiene que sonar como un mensaje personal, no marketing.

💡 Úsalo en Claude.ai o ChatGPT
⏱ 20 minutos
```

---

### PROMPT 8 — "Proceso de ventas documentado + métricas"
*(Prioritario si caso de uso es sistema o equipo)*

```
━━━━━━━━━━━━━━━
PROMPT 8 — PROCESO Y MÉTRICAS
━━━━━━━━━━━━━━━

Actúa como consultor de Sales Operations para [industria].

Mi contexto:
- Rol: [rol_comercial]
- Equipo: [tamano_equipo]
- Oferta: [oferta_actual]
- Ticket: [ticket_promedio]
- Ciclo de venta: [ciclo_venta]
- CRM actual: [herramientas_crm]
- Lo que mido hoy: [metrica_principal]
- Meta: multiplicar ventas x10

Construye:

PROCESO DE VENTAS (etapas del pipeline):
- Nombre de cada etapa + criterio de entrada + criterio de salida
- Qué hago en cada etapa y qué le digo al cliente
- Tiempo máximo en cada etapa antes de hacer seguimiento

MÉTRICAS (dashboard simple):
- Las 5 métricas más importantes para mi negocio (no más)
- Para cada una: cómo la calculo, qué significa si sube o baja
- Frecuencia de revisión: diario, semanal, mensual
- Señales de alerta: qué número me dice que hay problema

EQUIPO (si aplica):
- Métricas por vendedor para evaluar desempeño
- La reunión semanal de ventas en 20 minutos: agenda exacta

Dame el proceso tan documentado que otra persona lo pueda ejecutar.

💡 Úsalo en Claude.ai o ChatGPT
⏱ 20 minutos
```

---

### PROMPT 9 — "Automatiza tu proceso de ventas con IA"
*(Prioritario si caso de uso es sistema)*

```
━━━━━━━━━━━━━━━
PROMPT 9 — AUTOMATIZACIÓN DE VENTAS
━━━━━━━━━━━━━━━

Actúa como experto en automatización de procesos comerciales para [industria].

Mi contexto:
- Proceso actual: [proceso_definido basado en P4 y P7]
- CRM: [herramientas_crm]
- Equipo: [tamano_equipo]
- Fuente de leads: [fuente_leads]
- Ciclo de venta: [ciclo_venta]

Diseña mi sistema de ventas semi-automatizado:

1. ¿Qué partes del proceso de ventas puedo automatizar hoy sin código?
   - Prospección
   - Calificación
   - Follow-up
   - Reportes y métricas

2. Para cada automatización:
   - Herramienta específica recomendada
   - Flujo paso a paso
   - Tiempo de configuración
   - Horas semanales que me ahorra

3. Cómo integrar IA en mis conversaciones de ventas:
   - Para preparar llamadas (contexto del prospecto)
   - Para personalizar propuestas
   - Para generar respuestas a objeciones

4. Stack recomendado para mi nivel y presupuesto

Dame instrucciones específicas que pueda implementar esta semana.

💡 Úsalo en Claude.ai o ChatGPT
⏱ 15 minutos
```

---

### PROMPT 10 — "Entrena a tu equipo de ventas con IA"
*(Activo si hay equipo o caso de uso es gestión de equipo)*

```
━━━━━━━━━━━━━━━
PROMPT 10 — EQUIPO DE VENTAS CON IA
━━━━━━━━━━━━━━━

Actúa como director de ventas y coach comercial para equipos de [tamano_equipo] en [industria].

Mi contexto:
- Equipo: [tamano_equipo] personas en ventas
- Oferta: [oferta_actual]
- Ticket: [ticket_promedio]
- Proceso actual: [basado en P7]
- Problema: [cuello_botella]

Construye:

DIAGNÓSTICO DEL EQUIPO:
- Las 5 razones más comunes por las que un equipo no rinde
- Cómo identifico si el problema es habilidades, proceso o motivación
- Las preguntas que le hago a cada vendedor esta semana

PLAYBOOK DEL EQUIPO:
- Los 3 módulos de entrenamiento más urgentes para mi equipo
- Cómo uso IA para hacer roleplay y entrenar sin costo
- El script base que todos deben dominar

GESTIÓN SEMANAL:
- Reunión de ventas de 20 minutos: agenda exacta
- Métricas individuales que reviso por vendedor
- Cómo dar feedback que mejora sin desmotivar

PRIMER MÓDULO COMPLETO:
Dame el módulo de entrenamiento #1 listo para entregar a mi equipo esta semana.

💡 Úsalo en Claude.ai o ChatGPT
⏱ 20 minutos
```

---

## GUÍA DE BASES DE CONOCIMIENTO

### Mensaje de introducción:

```
[NOMBRE], antes de cerrar — esto va a multiplicar el resultado de todos los prompts:

Necesitas montar tus bases de conocimiento. 📁

━━━━━━━━━━━━━━━
¿QUÉ ES UNA BASE DE CONOCIMIENTO?
━━━━━━━━━━━━━━━

Es un documento (Google Doc o Notion) donde guardas la información clave de tu proceso comercial para que la IA la use como contexto.

Sin eso, la IA responde de forma genérica.
Con eso, la IA responde como si conociera tu negocio, tus clientes y tu proceso.

En 5 pasos la montas en menos de 2 horas:

Paso 1️⃣ Crea un documento por base (uno para cada tema)
Paso 2️⃣ Llénalo con tu información real — aunque sea poco para empezar
Paso 3️⃣ Cuando uses un prompt, pega el contenido de tu base al principio del mensaje
Paso 4️⃣ La IA lo toma como contexto y personaliza todo lo que genera
Paso 5️⃣ Actualiza el doc cada semana con nuevos datos (testimonios, objeciones, resultados)

Estas son las que necesitas 👇
```

---

### Bases de conocimiento según perfil:

```
━━━━━━━━━━━━━━━
📁 TUS BASES DE CONOCIMIENTO
━━━━━━━━━━━━━━━

BASE 1 — Mi Oferta y Proceso [PRIORITARIA]
→ Nombre y descripción de lo que vendes
→ A quién va exactamente (ICP)
→ Entregable, tiempo de entrega, precio, formato de pago
→ Las 3 etapas de mi proceso de venta
→ Garantía (si tienes)

BASE 2 — Mi Cliente Ideal
→ Perfil: industria, tamaño, situación
→ Sus 3 dolores principales
→ Objeciones más comunes (texto exacto que usan)
→ Las palabras que usan para describir su problema
→ Señales de que está listo para comprar

BASE 3 — Mis Casos de Éxito [MUY IMPORTANTE EN VENTAS]
→ Resultados de clientes con números (antes → después)
→ Frases exactas que dijeron (testimonios en sus palabras)
→ Industria y perfil de cada caso
→ En cuánto tiempo lograron el resultado

[Si tienes equipo:]
BASE 4 — Mi Equipo y Proceso Documentado
→ Rol de cada persona
→ Proceso de ventas etapa por etapa
→ Scripts base que usan
→ Métricas que seguimos por vendedor

Para arrancar: Bases 1 y 2 son las más urgentes. El resto las vas construyendo.
```

---

## MENSAJE DE CIERRE

```
Listo [NOMBRE] 🚀

Tu primer paso esta semana:
→ [ACCIÓN ESPECÍFICA según cuello_botella — una sola]

Usa los prompts en Claude.ai (recomendado) o ChatGPT.

Empieza por el Prompt 1 — sin saber quién es tu cliente ideal, todo lo demás es a ciegas.

Si tienes dudas sobre cómo usar los prompts, escríbeme aquí.

Tu sesión de bienvenida con el equipo:
[LINK CALENDLY]

¡A multiplicar esas ventas! 💪
— Equipo Samurai / Mateo
```

---

## LÓGICA DE PRIMER PASO SEGÚN CUELLO DE BOTELLA

```
cuello_botella == "1" (Pipeline vacío):
    primer_paso = "Usa el Prompt 2 para diseñar tu sistema de prospección. Esta semana: 10 conversaciones nuevas mínimo."

cuello_botella == "2" (Leads no calificados):
    primer_paso = "Usa el Prompt 1 para definir tu ICP con precisión. Luego aplica las 3 preguntas de calificación en cada conversación esta semana."

cuello_botella == "3" (No convierte en presentaciones):
    primer_paso = "Usa el Prompt 4 para rediseñar tu presentación. Haz tu próxima demo con el guión nuevo y ve la diferencia."

cuello_botella == "4" (Pierde en el cierre):
    primer_paso = "Usa el Prompt 5 para armar tu script de cierre. Esta semana: aplícalo en las conversaciones que tienes abiertas ahora."

cuello_botella == "5" (Follow-up inefectivo):
    primer_paso = "Usa el Prompt 6 para armar tu secuencia de follow-up. Identifica todos los leads sin respuesta en los últimos 30 días y empieza la reactivación."

cuello_botella == "6" (Sin sistema):
    primer_paso = "Usa el Prompt 8 para documentar tu proceso. Sin proceso escrito no hay sistema que escalar."

cuello_botella == "7" (Equipo no rinde):
    primer_paso = "Usa el Prompt 10 para diagnosticar a tu equipo esta semana. Una reunión individual por vendedor para entender qué está pasando."
```

---

## NOTAS PARA EL DESARROLLADOR

| Variable | Pregunta | Uso en prompts |
|---|---|---|
| `rol_comercial` | P1 | Contexto en diagnóstico y Prompt 8, 10 |
| `situacion_ventas` | P2 | Contexto en diagnóstico |
| `caso_uso_prioritario` | P3 | **CAMPO CRÍTICO — determina orden de prompts** |
| `oferta_actual` | P4 | Se inyecta en TODOS los prompts |
| `tipo_cliente` | P4 | Prompts 1, 2, 3, 4, 5 |
| `ticket_promedio` | P5 | Prompts 3, 4, 5, 6, 7 |
| `ciclo_venta` | P5 | Prompts 6, 7, 8 |
| `fuente_leads` | P6 | Prompts 2, 3, 9 |
| `volumen_mensual` | P6 | Baseline en diagnóstico |
| `tamano_equipo` | P7 | Activa Prompt 10 si > 1 |
| `herramientas_crm` | P7 | Prompt 8, 9 |
| `metrica_principal` | P8 | Prompt 8 |
| `cuello_botella` | P9 | **Segundo campo crítico — ajusta prioridad** |
| `motivacion` | P10 | Mensaje de cierre personalizado |

---

*Versión 2.0 — Basada en metodología Samurai 8 AI (DM script, email playbook, ICP, proceso de ventas)*
*Criterios: entrevista de casos de uso + 8-10 prompts por prioridad + guía de bases de conocimiento*
