// Uso: node engine/render.js <carpeta_del_video>
// La carpeta debe tener spec.json, audio.mp3 y align.json (los genera tts.js).
// Produce video.mp4 (1080x1920, 30 fps) y portada.jpg.
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const { chromium } = require('playwright');

const FPS = 30;
const dir = path.resolve(process.argv[2]);
const spec = JSON.parse(fs.readFileSync(path.join(dir, 'spec.json'), 'utf8'));
const al = JSON.parse(fs.readFileSync(path.join(dir, 'align.json'), 'utf8'));
const chars = al.characters, starts = al.character_start_times_seconds, ends = al.character_end_times_seconds;

// --- tiempos de cada escena según el audio ---
const base = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
const fullText = spec.scenes.map(s => s.say.trim()).join(' ');
if (chars.join('') !== fullText) console.warn('Aviso: el texto alineado no coincide exactamente con el guion');
const audioEnd = ends[ends.length - 1];
let off = 0;
const scenes = spec.scenes.map((s, i) => {
  const say = s.say.trim();
  const o = off; off += say.length + 1;
  return { ...s, say, off: o, start: i === 0 ? 0 : Math.max(0, starts[Math.min(o, starts.length - 1)] - 0.12) };
});
scenes.forEach((s, i) => { s.end = i + 1 < scenes.length ? scenes[i + 1].start : audioEnd + (spec.tail ?? 1.8); });
const total = scenes[scenes.length - 1].end;

// tiempo (s) en que se pronuncia `cue` dentro de la escena (n-ésima aparición)
function cueTime(sc, cue, n = 1) {
  const hay = base(sc.say), needle = base(cue);
  let idx = -1, from = 0;
  for (let k = 0; k < n; k++) { idx = hay.indexOf(needle, from); if (idx < 0) break; from = idx + 1; }
  if (idx < 0) { console.warn(`  cue no encontrado: "${cue}" en escena "${sc.say.slice(0, 40)}…"`); return sc.start + 0.3; }
  return starts[Math.min(sc.off + idx, starts.length - 1)];
}

const SERIES = {
  bolsa: { kicker: 'Finanzas desde cero' },
  nadie: { kicker: 'Lo que nadie te cuenta' },
  fondo: { kicker: 'Finanzas a fondo' },
};

function sceneHTML(s, i) {
  const hdr = `<div class="hdr"><div class="topic">${spec.topic}</div><div class="handle">@_raulpallares</div></div>`;
  const title = s.title ? `<div class="ttl in" data-t="0">${s.title}${s.sub ? `<div class="sub">${s.sub}</div>` : ''}</div>` : '';
  const layout = s.layout || (s.title ? 'stage' : 'center');
  const body = `<div class="${layout}">${s.html || ''}</div>`;
  return `<section class="scene${s.dark ? ' dark' : ''}" id="s${i}">${s.noHeader ? '' : hdr}${title}${body}</section>`;
}

const html = `<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"></head><body>
${scenes.map(sceneHTML).join('\n')}
<script>window.__SERIES=${JSON.stringify(SERIES[spec.series] || {})};</script></body></html>`;
const pagePath = path.join(__dirname, `_page_${path.basename(dir)}.html`);
fs.writeFileSync(pagePath, html);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + pagePath);
  await page.evaluate(() => document.fonts.ready);

  // calcular el momento de aparición de cada elemento animado
  const cueMap = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('.scene').forEach((sec, si) => {
      sec.querySelectorAll('.in,[data-cue],[data-t],.grow,.draw,[data-count]').forEach((el, k) => {
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
    let t = c.cue ? cueTime(sc, c.cue, c.n) : sc.start + (c.t !== undefined ? +c.t : 0.25);
    times[c.k] = t + c.d;
  }
  await page.evaluate(({ times, bounds }) => {
    const ease = p => 1 - Math.pow(1 - p, 3);
    const els = [...document.querySelectorAll('[data-k]')].map(el => {
      const cs = getComputedStyle(el);
      const o = { el, t0: times[el.dataset.k], grow: el.classList.contains('grow'), draw: el.classList.contains('draw'),
        w: cs.getPropertyValue('--w').trim(), h: cs.getPropertyValue('--h').trim(), count: el.dataset.count };
      if (o.draw) { o.len = el.getTotalLength(); el.style.strokeDasharray = o.len; }
      if (o.count) { o.fmt = el.dataset.fmt || ''; o.dec = +(el.dataset.dec || 0); }
      return o;
    });
    const secs = [...document.querySelectorAll('.scene')];
    window.setT = t => {
      // cada escena aparece con un fundido de 0,3 s encima de la anterior
      secs.forEach((s, i) => {
        const [a, b] = bounds[i];
        s.style.zIndex = i + 1;
        s.style.opacity = t < a || t >= b + 0.35 ? 0 : (i === 0 ? 1 : Math.min(1, (t - a) / 0.3));
      });
      for (const o of els) {
        const p = ease(Math.max(0, Math.min(1, (t - o.t0) / 0.55)));
        if (o.grow) {
          if (o.w) o.el.style.width = `calc(${o.w} * ${p})`;
          if (o.h) o.el.style.height = `calc(${o.h} * ${p})`;
          o.el.style.opacity = p > 0 ? 1 : 0;
        } else if (o.draw) {
          const q = Math.max(0, Math.min(1, (t - o.t0) / 1.4));
          o.el.style.strokeDashoffset = o.len * (1 - q);
        } else {
          o.el.style.opacity = p;
          o.el.style.transform = `translateY(${(1 - p) * 26}px)`;
        }
        if (o.count) {
          const v = (+o.count) * p;
          o.el.textContent = v.toLocaleString('es-ES', { minimumFractionDigits: o.dec, maximumFractionDigits: o.dec }) + o.fmt;
        }
      }
    };
  }, { times, bounds: scenes.map(s => [s.start, s.end]) });

  const out = path.join(dir, 'video.tmp.mp4'); // se renombra a video.mp4 al terminar
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-i', path.join(dir, 'audio.mp3'), '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p',
    '-c:a', 'aac', '-b:a', '160k', '-t', total.toFixed(2), '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });

  const N = Math.ceil(total * FPS);
  const t0 = Date.now();
  for (let f = 0; f < N; f++) {
    await page.evaluate(t => window.setT(t), f / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 300 === 0) process.stdout.write(`  frame ${f}/${N} (${((Date.now() - t0) / 1000).toFixed(0)} s)\n`);
  }
  ff.stdin.end();
  const code = await new Promise(r => ff.on('close', r));
  if (code !== 0) { console.error('FALLO ffmpeg ' + code); process.exit(1); }
  fs.renameSync(out, path.join(dir, 'video.mp4'));

  // portada: escena de título (spec.coverScene, por defecto la 1) completamente montada
  const cs = scenes[spec.coverScene ?? 1] || scenes[0];
  await page.evaluate(t => window.setT(t), Math.min(cs.end - 0.05, cs.start + 2.5));
  await page.screenshot({ path: path.join(dir, 'portada.jpg'), type: 'jpeg', quality: 92 });
  await browser.close();
  fs.unlinkSync(pagePath);
  console.log(`OK ${path.join(dir, 'video.mp4')} · ${total.toFixed(1)} s · render ${((Date.now() - t0) / 1000).toFixed(0)} s`);
})();
