// Uso: node youtube-historia/engine/render.js <carpeta_del_video> [--preview segundos,segundos,...]
// Necesita spec.json, audio.mp3 y align.json (los genera tts.js). Produce video.mp4 (1920x1080, 30 fps).
// Con --preview solo guarda fotogramas sueltos (preview_<t>.jpg) para revisar sin renderizar todo.
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const { chromium } = require('playwright');

const FPS = 30, FADE = 0.6;
const dir = path.resolve(process.argv[2]);
const pi = process.argv.indexOf('--preview');
const preview = pi > 0 ? process.argv[pi + 1].split(',').map(Number) : null;
const spec = JSON.parse(fs.readFileSync(path.join(dir, 'spec.json'), 'utf8'));
const al = JSON.parse(fs.readFileSync(path.join(dir, 'align.json'), 'utf8'));
const starts = al.character_start_times_seconds, ends = al.character_end_times_seconds;

const base = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
const fullText = spec.scenes.map(s => s.say.trim()).join(' ');
if (al.characters.join('') !== fullText) console.warn('Aviso: el texto alineado no coincide exactamente con el guion');
const audioEnd = ends[ends.length - 1];
let off = 0;
const scenes = spec.scenes.map((s, i) => {
  const say = s.say.trim(); const o = off; off += say.length + 1;
  return { ...s, say, off: o, start: i === 0 ? 0 : Math.max(0, starts[Math.min(o, starts.length - 1)] - 0.25) };
});
scenes.forEach((s, i) => { s.end = i + 1 < scenes.length ? scenes[i + 1].start : audioEnd + (spec.tail ?? 3); });
const total = scenes[scenes.length - 1].end;

function cueTime(sc, cue, n = 1) {
  const hay = base(sc.say), needle = base(cue);
  let idx = -1, from = 0;
  for (let k = 0; k < n; k++) { idx = hay.indexOf(needle, from); if (idx < 0) break; from = idx + 1; }
  if (idx < 0) { console.warn(`  cue no encontrado: "${cue}" en "${sc.say.slice(0, 50)}…"`); return sc.start + 0.4; }
  return starts[Math.min(sc.off + idx, starts.length - 1)];
}

// movimiento de cámara (Ken Burns): [escala inicial, escala final, desplazamiento x, y en % del sobrante]
const KB = { in: [1.0, 1.12, 0, 0], out: [1.14, 1.0, 0, 0], left: [1.12, 1.12, 0.6, -0.6], right: [1.12, 1.12, -0.6, 0.6],
  up: [1.12, 1.12, 0, 0], still: [1.03, 1.06, 0, 0] };
function sceneHTML(s, i) {
  const cls = ['scene', s.img ? '' : 'paper', s.side ? 'side-' + s.side : ''].join(' ');
  let ph = '';
  if (s.img) {
    const src = path.join(dir, s.img);
    if (s.side) ph += `<div class="ph blur"><img src="file://${src}" data-fill="1"></div>`;
    ph += `<div class="ph main"><img src="file://${src}" data-kb="${s.kb || (i % 2 ? 'in' : 'out')}" data-fx="${s.fx ?? 0.5}" data-fy="${s.fy ?? 0.5}"></div>`;
    ph += `<div class="vig"></div>${s.shade ? '<div class="shade"></div>' : ''}`;
  }
  const cap = s.cap ? `<div class="cap in" data-t="0.4">${s.cap}</div>` : '';
  return `<section class="${cls}" id="s${i}">${ph}${s.html || ''}${cap}</section>`;
}
// grano de película: ruido SVG que se mueve cada fotograma
const grain = `<svg class="grain" xmlns="http://www.w3.org/2000/svg" width="2040" height="1200"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>`;
const html = `<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${path.join(__dirname, 'style.css')}"></head><body>
${scenes.map(sceneHTML).join('\n')}${grain}<div class="flick" style="opacity:0"></div>${spec.brand ? `<div class="brand">${spec.brand}</div>` : ''}</body></html>`;
const pagePath = path.join(dir, '_page.html');
fs.writeFileSync(pagePath, html);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file://' + pagePath);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForFunction(() => [...document.images].every(i => i.complete));

  const cueMap = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('.scene').forEach((sec, si) => {
      sec.querySelectorAll('.in,.grow,[data-count]').forEach((el, k) => {
        el.dataset.k = si + '_' + k;
        let src = el;
        while (src && src !== sec && !src.dataset.cue && src.dataset.t === undefined) src = src.parentElement;
        out.push({ k: el.dataset.k, si, cue: src?.dataset?.cue, n: +(src?.dataset?.n || 1), t: src?.dataset?.t, d: +(el.dataset.d || 0) });
      });
    });
    return out;
  });
  const times = {};
  for (const c of cueMap) {
    const sc = scenes[c.si];
    times[c.k] = (c.cue ? cueTime(sc, c.cue, c.n) : sc.start + (c.t !== undefined ? +c.t : 0.4)) + c.d;
  }
  await page.evaluate(({ times, bounds, KB, FADE }) => {
    const ease = p => 1 - Math.pow(1 - p, 3);
    const els = [...document.querySelectorAll('[data-k]')].map(el => {
      const cs = getComputedStyle(el);
      return { el, t0: times[el.dataset.k], grow: el.classList.contains('grow'), w: cs.getPropertyValue('--w').trim(),
        h: cs.getPropertyValue('--h').trim(), count: el.dataset.count, fmt: el.dataset.fmt || '', dec: +(el.dataset.dec || 0) };
    });
    const secs = [...document.querySelectorAll('.scene')];
    // tamaño "cover" de cada foto dentro de su caja
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
          // margen sobrante para desplazar sin que se vea el borde
          const mx = Math.max(0, (o.w * sc - o.bw) / 2), my = Math.max(0, (o.h * sc - o.bh) / 2);
          const fx = (0.5 - o.fx) * 2, fy = (0.5 - o.fy) * 2; // punto de interés
          const px = Math.max(-1, Math.min(1, fx + k[2] * (p - 0.5) * 2)), py = Math.max(-1, Math.min(1, fy + k[3] * (p - 0.5) * 2));
          o.img.style.transform = `translate(-50%,-50%) translate(${px * mx}px,${py * my}px) scale(${sc})`;
        }
      });
      for (const o of els) {
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
  }, { times, bounds: scenes.map(s => [s.start, s.end]), KB, FADE });

  if (preview) {
    for (const t of preview) { await page.evaluate(t => window.setT(t), t);
      await page.screenshot({ path: path.join(dir, `preview_${t}.jpg`), type: 'jpeg', quality: 85 }); }
    await browser.close(); return;
  }
  const out = path.join(dir, 'video.tmp.mp4');
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-i', path.join(dir, 'audio.mp3'), '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p',
    '-c:a', 'aac', '-b:a', '192k', '-t', total.toFixed(2), '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const N = Math.ceil(total * FPS), t0 = Date.now();
  for (let f = 0; f < N; f++) {
    await page.evaluate(t => window.setT(t), f / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 90 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 900 === 0) console.log(`  frame ${f}/${N} (${((Date.now() - t0) / 1000).toFixed(0)} s)`);
  }
  ff.stdin.end();
  const code = await new Promise(r => ff.on('close', r));
  if (code !== 0) { console.error('FALLO ffmpeg ' + code); process.exit(1); }
  fs.renameSync(out, path.join(dir, 'video.mp4'));
  await browser.close();
  fs.writeFileSync(path.join(dir, 'escenas.json'), JSON.stringify(scenes.map(s => ({ start: +s.start.toFixed(2), say: s.say.slice(0, 60) })), null, 1));
  console.log(`OK video.mp4 · ${total.toFixed(1)} s · render ${((Date.now() - t0) / 1000).toFixed(0)} s`);
})();
