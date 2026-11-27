# Genera descripcion.txt del episodio 6 (capítulos calculados con los tiempos reales de la voz)
import os, json, re
here = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(here, 'spec.json'))); al = json.load(open(os.path.join(here, 'align.json')))
starts, off = [], 0
for s in spec['scenes']:
    starts.append(al['character_start_times_seconds'][min(off, len(al['characters']) - 1)]); off += len(s['say'].strip()) + 1
CAP = [(0, 'Las 4:45 del 1 de septiembre'), (2, 'Danzig y el corredor polaco'), (5, '1939: la garantía a Polonia'), (9, 'El pacto Ribbentrop-Mólotov'),
       (11, 'Obersalzberg y el ataque aplazado'), (14, 'La Directiva n.º 1'), (15, 'Gleiwitz: el ataque falso'), (19, 'Tczew, Wielun y Westerplatte'),
       (23, 'Fuerzas y guerra relámpago'), (26, 'El mito de la caballería polaca'), (29, 'Los correos de Danzig'), (31, 'Los siete días de Westerplatte'),
       (33, 'El discurso de Hitler'), (36, '3 de septiembre: Reino Unido y Francia declaran la guerra'), (40, 'La guerra de broma'),
       (42, 'El terror contra los civiles'), (45, '17 de septiembre: la URSS invade Polonia'), (48, 'La caída de Varsovia'), (52, 'El balance'),
       (55, 'Enigma: el legado polaco'), (57, 'Conclusión')]
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
titulo = '1 de septiembre de 1939: el día que empezó la Segunda Guerra Mundial | Documental'
desc = f"""A las 4:45 de la madrugada del 1 de septiembre de 1939, el acorazado Schleswig-Holstein abrió fuego contra Westerplatte y Alemania invadió Polonia. Así empezó la Segunda Guerra Mundial. En este documental: el pacto secreto entre Hitler y Stalin, el ataque falso de Gleiwitz, el bombardeo de Wielun, la resistencia de Westerplatte y de los correos de Danzig, el mito de la caballería polaca, el ultimátum británico, la invasión soviética y la caída de Varsovia.

📌 Capítulo 6 de la serie sobre el nazismo y la Segunda Guerra Mundial. Anterior: Los españoles de Mauthausen. Próximo: Toda la Segunda Guerra Mundial en 20 minutos.

⏱️ Capítulos
{cap}

📚 Fuentes
- Museo de la Segunda Guerra Mundial de Gdansk e Instituto de la Memoria Nacional de Polonia (IPN)
- Proyecto Avalon (Universidad de Yale): protocolo secreto del pacto germano-soviético, Directiva n.º 1, Libro Azul británico
- United States Holocaust Memorial Museum (USHMM) y Deutsches Historisches Museum (LeMO)
- Encyclopaedia Britannica y The National WWII Museum: la invasión de Polonia
- GCHQ: la reunión de Pyry (julio de 1939) y Enigma
Algunas horas (4:30, 4:40, 4:45) y cifras de víctimas varían según la fuente; usamos las más citadas y formulaciones prudentes. La frase sobre los armenios del 22 de agosto de 1939 se conoce por un solo resumen de aquella reunión y su autenticidad está discutida.

🖼️ Imágenes: Bundesarchiv, archivo federal alemán (licencia CC BY-SA 3.0 DE).
{chr(10).join(cred.values())}

Contenido histórico y educativo. Este canal no hace apología de ninguna ideología: contamos la historia para que no se repita.

#historia #segundaguerramundial #polonia #1939 #documental"""
tags = '1 de septiembre de 1939, invasión de polonia, segunda guerra mundial, westerplatte, gleiwitz, pacto ribbentrop molotov, danzig, blitzkrieg, hitler, stalin, documental, historia'

open(os.path.join(here, 'descripcion.txt'), 'w').write(f"TÍTULO\n{titulo}\n\nDESCRIPCIÓN\n{desc}\n\nETIQUETAS\n{tags}\n")
print('OK descripcion.txt ·', len(titulo), 'car. título ·', len(desc), 'car. descripción')
