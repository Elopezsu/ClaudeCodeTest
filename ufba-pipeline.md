# Pipeline AI para UFBA — Terminar la Carrera Rápido

**Objetivo:** Usar AI + conocimientos adquiridos en viajes para terminar la carrera en UFBA lo más rápido posible.  
**Estado:** Diseñado 2026-06-04. Ejecutar cuando empiece la universidad.

---

## Pipeline

```
Granola.so (graba + transcribe clase en Mac)
       ↓
Exportar nota como Markdown
       ↓
Make.com (automation ya disponible)
       ↓
Google Drive (carpeta /clases-ufba/fecha)
       ↓
Google Drive MCP → Claude
       ↓
Extrae lo relevante + ayuda con tareas
```

---

## Hardware y setup

| Componente | Decisión | Razón |
|-----------|----------|-------|
| Laptop | Mac (ya tiene) | Granola es app nativa Mac — mejor integración |
| App de grabación | Granola.so modo "in-person" | Exporta Markdown, soporta portugués (Whisper), integra con Claude |
| Micrófono | AirPods conectados al Mac | Captan mejor que el mic integrado del laptop |
| Posición en clase | Primera o segunda fila | Buena calidad de audio para el mic |
| Hardware adicional | PLAUD Note descartado por ahora | Validar primero con Granola antes de gastar $170 |

---

## Infraestructura disponible (ya lista)

- **Make.com:** cuenta activa con escenarios (ValuSignal)
- **Google Drive MCP:** configurado en Claude Code
- **Claude Code:** disponible

---

## Pasos para ejecutar (cuando empiece UFBA)

1. Instalar Granola.so en el Mac
2. Primeras 2 semanas: validar calidad de transcripción en portugués
3. Crear carpeta `/clases-ufba/` en Google Drive
4. Construir escenario Make: watcher de carpeta → subir a Drive
5. Conectar MCP Drive a la carpeta correcta
6. Probar el pipeline completo con una clase real

---

## Notas del diseño

- Granola está optimizado para videollamadas pero funciona en modo in-person
- En Mac, los AirPods como micrófono mejoran significativamente la captura de audio
- Make.com ya conocemos el stack — costo marginal casi cero para construir el escenario
- El MCP de Google Drive ya está configurado en este entorno
