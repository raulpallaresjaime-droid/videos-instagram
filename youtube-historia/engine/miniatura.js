// Uso: node youtube-historia/engine/miniatura.js <carpeta_del_video>
// Lee "thumb" del spec.json ({img, l1, l2, l3, fy}) y genera miniatura.jpg (1280×720).
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const dir = path.resolve(process.argv[2]);
const spec = JSON.parse(fs.readFileSync(path.join(dir, 'spec.json'), 'utf8'));
const t = spec.thumb;
const css = fs.readFileSync(path.join(__dirname, 'style.css'), 'utf8').split('\n').filter(l => l.startsWith('@font-face'))
  .map(l => l.replace(/url\(\.\.\/\.\.\//g, `url(file://${path.join(__dirname, '../..')}/`)).join('\n');
const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css}
*{margin:0;padding:0;box-sizing:border-box}body{width:1280px;height:720px;overflow:hidden;background:#0d0c0a}
.ph{position:absolute;right:0;top:0;width:62%;height:100%;overflow:hidden}
.ph img{width:100%;height:100%;object-fit:cover;object-position:50% ${(t.fy ?? 0.3) * 100}%;filter:grayscale(1) contrast(1.25) brightness(.95)}
.ph::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,#0d0c0a 0%,rgba(13,12,10,.0) 45%),radial-gradient(ellipse at 60% 40%,transparent 50%,rgba(0,0,0,.6))}
.tx{position:absolute;left:56px;top:0;bottom:0;width:62%;display:flex;flex-direction:column;justify-content:center}
.l1{font-family:OS;font-weight:700;font-size:96px;line-height:.98;color:#ebe3cf;text-transform:uppercase;text-shadow:0 4px 20px #000}
.l2{font-family:OS;font-weight:700;font-size:170px;line-height:1;color:#e0392b;text-shadow:0 6px 30px #000;margin-top:6px}
.l3{display:inline-block;font-family:OS;font-weight:500;font-size:40px;letter-spacing:3px;color:#0d0c0a;background:#d4a843;padding:4px 18px;margin-top:18px;text-transform:uppercase;align-self:flex-start}
</style></head><body><div class="ph"><img src="file://${path.join(dir, t.img)}"></div>
<div class="tx"><div class="l1">${t.l1}</div><div class="l2">${t.l2}</div>${t.l3 ? `<div class="l3">${t.l3}</div>` : ''}</div></body></html>`;
const p = path.join(dir, '_thumb.html'); fs.writeFileSync(p, html);
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await pg.goto('file://' + p); await pg.evaluate(() => document.fonts.ready);
  await pg.screenshot({ path: path.join(dir, 'miniatura.jpg'), type: 'jpeg', quality: 92 });
  await b.close(); fs.unlinkSync(p); console.log('OK miniatura.jpg');
})();
