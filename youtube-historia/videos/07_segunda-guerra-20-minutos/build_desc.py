# Genera descripcion.txt del episodio 7 (capítulos calculados con los tiempos reales de la voz)
import os, json, re
here = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(here, 'spec.json'))); al = json.load(open(os.path.join(here, 'align.json')))
starts, off = [], 0
for s in spec['scenes']:
    starts.append(al['character_start_times_seconds'][min(off, len(al['characters']) - 1)]); off += len(s['say'].strip()) + 1
CAP = [(0, 'Seis años y un día'), (2, '1939: Polonia'), (6, '1940: la caída de Francia'), (11, 'La batalla de Inglaterra y el Blitz'), (14, 'Hendaya: Franco y Hitler'),
       (15, 'Italia, Rommel y el norte de África'), (17, '1941: Operación Barbarroja'), (23, 'El Holocausto'), (25, 'Pearl Harbor'), (28, '1942: Japón y Midway'),
       (30, 'Stalingrado'), (34, 'El Alamein'), (35, '1943: Kursk e Italia'), (39, '1944: el Día D'), (41, 'Bagration y la liberación de París'),
       (43, 'Stauffenberg y las Ardenas'), (45, 'El Pacífico'), (46, '1945: Auschwitz, Yalta y Berlín'), (50, 'Hiroshima y Nagasaki'), (53, 'La rendición de Japón'),
       (54, 'El balance'), (56, 'El mundo después'), (57, 'Conclusión')]
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
titulo = 'Toda la Segunda Guerra Mundial en 20 minutos | Documental'
desc = f"""Seis años y un día: del 1 de septiembre de 1939 al 2 de septiembre de 1945. En este documental te cuento toda la Segunda Guerra Mundial en unos 20 minutos: la invasión de Polonia, la caída de Francia, la batalla de Inglaterra, Hendaya, la Operación Barbarroja, el Holocausto, Pearl Harbor, Midway, Stalingrado, El Alamein, Kursk, el Día D, la liberación de París con los españoles de la Nueve, la caída de Berlín, Hiroshima y Nagasaki.

📌 Capítulo 7 de la serie sobre el nazismo y la Segunda Guerra Mundial. Anterior: 1 de septiembre de 1939. Próximo: Operación Barbarroja, el mayor error de Hitler.

⏱️ Capítulos
{cap}

📚 Fuentes
- Encyclopaedia Britannica: Segunda Guerra Mundial (costes de la guerra), Operación Barbarroja, asedio de Leningrado, Hiroshima
- Imperial War Museum: Dunkerque y el Blitz
- United States Holocaust Memorial Museum (USHMM): el Holocausto y la liberación de Auschwitz
- National Archives (EE. UU.) y The National WWII Museum: Pearl Harbor y el Día D
Las cifras de víctimas de la guerra son estimaciones y varían mucho según la fuente (el total va de unos 60 a más de 70 millones; Hiroshima y Nagasaki, según los cálculos a finales de 1945). Usamos las más citadas y formulaciones prudentes.

🖼️ Imágenes: Bundesarchiv, archivo federal alemán (CC BY-SA 3.0 DE) y Wikimedia Commons.
{chr(10).join(cred.values())}

Contenido histórico y educativo. Este canal no hace apología de ninguna ideología: contamos la historia para que no se repita.

#historia #segundaguerramundial #ww2 #documental #historiaenespañol"""
tags = 'segunda guerra mundial, segunda guerra mundial resumen, ww2, documental, historia, hitler, stalingrado, dia d, pearl harbor, hiroshima, barbarroja, holocausto'

open(os.path.join(here, 'descripcion.txt'), 'w').write(f"TÍTULO\n{titulo}\n\nDESCRIPCIÓN\n{desc}\n\nETIQUETAS\n{tags}\n")
print('OK descripcion.txt ·', len(titulo), 'car. título ·', len(desc), 'car. descripción')
