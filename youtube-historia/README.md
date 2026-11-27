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

## Clips de vídeo de archivo (desde el episodio 9)

**Regla: 1 escena de cada 3-4 lleva un clip** (imágenes en movimiento) en vez de una foto. Los episodios 1-8 no se tocan.

Fuentes (solo dominio público):
- **Wikimedia Commons** (la que funciona desde aquí): muchas copias de material del Gobierno de EE. UU. —NARA,
  US Army Signal Corps, la serie «Why We Fight» (1942-45), Universal Newsreels (1929-67)—. Comprobar en la ficha
  que la licencia es *Public domain* por ser obra del Gobierno de EE. UU. (o noticiario sin copyright renovado).
- NARA directamente (`catalog.archives.gov`) necesita una clave de su API; archive.org está bloqueado por la red
  del entorno. De momento, todo por Commons.
- **Prohibido**: British Pathé, Getty, AP, Bundesarchiv-Filmothek, Riefenstahl o cualquier material con derechos;
  imágenes explícitas (cadáveres, ejecuciones); propaganda nazi sin contexto (los planos alemanes que aparecen
  dentro de «Why We Fight» se pueden usar como imagen, con el pie de foto que diga de dónde salen).

```bash
python3 engine/commons.py vsearch "Why We Fight" 10          # vídeos: tamaño | duración | licencia | título
U=$(python3 engine/commons.py vurl "File:Why We Fight.2.The Nazis Strike.webm")   # URL sin gastar API
python3 engine/clip.py sheet "$U" 300 360 hoja.jpg 15        # hoja de contactos con el segundo de cada plano
python3 engine/clip.py "$U" 612 12 videos/<carpeta>/clips/acerias.mp4 [fy]   # recorte listo para usar
```

- ffmpeg lee solo el tramo pedido de la película (no la descarga entera). `vsearch` usa la API de Commons, que
  limita mucho: lanzar las búsquedas en segundo plano al principio. `vurl` y `clip.py` no gastan API.
- `clip.py` quita bandas negras, encuadra a 16:9 (4:3 se recorta; `fy` 0-1 elige qué parte vertical se queda),
  1920×1080, 30 fps, sin audio, ≤20 s, ~3-5 MB, y apunta el crédito en `clips/creditos.txt`.
- En el spec, una escena con clip es igual que una con foto, cambiando `img` por `clip`:
  `{"say": "…", "clip": "clips/acerias.mp4", "clipStart": 0, "cap": "Acerías alemanas · «Why We Fight» (1943)"}`.
  `clipStart` = segundo del clip donde empieza (por defecto 0). Si el clip es más corto que la escena se ralentiza
  hasta 0,6× y, si aun así no llega, se congela en el último fotograma (el render avisa): elegir tramos de al menos la
  duración de la escena, o partir la escena. `clipRate` fuerza la velocidad. Vale todo lo de las fotos: mismo filtro
  blanco y negro, viñeta, grano, `cap`, `shade`, `side`, `html` encima; `kb` por defecto es un zoom muy suave.
- El render trocea cada clip en fotogramas (`_clips_cache/`, se borra al acabar) y los avanza en sincronía con el
  tiempo del vídeo, así que funciona igual en `--preview` y en el render en paralelo por tramos.
- Ejemplo de prueba (voz falsa): `videos/_prueba_clips/` (2 fotos + 2 clips de «Why We Fight»).

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
