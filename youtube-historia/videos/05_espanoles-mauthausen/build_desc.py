# Genera descripcion.txt del episodio 5 (capítulos calculados con los tiempos reales de la voz)
import os, json, re
here = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(here, 'spec.json'))); al = json.load(open(os.path.join(here, 'align.json')))
starts, off = [], 0
for s in spec['scenes']:
    starts.append(al['character_start_times_seconds'][min(off, len(al['characters']) - 1)]); off += len(s['say'].strip()) + 1
CAP = [(0, 'Los españoles olvidados'), (2, 'La Retirada (1939)'), (4, 'Los campos de la playa'), (8, 'Trabajadores y soldados en Francia'),
       (10, '1940: Francia cae'), (13, 'De los Stalag a Mauthausen'), (15, 'El convoy de los 927'), (19, 'El régimen de Franco'),
       (24, 'Mauthausen: el campo del granito'), (28, 'El triángulo azul'), (32, 'La escalera de la muerte'), (36, 'Gusen, el infierno del infierno'),
       (40, 'La solidaridad de los españoles'), (43, 'Francisco Boix y las fotos de las SS'), (48, 'La liberación (5 de mayo de 1945)'),
       (54, 'Boix en Núremberg'), (58, 'El exilio y el olvido'), (62, 'La lista del BOE (2019)'), (65, 'Conclusión')]
mmss = lambda t: f'{int(t // 60)}:{int(t % 60):02d}'
cap = '\n'.join(f'{mmss(0 if i == 0 else max(0, starts[i] - 0.25))} {t}' for i, t in CAP)
usadas = {os.path.basename(x) for sc in spec['scenes'] for x in (sc.get('img'), sc.get('bg')) if x}
cred = {}
for l in open(os.path.join(here, 'img', 'creditos.txt')):
    n, t, lic, art = (l.rstrip('\n').split('\t') + ['', '', '', ''])[:4]
    if n not in usadas: continue
    t = t.replace('File:', '')
    if t.startswith('Bundesarchiv'): t = t.split(' (')[0]
    if '\\u' in t: t = t.encode('latin-1', 'backslashreplace').decode('unicode_escape')
    t = re.sub(r' \(\)', '', t).replace('\\/', '/')
    if t.startswith('Bundesarchiv'): t = t.split(' (')[0]  # solo la signatura: la descripción no puede pasar de 5.000 caracteres
    art = '' if 'Unknown' in art else art.split(' (')[0]
    cred[n] = f"- {t} ({lic}{', ' + art if art else ''})"
titulo = '4.427 españoles murieron en un campo nazi. Casi nadie los recuerda'
desc = f"""Unos 7.500 republicanos españoles pasaron por el campo de concentración nazi de Mauthausen y sus subcampos, y más de 4.400 murieron allí, la mayoría en Gusen. Habían perdido la Guerra Civil, cruzado a Francia en la Retirada de 1939 y caído prisioneros en 1940. El régimen de Franco no los reclamó. Esta es su historia: el convoy de los 927, la escalera de la muerte, la solidaridad que salvó vidas y el fotógrafo Francisco Boix, que sacó a escondidas las fotos de las SS y declaró en Núremberg.

📌 Capítulo 5 de la serie sobre el nazismo y la Segunda Guerra Mundial. Anterior: La Noche de los cristales rotos. Próximo: 1 de septiembre de 1939, el día que empezó la guerra.

⏱️ Capítulos
{cap}

📚 Fuentes
- Memorial de Mauthausen (mauthausen-memorial.org): historia del campo, cantera Wiener Graben, juicios a los responsables
- BOE, 9 de agosto de 2019: lista de 4.427 españoles fallecidos en Mauthausen y Gusen (Registro Civil Central)
- Ministerio de Memoria Democrática: «Rotspaniers» y españoles deportados a los campos nazis
- United States Holocaust Memorial Museum (USHMM): Francisco Boix
- Actas del Tribunal Militar Internacional de Núremberg (Proyecto Avalon, Universidad de Yale), sesión del 29 de enero de 1946
- Benito Bermejo y Sandra Checa, «Libro memorial. Españoles deportados a los campos nazis (1940-1945)»; Montse Armengou y Ricard Belis, «El convoy de los 927»
Las cifras de la Retirada, del convoy de Angulema y de los deportados varían ligeramente según la fuente; usamos las más citadas y formulaciones aproximadas («unos», «más de»).

🖼️ Imágenes: Bundesarchiv, archivo federal alemán (licencia CC BY-SA 3.0 DE; muchas son fotos tomadas por las propias SS en Mauthausen), y Wikimedia Commons.
{chr(10).join(cred.values())}

Contenido histórico y educativo. Este canal no hace apología de ninguna ideología: contamos la historia para que no se repita.

#historia #mauthausen #republicanos #segundaguerramundial #documental"""
tags = 'españoles de mauthausen, mauthausen, gusen, republicanos españoles, francisco boix, convoy de los 927, rotspanier, exilio republicano, holocausto, segunda guerra mundial, documental, historia'

open(os.path.join(here, 'descripcion.txt'), 'w').write(f"TÍTULO\n{titulo}\n\nDESCRIPCIÓN\n{desc}\n\nETIQUETAS\n{tags}\n")
print('OK descripcion.txt ·', len(titulo), 'car. título ·', len(desc), 'car. descripción')
