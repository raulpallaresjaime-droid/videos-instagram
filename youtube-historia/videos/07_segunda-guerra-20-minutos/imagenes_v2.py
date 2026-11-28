# Imágenes v2 del capítulo 7 (normas de imagen de Raúl: más imágenes, caras con rótulo, clips, sin repetir para rellenar).
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
UN = ' · Universal/United News'
M = {
 0: ([L(I+'schleswig1.jpg', cap='1 de septiembre de 1939: el Schleswig-Holstein abre fuego en Danzig'), L(C+'missouri.mp4', 'bahia de tokio', cap='USS Missouri, bahía de Tokio, 2 de septiembre de 1945'), L(C+'dday_desembarco.mp4', 'por el camino', cap='Normandía, 6 de junio de 1944 · United News')], {'shade': True}),
 1: ([L(I+'stalingrado_vista.jpg'), L(C+'pearl_humo.mp4', 'las batallas', cap='Pearl Harbor, 7 de diciembre de 1941'+WWF)], {'shade': True}),
 2: ([L(P+'hitler.jpg', fy=0.25, who=who('Adolf Hitler', 'En el poder desde 1933'))], {'side': 'right'}),
 3: ([L(I+'pacto.jpg', cap='Moscú, agosto de 1939: Mólotov, Stalin y Ribbentrop')], {}),
 4: ([L(I+'panzer1.jpg', cap='Polonia, septiembre de 1939'), L(I+'refugiados.jpg', 'la union sovietica entra', cap='Refugiados polacos, 1939')], {}),
 5: ([L(I+'varsovia_ruinas.jpg', dark=True), L(C+'antiaereo.mp4', 'esperan detras', cap='Soldados británicos de guardia, 1939-1940'+WWF)], {}),
 6: ([L(C+'stukas_noruega.mp4', cap='Ataque alemán en Noruega, abril de 1940'+WWF), L(C+'rotterdam_arde.mp4', 'holanda', cap='Rotterdam arde tras el bombardeo, mayo de 1940'+WWF), L(C+'churchill_1940.mp4', 'winston churchill', who=who('Winston Churchill', 'Primer ministro británico desde el 10 de mayo de 1940'))], {}),
 7: ([L(I+'rotterdam.jpg', cap='Rotterdam destruida, mayo de 1940'), L(C+'rotterdam_ruinas.mp4', 'las ardenas'), L(I+'stuka.jpg', 'rompieron')], {}),
 8: ([L(C+'dunkerque_mar.mp4', cap='Barcos frente a Dunkerque, 1940'+WWF), L(I+'dunkerque.jpg', 'un milagro', cap='Material abandonado en Dunkerque'), L(C+'dunkerque_soldados.mp4', 'rescata', cap='Soldados evacuados de Dunkerque'+WWF)], {}),
 9: ([L(I+'paris_desfile.jpg', cap='Desfile alemán en París, junio de 1940'), L(C+'compiegne.mp4', 'compiegne', cap='Compiègne, 22 de junio de 1940'+WWF), L(C+'franceses_lloran.mp4', 'la humillacion', cap='Franceses ante la derrota'+WWF)], {}),
 10: ([L(I+'hitler_paris.jpg', cap='Hitler en París, 23 de junio de 1940'), L(C+'hitler_compiegne.mp4', 'seis semanas', dark=True)], {'side': 'right'}),
 11: ([L(I+'heinkel_londres.jpg'), L(C+'raf_despegue.mp4', 'dominar el cielo', cap='Cazas de la RAF despegan'+WWF), L(C+'combate_aereo.mp4', 'batalla de inglaterra', cap='Combate aéreo sobre Inglaterra, 1940'+WWF)], {}),
 12: ([L(C+'antiaereo.mp4', 'con la ayuda del radar', clipStart=6), L(C+'formacion_nubes.mp4', 'nunca tantos'), L(C+'churchill_1940.mp4', 'aplazo la invasion', dark=True)], {}),
 13: ([L(C+'londres_bombardeado.mp4', cap='Londres tras el Blitz'+WWF), L(C+'san_pablo_humo.mp4', 'fue el blitz', cap='La catedral de San Pablo entre el humo, Londres'+WWF), L(C+'blitz_casas.mp4', 'mas de 40.000')], {}),
 14: ([L(I+'hendaya.jpg', who=who('Francisco Franco y Adolf Hitler', 'Hendaya, 23 de octubre de 1940'))], {}),
 15: ([L(I+'mussolini.jpg', 'mussolini', fy=0.3, who=who('Benito Mussolini', 'Dictador de Italia')), L(I+'africa.jpg', 'norte de africa')], {}),
 16: ([L(I+'rommel.jpg', 'erwin rommel', fy=0.25, who=who('Erwin Rommel', 'General alemán en el norte de África'))], {'side': 'right'}),
 17: ([L(I+'vormarsch_panzer.jpg', cap='Carros alemanes en el este, 1941'), L(P+'hitler.jpg', 'mi lucha', fy=0.25, dark=True)], {}),
 18: ([L(C+'barbarroja_aviones.mp4', cap='22 de junio de 1941: empieza la invasión de la URSS'+WWF), L(C+'barbarroja_tanques.mp4', 'operacion barbarroja'), L(C+'civiles_escuchan.mp4', 'stalin', cap='Ciudadanos soviéticos escuchan la noticia de la invasión'+WWF)], {}),
 19: ([L(I+'prisioneros_col.jpg', cap='Columnas de prisioneros soviéticos, 1941'), L(C+'columna_humo.mp4', 'la mayoria moririan', dark=True)], {}),
 20: ([L(I+'division_azul.jpg', cap='Voluntarios de la División Azul en el frente ruso')], {}),
 21: ([L(C+'leningrado_calle.mp4', cap='Leningrado sitiada, invierno de 1941-1942'+WWF), L(C+'leningrado_agua.mp4', 'sin comida', cap='Vecinos de Leningrado sacan agua del hielo'+WWF), L(C+'racion_pan.mp4', '800.000', cap='Ración de pan en Leningrado: 125 gramos al día'+WWF)], {}),
 22: ([L(I+'schnee_moskau.jpg', cap='Ante Moscú, invierno de 1941'), L(I+'schnee_marsch.jpg', 'un invierno terrible'), L(C+'invierno_moscu.mp4', 'contraataco', cap='Contraataque soviético ante Moscú'+WWF)], {}),
 23: ([L(I+'dorf_brennt.jpg', cap='Un pueblo arde en Ucrania, 1941'), L(P+'himmler.jpg', 'einsatzgruppen', fy=0.25, dark=True)], {}),
 24: ([L(I+'wannsee.jpg', 'wannsee', cap='Invitación de Heydrich a la conferencia de Wannsee'), L(I+'alb_madres_camino.jpg', 'auschwitz', cap='Birkenau, 1944: madres y niños camino de las cámaras de gas · Álbum de Auschwitz')], {}),
 25: ([L(C+'portaaviones.mp4', cap='La guerra en el Pacífico · «Appointment in Tokyo»', dark=True)], {}),
 26: ([L(C+'pearl_harbor.mp4', 'pearl harbor', cap='Pearl Harbor, 7 de diciembre de 1941'+WWF), L(I+'pearl.jpg', cap='El USS Arizona ardiendo en Pearl Harbor')], {}),
 27: ([L(C+'pearl_explosiones.mp4'), L(I+'roosevelt.jpg', 'roosevelt', fy=0.3, who=who('Franklin D. Roosevelt', 'Presidente de Estados Unidos'))], {}),
 28: ([L(C+'batalla_naval.mp4', cap='Guerra en el Pacífico, 1942 · «Appointment in Tokyo»'), L(C+'portaaviones.mp4', 'singapur', clipStart=7)], {}),
 29: ([L(I+'midway.jpg', cap='Bombarderos estadounidenses sobre un crucero japonés en llamas, Midway, junio de 1942'), L(C+'ataque_barco.mp4', 'cuatro portaaviones', cap='Ataque a un barco en el Pacífico · «Appointment in Tokyo»')], {}),
 30: ([L(I+'stalingrado_ruinas.jpg'), L(I+'paulus.jpg', 'stalingrado', fy=0.25, who=who('Friedrich Paulus', 'Jefe del Sexto Ejército alemán'))], {'side': 'right'}),
 31: ([L(C+'stalingrado_lucha.mp4', cap='Stalingrado, 1942'+WWF), L(I+'stalingrado_fabrica.jpg', 'la guerra de las ratas')], {}),
 32: ([L(I+'stalingrado_lanzallamas.jpg'), L(I+'stalingrado_paulus.jpg', 'hitler prohibe', cap='Paulus (derecha) en Stalingrado'), L(C+'stalingrado_ruinas.mp4', 'en el hielo')], {}),
 33: ([L(I+'stalingrado_prisioneros.jpg', cap='Prisioneros alemanes en Stalingrado'), L(C+'stalingrado_rendicion.mp4', '91.000', cap='Oficiales alemanes capturados en Stalingrado'+WWF), L(C+'stalingrado_soldados.mp4', 'el principio del fin')], {}),
 34: ([L(I+'africa.jpg', dark=True), L(I+'rommel.jpg', 'derrotaban a rommel', fy=0.25, dark=True), L(I+'eisenhower_dday.jpg', 'marruecos', dark=True)], {}),
 35: ([L(I+'stalingrado_vista.jpg', dark=True), L(C+'ataque_barco.mp4', 'el atlantico', dark=True)], {}),
 36: ([L(I+'kursk.jpg', cap='Kursk, julio de 1943'), L(C+'tropas_sovieticas.mp4', 'los sovieticos')], {}),
 37: ([L(I+'mussolini.jpg', 'mussolini', fy=0.3, dark=True)], {}),
 38: ([L(C+'b29_formacion.mp4', clipStart=4, cap='Bombarderos estadounidenses · «To the Shores of Iwo Jima»'), L(I+'reichstag_ruina.jpg', 'hamburgo', dark=True)], {}),
 39: ([L(C+'dday_flota.mp4', cap='Normandía, 6 de junio de 1944 · United News'), L(I+'dday.jpg', 'mas de 150.000', cap='«En las fauces de la muerte»: Omaha, 6 de junio de 1944'), L(C+'dday_barcazas.mp4', 'miles de barcos')], {}),
 40: ([L(C+'dday_obstaculos.mp4', cap='Obstáculos alemanes en la playa · United News'), L(I+'normandia_lancha.jpg', 'al caer la noche'), L(I+'eisenhower_dday.jpg', 'hitler tenia ahora', who=who('Dwight D. Eisenhower', 'Comandante supremo aliado'))], {}),
 41: ([L(C+'tropas_sovieticas.mp4', clipStart=3, cap='Tropas soviéticas'+WWF)], {}),
 42: ([L(I+'paris_desfile.jpg', dark=True), L(C+'paris_arco.mp4', 'la nueve', cap='El Arco del Triunfo, París · «Why We Fight»')], {}),
 43: ([L(I+'stauffenberg.jpg', 'stauffenberg', fy=0.25, who=who('Claus von Stauffenberg', 'A la izquierda, con Hitler, 5 días antes del atentado'))], {'side': 'right'}),
 44: ([L(I+'schnee_marsch.jpg', dark=True)], {}),
 45: ([L(C+'desembarco_pacifico.mp4', cap='Desembarco en el Pacífico · «Appointment in Tokyo»'), L(C+'iwojima_combate.mp4', 'kamikazes', cap='Combates en Iwo Jima, 1945 · «To the Shores of Iwo Jima»')], {}),
 46: ([L(I+'rampa_ninos.jpg', cap='Niños en la rampa de Birkenau, 1944 · Álbum de Auschwitz'), L(I+'lib_ninos.jpg', 'el mundo empieza', cap='Niños supervivientes de Auschwitz, enero de 1945')], {}),
 47: ([L(I+'yalta.jpg', who=who('Churchill, Roosevelt y Stalin', 'Yalta, febrero de 1945'))], {}),
 48: ([L(I+'reichstag_ruina.jpg'), L(I+'roosevelt.jpg', 'roosevelt muere', fy=0.3, dark=True), L(P+'hitler.jpg', 'el 30 de abril', fy=0.25, dark=True)], {}),
 49: ([L(I+'karlshorst.jpg', 'el 7 de mayo', cap='Berlín, 8 de mayo de 1945: Keitel firma la rendición de la Wehrmacht')], {}),
 50: ([L(I+'iwojima.jpg', cap='Iwo Jima, 23 de febrero de 1945'), L(C+'iwojima_bandera.mp4', 'invadir japon', cap='Iwo Jima · «To the Shores of Iwo Jima»')], {}),
 51: ([L(C+'b29.mp4', cap='Aviones estadounidenses en el Pacífico, 1945 · «To the Shores of Iwo Jima»'), L(I+'atomica.jpg', 'hiroshima'), L(C+'hiroshima_panorama.mp4', '140.000', cap='Hiroshima, 1946 · US Air Force')], {'shade': True}),
 52: ([L(C+'hiroshima_reloj.mp4', cap='Un reloj detenido por la explosión, Hiroshima · US Air Force'), L(I+'hiroshima_ruinas.jpg', 'la union sovietica', cap='Hiroshima tras la bomba'), L(I+'hirohito.jpg', 'hirohito', fy=0.3, who=who('Hirohito', 'Emperador de Japón (con MacArthur, septiembre de 1945)'))], {}),
 53: ([L(C+'delegacion_japonesa.mp4', cap='La delegación japonesa a bordo del Missouri · «Appointment in Tokyo»'), L(C+'firma_japon.mp4', 'japon firmo'), L(C+'macarthur_firma.mp4', 'seis anos y un dia', cap='Douglas MacArthur firma por los aliados')], {}),
 54: ([L(I+'varsovia_ruinas.jpg'), L(C+'hiroshima_arbol.mp4', 'mas de 60 millones', dark=True)], {}),
 55: ([L(C+'leningrado_agua.mp4', dark=True), L(I+'refugiados.jpg', 'polonia', dark=True)], {}),
 56: ([L(I+'reichstag_ruina.jpg', dark=True)], {}),
 57: ([L(I+'stalingrado_vista.jpg', dark=True), L(I+'alb_madres_camino.jpg', 'una nina', dark=True)], {}),
 58: ([L(I+'schleswig1.jpg', dark=True)], {}),
 59: ([L(I+'vormarsch_panzer.jpg', dark=True)], {}),
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
