# Buscar y descargar imágenes de Wikimedia Commons (dominio público / licencias libres).
# Uso:
#   python3 commons.py search "Reichstag fire 1933" [n]     → lista título, licencia, tamaño
#   python3 commons.py get "File:Nombre.jpg" salida.jpg      → descarga a 2400 px de ancho y guarda la atribución
import json, sys, urllib.request, urllib.error, urllib.parse, os, re
API = 'https://commons.wikimedia.org/w/api.php'
UA = {'User-Agent': 'HistoriaDocBot/1.0 (https://claude.ai/code; educational documentary video tool) python-urllib'}
def call(**p):
    p.update(format='json', formatversion=2)
    req = urllib.request.Request(API + '?' + urllib.parse.urlencode(p), headers=UA)
    return json.load(fetch(req))
def fetch(req):
    import time
    for k in range(10):
        try:
            time.sleep(20)
            return urllib.request.urlopen(req, timeout=120)
        except urllib.error.HTTPError as e:
            if e.code != 429 or k == 9: raise
            time.sleep(int(e.headers.get('Retry-After') or 10 * (k + 1)))
def info(titles, width=1920):
    r = call(action='query', prop='imageinfo', titles='|'.join(titles), iiprop='url|size|extmetadata', iiurlwidth=width)
    for pg in r['query']['pages']:
        if 'imageinfo' not in pg: continue
        ii = pg['imageinfo'][0]; m = ii.get('extmetadata', {})
        g = lambda k: re.sub('<[^>]+>', '', m.get(k, {}).get('value', '')).strip()
        yield pg['title'], ii, g('LicenseShortName'), g('Artist')[:60], g('DateTimeOriginal')[:20]
cmd = sys.argv[1]
if cmd == 'search':
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    r = call(action='query', list='search', srsearch=sys.argv[2] + ' filetype:bitmap', srnamespace=6, srlimit=n)
    titles = [x['title'] for x in r['query']['search']]
    for t, ii, lic, art, date in info(titles, 400) if titles else []:
        print(f"{ii['width']}x{ii['height']} | {lic} | {date} | {t}")
elif cmd == 'get':
    t, out = sys.argv[2], sys.argv[3]
    for title, ii, lic, art, date in info([t]):
        # original si no es enorme; si no, miniatura de tamaño estándar (1920) para no saturar a Wikimedia
        url = ii['url'] if ii['width'] <= 3200 or not ii.get('thumburl') else ii['thumburl']
        data = fetch(urllib.request.Request(url, headers=UA)).read()
        open(out, 'wb').write(data)
        with open(os.path.join(os.path.dirname(os.path.abspath(out)), 'creditos.txt'), 'a') as f:
            f.write(f"{os.path.basename(out)}\t{title}\t{lic}\t{art}\n")
        print('OK', out, lic, ii['width'], 'x', ii['height'])
