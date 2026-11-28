# Imágenes v2 del capítulo 8 (normas de imagen de Raúl: más imágenes, caras con rótulo, clips, sin repetir para rellenar).
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
 0: ([L(C+'barbarroja_aviones.mp4', cap='22 de junio de 1941'+WWF), L(I+'vormarsch_panzer.jpg', 'a lo largo', cap='Carros alemanes al comienzo de la invasión'), L(C+'barbarroja_tanques.mp4', 'mas de 3', cap='La Wehrmacht entra en la Unión Soviética'+WWF)], {'shade': True}),
 1: ([L(P+'hitler.jpg', fy=0.25, dark=True), L(I+'schnee_moskau.jpg', 'seis meses despues', cap='Ante Moscú, invierno de 1941')], {'shade': True}),
 2: ([L(P+'hitler.jpg', fy=0.25, who=who('Adolf Hitler', 'Autor de «Mi lucha»'))], {'side': 'right'}),
 3: ([L(I+'hitler_polonia.jpg', cap='Hitler con sus generales'), L(I+'prisionero_comisario.jpg', 'guerra de exterminio', cap='Prisionero soviético, 1941: retrato tomado por un fotógrafo de propaganda alemán')], {}),
 4: ([L(I+'pacto.jpg', cap='Moscú, agosto de 1939: Mólotov, Stalin y Ribbentrop'), L(C+'campesinos.mp4', 'envio a alemania', cap='Cosecha en la Unión Soviética'+WWF)], {}),
 5: ([L(I+'lagebesprechung.jpg'), L(I+'halder.jpg', 'ordeno a sus generales', fy=0.25, who=who('Franz Halder', 'Jefe del Estado Mayor del Ejército'))], {'side': 'right'}),
 6: ([L(I+'lagebesprechung.jpg', dark=True)], {}),
 7: ([L(I+'hitler_paris.jpg', cap='Hitler en París, junio de 1940'), L(C+'tropas_sovieticas.mp4', 'el ejercito rojo', cap='El Ejército Rojo'+WWF)], {'side': 'right'}),
 8: ([L(P+'hitler.jpg', fy=0.25, dark=True)], {}),
 9: ([L(I+'dorf_brennt.jpg', cap='Un pueblo arde en Ucrania, 1941'), L(C+'campesinos.mp4', 'territorios ocupados', clipStart=5, dark=True)], {}),
 10: ([L(I+'prisionero_comisario.jpg', 'comisarios politicos', dark=True)], {}),
 11: ([L(I+'pacto_stalin.jpg', fy=0.25, who=who('Iósif Stalin', 'Dictador de la Unión Soviética')), L(I+'bug_stug.jpg', 'se acumulaban tropas', cap='Cañones de asalto alemanes junto al río Bug, frontera soviética')], {}),
 12: ([L(I+'pacto_stalin.jpg', fy=0.25, dark=True), L(C+'artilleria.mp4', 'un soldado aleman', dark=True)], {}),
 13: ([L(I+'panzer3.jpg', cap='Carros Panzer III'), L(I+'tross.jpg', 'mas de')], {}),
 14: ([L(C+'columna_motor.mp4', cap='Columna motorizada alemana'+WWF)], {}),
 15: ([L(C+'bombarderos.mp4', cap='Bombarderos alemanes'+WWF), L(C+'stuka2.mp4', 'sin camuflar', dark=True)], {}),
 16: ([L(I+'molotow.jpg', 'molotov', who=who('Viacheslav Mólotov', 'Ministro de Exteriores soviético')), L(C+'civiles_escuchan.mp4', 'anuncio la invasion', cap='Moscovitas escuchan el anuncio de la invasión'+WWF)], {}),
 17: ([L(I+'pacto_stalin.jpg', fy=0.25, dark=True), L(C+'voluntarios.mp4', 'camaradas', cap='Voluntarios soviéticos, 1941'+WWF), L(C+'tierra_quemada.mp4', 'tierra quemada', cap='Tierra quemada'+WWF)], {}),
 18: ([L(C+'columna_humo.mp4', cap='El avance alemán, verano de 1941'+WWF), L(C+'lucha_casas.mp4', 'avanzaban a toda velocidad', cap='Combates en el verano de 1941'+WWF)], {}),
 19: ([L(I+'smolensk_tross.jpg', cap='Carros tirados por caballos cerca de Smolensk, julio de 1941'), L(I+'nowgorod_rio.jpg', 'caballos', cap='Soldados alemanes cruzan un río con sus caballos, 1941')], {}),
 20: ([L(I+'minsk_ruinas.jpg', cap='Minsk en ruinas, 1941')], {}),
 21: ([L(I+'prisioneros_col.jpg'), L(I+'prisioneros_marcha.jpg', 'columnas interminables')], {}),
 22: ([L(I+'prisioneros_dnjepr.jpg'), L(I+'prisioneros_lager.jpg', '5,7 millones', cap='Prisioneros soviéticos en un campo alemán, Porjov')], {'side': 'right'}),
 23: ([L(C+'tropas_sovieticas.mp4', clipStart=3, cap='Tropas soviéticas'+WWF)], {}),
 24: ([L(I+'guderian.jpg', cap='El general Heinz Guderian en el frente del este'), L(I+'halder.jpg', 'franz halder', fy=0.25, who=who('Franz Halder', 'Jefe del Estado Mayor: su diario, agosto de 1941'))], {'side': 'right'}),
 25: ([L(I+'wjasma_panzer.jpg'), L(C+'voluntarios.mp4', 'aparecia otro', clipStart=4, dark=True)], {}),
 26: ([L(C+'presa_dnieper.mp4', cap='La presa del Dniéper, 1941'+WWF), L(C+'tierra_quemada.mp4', 'en pleno invierno', clipStart=5, dark=True)], {}),
 27: ([L(I+'lagebesprechung.jpg', dark=True), L(P+'hitler.jpg', 'hacia kiev', fy=0.25, dark=True)], {}),
 28: ([L(I+'kiew.jpg', cap='Kiev, septiembre de 1941'), L(I+'prisioneros_dnjepr.jpg', '665.000', dark=True)], {}),
 29: ([L(I+'kiew.jpg', dark=True)], {}),
 30: ([L(I+'dorf_reiter.jpg', dark=True), L(P+'himmler.jpg', 'einsatzgruppen', fy=0.25, who=who('Heinrich Himmler', 'Jefe de las SS'))], {}),
 31: ([L(I+'leningrad_winter.jpg'), L(C+'leningrado_calle.mp4', 'rendirla por hambre', cap='Leningrado sitiada'+WWF)], {}),
 32: ([L(C+'leningrado_agua.mp4', cap='Vecinos de Leningrado sacan agua del hielo'+WWF), L(C+'racion_pan.mp4', '125 gramos', cap='La ración de pan de Leningrado, diciembre de 1941'+WWF), L(I+'leningrad_winter.jpg', '800.000', dark=True)], {}),
 33: ([L(I+'division_azul.jpg', cap='Voluntarios de la División Azul en el frente ruso')], {}),
 34: ([L(I+'wjasma_fuego.jpg', cap='Viazma en llamas, octubre de 1941'), L(I+'wjasma_gefang.jpg', 'briansk', cap='Soldados soviéticos capturados cerca de Viazma')], {}),
 35: ([L(C+'civiles_escuchan.mp4', clipStart=7, dark=True), L(I+'pacto_stalin.jpg', 'stalin decidio quedarse', fy=0.25, dark=True)], {}),
 36: ([L(I+'schlamm2.jpg', cap='El barro de la «rasputitsa», otoño de 1941'), L(I+'schlamm3.jpg', 'se hundian')], {}),
 37: ([L(I+'schlamm1.jpg')], {'side': 'right'}),
 38: ([L(C+'invierno_moscu.mp4', cap='El Ejército Rojo en el invierno de 1941'+WWF)], {}),
 39: ([L(I+'schnee_moskau.jpg'), L(C+'esquiadores.mp4', '30 kilometros', dark=True)], {}),
 40: ([L(I+'schnee_schlitten.jpg', cap='Soldados alemanes con un coche averiado en la nieve'), L(I+'schnee_marsch.jpg', 'los motores no arrancaban')], {}),
 41: ([L(P+'goebbels.jpg', 'goebbels', fy=0.3, who=who('Joseph Goebbels', 'Ministro de Propaganda'))], {'side': 'right'}),
 42: ([L(C+'tropas_blanco.mp4', cap='Soldados soviéticos con ropa de invierno'+WWF)], {}),
 43: ([L(C+'contraofensiva.mp4', cap='La contraofensiva soviética ante Moscú, diciembre de 1941'+WWF), L(I+'wjasma_gefang.jpg', 'tuvo que', dark=True), L(C+'civiles_liberados.mp4', 'retroceder', cap='Pueblos liberados cerca de Moscú'+WWF)], {}),
 44: ([L(C+'pearl_harbor.mp4', cap='Pearl Harbor, 7 de diciembre de 1941'+WWF), L(I+'lagebesprechung.jpg', 'el 11 de diciembre', dark=True)], {}),
 45: ([L(P+'hitler.jpg', fy=0.25, dark=True)], {}),
 46: ([L(C+'columna_nieve.mp4', cap='Invierno de 1941-1942'+WWF), L(I+'schnee_schlitten.jpg', 'un millon de bajas', dark=True)], {}),
 47: ([L(I+'prisioneros_marcha.jpg', dark=True), L(C+'presa_dnieper.mp4', 'un territorio inmenso', clipStart=7, dark=True)], {}),
 48: ([L(I+'stalingrado_vista.jpg', cap='Stalingrado, 1942')], {}),
 49: ([L(I+'pacto.jpg', dark=True)], {}),
 50: ([L(I+'dorf_brennt.jpg', dark=True)], {}),
 51: ([L(I+'wjasma_fuego.jpg', dark=True)], {}),
 52: ([L(I+'schnee_moskau.jpg', dark=True)], {}),
 53: ([L(I+'stalingrado_vista.jpg', dark=True)], {}),
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
