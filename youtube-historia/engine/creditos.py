# Bloque de créditos para la descripción de YouTube: solo las fotos y clips que usa el spec
# (img, bg, clip e imgs: [...]), de img/, clips/ y personas/. Bundesarchiv en una línea (límite de 5.000 caracteres).
import os, re
def bloque(here, spec):
    usadas = set()
    for sc in spec['scenes']:
        for x in [sc.get('img'), sc.get('bg'), sc.get('clip')] + [l.get('img') or l.get('clip') for l in sc.get('imgs', [])]:
            if x: usadas.add(os.path.normpath(x))
    root = os.path.abspath(os.path.join(here, '..', '..'))
    ba, fotos, pelis = [], {}, {}
    for carpeta, rel in [(os.path.join(here, 'img'), 'img'), (os.path.join(here, 'clips'), 'clips'), (os.path.join(root, 'personas'), 'personas')]:
        f = os.path.join(carpeta, 'creditos.txt')
        if not os.path.exists(f): continue
        for l in open(f):
            n, t, lic, art = (l.rstrip('\n').split('\t') + ['', '', '', ''])[:4]
            if os.path.normpath(os.path.join(rel, n)) not in usadas: continue
            t = t.replace('File:', '').replace('Wikimedia Commons, ', '')
            if t.startswith('Bundesarchiv'): ba.append(t.split(' (')[0].replace('Bundesarchiv, ', '')); continue
            if '\\u' in t:
                try: t = t.encode('latin-1', 'backslashreplace').decode('unicode_escape')
                except UnicodeDecodeError: pass
            t = re.sub(r' \(\)', '', t).replace('\\/', '/')
            if rel == 'clips':
                t = re.sub(r'\.(webm|ogv)$', '', t).replace('_', ' '); pelis[t] = f'- {t} (película, dominio público en EE. UU.; vía Wikimedia Commons)'; continue
            t = re.sub(r'\.(jpe?g|png|tif)$', '', t, flags=re.I).replace('_', ' ')
            art = '' if 'Unknown' in art else art.split(' (')[0]
            lic = 'dominio público' if 'público' in lic.lower() or 'public' in lic.lower() else '' if 'ver licencia' in lic else lic
            fotos[t] = f'- {t}' + (f' ({lic}{", " + art if art else ""})' if lic or art else '')
    out = ['🖼️ Imágenes y vídeo de archivo (Wikimedia Commons, salvo indicación):']
    out += sorted(pelis.values()) + sorted(fotos.values())
    if ba: out.append(f"- Bundesarchiv, archivo federal alemán (CC BY-SA 3.0 DE): {', '.join(sorted(set(ba)))}")
    return '\n'.join(out)
