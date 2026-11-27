# Genera descripcion.txt del episodio 4 (capítulos calculados con los tiempos reales de la voz)
import os, json, re
here = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(here, 'spec.json'))); al = json.load(open(os.path.join(here, 'align.json')))
starts, off = [], 0
for s in spec['scenes']:
    starts.append(al['character_start_times_seconds'][min(off, len(al['characters']) - 1)]); off += len(s['say'].strip()) + 1
CAP = [(0, 'Una sola noche'), (2, 'Los judíos de Alemania (1933-1937)'), (7, '1938: Austria, Évian y la J roja'), (13, 'La expulsión de los judíos polacos'),
       (17, 'Herschel Grynszpan y el disparo de París'), (22, '9 de noviembre: el discurso de Goebbels'), (26, 'Las órdenes de Heydrich'), (28, 'Arden las sinagogas'),
       (33, 'Los cristales rotos'), (38, 'Baden-Baden y las detenciones'), (40, '30.000 hombres a los campos'), (43, 'Göring: la multa de mil millones'),
       (48, 'La reacción del mundo y el Kindertransport'), (52, 'El viaje del St. Louis'), (54, 'Qué fue de Grynszpan'), (56, '¿Kristallnacht o pogromo?'),
       (57, 'El camino hacia el Holocausto'), (60, 'Conclusión')]
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
    if t.startswith('Bundesarchiv'): t = t.split(' (')[0]  # solo la signatura: la descripción no puede pasar de 5.000 caracteres
    art = '' if 'Unknown' in art else art.split(' (')[0]
    cred[n] = f"- {t} ({lic}{', ' + art if art else ''})"
titulo = 'La noche que anunció el Holocausto'
desc = f"""En la noche del 9 al 10 de noviembre de 1938 ardieron o fueron destrozadas más de 1.400 sinagogas y casas de oración en Alemania y Austria, unos 7.500 comercios judíos acabaron con los escaparates rotos y unos 30.000 hombres fueron enviados a campos de concentración. Así fue el pogromo de noviembre: el disparo de Herschel Grynszpan en París, el discurso de Goebbels, las órdenes de Heydrich y la factura que se obligó a pagar a las víctimas.

📌 Capítulo 4 de la serie sobre el nazismo y la Segunda Guerra Mundial. Anterior: Auschwitz por dentro. Próximo: Los españoles de Mauthausen.

⏱️ Capítulos
{cap}

📚 Fuentes
- United States Holocaust Memorial Museum (USHMM): Kristallnacht, expulsión de judíos polacos (Zbaszyn), Kindertransport, viaje del St. Louis
- Bundeszentrale für politische Bildung (bpb) y Deutsches Historisches Museum (LeMO): Novemberpogrom 1938
- Actas de la reunión del 12 de noviembre de 1938 (documento 1816-PS, Proyecto Avalon, Universidad de Yale)
- Encyclopaedia Britannica
Las cifras de sinagogas, comercios y víctimas son las más citadas por estas fuentes; algunas varían ligeramente según el estudio.

🖼️ Imágenes: Bundesarchiv, archivo federal alemán (licencia CC BY-SA 3.0 DE), y Wikimedia Commons.
{chr(10).join(cred.values())}

Contenido histórico y educativo. Este canal no hace apología de ninguna ideología: contamos la historia para que no se repita.

#historia #holocausto #kristallnacht #segundaguerramundial #documental"""
tags = 'noche de los cristales rotos, kristallnacht, pogromo de noviembre, 1938, holocausto, nazismo, goebbels, herschel grynszpan, segunda guerra mundial, documental, historia, kindertransport'

open(os.path.join(here, 'descripcion.txt'), 'w').write(f"TÍTULO\n{titulo}\n\nDESCRIPCIÓN\n{desc}\n\nETIQUETAS\n{tags}\n")
print('OK descripcion.txt ·', len(titulo), 'car. título ·', len(desc), 'car. descripción')
