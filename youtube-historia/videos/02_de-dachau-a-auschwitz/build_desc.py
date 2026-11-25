# Genera descripcion.txt del episodio 2 (capítulos calculados con los tiempos reales de la voz)
import os, json, re
here = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(here, 'spec.json'))); al = json.load(open(os.path.join(here, 'align.json')))
starts, off = [], 0
for s in spec['scenes']:
    starts.append(al['character_start_times_seconds'][min(off, len(al['characters']) - 1)]); off += len(s['say'].strip()) + 1
CAP = [(0, '1933: el primer día de Dachau'), (2, 'Custodia protectora y campos salvajes'), (5, 'Himmler y el campo de Dachau'),
       (7, 'Theodor Eicke y la escuela de Dachau'), (10, 'El código de los triángulos'), (12, 'Los grandes campos (1936-1939)'),
       (14, 'Los españoles de Mauthausen'), (16, 'La Noche de los cristales rotos'), (18, 'La guerra y el nacimiento de Auschwitz'),
       (21, 'Zyklon B y Birkenau'), (23, 'Los centros de exterminio'), (25, 'La Conferencia de Wannsee'), (26, 'La selección en Auschwitz-Birkenau'),
       (29, 'La liberación'), (31, 'Conclusión')]
mmss = lambda t: f'{int(t // 60)}:{int(t % 60):02d}'
cap = '\n'.join(f'{mmss(0 if i == 0 else max(0, starts[i] - 0.25))} {t}' for i, t in CAP)
usadas = {os.path.basename(x) for sc in spec['scenes'] for x in (sc.get('img'), sc.get('bg')) if x}
cred = {}
for l in open(os.path.join(here, 'img', 'creditos.txt')):
    n, t, lic, art = (l.rstrip('\n').split('\t') + ['', '', '', ''])[:4]
    if n not in usadas: continue
    t = t.replace('File:', '')
    if '\\u' in t: t = t.encode('latin-1', 'backslashreplace').decode('unicode_escape')
    t = re.sub(r' \(\)', '', t).replace('\\/', '/')
    art = '' if 'Unknown' in art else art.split(' (')[0]
    cred[n] = f"- {t} ({lic}{', ' + art if art else ''})"
titulo = 'De Dachau a Auschwitz: cómo nacieron los campos de concentración nazis | Documental'
desc = f"""El 22 de marzo de 1933 llegaron a Dachau unos 200 presos políticos. Doce años después, solo en Auschwitz habían sido asesinadas más de 1,1 millones de personas. Así nació, paso a paso, el sistema de campos nazi: de las primeras detenciones sin juicio a los centros de exterminio.

📌 Capítulo 2 de la serie sobre el nazismo y la Segunda Guerra Mundial. Anterior: cómo Hitler llegó al poder. Próximo: Auschwitz por dentro.

⏱️ Capítulos
{cap}

📚 Fuentes
- United States Holocaust Memorial Museum (USHMM): Dachau, Sachsenhausen, Kristallnacht, Auschwitz (fechas clave), Centros de exterminio, El sistema de campos nazi
- Memorial y Museo de Auschwitz-Birkenau
- Estudios sobre la deportación de republicanos españoles a Mauthausen (las cifras varían según la fuente)
Algunas cifras de víctimas son estimaciones y varían ligeramente según la fuente.

🖼️ Imágenes: Bundesarchiv, archivo federal alemán (licencia CC BY-SA 3.0 DE), y Wikimedia Commons.
{chr(10).join(cred.values())}

Contenido histórico y educativo. Este canal no hace apología de ninguna ideología: contamos la historia para que no se repita.

#historia #holocausto #segundaguerramundial #auschwitz #documental"""
tags = 'historia, holocausto, campos de concentración, auschwitz, dachau, segunda guerra mundial, nazismo, mauthausen, españoles en mauthausen, documental, noche de los cristales rotos'
open(os.path.join(here, 'descripcion.txt'), 'w').write(f"TÍTULO\n{titulo}\n\nDESCRIPCIÓN\n{desc}\n\nETIQUETAS\n{tags}\n")
print('OK descripcion.txt ·', len(titulo), 'car. título ·', len(desc), 'car. descripción')
