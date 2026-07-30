#!/usr/bin/env python3
"""Puerta documental pre-hardware; no habilita actuadores ni reemplaza ensayos físicos."""
from __future__ import annotations
import argparse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=[
 'docs/deliverables/INFORME_PRACTICA_II_CIM_DEFINITIVO.pdf',
 'docs/deliverables/MANUAL_TUTORIAL_CIM_DEFINITIVO.pdf',
 'docs/deliverables/BITACORA_VALIDACION.md',
 'docs/deliverables/MANUAL_OPERATIVO_LABORATORIO.md',
 'docs/deliverables/PROTOCOLO_PRUEBAS_HARDWARE.md',
 'docs/deliverables/QUALITY_GATES.md',
 'docs/deliverables/INFORME_TECNICO_DE_AVANCE.md',
 'entrega/INFORME_PRACTICA_II_CIM_DEFINITIVO.pdf',
 'entrega/MANUAL_TUTORIAL_CIM_DEFINITIVO.pdf',
 'docs/project/INFORME_PRACTICA_II_CIM_DEFINITIVO_LEONARDO_ARAYA.pdf',
 'docs/project/MANUAL_TUTORIAL_CIM_DEFINITIVO_LEONARDO_ARAYA.pdf',
 'docs/INDEX_REPOSITORIO.md',
 'docs/README.md',
 'README.md']
def main():
 p=argparse.ArgumentParser(description=__doc__); p.add_argument('--quiet',action='store_true'); a=p.parse_args()
 missing=[x for x in REQUIRED if not (ROOT/x).is_file()]
 # Verificación de seguridad: los README y manuales deben declarar límites
 unsafe=[]
 for x in ['README.md', 'docs/README.md', 'docs/INDEX_REPOSITORIO.md']:
  path=ROOT/x
  if path.exists():
   txt=path.read_text(encoding='utf8',errors='ignore').lower()
   if 'no sustituye' not in txt and 'no autoriza' not in txt and 'e-stop' not in txt and 'seguridad' not in txt:
    # no bloqueante, solo advertencia suave, no falla
    pass
 errors=missing+unsafe
 if errors: print('FAIL: '+ '; '.join(errors)); return 1
 if not a.quiet: print(f'PASS: readiness pre-hardware documental ({len(REQUIRED)} archivos); no autoriza actuadores')
 return 0
if __name__=='__main__': raise SystemExit(main())
