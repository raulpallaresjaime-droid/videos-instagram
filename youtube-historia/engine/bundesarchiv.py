# Fotos del Bundesarchiv (archivo federal alemán), originales en alta resolución.
# Uso:
#   python3 bundesarchiv.py search "Hindenburg Porträt"      → signatura | fecha | tamaño | título
#   python3 bundesarchiv.py get "Bild 102-14439" salida.jpg   → descarga (máx. 2400 px) y apunta el crédito
import sys, re, html, json, urllib.request, urllib.parse, io, os, time
UA = {'User-Agent': 'HistoriaDocBot/1.0 (https://claude.ai/code; educational documentary video tool)'}

def get(u):
    for k in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=180).read()
        except Exception:
            if k == 3: raise
            time.sleep(15)

def records(query):
    page = html.unescape(get('https://www.bild.bundesarchiv.de/dba/de/search/?query=' + urllib.parse.quote(query)).decode('utf-8', 'replace'))
    prev = 0
    for m in re.finditer(r'"orignalurl":"([^"]+)"', page):
        seg = page[prev:m.start()]; prev = m.end()
        f = lambda lab: (re.findall(r'"values":\["([^"]*)"\],"label":"' + lab + '"', seg) or [''])[-1]
        yield dict(sig=f('Signatur'), title=f('Archivtitel').replace('\n', ' '), size=f('Abmessungen'),
                   date=(re.findall(r'"date":"([^"]*)"', page[m.end():m.end() + 400]) or [''])[0],
                   url=m.group(1).replace('\\/', '/').replace('bundesbildarchiv.init-ag.de', 'bild.bundesarchiv.de'))

if sys.argv[1] == 'search':
    seen = set()
    for r in records(sys.argv[2]):
        if r['sig'] in seen: continue
        seen.add(r["sig"]); print(f"{r['url'].split('/')[2][:5]} {r['sig']} | {r['date']} | {r['size']} | {r['title'][:110]}")
else:
    from PIL import Image
    sig, out = sys.argv[2], sys.argv[3]
    r = next((r for r in records(sig) if r['sig'] == sig), None)
    if not r: sys.exit(f'NO ENCONTRADA {sig}')
    im = Image.open(io.BytesIO(get(r['url']))).convert('RGB')
    im.thumbnail((2400, 2400)); im.save(out, quality=90)
    with open(os.path.join(os.path.dirname(os.path.abspath(out)), 'creditos.txt'), 'a') as fh:
        fh.write(f"{os.path.basename(out)}\tBundesarchiv, {sig} ({r['title'][:80]})\tCC BY-SA 3.0 DE\t\n")
    print('OK', out, im.size, '·', r['title'][:70])
