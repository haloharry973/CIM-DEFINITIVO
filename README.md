# CIM-DEFINITIVO

<p align="center">
  <img src="docs/assets/ubb_logo.png" alt="Universidad del Bío-Bío" width="300">
</p>

<p align="center"><strong>Proyecto académico — Universidad del Bío-Bío · Ingeniería de Ejecución en Computación e Informática</strong></p>

Sistema CIM (Computer Integrated Manufacturing) con cinco aplicaciones Android, una app Wear, una biblioteca de red compartida y firmware ESP32/Wemos D1 R32 para las estaciones de Coordinación, PLC, Manufactura, Calidad y Almacenamiento.

> **Estado de validación automática:** el proyecto cuenta con CI para `testAllModules` y `buildAllApks`; además dispone de puertas locales/Gradle para `lintAll`, validación de APKs, checksums y `tools/validate_system_100.py`. La validación estructural de simulación debe marcar 100% antes de declarar una entrega automatizable. Las pruebas físicas de hardware, E-stop, relés, robot y láser siguen requiriendo evidencia de laboratorio.

## Navegación y estado

- **Documentación central:** [docs/README.md](docs/README.md) · [índice del repositorio](docs/INDEX_REPOSITORIO.md).
- **Cómo usar y validar:** [instructivo completo](docs/INSTRUCTIVO_USO_PROYECTO.md) · [estado de validación/cobertura](docs/VALIDACION_Y_COBERTURA.md).
- **Entrega vigente:** [entrega pre-hardware](docs/deliverables/ENTREGA_PRE_HARDWARE_LEONARDO_ARAYA.md).
- **Evidencia y bloqueadores:** [bitácora de validación](docs/deliverables/BITACORA_VALIDACION.md).
- **Colaboración y seguridad:** [CONTRIBUTING.md](CONTRIBUTING.md) · [SECURITY.md](SECURITY.md) · [CHANGELOG.md](CHANGELOG.md).

## Estructura activa

```text
- No incluir APK, keystores, claves, modelos duplicados ni archivos generados en commits.
- La firma release usa variables/propiedades locales (`CIM_RELEASE_*`); nunca hardcodear contraseñas en Gradle.
- Los informes deben describir resultados verificables de CI y pruebas de hardware; no declarar funcionalidades no probadas.

## Entrega pre-hardware y laboratorio

La entrega pre-hardware de Leonardo Araya se encuentra en [docs/deliverables/ENTREGA_PRE_HARDWARE_LEONARDO_ARAYA.md](docs/deliverables/ENTREGA_PRE_HARDWARE_LEONARDO_ARAYA.md) (con su PDF). Reúne el protocolo de pruebas, el manual de laboratorio, la matriz de riesgos y el semáforo de preparación. El índice navegable está en [docs/INDEX_REPOSITORIO.md](docs/INDEX_REPOSITORIO.md).

Antes de llevar un commit al banco, ejecute:

```bash
python3 tools/validate_firmware_contract.py --quiet
python3 tools/validate_system_100.py --quiet
python3 tools/prehardware_readiness.py --quiet
python3 -m compileall -q tools
git diff --check
```

Estos controles sólo verifican contratos, estructura, documentación y sintaxis. **No autorizan energizar actuadores ni reemplazan E-stop, interlocks, supervisión ni pruebas de hardware.** Para cualquier ensayo físico siga `docs/deliverables/MANUAL_OPERATIVO_LABORATORIO.md` y registre evidencia en la bitácora.
