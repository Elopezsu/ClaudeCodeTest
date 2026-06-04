# Pipeline AI para UFBA — Terminar la Carrera en 3 Años

**Objetivo:** Usar AI + conocimientos adquiridos en viajes para terminar la carrera en UFBA en 3 años en lugar de 4.  
**Meta de graduación:** 2031 (si entra enero 2028)  
**Estado:** Investigado 2026-06-04, pendiente de ejecutar al inicio de la universidad.

---

## Pipeline diseñado

```
PLAUD NotePin (graba clase con aislamiento de ruido)
       ↓
Sincroniza con app → exporta transcripción
       ↓
Make.com (automation ya disponible)
       ↓
Google Drive (carpeta /clases-ufba/fecha)
       ↓
Google Drive MCP → Claude
       ↓
Extrae lo relevante + ayuda con tareas y trabajos
```

---

## Comparativa de dispositivos — investigación 2026-06-04

| Dispositivo | Aislamiento ruido | Capacidad | Precio hardware | Suscripción |
|------------|------------------|-----------|----------------|-------------|
| **PLAUD NotePin** ✅ | ★★★★★ Micrófonos Knowles + beamforming | 64–128 GB local (1,000 hrs) | $159–189 | $99/año o 300 min/mes gratis |
| Limitless Pendant | ★★★★ | Solo nube | $99–199 | $19/mes |
| Bee AI | ★★★ | Solo nube | $49.99 | $19/mes obligatorio |
| Granola.so | ★★★ (Mac nativo) | Nube | Gratis | Plan gratis disponible |

**PLAUD NotePin elegido porque:**
- Mejor aislamiento de ruido para aulas — beamforming enfoca en la voz, cancela murmullo del aula
- 64–128 GB de almacenamiento LOCAL — no depende de WiFi en clase
- Plan gratuito incluye 300 min/mes de transcripción con GPT + Claude
- Formato de solapa — discreto en clase
- Transcribe bien en portugués

**Estrategia de inicio:** Probar primero Granola.so gratis (Mac nativo) las primeras 2 semanas. Si la transcripción en portugués es buena, puede ser suficiente sin comprar hardware. Si no, comprar PLAUD NotePin ($159).

---

## Por qué 3 años es alcanzable

| Factor | Ganancia estimada |
|--------|-----------------|
| AI para síntesis de clases | Reduce tiempo de estudio por examen ~30–40% |
| AI para tareas y trabajos | Estructura argumentos con fuentes exactas del profesor |
| Portugués ya dominado al llegar | No pierde el primer año de adaptación al idioma |
| Conocimiento previo de viajes | Historia y Ciencias Sociales = contexto real, no abstracto |
| Empezar TCC al final del año 3 | Termina en el verano en lugar de usar todo el año 4 |

El cuarto año en Brasil generalmente se usa solo en pasantías + Trabalho de Conclusão de Curso (TCC). Con AI ese tiempo se comprime significativamente.

---

## Infraestructura disponible (ya lista)

- **Make.com:** cuenta activa con escenarios (ValuSignal)
- **Google Drive MCP:** configurado en Claude Code
- **Claude Code:** disponible
- **Mac:** plataforma ideal para Granola (plan B)

---

## Pasos para ejecutar al llegar a UFBA (enero 2028)

1. Primeras 2 semanas: probar Granola.so gratis para validar calidad de transcripción en portugués
2. Si Granola no es suficiente: comprar PLAUD NotePin (~$159)
3. Crear carpeta `/clases-ufba/` en Google Drive
4. Construir escenario Make: exportar transcripción → carpeta Drive automáticamente
5. Configurar MCP Drive apuntando a esa carpeta
6. Usar Claude para extraer puntos clave antes de cada examen y estructurar trabajos
