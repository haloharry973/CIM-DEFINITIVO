# CIM-DEFINITIVO — Práctica II | UBB

<p align="center">
  <img src="docs/assets/ubb_logo.png" alt="Universidad del Bío-Bío" width="280">
</p>

<p align="center"><strong>Universidad del Bío-Bío · Facultad de Ciencias Empresariales<br>Ing. de Ejecución en Computación e Informática — Leonardo Araya Labarca — 2026</strong></p>

> Sistema CIM (Computer Integrated Manufacturing) v6.0 — 5 estaciones Android + Wear + core-network + firmware ESP32/Wemos D1 R32. 
> Estado: **100% automatizable pre-hardware VALIDADO** — CI verde, 6 APKs, 12/12 checks estructurales. Validación física pendiente de protocolo de laboratorio.

---

## 🎯 Qué presentar (para evaluación)

**Carpeta `entrega/` – solo 2 PDFs finales (listos para imprimir):**

| Documento | Contenido | Páginas |
|---|---|---|
| `INFORME_PRACTICA_II_CIM_DEFINITIVO.pdf` | Informe académico UBB con resumen, objetivos, arquitectura, metodología 240h, bitácora commits, evidencias CI, conclusiones | ~25 pág |
| `MANUAL_TUTORIAL_CIM_DEFINITIVO.pdf` | Tutorial paso a paso instalación, flasheo ESP32, uso estaciones, seguridad, troubleshooting | ~30 pág |

**Carpeta `docs/project/` – fuente generadora y extras para defensa:**

- `INFORME_PRACTICA_II_CIM_DEFINITIVO_LEONARDO_ARAYA.pdf` (versión con nombre completo)
- `MANUAL_TUTORIAL_CIM_DEFINITIVO_LEONARDO_ARAYA.pdf`
- `DOCUMENTACION_SISTEMA_CIM.md` — arquitectura técnica
- `GENERADOR_PRACTICA_II.py` — script reportlab que genera ambos PDFs desde cero (reproducible)

**Carpeta `docs/deliverables/` – evidencias que respaldan lo presentado:**

- `BITACORA_VALIDACION.md` — registro vivo de commits y ensayos
- `QUALITY_GATES.md` — criterios Gate 0..6
- `MANUAL_OPERATIVO_LABORATORIO.md` y `PROTOCOLO_PRUEBAS_HARDWARE.md` — seguridad y paso a banco
- `INFORME_TECNICO_DE_AVANCE.md`

> Si solo necesitas entregar, basta con `entrega/`. Si te piden trazabilidad, añade `docs/deliverables/`.

---

## 🛠️ Qué usar para mejorar (para seguir desarrollando)

**Código activo (no histórico):**

```
android/                 # 5 apps + Wear + core-network (27 archivos Kotlin)
  apps/app-coordinador   # Hub, autorización, orquestación (com.industria.coordinacion)
  apps/app-plc           # Cinta, sensores pallet (com.industria.plc)
  apps/app-manufactura   # Robot Scorbot, G-code, láser (com.industria.manufactura)
  apps/app-calidad       # Cámara, ArUco, YOLO (com.industria.calidad)
  apps/app-almacen       # Rack 3x6 (com.industria.almacenamiento)
  apps/wear-coordinador  # Supervisión Wear OS
  core-network/          # Protocolo, BLE/TCP, identidad UUID, máquina pallet

esp32/firmware/          # Firmware canónico (NO usar archive/)
  esp32_plc_master.ino
  esp32_scorbot_manufactura.ino
  esp32_scorbot_calidad.ino
  esp32_scorbot_almacen.ino
  cim_ble_firmware.h

config/                  # Gradle centralizado JDK17, compileSdk 35
tools/                   # Validadores y simuladores
  validate_system_100.py            # Puerta 12/12 pre-hardware
  validate_firmware_contract.py     # Contrato UUID/tipo/capacidades
  prehardware_readiness.py          # Semáforo banco
  hub_simulator.py / vision_safety_simulator.py
  export_yolo_to_tflite.py / inspect_yolo_checkpoint.py
  generate_project_pdfs.py          # Generador antiguo
  GENERADOR en docs/project/GENERADOR_PRACTICA_II.py (nuevo)

docs/
  INDEX_REPOSITORIO.md              # Mapa completo
  INSTRUCTIVO_USO_PROYECTO.md       # Cómo compilar, instalar, simular
  VALIDACION_Y_COBERTURA.md         # Qué cubre CI y qué no
  safety/SAFETY_ASSURANCE_ARCHITECTURE.md
  vision/DATASET_CAPTURE_AND_LABELING.md
  quickstart/README.md
```

**Comandos para validar antes de mejorar:**

```bash
python3 tools/validate_firmware_contract.py --quiet
python3 tools/validate_system_100.py --quiet   # debe dar 12/12 PASS
python3 tools/prehardware_readiness.py --quiet
python3 -m compileall -q tools
git diff --check

# Android (requiere JDK17 + SDK)
cd config
./gradlew testAllModules lintAll buildAllApks validateApks writeApkChecksums
```

Artifacts: `config/output-apks/` + `SHA256SUMS.txt` (no versionar APKs).

---

## 📁 Estructura limpia actual (post-ordenamiento 2026-07-30)

```text
CIM-DEFINITIVO/
├── README.md                        # Este archivo (presentación + mejora)
├── CHANGELOG.md / CONTRIBUTING.md / SECURITY.md
├── .github/workflows/android-ci.yml # CI: test + build APKs
├── android/                         # Código para mejorar
├── config/                          # Build centralizado
├── esp32/firmware/                  # Firmware canónico
├── tools/                           # Scripts para mejorar
├── docs/                            # Documentación activa limpia
│   ├── README.md, INDEX_REPOSITORIO.md, INSTRUCTIVO..., VALIDACION...
│   ├── assets/imagenes/             # cim_arquitectura_v6.png, ui_* etc + ubb_logo.png
│   ├── assets/ubb_logo.png
│   ├── deliverables/                # Final + evidencias (sin duplicados)
│   │   ├── INFORME_PRACTICA_II_CIM_DEFINITIVO.pdf  (5.2 MB)
│   │   ├── MANUAL_TUTORIAL_CIM_DEFINITIVO.pdf      (5.9 MB)
│   │   ├── BITACORA_VALIDACION.md
│   │   ├── QUALITY_GATES.md
│   │   ├── MANUAL_OPERATIVO_LABORATORIO.md
│   │   ├── PROTOCOLO_PRUEBAS_HARDWARE.md
│   │   └── ... (solo esenciales)
│   ├── project/                     # Fuente + PDFs finales
│   │   ├── DOCUMENTACION_SISTEMA_CIM.md
│   │   ├── GENERADOR_PRACTICA_II.py
│   │   ├── INFORME_PRACTICA_II_...pdf
│   │   └── MANUAL_TUTORIAL_...pdf
│   ├── safety/, vision/, quickstart/, audits/
│   └── styles/                      # industrial_pdf.css (opcional)
├── entrega/                         # SOLO lo que se presenta (2 PDFs)
│   ├── INFORME_PRACTICA_II_CIM_DEFINITIVO.pdf
│   ├── MANUAL_TUTORIAL_CIM_DEFINITIVO.pdf
│   └── README.md
├── logs/                            # Placeholders para logs futuros
└── archive/                         # Histórico (NO operativo)
    ├── historico-entrega/           # Entrega pre-hardware antigua movida aquí
    ├── legacy/, firmware-v7-snapshot/, organized-snapshot/ etc
    └── README.md
```

**Eliminado en limpieza 2026-07-30 (ya no ocupa espacio):**
- `.fastRequest/`, `Template.rar`, `assets/models/bestMH.pt` (19 MB, debe ser descargado aparte, gitignored), `docs/images/` duplicado, `entrega/informes/5_INFORMES/` duplicado, `docs/project/ENTREGA_FINAL...pdf` y `MANUAL_IMPLEMENTACION...pdf` antiguos, `docs/*.mjs`, `package-lock.json`, `__pycache__/`

---

## 🚀 Uso rápido (para defensa)

1. **Leer:** `docs/INDEX_REPOSITORIO.md` → `docs/INSTRUCTIVO_USO_PROYECTO.md`
2. **Validar:** `python3 tools/validate_system_100.py` → 12/12
3. **Compilar:** `cd config && ./gradlew buildAllApks`
4. **Instalar:** `tools/powershell/Instalar-APKs.ps1` o `adb install -r config/output-apks/*.apk`
5. **Operar en simulación:** Coordinador primero (Iniciar Hub) → PLC → Manufactura → Calidad → Almacén
6. **Firmware:** Solo `esp32/firmware/` — ver `esp32/README.md` + `docs/deliverables/MANUAL_OPERATIVO_LABORATORIO.md`

CI verde referencia: `Android CIM CI` ejecución `30422387003` commit `3286792`.

---

## ⚠️ Seguridad

- No flashear desde `archive/`.
- No energizar actuadores sin E-Stop físico independiente, interlocks, supervisor y acta en `BITACORA_VALIDACION.md`.
- No versionar APKs, `*.keystore`, `*.pt`, `*.tflite`, secretos. Firma release vía `CIM_RELEASE_*`.

---

**Autor:** Leonardo Araya — IECI — UBB 2026  
**Repositorio:** `haloharry973/CIM-DEFINITIVO` rama `arena/019fb0f7-cim-definitivo`  
**Generador PDFs:** `docs/project/GENERADOR_PRACTICA_II.py` con `reportlab` + logo UBB oficial.
