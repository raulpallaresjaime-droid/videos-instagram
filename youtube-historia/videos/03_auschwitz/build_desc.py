# Genera descripcion.txt del episodio 3 (capítulos calculados con los tiempos reales de la voz)
import os, json, re
here = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(here, 'spec.json'))); al = json.load(open(os.path.join(here, 'align.json')))
starts, off = [], 0
for s in spec['scenes']:
    starts.append(al['character_start_times_seconds'][min(off, len(al['characters']) - 1)]); off += len(s['say'].strip()) + 1
CAP = [(0, 'Auschwitz: 1,1 millones de víctimas'), (2, '1940: el origen del campo'), (8, 'Auschwitz I: Arbeit macht frei y el bloque 11'),
       (12, 'Witold Pilecki, el hombre que entró voluntario'), (14, '1941: el Zyklon B'), (16, 'Birkenau'), (20, 'La solución final y las cámaras de gas'),
       (23, 'Los trenes de toda Europa'), (25, 'La selección en el andén'), (29, 'Sonderkommando y «Canadá»'), (31, 'El número tatuado y la vida en el campo'),
       (34, 'IG Farben, Monowitz y Primo Levi'), (38, 'Josef Mengele'), (40, 'El genocidio de los gitanos'), (43, '1944: los judíos de Hungría'),
       (48, 'Ana Frank'), (49, 'Resistencia: Vrba, Wetzler y la revuelta'), (53, 'El final y las marchas de la muerte'), (55, 'La liberación'),
       (57, 'Las cifras'), (60, 'Qué fue de Höss'), (62, 'Conclusión')]
mmss = lambda t: f'{int(t // 60)}:{int(t % 60):02d}'
cap = '\n'.join(f'{mmss(0 if i == 0 else max(0, starts[i] - 0.25))} {t}' for i, t in CAP)
# créditos de todas las imágenes y clips usados (img, bg e imgs: [...], también de personas/ y clips/)
usadas = set()
for sc in spec['scenes']:
    for x in [sc.get('img'), sc.get('bg'), sc.get('clip')] + [l.get('img') or l.get('clip') for l in sc.get('imgs', [])]:
        if x: usadas.add(os.path.normpath(x))
root = os.path.abspath(os.path.join(here, '..', '..'))
ba, cred, grupos = [], {}, {}
for carpeta, rel in [(os.path.join(here, 'img'), 'img'), (os.path.join(here, 'clips'), 'clips'), (os.path.join(root, 'personas'), 'personas')]:
    f = os.path.join(carpeta, 'creditos.txt')
    if not os.path.exists(f): continue
    for l in open(f):
        n, t, lic, art = (l.rstrip('\n').split('\t') + ['', '', '', ''])[:4]
        if os.path.normpath(os.path.join(rel, n)) not in usadas: continue
        t = t.replace('File:', '').replace('Wikimedia Commons, ', '')
        if '\\u' in t: t = t.encode('latin-1', 'backslashreplace').decode('unicode_escape')
        t = re.sub(r' \(\)', '', t).replace('\\/', '/')
        if t.startswith('Bundesarchiv'):  # solo la signatura, todas en una línea (límite de 5.000 caracteres)
            ba.append(t.split(' (')[0].replace('Bundesarchiv, ', '')); continue
        if n.startswith('alb_'): grupos.setdefault('Álbum de Auschwitz (SS, 1944; dominio público)', 0); grupos['Álbum de Auschwitz (SS, 1944; dominio público)'] += 1; continue
        if n.startswith(('hoss', 'mengele', 'solahutte')): grupos.setdefault('Álbum Höcker (1944; dominio público, USHMM)', 0); grupos['Álbum Höcker (1944; dominio público, USHMM)'] += 1; continue
        if rel == 'clips':
            t = re.sub(r'\.webm$', '', t).replace('_', ' '); cred[t] = f"- {t} (película, dominio público; vía NARA y Wikimedia Commons)"; continue
        else: t = re.sub(r'\.(jpe?g|png|tif)$', '', t, flags=re.I).replace('_', ' ')
        art = '' if 'Unknown' in art else art.split(' (')[0]
        lic = 'dominio público' if 'público' in lic.lower() or 'public' in lic.lower() else '' if 'ver licencia' in lic else lic
        cred[t] = f"- {t}" + (f" ({lic}{', ' + art if art else ''})" if lic or art else '')
titulo = 'Así funcionaba Auschwitz: la fábrica de muerte nazi por dentro'
desc = f"""Al menos 1,3 millones de personas fueron deportadas a Auschwitz. Más de 1,1 millones nunca salieron. Entramos en el mayor campo de exterminio nazi para entender cómo funcionaba: los trenes, la selección en el andén, el número tatuado, el trabajo esclavo para IG Farben, la resistencia y la liberación.

📌 Capítulo 3 de la serie sobre el nazismo y la Segunda Guerra Mundial. Anterior: De Dachau a Auschwitz. Próximo: La Noche de los cristales rotos.

⏱️ Capítulos
{cap}

📚 Fuentes
- Memorial y Museo de Auschwitz-Birkenau (auschwitz.org): número de víctimas (estudios de Franciszek Piper), topografía del campo, selecciones, evacuación y liberación
- United States Holocaust Memorial Museum (USHMM): Auschwitz, tatuajes y números, deportación de judíos de Hungría, revuelta de 1944
- Encyclopaedia Britannica: Auschwitz, Rudolf Höss, informe Vrba-Wetzler
Las cifras de víctimas son estimaciones de los historiadores y pueden variar ligeramente según la fuente.

🖼️ Imágenes y vídeo de archivo (Wikimedia Commons, salvo indicación):
{chr(10).join(f'- {g}: {k} fotos' for g, k in grupos.items())}
{chr(10).join(sorted(cred.values()))}
- Bundesarchiv, archivo federal alemán (CC BY-SA 3.0 DE): {', '.join(sorted(set(ba)))}

Contenido histórico y educativo. Este canal no hace apología de ninguna ideología: contamos la historia para que no se repita.

#historia #holocausto #auschwitz #segundaguerramundial #documental"""
tags = 'auschwitz, auschwitz birkenau, holocausto, campos de concentración, segunda guerra mundial, nazismo, documental, historia, rudolf höss, mengele, ana frank, primo levi, pilecki'

open(os.path.join(here, 'descripcion.txt'), 'w').write(f"TÍTULO\n{titulo}\n\nDESCRIPCIÓN\n{desc}\n\nETIQUETAS\n{tags}\n")
print('OK descripcion.txt ·', len(titulo), 'car. título ·', len(desc), 'car. descripción')
