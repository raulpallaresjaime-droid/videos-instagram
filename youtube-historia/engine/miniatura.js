// Uso: node youtube-historia/engine/miniatura.js <carpeta_del_video>
// Lee "thumb" del spec.json y genera miniatura.jpg (1280×720):
//   {img, fx, fy, zoom,              foto principal (a la derecha, o de fondo si hay cara)
//    face: {img, fx, fy, zoom, w},   opcional: cara de un personaje a la derecha (w = ancho en %, por defecto 46)
//    l1, l2, l3}                     texto: frase corta, cifra o palabra grande en rojo, etiqueta
// Las rutas se buscan en la carpeta del episodio y, si no están, en youtube-historia/ ("personas/hitler.jpg").
// `zoom` (1 = encuadre normal) sirve para quedarse solo con la cara y dejar fuera brazaletes o insignias:
// NUNCA símbolos nazis en la miniatura.
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const dir = path.resolve(process.argv[2]);
const spec = JSON.parse(fs.readFileSync(path.join(dir, 'spec.json'), 'utf8'));
const t = spec.thumb;
const res = p => { const a = path.join(dir, p); return fs.existsSync(a) ? a : path.join(__dirname, '..', p); };
const css = fs.readFileSync(path.join(__dirname, 'style.css'), 'utf8').split('\n').filter(l => l.startsWith('@font-face'))
  .map(l => l.replace(/url\(\.\.\/\.\.\//g, `url(file://${path.join(__dirname, '../..')}/`)).join('\n');
const pic = (o, cls) => `<div class="${cls}"><img src="file://${res(o.img)}" style="object-position:${(o.fx ?? 0.5) * 100}% ${(o.fy ?? 0.3) * 100}%;
  transform-origin:${(o.fx ?? 0.5) * 100}% ${(o.fy ?? 0.3) * 100}%;transform:scale(${o.zoom || 1})"></div>`;
const f = t.face;
const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css}
*{margin:0;padding:0;box-sizing:border-box}body{width:1280px;height:720px;overflow:hidden;background:#0d0c0a}
.ph,.bg,.fc{position:absolute;top:0;height:100%;overflow:hidden}
.ph{right:0;width:62%}.bg{left:0;width:100%}.fc{right:0;width:${f?.w || 46}%}
img{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.3) brightness(.95)}
.bg img{filter:grayscale(1) contrast(1.2) brightness(.5)}
.ph::after,.fc::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,#0d0c0a 0%,rgba(13,12,10,0) 42%),radial-gradient(ellipse at 60% 40%,transparent 50%,rgba(0,0,0,.55))}
.bg::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(13,12,10,.85) 0%,rgba(13,12,10,.2) 60%)}
.tx{position:absolute;left:56px;top:0;bottom:0;width:${f ? 58 : 62}%;display:flex;flex-direction:column;justify-content:center}
.l1{font-family:OS;font-weight:700;font-size:92px;line-height:.98;color:#ebe3cf;text-transform:uppercase;text-shadow:0 4px 20px #000}
.l2{font-family:OS;font-weight:700;font-size:${t.l2size || 170}px;line-height:1;color:#e0392b;text-shadow:0 6px 30px #000;margin-top:6px;white-space:nowrap;text-transform:uppercase}
.l3{display:inline-block;font-family:OS;font-weight:500;font-size:40px;letter-spacing:3px;color:#0d0c0a;background:#d4a843;padding:4px 18px;margin-top:18px;text-transform:uppercase;align-self:flex-start}
</style></head><body>${f ? pic(t, 'bg') + pic(f, 'fc') : pic(t, 'ph')}
<div class="tx">${t.l1 ? `<div class="l1">${t.l1}</div>` : ''}${t.l2 ? `<div class="l2">${t.l2}</div>` : ''}${t.l3 ? `<div class="l3">${t.l3}</div>` : ''}</div></body></html>`;
const p = path.join(dir, '_thumb.html'); fs.writeFileSync(p, html);
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await pg.goto('file://' + p); await pg.evaluate(() => document.fonts.ready);
  await pg.waitForFunction(() => [...document.images].every(i => i.complete));
  await pg.screenshot({ path: path.join(dir, 'miniatura.jpg'), type: 'jpeg', quality: 92 });
  await b.close(); fs.unlinkSync(p); console.log('OK miniatura.jpg');
})();
