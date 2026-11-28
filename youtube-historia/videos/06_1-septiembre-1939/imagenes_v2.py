# Imágenes v2 del capítulo 6 (normas de imagen de Raúl: más imágenes, caras con rótulo, clips, sin repetir para rellenar).
# Reutiliza la voz: no cambia ningún `say`. Uso:  python3 build_spec.py && python3 imagenes_v2.py
# Las capas sin `cue` se reparten a partes iguales en la escena. Si un archivo no existe, la capa se omite.
import json, os, unicodedata
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
WWF = ' · «Why We Fight»'

M = {
 0: ([L(I+'schleswig1.jpg'), L(I+'schleswig2.jpg', 'apunta sus canones', cap='El Schleswig-Holstein dispara contra Westerplatte'), L(C+'puerto_danzig.mp4', 'y abre fuego', cap='Danzig, septiembre de 1939'+WWF)], {'shade': True}),
 1: ([L(I+'schleswig3.jpg')], {'shade': True}),
 2: ([L(C+'vias_aereo.mp4', cap='Polonia vista desde un avión alemán, 1939'+WWF)], {}),
 3: ([L(I+'westerplatte_puerta.jpg', cap='Entrada del depósito polaco de Westerplatte'), L(I+'correos2.jpg', 'su oficina de correos')], {}),
 4: ([L(I+'danzig_ss.jpg'), L(I+'forster.jpg', 'albert forster', fy=0.3, who=who('Albert Forster', 'Jefe del partido nazi en Danzig'))], {'shade': True, 'side': 'right'}),
 5: ([L(C+'hitler_discurso.mp4', cap='Hitler en un discurso'+WWF), L(I+'tanques2.jpg', 'polonia')], {}),
 6: ([L(I+'chamberlain.jpg', 'neville chamberlain', fy=0.25, who=who('Neville Chamberlain', 'Primer ministro británico'))], {'side': 'right'}),
 7: ([L(P+'hitler.jpg', fy=0.25), L(I+'hitler_polonia.jpg', 'fall weiss', cap='Hitler con sus generales, 1939')], {}),
 8: ([L(I+'pacto_stalin.jpg', 'stalin', fy=0.25, who=who('Iósif Stalin', 'Dictador de la Unión Soviética'))], {'side': 'right'}),
 9: ([L(I+'ribbentrop.jpg', fy=0.2, who=who('Joachim von Ribbentrop', 'Ministro de Exteriores alemán')), L(I+'pacto_firma.jpg', 'viacheslav molotov', cap='Mólotov firma el pacto; detrás, Ribbentrop y Stalin'), L(I+'pacto.jpg', 'el mundo no da credito')], {'shade': True, 'side': 'right'}),
 10: ([L(I+'pacto_stalin.jpg', dark=True)], {}),
 11: ([L(I+'hitler_polonia.jpg', dark=True)], {}),
 12: ([L(I+'mussolini.jpg', 'mussolini', fy=0.3, who=who('Benito Mussolini', 'Dictador de Italia')), L(C+'stuka2.mp4', 'marcha atras', dark=True)], {'side': 'right'}),
 13: ([L(C+'soldados_marcha.mp4', cap='Soldados alemanes, 1939'+WWF), L(I+'frontera2.jpg', 'un pequeno comando', dark=True)], {}),
 14: ([L(I+'henderson.jpg', cap='Diplomáticos en Berlín: el embajador británico Nevile Henderson (centro)'), L(P+'hitler.jpg', 'hitler ya ha decidido', fy=0.25, dark=True)], {}),
 15: ([L(P+'heydrich.jpg', 'un grupo de hombres', fy=0.25, who=who('Reinhard Heydrich', 'Jefe del SD: ordenó el montaje'))], {'side': 'right'}),
 16: ([L(P+'heydrich.jpg', dark=True)], {}),
 17: ([L(C+'barricadas.mp4', dark=True)], {}),
 18: ([L(I+'frontera1.jpg', dark=True)], {}),
 19: ([L(C+'stuka_vuelo.mp4', cap='Bombarderos en picado Stuka'+WWF), L(I+'stuka.jpg', 'puentes sobre el vistula')], {}),
 20: ([L(C+'bombarderos.mp4', cap='Bombarderos alemanes sobre Polonia'+WWF), L(C+'ciudad_bombardeada.mp4', 'tres cuartas partes', cap='Ciudad polaca tras el bombardeo'+WWF)], {'shade': True}),
 21: ([L(C+'tanques_avance.mp4', cap='Carros alemanes entran en Polonia'+WWF)], {}),
 22: ([L(I+'frontera2.jpg'), L(I+'frontera1.jpg', 'preparadas por la propaganda')], {}),
 23: ([L(I+'tanques.jpg'), L(C+'ataque_aereo.mp4', 'aviones', cap='Ataque aéreo alemán'+WWF)], {}),
 24: ([L(I+'renault.jpg', cap='Carros polacos capturados'), L(C+'carros_caballos.mp4', '880 tanques', cap='El ejército polaco, 1939'+WWF)], {}),
 25: ([L(I+'panzer1.jpg'), L(C+'columna_motor.mp4', 'rompen las lineas')], {}),
 26: ([L(C+'caballeria_carga.mp4', cap='Caballería polaca'+WWF)], {}),
 27: ([L(I+'caballeria.jpg', cap='Tropas montadas alemanas entran en un pueblo polaco'), L(C+'puente_tanque.mp4', 'llegaron blindados')], {}),
 28: ([L(I+'caballeria.jpg', dark=True)], {}),
 29: ([L(I+'correos1.jpg'), L(I+'correos2.jpg', 'resisten')], {}),
 30: ([L(I+'correos3.jpg')], {}),
 31: ([L(I+'schleswig2.jpg', dark=True), L(I+'westerplatte_sold.jpg', 'infanteria', cap='Soldados alemanes en las ruinas de Westerplatte')], {}),
 32: ([L(I+'westerplatte_ruinas.jpg'), L(C+'bandera_blanca.mp4', 'se rindieron', cap='Rendición polaca, 1939'+WWF)], {}),
 33: ([L(I+'reichstag.jpg', cap='Ópera Kroll, Berlín, 1 de septiembre de 1939: Hitler ante el Reichstag')], {}),
 34: ([L(C+'hitler_discurso.mp4'), L(I+'reichstag.jpg', 'ni siquiera la hora', dark=True)], {}),
 36: ([L(I+'chamberlain.jpg', dark=True)], {}),
 37: ([L(I+'henderson.jpg', dark=True)], {}),
 38: ([L(I+'chamberlain.jpg', fy=0.25), L(C+'varsovia_humo.mp4', 'francia hace lo mismo', cap='Varsovia, septiembre de 1939'+WWF)], {}),
 40: ([L(C+'artilleria.mp4', cap='Artillería, 1939'+WWF), L(I+'varsovia_humo.jpg', 'region del sarre')], {}),
 41: ([L(I+'vars_civiles.jpg', 'se muere de verdad', cap='Varsovia, septiembre de 1939')], {}),
 42: ([L(C+'civiles_huyen.mp4', cap='Civiles polacos huyen de un bombardeo'+WWF), L(I+'refugiados.jpg', 'tambien a los civiles')], {}),
 43: ([L(P+'heydrich.jpg', 'einsatzgruppen', fy=0.25, dark=True), L(I+'vars_civiles2.jpg', 'maestros', cap='Civiles polacos en Varsovia, 1939')], {}),
 44: ([L(I+'vars_tumbas.jpg', cap='Varsovia: tumbas provisionales de víctimas de los bombardeos')], {}),
 45: ([L(I+'lublin_sov.jpg', cap='Soldados alemanes y soviéticos se encuentran en Polonia'), L(I+'pacto_stalin.jpg', 'cobrar su parte', fy=0.25)], {}),
 46: ([L(I+'refugiados.jpg', dark=True)], {}),
 47: ([L(I+'brest.jpg', cap='Brest-Litovsk, 22 de septiembre de 1939: desfile germano-soviético')], {}),
 48: ([L(C+'varsovia_aerea.mp4', cap='Varsovia bajo el asedio'+WWF), L(I+'varsovia_aerea.jpg', 'los incendios', cap='Incendios en Varsovia, vistos desde el aire')], {'shade': True}),
 49: ([L(I+'kutrzeba.jpg', 'tadeusz kutrzeba', fy=0.3, who=who('Tadeusz Kutrzeba', 'General polaco')), L(I+'blaskowitz.jpg', 'johannes blaskowitz', who=who('Johannes Blaskowitz', 'General alemán (izquierda)')), L(C+'prisioneros_columna.mp4', 'cien mil soldados', cap='Prisioneros polacos'+WWF)], {}),
 50: ([L(I+'varsovia_ruinas.jpg'), L(I+'vars_ochota.jpg', 'barrios enteros', cap='Varsovia: la población abandona los barrios destruidos')], {}),
 51: ([L(I+'desfile.jpg'), L(C+'oficiales_polacos.mp4', 'kock', cap='Soldados polacos prisioneros'+WWF)], {}),
 52: ([L(I+'prisioneros.jpg'), L(I+'prisioneros_vars.jpg', 'cientos de miles')], {}),
 53: ([L(I+'pacto2.jpg', cap='Moscú, 28 de septiembre de 1939: segundo tratado germano-soviético')], {}),
 54: ([L(I+'mujeres_pan.jpg', cap='Mujeres y niños polacos, 1939')], {}),
 55: ([L(C+'humo.mp4'), L(I+'enigma.jpg', 'enigma', cap='Una máquina Enigma en uso por el ejército alemán')], {}),
 56: ([L(I+'enigma.jpg', dark=True)], {}),
 57: ([L(I+'westerplatte_puerta.jpg', dark=True)], {}),
 58: ([L(I+'schleswig3.jpg'), L(P+'heydrich.jpg', 'una emisora', fy=0.25, dark=True), L(I+'pacto.jpg', 'un pacto secreto', dark=True)], {}),
 59: ([L(I+'varsovia_ruinas2.jpg')], {}),
 60: ([L(I+'schleswig1.jpg', dark=True)], {}),
}

def norm(s): return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
for i, (layers, opts) in M.items():
    sc = S[i]
    for x in layers:
        if x.get('cue') and norm(x['cue']) not in norm(sc['say']): print(f'  ¡cue no encontrado! escena {i}: {x["cue"]}')
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
