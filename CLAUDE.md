# Oficina de vídeos de Instagram · @_raulpallares

Reels de finanzas en español (España) con la voz clonada de Raúl. Tres series, tres días:

| Día (10:00 Europe/Madrid) | Serie (`series` en spec) | Kicker de portada |
|---|---|---|
| Martes | `bolsa` · Serie de bolsa | FINANZAS DESDE CERO |
| Jueves | `fondo` · Finanzas a fondo | FINANZAS A FONDO |
| Domingo | `nadie` · Lo que nadie te cuenta | LO QUE NADIE TE CUENTA |

(Elegidos con el mapa de mejores horas de Metricool: jueves, martes y domingo a las 10:00.
Ojo: en `getBestTimeToPostByNetwork`, `dayOfWeek` 1 = domingo.) Se publica también en festivos.

`calendario.json` es la fuente de verdad: fecha, serie, tema y estado de cada publicación
(`pendiente` → `hecho` → `programado` → `publicado`).

## Tarea semanal (se ejecuta sola cada semana)

Objetivo: dejar **las 3 publicaciones de la semana siguiente** (martes, jueves y domingo) listas y
programadas en Metricool **pendientes de la revisión de Raúl**. Raúl solo revisa; nunca hay
que pedirle que haga nada a mano.

1. `npm ci` (solo si no existe `node_modules/`).
2. Para cada publicación de la semana siguiente:
   - `pendiente` → escribir guion + `spec.json`, generar voz, renderizar (ver abajo), escribir `caption.txt`, estado `hecho`.
   - `hecho` → solo programar.
   - Si la fecha no tiene tema en el calendario, elegir un tema nuevo coherente con la serie
     (sin repetir ninguno ya publicado), añadirlo a `calendario.json` y decirlo en el informe.
3. `git add` + commit + `git push` (los vídeos tienen que estar en GitHub ANTES de programar,
   porque Metricool los descarga desde la URL pública).
4. Programar cada vídeo en Metricool (ver "Metricool") y poner estado `programado` con el `plannerUrl`.
5. Commit + push del calendario actualizado.
6. Si alguna publicación del lote tiene campo `aviso` en el calendario, decírselo a Raúl en el informe
   (quiere saberlo para ordenar su Drive).
7. Informe final corto para Raúl: qué se ha programado, enlaces de Metricool, temas nuevos
   propuestos y cualquier dato que no se haya podido verificar.

Si algo falla (ElevenLabs sin caracteres, Metricool rechaza el vídeo, push rechazado…), no
inventar ni publicar nada a medias: dejar el estado como estaba y explicarlo en el informe.

## Norma de Raúl sobre la duración (Instagram y YouTube)
**Nunca acortar un vídeo para ahorrar créditos de ElevenLabs.** La duración la marca el contenido: cada vídeo dura
lo que necesite para contar toda la información relevante (puede ser más corto o más largo que la horquilla si el
tema lo pide). Si el saldo no llega para todos los vídeos previstos a su duración correcta, se hacen **menos vídeos**
y se avisa a Raúl (o se le pregunta antes), nunca se comprimen los guiones para que quepan más.

## Guion

- Español de España, tuteando, frases cortas, tono cercano y didáctico. Ejemplos con números
  sencillos (100 €, 1.000 €, una cafetería inventada «Café Lumen», etc.).
- **Duración: 1:45–2:30 → 1.900–2.500 caracteres** en total (la voz va a ~16,5 caracteres/s).
- Estructura: gancho en forma de pregunta o dato sorprendente (escena oscura) → portada con el
  título (oscura) → 5-8 escenas de explicación en crema → cierre con la idea clave (oscura).
- `nadie`: en la portada se dice «Esto es lo que nadie te cuenta sobre …».
- `bolsa`: nivel cero, para todos los públicos. `fondo`: algo más técnico, pero explicado.
- Cierre con una frase redonda tipo «Porque en bolsa, evitar una gran caída vale más que acertar una gran subida».
- **Datos reales y verificados** con búsqueda web (fuente fiable: J.P. Morgan, Morningstar,
  SPIVA, ESMA, CNMV, Banco de España, INE, informes de empresas…). Nunca inventar cifras.
  Si un dato es aproximado, decirlo («unos», «casi») y poner «datos aproximados» en el subtítulo.
  La fuente va en el `disc` de la escena final.
- Escribir los números en cifras en `say` está bien (la voz los lee bien): «un 5 %», «1.000 euros».
- Siempre: «Contenido educativo, no es recomendación de inversión.» en la escena final.

## spec.json

```json
{
  "series": "nadie",
  "topic": "<span class=\"k\">Lo que</span> <span class=\"c-orange\">nadie te cuenta</span>",
  "title_post": "Título corto",
  "coverScene": 1,
  "scenes": [
    {"dark": true, "say": "Texto que dice la voz en esta escena", "html": "..."},
    {"title": "Hagamos la <em class=\"c-teal\">cuenta</em>", "sub": "opcional", "say": "...", "html": "..."}
  ]
}
```

- `topic` es la cabecera (arriba a la izquierda). Para `bolsa` y `fondo` es el nombre del tema,
  con una palabra en color: `Cuenta de <span class="c-teal">resultados</span>`. Para `nadie`, siempre
  el del ejemplo. `<span class="k">` = color de texto normal (se invierte en escenas oscuras).
- Escena sin `title` → contenido centrado (gancho, portada, cierre). Con `title` → título arriba
  y contenido en `.stage` (`"layout": "stage top"` para pegarlo arriba).
- El texto de todas las `say` seguidas es el guion completo que se manda a ElevenLabs.
- **Animación sincronizada con la voz**: cualquier elemento con clase `in` aparece cuando se
  pronuncia `data-cue="palabras"` (búsqueda sin tildes dentro del `say` de esa escena;
  `data-n="2"` para la 2.ª aparición), o en `data-t="segundos"` desde el inicio de la escena.
  `data-d="0.3"` añade un retraso. Las barras con clase `grow` crecen hasta `--w` / `--h`.
  `data-count="32421" data-fmt=" $"` hace un contador.
- Colores: `c-navy` `c-teal` `c-orange` (en escenas oscuras se aclaran solos). Tipografías:
  Playfair Display (títulos, `<em>` = cursiva de color), Inter (texto), IBM Plex Mono (cifras).
- Componentes (ver `engine/style.css`): `.kicker` `.hero` `.q` `.final` `.disc` `.rule`
  `.pill(.navy|.teal|.orange|.sand|.lg)` `.card(.navy|.teal|.orange|.sand)` con `.lab` + `.val`/`.txt`,
  `.bars > .b > span + i.grow[--w]` (clase `short` si la barra es tan corta que el texto no cabe), `.cols > .c > b + i.grow[--h] + span`,
  `.steps > .step > .n + div(.t,.d)`, `.row` `.col` `.note` `.big` `.arrow` `.label`.
- Ejemplo completo: `videos/2026-12-06_nadie_10-mejores-dias/spec.json`.
- **La primera escena tiene que mostrar algo desde el segundo 0** (`data-t="0"`): en Instagram el
  primer segundo decide si la gente sigue mirando. Nunca empezar con la pantalla vacía.
- Una idea por escena, pocos elementos, que se vayan montando según habla. Revisar siempre el
  resultado con una hoja de fotogramas (ffmpeg `tile`) y corregir solapes o textos cortados.

## Producir un vídeo

```bash
node engine/tts.js videos/<carpeta>      # ElevenLabs → audio.mp3 + align.json
node engine/render.js videos/<carpeta>   # → video.mp4 (1080×1920, 30 fps) + portada.jpg
```

- Voz: «Raúl's voice» `qZBD95GE6BZToWCjEQiK`, modelo **`eleven_v4`**, ajustes de la voz
  (estabilidad 0,5, similitud 0,75). No cambiarlo: es lo que Raúl usa en ElevenLabs.
- La clave de ElevenLabs la inyecta el proxy del entorno `videos-instagram`; no hay variable de entorno.
- Antes de generar la voz, revisar el guion: cada carácter cuesta (plan Creator, 131.000/mes).
  Saldo: `curl -s https://api.elevenlabs.io/v1/user/subscription`.
- **El saldo se renueva el día 3 de cada mes y es compartido con YouTube.** En cada informe decir a Raúl cuántos
  caracteres quedan y, si a pocos días de la renovación sobran, proponerle adelantar vídeos de Instagram para
  aprovecharlos (así no faltan después en meses con mucho YouTube).
- `audio.mp3` y `align.json` se suben al repo: así se puede volver a renderizar (por ejemplo,
  para corregir un texto en pantalla) sin volver a pagar la voz.

## caption.txt (texto de la publicación)

Mismo estilo que los anteriores (ver los `caption.txt` existentes):
gancho con un dato o pregunta + emoji → 2-3 frases → (si hay carrusel: «En mi perfil tienes el
carrusel con la explicación completa 👆») → «Guárdalo y compártelo con quien … 📌» →
5 hashtags (`#finanzaspersonales #bolsa #educacionfinanciera #inversion` + uno del tema;
`nadie` lleva `#loquenadietecuenta`, `fondo` lleva `#finanzasafondo`).

## Metricool

- Marca `_raulpallares`, `blogId` 8071218, Instagram, zona Europe/Madrid.
- URL del vídeo (rama `main`):
  `https://raw.githubusercontent.com/raulpallaresjaime-droid/videos-instagram/main/videos/<carpeta>/video.mp4`
  (la portada no se sube aparte: va como `videoCoverMilliseconds`, ver abajo).
- Tipo `REEL`, `showReelOnFeed: true`, fecha `<fecha>T10:00:00`, texto = `caption.txt`.
- **Portada = un fotograma del propio vídeo** (como hace Raúl), nunca el primero (es oscuro y en el
  perfil se ve negro) ni la portada oscura del título. `python3 engine/portada.py videos/<carpeta>`
  elige la escena crema más visual ya completa, guarda `portada.jpg` e imprime los milisegundos:
  pásalos en `videoCoverMilliseconds` (y no uses `videoThumbnailUrl`). Revisa la portada recortada a
  3:4 (así se ve en el perfil); si sale a medio animar o poco visual, fija `"coverMs"` en el spec.
- Revisión: crear la publicación con `createScheduledPost` y **`"draft": true`** (borrador con
  la fecha y la hora puestas). Raúl la revisa en Metricool y pulsa Programar. Así se hizo con las
  primeras y funciona. **Nunca** crear una publicación que se publique sola sin su revisión.
- Metricool descarga el vídeo de GitHub y lo copia a sus servidores al crear la publicación, así
  que el push tiene que estar hecho antes.
- Comprobar antes con `getScheduledPosts` que esa fecha no tiene ya una publicación (no duplicar).

## Drive

Carpeta `VIDEOS CONTENIDO INSTAGRAM` (id `1-42fjlTA8RPqkQVa5F-3-JirXvTaDQh6`) con subcarpetas
`SERIE DE BOLSA`, `LO QUE NADIE TE CUENTA`, `FINANZAS A FONDO`. El conector de Drive solo sube
archivos de hasta ~3 MB, así que los vídeos viven en GitHub; a Drive solo se suben archivos
pequeños si hace falta (portadas, guiones).

---

# Canal de YouTube «Sombras del 39» (@Sombras.del.39)

Documentales sin cara (diciembre 2026: ~10 min; **desde enero 2027: mini documentales de 15-20 min**, 1 por semana), sobre la Segunda Guerra Mundial y el nazismo (campos, Holocausto, batallas).
Todo vive en `youtube-historia/` (motor, música, efectos, logos) y `youtube-historia/calendario.json` es la fuente
de verdad (`pendiente` → `hecho` → `programado`). Detalle técnico en `youtube-historia/README.md`.

## Títulos, miniaturas y símbolos (normas de Raúl, desde el capítulo 11)
- **Título = [lo que la gente busca en YouTube: evento, lugar o persona importante] + [gancho].** Lo buscable va
  delante («Pearl Harbor: el ataque que Estados Unidos no vio venir», «Así funcionaba Auschwitz: …», «Stalingrado:
  …»). Nunca un gancho suelto sin el nombre del hecho («51 días de cuenta atrás» → «Pearl Harbor: 51 días de cuenta
  atrás»). Siempre veraz y con cifras verificadas. Desde el cap. 11 el título y la miniatura los decide el equipo
  (CEO) sin preguntar a Raúl, siguiendo esta norma.
- **Miniatura:** cara reconocible o imagen con peso, mucho contraste, 2-4 palabras o una cifra grande, coherente con el título.
- **Símbolos nazis:** permitidos en el vídeo cuando aparecen en fotos o clips históricos con contexto (por ejemplo, al
  fondo de un mitin). **Nunca** en la miniatura, ni en los primeros segundos, ni en primer plano sin motivo.

## Tarea semanal (domingo)
Dejar **los episodios de la semana siguiente** (martes y jueves 16:00 Europe/Madrid en diciembre 2026; desde enero
solo martes 16:00) como **borradores en Metricool** para que Raúl los revise. Nunca publicar sin su revisión.
1. `npm ci` si no hay `node_modules/`.
2. Para cada episodio `pendiente` de la semana siguiente (tema en `calendario.json`; si falta, elegir uno coherente
   con la serie y decirlo en el informe): carpeta `youtube-historia/videos/NN_slug/` copiando la estructura del
   episodio anterior (`build_spec.py`, `build_desc.py`).
   - Investigar y **verificar todas las cifras** con búsqueda web (USHMM, Memorial de Auschwitz, Bundestag,
     Britannica, DHM…). Si las fuentes discrepan, usar formulaciones prudentes («unos», «más de», «miles»).
   - Guion: diciembre 8.500-9.500 caracteres (~10-11 min); **desde enero 12.500-16.500 caracteres (15-20 min), 50-65 escenas**
     (a 13,8 car/s). Escenas de 15-25 s, gancho con dato en la escena 0,
     título «Capítulo N» en la 1, cierre en melancolía y anuncio del siguiente capítulo.
   - Fotos: `engine/bundesarchiv.py search/get` (rápido, alta resolución; su servidor `bundesbildarchiv.init-ag.de`
     a veces corta la conexión: elegir otra). Wikimedia (`engine/commons.py`) limita mucho: lanzarlo al principio en
     segundo plano y usar `fallback` en el spec. **Nada de cadáveres ni imágenes explícitas**, y nada de símbolos
     nazis en la miniatura. Revisar siempre las fotos con una hoja de contactos antes de usarlas.
   - **Normas de imagen (revisión de Raúl del cap. 3: «imágenes pocas, repetidas y banales»)**, detalle en
     `youtube-historia/README.md`: (1) cada vez que se nombra a una persona relevante (verdugos, víctimas, supervivientes)
     aparece **su cara con rótulo** `who: {name, role}` («Rudolf Höss · comandante de Auschwitz»), con retratos de la
     biblioteca `youtube-historia/personas/`; (2) **cambio de imagen cada 6-10 s** (`imgs: [...]`, 2-3 por escena de 20 s) y
     **nada de repetir imágenes para rellenar**: una foto o clip solo se repite cuando se vuelve a hablar de ese sitio,
     hecho o persona (aunque sea minutos después); el render avisa `REPETIDA` y hay que revisar cada aviso; (3) imágenes con peso (presos, niños,
     familias en los andenes, zapatos, maletas, barracones, liberación, Núremberg, documentos), las banales en minoría;
     revisar con hoja de contactos y sustituir las flojas; (4) lo más explícito solo si es imprescindible, con `blur` (12 px por defecto: que se intuya sin llegar a verse), breve,
     nunca en el primer minuto ni en la miniatura y con contexto; nada de sangre ni ejecuciones.
   - **Clips de vídeo (desde el episodio 9): 1 escena de cada 3-4 con `clip`** en vez de foto, priorizando los que muestran a los personajes (noticiarios con Hitler o Göring, juicios de Núremberg…). Solo dominio público:
     películas del Gobierno de EE. UU. (NARA, US Army Signal Corps, «Why We Fight», Universal Newsreels) copiadas en
     Wikimedia Commons. Nada de British Pathé, Getty, Bundesarchiv-Filmothek ni Riefenstahl; nada explícito (cadáveres,
     ejecuciones) ni propaganda nazi sin contexto. Flujo: `commons.py vsearch "texto"` → `commons.py vurl "File:…"` →
     `clip.py sheet <url> <inicio> <dur> hoja.jpg 10` (elegir tramo mirando la hoja) → `clip.py <url> <inicio> <dur>
     clips/x.mp4` (lee solo ese tramo, ≤20 s, 1920×1080, sin audio, apunta el crédito). Detalle en `youtube-historia/README.md`.
   - **Títulos y miniaturas que enganchen** (norma de Raúl): el título NO resume el vídeo, es un gancho que da ganas de
     hacer clic (curiosidad, dato impactante, pregunta), siempre veraz y sin sensacionalismo falso. La miniatura lo
     complementa sin repetirlo: la cara de un personaje, un dato enorme, contraste fuerte, pocas palabras; nunca
     símbolos nazis ni nada explícito. Proponer título + 1 alternativa + idea de miniatura y esperar el visto bueno.
   - Nombres con letras no españolas (ł, ż, ś…): sin ellas en `say` y en los títulos (la tipografía no las tiene).
   - `node youtube-historia/engine/tts.js <carpeta>` (voz Salva `hyKxCTlAqtnW188CgltM`, `eleven_v4`).
   - Revisar con `render.js <carpeta> --preview t1,t2,…` (un fotograma por escena) y corregir solapes/huecos.
   - `node youtube-historia/engine/render.js <carpeta>` (~30 min, mezcla voz + música + tecleo) y
     `node youtube-historia/engine/miniatura.js <carpeta>`; `python3 build_desc.py`.
   - Comprimir para GitHub (<100 MB): `ffmpeg -i video.mp4 -c:v libx264 -preset slow -crf 27 -c:a aac -b:a 160k -movflags +faststart youtube.mp4`.
     Si pasa de 100 MB (clips y grano comprimen peor), usar H.265: `ffmpeg -i video.mp4 -c:v libx265 -preset medium -crf 28 -tag:v hvc1 -c:a aac -b:a 160k -movflags +faststart youtube.mp4`.
3. `git add` + commit + push (Metricool descarga `youtube.mp4` y `miniatura.jpg` de raw.githubusercontent.com).
4. Metricool (`blogId` 8071218; plan gratuito: el YouTube de la marca _raulpallares es Sombras del 39). Si la sesión
   no tiene las herramientas de Metricool, enviar carpeta + fecha + hora de cada vídeo con `send_message` a la sesión
   `session_011oL6uVdD4Dku2QrjEGuJmH`, que crea los borradores:
   comprobar con `getScheduledPosts` que no hay ya vídeo ese día; `createScheduledPost` con `"draft": true`,
   `providers: [{"network":"youtube"}]`, `videoThumbnailUrl` = miniatura, texto = descripción, y
   `youtubeData: {title, type:"video", privacy:"public", tags, category:"EDUCATION", madeForKids:false, isAiGeneratedContent:false}`.
5. Estado `programado` + `plannerUrl` en `calendario.json`, commit + push.
6. Informe corto para Raúl: qué se ha dejado en borrador, enlaces, temas nuevos y lo que no se haya podido verificar.
   Saldo de ElevenLabs compartido con Instagram. Con `eleven_v4` cada carácter de guion consume ~0,5 créditos
   (un episodio de 15-20 min ≈ 7.000 créditos). Decir siempre el saldo que queda; si no llega, avisar.
