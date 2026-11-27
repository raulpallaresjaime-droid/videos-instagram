// Uso: node youtube-historia/engine/render.js <carpeta_del_video> [--preview s1,s2,...] [--workers 3]
// Necesita spec.json, audio.mp3 y align.json (tts.js). Produce:
//   eventos.json   tiempos de escenas, tecleos y golpes (lo usa mix.py)
//   video.mp4      1920x1080, 30 fps, con la mezcla final (voz + música + efectos)
// Con --preview solo guarda fotogramas sueltos (preview_<t>.jpg).
// Uso interno: --part i/N renderiza solo un tramo de fotogramas (sin audio).
const fs = require('fs');
const path = require('path');
const { spawn, execFileSync } = require('child_process');
const { chromium } = require('playwright');

const FPS = 30, FADE = 0.6, TYPE_CPS = 18; // caracteres por segundo de la máquina de escribir
const arg = k => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : null; };
const dir = path.resolve(process.argv[2]);
const preview = arg('--preview') ? arg('--preview').split(',').map(Number) : null;
const part = arg('--part') ? arg('--part').split('/').map(Number) : null;
const WORKERS = +(arg('--workers') || 3);
const spec = JSON.parse(fs.readFileSync(path.join(dir, 'spec.json'), 'utf8'));
const al = JSON.parse(fs.readFileSync(path.join(dir, 'align.json'), 'utf8'));
const starts = al.character_start_times_seconds, ends = al.character_end_times_seconds;

const base = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
const fullText = spec.scenes.map(s => s.say.trim()).join(' ');
if (al.characters.join('') !== fullText && !part) console.warn('Aviso: el texto alineado no coincide exactamente con el guion');
const audioEnd = ends[ends.length - 1];
let off = 0;
const scenes = spec.scenes.map((s, i) => {
  const say = s.say.trim(); const o = off; off += say.length + 1;
  return { ...s, say, off: o, start: i === 0 ? 0 : Math.max(0, starts[Math.min(o, starts.length - 1)] - 0.25) };
});
scenes.forEach((s, i) => { s.end = i + 1 < scenes.length ? scenes[i + 1].start : audioEnd + (spec.tail ?? 4); });
const total = scenes[scenes.length - 1].end;
const N = Math.ceil(total * FPS);

function cueTime(sc, cue, n = 1) {
  const hay = base(sc.say), needle = base(cue);
  let idx = -1, from = 0;
  for (let k = 0; k < n; k++) { idx = hay.indexOf(needle, from); if (idx < 0) break; from = idx + 1; }
  if (idx < 0) { if (!part) console.warn(`  cue no encontrado: "${cue}" en "${sc.say.slice(0, 50)}…"`); return sc.start + 0.4; }
  return starts[Math.min(sc.off + idx, starts.length - 1)];
}

// ---------- Capas de imagen ----------
// Cada escena puede llevar varias imágenes/clips seguidos: `imgs: [item, item, …]`. item = "img/x.jpg" o
// { img | clip, clipStart, clipRate, kb, fx, fy, blur, cue, n, t, cap, who: {name, role} }.
// Cada capa entra con un fundido (XF) cuando se pronuncia `cue` (o en `t` s desde el inicio de la escena; si no hay
// ninguno, se reparten a partes iguales) y tiene su propio Ken Burns. `img`/`clip` sueltos = una sola capa (compatible
// con los episodios antiguos). Las rutas se buscan en la carpeta del episodio y, si no están, en youtube-historia/
// (así sirve la biblioteca de retratos: "personas/hoss.jpg").
// Clips: cada capa con `clip` se trocea en fotogramas JPG (_clips_cache/) y el render cambia de fotograma en
// sincronía con su propio reloj (funciona igual en --preview y en los tramos en paralelo). Si el clip es más corto que
// su capa se ralentiza hasta 0,6× y después se congela (el render avisa).
// `who` = rótulo de identificación (nombre + cargo) que aparece al entrar la capa y dura ~7 s.
// `blur` = desenfoque fuerte (true = 26 px, o un número) para lo más duro.
const KB = { clip: [1.0, 1.05, 0, 0], in: [1.0, 1.12, 0, 0], out: [1.14, 1.0, 0, 0], left: [1.12, 1.12, 0.6, -0.6], right: [1.12, 1.12, -0.6, 0.6],
  up: [1.12, 1.12, 0, 0], still: [1.04, 1.1, 0, 0] };
const XF = 0.8, CLIP_FPS = 30, CLIP_CACHE = path.join(dir, '_clips_cache');
const resolve = p => { const a = path.join(dir, p); return fs.existsSync(a) ? a : path.join(__dirname, '..', p); };
const usage = {};
scenes.forEach((s, i) => {
  let items = s.imgs || (s.img || s.clip ? [{ img: s.img, clip: s.clip, clipStart: s.clipStart, clipRate: s.clipRate, kb: s.kb,
    fx: s.fx, fy: s.fy, blur: s.blur, who: s.who }] : []);
  items = items.map(x => typeof x === 'string' ? { [/\.(mp4|webm)$/i.test(x) ? 'clip' : 'img']: x } : { ...x });
  s.photo = items.length > 0;
  if (!items.length && s.bg) items = [{ img: s.bg, bg: true, kb: 'still' }]; // fondo oscuro de gráficos y citas
  const dur = s.end - s.start;
  items.forEach((L, j) => {
    L.a = j === 0 ? s.start : L.cue ? cueTime(s, L.cue, L.n || 1) - 0.2 : L.t !== undefined ? s.start + L.t : s.start + dur * j / items.length;
  });
  items.forEach((L, j) => {
    L.e = j + 1 < items.length ? items[j + 1].a + XF : s.end + FADE;           // fin de la capa (cubierta por la siguiente)
    L.out = j + 1 < items.length ? items[j + 1].a : s.end;                     // cuándo empieza a irse
    L.kb = KB[L.kb] ? L.kb : L.clip ? 'clip' : (i + j) % 2 ? 'in' : 'out';
    const key = (L.img || L.clip) + (L.clip ? '@' + (L.clipStart || 0) : '');
    (usage[key] = usage[key] || []).push(i);
    if (L.clip) {
      const src = resolve(L.clip);
      const len = +execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src]).toString().trim();
      const avail = Math.max(0.1, len - (L.clipStart || 0)), need = L.e - L.a;
      L.rate = L.clipRate || Math.max(0.6, Math.min(1, avail / need));
      if (!part && avail < need * L.rate - 0.05) console.warn(`  Aviso: el clip ${L.clip} (escena ${i}) se congela ${(need - avail / L.rate).toFixed(1)} s (es corto)`);
      L.cdir = path.join(CLIP_CACHE, `${i}_${j}_${path.basename(L.clip).replace(/\W/g, '_')}_${L.clipStart || 0}`);
      if (!fs.existsSync(path.join(L.cdir, '.ok'))) { // solo la primera vez (el proceso principal, antes de los tramos)
        fs.mkdirSync(L.cdir, { recursive: true });
        execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-ss', String(L.clipStart || 0), '-t', String(Math.min(avail, need * L.rate + 0.5)),
          '-i', src, '-an', '-vf', `fps=${CLIP_FPS},scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720`,
          '-q:v', '3', path.join(L.cdir, '%05d.jpg')]);
        fs.writeFileSync(path.join(L.cdir, '.ok'), '');
      }
      L.frames = fs.readdirSync(L.cdir).filter(f => f.endsWith('.jpg')).length;
      L.src = path.join(L.cdir, '00001.jpg');
    } else L.src = resolve(L.img);
    if (!fs.existsSync(L.src)) throw new Error(`No existe la imagen ${L.img || L.clip} (escena ${i})`);
  });
  s.layers = items;
});
if (!part) { // regla: cada foto o clip, una sola vez por capítulo
  const rep = Object.entries(usage).filter(([, v]) => v.length > 1);
  rep.forEach(([k, v]) => console.warn(`  REPETIDA: ${k} en las escenas ${v.join(', ')}`));
}

function sceneHTML(s, i) {
  const cls = ['scene', s.photo ? '' : 'paper', s.side ? 'side-' + s.side : ''].join(' ');
  let ph = '', labs = '';
  s.layers.forEach((L, j) => {
    const at = ` data-clip="${L.clip ? j : ''}"`;
    const bl = L.blur ? ` style="--blur:${L.blur === true ? 26 : L.blur}px"` : '';
    ph += `<div class="layer${L.blur ? ' blurred' : ''}" data-l="${j}"${bl}>`;
    if (s.side) ph += `<div class="ph blur"><img src="file://${L.src}" data-fill="1"${at}></div>`;
    ph += `<div class="ph ${L.bg ? 'bgimg' : 'main'}"><img src="file://${L.src}" data-kb="${L.kb}" data-fx="${L.fx ?? 0.5}" data-fy="${L.fy ?? 0.5}"${at}></div></div>`;
    if (L.cap) labs += `<div class="cap lcap" data-l="${j}">${L.cap}</div>`;
    if (L.who) labs += `<div class="idl${s.side === 'right' ? ' r' : ''}" data-l="${j}" data-w="1"><b>${L.who.name}</b>${L.who.role ? `<span>${L.who.role}</span>` : ''}</div>`;
  });
  if (s.layers.length) ph += `<div class="vig"></div>${s.shade && s.photo ? '<div class="shade"></div>' : ''}`;
  const cap = s.cap ? `<div class="cap in" data-t="0.4">${s.cap}</div>` : '';
  return `<section class="${cls}" id="s${i}">${ph}${s.html || ''}${cap}${labs}</section>`;
}
const grain = `<svg class="grain" xmlns="http://www.w3.org/2000/svg" width="2040" height="1200"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>`;
const html = `<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${path.join(__dirname, 'style.css')}"></head><body>
${scenes.map(sceneHTML).join('\n')}${grain}<div class="flick" style="opacity:0"></div>${spec.brand ? `<div class="brand">${spec.brand}</div>` : ''}</body></html>`;
const pagePath = path.join(dir, part ? `_page_${part[0]}.html` : '_page.html');
fs.writeFileSync(pagePath, html);

async function setup(page) {
  await page.goto('file://' + pagePath);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForFunction(() => [...document.images].every(i => i.complete));
  // fechas y etiquetas siempre a máquina; .tw en cualquier otro texto
  const cueMap = await page.evaluate(() => {
    document.querySelectorAll('.date,.tag').forEach(el => el.classList.add('tw'));
    const out = [];
    document.querySelectorAll('.scene').forEach((sec, si) => {
      sec.querySelectorAll('.in,.grow,[data-count],.tw').forEach((el, k) => {
        el.dataset.k = si + '_' + k;
        let src = el;
        while (src && src !== sec && !src.dataset.cue && src.dataset.t === undefined) src = src.parentElement;
        out.push({ k: el.dataset.k, si, cue: src?.dataset?.cue, n: +(src?.dataset?.n || 1), t: src?.dataset?.t, d: +(el.dataset.d || 0),
          tw: el.classList.contains('tw'), chars: el.textContent.trim().length, text: el.textContent.trim(),
          hit: el.classList.contains('stamp') || el.classList.contains('hit') });
      });
    });
    return out;
  });
  const times = {};
  for (const c of cueMap) {
    const sc = scenes[c.si];
    times[c.k] = (c.cue ? cueTime(sc, c.cue, c.n) : sc.start + (c.t !== undefined ? +c.t : 0.4)) + c.d;
  }
  // regla anti-pantalla vacía: en escenas sin foto, lo primero aparece como muy tarde 0,8 s después de empezar
  scenes.forEach((sc, si) => {
    if (sc.photo && !sc.side) return; // en retratos, la mitad de texto tampoco puede quedarse vacía
    const own = cueMap.filter(c => c.si === si);
    if (!own.length) return;
    const first = Math.min(...own.map(c => times[c.k]));
    if (first - sc.start > 1.2) own.filter(c => times[c.k] - first < 0.05).forEach(c => { times[c.k] = sc.start + 0.6; });
  });
  // varios textos a máquina en la misma escena: uno detrás de otro, nunca a la vez
  scenes.forEach((sc, si) => {
    let free = 0;
    cueMap.filter(c => c.si === si && c.tw).sort((x, y) => times[x.k] - times[y.k]).forEach(c => {
      times[c.k] = Math.max(times[c.k], free); free = times[c.k] + c.chars / TYPE_CPS + 0.15;
    });
  });
  await page.evaluate(({ times, bounds, KB, FADE, XF, CPS, layers }) => {
    const ease = p => 1 - Math.pow(1 - p, 3);
    const els = [...document.querySelectorAll('[data-k]')].map(el => {
      const cs = getComputedStyle(el);
      const o = { el, t0: times[el.dataset.k], grow: el.classList.contains('grow'), w: cs.getPropertyValue('--w').trim(),
        h: cs.getPropertyValue('--h').trim(), count: el.dataset.count, fmt: el.dataset.fmt || '', dec: +(el.dataset.dec || 0),
        tw: el.classList.contains('tw') && !el.dataset.count };
      if (o.tw) { // trocear el HTML en etiquetas y caracteres para teclearlo sin romper <br>, <span>…
        o.tokens = []; o.full = el.innerHTML;
        for (const part of o.full.split(/(<[^>]+>|&[a-z#0-9]+;)/i)) {
          if (!part) continue;
          if (part.startsWith('<')) o.tokens.push({ tag: part });
          else if (part.startsWith('&')) o.tokens.push({ ch: part });
          else for (const ch of [...part]) o.tokens.push({ ch });
        }
        o.n = o.tokens.filter(x => x.ch).length; o.last = -1;
        el.style.minHeight = el.offsetHeight + 'px';
      }
      return o;
    });
    const secs = [...document.querySelectorAll('.scene')];
    const imgs = secs.map((sec, si) => [...sec.querySelectorAll('.layer')].map((lay, j) => ({ lay, ...layers[si][j],
      labs: [...sec.querySelectorAll(`.lcap[data-l="${j}"],.idl[data-l="${j}"]`)],
      imgs: [...lay.querySelectorAll('.ph img')].map(img => {
        const box = img.parentElement.getBoundingClientRect();
        const r = Math.max(box.width / img.naturalWidth, box.height / img.naturalHeight);
        img.style.width = img.naturalWidth * r + 'px'; img.style.height = img.naturalHeight * r + 'px';
        return { img, bw: box.width, bh: box.height, w: img.naturalWidth * r, h: img.naturalHeight * r,
          kb: KB[img.dataset.kb] || KB.in, fx: +img.dataset.fx, fy: +img.dataset.fy, fill: !!img.dataset.fill,
          clip: img.dataset.clip !== '' && img.dataset.clip !== undefined, cur: 1 };
      }) })));
    const grain = document.querySelector('.grain'), flick = document.querySelector('.flick');
    window.setT = t => {
      const loads = [];
      secs.forEach((s, i) => {
        const [a, b] = bounds[i];
        const vis = t >= a && t < b + FADE;
        s.style.zIndex = i + 1;
        s.style.opacity = !vis ? 0 : (i === 0 ? 1 : Math.min(1, (t - a) / FADE));
        if (!vis) return;
        const ls = imgs[i];
        ls.forEach((L, j) => {
          const next = ls[j + 1];
          const covered = next && t >= next.a + XF; // ya tapada del todo por la siguiente: no se pinta
          const op = t < L.a || covered ? 0 : j === 0 ? 1 : Math.min(1, (t - L.a) / XF);
          L.lay.style.opacity = op;
          for (const lab of L.labs) { // pies de foto y rótulos de identificación de esta capa
            const w = lab.dataset.w, a0 = L.a + (w ? 0.5 : 0.4), end = w ? Math.min(L.out, L.a + 7) : L.out;
            lab.style.opacity = op && t >= a0 ? Math.min(1, (t - a0) / 0.5, Math.max(0, (end - t) / 0.4)) : 0;
            if (w) lab.style.transform = `translateY(${(1 - Math.min(1, Math.max(0, (t - a0) / 0.5))) * 20}px)`;
          }
          if (!op) return;
          const p = Math.max(0, Math.min(1, (t - L.a) / (L.e - L.a)));
          for (const o of L.imgs) {
            const k = o.fill ? [1.1, 1.1, 0, 0] : o.kb;
            const sc = k[0] + (k[1] - k[0]) * p;
            const mx = Math.max(0, (o.w * sc - o.bw) / 2), my = Math.max(0, (o.h * sc - o.bh) / 2);
            const fx = (0.5 - o.fx) * 2, fy = (0.5 - o.fy) * 2;
            const px = Math.max(-1, Math.min(1, fx + k[2] * (p - 0.5) * 2)), py = Math.max(-1, Math.min(1, fy + k[3] * (p - 0.5) * 2));
            o.img.style.transform = `translate(-50%,-50%) translate(${px * mx}px,${py * my}px) scale(${sc})`;
            if (o.clip) { // fotograma del clip que toca en este instante
              const f = Math.max(1, Math.min(L.frames, 1 + Math.floor((t - L.a) * L.rate * 30 + 1e-6)));
              if (f !== o.cur) { o.cur = f; o.img.src = L.dir + '/' + String(f).padStart(5, '0') + '.jpg'; loads.push(o.img.decode().catch(() => {})); }
            }
          }
        });
      });
      for (const o of els) {
        if (o.tw) {
          const typed = Math.max(0, Math.min(o.n, Math.floor((t - o.t0) * CPS)));
          o.el.style.opacity = t < o.t0 ? 0 : 1;
          const caret = t >= o.t0 && typed < o.n;
          const key = typed * 2 + (caret ? 1 : 0);
          if (key !== o.last) {
            let k = 0, s = '';
            for (const x of o.tokens) { if (x.tag) { s += x.tag; continue; } if (k++ >= typed) break; s += x.ch; }
            o.el.innerHTML = s + (caret ? '<span class="caret">▌</span>' : '');
            o.last = key;
          }
          continue;
        }
        const p = ease(Math.max(0, Math.min(1, (t - o.t0) / 0.7)));
        if (o.grow) {
          if (o.w) o.el.style.width = `calc(${o.w} * ${p})`;
          if (o.h) o.el.style.height = `calc(${o.h} * ${p})`;
        } else { o.el.style.opacity = p; o.el.style.transform = `translateY(${(1 - p) * 24}px)`; }
        if (o.count) o.el.textContent = (Math.round(+o.count * p * 10 ** o.dec) / 10 ** o.dec)
          .toLocaleString('es-ES', { minimumFractionDigits: o.dec, maximumFractionDigits: o.dec }) + o.fmt;
      }
      const f = Math.floor(t * 30);
      grain.style.transform = `translate(${(f * 37) % 60 - 30}px,${(f * 53) % 60 - 30}px)`;
      flick.style.opacity = (Math.sin(f * 12.9898) * 43758.5453 % 1 + 1) % 1 * 0.04;
      return Promise.all(loads);
    };
  }, { times, bounds: scenes.map(s => [s.start, s.end]), KB, FADE, XF, CPS: TYPE_CPS,
    layers: scenes.map(s => s.layers.map(L => ({ a: L.a, e: L.e, out: L.out, rate: L.rate, frames: L.frames, dir: L.cdir ? 'file://' + L.cdir : null }))) });
  return { cueMap, times };
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  const { cueMap, times } = await setup(page);

  if (part) { // tramo de fotogramas sin audio
    const [i, n] = part, a = Math.floor(N * i / n), b = Math.floor(N * (i + 1) / n);
    const out = path.join(dir, `_part_${i}.mp4`);
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
      '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', out], { stdio: ['pipe', 'inherit', 'inherit'] });
    const t0 = Date.now();
    for (let f = a; f < b; f++) {
      await page.evaluate(t => window.setT(t), f / FPS);
      const buf = await page.screenshot({ type: 'jpeg', quality: 90 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if ((f - a) % 1500 === 0) console.log(`  [${i}] ${f - a}/${b - a} (${((Date.now() - t0) / 1000).toFixed(0)} s)`);
    }
    ff.stdin.end();
    const code = await new Promise(r => ff.on('close', r));
    await browser.close(); fs.unlinkSync(pagePath); process.exit(code);
  }

  // eventos para la mezcla de audio
  const ev = {
    total, scenes: scenes.map(s => ({ start: +s.start.toFixed(3), end: +s.end.toFixed(3), mood: s.mood || null })),
    typing: cueMap.filter(c => c.tw).map(c => ({ t: +times[c.k].toFixed(3), text: c.text, cps: TYPE_CPS })),
    hits: cueMap.filter(c => c.hit).map(c => +times[c.k].toFixed(3)),
  };
  fs.writeFileSync(path.join(dir, 'eventos.json'), JSON.stringify(ev, null, 1));
  // informe de escenas: cuánto tarda en aparecer el primer elemento en las que no tienen foto
  scenes.forEach((sc, si) => {
    if (sc.photo) return;
    const own = cueMap.filter(c => c.si === si).map(c => times[c.k] - sc.start);
    const first = own.length ? Math.min(...own) : Infinity;
    if (first > 1.5) console.warn(`  Aviso: escena ${si} sin nada en pantalla durante ${first.toFixed(1)} s`);
  });

  if (preview) {
    for (const t of preview) { await page.evaluate(t => window.setT(t), t);
      await page.screenshot({ path: path.join(dir, `preview_${t}.jpg`), type: 'jpeg', quality: 85 }); }
    await browser.close(); fs.unlinkSync(pagePath); return;
  }
  await browser.close(); fs.unlinkSync(pagePath);

  // render en paralelo por tramos
  const t0 = Date.now();
  const codes = await Promise.all([...Array(WORKERS).keys()].map(i => new Promise(res => {
    const p = spawn('node', [__filename, dir, '--part', `${i}/${WORKERS}`], { stdio: 'inherit' });
    p.on('close', res);
  })));
  if (codes.some(c => c !== 0)) { console.error('FALLO en algún tramo'); process.exit(1); }
  const list = path.join(dir, '_parts.txt');
  fs.writeFileSync(list, [...Array(WORKERS).keys()].map(i => `file '${path.join(dir, `_part_${i}.mp4`)}'`).join('\n'));
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', list, '-c', 'copy', path.join(dir, 'video_mudo.mp4')]);
  [...Array(WORKERS).keys()].forEach(i => fs.unlinkSync(path.join(dir, `_part_${i}.mp4`))); fs.unlinkSync(list);
  console.log(`  vídeo sin audio listo · ${((Date.now() - t0) / 1000).toFixed(0)} s`);
  execFileSync('python3', [path.join(__dirname, 'mix.py'), dir], { stdio: 'inherit' });
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', path.join(dir, 'video_mudo.mp4'), '-i', path.join(dir, 'mezcla.wav'),
    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', path.join(dir, 'video.mp4')]);
  fs.rmSync(CLIP_CACHE, { recursive: true, force: true });
  console.log(`OK video.mp4 · ${total.toFixed(1)} s · ${((Date.now() - t0) / 1000).toFixed(0)} s`);
})();
