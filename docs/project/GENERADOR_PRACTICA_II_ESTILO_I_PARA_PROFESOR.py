#!/usr/bin/env python3
"""
Generador Informe Práctica II estilo Práctica I, pero con CIM explicado para profesor.
Formato UBB - Leonardo Araya - Para profesor guía
"""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak,
    Table, TableStyle, HRFlowable
)
from reportlab.lib.utils import ImageReader

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "docs" / "assets" / "imagenes"
ASSETS2 = ROOT / "docs" / "assets"
OUT_DIR = ROOT / "docs" / "project"
OUT_DIR.mkdir(parents=True, exist_ok=True)

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
    styles.add(ParagraphStyle(name='UBBTitle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=18, leading=22, alignment=TA_CENTER, spaceAfter=12, textColor=colors.HexColor('#0a2d5c')))
    styles.add(ParagraphStyle(name='UBBSubtitle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=14, leading=18, alignment=TA_CENTER, spaceAfter=10, textColor=colors.HexColor('#1a4a8a')))
    styles.add(ParagraphStyle(name='UBBHeader1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=colors.HexColor('#0a2d5c'), spaceBefore=18, spaceAfter=10, keepWithNext=True))
    styles.add(ParagraphStyle(name='UBBHeader2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=colors.HexColor('#1e4a7a'), spaceBefore=14, spaceAfter=8))
    styles.add(ParagraphStyle(name='UBBHeader3', parent=styles['Heading3'], fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=colors.HexColor('#2c5282'), spaceBefore=10, spaceAfter=6))
    styles.add(ParagraphStyle(name='UBBNormal', parent=styles['Normal'], fontName='Helvetica', fontSize=10.5, leading=15, alignment=TA_JUSTIFY, spaceAfter=8))
    styles.add(ParagraphStyle(name='UBBBullet', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14, leftIndent=20, spaceAfter=4, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='UBBCenter', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14, alignment=TA_CENTER, spaceAfter=6))
    styles.add(ParagraphStyle(name='UBBsmall', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=12, alignment=TA_CENTER, textColor=colors.HexColor('#4a5568')))
    styles.add(ParagraphStyle(name='CodeStyle', parent=styles['Normal'], fontName='Courier', fontSize=8.5, leading=11, leftIndent=12, rightIndent=12, backColor=colors.HexColor('#f7fafc'), borderColor=colors.HexColor('#e2e8f0'), borderWidth=0.5, borderPadding=(6,6,6,6), spaceAfter=10))
    styles.add(ParagraphStyle(name='QuoteStyle', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=10, leading=14, leftIndent=20, rightIndent=20, backColor=colors.HexColor('#ebf8ff'), borderColor=colors.HexColor('#90cdf4'), borderWidth=0.5, borderPadding=(8,8,8,8), spaceAfter=10, alignment=TA_JUSTIFY))
    return styles

def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#2c5282'))
    canvas.setLineWidth(0.8)
    canvas.line(doc.leftMargin, doc.height + doc.topMargin + 5, doc.width + doc.leftMargin, doc.height + doc.topMargin + 5)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor('#718096'))
    canvas.drawCentredString(A4[0]/2, 20, f"Página {doc.page}")
    canvas.setFont('Helvetica-Bold', 7)
    canvas.drawString(doc.leftMargin, 20, "Practica II estilo Practica I - CIM para Profesor - Leonardo Araya")
    canvas.drawRightString(doc.width + doc.leftMargin, 20, "Universidad del Bío-Bío - IECI")
    canvas.restoreState()

def cover_page(styles):
    elems = []
    if UBB_LOGO.exists():
        try:
            img = Image(str(UBB_LOGO), width=5*cm, height=5*cm, kind='proportional')
            img.hAlign='CENTER'
            elems.append(img)
        except: pass
    elems.append(Spacer(1,0.5*cm))
    elems.append(Paragraph("UNIVERSIDAD DEL BÍO-BÍO", styles['UBBSubtitle']))
    elems.append(Paragraph("Facultad de Ciencias Empresariales<br/>Escuela de Ingeniería de Ejecución en Computación e Informática", styles['UBBCenter']))
    elems.append(Spacer(1,0.6*cm))
    elems.append(HRFlowable(width="80%", thickness=1, color=colors.HexColor('#2c5282'), spaceBefore=4, spaceAfter=8, hAlign='CENTER'))
    elems.append(Spacer(1,0.6*cm))
    # Título estilo Practica I
    elems.append(Paragraph("INFORME DE PRÁCTICA PROFESIONAL II<br/>(Formato Práctica I adaptado)<br/><br/>Proyecto CIM DEFINITIVO v6.0<br/>Explicado para Profesor Guía", styles['UBBTitle']))
    elems.append(Spacer(1,1*cm))
    data = [
        ["Estudiante:", "Leonardo Araya Labarca"],
        ["RUT:", "—"],
        ["Carrera:", "Ing. de Ejecución en Computación e Informática (29037)"],
        ["Profesor Guía UBB:", "Depto. Sistemas de Información - UBB"],
        ["Profesor Supervisor:", "Laboratorio CIM - UBB"],
        ["Empresa / Lugar:", "Laboratorio CIM - Universidad del Bío-Bío, Concepción"],
        ["Periodo Práctica II:", "10 de marzo al 28 de julio de 2026"],
        ["Horas Totales:", "240 horas (cronología reconstruida)"],
        ["Fecha Entrega:", "30 de julio de 2026"],
        ["Concepción - Chile", "2026"],
    ]
    t = Table(data, colWidths=[4.2*cm, 10*cm])
    t.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-2), 'Helvetica-Bold'),
        ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9.5),
        ('ALIGN', (0,0), (0,-1), 'RIGHT'),
        ('ALIGN', (1,0), (1,-1), 'LEFT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('LINEBELOW', (0,0), (-1,-2), 0.25, colors.HexColor('#e2e8f0')),
        ('ALIGN', (0,-1), (-1,-1), 'CENTER'),
        ('SPAN', (0,-1), (-1,-1)),
    ]))
    elems.append(t)
    elems.append(Spacer(1,1.2*cm))
    elems.append(Paragraph("Informe redactado en estilo Práctica I, con lenguaje pedagógico para explicar el sistema CIM a un profesor no especialista en el detalle de implementación. Incluye marco teórico, analogías y justificación académica.", styles['UBBsmall']))
    elems.append(PageBreak())
    return elems

def contenido(styles):
    elems = []

    # INDICE estilo Practica I
    elems.append(Paragraph("ÍNDICE", styles['UBBHeader1']))
    indice = [
        "I. Introducción ................................................................................................. 3",
        "II. Objetivos de la Práctica ................................................................................ 4",
        "III. Descripción de la Empresa / Laboratorio .......................................................... 5",
        "IV. Marco Teórico: ¿Qué es CIM y por qué importa? .............................................. 6",
        "    4.1 Origen de CIM (80s) y evolución a Industria 4.0",
        "    4.2 Analogía simple: CIM como orquesta sinfónica",
        "    4.3 Componentes de un CIM moderno",
        "V. Descripción General del Proyecto CIM DEFINITIVO ........................................ 9",
        "    5.1 Antes vs. Después (problema y solución)",
        "    5.2 Arquitectura en lenguaje para profesor",
        "    5.3 Las 5 estaciones explicadas como puestos de trabajo",
        "VI. Metodología de Trabajo ............................................................................... 13",
        "VII. Desarrollo de la Práctica: Actividades Realizadas ........................................ 14",
        "VIII. Conocimientos Aplicados y Aprendizajes ..................................................... 17",
        "IX. Explicación Técnica Pedagógica (para profesor) ................................................ 18",
        "    9.1 ¿Cómo hablan las máquinas entre sí? (protocolo)",
        "    9.2 ¿Cómo sabe el sistema quién es quién? (identidad UUID)",
        "    9.3 ¿Cómo no se equivoca? (máquina de estados + visión conservadora)",
        "    9.4 ¿Por qué no se prueba con hardware real aún? (seguridad)",
        "X. Resultados Obtenidos ................................................................................... 22",
        "XI. Dificultades Encontradas y Soluciones ....................................................... 24",
        "XII. Conclusiones ............................................................................................ 25",
        "XIII. Bibliografía ............................................................................................. 26",
        "XIV. Anexos ................................................................................................... 27",
    ]
    for line in indice:
        elems.append(Paragraph(line, styles['UBBNormal']))
    elems.append(PageBreak())

    # I Introduccion estilo Practica I
    elems.append(Paragraph("I. INTRODUCCIÓN", styles['UBBHeader1']))
    elems.append(Paragraph(
        "El presente informe corresponde a la Práctica Profesional II de la carrera de Ingeniería de Ejecución en Computación e Informática de la Universidad del Bío-Bío, "
        "realizada por el estudiante Leonardo Araya Labarca en el Laboratorio CIM de la misma universidad, entre el 10 de marzo y el 28 de julio de 2026, completando 240 horas de dedicación.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "A diferencia de la Práctica I, donde el foco estuvo en el levantamiento de requerimientos y el conocimiento de la organización, "
        "la Práctica II exige aplicar conocimientos de ingeniería en un proyecto real, proponer mejoras y dejar resultados verificables. "
        "En este caso, el proyecto fue <b>CIM DEFINITIVO v6.0</b>, un sistema de manufactura integrada que busca modernizar la celda de producción del laboratorio, "
        "antes controlada por PLCs heterogéneos y software desactualizado.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "Este informe está redactado <b>en formato Práctica I</b> como solicitó el profesor guía: lenguaje claro, estructura tradicional de práctica (empresa, objetivos, actividades, aprendizajes), "
        "pero incorporando un capítulo especial de <b>explicación pedagógica del CIM para un profesor</b>, donde se usan analogías y ejemplos cotidianos para que cualquier docente, "
        "incluso sin especialidad en manufactura, comprenda qué se hizo y por qué importa.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "El alcance de esta práctica es <b>pre-hardware 100% automatizable</b>: todo el software se valida automáticamente con integración continua, sin energizar robot, láser, cinta ni relés. "
        "Las pruebas físicas quedan para tesis, con protocolo de seguridad y E-Stop independiente.",
        styles['UBBNormal']))
    elems.append(PageBreak())

    # II Objetivos
    elems.append(Paragraph("II. OBJETIVOS DE LA PRÁCTICA", styles['UBBHeader1']))
    elems.append(Paragraph("Objetivo General (formato Práctica I):", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Aplicar los conocimientos adquiridos durante la carrera en un entorno real de laboratorio, desarrollando e implementando una solución de software que integre hardware de manufactura, "
        "dejando una plataforma reproducible, trazable y validable automáticamente, y documentando el proceso para futuras generaciones de estudiantes.",
        styles['UBBNormal']))
    elems.append(Paragraph("Objetivos Específicos:", styles['UBBHeader2']))
    objs = [
        "Conocer la organización del Laboratorio CIM, sus equipos (cinta, robot Scorbot ER-VII, láser, cámara, rack) y sus riesgos.",
        "Analizar el sistema antiguo y proponer una arquitectura moderna basada en Android (Kotlin) y ESP32, separando responsabilidades por estaciones.",
        "Implementar identidad de estaciones con UUID canónico, para que el sistema sepa quién es quién y bloquee intrusos (como un guardia que pide carnet).",
        "Desarrollar un protocolo simple de comunicación que permita a las 5 estaciones hablar con el coordinador sin enredarse.",
        "Crear una máquina de estados que impida que un pallet salte de la cinta al almacén sin pasar por calidad (como impedir que un alumno pase de ramo sin prueba).",
        "Lograr compilación automática 100% verde en GitHub Actions (testAllModules, lintAll, buildAllApks) con 6 APKs y checksums.",
        "Documentar todo en formato académico UBB, con bitácora, Quality Gates y manuales de seguridad, diferenciando validación automática de validación física.",
    ]
    for o in objs:
        elems.append(Paragraph(f"• {o}", styles['UBBBullet']))
    elems.append(PageBreak())

    # III Empresa
    elems.append(Paragraph("III. DESCRIPCIÓN DE LA EMPRESA / LABORATORIO", styles['UBBHeader1']))
    elems.append(Paragraph("Universidad del Bío-Bío:", styles['UBBHeader2']))
    elems.append(Paragraph(
        "La Universidad del Bío-Bío es universidad estatal, acreditada 5 años hasta 2030, nivel avanzado. La carrera IECI (Ing. Ejecución en Computación e Informática) se imparte en Facultad de Ciencias Empresariales, sede Concepción, "
        "acreditada 6 años, con consejo asesor externo. Cuenta con laboratorios de redes, desarrollo y manufactura. "
        "El Laboratorio CIM es un espacio semi-industrial donde los estudiantes aprenden automatización.",
        styles['UBBNormal']))
    elems.append(Paragraph("Laboratorio CIM (como empresa):", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Piense en el laboratorio como una pequeña fábrica de 5 puestos: (1) Coordinación es la oficina del jefe que autoriza, (2) PLC es la cinta que mueve cajas, (3) Manufactura es el brazo robótico que marca con láser, "
        "(4) Calidad es el inspector con lupa (cámara) que dice si pasa o no, (5) Almacén es la bodega con estanterías. "
        "Cada puesto tenía su propio control antiguo, sin hablar entre sí. Mi trabajo fue hacer que hablen el mismo idioma y que el jefe pueda ver todo desde una tablet.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "Organización: operador (estudiante que ejecuta), supervisor (profesor que autoriza y vigila E-Stop), encargado de laboratorio (seguridad eléctrica). "
        "Todo queda registrado en bitácora con fecha, commit, versión.",
        styles['UBBNormal']))
    elems.append(PageBreak())

    # IV Marco Teorico CIM explicado para profesor
    elems.append(Paragraph("IV. MARCO TEÓRICO: ¿QUÉ ES CIM Y POR QUÉ IMPORTA? (Explicado para profesor)", styles['UBBHeader1']))
    elems.append(Paragraph("4.1 Origen de CIM (años 80) y evolución a Industria 4.0", styles['UBBHeader2']))
    elems.append(Paragraph(
        "CIM (Computer Integrated Manufacturing) nació en los 80 cuando las fábricas quisieron que diseño (CAD), planificación (MRP) y producción (robots, cintas) se comunicaran por computador. "
        "Antes, cada máquina era una isla. CIM propuso un archipiélago conectado. Hoy, con Industria 4.0, CIM se combina con IoT, visión artificial y móviles. "
        "Nuestro proyecto es un CIM a escala laboratorio, pero con tecnologías actuales: Android en vez de PLCs viejos, BLE en vez de cables serie, YOLO (inteligencia artificial) en vez de inspección manual.",
        styles['UBBNormal']))
    elems.append(Paragraph("4.2 Analogía simple: CIM como orquesta sinfónica", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Imagine una orquesta: cada músico (estación) sabe tocar su instrumento, pero necesita partitura y director. "
        "CIM DEFINITIVO: Coordinador es el director (lleva el tiempo, autoriza quién toca), PLC es la percusión que marca el ritmo de entrada de pallets, "
        "Manufactura es el solista que hace el trabajo fino, Calidad es el afinador que dice si está bien, Almacén es el archivero que guarda partituras. "
        "Sin director, cada músico toca a destiempo. Sin protocolo, se pisan. Nuestro protocolo es la partitura común.",
        styles['UBBNormal'],))
    elems.append(Paragraph(
        "<b>Para el profesor:</b> Si usted ha dirigido tesis o prácticas, sabe que lo difícil no es que un alumno haga su parte, sino que todos entreguen a tiempo y sin copiar. CIM hace lo mismo: orquesta entregas.",
        styles['QuoteStyle']))
    elems.append(Paragraph("4.3 Componentes de un CIM moderno (en palabras simples)", styles['UBBHeader2']))
    comps = [
        "<b>Sensores y actuadores:</b> ojos y manos (sensor GPIO34 detecta pallet, relé GPIO5 mueve cinta, robot mueve brazo, láser marca).",
        "<b>Controladores:</b> cerebro chico (ESP32/Wemos) que habla BLE con tablet.",
        "<b>Supervisión:</b> tablet Android que muestra estado y autoriza (mucho más barato y visual que PLC industrial de $5000).",
        "<b>Red:</b> dos capas: BLE (campo, corta distancia, bajo consumo) + Wi-Fi/TCP (supervisión, larga distancia). Como hablar en voz baja con el compañero y gritar al jefe.",
        "<b>Software:</b> 6 apps Android + Wear + core-network (biblioteca común, como reglamento interno).",
        "<b>Visión:</b> cámara + ArUco (marcadores como QR) + YOLO (detesta piezas). Decisión conservadora: si duda, pide revisión humana, no aprueba automático (como profesor que prefiere segunda corrección).",
    ]
    for c in comps:
        elems.append(Paragraph(f"• {c}", styles['UBBBullet']))

    elems.append(PageBreak())

    # V Descripcion general CIM DEFINITIVO
    elems.append(Paragraph("V. DESCRIPCIÓN GENERAL DEL PROYECTO CIM DEFINITIVO", styles['UBBHeader1']))
    elems.append(Paragraph("5.1 Antes vs. Después", styles['UBBHeader2']))
    data = [
        ["Aspecto", "Antes (legacy)", "Después (CIM DEFINITIVO v6.0)"],
        ["Control", "PLCs heterogéneos, software viejo", "Android Kotlin + ESP32, código abierto"],
        ["Comunicación", "Cables serie, sin estándar", "BLE MTU 20 + TCP, protocolo texto ID|TIMESTAMP|..."],
        ["Identidad", "Sin verificación", "UUID canónico, MAC, capacidades, bloqueo persistente"],
        ["UI", "Consola texto", "Material 3, visualización arcade, Wear OS"],
        ["Visión", "Manual", "CameraX + ArUco + YOLO bestMH.pt, decisión REVIEW_REQUIRED"],
        ["Trazabilidad", "Papel", "GitHub Actions CI verde, SHA256SUMS, bitácora"],
        ["Seguridad", "Software único control", "E-Stop físico independiente, interlocks, semáforo"],
    ]
    t = Table(data, colWidths=[2.5*cm,5.5*cm,6.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.4, colors.grey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7fafc')]),
    ]))
    elems.append(t)
    elems.append(Spacer(1,0.4*cm))

    elems.append(Paragraph("5.2 Arquitectura en lenguaje para profesor", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Piense en 3 pisos: planta baja (campo) con Wemos que tocan sensores/actuadores, primer piso con tablets que traducen BLE a Wi-Fi, segundo piso con Coordinador que orquesta. "
        "Wear OS es el balcón desde donde el jefe mira sin bajar. Todo validado con 12 checks automáticos (validate_system_100.py) que revisan que nada falte, como lista de asistencia.",
        styles['UBBNormal']))
    if IMG_ARQ.exists():
        try:
            im = Image(str(IMG_ARQ), width=16*cm, height=9*cm, kind='proportional')
            im.hAlign='CENTER'
            elems.append(im)
            elems.append(Paragraph("Figura 1: Arquitectura CIM v6.0 explicada visualmente (3 capas)", styles['UBBsmall']))
        except: pass

    elems.append(Paragraph("5.3 Las 5 estaciones explicadas como puestos de trabajo", styles['UBBHeader2']))
    estaciones = [
        ["<b>Coordinador</b> (jefe de producción)", "Hub TCP puerto 8888, autoriza, orquesta, muestra dashboard. APP ID: com.industria.coordinacion"],
        ["<b>PLC</b> (operario cinta)", "Detecta pallet por GPIO34, envía PALLET_ARRIVED. Como guardia que avisa llegó camión. APP ID: com.industria.plc"],
        ["<b>Manufactura</b> (tornero + soldador)", "Robot Scorbot 5 GDL + láser. G-code como receta. En simulación solo telemetría, sin mover. APP ID: com.industria.manufactura"],
        ["<b>Calidad</b> (inspector)", "Cámara + ArUco + YOLO. Si confianza < umbral, REVIEW_REQUIRED, no PASS automático. Como profesor que pide recorrección. APP ID: com.industria.calidad"],
        ["<b>Almacén</b> (bodeguero)", "Rack 3x6, guarda/recupera por ID. Trazable. APP ID: com.industria.almacenamiento"],
        ["<b>Wear</b> (supervisor con smartwatch)", "Solo mira, no controla seguridad. Como apoderado mirando por ventana."],
    ]
    for title, desc in estaciones:
        elems.append(Paragraph(f"• {title}: {desc}", styles['UBBBullet']))

    if IMG_FLUJO.exists():
        try:
            im = Image(str(IMG_FLUJO), width=15*cm, height=8*cm, kind='proportional')
            im.hAlign='CENTER'
            elems.append(im)
            elems.append(Paragraph("Figura 2: Flujo pallet IDLE→MOVING→PROCESSING→QUALITY→STORAGE", styles['UBBsmall']))
        except: pass
    elems.append(PageBreak())

    # VI Metodologia
    elems.append(Paragraph("VI. METODOLOGÍA DE TRABAJO", styles['UBBHeader1']))
    elems.append(Paragraph(
        "Metodología ágil simple, estilo Práctica I: cada semana planificaba con profesor, ejecutaba, validaba automático, registraba en bitácora. "
        "Como hacer tesis: no avanzar sin commit verde. Pasos: feature branch → pruebas locales (validate_firmware_contract, validate_system_100, prehardware_readiness, compileall, git diff) → push → CI (testAllModules, lintAll, buildAllApks) → merge solo si verde.",
        styles['UBBNormal']))
    elems.append(Paragraph("Cronograma 10 mar – 14 jul 2026 (240h):", styles['UBBHeader2']))
    cron = [
        ["10–16 mar", "14", "Conocer lab, levantar problema, definir 5 estaciones"],
        ["17–23 mar", "14", "Investigar arquitecturas CIM, decidir BLE+TCP"],
        ["24–30 mar", "14", "Diseñar identidad UUID, capacidades"],
        ["31 mar–6 abr", "14", "Máquina estados pallet (evitar saltos imposibles)"],
        ["7–13 abr", "14", "PLC/cinta/sensor"],
        ["14–20 abr", "14", "Manufactura robot/G-code"],
        ["21–27 abr", "14", "Calidad cámara/ArUco/YOLO"],
        ["28 abr–4 may", "14", "Almacén rack"],
        ["5–11 may", "14", "BLE framing MTU 20"],
        ["12–18 may", "14", "Admisión/bloqueo nodos"],
        ["19–25 may", "14", "Simuladores hub/visión 1000 casos"],
        ["26 may–1 jun", "14", "YOLO bestMH.pt inspección/export"],
        ["2–8 jun", "14", "Gradle CI APKs + SHA256"],
        ["9–15 jun", "14", "Corrección Kotlin PLC/Calidad bloqueantes"],
        ["16–22 jun", "14", "Documentación limpia (esta limpieza)"],
        ["23–29 jun", "12", "Riesgos, seguridad, E-Stop"],
        ["30 jun–14 jul", "18", "Generación informes UBB + tutorial"],
    ]
    t = Table([["Periodo","Horas","Actividad"]]+cron, colWidths=[2.2*cm,1*cm,11.3*cm])
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

    # VII Desarrollo
    elems.append(Paragraph("VII. DESARROLLO DE LA PRÁCTICA: ACTIVIDADES REALIZADAS", styles['UBBHeader1']))
    elems.append(Paragraph("Formato Práctica I: relato semanal con logros y problemas.", styles['UBBNormal']))
    acts = [
        "<b>Semana 1-2 (mar):</b> Reunión profesor, definir alcance 5 estaciones. Problema: profesor dudaba hardware real vs simulación. Solución: definir pre-hardware 100% automatizable sin actuadores.",
        "<b>Semana 3-4 (mar):</b> Diseño UUID canónico, política admisión. Analogía carnet universitario: sin UUID válido no entra a lab.",
        "<b>Abril:</b> Implementación PLC (sensor GPIO34) y Manufactura (G-code). Bloqueante: Kotlin null safety en PLC. Solución: logs + constante duplicada corregida commit cb41ef4.",
        "<b>Abril-mayo:</b> Calidad CameraX/ArUco. Bloqueante: CameraX lifecycle. Commit 069a0b1. Solución: desacoplar prueba G-code de OpenCV/Bitmap (340f54a).",
        "<b>Mayo:</b> BLE framing MTU 20, fragmentación/reensamblado. Problema: mensajes partidos se perdían. Solución: buffer + timeout, commits f2d9e35.",
        "<b>Mayo-junio:</b> Bloqueo persistente dispositivos (4677ee1), Quality Gates (2e6f0c3), simuladores hub/vision 1000 casos.",
        "<b>Junio:</b> CI verde: testAllModules, lintAll, buildAllApks, validateApks, writeApkChecksums. Logs: 6 APKs + SHA256SUMS.txt en config/output-apks/.",
        "<b>Junio-julio:</b> Documentación, auditoría técnica, limpieza repo (eliminar 76 archivos duplicados, 19MB bestMH.pt triplicado).",
        "<b>Julio:</b> Generación PDFs UBB con reportlab, logo oficial, validación 12/12 PASS.",
    ]
    for a in acts:
        elems.append(Paragraph(f"• {a}", styles['UBBBullet']))
    elems.append(Paragraph("Comandos ejecutados antes de cada entrega:", styles['UBBHeader2']))
    elems.append(Paragraph("python3 tools/validate_firmware_contract.py --quiet<br/>python3 tools/validate_system_100.py --quiet  # 12/12 PASS<br/>python3 tools/prehardware_readiness.py --quiet<br/>python3 -m compileall -q tools<br/>git diff --check<br/>cd config && ./gradlew testAllModules lintAll buildAllApks", styles['CodeStyle']))
    elems.append(PageBreak())

    # VIII Conocimientos aplicados
    elems.append(Paragraph("VIII. CONOCIMIENTOS APLICADOS Y APRENDIZAJES", styles['UBBHeader1']))
    elems.append(Paragraph("Asignaturas aplicadas:", styles['UBBHeader2']))
    for mat in ["<b>Programación Avanzada:</b> Kotlin, corrutinas, ViewModel, pruebas JVM.", "<b>Redes:</b> TCP 8888, BLE GATT, MTU, reconexión.", "<b>Sistemas Embebidos:</b> ESP32, GPIO34 sensor, GPIO5 relé, estado seguro arranque.", "<b>Visión Artificial:</b> CameraX, ArUco, YOLO bestMH.pt, decisión conservadora.", "<b>Ingeniería Software:</b> CI, lint, Gradle, Git branching, bitácora.", "<b>Seguridad Industrial:</b> E-Stop independiente, interlocks, semáforo verde/ámbar/rojo."]:
        elems.append(Paragraph(f"• {mat}", styles['UBBBullet']))
    elems.append(Paragraph("Aprendizajes personales (formato Práctica I):", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Aprendí que lo difícil no es que el código compile, sino que sea trazable y seguro. En Práctica I pensé que bastaba entregar. En Práctica II entendí que hay que decir qué NO se probó. "
        "También que un repo limpio vale tanto como código: eliminé 76 archivos y el proyecto pasó de desordenado a presentable, manteniendo 12/12 PASS.",
        styles['UBBNormal']))
    elems.append(PageBreak())

    # IX Explicacion pedagogica para profesor
    elems.append(Paragraph("IX. EXPLICACIÓN TÉCNICA PEDAGÓGICA (PARA PROFESOR)", styles['UBBHeader1']))
    elems.append(Paragraph("Este capítulo es la esencia de 'explicado para un profesor': sin jerga innecesaria, con analogías.", styles['UBBNormal']))

    elems.append(Paragraph("9.1 ¿Cómo hablan las máquinas entre sí? (protocolo)", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Como en un colegio: cada mensaje lleva <b>quién envía, a quién, qué quiere, con qué prioridad</b>. Formato: ID|TIMESTAMP|SOURCE_MAC|SOURCE_APP|DEST_MAC|DEST_APP|CMD|PRIORITY|SESSION|PAYLOAD. "
        "Ejemplo real: PLC_001|2026-07-28T10:00:00Z|AA:BB:CC:DD:EE:01|com.industria.plc|...|PALLET_ARRIVED|HIGH|SESS_123|{sensor:1}. "
        "Es como un correo con asunto, remitente, destinatario y cuerpo. El coordinador es el director que lee todos los correos y decide.",
        styles['UBBNormal']))
    elems.append(Paragraph("9.2 ¿Cómo sabe el sistema quién es quién? (identidad UUID)", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Cada estación tiene carnet: MAC (como RUT), UUID canónico (como código de carrera CIM-ST-ALM-X1), tipo (PLC, MANUF...), capacidades (qué sabe hacer). "
        "StationIdentityPolicy es el guardia: si carnet no coincide con lista permitida, bloquea persistente (no deja entrar más, como alumno expulsado). "
        "Token de emparejamiento viaja como SHA-256 (huella digital, no contraseña en claro), como guardar hash de clave, no la clave.",
        styles['UBBNormal']))

    elems.append(Paragraph("9.3 ¿Cómo no se equivoca? (máquina de estados + visión conservadora)", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Máquina de estados pallet impide transiciones imposibles: no puede ir de STORAGE a PROCESSING sin pasar por QUALITY, como no puede pasar de ramo sin prueba. "
        "Pruebas JVM bloquean esos saltos. Visión conservadora: si YOLO tiene baja confianza, devuelve REVIEW_REQUIRED, no PASS. "
        "Es como profesor que prefiere pedir segunda oportunidad antes que aprobar dudoso. Simulador vision_safety_simulator.py prueba 1000 casos raros.",
        styles['UBBNormal']))

    elems.append(Paragraph("9.4 ¿Por qué no se prueba con hardware real aún? (seguridad)", styles['UBBHeader2']))
    elems.append(Paragraph(
        "Porque mover robot Scorbot, cinta o láser sin E-Stop independiente puede causar daño. En Práctica II definimos semáforo: "
        "Verde = estructura OK, Ámbar = falta inspección eléctrica, Rojo = no autorizado hasta acta firmada. "
        "Es como práctica de química: no enciendes mechero sin gafas y supervisor. Nuestra entrega es pre-hardware 100% automatizable, no 100% integral.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "Para el profesor: esto enseña a decir 'no sé / no probé' con evidencia, no inventar. En bitácora queda pendiente: BLE multiconexión 2+ ESP32, cámara real, LAN estable, actuadores con E-Stop.",
        styles['QuoteStyle']))

    # Imagenes UI explicadas para profesor
    elems.append(Paragraph("Visuales para profesor (qué ve el operario):", styles['UBBHeader2']))
    for path, title, expl in [
        (IMG_COORD, "Coordinador", "Jefe: ve lista estaciones, autoriza con botón, ve IP/puerto hub"),
        (IMG_PLC, "PLC", "Operario cinta: botón iniciar/detener, evento pallet"),
        (IMG_MANU, "Manufactura", "Tornero: carga G-code, Home, Run simulación"),
        (IMG_CALI, "Calidad", "Inspector: cámara, ArUco, botón Evaluar PASS/FAIL"),
        (IMG_ALMA, "Almacén", "Bodeguero: buscar posición libre, guardar/recuperar"),
        (IMG_BLE, "BLE Connect", "Guardia: lista dispositivos, conectar, ver UUID"),
    ]:
        if path.exists():
            try:
                im = Image(str(path), width=7.5*cm, height=5.5*cm, kind='proportional')
                elems.append(im)
                elems.append(Paragraph(f"Figura: {title} — {expl}", styles['UBBsmall']))
            except: pass
    elems.append(PageBreak())

    # X Resultados
    elems.append(Paragraph("X. RESULTADOS OBTENIDOS", styles['UBBHeader1']))
    elems.append(Paragraph(
        "Resultado principal: plataforma reproducible, CI verde ejecución 30422387003 (commit 3286792), 6 APKs debug + SHA256SUMS.txt. "
        "validate_system_100.py 12/12 PASS local. No se declara hardware probado sin evidencia.",
        styles['UBBNormal']))
    res_table = [
        ["Área", "Evidencia", "Interpretación para profesor"],
        ["Build", "CI verde testAllModules + buildAllApks", "Código compila sin errores, como entregar sin faltas ortográficas"],
        ["Estructura", "12/12 PASS", "Carpeta ordenada, sin archivos basura"],
        ["Firmware contrato", "PASS", "Carnet de cada Wemos coincide con lista"],
        ["UI", "Fuentes androidTest, no CI emulador", "Pantallas existen, falta probar en todos los celulares, como libro sin imprimir"],
        ["Hardware", "Pendiente", "Falta ir a laboratorio, como práctica sin ir a empresa aún"],
    ]
    t = Table(res_table, colWidths=[2*cm,5*cm,7.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.4, colors.grey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7fafc')]),
    ]))
    elems.append(t)
    elems.append(Spacer(1,0.4*cm))
    elems.append(Paragraph("Mejoras concretas verificables:", styles['UBBHeader2']))
    for m in ["Kotlin PLC y Calidad compilando", "UUID + bloqueo persistente", "SHA-256 handshake", "Máquina estados pallet", "Fragmentación BLE MTU 20", "Simuladores 1000 casos", "YOLO bestMH.pt inspección", "Checksums SHA-256 APKs", "Repo limpio 76 archivos menos"]:
        elems.append(Paragraph(f"• {m}", styles['UBBBullet']))
    elems.append(PageBreak())

    # XI Dificultades
    elems.append(Paragraph("XI. DIFICULTADES ENCONTRADAS Y SOLUCIONES", styles['UBBHeader1']))
    probs = [
        ["Kotlin null safety PLC", "Logs NPE, constante duplicada", "Corregir logs, commit cb41ef4"],
        ["CameraX lifecycle", "Cámara negra", "Desacoplar G-code de OpenCV, 069a0b1"],
        ["BLE mensajes partidos", "Pérdida telemetría", "Buffer + timeout, framing, f2d9e35"],
        ["Repo desordenado 114 MB + duplicados", "76 archivos, bestMH.pt x3", "Limpieza y .gitignore, 12/12 PASS mantenido"],
        ["E-Stop no implementado", "Riesgo seguridad", "Semáforo rojo, no autorizar actuadores, manual operativo"],
    ]
    t = Table([["Problema","Causa","Solución"]]+probs, colWidths=[4*cm,4.5*cm,6*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#c53030')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#feb2b2')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#fff5f5')]),
    ]))
    elems.append(t)
    elems.append(PageBreak())

    # XII Conclusiones
    elems.append(Paragraph("XII. CONCLUSIONES", styles['UBBHeader1']))
    elems.append(Paragraph(
        "La Práctica II permitió pasar de un proyecto desordenado a una plataforma presentable y auditable, manteniendo formato Práctica I que el profesor conoce, pero explicando CIM con analogías. "
        "Se logró CI verde, 6 APKs, identidad segura, máquina de estados robusta y documentación que diferencia validación automática de física.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "Aprendizaje clave (formato Práctica I): no basta con que funcione en mi PC; debe compilar en CI, estar documentado y decir qué falta. "
        "La reconstrucción de 240h muestra dedicación en análisis, desarrollo, simulación y limpieza, sin inventar pruebas físicas.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "Para futuro (tesis): ejecutar protocolo HW-01..HW-09 con E-Stop, interlocks, supervisor, captura CIM_ID, BLE multiconexión, cámara real. "
        "Entonces se podrá decir 100% integral, no solo 100% automatizable.",
        styles['UBBNormal']))
    elems.append(Paragraph(
        "Este informe, en estilo Práctica I pero con CIM explicado para profesor, demuestra que el estudiante puede explicar lo técnico en simple, "
        "habilidad clave de ingeniero: traducir orquesta a jefe.",
        styles['QuoteStyle']))

    elems.append(Paragraph("XIII. BIBLIOGRAFÍA", styles['UBBHeader1']))
    for b in ["Universidad del Bío-Bío – Manual marca UBB", "Android Developers – CameraX, BLE, Wear OS, Gradle Lint", "Espressif – ESP32 BLE GATT", "Scorbot ER-VII manual seguridad", "Redmon et al. YOLO", "OpenCV ArUco", "Docs CIM – INSTRUCTIVO, VALIDACION, SAFETY"]:
        elems.append(Paragraph(f"• {b}", styles['UBBBullet']))

    elems.append(Paragraph("XIV. ANEXOS", styles['UBBHeader1']))
    elems.append(Paragraph("Anexo A – Comandos validación (como en Práctica I)", styles['UBBHeader2']))
    elems.append(Paragraph("python3 tools/validate_firmware_contract.py --quiet<br/>python3 tools/validate_system_100.py --quiet  # 12/12<br/>python3 tools/prehardware_readiness.py --quiet<br/>cd config && ./gradlew testAllModules lintAll buildAllApks", styles['CodeStyle']))
    elems.append(Paragraph("Anexo B – Estructura limpia para profesor", styles['UBBHeader2']))
    elems.append(Paragraph("CIM-DEFINITIVO/<br/>├── entrega/ (2 PDFs finales para presentar)<br/>├── docs/project/ (generador + PDFs)<br/>├── docs/deliverables/ (bitácora, quality gates)<br/>├── android/ (5 apps + Wear + core-network) para mejorar<br/>├── esp32/firmware/ (canónico)<br/>├── config/ (Gradle)<br/>└── tools/ (validadores)", styles['CodeStyle']))
    elems.append(Paragraph("Fin – Informe Práctica II estilo Práctica I, CIM explicado para profesor – Leonardo Araya – UBB 2026", styles['UBBCenter']))

    return elems

def build_pdf():
    styles = get_styles()
    out_path = OUT_DIR / "INFORME_PRACTICA_II_ESTILO_PRACTICA_I_CIM_EXPLICADO_PROFESOR_LEONARDO_ARAYA.pdf"
    delivery_path = ROOT / "docs" / "deliverables" / "INFORME_PRACTICA_II_ESTILO_PRACTICA_I_CIM_PARA_PROFESOR.pdf"
    entrega_path = ROOT / "entrega" / "INFORME_PRACTICA_II_ESTILO_PRACTICA_I_CIM_PARA_PROFESOR.pdf"

    elems = []
    elems.extend(cover_page(styles))
    elems.extend(contenido(styles))

    doc = SimpleDocTemplate(str(out_path), pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2.5*cm, bottomMargin=2.5*cm, title="Informe Practica II estilo Practica I - CIM para Profesor - UBB", author="Leonardo Araya - UBB")
    doc.build(elems, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Generado: {out_path} ({out_path.stat().st_size/1024/1024:.2f} MB)")

    import shutil
    for p in [delivery_path, entrega_path]:
        p.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(out_path, p)
        print(f"Copiado a {p}")

if __name__ == "__main__":
    build_pdf()
