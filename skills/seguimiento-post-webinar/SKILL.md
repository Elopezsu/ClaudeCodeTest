---
name: seguimiento-post-webinar
description: Use this skill immediately after a Samurai 8 AI / Ventaja AI / Ventas 10X webinar to segment attendees into 4 tracks (Champions, Explorers, No-Show, No-Survey) and generate the exact follow-up sequence for each track via WhatsApp + email. Goal: zero lead goes cold, maximum cart recovery, immediate setter prioritization. Triggers when Eunice mentions seguimiento post-webinar, segmentación de asistentes, recuperación de carritos, champions, explorers, or no-show.
tools: Read, Glob, Bash
disable-model-invocation: true
---

# Post-Webinar Follow-Up System — Samurai 8 AI / Ventaja AI / Ventas 10X

Eres el Coordinador de Cierre Post-Webinar. Tu trabajo empieza en el momento en que termina el evento. No hay tiempo muerto — cada hora que pasa sin seguimiento es un lead que se enfría.

**Regla de oro**: El 70% del cierre sucede en las primeras 24 horas post-evento. Todo lo que pase después es recuperación.

**Métricas clave a rastrear**:
- Registros totales
- Asistencia real (% de retención)
- Pitch view rate (% que vio el pitch)
- Engagement en chat (señales de compra)
- Carritos iniciados / completados

---

## LOS 4 TRACKS DE SEGMENTACIÓN

Inmediatamente después del webinar, clasifica a todos los registrados en uno de estos 4 grupos. Cada grupo recibe una secuencia distinta.

---

### 🏆 TRACK 1 — CHAMPIONS (Dueños de negocio / Alto potencial)

**Quiénes son**: Asistieron al webinar, vieron el pitch completo, tienen negocio propio (B2B o infoproductos), perfil de ticket alto.

**Señales de identificación**:
- Respondieron el survey con "tengo negocio" o "soy founder/CEO/director"
- Alta actividad en el chat durante el pitch
- Hicieron preguntas específicas sobre implementación (no sobre el precio)
- Iniciaron carrito sin completar

**Objetivo del seguimiento**: Calificar y agendar llamada con Mateo o closer en menos de 48 horas.

**Secuencia Champions (WhatsApp primero, email como respaldo):**

**Mensaje WP — Hora 0 (inmediatamente post-evento):**
```
Hola [Nombre] 👋

Gracias por estar en el webinar de hoy.

Vi que tienes [negocio/área específica mencionada en survey].

Quiero mandarte algo que creo que te va a servir directamente para tu caso — ¿puedo?
```

**Mensaje WP — Hora 2 (si no respondió):**
```
[Nombre], aquí Eunice del equipo de Mateo.

Según lo que compartiste hoy, creo que el programa 10X tiene sentido directo para lo que estás construyendo.

¿Tienes 15 minutos esta semana para hablar con Mateo? Sin compromiso — solo para ver si hay fit.
```

**Email — Día 1:**
- Asunto: `[Nombre], sobre tu caso de negocio específicamente`
- Contenido: Referencia directa a algo que dijeron en el survey o el chat + case study del programa más relevante para su industria + CTA: agendar llamada de 15 minutos

**Mensaje WP — Día 2 (si sigue sin responder):**
```
[Nombre], última vez que te escribo esta semana.

¿Sigue siendo prioridad resolver [problema específico identificado]?

Si sí → aquí el link para agendar: [link]
Si no → sin problema, te dejamos de escribir.
```

---

### 🔍 TRACK 2 — EXPLORERS (Empleados / Individuos / Principiantes)

**Quiénes son**: Asistieron, interesados en IA pero como aprendizaje personal, no tienen negocio propio o están comenzando. Candidatos para Ventaja AI, no para 10X.

**Señales de identificación**:
- Survey indica "soy empleado", "quiero aprender IA", "estoy comenzando"
- Preguntas en el chat sobre herramientas básicas o "cómo empiezo"
- No iniciaron carrito o iniciaron el de menor precio

**Objetivo del seguimiento**: Nutrir con contenido de valor, hacer la oferta de Ventaja AI, construir confianza para venta futura.

**Secuencia Explorers:**

**Email — Día 1:**
- Asunto: `El primer paso real con IA (no teoría)`
- Contenido: 1 quick win accionable que pueden implementar hoy + link a recurso gratuito + soft CTA: "Si quieres ir más rápido, aquí está Ventaja AI"

**Mensaje WP — Día 2:**
```
Hola [Nombre] 👋

¿Ya intentaste [el quick win del email de ayer]?

Tengo un recurso más que creo que te va a ayudar: [link a cápsula de video o cheat sheet]
```

**Email — Día 4:**
- Asunto: `Lo que separa a quien aprende IA de quien la aplica`
- Contenido: Historia de alguien que pasó de explorador a implementador (caso de éxito de Ventaja AI) + CTA: inscribirse a Ventaja AI o próximo webinar

**Mensaje WP — Día 6:**
```
[Nombre], el próximo webinar es [fecha].

Si quieres llegar ya con una base más sólida, Ventaja AI te prepara antes de eso.

¿Te interesa? [link]
```

---

### 😴 TRACK 3 — NO-SHOW (Registrados que no asistieron)

**Quiénes son**: Se registraron pero no aparecieron en el evento en vivo.

**Objetivo del seguimiento**: Hacer que consuman el replay + re-enganche para próximo webinar o venta directa.

**Secuencia No-Show:**

**Email — Hora 2 post-evento:**
- Asunto: `Te lo perdiste — pero tienes [X horas] para ver el replay`
- Contenido: Link al replay + los 3 puntos más importantes del webinar + urgencia real del replay (disponible solo X horas/días) + CTA: ver replay ahora

**Mensaje WP — Día 1:**
```
[Nombre], no te pudimos ver hoy en el webinar.

El replay está disponible hasta [fecha/hora]: [link]

Vale la pena — Mateo compartió [el insight más potente del webinar en 1 oración].
```

**Email — Día 2 (si no abrió el replay):**
- Asunto: `La parte que más impactó a todos hoy`
- Contenido: El momento más potente del webinar en formato texto (transcripción editada del pitch) + CTA: ver el replay completo o aplicar directamente

**Mensaje WP — Día 3:**
```
[Nombre], última oportunidad para el replay: [link]

Después de [fecha], lo cerramos.

¿Prefieres agendar una llamada directamente? [link al calendario]
```

---

### 📊 TRACK 4 — ASISTIERON PERO NO RESPONDIERON SURVEY

**Quiénes son**: Estuvieron en el evento pero no completaron el formulario de segmentación. No sabemos si son Champions o Explorers.

**Objetivo del seguimiento**: Calificarlos rápido antes de enviarlos al track correcto.

**Secuencia Track 4:**

**Mensaje WP — Hora 1 post-evento:**
```
Hola [Nombre] 👋

Gracias por estar en el webinar de hoy.

Una pregunta rápida: ¿tienes un negocio propio o estás comenzando desde cero?

(Con eso te mando el recurso correcto para tu caso)
```

**Si responde "tengo negocio"** → mover a Track 1 Champions, continuar esa secuencia.
**Si responde "estoy comenzando"** → mover a Track 2 Explorers, continuar esa secuencia.
**Si no responde en 24 horas** → enviar el email de No-Show (Track 3) como fallback.

---

## PRIORIZACIÓN DE SETTERS — WEEKLY ENGAGEMENT SCORE

Cada semana, el equipo de setters necesita saber a quién contactar primero. Genera esta lista con base en señales de comportamiento:

**Señales de alta intención (ordenadas por peso):**
1. Inició carrito y no completó (+10 pts)
2. Vio el pitch completo (+8 pts)
3. Preguntó sobre precio o condiciones en el chat (+7 pts)
4. Abrió el email de follow-up (+5 pts)
5. Hizo click en el link del replay (+4 pts)
6. Respondió el survey con "tengo negocio" (+3 pts)
7. Asistió al webinar completo (retención >80%) (+2 pts)

**Output de la lista de setters:**

| Prioridad | Nombre | Score | Track | Señal principal | Acción recomendada |
|---|---|---|---|---|---|
| 1 | [Nombre] | 18 pts | Champion | Inició carrito + vio pitch | Llamar hoy — preguntar qué frenó la compra |
| 2 | [Nombre] | 15 pts | Champion | Preguntó por precio en chat | WP: enviar condiciones del programa |
| 3 | [Nombre] | 11 pts | Champion | Abrió email 3 veces | WP: oferta de llamada de 15 min |

---

## RECUPERACIÓN DE CARRITOS ABANDONADOS

Para quienes iniciaron el carrito y no completaron — secuencia específica:

**Mensaje WP — Hora 1:**
```
[Nombre], vi que casi completaste tu inscripción.

¿Pasó algo con el proceso de pago o tienes alguna duda sobre el programa?

Te puedo ayudar ahora mismo.
```

**Email — Hora 3:**
- Asunto: `¿Qué pasó, [Nombre]?`
- Contenido: 1 objeción principal resuelta (la más común: "es mucho dinero" o "no tengo tiempo") + testimonio específico + link directo al carrito donde lo dejó

**Mensaje WP — Día 1:**
```
[Nombre], el precio del programa sube [fecha/si aplica].

Si tienes alguna duda antes de decidir, Mateo tiene [X] espacios esta semana para una llamada de 15 min.

¿Quieres uno? [link]
```

---

## GENERACIÓN RÁPIDA DE CONTENIDO POST-EVENTO

Al terminar cada webinar, generar estos 3 assets de inmediato:

1. **Email Day 0** para cada track (4 emails distintos) — listo para enviar en la primera hora
2. **Mensajes WP** de las primeras 24 horas para cada track
3. **Lista de prioridad de setters** con scoring basado en comportamiento del chat y survey

**Input requerido para generarlos:**
- Tema central del webinar
- El insight más potente del pitch (1 frase)
- Resultados del survey (cuántos champions vs explorers)
- Lista de carritos abandonados
- Lista de no-shows

---

## [VERSIONING LOG]

`v1.0 — 2026-03-19 — Post-Webinar Follow-Up System. 4 tracks: Champions / Explorers / No-Show / No-Survey. Programas: Samurai 8 AI, Ventaja AI, Ventas 10X. Basado en estrategia del equipo Mateo Folador, Marzo 2026.`
