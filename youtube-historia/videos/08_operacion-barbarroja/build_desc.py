# Genera descripcion.txt del episodio 8 (capítulos calculados con los tiempos reales de la voz)
import os, json, re
here = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(here, 'spec.json'))); al = json.load(open(os.path.join(here, 'align.json')))
starts, off = [], 0
for s in spec['scenes']:
    starts.append(al['character_start_times_seconds'][min(off, len(al['characters']) - 1)]); off += len(s['say'].strip()) + 1
CAP = [(0, '22 de junio de 1941, 3:15'), (2, 'El espacio vital'), (4, 'Del pacto a la directiva 21'), (7, 'Una campaña rápida'), (9, 'El plan del hambre y la orden de los comisarios'),
       (11, 'Stalin no quiso creerlo'), (13, 'El mayor ejército de la historia'), (15, 'El primer día'), (18, 'Cercos y prisioneros'), (23, 'Smolensk: el primer frenazo'),
       (26, 'Fábricas hacia los Urales'), (27, 'Kiev'), (29, 'Babi Yar'), (31, 'Leningrado y la División Azul'), (34, 'Operación Tifón'),
       (36, 'El barro'), (38, 'El desfile del 7 de noviembre'), (39, 'A 30 km del Kremlin'), (40, 'El invierno'), (43, 'La contraofensiva'),
       (46, 'El balance'), (48, '¿Por qué fue su mayor error?'), (51, 'Conclusión')]
mmss = lambda t: f'{int(t // 60)}:{int(t % 60):02d}'
cap = '\n'.join(f'{mmss(0 if i == 0 else max(0, starts[i] - 0.25))} {t}' for i, t in CAP)
import sys; sys.path.insert(0, os.path.join(here, '..', '..', 'engine')); import creditos
CRED = creditos.bloque(here, spec)
titulo = 'El día que Hitler firmó su derrota sin saberlo'
desc = f"""El 22 de junio de 1941, más de 3 millones de soldados alemanes invadieron la Unión Soviética. Hitler creía que bastaba «una patada a la puerta». Seis meses después, su ejército se congelaba a las puertas de Moscú. En este documental: la directiva n.º 21, el plan del hambre, los avisos que Stalin ignoró, los grandes cercos, el destino de los prisioneros soviéticos, Kiev y Babi Yar, el asedio de Leningrado, la División Azul, la Operación Tifón, el barro, el invierno y la contraofensiva de Zhúkov.

📌 Capítulo 8 de la serie sobre el nazismo y la Segunda Guerra Mundial. Anterior: Toda la Segunda Guerra Mundial en 20 minutos. Próximo: Stalingrado.

⏱️ Capítulos
{cap}

📚 Fuentes
- German History in Documents and Images (GHI) y Proyecto Núremberg de Harvard: directiva n.º 21 (18 de diciembre de 1940)
- United States Holocaust Memorial Museum (USHMM): prisioneros de guerra soviéticos, Kiev y Babi Yar
- Encyclopaedia Britannica: Operación Barbarroja, batalla de Moscú, asedio de Leningrado
- Deutsches Historisches Museum (LeMO) y World History Encyclopedia: Kiev y Viazma
Muchas cifras (aviones destruidos el primer día, prisioneros de Kiev, víctimas de Leningrado) proceden de fuentes alemanas o soviéticas de la época y varían según la fuente; usamos las más citadas y formulaciones prudentes. La frase de la «patada a la puerta» se atribuye a Hitler en varias fuentes, pero no está en un documento oficial.

{CRED}

Contenido histórico y educativo. Este canal no hace apología de ninguna ideología: contamos la historia para que no se repita.

#historia #segundaguerramundial #barbarroja #documental #historiaenespañol"""
tags = 'operacion barbarroja, segunda guerra mundial, frente oriental, hitler, stalin, batalla de moscu, leningrado, babi yar, division azul, zhukov, documental, historia'

open(os.path.join(here, 'descripcion.txt'), 'w').write(f"TÍTULO\n{titulo}\n\nDESCRIPCIÓN\n{desc}\n\nETIQUETAS\n{tags}\n")
print('OK descripcion.txt ·', len(titulo), 'car. título ·', len(desc), 'car. descripción')
