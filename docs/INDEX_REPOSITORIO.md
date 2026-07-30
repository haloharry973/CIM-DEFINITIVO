# Índice del repositorio CIM — Limpio 2026-07-30

## 🎯 Para presentar

| Ubicación | Qué es | Estado |
|---|---|---|
| `../entrega/INFORME_PRACTICA_II_CIM_DEFINITIVO.pdf` | Informe académico UBB Práctica II (5.2 MB) | **Final** |
| `../entrega/MANUAL_TUTORIAL_CIM_DEFINITIVO.pdf` | Manual tutorial paso a paso (5.9 MB) | **Final** |
| `project/INFORME_PRACTICA_II_...pdf` | Mismo informe con nombre completo Leonardo Araya | Final |
| `project/MANUAL_TUTORIAL_...pdf` | Mismo manual con nombre completo | Final |
| `project/GENERADOR_PRACTICA_II.py` | Generador reportlab reproducible | Activo |
| `project/DOCUMENTACION_SISTEMA_CIM.md` | Arquitectura técnica resumida | Activo |

## 🛠️ Código operativo para mejorar

| Ubicación | Contenido |
|---|---|
| `../android/` | 5 apps + Wear + `core-network` (código para mejorar) |
| `../esp32/firmware/` | Firmware canónico Wemos D1 R32 (4 .ino + .h) |
| `../config/` | Gradle centralizado JDK17, compileSdk 35 |
| `../tools/` | Validadores, simuladores, export YOLO |
| `../.github/workflows/android-ci.yml` | CI testAllModules + buildAllApks |

## 📚 Documentación activa limpia

| Documento | Uso |
|---|---|
| `README.md` | Centro de documentación (presentar vs mejorar) |
| `INSTRUCTIVO_USO_PROYECTO.md` | Preparación, build, instalación, simulación, paso a laboratorio |
| `VALIDACION_Y_COBERTURA.md` | Alcance CI, qué cubre 12/12 y qué no |
| `deliverables/BITACORA_VALIDACION.md` | Registro vivo evidencia |
| `deliverables/QUALITY_GATES.md` | Gate 0..6 criterios |
| `deliverables/MANUAL_OPERATIVO_LABORATORIO.md` | Reglas operación segura |
| `deliverables/PROTOCOLO_PRUEBAS_HARDWARE.md` | HW-01..HW-09 |
| `deliverables/INFORME_TECNICO_DE_AVANCE.md` | Avance técnico resumido |
| `deliverables/FALENCIAS_RIESGOS_Y_PLAN.md` | Riesgos abiertos |
| `safety/SAFETY_ASSURANCE_ARCHITECTURE.md` | Arquitectura seguridad |
| `vision/DATASET_CAPTURE_AND_LABELING.md` | Dataset y etiquetado |
| `quickstart/README.md` | Guía rápida |
| `audits/AUDITORIA_TECNICA_2026-07-28.md` | Auditoría técnica |

Todo lo anterior es **para mejorar** (no solo para presentar).

## 🗃️ Histórico / no usar para presentar

| Ubicación | Motivo |
|---|---|
| `../archive/` | Snapshots, firmware antiguo, reportes históricos. No compilar/flashear desde aquí |
| `../archive/historico-entrega/ENTREGA_PRE_HARDWARE...` | Entrega antigua movida aquí en limpieza 2026-07-30 |
| `../archive/legacy/`, `organized-snapshot/`, `reports/` | Material histórico |
| `assets/` en raíz | Eliminado en limpieza, ahora todo en `docs/assets/imagenes/` |
| `entrega/informes/5_INFORMES/` | Eliminado duplicado 2026-07-30 |
| `docs/images/` duplicado, `docs/*.mjs`, `package-lock.json` | Eliminado antigua pipeline Node/Puppeteer |

## Comandos de control (antes de cualquier mejora)

```bash
python3 tools/validate_firmware_contract.py --quiet
python3 tools/validate_system_100.py --quiet   # 12/12 PASS esperado
python3 tools/prehardware_readiness.py --quiet
python3 -m compileall -q tools
git diff --check
```

Para Android:
```bash
cd config
./gradlew testAllModules lintAll buildAllApks validateApks writeApkChecksums
```

> **Regla:** `archive/` no es fuente operativa. `entrega/` solo contiene 2 PDFs finales. Todo activo está en `android/`, `esp32/firmware/`, `tools/`, `config/`, `docs/` limpio.
