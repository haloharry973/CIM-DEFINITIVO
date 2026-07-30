# Datos de APKs recuperados — 2026-07-30

## Archivos recuperados en limpieza

### 1. `android/apks/INSTRUCCIONES_VINCULACION_IA.txt`
Protocolo de handshake para vinculación de APKs con Hub Coordinador:
- Puerto 8888 TCP
- Trama: `CIM_MASTER_HUB_V1;[Nombre_App];[Password];[MAC];[UUID]`
- UUIDs oficiales: CIM-ST-ALM-X1, MAN-X2, CAL-X3, PLC-X4
- Estados: IDLE, BUSY, ERROR
- Comandos: REQ_PERM, GRANTED, ABORT

### 2. `docs/assets/models/bestMH.pt` (19 MB)
Modelo YOLO canónico para app-calidad. SHA-256 esperado:
`1305a2f90f86e8d9a50581d07c87d63efa1d721048d1a0a251a5ed9c5a607733`
Clases: caballo_hembra, caballo_macho, craneo_*, hacha_*, lomoToro_*, tuerca_macho

**Nota:** Este .pt está gitignored intencionalmente (19 MB) para no inflar el repo, pero se mantiene localmente en `docs/assets/models/` para que puedas generar TFLite:

```bash
pip install -r tools/requirements.txt
python tools/inspect_yolo_checkpoint.py docs/assets/models/bestMH.pt
python tools/export_yolo_to_tflite.py docs/assets/models/bestMH.pt --profile float32
```

### 3. `android/apks/` datos preservados
- `INSTALL_GUIDE.md` — guía instalación ADB
- `README.md` — no versiona APKs, genera con `cd config && ./gradlew buildAllApks`
- `manifest.json` — expected APKs list

### 4. `android/apps/*/app/src/main/assets/industrial_requirements.txt`
Requisitos industriales por estación — preservados en cada app (no se eliminaron).

Si necesitas recuperar además:
- `esp32/scripts/` (panel python legacy con cinta.py, detectoraruco.py etc) → estaba en `esp32/scripts/coordinador/esp32_scripts/` y fue movido a `archive/` en limpieza
- `config/scripts/` (build_all_apps.ps1, install_apks.ps1 etc) → movido a `archive/` histórico

Avisar si quieres que los restaure completos en su ubicación original.
