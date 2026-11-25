// Genera propuestas de foto de perfil (800x800) y banner (2560x1440) del canal
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const R = path.resolve(__dirname, '../..'), F = `file://${R}/node_modules/@fontsource`;
const css = `@font-face{font-family:OS;font-weight:700;src:url(${F}/oswald/files/oswald-latin-700-normal.woff2)}
@font-face{font-family:OS;font-weight:500;src:url(${F}/oswald/files/oswald-latin-500-normal.woff2)}
@font-face{font-family:TY;src:url(${F}/special-elite/files/special-elite-latin-400-normal.woff2)}
@font-face{font-family:PF;font-weight:700;font-style:italic;src:url(${F}/playfair-display/files/playfair-display-latin-700-italic.woff2)}
*{margin:0;padding:0;box-sizing:border-box}body{background:#0d0c0a;color:#ebe3cf;overflow:hidden}
.grain{position:absolute;inset:0;opacity:.16;mix-blend-mode:overlay}
.ph{position:absolute;inset:0;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.15) brightness(.42)}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,transparent 35%,rgba(0,0,0,.85) 100%)}`;
const grain = `<svg class="grain" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>`;
const img = n => `file://${R}/youtube-historia/videos/01_hitler-llega-al-poder/img/${n}.jpg`;
const P = {
  // A: sello circular
  perfil_A: [800, 800, `<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">
    <div style="width:640px;height:640px;border-radius:50%;border:14px solid #d4a843;display:flex;flex-direction:column;align-items:center;justify-content:center;background:radial-gradient(circle,#1d1a15 0%,#0d0c0a 70%)">
    <div style="font-family:TY;font-size:62px;color:#d4a843;letter-spacing:5px">SOMBRAS</div>
    <div style="font-family:TY;font-size:40px;color:#d4a843;letter-spacing:10px;margin-top:2px">DEL</div>
    <div style="font-family:OS;font-weight:700;font-size:290px;line-height:.9;color:#ebe3cf;text-shadow:18px 14px 0 rgba(0,0,0,.65)">39</div>
    <div style="width:240px;height:8px;background:#c0392b;margin-top:14px"></div></div></div>`],
  // B: foto del Reichstag en llamas
  perfil_B: [800, 800, `<div class="ph" style="background-image:url(${img('incendio')});filter:grayscale(1) contrast(1.2) brightness(.38)"></div><div class="vig"></div>
    <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
    <div style="font-family:TY;font-size:66px;color:#d4a843;letter-spacing:6px;text-shadow:0 4px 20px #000">SOMBRAS DEL</div>
    <div style="font-family:OS;font-weight:700;font-size:330px;line-height:.92;color:#ebe3cf;text-shadow:0 10px 40px #000">39</div>
    <div style="width:260px;height:8px;background:#c0392b;margin-top:10px"></div></div>`],
  // Banner: zona segura central 1546x423
  banner: [2560, 1440, `<div class="ph" style="background-image:url(${img('antorchas')});background-position:50% 40%"></div><div class="vig"></div>
    <div style="position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;align-items:center">
    <div style="display:flex;align-items:center;gap:34px">
      <div style="font-family:TY;font-size:92px;color:#d4a843;letter-spacing:8px;text-shadow:0 6px 30px #000">SOMBRAS DEL</div>
      <div style="font-family:OS;font-weight:700;font-size:210px;line-height:1;color:#ebe3cf;text-shadow:0 8px 40px #000">39</div></div>
    <div style="width:300px;height:7px;background:#c0392b;margin:6px 0 22px"></div>
    <div style="font-family:PF;font-style:italic;font-weight:700;font-size:50px;text-shadow:0 4px 20px #000">La Segunda Guerra Mundial, contada con documentos reales</div>
    <div style="font-family:OS;font-weight:500;font-size:40px;letter-spacing:6px;color:#0d0c0a;background:#d4a843;padding:6px 26px;margin-top:26px">NUEVO CAPÍTULO CADA SEMANA</div></div>`],
};
(async () => {
  const b = await chromium.launch();
  for (const [name, [w, h, body]] of Object.entries(P)) {
    const pg = await b.newPage({ viewport: { width: w, height: h } });
    const f = path.join(__dirname, '_tmp.html');
    fs.writeFileSync(f, `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body style="width:${w}px;height:${h}px">${body}${grain}</body></html>`);
    await pg.goto('file://' + f);
    await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(300);
    await pg.screenshot({ path: path.join(__dirname, name + '.png') }); await pg.close();
  }
  await b.close(); fs.unlinkSync(path.join(__dirname, '_tmp.html')); console.log('OK');
})();
