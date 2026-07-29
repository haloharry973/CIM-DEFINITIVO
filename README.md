# CIM-DEFINITIVO

Autor: haloharry973

Proyecto académico adaptado y mantenido por mí. Este repositorio contiene el sistema CIM (Computer Integrated Manufacturing) con aplicaciones Android, firmware ESP32 y herramientas para desarrollo y pruebas. He dejado comentarios simples junto a cada carpeta para que cualquiera pueda orientarse rápidamente sobre dónde está cada cosa.

Estado: versión de desarrollo (ver pestaña Actions para CI).

Contenido principal y breve descripción de carpetas:

- android/                 -> Código Android: 5 apps, app Wear y librería de red compartida.
- config/                  -> Configuración y scripts Gradle para compilar y validar los módulos.
- esp32/                   -> Firmware y recursos para las placas ESP32/Wemos.
- tools/                   -> Scripts de soporte, validadores, simuladores y utilidades.
- docs/                    -> Documentación del proyecto, guías y entregables.
- entrega/                 -> Informes y documentos preparados para entrega.
- logs/                    -> Reportes y convenciones de validación.
- archive/                 -> Historial y snapshots: material de referencia (no usar en producción).
- .github/                 -> Configuración de GitHub (CI, plantillas).

Cómo compilar (resumen rápido):

1. Instalar JDK 17 y Android SDK.
2. Ir a la carpeta `config` y ejecutar:

   ```bash
   ./gradlew testAllModules lintAll buildAllApks validateApks writeApkChecksums
   ```

3. Los APKs aparecen en `config/output-apks/`.

Notas importantes:

- No incluir claves, APKs release o keystores en el repositorio.
- `archive/` es sólo histórico; comprobar versiones antes de usar.
- Los comandos de validación en `tools/` ayudan a probar sin hardware, pero no reemplazan pruebas reales.

Si quieres que cambie el texto (más personal, más técnico o en otro estilo), dime cómo lo quieres y lo actualizo.
