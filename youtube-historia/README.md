# Canal de YouTube de historia · Segunda Guerra Mundial

Documentales de unos 10-12 min en español, sin cara, con la voz «Salva - The Spanish Narrator» de ElevenLabs
(`hyKxCTlAqtnW188CgltM`, modelo `eleven_v4`, estabilidad 0,5, similitud 0,75). Nombre del canal: **Sombras del 39**.
Raúl revisa cada vídeo antes de publicarlo.

## Producir un episodio

```bash
cd youtube-historia/videos/<carpeta>
python3 build_spec.py                                  # guion + escenas → spec.json y guion.txt
python3 ../../engine/commons.py search "texto" 8      # buscar fotos de archivo en Wikimedia Commons
python3 ../../engine/commons.py get "File:..." img/x.jpg   # descargar (apunta el crédito en img/creditos.txt)
cd ../../..
node youtube-historia/engine/tts.js youtube-historia/videos/<carpeta>      # voz → audio.mp3 + align.json
node youtube-historia/engine/render.js youtube-historia/videos/<carpeta> --preview 5,60,120   # fotogramas sueltos
node youtube-historia/engine/render.js youtube-historia/videos/<carpeta>   # → video.mp4 (1920×1080, 30 fps)
node youtube-historia/engine/miniatura.js youtube-historia/videos/<carpeta> # → miniatura.jpg (1280×720)
```

- Wikimedia limita mucho las descargas desde este entorno: `commons.py` respeta sus esperas, así que conviene
  lanzar las descargas en segundo plano al principio.
- Escena con `img` → foto en blanco y negro con movimiento de cámara (`kb`: in, out, left, right, up, still;
  `fx`/`fy` = punto de interés), `side: "right"|"left"` para retratos con texto al lado, `cap` = pie de foto,
  `shade` = oscurecer. Escena sin `img` → fondo oscuro (gráficos, citas, líneas de tiempo).
- Animación sincronizada con la voz igual que en Instagram: clase `in` + `data-cue="palabras"` o `data-t`.
- Datos siempre verificados (USHMM, Bundestag, Britannica, DHM…). Nada de símbolos nazis en la miniatura.

## Episodios propuestos

1. Cómo Hitler llegó al poder sin ganar nunca la mayoría *(piloto)*
2. De Dachau a Auschwitz: cómo nació el sistema de campos de concentración
3. Auschwitz: cómo funcionaba el mayor campo de exterminio nazi
4. La Noche de los cristales rotos (1938)
5. Los españoles de Mauthausen: los republicanos olvidados en un campo nazi
6. 1 de septiembre de 1939: el día que empezó la Segunda Guerra Mundial
7. Toda la Segunda Guerra Mundial explicada en 20 minutos
8. Operación Barbarroja: el mayor error de Hitler
9. Stalingrado: la batalla que cambió la guerra
10. Los últimos días de Hitler en el búnker
