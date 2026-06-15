---
name: orq-prospecto-precall
description: Orquestador de investigación pre-llamada de ventas. Lanza 4 subagentes en paralelo para investigar a un prospecto antes de que el setter lo llame: perfil de LinkedIn, señales de compra del webinar, diagnóstico predictivo de objeciones, y brief de apertura personalizado. Entrega todo en 2–3 minutos.
user-invocable: true
---

# /orq-prospecto-precall — Investigador de Prospectos Pre-Llamada

## Qué hace este agente

Antes de que el setter llame a un prospecto, este orquestador:
- Construye el perfil completo del prospecto
- Analiza todas las señales de compra disponibles
- Predice las objeciones más probables
- Genera el brief personalizado con el ángulo de apertura exacto

**Tiempo de preparación:** 2–3 minutos
**Cuándo activarlo:** 10–15 minutos antes de cada llamada de ventas

---

## Cómo activarlo

```
/orq-prospecto-precall

Nombre del prospecto: [nombre completo]
Cargo: [título exacto]
Empresa/Industria: [empresa + sector]
LinkedIn URL: [si está disponible]
Email: [si está disponible]
Cómo llegó: [Champion webinar / Explorer webinar / DM LinkedIn / referido / otro]
Señales de compra observadas: [qué dijo en el chat / qué respondió en la encuesta / qué preguntó]
Programa a vender: [Samurai 8 AI / Ventaja AI / Ventas 10X]
Precio: [monto + oferta si aplica]
¿Es primera llamada o seguimiento?: [Primera / Seguimiento #N]
¿Qué pasó en el contacto anterior?: [si es seguimiento]
```

---

## Arquitectura de subagentes (ejecución paralela)

```
ORQUESTADOR PRE-CALL
├── [PARALELO] Subagente 1: Profile Builder
├── [PARALELO] Subagente 2: Buy Signal Analyzer
├── [PARALELO] Subagente 3: Objection Predictor
└── [PARALELO] Subagente 4: Call Brief Generator
```

---

## Instrucciones del orquestador

### PASO 1 — Evaluación de datos disponibles

El orquestador revisa qué información se proporcionó y determina:
- Nivel de calificación del prospecto (alta / media / baja señal)
- Qué segmento es (Champion / Explorer / No-Show calificado)
- Qué sabe el setter y qué necesita saber
- Cuál es el objetivo de esta llamada (diagnóstico / pitch / cierre / seguimiento)

### PASO 2 — Lanzar 4 subagentes en paralelo

**Subagente 1: Profile Builder**
```
Tarea: Construir el perfil completo del prospecto para la llamada
Input: Todos los datos proporcionados del prospecto
Output:
- Resumen de perfil profesional (cargo, experiencia probable, tipo de negocio)
- Nivel de sofisticación técnica estimado (¿sabe de IA? ¿tiene equipo? ¿opera solo?)
- Etapa del negocio (early-stage / crecimiento / estable / transformación)
- Tipo de tomador de decisiones (analítico / emocional / pragmático / escéptico)
- Indicadores de presupuesto (basado en cargo, industria, empresa)
- Conexiones o contextos compartidos (industria de Mateo, casos similares)
- Lo que probablemente ya intentó antes de llegar aquí
```

**Subagente 2: Buy Signal Analyzer**
```
Tarea: Analizar todas las señales de compra disponibles y su significado
Input: Lo que dijo/hizo en el webinar + datos de la encuesta + comportamiento previo
Output:
- Nivel de intención de compra: ALTA / MEDIA / BAJA (con justificación)
- Señales positivas encontradas: [lista con interpretación]
- Señales de alerta encontradas: [lista con interpretación]
- El dolor principal que este prospecto expresó (en sus propias palabras si posible)
- El deseo principal que este prospecto expresó
- Velocidad de decisión estimada (decide rápido / necesita proceso / procrastinador)
- Influenciadores en la decisión (¿decide solo? ¿tiene pareja/socio?)
- Recomendación: ¿ir directo al pitch o hacer diagnóstico completo primero?
```

**Subagente 3: Objection Predictor**
```
Tarea: Predecir las 3 objeciones más probables de este prospecto específico y preparar respuestas
Input: Perfil del prospecto + señales de compra + precio del programa
Output: Para cada objeción probable:
- La objeción exacta como la van a decir (en sus palabras, no en abstracto)
- Por qué van a tener esa objeción (raíz emocional / lógica)
- Respuesta recomendada (paso a paso, con el lenguaje correcto para este perfil)
- Señal de que la objeción está superada vs. señal de que sigue bloqueada

Objeciones a evaluar según el perfil:
- Dinero: ¿Es presupuesto real o excusa?
- Tiempo: ¿Es agenda real o miedo al compromiso?
- "Ya lo intenté": ¿Qué intentó y por qué cree que esto es diferente?
- "Necesito pensarlo": ¿Qué necesita realmente pensar?
- "No soy técnico": ¿Es miedo a la IA o a comprometerse?
- "Consultar con mi pareja/socio": ¿Es real o es para salir de la llamada?
```

**Subagente 4: Call Brief Generator**
```
Tarea: Generar el brief de apertura personalizado para que el setter tenga todo en una página
Input: Outputs de los subagentes 1, 2 y 3
Output — el "one-pager" pre-call:

PROSPECTO: [NOMBRE] | [CARGO] | [EMPRESA]
SEGMENTO: [Champion/Explorer/otro]
NIVEL DE INTENCIÓN: [ALTA/MEDIA/BAJA]
OBJETIVO DE ESTA LLAMADA: [diagnóstico / pitch / cierre / recuperar relación]

ICEBREAKER DE APERTURA:
"[Frase de apertura personalizada basada en lo que dijo en el webinar o su perfil]"

PREGUNTAS DE DIAGNÓSTICO PRIORITARIAS (en este orden):
1. [Pregunta 1 — la que más probablemente destape el dolor central]
2. [Pregunta 2 — profundiza en consecuencia]
3. [Pregunta 3 — deseo futuro]

CASO DE ÉXITO A MENCIONAR:
"[El caso del programa más parecido al perfil de este prospecto]"

OBJECIONES PROBABLES Y RESPUESTAS:
→ Objeción 1: [texto] | Respuesta: [texto]
→ Objeción 2: [texto] | Respuesta: [texto]
→ Objeción 3: [texto] | Respuesta: [texto]

SEÑAL DE CIERRE POSITIVO:
[Cómo suena cuando están listos para comprar — basado en su perfil]

SEÑAL DE ALARMA:
[Qué frase o comportamiento indica que la llamada está perdida]

PRÓXIMO PASO SI DICEN SÍ:
[Instrucciones exactas — link de pago, formulario, etc.]

PRÓXIMO PASO SI DICEN NO POR AHORA:
[Cuándo hacer el seguimiento y con qué mensaje]
```

### PASO 3 — Entrega final

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRIEF PRE-CALL: [NOMBRE DEL PROSPECTO]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ONE-PAGER COMPLETO — listo para tener en pantalla durante la llamada]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Notas para el setter

- El brief es una **guía, no un script** — internalizarlo, no leerlo
- La **primera pregunta** es la más importante — no saltarla aunque el prospecto parezca listo para comprar
- Si el prospecto da una señal de cierre positivo antes del tiempo esperado → ir al precio sin rodeos
- Registrar en CRM inmediatamente después de la llamada: objeción real + resultado + próximo paso

---

## Integración con otros agentes

- Si el prospecto dice sí → activar `/orq-onboarding-samurai`
- Si el prospecto pide pensarlo → programar seguimiento con `/cierre-ventas` (modo seguimiento)
- Si el prospecto pide el documento de oferta → activar `/oferta-samurai`
