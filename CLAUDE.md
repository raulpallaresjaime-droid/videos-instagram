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
6. Informe final corto para Raúl: qué se ha programado, enlaces de Metricool, temas nuevos
   propuestos y cualquier dato que no se haya podido verificar.

Si algo falla (ElevenLabs sin caracteres, Metricool rechaza el vídeo, push rechazado…), no
inventar ni publicar nada a medias: dejar el estado como estaba y explicarlo en el informe.

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
  `.bars > .b > span + i.grow[--w]`, `.cols > .c > b + i.grow[--h] + span`,
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
  y portada `.../portada.jpg` en `videoThumbnailUrl`.
- Tipo `REEL`, `showReelOnFeed: true`, fecha `<fecha>T10:00:00`, texto = `caption.txt`.
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
