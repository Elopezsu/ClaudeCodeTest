---
name: automatizacion-make
description: Diseña blueprints de automatización para Make.com o n8n orientados al ecosistema de Mateo Folador / Samurai 8 AI. Genera el mapa lógico del flujo, los módulos necesarios, y el pseudocódigo de configuración.
user-invocable: true
---

# /automatizacion-make — Diseñador de Blueprint de Automatización

## Qué hace este skill

Diseña blueprints de automatización completos para Make.com (Integromat) o n8n:

- Mapa visual del flujo (en texto/ASCII para revisar antes de construir)
- Lista de módulos/nodos necesarios con configuración
- Condiciones lógicas y filtros
- Manejo de errores
- Estimado de operaciones/mes
- Instrucciones paso a paso para construirlo

---

## Cómo activarlo

Escribe `/automatizacion-make` y proporciona:

```
Plataforma: [Make.com / n8n / cualquiera]
¿Qué proceso quieres automatizar?: [descripción en lenguaje natural]
Trigger (qué lo dispara): [ej. "cuando llega un nuevo registro en Airtable"]
Resultado final deseado: [ej. "mandar email personalizado + agregar a CRM"]
Herramientas involucradas: [lista las apps que ya usas]
Volumen estimado: [ej. "~200 triggers por semana"]
¿Tienes acceso API a todas las herramientas?: [Sí / No / No sé]
```

---

## Automatizaciones más comunes del ecosistema Mateo Folador

### 1. Post-Webinar Segmentation Flow
**Trigger:** Nueva respuesta en encuesta post-webinar (Typeform / Google Forms)
**Acción:** Clasificar en Champions / Explorers / No-Survey y mover a lista correcta en CRM + notificar al setter

### 2. WhatsApp Community Welcome Flow
**Trigger:** Nuevo miembro unido al grupo de WhatsApp (via WATI / Manychat)
**Acción:** Enviar mensaje de bienvenida personalizado + agregar a base de datos + asignar tag de semana

### 3. Lead Magnet → CRM → Nurture
**Trigger:** Descarga de lead magnet (Kajabi / Systeme.io / landing page)
**Acción:** Agregar a lista de email + iniciar secuencia de nurture + notificar al equipo si el lead tiene perfil alto

### 4. Setter Notification Flow
**Trigger:** Prospecto calificado (Champion) identificado post-webinar
**Acción:** Notificar al setter por WhatsApp/Slack con info del prospecto + agregar recordatorio en calendario + template de primer mensaje

### 5. Testimonial Collection Flow
**Trigger:** Cliente completa el programa (marca como completado en CRM)
**Acción:** Enviar email de felicitación + link a formulario de testimonial + agendar llamada de caso de éxito

### 6. Content Repurposing Notification
**Trigger:** Mateo publica un post nuevo en LinkedIn (via RSS o Zapier)
**Acción:** Notificar al equipo de contenido + crear tarea en Notion/ClickUp + guardar en biblioteca de contenido

### 7. Payment Failed → Recovery
**Trigger:** Pago fallido en Stripe/PayPal
**Acción:** Email automático de recuperación + notificación al setter + pausa de acceso si es necesario

---

## Estructura del blueprint (formato de salida)

### SECCIÓN 1: Diagrama del flujo

```
[TRIGGER]
    ↓
[PASO 1: Acción/Módulo]
    ↓
[CONDICIÓN/FILTRO] → SI NO → [RAMA B]
    ↓ SI
[PASO 2: Acción/Módulo]
    ↓
[PASO 3: Acción/Módulo]
    ↓
[RESULTADO FINAL]
```

### SECCIÓN 2: Módulos detallados

Para cada nodo en el flujo:

```
Módulo: [NOMBRE DEL MÓDULO]
App: [Make.com app / n8n node]
Tipo: Trigger / Action / Filter / Router / Error Handler
Configuración:
  - Campo 1: [valor o variable dinámica]
  - Campo 2: [valor o variable dinámica]
  - Filtros: [condición lógica]
Datos de salida: [qué variables genera este módulo]
```

### SECCIÓN 3: Lógica de condiciones

Todas las ramificaciones del flujo con sus condiciones exactas.

**Ejemplo:**
```
Router principal:
  ├── Rama A: Si [encuesta.score] >= 8 → Champions flow
  ├── Rama B: Si [encuesta.score] >= 5 → Explorers flow
  ├── Rama C: Si [encuesta.score] < 5 → No-priority flow
  └── Rama D: Si [encuesta] no existe → No-Survey flow
```

### SECCIÓN 4: Variables y mapeo de datos

Lista de todas las variables que fluyen entre módulos:
```
{{nombre}} — del módulo X, usado en módulos Y, Z
{{email}} — del módulo X, usado en módulos Y, Z
{{segmento}} — generado en módulo Router, usado en módulos Y, Z
```

### SECCIÓN 5: Manejo de errores

- ¿Qué pasa si una app no responde?
- ¿Qué pasa si los datos llegan incompletos?
- ¿Cómo notificar errores críticos?
- Recomendación de reintentos y timeouts

### SECCIÓN 6: Estimado de operaciones

```
Volumen: [X triggers/mes]
Módulos por ejecución: [Y módulos]
Operaciones totales: [X × Y = Z operaciones/mes]
Plan de Make.com recomendado: [plan según operaciones]
Costo estimado: [$/mes]
```

---

## Instrucciones de construcción (paso a paso)

El skill genera instrucciones específicas para construir el flujo desde cero:

```
Paso 1: En Make.com, crear nuevo escenario
Paso 2: Agregar módulo [APP] → [TIPO DE TRIGGER]
  - Conectar con cuenta de [APP]
  - Configurar: [campos específicos]
Paso 3: Agregar módulo [APP] → [TIPO DE ACCIÓN]
  - Mapear: {{campo}} de módulo anterior → campo destino
  - Configurar filtros: [condición específica]
...
```

---

## Templates disponibles

Al ejecutar `/automatizacion-make templates`, muestra lista de blueprints pre-diseñados listos para adaptar:

1. **post-webinar-segmentation** — Clasificación automática post-webinar
2. **whatsapp-welcome** — Bienvenida automática a nuevos miembros
3. **lead-to-crm** — Lead magnet → CRM → nurture sequence
4. **setter-notification** — Alerta al setter con info del prospecto
5. **testimonial-request** — Solicitud automática post-completar programa
6. **payment-recovery** — Recuperación de pagos fallidos
7. **content-library** — Guardar automáticamente contenido publicado

---

## Herramientas del ecosistema Mateo (integradas frecuentemente)

| Herramienta | Uso | Integración Make.com |
|---|---|---|
| Airtable | CRM / base de datos | ✅ Módulo nativo |
| Typeform | Encuestas post-webinar | ✅ Módulo nativo |
| WATI / Manychat | WhatsApp automations | ✅ Módulo nativo / Webhook |
| Kajabi / Systeme.io | Plataforma de cursos | ✅ Webhook |
| Stripe | Pagos | ✅ Módulo nativo |
| Notion / ClickUp | Gestión de tareas | ✅ Módulo nativo |
| Gmail / Brevo | Email | ✅ Módulo nativo |
| Slack | Notificaciones internas | ✅ Módulo nativo |
| Zoom / StreamYard | Webinars | ✅ Webhook |
| Claude API | Clasificación y generación de texto con IA | ✅ HTTP Module |

---

## Output del skill

Al ejecutar `/automatizacion-make`, Claude entrega:

1. **Diagrama del flujo** (texto/ASCII + descripción en prosa)
2. **Configuración de cada módulo** (lista detallada)
3. **Lógica de condiciones** (todas las ramificaciones)
4. **Mapeo de variables** (de dónde viene cada dato)
5. **Manejo de errores** (qué hacer cuando algo falla)
6. **Estimado de operaciones/mes**
7. **Instrucciones de construcción paso a paso**
8. **Checklist de pruebas** antes de activar el escenario

---

## Principios de automatización bien diseñada

- **Una sola fuente de verdad:** Todos los datos viven en el CRM (Airtable). Las automatizaciones actualizan ahí, no en islas.
- **Idempotente:** Ejecutar el flujo dos veces con los mismos datos no debe crear duplicados ni errores.
- **Alertas de error visibles:** Si algo falla, alguien debe saberlo en < 5 min.
- **Documentación inline:** Cada módulo tiene nombre descriptivo (no "Module 7").
- **Prueba antes de activar:** Siempre testear con datos reales en modo test antes de activar en producción.
