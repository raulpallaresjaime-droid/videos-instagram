#!/bin/bash
# Como lote.sh, pero antes de cada voz comprueba el saldo de ElevenLabs y PARA si no llega
# (necesario ≈ 0,6 créditos × caracteres del guion, con eleven_v4). Apunta lo gastado de verdad.
cd "$(dirname "$0")/.."
saldo(){ curl -s https://api.elevenlabs.io/v1/user/subscription | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['character_limit']-d['character_count'])"; }
for V in "$@"; do
  echo "== $V"
  if [ ! -f "$V/align.json" ]; then
    chars=$(python3 -c "import json,sys; print(sum(len(s['say'].strip())+1 for s in json.load(open(sys.argv[1]))['scenes']))" "$V/spec.json")
    need=$(( chars * 6 / 10 )); antes=$(saldo)
    if [ -z "$antes" ] || [ "$antes" -lt "$need" ]; then echo "PARO: saldo $antes < necesario $need ($chars caracteres)"; break; fi
    node engine/tts.js "$V" || { echo "FALLO voz $V"; break; }
    despues=$(saldo); echo "SALDO antes $antes · después $despues · gastado $((antes-despues)) por $chars caracteres"
  fi
  node engine/render.js "$V" 2>&1 | grep -v "frame " || echo "FALLO render $V"
  echo "PORTADA $(python3 engine/portada.py "$V")"
done
echo "== LOTE TERMINADO · saldo final $(saldo)"
