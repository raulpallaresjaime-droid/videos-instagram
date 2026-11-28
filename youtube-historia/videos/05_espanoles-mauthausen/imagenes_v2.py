# Imágenes v2 del capítulo 5 (normas de imagen de Raúl: más imágenes, caras con rótulo, clips, sin repetir para rellenar).
# Reutiliza la voz: no cambia ningún `say`. Uso:  python3 build_spec.py && python3 imagenes_v2.py
# Las capas sin `cue` se reparten a partes iguales en la escena. Si un archivo no existe, la capa se omite.
import json, os
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
spec = json.load(open(os.path.join(here, 'spec.json')))
S = spec['scenes']

def ok(p): return os.path.exists(os.path.join(here, p)) or os.path.exists(os.path.join(root, p))
def L(src, cue=None, **kw):
    d = {('clip' if src.endswith('.mp4') else 'img'): src, **kw}
    if cue: d['cue'] = cue
    return d
def who(name, role): return {'name': name, 'role': role}
C, I, P = 'clips/', 'img/', 'personas/'

M = {
 0: ([L(I+'escalera.jpg'), L(I+'m_cantera_g2.jpg'), L(I+'lib_vitorean.jpg', cap='Presos de Mauthausen reciben a los soldados estadounidenses, mayo de 1945')], {'shade': True}),
 1: ([L(I+'cantera3.jpg')], {}),
 2: ([L(I+'arg_heridos.jpg', cap='Republicanos heridos cruzan los Pirineos, febrero de 1939'), L(I+'retirada3.jpg')], {}),
 3: ([L(I+'arg_columna.jpg', cap='Columna de refugiados españoles llega a Francia, 1939'), L(I+'retirada.jpg')], {}),
 4: ([L(I+'arg_entrada.jpg', cap='Republicanos a la entrada del campo de Argelès-sur-Mer, febrero de 1939'), L(I+'arg_alambradas.jpg', cap='Detrás de las alambradas, Argelès, 1939')], {}),
 5: ([L(I+'arg_abrigo.jpg', cap='Un refugiado ante su abrigo en la arena, Argelès, marzo de 1939'), L(I+'arg_pan.jpg', cap='El reparto de pan en el campo de Argelès, 1939')], {}),
 6: ([L(I+'arg_mujeres_ninos.jpg', cap='Refugiadas españolas con sus hijos, 1939'), L(I+'retirada2.jpg')], {}),
 7: ([L(I+'arg_entrada2.jpg', cap='Entrada del campo de Argelès, 1939'), L(I+'arg_panel.jpg', 'para los republicanos', cap='El panel de los desaparecidos en Argelès')], {}),
 8: ([L(I+'junio1940.jpg')], {}),
 9: ([L(I+'arg_pan.jpg', dark=True)], {}),
 10: ([L(I+'prisioneros_fr2.jpg')], {}),
 11: ([L(I+'prisioneros_fr.jpg')], {}),
 12: ([L(I+'prisioneros_fr.jpg', dark=True)], {}),
 14: ([L(I+'llegada.jpg'), L(I+'m_llegada_yugo2.jpg', 'son los')], {}),
 15: ([L(I+'retirada.jpg', dark=True)], {}),
 16: ([L(I+'llegada_gusen.jpg')], {}),
 19: ([L(I+'hendaya.jpg')], {}),
 20: ([L(I+'serrano1.jpg', 'serrano suner', who=who('Ramón Serrano Suñer', 'Ministro y cuñado de Franco'))], {}),
 22: ([L(I+'franco_himmler.jpg', cap='Himmler en Madrid con Franco, octubre de 1940'), L(I+'himmler_frontera.jpg', cap='Himmler llega a España, octubre de 1940')], {}),
 23: ([L(I+'himmler_mauth.jpg'), L(I+'m_himmler_visita.jpg', cap='Himmler visita Mauthausen, abril de 1941')], {}),
 24: ([L(I+'ss_muro.jpg'), L(I+'m_019.jpg')], {}),
 25: ([L(I+'m_018.jpg', cap='La cantera Wiener Graben'), L(I+'cantera5.jpg')], {}),
 26: ([L(I+'cantera1.jpg'), L(I+'m_cantera_g3.jpg')], {}),
 27: ([L(I+'appellplatz.jpg')], {}),
 28: ([L(I+'desinfeccion.jpg'), L(I+'m_llegada_yugo2.jpg', 'les rapaban', cap='Recién llegados a Mauthausen')], {}),
 29: ([L(I+'llegada.jpg', dark=True)], {}),
 30: ([L(I+'m_jovenes_appell2.jpg', cap='Presos jóvenes en la plaza de recuento de Mauthausen'), L(I+'m_jovenes_appell.jpg')], {}),
 31: ([L(I+'gusen_obras.jpg'), L(I+'patatas.jpg')], {}),
 32: ([L(I+'cantera6.jpg'), L(I+'m_cantera_g2.jpg')], {}),
 33: ([L(I+'escalera.jpg', cap='La «escalera de la muerte» de la cantera de Mauthausen')], {}),
 34: ([L(I+'cantera_v.jpg')], {}),
 35: ([L(I+'himmler_cantera.jpg'), L(I+'m_himmler_ziereis.jpg', cap='Ziereis recibe a Himmler en Mauthausen')], {}),
 36: ([L(I+'gusen_torre.jpg'), L(I+'gusen_aereo.jpg', 'gusen era', cap='Gusen I y II desde el aire')], {}),
 37: ([L(I+'m_gusen_barracones.jpg'), L(I+'m_gusen_letrinas.jpg', cap='Letrinas de un barracón de Gusen')], {}),
 38: ([L(I+'tuneles.jpg'), L(I+'m_003.jpg')], {}),
 40: ([L(I+'jovenes.jpg')], {}),
 41: ([L(I+'lavanderia.jpg')], {}),
 42: ([L(I+'jovenes.jpg', dark=True)], {}),
 43: ([L(I+'boix.jpg', 'francisco boix', who=who('Francisco Boix', 'Fotógrafo, preso en Mauthausen'))], {}),
 44: ([L(I+'ricken.jpg')], {}),
 45: ([L(I+'ziereis_grupo.jpg', cap='Mandos de las SS posan en Mauthausen'), L(I+'m_004.jpg')], {}),
 46: ([L(I+'m_005.jpg')], {}),
 47: ([L(I+'cantera2.jpg')], {}),
 48: ([L(I+'ziereis_ss.jpg')], {}),
 50: ([L(I+'liberacion2.jpg'), L(I+'lib_vitorean.jpg', 'patrulla', cap='Soldados de la 11.ª División Acorazada de EE. UU. en Mauthausen, mayo de 1945')], {}),
 51: ([L(I+'liberacion2.jpg')], {}),
 52: ([L(I+'lib_gusen.jpg', cap='Gusen tras la liberación, 1945'), L(I+'lib_mujeres.jpg', cap='El campo de mujeres de Mauthausen tras la liberación')], {}),
 53: ([L(I+'ziereis.jpg', 'ziereis', fy=0.25, who=who('Franz Ziereis', 'Comandante de Mauthausen'))], {}),
 54: ([L(C+'boix_estrado.mp4', cap='Francisco Boix declara en Núremberg, enero de 1946'), L(C+'tribunal.mp4')], {}),
 55: ([L(C+'tribunal2.mp4', cap='El tribunal de Núremberg'), L(I+'himmler_cantera.jpg')], {}),
 56: ([L(C+'boix_estrado2.mp4')], {}),
 57: ([L(I+'ss_muro.jpg')], {}),
 58: ([L(I+'arg_alambradas.jpg', dark=True)], {}),
 59: ([L(I+'ricken.jpg', dark=True)], {}),
}
for i, (layers, opts) in M.items():
    sc = S[i]
    layers = [x for x in layers if ok(x.get('img') or x.get('clip'))]
    if not layers: continue
    for k in ('img', 'bg', 'kb', 'fx', 'fy', 'clip', 'cap'): sc.pop(k, None)
    side = opts.get('side', sc.get('side')); sc.pop('side', None)
    if side: sc['side'] = side
    if 'shade' in opts and not all(x.get('dark') for x in layers): sc['shade'] = opts['shade']
    if all(x.get('dark') for x in layers): sc.pop('shade', None)
    sc['imgs'] = layers
    if side == 'right' and 'html' in sc: sc['html'] = sc['html'].replace('class="ov center"', 'class="ov left"')
    if not side and 'html' in sc: sc['html'] = sc['html'].replace('class="ov left"', 'class="ov center"').replace('class="ov right"', 'class="ov center"')

json.dump(spec, open(os.path.join(here, 'spec.json'), 'w'), ensure_ascii=False, indent=1)
n = sum(len(s.get('imgs', [])) or (1 if s.get('img') or s.get('bg') else 0) for s in S)
print(f'OK spec.json · {len(S)} escenas · {n} imágenes/clips')
