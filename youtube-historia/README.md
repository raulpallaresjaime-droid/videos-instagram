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

## Normas de imagen (desde la revisión del capítulo 3)

Raúl: «el audio es un 10/10, pero las imágenes se quedan en suspenso: pocas, algunas repetidas y muchas banales».
Para todo capítulo nuevo (y al rehacer las imágenes de los capítulos 3-8, reutilizando su `audio.mp3` y `align.json`):

1. **Caras.** Cada vez que se nombra a una persona relevante (verdugos y también víctimas y supervivientes con nombre),
   en ese momento aparece su cara (retrato o clip) con un **rótulo de identificación**: nombre y cargo
   («Rudolf Höss · comandante de Auschwitz»). Retratos reutilizables en `personas/` (ver abajo).
2. **Más imágenes, sin repetir para rellenar.** Cambio de imagen cada 6-10 s: una escena de 20 s lleva 2-3 imágenes o
   clips (`imgs`). Una foto o clip solo se repite cuando se vuelve a hablar de ese sitio, hecho o persona (aunque sea
   minutos después), nunca para rellenar. El render avisa con `REPETIDA: …` (también los fondos `bg`): revisar cada aviso.
3. **Imágenes con peso**: caras de presos, niños, familias en los andenes (Álbum de Auschwitz), zapatos, maletas, pelo,
   gafas, barracones, alambradas, supervivientes en la liberación, Núremberg, documentos y órdenes firmadas… Las
   banales (fachadas, paisajes, grupos anónimos) solo de apoyo y en minoría. Revisar con hoja de contactos y sustituir las flojas.
4. **Lo duro, con cuidado.** Imágenes duras (supervivientes muy delgados) si aportan. Lo más explícito (cadáveres) solo
   si es imprescindible, con `blur`, breve, nunca en el primer minuto ni en la miniatura, y con contexto
   (pie de foto). Nada de sangre ni ejecuciones.
5. **Clips** de dominio público, 1 de cada 3-4 escenas, priorizando los que muestran a los personajes (ver abajo).

### Escenas con varias imágenes, rótulos y desenfoque

```json
{"say": "… Reinhard Heydrich reúne a quince altos cargos … Familias enteras bajan a la rampa … Muchos niños …",
 "imgs": [
   {"img": "personas/heydrich.jpg", "cue": "Reinhard Heydrich", "fy": 0.25,
    "who": {"name": "Reinhard Heydrich", "role": "Jefe de la Oficina Central de Seguridad del Reich"}},
   {"img": "img/llegada_hungria.jpg", "cue": "familias enteras", "cap": "Llegada de judíos húngaros · Álbum de Auschwitz, 1944"},
   {"clip": "clips/rampa.mp4", "clipStart": 2, "cue": "muchos ninos"},
   {"img": "img/x.jpg", "blur": true, "cap": "Imagen desenfocada por respeto a las víctimas"}
 ]}
```

- Cada elemento de `imgs` es una ruta (`"img/x.jpg"`, `"clips/y.mp4"`) o un objeto con `img` o `clip` (+ `clipStart`,
  `clipRate`), `kb`, `fx`, `fy`, `cap`, `who`, `blur` y **cuándo entra**: `cue` (palabras del `say`, sin tildes; `n` para la
  2.ª aparición) o `t` (segundos desde el inicio de la escena). Sin `cue`/`t`, se reparten a partes iguales. La primera
  entra con la escena.
- Fundido de 0,8 s entre imágenes y Ken Burns propio en cada una (alterna `in`/`out` si no se indica `kb`).
- `who: {name, role}` → rótulo abajo a la izquierda (a la derecha con `side: "right"`) que entra con la imagen y dura ~7 s.
  Usarlo justo cuando la voz nombra a la persona (`cue` con su nombre).
- `blur: true` = 12 px (norma de Raúl: que se intuya lo que hay sin llegar a verse; si se desenfoca demasiado no se entiende) o un número de píxeles. Para cadáveres amontonados y similares. `cap` de cada imagen = su pie de foto.
- `side`, `shade`, `html` y el `cap` de escena siguen funcionando igual. `img`/`clip` sueltos = una sola imagen (los
  episodios 1-8 se renderizan igual que antes).
- Rutas: primero en la carpeta del episodio y, si no existen, en `youtube-historia/` (`personas/…`).
- Prueba: `videos/_prueba_imagenes/` (rótulo + escena de 3 imágenes + imagen desenfocada, voz falsa).

### Biblioteca de retratos (`personas/`)

- `personas/<nombre>.jpg` + `personas/creditos.txt` + `personas/personas.json` (`name`, `role` y `fx`/`fy` de la cara
  para encuadrar). Solo licencias libres: Bundesarchiv (`engine/bundesarchiv.py search "Name Porträt"` / `get`, CC BY-SA 3.0 DE),
  Wikimedia Commons (dominio público: fotos de NARA, de los juicios, del Álbum Höcker…). Para descargar un archivo de
  Commons sin gastar API: `curl -A 'HistoriaDocBot/1.0' "$(python3 engine/commons.py vurl 'File:…')"`.
- Para no repetir la misma cara cada vez que sale alguien, guardar **varios retratos** de los personajes que salen mucho
  (`hitler.jpg`, `hitler_1938.jpg`, `hitler_bunker.jpg`…) y añadir a la biblioteca cada retrato nuevo que se use.
- El cargo del rótulo se adapta al momento del relato (Höss en 1940 = «comandante de Auschwitz»).

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
