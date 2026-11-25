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

const KB = { in: [1.0, 1.12, 0, 0], out: [1.14, 1.0, 0, 0], left: [1.12, 1.12, 0.6, -0.6], right: [1.12, 1.12, -0.6, 0.6],
  up: [1.12, 1.12, 0, 0], still: [1.04, 1.1, 0, 0] };
function sceneHTML(s, i) {
  const cls = ['scene', s.img ? '' : 'paper', s.side ? 'side-' + s.side : ''].join(' ');
  let ph = '';
  if (s.img) {
    const src = path.join(dir, s.img);
    if (s.side) ph += `<div class="ph blur"><img src="file://${src}" data-fill="1"></div>`;
    ph += `<div class="ph main"><img src="file://${src}" data-kb="${s.kb || (i % 2 ? 'in' : 'out')}" data-fx="${s.fx ?? 0.5}" data-fy="${s.fy ?? 0.5}"></div>`;
    ph += `<div class="vig"></div>${s.shade ? '<div class="shade"></div>' : ''}`;
  } else if (s.bg) { // escena de gráfico/cita: foto de fondo muy oscura para que nunca se vea negro
    ph += `<div class="ph bgimg"><img src="file://${path.join(dir, s.bg)}" data-kb="still" data-fx="0.5" data-fy="0.5"></div><div class="vig"></div>`;
  }
  const cap = s.cap ? `<div class="cap in" data-t="0.4">${s.cap}</div>` : '';
  return `<section class="${cls}" id="s${i}">${ph}${s.html || ''}${cap}</section>`;
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
    if (sc.img && !sc.side) return; // en retratos, la mitad de texto tampoco puede quedarse vacía
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
  await page.evaluate(({ times, bounds, KB, FADE, CPS }) => {
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
    const imgs = secs.map(sec => [...sec.querySelectorAll('.ph img')].map(img => {
      const box = img.parentElement.getBoundingClientRect();
      const r = Math.max(box.width / img.naturalWidth, box.height / img.naturalHeight);
      img.style.width = img.naturalWidth * r + 'px'; img.style.height = img.naturalHeight * r + 'px';
      return { img, bw: box.width, bh: box.height, w: img.naturalWidth * r, h: img.naturalHeight * r,
        kb: KB[img.dataset.kb] || KB.in, fx: +img.dataset.fx, fy: +img.dataset.fy, fill: !!img.dataset.fill };
    }));
    const grain = document.querySelector('.grain'), flick = document.querySelector('.flick');
    window.setT = t => {
      secs.forEach((s, i) => {
        const [a, b] = bounds[i];
        const vis = t >= a && t < b + FADE;
        s.style.zIndex = i + 1;
        s.style.opacity = !vis ? 0 : (i === 0 ? 1 : Math.min(1, (t - a) / FADE));
        if (!vis) return;
        const p = Math.max(0, Math.min(1, (t - a) / (b + FADE - a)));
        for (const o of imgs[i]) {
          const k = o.fill ? [1.1, 1.1, 0, 0] : o.kb;
          const sc = k[0] + (k[1] - k[0]) * p;
          const mx = Math.max(0, (o.w * sc - o.bw) / 2), my = Math.max(0, (o.h * sc - o.bh) / 2);
          const fx = (0.5 - o.fx) * 2, fy = (0.5 - o.fy) * 2;
          const px = Math.max(-1, Math.min(1, fx + k[2] * (p - 0.5) * 2)), py = Math.max(-1, Math.min(1, fy + k[3] * (p - 0.5) * 2));
          o.img.style.transform = `translate(-50%,-50%) translate(${px * mx}px,${py * my}px) scale(${sc})`;
        }
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
    };
  }, { times, bounds: scenes.map(s => [s.start, s.end]), KB, FADE, CPS: TYPE_CPS });
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
    if (sc.img) return;
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
  console.log(`OK video.mp4 · ${total.toFixed(1)} s · ${((Date.now() - t0) / 1000).toFixed(0)} s`);
})();
