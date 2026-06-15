---
name: orq-onboarding-samurai
description: Orquestador de onboarding para nuevos clientes de Samurai 8 AI / Ventaja AI. Lanza 4 subagentes en paralelo: bienvenida personalizada, diagnóstico inicial del negocio del cliente, plan de 90 días personalizado, y configuración del ecosistema de herramientas. Activa el sistema completo de onboarding en una sola ejecución.
user-invocable: true
---

# /orq-onboarding-samurai — Orquestador de Onboarding

## Qué hace este agente

Cuando un nuevo cliente paga e ingresa a Samurai 8 AI (o Ventaja AI), este orquestador activa simultáneamente todo el sistema de onboarding:
- Bienvenida personalizada (email + WhatsApp + Notion/ClickUp)
- Diagnóstico inicial del negocio del cliente
- Plan de 90 días personalizado según su situación
- Configuración del stack de herramientas que van a usar

**Cuándo activarlo:** Inmediatamente después de confirmar el pago.

---

## Cómo activarlo

```
/orq-onboarding-samurai

Nombre del cliente: [nombre completo]
Programa: [Samurai 8 AI / Ventaja AI / Ventas 10X]
Fecha de inicio: [fecha]
Cargo/Industria: [cargo + sector]
Negocio: [qué vende, a quién, cómo]
Tamaño del equipo: [solo / 2–5 personas / 6+]
Situación actual: [resumen del diagnóstico de la llamada de ventas]
Objetivo principal declarado: [lo que dijo querer lograr]
Herramientas que ya usa: [lista]
Nivel técnico: [principiante / intermedio / avanzado]
¿Tiene equipo de apoyo?: [Sí + quién / No]
Precio pagado: [monto]
¿Hay sesión de kick-off agendada?: [Sí - fecha / No]
```

---

## Arquitectura de subagentes (ejecución paralela)

```
ORQUESTADOR ONBOARDING
├── [PARALELO] Subagente 1: Welcome Package Creator
├── [PARALELO] Subagente 2: Business Diagnostic Analyst
├── [PARALELO] Subagente 3: 90-Day Plan Generator
└── [PARALELO] Subagente 4: Tool Stack Configurator
```

---

## Instrucciones del orquestador

### PASO 1 — Análisis de contexto inicial

El orquestador procesa los datos del nuevo cliente y determina:
- Su perfil de aprendizaje (técnico vs. estratégico vs. ejecutor)
- El módulo del programa donde más valor va a obtener primero
- Las herramientas prioritarias según su negocio
- El riesgo de abandono (clientes con poca claridad o equipo muy pequeño necesitan más acompañamiento)

### PASO 2 — Lanzar 4 subagentes en paralelo

**Subagente 1: Welcome Package Creator**
```
Tarea: Generar todos los materiales de bienvenida del nuevo cliente
Input: Todos los datos del cliente
Output:

EMAIL DE BIENVENIDA:
- Asunto: Bienvenido a [PROGRAMA], [NOMBRE] — esto es lo que pasa ahora
- Cuerpo: Celebración del paso dado + qué esperar en las primeras 48h + recursos de acceso
- Tono: Cálido, directo, concreto. Sin frases de motivador.

MENSAJE DE WHATSAPP (primer contacto):
- Mensaje corto (máx 5 líneas)
- Confirmación de acceso + próximo paso concreto
- Número/canal de soporte

MENSAJE DE GRUPO (si entra a un grupo de la comunidad del programa):
- Presentación breve del nuevo cliente para que el grupo lo reciba
- Template para que el cliente mismo se presente

CHECKLIST DE PRIMER DÍA (para el cliente):
- 5 acciones concretas a completar en las primeras 24 horas
- Recursos específicos a revisar primero
- Qué NO hacer todavía (evitar el error de querer implementar todo a la vez)

TAREA DE KICK-OFF:
- Si hay sesión agendada: agenda + preguntas a preparar
- Si no hay sesión: instrucciones de auto-diagnóstico para el primer módulo
```

**Subagente 2: Business Diagnostic Analyst**
```
Tarea: Construir el diagnóstico inicial del negocio del cliente para personalizar el programa
Input: Situación actual + objetivo + industria + herramientas actuales
Output:
- Mapa de situación actual: qué tiene, qué le falta, qué está roto
- Los 3 bottlenecks principales identificados (en orden de impacto)
- Quick wins disponibles (qué puede implementar en las primeras 2 semanas para ver resultado rápido)
- Riesgos y alertas (qué podría frenar su progreso si no se atiende)
- Nivel de madurez digital del negocio (escala 1–5 con descripción)
- Módulos del programa en orden de prioridad para este cliente específico
  (no todos empiezan por el módulo 1 — el orden debe ser personalizado)
```

**Subagente 3: 90-Day Plan Generator**
```
Tarea: Crear el plan personalizado de 90 días para este cliente
Input: Diagnóstico del Subagente 2 + objetivo declarado + programa
Output:

MES 1 (Días 1–30): FUNDAMENTOS Y QUICK WIN
- Semana 1: [Módulo + entregable concreto]
- Semana 2: [Módulo + entregable concreto]
- Semana 3: [Módulo + entregable concreto]
- Semana 4: [Módulo + entregable concreto + primer milestone]
- Milestone del mes: [resultado medible esperado]

MES 2 (Días 31–60): IMPLEMENTACIÓN CORE
- Semana 5–8: [Módulos + entregables]
- Milestone del mes: [resultado medible esperado]

MES 3 (Días 61–90): OPTIMIZACIÓN Y ESCALA
- Semana 9–12: [Módulos + entregables]
- Milestone del mes: [resultado medible esperado = la promesa central del programa]

MÉTRICA DE ÉXITO (cómo saber que el programa funcionó):
[Resultado concreto y medible que define éxito para este cliente]

CHECK-INS RECOMENDADOS:
- Check-in semana 2: [qué revisar]
- Check-in semana 4: [qué revisar — debe tener el quick win]
- Check-in semana 8: [qué revisar]
- Sesión de cierre semana 12: [evaluación final]
```

**Subagente 4: Tool Stack Configurator**
```
Tarea: Definir el stack de herramientas exacto para este cliente y el orden de configuración
Input: Herramientas actuales + nivel técnico + tamaño de equipo + tipo de negocio
Output:

STACK RECOMENDADO (priorizado):
Herramienta 1: [nombre] — Por qué + cómo configurarla primero
Herramienta 2: [nombre] — Por qué + cuándo agregarla
Herramienta 3: [nombre] — Por qué + en qué fase del programa
(máximo 5–7 herramientas — evitar el síndrome de "instalar todo y no usar nada")

HERRAMIENTAS A MANTENER DE LAS QUE YA USA:
[Las que tienen en su stack actual y son compatibles]

HERRAMIENTAS A REEMPLAZAR O ELIMINAR:
[Las que están creando fricción o son redundantes]

INTEGRACIONES CLAVE:
[Qué conectar con qué y por qué]

GUÍA DE CONFIGURACIÓN PASO A PASO (semana 1):
[Instrucciones específicas para las primeras 3 herramientas]
```

### PASO 3 — Entrega final del orquestador

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ONBOARDING: [NOMBRE] — [PROGRAMA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📬 MATERIALES DE BIENVENIDA
[Email listo para enviar]
[Mensaje WhatsApp listo]
[Mensaje de presentación para el grupo]
[Checklist de primer día del cliente]

🔍 DIAGNÓSTICO INICIAL
[Mapa de situación + bottlenecks + quick wins + riesgos]

📅 PLAN DE 90 DÍAS
[Tabla semana a semana con módulos, entregables y milestones]

🛠️ STACK DE HERRAMIENTAS
[Lista priorizada + guía de configuración semana 1]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Integración con otros agentes

- Si el cliente tiene un resultado notable en semana 4 → activar `/caso-de-exito`
- Si el cliente termina el programa → activar flujo de testimonial (Make.com automation)
- Si el cliente tiene problemas de implementación → usar `/automatizacion-make` para diseñar su flujo específico
