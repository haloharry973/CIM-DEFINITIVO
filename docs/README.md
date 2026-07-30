# Centro de documentación CIM — Versión limpia 2026-07-30

<p align="center">
  <img src="assets/ubb_logo.png" alt="Universidad del Bío-Bío" width="280">
</p>

Documentación activa, sin duplicados, orientada a **presentar** y a **mejorar**.

## 🎯 Para presentar (evaluación)

1. **Entrega final (2 PDFs):** `../entrega/` — `INFORME_PRACTICA_II_CIM_DEFINITIVO.pdf` + `MANUAL_TUTORIAL_CIM_DEFINITIVO.pdf`
2. **Fuente y generador:** `project/` — `GENERADOR_PRACTICA_II.py` (reportlab) + `DOCUMENTACION_SISTEMA_CIM.md`
3. **Evidencias:** `deliverables/` — Bitácora, Quality Gates, Manual Operativo, Protocolo

Orden de lectura recomendado:
1. `INDEX_REPOSITORIO.md` — mapa
2. `INSTRUCTIVO_USO_PROYECTO.md` — cómo compilar/instalar
3. `VALIDACION_Y_COBERTURA.md` — qué valida CI y qué no
4. `project/DOCUMENTACION_SISTEMA_CIM.md` — arquitectura
5. `deliverables/INFORME_PRACTICA_II_CIM_DEFINITIVO.pdf` — informe académico
6. `deliverables/MANUAL_TUTORIAL_CIM_DEFINITIVO.pdf` — tutorial

## 🛠️ Para mejorar (desarrollo continuo)

| Necesidad | Ubicación |
|---|---|
| Compilar Android | `../config/` + `../android/` |
| Firmware canónico | `../esp32/firmware/` |
| Validadores 12/12 | `../tools/validate_system_100.py` |
| Simulación hub/visión | `../tools/hub_simulator.py`, `vision_safety_simulator.py` |
| Seguridad | `safety/SAFETY_ASSURANCE_ARCHITECTURE.md` |
| Visión / dataset | `vision/DATASET_CAPTURE_AND_LABELING.md` |
| Quickstart | `quickstart/README.md` |
| Auditoría | `audits/AUDITORIA_TECNICA_2026-07-28.md` |

**Qué NO usar:**
- `../archive/` — histórico, no operativo
- `../assets/` en raíz — eliminado (ahora todo en `assets/imagenes/`)
- PDFs antiguos `ENTREGA_FINAL...` — movidos a `../archive/historico-entrega/`

## 📁 Estructura vigente

```
docs/
├── README.md (este)
├── INDEX_REPOSITORIO.md
├── INSTRUCTIVO_USO_PROYECTO.md
├── VALIDACION_Y_COBERTURA.md
├── assets/
│   ├── ubb_logo.png
│   ├── imagenes/ (cim_arquitectura_v6.png, ui_*.png, esp32_wokwi...)
│   └── diagramas/.gitkeep
├── deliverables/ (solo final + esenciales, sin duplicados)
│   ├── INFORME_PRACTICA_II_CIM_DEFINITIVO.pdf
│   ├── MANUAL_TUTORIAL_CIM_DEFINITIVO.pdf
│   ├── BITACORA_VALIDACION.md
│   ├── QUALITY_GATES.md
│   ├── MANUAL_OPERATIVO_LABORATORIO.md
│   ├── PROTOCOLO_PRUEBAS_HARDWARE.md
│   └── ...
├── project/
│   ├── DOCUMENTACION_SISTEMA_CIM.md
│   ├── GENERADOR_PRACTICA_II.py
│   ├── INFORME_PRACTICA_II_...pdf
│   └── MANUAL_TUTORIAL_...pdf
├── safety/, vision/, quickstart/, audits/
└── styles/industrial_pdf.css
```

**Limpieza 2026-07-30:** se eliminaron `docs/images/` duplicado, `docs/*.mjs`, `package*.json`, `entrega/informes/`, `assets/models/bestMH.pt` (19MB, debe gestionarse aparte), `Template.rar`, `.fastRequest/`. Todo movido o borrado está trazado en `archive/historico-entrega/` o git history.
