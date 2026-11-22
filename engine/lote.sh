#!/bin/bash
# Uso: bash engine/lote.sh videos/carpeta1 videos/carpeta2 ...
# Genera voz (si falta) y vídeo de cada carpeta, una detrás de otra.
cd "$(dirname "$0")/.."
for V in "$@"; do
  echo "== $V"
  [ -f "$V/align.json" ] || node engine/tts.js "$V" || { echo "FALLO voz $V"; continue; }
  node engine/render.js "$V" 2>&1 | grep -v "frame " || echo "FALLO render $V"
done
echo "== LOTE TERMINADO"
