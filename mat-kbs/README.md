# MAT — Bases de Conocimiento del Sistema de Agentes

Este repositorio contiene las bases de conocimiento (KBs) que alimentan el sistema de agentes IA de MAT.

## Cómo usar

Para construir una nueva KB, abre Claude Code y ejecuta:

```
/mat:construye-kb
```

El agente te guiará paso a paso. Al final guarda el archivo `.md` en la carpeta correspondiente.

## Estructura de carpetas

```
mat-kbs/
├── paid-media/       → Estrategias Meta/Google/TikTok Ads, patrones ganadores
├── embudos/          → TOFU, MOFU, BOFU, frameworks de conversión
├── copywriting/      → Principios de copy, estructuras, niveles de consciencia
├── contenido/        → Parrillas, narrativa, formatos, plataformas
├── ventas/           → Cierre, objeciones, WhatsApp, canales directos
├── video/            → Guiones, hooks visuales, retención, reels/TikTok
└── juan-pablo/       → Metodología propia MAT, casos de éxito
```

## Formato de archivos

Cada KB sigue esta estructura:

```markdown
# [Nombre] — MAT Knowledge Base

> Categoría: ...
> Fuente: ...
> Fecha: ...
> Conectar a: [agente]

## Principios Fundamentales
## Metodología / Proceso
## Reglas No Negociables
## Casos de Aplicación
## Frases y Conceptos Clave
## Errores Comunes a Evitar
## Aplicación en MAT
```

## Referentes por categoría

### Paid Media
Jon Loomer · Depesh Mandalia · Ralph Burns · Billy Gene · Aaron Young · Brett Curry

### Contenido & Social Media
Gary Vaynerchuk · Alex Hormozi · Manuela Villegas · Vilma Núñez · Aleyda Solis

### Embudos de Ventas
Russell Brunson · Alex Hormozi · Ryan Deiss · Todd Brown · Frank Kern · Sam Ovens

### Copywriting
David Ogilvy · Eugene Schwartz · Gary Halbert · Dan Kennedy · Maïder Tomasena

### Ventas & Conversión
Alex Hormozi · Jordan Belfort · Grant Cardone · Jeb Blount · Chet Holmes

### Video & Guiones
Mr. Beast · Peter McKinnon · Think Media · Natalia Zuluaga · Luisa Fernanda W

### Email + WhatsApp
Andre Chaperon · Ben Settle · Ryan Levesque · Wati Blog

## Agentes que usan estas KBs

| Tier | Agente | KBs que consume |
|------|--------|----------------|
| 1 | Orquestador de Contenido | juan-pablo + contenido |
| 1 | Agente Parrilla | contenido + juan-pablo |
| 1 | Copy Calentamiento | copywriting + ventas |
| 2 | Intel Competitiva | paid-media |
| 2 | Extractor de Patrones | paid-media + juan-pablo |
| 2 | Estratega MAT | todos |
| 3 | TOFU | contenido + copywriting + video |
| 3 | MOFU | ventas + copywriting + embudos |
| 3 | BOFU | ventas + copywriting + embudos |
| 3 | Guionista TOFU | video + contenido |
| 3 | Guionista MOFU | video + ventas |
| 3 | Guionista BOFU | video + ventas + copywriting |
| 4 | Onboarding | juan-pablo + todos |
