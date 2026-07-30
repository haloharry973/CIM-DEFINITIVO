#!/usr/bin/env python3
"""
Generador de Informe Práctica II y Manual/Tutorial CIM DEFINITIVO
Formato Universidad del Bío-Bío - Leonardo Araya
Usa reportlab para PDFs académicos con logo oficial.
"""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak,
    Table, TableStyle, ListFlowable, ListItem, KeepTogether, HRFlowable
)
from reportlab.platypus.doctemplate import BaseDocTemplate, PageTemplate, Frame
from reportlab.platypus import PageBreak
import os

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "docs" / "assets" / "imagenes"
ASSETS2 = ROOT / "docs" / "assets"
OUT_DIR = ROOT / "docs" / "project"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Resolver logos e imagenes
UBB_LOGO = ASSETS2 / "ubb_logo.png" if (ASSETS2 / "ubb_logo.png").exists() else ASSETS / "ubb_logo.png"
IMG_ARQ = ASSETS / "cim_arquitectura_v6.png"
IMG_FLUJO = ASSETS / "cim_flujo_app.png"
IMG_COORD = ASSETS / "ui_app_coordinador.png"
IMG_PLC = ASSETS / "ui_app_plc.png"
IMG_MANU = ASSETS / "ui_app_manufactura.png"
IMG_CALI = ASSETS / "ui_app_calidad.png"
IMG_ALMA = ASSETS / "ui_app_almacen.png"
IMG_BLE = ASSETS / "ui_bluetooth_connect.png"
IMG_ESP32 = ASSETS / "esp32_wokwi_simulacion.png"

def get_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='UBBTitle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        spaceAfter=12,
        textColor=colors.HexColor('#0a2d5c')
    ))
    styles.add(ParagraphStyle(
        name='UBBSubtitle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        alignment=TA_CENTER,
        spaceAfter=10,
        textColor=colors.HexColor('#1a4a8a')
    ))
    styles.add(ParagraphStyle(
        name='UBBHeader1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#0a2d5c'),
        spaceBefore=18,
        spaceAfter=10,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='UBBHeader2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#1e4a7a'),
        spaceBefore=14,
        spaceAfter=8
    ))
    styles.add(ParagraphStyle(
        name='UBBHeader3',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#2c5282'),
        spaceBefore=10,
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        name='UBBNormal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10.5,
        leading=15,
        alignment=TA_JUSTIFY,
        spaceAfter=8
    ))
    styles.add(ParagraphStyle(
        name='UBBBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        leftIndent=20,
        spaceAfter=4,
        alignment=TA_LEFT
    ))
    styles.add(ParagraphStyle(
        name='UBBCenter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        name='UBBsmall',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#4a5568')
    ))
    styles.add(ParagraphStyle(
        name='CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=11,
        leftIndent=12,
        rightIndent=12,
        backColor=colors.HexColor('#f7fafc'),
        borderColor=colors.HexColor('#e2e8f0'),
        borderWidth=0.5,
        borderPadding=(6,6,6,6),
        spaceAfter=10
    ))
    return styles

def add_page_number(canvas, doc):
    canvas.saveState()
    # header line
    canvas.setStrokeColor(colors.HexColor('#2c5282'))
    canvas.setLineWidth(0.8)
    canvas.line(doc.leftMargin, doc.height + doc.topMargin + 5, doc.width + doc.leftMargin, doc.height + doc.topMargin + 5)
    # footer
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor('#718096'))
    canvas.drawCentredString(A4[0]/2, 20, f"Página {doc.page}")
    canvas.setFont('Helvetica-Bold', 7)
    canvas.drawString(doc.leftMargin, 20, "CIM v6.0 - UBB - Práctica II - Leonardo Araya")
    canvas.drawRightString(doc.width + doc.leftMargin, 20, "Universidad del Bío-Bío")
    canvas.restoreState()

def cover_page(style_map):
    """Elements for cover"""
    elems = []
    if UBB_LOGO.exists():
        try:
            img = Image(str(UBB_LOGO), width=5*cm, height=5*cm, kind='proportional')
            img.hAlign = 'CENTER'
            elems.append(img)
        except:
            pass
    elems.append(Spacer(1, 0.5*cm))
    elems.append(Paragraph("UNIVERSIDAD DEL BÍO-BÍO", style_map['UBBSubtitle']))
    elems.append(Paragraph("Facultad de Ciencias Empresariales<br/>Departamento de Sistemas de Información<br/>Ingeniería de Ejecución en Computación e Informática", style_map['UBBCenter']))
    elems.append(Spacer(1, 0.8*cm))
    elems.append(HRFlowable(width="80%", thickness=1, lineCap='round', color=colors.HexColor('#2c5282'), spaceBefore=4, spaceAfter=8, hAlign='CENTER'))
    elems.append(Spacer(1, 0.8*cm))
    elems.append(Paragraph("INFORME PRÁCTICA PROFESIONAL II<br/><br/>Proyecto: CIM DEFINITIVO v6.0<br/>Sistema de Manufactura Integrada por Computador", style_map['UBBTitle']))
    elems.append(Spacer(1, 1.2*cm))
    
    data = [
        ["Estudiante:", "Leonardo Araya Labarca"],
        ["Carrera:", "Ing. de Ejecución en Computación e Informática"],
        ["Profesor Guía:", "Depto. Sistemas - UBB"],
        ["Empresa / Laboratorio:", "Laboratorio CIM - Universidad del Bío-Bío / Proyecto Interno"],
        ["Periodo:", "10 de marzo – 28 de julio de 2026 (240 hrs)"],
        ["Fecha Entrega:", "28 de julio de 2026"],
        ["Concepción – Chile", "2026"],
    ]
    t = Table(data, colWidths=[4*cm, 10*cm])
    t.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-2), 'Helvetica-Bold'),
        ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('ALIGN', (0,0), (0,-1), 'RIGHT'),
        ('ALIGN', (1,0), (1,-1), 'LEFT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('LINEBELOW', (0,0), (-1,-2), 0.3, colors.HexColor('#e2e8f0')),
        ('ALIGN', (0,-1), (-1,-1), 'CENTER'),
        ('SPAN', (0,-1), (-1,-1)),
    ]))
    elems.append(t)
    elems.append(Spacer(1, 2*cm))
    elems.append(Paragraph("Documento generado automáticamente desde repositorio CIM-DEFINITIVO. Evidencia verificable en GitHub Actions y bitácora de validación.", style_map['UBBsmall']))
    elems.append(PageBreak())
    return elems

def informe_content(styles):
    elems = []
    # TOC simulado
    elems.append(Paragraph("ÍNDICE GENERAL", styles['UBBHeader1']))
    toc_items = [
        "1. Resumen Ejecutivo ................................................................................ 3",
        "2. Introducción ........................................................................................ 4",
        "3. Objetivos .......................................................................................... 5",
        "   3.1 Objetivo General",
        "   3.2 Objetivos Específicos",
        "4. Descripción de la Empresa / Contexto Institucional ........................................ 6",
        "5. Descripción del Proyecto CIM DEFINITIVO .............................................. 7",
        "   5.1 Arquitectura General",
        "   5.2 Aplicaciones Android",
        "   5.3 Firmware ESP32/Wemos D1 R32",
        "   5.4 Biblioteca core-network y Protocolo",
        "   5.5 Modelo de Visión y Seguridad",
        "6. Metodología y Planificación ..................................................................... 11",
        "7. Actividades Realizadas (Bitácora 10 mar – 14 jul 2026) ............................... 12",
        "8. Resultados y Evidencias Verificables ........................................................ 14",
        "9. Limitaciones, Riesgos y Análisis Crítico .................................................... 18",
        "10. Conclusiones ........................................................................................ 20",
        "11. Bibliografía ......................................................................................... 21",
        "12. Anexos ............................................................................................... 22",
    ]
    for item in toc_items:
        elems.append(Paragraph(item, styles['UBBNormal']))
    elems.append(PageBreak())

    # Resumen
    elems.append(Paragraph("1. RESUMEN EJECUTIVO", styles['UBBHeader1']))
    elems.append(Paragraph(
        "El presente informe corresponde a la Práctica Profesional II de la carrera de Ingeniería de Ejecución en Computación e Informática "
        "de la Universidad del Bío-Bío, desarrollada por el estudiante Leonardo Araya Labarca durante el periodo 10 de marzo al 28 de julio de 2026, "
        "con una dedicación total estimada de 240 horas. El proyecto asignado fue <b>CIM DEFINITIVO v6.0</b>, un sistema de Manufactura Integrada por Computador (Computer Integrated Manufacturing) "
        "que orquesta cinco estaciones productivas mediante aplicaciones Android, una aplicación Wear OS para supervisión, una biblioteca de comunicación compartida (core-network) "
        "y firmware para placas ESP32/Wemos D1 R32 que controlan cinta, sensores, robot Scorbot, láser y almacenamiento.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "El objetivo principal de la práctica fue lograr una plataforma reproducible, trazable y validable automáticamente al 100% en su alcance pre-hardware, "
        "es decir, que toda la estructura de código, contratos de firmware, documentación, pruebas unitarias JVM, análisis Lint, compilación de APKs y generación de checksums "
        "pase sin errores en integración continua (GitHub Actions). La validación física con hardware real (BLE multiconexión, cámara, actuadores, E-Stop, LAN) queda explícitamente fuera de esta entrega y se documenta como pendiente en la bitácora.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "Como resultados verificables se obtuvo: corrección de bloqueantes Kotlin en módulos PLC y Calidad, compilación exitosa de 6 APKs debug mediante CI (workflow Android CIM CI, ejecución 30422387003), "
        "implementación de política de identidad con UUID canónico, bloqueo persistente de dispositivos rechazados, handshake con hash SHA-256, "
        "máquina de estados de pallet que bloquea transiciones imposibles, simuladores de hub y visión con 1000 casos, herramientas de inspección del checkpoint YOLO bestMH.pt, y documentación activa conforme a Quality Gates. "
        "La puerta estructural <b>validate_system_100.py</b> reporta 12/12 PASS local y CI verde.",
        styles['UBBNormal']))
    elems.append(Paragraph("<b>Palabras clave:</b> CIM, Android, ESP32, BLE, Manufactura Integrada, Práctica Profesional II, UBB, Validación 100%, Kotlin, Computer Integrated Manufacturing", styles['UBBNormal']))
    elems.append(PageBreak())

    # Introducción
    elems.append(Paragraph("2. INTRODUCCIÓN", styles['UBBHeader1']))
    elems.append(Paragraph(
        "La industria 4.0 demanda sistemas que integren software, redes y hardware de manera segura y trazable. En el Laboratorio de la Universidad del Bío-Bío se mantiene una celda CIM compuesta por estaciones de Coordinación, PLC (cinta transportadora y sensores), "
        "Manufactura (robot Scorbot ER-VII y láser), Calidad (cámara, ArUco y visión artificial) y Almacenamiento (rack automatizado). Históricamente el control se realizó con PLCs industriales y software heterogéneo, lo que dificultaba la actualización y la observabilidad.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "El proyecto CIM DEFINITIVO nace como refactorización completa en Android nativo (Kotlin), buscando: (i) estandarizar la UI/UX con Material 3, (ii) centralizar el protocolo de comunicación en una biblioteca core-network, "
        "(iii) añadir identidad criptográficamente verificable (UUID + capacidades), (iv) soportar BLE para la capa de campo y TCP/Wi-Fi para la capa de supervisión, y (v) dejar trazabilidad completa mediante CI y bitácora de validación.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "Para la Práctica II se definió un alcance pre-hardware preciso: No se energizan actuadores; toda prueba peligrosa queda bloqueada por semáforo rojo (ver docs/deliverables/PRE_HARDWARE_READINESS.md). Esto responde tanto a criterios de seguridad (necesidad de E-Stop físico independiente, interlocks, supervisión) como académicos (exigir evidencia verificable).",
        styles['UBBNormal']))
    elems.append(Paragraph("Contexto académico:", styles['UBBHeader2']))
    elems.append(Paragraph(
        "La Práctica Profesional II, según reglamento IECI-UBB, busca que el estudiante: potencie competencias conceptuales y actitudinales, aplique contenidos temáticos en entorno real, "
        "identifique situación organizacional, proponga mejoras y documente resultados. El Laboratorio CIM cumple como entorno relevante semi-industrial.",
        styles['UBBNormal']))
    elems.append(PageBreak())

    # Objetivos
    elems.append(Paragraph("3. OBJETIVOS", styles['UBBHeader1']))
    elems.append(Paragraph("3.1 Objetivo General", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Diseñar, implementar, validar automáticamente y documentar el sistema CIM DEFINITIVO v6.0 para operación pre-hardware reproducible, con 6 aplicaciones Android, firmware ESP32/Wemos y protocolos seguros, "
        "dejando trazable el camino hacia la validación física de laboratorio.",
        styles['UBBNormal']))
    elems.append(Paragraph("3.2 Objetivos Específicos", styles['UBBHeader2']))
    objs = [
        "Corregir bloqueantes de compilación Kotlin en módulos PLC y Calidad para obtener builds verdes en CI.",
        "Implementar identidad de estación basada en UUID canónico, MAC, versión, capacidades y política de admisión/bloqueo persistente.",
        "Definir e implementar protocolo de mensajería ID|TIMESTAMP|SOURCE_MAC|SOURCE_APP|DEST_MAC|DEST_APP|CMD|PRIORITY|SESSION|PAYLOAD, con transporte como hash SHA-256 del token de emparejamiento.",
        "Desarrollar máquina de estados de pallet que impida transiciones inválidas, validada con pruebas JVM.",
        "Crear simuladores hub_simulator.py y vision_safety_simulator.py para 1000 casos de seguridad sin activar automatización ante datos incompletos.",
        "Configurar CI (Android CIM CI) para testAllModules, lintAll, buildAllApks, validateApks y writeApkChecksums con artefactos y SHA256SUMS.txt.",
        "Alcanzar 12/12 checks en validate_system_100.py (estructura activa, herramientas, firmware canónico, ausencia de APKs versionadas, configuración CI).",
        "Proveer herramientas de inspección y exportación YOLO (inspect_yolo_checkpoint.py, export_yolo_to_tflite.py) para trazabilidad del modelo bestMH.pt.",
        "Elaborar documentación activa: Instructivo, Manual de Sistema, Manual Operativo de Laboratorio, Protocolo HW, Matriz de Riesgos, Quality Gates y Bitácora.",
        "Declarar explícitamente limitaciones vigentes y protocolo de paso a laboratorio con E-Stop e interlocks."
    ]
    for o in objs:
        elems.append(Paragraph(f"• {o}", styles['UBBBullet']))

    elems.append(PageBreak())

    # Descripción Empresa
    elems.append(Paragraph("4. DESCRIPCIÓN DE LA EMPRESA / CONTEXTO INSTITUCIONAL", styles['UBBHeader1']))
    elems.append(Paragraph("Universidad del Bío-Bío – Facultad de Ciencias Empresariales", styles['UBBHeader2']))
    elems.append(Paragraph(
        "La Universidad del Bío-Bío es una institución estatal acreditada por 5 años hasta 2030 en nivel avanzado. La carrera de Ingeniería de Ejecución en Computación e Informática, impartida en la sede Concepción, está acreditada por 6 años. Cuenta con consejo asesor externo y laboratorios de redes, manufactura y desarrollo.",
        styles['UBBNormal']))
    elems.append(Paragraph("Laboratorio CIM – Organización interna", styles['UBBHeader2']))
    elems.append(Paragraph(
        "El laboratorio posee una celda compuesta por: cinta transportadora con sensor de proximidad (GPIO34), robot Scorbot ER-VII con 5 GDL, efector láser de marcado, cámara para visión, rack de almacenamiento y tablero eléctrico con relés (GPIO5). La operación requiere: operador, supervisor, E-Stop independiente, delimitación de zona de movimiento, y registro de evidencia en BITACORA_VALIDACION.md.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "Stakeholders del proyecto: estudiante (desarrollo/documentación), profesor guía IECI, encargado de laboratorio (seguridad), futuros tesistas (continuidad). El proyecto se gestiona en GitHub haloharry973/CIM-DEFINITIVO con flujo de ramas arena/ y Pull Requests con CI verde obligatorio.",
        styles['UBBNormal']))
    elems.append(PageBreak())

    # Descripción proyecto
    elems.append(Paragraph("5. DESCRIPCIÓN DEL PROYECTO CIM DEFINITIVO", styles['UBBHeader1']))
    elems.append(Paragraph("5.1 Arquitectura General", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Arquitectura en tres capas: (1) Capa de Campo: ESP32/Wemos D1 R32 con firmware C, anuncios CIM_ID por BLE, telemetría y actuación de relés/sensores; (2) Capa de Estación: Apps Android (Kotlin) que hacen de gateway BLE-WiFi; (3) Capa de Coordinación: app hub TCP que orquesta flujo y autorización; (4) Capa de Supervisión: Wear OS y logs.",
        styles['UBBNormal']))
    if IMG_ARQ.exists():
        try:
            im = Image(str(IMG_ARQ), width=16*cm, height=9*cm, kind='proportional')
            im.hAlign = 'CENTER'
            elems.append(im)
            elems.append(Paragraph("Figura 1: Arquitectura CIM v6.0 – 5 estaciones + Wear + core-network + ESP32", styles['UBBsmall']))
        except:
            pass
    elems.append(Spacer(1, 0.3*cm))
    data_arch = [
        ["Capa", "Ubicación", "Responsabilidad"],
        ["Coordinación", "android/apps/app-coordinador", "Hub, autorización, orquestación"],
        ["PLC", "app-plc", "Cinta, sensores, eventos pallet"],
        ["Manufactura", "app-manufactura", "Robot, G-code, láser"],
        ["Calidad", "app-calidad", "Cámara, ArUco, YOLO, PASS/FAIL"],
        ["Almacén", "app-almacen", "Rack, guardar/recuperar"],
        ["Supervisión", "wear-coordinador", "Vista compacta Wear OS"],
        ["Red", "core-network", "Protocolo, BLE/TCP, identidad"],
        ["Firmware", "esp32/firmware", "BLE canónico estacionado"],
    ]
    t = Table(data_arch, colWidths=[2.5*cm, 4.5*cm, 8*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7fafc')]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    elems.append(t)
    elems.append(Spacer(1, 0.4*cm))

    elems.append(Paragraph("5.2 Aplicaciones Android", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Seis módulos Gradle con compileSdk 35, JDK 17, Kotlin 1.9+. Cada app posee: CimApplication, MainActivity, ViewModel por estación, core-network como dependencia, pruebas JVM y lint. Application IDs: com.industria.coordinacion, com.industria.plc, com.industria.manufactura, com.industria.calidad, com.industria.almacenamiento, com.industria.wear. Las UIs implementan visualización arcade basada en eventos aceptados y máquina de estados.",
        styles['UBBNormal']))
    if IMG_FLUJO.exists():
        try:
            im = Image(str(IMG_FLUJO), width=15*cm, height=8*cm, kind='proportional')
            im.hAlign='CENTER'
            elems.append(im)
            elems.append(Paragraph("Figura 2: Flujo de aplicación y estados de pallet", styles['UBBsmall']))
        except: pass

    elems.append(Paragraph("5.3 Firmware ESP32 / Wemos D1 R32", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Firmware canónico en esp32/firmware/: esp32_plc_master.ino, esp32_scorbot_manufactura.ino, esp32_scorbot_calidad.ino, esp32_scorbot_almacen.ino y cabecera común cim_ble_firmware.h. Incluye: definición CIM_ID, UUID, tipo, capacidades, anuncio BLE, framing y fragmentación para MTU inicial 20 bytes, reensamblado seguro, manejo de GPIO34 (sensor) y GPIO5 (relé) con estado seguro al arranque. Validado por validate_firmware_contract.py que exige UUID, nombre, tipo, versión coincidente con documentación.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "Se prohíbe usar firmware de archive/ para flasheo. Todo flasheo debe registrar commit, placa, puerto, versión en bitácora.",
        styles['UBBNormal']))

    elems.append(Paragraph("5.4 Biblioteca core-network y Protocolo", styles['UBBHeader2']))
    elems.append(Paragraph(
        "core-network implementa: protocolo de texto ID|TIMESTAMP|SOURCE_MAC|SOURCE_APP|DEST_MAC|DEST_APP|CMD|PRIORITY|SESSION|PAYLOAD, identidad StationIdentityPolicy con lista permitida/bloqueada persistente, handshake Android con token como SHA-256, fragmentación BLE, máquina de estados de pallet, telemetría y utilidades de visión.",
        styles['UBBNormal']))
    elems.append(Paragraph("Ejemplo de mensaje:", styles['UBBBullet']))
    elems.append(Paragraph("PLC_001|2026-07-28T10:00:00Z|AA:BB:CC:DD:EE:01|com.industria.plc|FF:FF:FF:FF:FF:FF|com.industria.coordinacion|PALLET_ARRIVED|HIGH|SESS_123|{sensor:1, pos:45}", styles['CodeStyle']))

    elems.append(Paragraph("5.5 Modelo de Visión y Seguridad", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Se utiliza checkpoint YOLO bestMH.pt para detección. Herramientas permiten inspeccionar clases, hash y exportar a TFLite. La lógica de decisión de visión en app-calidad es conservadora: ante baja confianza o datos incompletos retorna REVIEW_REQUIRED, no PASS automático. Se incluye simulador de seguridad de visión con 1000 casos (tools/vision_safety_simulator.py) validado por pruebas JVM. La cámara real, OpenCV y ArUco quedan pendientes de evidencia en dispositivo físico.",
        styles['UBBNormal']))
    elems.append(PageBreak())

    # Metodología
    elems.append(Paragraph("6. METODOLOGÍA Y PLANIFICACIÓN", styles['UBBHeader1']))
    elems.append(Paragraph("Enfoque de trabajo:", styles['UBBHeader2']))
    elems.append(Paragraph("Se adoptó desarrollo iterativo con validación automatizable continua: feature branch -> pruebas locales (validate_firmware_contract, validate_system_100, prehardware_readiness, compileall, git diff --check) -> push -> CI (testAllModules, lintAll, buildAllApks, validateApks, writeApkChecksums) -> revisión documental -> merge.", styles['UBBNormal']))
    elems.append(Paragraph("Cronograma 10 mar – 14 jul 2026 (240 hrs estimadas):", styles['UBBHeader2']))
    cron = [
        ["Periodo", "Horas", "Actividad clave"],
        ["10–16 mar", "14", "Levantamiento problema CIM, objetivos, alcance"],
        ["17–23 mar", "14", "Revisión arquitectura Android, coordinador, PLC"],
        ["24–30 mar", "14", "Diseño identidad estación, UUID, capacidades"],
        ["31 mar–6 abr", "14", "Flujos coordinación y eventos pallet"],
        ["7–13 abr", "14", "Estación PLC, cinta, sensor, telemetría"],
        ["14–20 abr", "14", "Manufactura, robot, G-code"],
        ["21–27 abr", "14", "Calidad, cámara, ArUco, visión"],
        ["28 abr–4 may", "14", "Almacén, rack, trazabilidad"],
        ["5–11 may", "14", "BLE framing, MTU 20 bytes, recuperación"],
        ["12–18 may", "14", "Autenticación/admisión nodos, bloqueos"],
        ["19–25 may", "14", "Simulación hub, escenarios seguridad"],
        ["26 may–1 jun", "14", "Checkpoint YOLO, exportación TFLite"],
        ["2–8 jun", "14", "Configuración Gradle, CI"],
        ["9–15 jun", "14", "Correcciones Kotlin, red, estados"],
        ["16–22 jun", "14", "Documentación, quickstart, rutas activas"],
        ["23–29 jun", "12", "Evaluación riesgos integración"],
        ["30 jun–6 jul", "10", "Criterios validación, trazabilidad"],
        ["7–14 jul", "8", "Consolidación, plan banco"],
    ]
    t = Table(cron, colWidths=[2.5*cm,1.2*cm,10.8*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7fafc')]),
    ]))
    elems.append(t)
    elems.append(PageBreak())

    # Actividades
    elems.append(Paragraph("7. ACTIVIDADES REALIZADAS (BITÁCORA)", styles['UBBHeader1']))
    elems.append(Paragraph("Actividades trazables por commit y evidencia:", styles['UBBNormal']))
    acts = [
        "f972771: Auditoría técnica inicial y corrección de bloqueantes Kotlin.",
        "cb41ef4: Corrección PLC – logs, constante duplicada, flujo BLE.",
        "069a0b1/97b3d9a: Corrección CameraX/ArUco en Calidad – compilación en build completo.",
        "340f54a: Desacoplamiento prueba G-code de OpenCV/Bitmap Android – suite ampliada.",
        "b8d4a98: Máquina de estados pallet – bloqueo transiciones inválidas por lógica.",
        "f2d9e35/e92b711/e780597: Correcciones framing BLE y aislamiento firmware Wemos.",
        "4677ee1: Bloqueo persistente dispositivos rechazados.",
        "2e6f0c3: Quality Gates entrega.",
        "arena/019fab05: Puerta 100% automatizable, lint real, checksums APKs, mitigación secretos Gradle/handshake SHA-256.",
        "Entrega pre-hardware 2026-07-29: contrato estático firmware, protocolo, manual operativo, matriz riesgos, semáforo preparación y PDF entrega."
    ]
    for a in acts:
        elems.append(Paragraph(f"• {a}", styles['UBBBullet']))
    elems.append(Paragraph("Comandos de validación ejecutados localmente antes de cada ensayo:", styles['UBBHeader2']))
    elems.append(Paragraph("python3 tools/validate_firmware_contract.py --quiet<br/>python3 tools/validate_system_100.py --quiet<br/>python3 tools/prehardware_readiness.py --quiet<br/>python3 -m compileall -q tools<br/>git diff --check<br/>cd config && ./gradlew testAllModules lintAll buildAllApks validateApks writeApkChecksums", styles['CodeStyle']))
    elems.append(PageBreak())

    # Resultados
    elems.append(Paragraph("8. RESULTADOS Y EVIDENCIAS VERIFICABLES", styles['UBBHeader1']))
    elems.append(Paragraph("8.1 Evidencia de compilación e integración continua", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Commit 3286792, rama entrega, GitHub Actions completó workflow Android CIM CI: ejecución 30422387003 con JDK 17, ejecutando testAllModules y buildAllApks correctamente. CI verde en PR #3 (79bbb98). Validación estructural local: 12/12 PASS. Config/output-apks contiene 6 APK debug + SHA256SUMS.txt.",
        styles['UBBNormal']))
    
    res_table = [
        ["Área", "Evidencia disponible", "Conclusión"],
        ["Gradle build debug", "CI verde testAllModules + buildAllApks", "No se detectaron errores en tareas CI"],
        ["Validación estructural", "validate_system_100.py 12/12", "Estructura y entregables comprobados"],
        ["Firmware contrato", "validate_firmware_contract.py PASS", "Contrato estático ok, falta flasheo"],
        ["UI instrumental", "Fuentes androidTest presentes, no CI emulador", "No certificada visual funcional"],
        ["Hardware BLE/cámara", "Pendiente física", "No verificado CI"],
    ]
    t = Table(res_table, colWidths=[2.8*cm,5.2*cm,6.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#ebf8ff')]),
    ]))
    elems.append(t)
    elems.append(Spacer(1,0.4*cm))
    elems.append(Paragraph("8.2 Mejoras verificables incorporadas", styles['UBBHeader2']))
    mejoras = [
        "Corrección bloqueantes Kotlin PLC y Calidad.",
        "Compilación 6 APKs mediante CI.",
        "Identidad estación UUID canónico + registro MAC/IP/modelo/capacidades.",
        "Bloqueo persistente dispositivos rechazados.",
        "Admisión Wemos D1 R32 por UUID/tipo/capacidades.",
        "Fragmentación y reensamblado BLE MTU 20 bytes.",
        "Máquina de estados pallet bloquea transiciones imposibles.",
        "Visualización arcade basada en eventos aceptados.",
        "Inspección/exportación checkpoint YOLO bestMH.pt.",
        "Puerta 100% automatizable estructura activa.",
        "Firma release sin contraseñas embebidas Gradle (CIM_RELEASE_*).",
        "Handshake Android token SHA-256.",
        "Checksums SHA-256 APKs debug.",
    ]
    for m in mejoras:
        elems.append(Paragraph(f"• {m}", styles['UBBBullet']))

    elems.append(Paragraph("8.3 Capturas de UI", styles['UBBHeader2']))
    # Insertar 2 imagenes UI por fila si existen
    for path_list, title in [
        ([IMG_COORD, IMG_PLC], "Coordinador y PLC"),
        ([IMG_MANU, IMG_CALI], "Manufactura y Calidad"),
        ([IMG_ALMA, IMG_BLE], "Almacén y Bluetooth Connect"),
    ]:
        row = []
        valid = [p for p in path_list if p.exists()]
        if not valid:
            continue
        for p in valid:
            try:
                im = Image(str(p), width=7.5*cm, height=6*cm, kind='proportional')
                row.append(im)
            except:
                row.append(Paragraph("[imagen no disponible]", styles['UBBsmall']))
        if len(row)==1:
            row.append(Paragraph("", styles['UBBsmall']))
        t = Table([row], colWidths=[7.8*cm,7.8*cm])
        elems.append(t)
        elems.append(Paragraph(f"Figura: {title}", styles['UBBsmall']))
        elems.append(Spacer(1,0.2*cm))

    elems.append(PageBreak())
    elems.append(Paragraph("9. LIMITACIONES, RIESGOS Y ANÁLISIS CRÍTICO", styles['UBBHeader1']))
    elems.append(Paragraph("9.1 Limitaciones vigentes declaradas", styles['UBBHeader2']))
    lims = [
        "No existe prueba física documentada con Wemos, relé, Scorbot ni láser.",
        "Modelo YOLO aún no convertido y validado como TFLite dentro de Android.",
        "E-Stop físico independiente no implementado en hardware.",
        "Movimiento robot y potencia láser sin realimentación física validada.",
        "Simulación no reemplaza pruebas eléctricas, mecánicas ni de seguridad.",
    ]
    for l in lims:
        elems.append(Paragraph(f"• {l}", styles['UBBBullet']))

    elems.append(Paragraph("9.2 Top 5 bloqueadores hacia 100% integral", styles['UBBHeader2']))
    bloq = [
        ["1", "BLE multiconexión 2+ ESP32 reales", "Logs 2+ placas, admisión/reconexión", "Pendiente lab"],
        ["2", "OpenCV + cámara dispositivo físico", "APK, dispositivo, imágenes ArUco, pallet trazable", "Pendiente lab"],
        ["3", "Actuadores Scorbot, láser, cinta", "E-Stop + interlocks + acta", "Bloqueado seguridad"],
        ["4", "LAN estable Coordinador", "Topología, IP/puerto, recuperación logs", "Pendiente infra"],
        ["5", "Tests unitarios faltantes Calidad/Manufactura/Almacén", "Pruebas reproducibles, cobertura error/estado", "Pendiente SW"],
    ]
    t = Table([["Pri","Bloqueador","Evidencia mínima cierre","Estado"]]+bloq, colWidths=[0.8*cm,4.5*cm,5.5*cm,3.2*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#c53030')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#feb2b2')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#fff5f5')]),
    ]))
    elems.append(t)

    elems.append(Paragraph("9.3 Seguridad y alcance de validación", styles['UBBHeader2']))
    elems.append(Paragraph(
        "La validación automática cubre estructura, contrato, sintaxis y tareas CI configuradas. No comprueba UI en todos los dispositivos, rendimiento LAN/BLE, cámara real, tensión eléctrica, E-Stop, relé, robot, cinta ni láser. Consulta VALIDACION_Y_COBERTURA.md, manual laboratorio y protocolo hardware. Por ello no es correcto afirmar 'no existe el más mínimo error en todo el sistema': las pruebas solo demuestran ausencia de fallos dentro de escenarios ejecutados. La formulación precisa es: las validaciones automatizadas y build configurados aprobaron; la validación UI instrumental y física continúa limitada por evidencia disponible.",
        styles['UBBNormal']))

    elems.append(PageBreak())
    elems.append(Paragraph("10. CONCLUSIONES", styles['UBBHeader1']))
    elems.append(Paragraph(
        "La Práctica II permitió consolidar una plataforma CIM reproducible y auditable, cumpliendo el objetivo de 100% automatizable pre-hardware. Se logró CI verde, 6 APKs, identidad segura, máquina de estados robusta y documentación que diferencia explícitamente entre validación automática y validación física. El enfoque de puertas (validate_system_100.py) y Quality Gates evita declaraciones no sustentadas.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "Como aprendizaje, se destaca la importancia de contratos estáticos validados antes del banco, de no versionar binarios, de transportar secretos como hash y de registrar evidencia con fecha/operador/commit/dispositivo. La reconstrucción retrospectiva de 240 hrs evidencia dedicación en análisis, desarrollo, simulación y documentación, sin inventar mediciones físicas.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "El trabajo futuro (para tesis) consiste en ejecutar el protocolo HW-01 a HW-09 con E-Stop, interlocks, supervisor, captura de CIM_ID, pruebas BLE multiconexión, cámara real y actas firmadas, para luego cerrar los Quality Gates Gate 2 a Gate 5.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "Se concluye que la entrega pre-hardware está preparada para revisión de banco condicionada, sin autorización para operación de relé con carga, robot, láser o ciclo autónomo hasta cerrar ítems de seguridad y registrar evidencia en bitácora.",
        styles['UBBNormal']))

    elems.append(Paragraph("11. BIBLIOGRAFÍA", styles['UBBHeader1']))
    bib = [
        "Universidad del Bío-Bío – Manual de Comunicación Corporativa – Marca y escudo institucional.",
        "Documentación Android Developers – CameraX, BLE, Wear OS, Gradle, Lint.",
        "Espressif – ESP32 Technical Reference Manual, BLE GATT.",
        "Scorbot ER-VII – Manual de operación y seguridad.",
        "Redmon, J. et al. – YOLO object detection.",
        "OpenCV – ArUco marker detection documentation.",
        "Docs CIM – INSTRUCTIVO_USO_PROYECTO.md, VALIDACION_Y_COBERTURA.md, SAFETY_ASSURANCE_ARCHITECTURE.md",
        "GitHub Actions – Workflow Android CIM CI – ejecución 30422387003",
    ]
    for b in bib:
        elems.append(Paragraph(f"• {b}", styles['UBBBullet']))

    elems.append(Paragraph("12. ANEXOS", styles['UBBHeader1']))
    elems.append(Paragraph("Anexo A – Comandos de control obligatorio", styles['UBBHeader2']))
    elems.append(Paragraph("python3 tools/validate_firmware_contract.py --quiet<br/>python3 tools/validate_system_100.py --quiet<br/>python3 tools/prehardware_readiness.py --quiet<br/>python3 -m compileall -q tools<br/>git diff --check", styles['CodeStyle']))
    elems.append(Paragraph("Anexo B – Estructura activa repositorio", styles['UBBHeader2']))
    elems.append(Paragraph(
        "CIM-DEFINITIVO/<br/>├── android/ (5 apps + Wear + core-network)<br/>├── config/ (Gradle centralizado)<br/>├── esp32/firmware/ (firmware canónico)<br/>├── tools/ (validadores, simuladores)<br/>├── docs/ (documentación activa)<br/>├── entrega/ (informes seleccionados)<br/>└── archive/ (historial, no operativo)",
        styles['CodeStyle']))
    elems.append(Paragraph("Anexo C – Protocolo pruebas hardware HW-01..HW-09", styles['UBBHeader2']))
    elems.append(Paragraph(
        "HW-01 Inspección sin energía – cableado/polaridad/masa GPIO34<br/>"
        "HW-02 E-Stop – corta energía actuadores independiente software<br/>"
        "HW-03 Identidad – CIM_ID coincide UUID/capacidades<br/>"
        "HW-04 Admisión BLE – acepta válido, rechaza incompatible<br/>"
        "HW-05 Sensor GPIO34 – lecturas estables<br/>"
        "HW-06 Relé GPIO5 sin carga – arranque seguro<br/>"
        "HW-07 Reconexión – pérdida/reingreso estado seguro<br/>"
        "HW-08 Visión – cámara/pieza/ArUco trazable<br/>"
        "HW-09 Actuadores – fuera alcance pre-hardware hasta HW-01..08 aprobadas",
        styles['UBBNormal']))
    elems.append(Spacer(1, 1*cm))
    elems.append(Paragraph("Fin del Informe Práctica II – Leonardo Araya – UBB 2026", styles['UBBCenter']))
    return elems

def informe_tutorial_content(styles):
    elems = []
    elems.append(Paragraph("ÍNDICE MANUAL / TUTORIAL", styles['UBBHeader1']))
    toc = [
        "1. Introducción al Sistema CIM ........................................................................ 3",
        "2. Requisitos e Instalación ............................................................................. 4",
        "3. Arquitectura y Flujo Operativo ............................................................... 6",
        "4. Tutorial Paso a Paso – Instalación Android ................................................ 8",
        "5. Tutorial Firmware ESP32 / Wemos D1 R32 ............................................... 12",
        "6. Uso del Sistema – Coordinador, PLC, Manufactura, Calidad, Almacén, Wear .... 14",
        "7. Comunicación, Identidad y Seguridad ....................................................... 18",
        "8. Simulación y Herramientas de Visión ....................................................... 19",
        "9. Solución de Problemas Frecuentes ........................................................... 20",
        "10. Protocolo de Laboratorio y Seguridad ....................................................... 22",
    ]
    for t in toc:
        elems.append(Paragraph(t, styles['UBBNormal']))
    elems.append(PageBreak())

    elems.append(Paragraph("1. INTRODUCCIÓN AL SISTEMA CIM", styles['UBBHeader1']))
    elems.append(Paragraph(
        "Bienvenido al <b>Manual de Usuario y Tutorial del Sistema CIM DEFINITIVO v6.0</b>. Este documento te guiará desde cero para instalar, configurar y operar la celda de manufactura integrada por computador desarrollada en la Universidad del Bío-Bío. Al finalizar podrás: instalar las 6 APKs, flashear los ESP32, iniciar el hub Coordinador, admitir estaciones y ejecutar un ciclo completo de pallet en simulación segura sin energizar actuadores peligrosos.",
        styles['UBBNormal']))
    elems.append(Paragraph("¿Qué es CIM DEFINITIVO?", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Es una refactorización completa de la celda CIM del laboratorio: en lugar de PLCs heterogéneos, usa tablets/celulares Android como controladores de estación y placas Wemos D1 R32 (ESP32) como interfaz de campo BLE. La lógica de negocio (máquina de estados pallet, admisión por UUID, visión conservadora) vive en Kotlin y es validada automáticamente por CI. El estado actual es pre-hardware 100% automatizable: puedes probar todo el software sin riesgo.",
        styles['UBBNormal']))
    elems.append(Paragraph("Público objetivo:", styles['UBBHeader2']))
    for pub in ["Estudiantes IECI en Práctica II / Tesis", "Encargado de laboratorio", "Futuros mantenedores del código"]:
        elems.append(Paragraph(f"• {pub}", styles['UBBBullet']))
    elems.append(PageBreak())

    elems.append(Paragraph("2. REQUISITOS E INSTALACIÓN", styles['UBBHeader1']))
    elems.append(Paragraph("2.1 Requisitos de Software", styles['UBBHeader2']))
    req_sw = [
        ["Recurso", "Versión", "Uso"],
        ["Git", "2.x +", "Obtener código"],
        ["Python 3", "3.11+", "Validadores"],
        ["JDK", "17", "Gradle/Android"],
        ["Android SDK", "compileSdk 35, build-tools", "Compilar apps"],
        ["Android Studio o cmdline-tools", "Hedgehog+", "ADB, emulador"],
        ["Chrome/Edge", "Reciente", "Generar PDFs (opcional)"],
        ["Arduino IDE / CLI / PlatformIO", "1.8+ / 2.x", "Flasheo ESP32"],
    ]
    t = Table(req_sw, colWidths=[3*cm,2.5*cm,9*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7fafc')]),
    ]))
    elems.append(t)
    elems.append(Spacer(1,0.4*cm))
    elems.append(Paragraph("2.2 Requisitos Hardware (para paso a laboratorio, NO para este tutorial)", styles['UBBHeader2']))
    for hw in [
        "Wemos D1 R32 (4 unidades mínimo) + cables USB",
        "Fuente 12V, fusible, tablero con relé GPIO5 y sensor GPIO34 con interfaz protegida",
        "Tablet/celular Android 8.0+ (6 dispositivos ideal)",
        "Red Wi-Fi controlada, sin acceso internet obligatorio",
        "E-Stop físico independiente probado – OBLIGATORIO antes de cualquier actuador",
        "Zona delimitada sin personas en radio movimiento Scorbot"
    ]:
        elems.append(Paragraph(f"• {hw}", styles['UBBBullet']))
    elems.append(Paragraph("NOTA DE SEGURIDAD:", styles['UBBHeader3']))
    elems.append(Paragraph(
        "Este tutorial cubre solo instalación y simulación. Nunca conectes actuadores reales sin E-Stop físico que corte energía de actuadores independientemente del software, interlocks, supervisor y acta firmada. Ver MANUAL_OPERATIVO_LABORATORIO.md.",
        styles['UBBNormal']))

    elems.append(PageBreak())

    elems.append(Paragraph("3. ARQUITECTURA Y FLUJO OPERATIVO", styles['UBBHeader1']))
    if IMG_ARQ.exists():
        try:
            im = Image(str(IMG_ARQ), width=16*cm, height=9*cm, kind='proportional')
            im.hAlign='CENTER'; elems.append(im)
            elems.append(Paragraph("Figura: Arquitectura 3 capas CIM v6.0", styles['UBBsmall']))
        except: pass
    if IMG_FLUJO.exists():
        try:
            im = Image(str(IMG_FLUJO), width=15*cm, height=8*cm, kind='proportional')
            im.hAlign='CENTER'; elems.append(im)
            elems.append(Paragraph("Figura: Flujo de pallets y estados (IDLE, MOVING, PROCESSING, QUALITY, STORAGE, BLOCKED)", styles['UBBsmall']))
        except: pass
    elems.append(Paragraph("Flujo simplificado de un pallet:", styles['UBBHeader2']))
    flujo = [
        "1. PLC detecta pallet (sensor GPIO34) -> envía PALLET_ARRIVED al Coordinador.",
        "2. Coordinador autoriza y ordena a Manufactura.",
        "3. Manufactura ejecuta G-code robot + láser (en simulación solo telemetría).",
        "4. Manufactura marca COMPLETED -> Coordinador envía a Calidad.",
        "5. Calidad captura cámara, detecta ArUco, YOLO bestMH.pt decide PASS/FAIL/REVIEW_REQUIRED.",
        "6. Según decisión, Coordinador deriva a Almacén (PASS) o a revisión (FAIL/BLOCKED).",
        "7. Almacén guarda en rack y confirma STORED.",
    ]
    for f in flujo:
        elems.append(Paragraph(f"• {f}", styles['UBBBullet']))
    elems.append(PageBreak())

    elems.append(Paragraph("4. TUTORIAL PASO A PASO – INSTALACIÓN ANDROID", styles['UBBHeader1']))
    elems.append(Paragraph("Paso 0 – Clonar y validar repositorio", styles['UBBHeader2']))
    elems.append(Paragraph("Abre terminal en carpeta deseada:", styles['UBBNormal']))
    elems.append(Paragraph("git clone https://github.com/haloharry973/CIM-DEFINITIVO.git<br/>cd CIM-DEFINITIVO<br/>python3 tools/validate_firmware_contract.py --quiet<br/>python3 tools/validate_system_100.py --quiet<br/>python3 tools/prehardware_readiness.py --quiet<br/>python3 -m compileall -q tools<br/>git diff --check", styles['CodeStyle']))
    elems.append(Paragraph("Debes ver PASS / sin errores. Si falla, corrige el archivo indicado.", styles['UBBNormal']))

    elems.append(Paragraph("Paso 1 – Preparar SDK", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Instala JDK 17 (no 21). Configura ANDROID_HOME / ANDROID_SDK_ROOT apuntando a tu SDK. "
        "Acepta licencias: sdkmanager --licenses. Asegura platform-tools (ADB) en PATH.",
        styles['UBBNormal']))

    elems.append(Paragraph("Paso 2 – Compilar APKs", styles['UBBHeader2']))
    elems.append(Paragraph("En Linux/Mac:", styles['UBBNormal']))
    elems.append(Paragraph("cd config<br/>./gradlew testAllModules<br/>./gradlew lintAll<br/>./gradlew buildAllApks validateApks writeApkChecksums", styles['CodeStyle']))
    elems.append(Paragraph("En Windows PowerShell:", styles['UBBNormal']))
    elems.append(Paragraph("cd config<br/>.\\gradlew.bat testAllModules<br/>.\\gradlew.bat lintAll<br/>.\\gradlew.bat buildAllApks validateApks writeApkChecksums", styles['CodeStyle']))
    elems.append(Paragraph(
        "Las APK debug quedan en config/output-apks/ con SHA256SUMS.txt. No las subas al repo (están en .gitignore). "
        "Si no tienes SDK local, revisa la pestaña Actions del repo: descarga artefactos del último CI verde.",
        styles['UBBNormal']))

    elems.append(Paragraph("Paso 3 – Instalar en dispositivos", styles['UBBHeader2']))
    elems.append(Paragraph("Conecta tablet por USB, habilita depuración USB y:", styles['UBBNormal']))
    elems.append(Paragraph("adb devices  # debe listar dispositivo\n.\\tools\\powershell\\Instalar-APKs.ps1  # en Windows\n# o manual:\nadb install -r config/output-apks/app-coordinador-debug.apk\nadb install -r config/output-apks/app-plc-debug.apk\nadb install -r config/output-apks/app-manufactura-debug.apk\nadb install -r config/output-apks/app-calidad-debug.apk\nadb install -r config/output-apks/app-almacen-debug.apk\nadb install -r config/output-apks/wear-coordinador-debug.apk  # si tienes Wear", styles['CodeStyle']))

    elems.append(Paragraph("Paso 4 – Primer arranque (orden importante)", styles['UBBHeader2']))
    elems.append(Paragraph(
        "IMPORTANTE: Abre primero <b>Coordinador</b>. Pulsa 'Iniciar Hub'. Anota IP y puerto mostrados. "
        "Luego abre PLC, Manufactura, Calidad, Almacén en ese orden. Cada estación pedirá admisión. "
        "En Coordinador verás solicitudes con MAC, UUID, versión, capacidades. Acepta si UUID coincide con lista esperada. "
        "Los rechazados quedan bloqueados persistentemente (puedes desbloquear desde Coordinador).",
        styles['UBBNormal']))
    if IMG_COORD.exists():
        try:
            im = Image(str(IMG_COORD), width=7*cm, height=6*cm, kind='proportional')
            elems.append(im)
            elems.append(Paragraph("Figura: UI App Coordinador – Hub e identidad", styles['UBBsmall']))
        except: pass

    elems.append(PageBreak())

    elems.append(Paragraph("5. TUTORIAL FIRMWARE ESP32 / WEMOS D1 R32", styles['UBBHeader1']))
    elems.append(Paragraph("Paso 5 – Revisar firmware canónico", styles['UBBHeader2']))
    elems.append(Paragraph("Solo usar esp32/firmware/ (no archive/):", styles['UBBNormal']))
    elems.append(Paragraph("esp32/firmware/esp32_plc_master.ino\nesp32/firmware/esp32_scorbot_manufactura.ino\nesp32/firmware/esp32_scorbot_calidad.ino\nesp32/firmware/esp32_scorbot_almacen.ino\nesp32/firmware/cim_ble_firmware.h", styles['CodeStyle']))
    elems.append(Paragraph("Paso 6 – Flasheo", styles['UBBHeader2']))
    elems.append(Paragraph("Con Arduino IDE: selecciona placa 'WEMOS D1 R32', puerto COMx, abre .ino y Subir. Con CLI:", styles['UBBNormal']))
    elems.append(Paragraph(".\\tools\\powershell\\Flashear-ESP32.ps1 -Port COM3 -Firmware PLC\n# o\narduino-cli compile --fqbn esp32:esp32:d1_mini32 esp32/firmware/esp32_plc_master.ino\narduino-cli upload -p COM3 --fqbn esp32:esp32:d1_mini32 esp32/firmware/esp32_plc_master.ino", styles['CodeStyle']))
    elems.append(Paragraph("Paso 7 – Captura CIM_ID", styles['UBBHeader2']))
    elems.append(Paragraph("Abre Monitor Serie 115200 baud. Debes ver anuncio tipo CIM_ID:PLC_001:UUID:CAP:... Anota y registra en bitácora con fecha, operador, commit, placa, puerto.", styles['UBBNormal']))
    if IMG_ESP32.exists():
        try:
            im = Image(str(IMG_ESP32), width=14*cm, height=8*cm, kind='proportional')
            elems.append(im)
            elems.append(Paragraph("Figura: Simulación Wokwi ESP32 – referencia para captura CIM_ID", styles['UBBsmall']))
        except: pass
    elems.append(PageBreak())

    elems.append(Paragraph("6. USO DEL SISTEMA – ESTACIONES", styles['UBBHeader1']))
    # Each station tutorial with image
    for title, img_path, desc in [
        ["6.1 Estación PLC / Cinta", IMG_PLC, "Gestiona cinta transportadora y sensor de proximidad. Eventos: PALLET_ARRIVED, PALLET_LEFT. Muestra estado sensor GPIO34 (simulado sin hardware). Botones: Iniciar cinta (solo telemetría en pre-hardware), Detener, Enviar evento manual."],
        ["6.2 Estación Manufactura / Scorbot + Láser", IMG_MANU, "Controla robot y láser. En pre-hardware no energiza. Permite cargar G-code, ver posiciones, ejecutar simulación de trayectoria. Orden láser solo con autorización. Botones: Home, Ejecutar G-code (sim), Parada segura."],
        ["6.3 Estación Calidad / Cámara + ArUco + YOLO", IMG_CALI, "Cámara con CameraX, detección ArUco, inferencia YOLO (TFLite pendiente). En simulación muestra resultado REVIEW_REQUIRED ante baja confianza. Botones: Iniciar cámara, Capturar, Detectar ArUco, Evaluar Calidad. Resultado PASS/FAIL asociado a pallet."],
        ["6.4 Estación Almacén / Rack", IMG_ALMA, "Gestiona posiciones de rack para guardar/recuperar. Operaciones trazables con pallet ID. Botones: Buscar posición libre, Guardar, Recuperar, Listar inventario."],
    ]:
        elems.append(Paragraph(title, styles['UBBHeader2']))
        elems.append(Paragraph(desc, styles['UBBNormal']))
        if img_path.exists():
            try:
                im = Image(str(img_path), width=8*cm, height=6*cm, kind='proportional')
                im.hAlign='LEFT'
                elems.append(im)
            except: pass
        elems.append(Spacer(1,0.4*cm))

    elems.append(Paragraph("6.5 App Wear – Supervisión", styles['UBBHeader2']))
    elems.append(Paragraph("Vista compacta de estados para smartwatch. Solo supervisión, no control de seguridad. Muestra lista pallets, estados, alertas.", styles['UBBNormal']))
    if IMG_BLE.exists():
        try:
            im = Image(str(IMG_BLE), width=8*cm, height=6*cm, kind='proportional')
            elems.append(im)
            elems.append(Paragraph("Figura: Conexión Bluetooth – Lista de dispositivos y estado BLE", styles['UBBsmall']))
        except: pass
    elems.append(PageBreak())

    elems.append(Paragraph("7. COMUNICACIÓN, IDENTIDAD Y SEGURIDAD", styles['UBBHeader1']))
    elems.append(Paragraph("Formato mensaje:", styles['UBBHeader2']))
    elems.append(Paragraph("ID|TIMESTAMP|SOURCE_MAC|SOURCE_APP|DEST_MAC|DEST_APP|CMD|PRIORITY|SESSION|PAYLOAD", styles['CodeStyle']))
    elems.append(Paragraph("Identidad:", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Cada estación tiene UUID canónico, MAC, tipo (PLC, MANUFACTURA, CALIDAD, ALMACEN, COORDINADOR), versión y capacidades. "
        "StationIdentityPolicy valida: UUID coincidente, tipo esperado, capacidades compatibles. Incompatible = bloqueo persistente. "
        "Token emparejamiento viaja como SHA-256, no texto plano.",
        styles['UBBNormal']))
    elems.append(Paragraph("Seguridad conservadora:", styles['UBBHeader2']))
    for sec in [
        "Fragmentación BLE con MTU 20 bytes inicial, reensamblado seguro con timeout.",
        "Máquina pallet bloquea transiciones imposibles (ej: STORAGE -> PROCESSING sin pasar por QUALITY).",
        "Visión conservadora: baja confianza = REVIEW_REQUIRED, no PASS.",
        "Relé GPIO5 arranca en estado seguro (abierto).",
        "E-Stop independiente obligatorio – software nunca único control.",
    ]:
        elems.append(Paragraph(f"• {sec}", styles['UBBBullet']))

    elems.append(PageBreak())
    elems.append(Paragraph("8. SIMULACIÓN Y HERRAMIENTAS DE VISIÓN", styles['UBBHeader1']))
    elems.append(Paragraph("Simuladores sin hardware:", styles['UBBHeader2']))
    elems.append(Paragraph("python3 tools/hub_simulator.py  # simula hub coordinador y admisión\npython3 tools/vision_safety_simulator.py  # 1000 casos seguridad visión\npython3 tools/inspect_yolo_checkpoint.py --checkpoint assets/models/bestMH.pt\npython3 tools/export_yolo_to_tflite.py --checkpoint bestMH.pt --output bestMH.tflite\npython3 tools/tflite_yolo_test.py", styles['CodeStyle']))
    elems.append(Paragraph("Estos comandos permiten validar lógica sin banco.", styles['UBBNormal']))

    elems.append(Paragraph("9. SOLUCIÓN DE PROBLEMAS FRECUENTES", styles['UBBHeader1']))
    probs = [
        ["Problema", "Causa probable", "Solución"],
        ["APK no instala", "Depuración USB desactivada / firma distinta", "Habilita depuración, desinstala versión previa, adb install -r"],
        ["Coordinador no ve estación", "IP/puerto incorrecto / firewall / red distinta", "Verifica Wi-Fi misma red, revisa IP mostrada en Coordinador, desactiva firewall"],
        ["BLE no conecta", "Permisos ubicación / Bluetooth desactivado / firmware no flasheado", "Concede permisos, activa Bluetooth, revisa CIM_ID en Monitor Serie"],
        ["validate_system_100 FAIL", "Falta archivo activo o hay APK versionada en repo", "Lee log, corrige estructura, git rm APKs versionadas"],
        ["Lint falla", "Uso API deprecada / resource no encontrado", "Ejecuta ./gradlew :app:lintDebug --stacktrace, corrige"],
        ["Cámara negra en Calidad", "Permiso cámara no concedido / emulador sin cámara", "Concede permiso, prueba en dispositivo físico con cámara"],
        ["E-Stop no corta energía", "Cableado incorrecto / relé sin alimentación independiente", "DETENER TODO, revisar esquema eléctrico, no continuar sin E-Stop probado"],
    ]
    t = Table(probs, colWidths=[3*cm,4.5*cm,7*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7fafc')]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    elems.append(t)
    elems.append(PageBreak())

    elems.append(Paragraph("10. PROTOCOLO DE LABORATORIO Y SEGURIDAD", styles['UBBHeader1']))
    elems.append(Paragraph("Checklist antes de energizar (reproducido de MANUAL_OPERATIVO_LABORATORIO.md):", styles['UBBHeader2']))
    checklist = [
        "Operador y supervisor identificados; área delimitada y sin personas en zona de movimiento.",
        "E-Stop físico independiente probado y accesible (corta energía actuadores, no solo orden software).",
        "Robot/láser sin permiso operación; relé GPIO5 sin carga durante pruebas iniciales.",
        "Fuente, fusible, masas, conectores y polaridad inspeccionados.",
        "GPIO34 con interfaz eléctrica definida (no aplicar tensión fuera rango ESP32 ni dejar flotante).",
        "Firmware tomado de esp32/firmware/, commit y puertos anotados.",
    ]
    for c in checklist:
        elems.append(Paragraph(f"☐ {c}", styles['UBBBullet']))

    elems.append(Paragraph("Secuencia arranque controlado:", styles['UBBHeader2']))
    for step in [
        "1. Energizar lógica con actuadores aislados.",
        "2. Abrir monitor serie y confirmar anuncio CIM_ID esperado.",
        "3. Conectar una estación BLE y comprobar UUID/tipo/capacidades.",
        "4. Ejecutar solo comandos lectura/telemetría. Registrar timeout, desconexión o rechazo.",
        "5. Probar sensor y relé sin carga, con una persona observando E-Stop.",
        "6. Ante anomalía: accionar E-Stop, retirar energía actuadores, conservar logs, registrar incidencia.",
    ]:
        elems.append(Paragraph(f"• {step}", styles['UBBBullet']))

    elems.append(Paragraph("Criterios de detención inmediata:", styles['UBBHeader2']))
    for crit in [
        "Identidad distinta / CIM_ID inesperado",
        "Relé activo al arranque",
        "E-Stop ineficaz",
        "GPIO flotante / lecturas erráticas",
        "Pérdida enlace en estado riesgo",
        "Movimiento inesperado robot/cinta",
        "Ausencia supervisor",
    ]:
        elems.append(Paragraph(f"• {crit}", styles['UBBBullet']))

    elems.append(Spacer(1, 0.8*cm))
    elems.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2c5282')))
    elems.append(Paragraph("Documento fin – Tutorial CIM DEFINITIVO v6.0 – Universidad del Bío-Bío – Leonardo Araya 2026", styles['UBBCenter']))
    elems.append(Paragraph("Para evidencia y bitácora usar docs/deliverables/BITACORA_VALIDACION.md – Cada ensayo debe registrar fecha, operador, commit, APK/firmware, dispositivo, escenario, esperado, observado, logs/captura, incidencia, acción y aprobación.", styles['UBBsmall']))

    return elems

def build_pdf(path_out, elements, title):
    doc = SimpleDocTemplate(
        str(path_out),
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2.5*cm,
        bottomMargin=2.5*cm,
        title=title,
        author="Leonardo Araya - UBB",
        subject="CIM DEFINITIVO v6.0"
    )
    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Generado: {path_out} ({path_out.stat().st_size/1024/1024:.2f} MB)")

def main():
    styles = get_styles()
    # Informe
    print("Generando Informe Práctica II...")
    informe_path = OUT_DIR / "INFORME_PRACTICA_II_CIM_DEFINITIVO_LEONARDO_ARAYA.pdf"
    elems = []
    elems.extend(cover_page(styles))
    elems.extend(informe_content(styles))
    build_pdf(informe_path, elems, "Informe Practica II - CIM DEFINITIVO - Leonardo Araya - UBB")

    # Tutorial / Manual
    print("Generando Manual / Tutorial...")
    manual_path = OUT_DIR / "MANUAL_TUTORIAL_CIM_DEFINITIVO_LEONARDO_ARAYA.pdf"
    elems2 = []
    # portada manual
    if UBB_LOGO.exists():
        try:
            img = Image(str(UBB_LOGO), width=5*cm, height=5*cm, kind='proportional')
            img.hAlign = 'CENTER'
            elems2.append(img)
        except: pass
    elems2.append(Spacer(1,0.5*cm))
    elems2.append(Paragraph("UNIVERSIDAD DEL BÍO-BÍO<br/>Facultad de Ciencias Empresariales", styles['UBBCenter']))
    elems2.append(Spacer(1,0.8*cm))
    elems2.append(Paragraph("MANUAL DE USUARIO Y TUTORIAL<br/>CIM DEFINITIVO v6.0<br/>Sistema de Manufactura Integrada por Computador", styles['UBBTitle']))
    elems2.append(Spacer(1,0.8*cm))
    data = [
        ["Autor:", "Leonardo Araya Labarca"],
        ["Carrera:", "Ing. de Ejecución en Computación e Informática"],
        ["Versión:", "v6.0 - Pre-hardware 100% automatizable"],
        ["Fecha:", "28 de julio de 2026"],
        ["Repositorio:", "haloharry973/CIM-DEFINITIVO"],
    ]
    t = Table(data, colWidths=[3*cm, 11*cm])
    t.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, colors.HexColor('#e2e8f0')),
    ]))
    elems2.append(t)
    elems2.append(Spacer(1,1*cm))
    elems2.append(Paragraph("Este manual guía la instalación, configuración y operación segura del sistema CIM en modo simulación y prepara el paso a laboratorio con protocolo de seguridad.", styles['UBBNormal']))
    elems2.append(PageBreak())
    elems2.extend(informe_tutorial_content(styles))
    build_pdf(manual_path, elems2, "Manual Tutorial CIM DEFINITIVO v6.0 - Leonardo Araya - UBB")

    # Copias adicionales en deliverables y entrega
    for extra_path in [
        ROOT / "docs" / "deliverables" / "INFORME_PRACTICA_II_CIM_DEFINITIVO.pdf",
        ROOT / "entrega" / "INFORME_PRACTICA_II_CIM_DEFINITIVO.pdf",
    ]:
        extra_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            import shutil
            shutil.copy2(informe_path, extra_path)
            print(f"Copiado a {extra_path}")
        except Exception as e:
            print(f"No se pudo copiar a {extra_path}: {e}")

    for extra_path in [
        ROOT / "docs" / "deliverables" / "MANUAL_TUTORIAL_CIM_DEFINITIVO.pdf",
        ROOT / "entrega" / "MANUAL_TUTORIAL_CIM_DEFINITIVO.pdf",
    ]:
        extra_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            import shutil
            shutil.copy2(manual_path, extra_path)
            print(f"Copiado a {extra_path}")
        except Exception as e:
            print(f"No se pudo copiar a {extra_path}: {e}")

if __name__ == "__main__":
    main()
