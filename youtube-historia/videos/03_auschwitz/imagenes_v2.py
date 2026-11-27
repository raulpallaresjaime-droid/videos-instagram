# Imágenes v2 del capítulo 3 (revisión de Raúl: más imágenes, caras con rótulo, clips, imágenes con peso).
# Reutiliza la voz: no cambia ningún `say`. Uso:  python3 build_spec.py && python3 imagenes_v2.py
# Cada escena: lista de capas (ver youtube-historia/README.md, «Escenas con varias imágenes»).
# Si un archivo no existe, esa capa se omite (y si la escena se queda sin ninguna, conserva su imagen original).
import json, os, re
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
M = {  # escena: (capas, opciones de escena)
 0: ([L(C+'anciano.mp4'), L(C+'via_tren.mp4', 'ningun otro sitio'), L(C+'arbeit_puerta.mp4', 'se llamaba auschwitz')], {'shade': True}),
 1: ([L(I+'puerta_birkenau.jpg')], {}),
 2: ([L(C+'invasion_polonia.mp4', cap='Invasión alemana de Polonia, septiembre de 1939'), L(I+'polonia.jpg', 'se anexiona', cap='Polonia, septiembre de 1939: judíos detenidos por la policía alemana')], {}),
 3: ([L(C+'prisioneros_polacos.mp4'), L(P+'himmler.jpg', 'heinrich himmler', fy=0.3, who=who('Heinrich Himmler', 'Jefe de las SS y de la policía alemana'))], {'side': 'right'}),
 4: ([L(I+'deportacion.jpg'), L(I+'aereo_usaf44.jpg', 'casi cualquier rincon', cap='Auschwitz-Birkenau desde el aire, 1944: las vías del tren')], {'shade': True}),
 5: ([L(I+'dachau1.jpg', cap='Dachau, el campo modelo de las SS'),
      L(P+'hoss.jpg', 'rudolf hoss', fy=0.3, who=who('Rudolf Höss', 'Primer comandante de Auschwitz'))], {'side': 'right'}),
 6: ([L(I+'sachs_polacos.jpg', cap='Presos polacos llegando a un campo de concentración'),
      L(C+'alambrada_pasillo.mp4', 'reciben los numeros')], {}),
 7: ([L(I+'puerta_ai.jpg', cap='Auschwitz I: la puerta del campo principal'), L(I+'torre.jpg', 'de hambre')], {}),
 8: ([L(C+'arbeit_puerta.mp4'), L(I+'arbeit_1955.jpg', 'una de las mentiras', cap='La puerta de Auschwitz I, 1955')], {'shade': True}),
 9: ([L(I+'a1_bloques_1955.jpg', cap='Los bloques de ladrillo de Auschwitz I'), L(C+'literas2.mp4', 'duermen en el suelo')], {}),
 10: ([L(I+'alb_recuento.jpg', cap='Recuento de presas en Birkenau · Álbum de Auschwitz, 1944'), L(I+'sachsenhausen.jpg', 'si falta uno')], {}),
 11: ([L(I+'bloque11.jpg', cap='El bloque 11 de Auschwitz I'), L(I+'celda_hambre.jpg', 'algunas son tan pequenas', cap='Celdas del sótano del bloque 11'), L(I+'muro_muerte.jpg', 'muro de la muerte', cap='El muro de la muerte, junto al bloque 11')], {'shade': True}),
 12: ([L(P+'pilecki.jpg', fy=0.3, who=who('Witold Pilecki', 'Oficial de la resistencia polaca')),
       L(P+'pilecki_auschwitz.jpg', 'quiere entrar', cap='Pilecki, fichado en Auschwitz con el número 4859')], {'side': 'right'}),
 13: ([L(C+'cartel_6000v.mp4'), L(I+'pilecki_juicio.jpg', 'el regimen comunista', cap='Pilecki ante el tribunal comunista, 1948')], {'side': None}),
 14: ([L(I+'pow_sovieticos4.jpg', cap='Prisioneros de guerra soviéticos, 1941'), L(I+'pow_sovietico.jpg', 'brutalidad especial')], {'shade': True}),
 15: ([L(I+'bloque11.jpg'), L(C+'zyklon.mp4', 'un pesticida', cap='Latas de Zyklon B halladas en Auschwitz, 1945'), L(I+'factura_zyklon.jpg', 'para las ss', cap='Factura de 195 kg de Zyklon B para Auschwitz, 1944')], {'shade': True}),
 16: ([L(I+'birkenau.jpg'), L(C+'barracones_nieve.mp4', 'birkenau', cap='Birkenau, enero de 1945')], {}),
 17: ([L(I+'buna_presos.jpg'), L(I+'buna_presos_calle.jpg', 'trabajan con frio', cap='Presos trabajando en una obra en Auschwitz')], {}),
 18: ([L(I+'aereo_usaf44b.jpg', cap='Birkenau desde el aire: foto de reconocimiento de EE. UU., 1944'), L(C+'birk_panorama.mp4', 'en unas 140')], {}),
 19: ([L(I+'barracon_literas_1955.jpg'), L(C+'literas.mp4', 'varios cientos'), L(I+'letrinas.jpg', 'letrinas colectivas', cap='Letrinas colectivas de Birkenau')], {}),
 20: ([L(I+'wannsee.jpg', cap='Invitación de Heydrich a la conferencia de Wannsee'), L(P+'heydrich.jpg', 'solucion final', fy=0.25, who=who('Reinhard Heydrich', 'Convocó la conferencia de Wannsee')), L(I+'wannsee_protocolo.jpg', 'pieza central', cap='Documentos de la conferencia de Wannsee, 1942')], {'shade': True}),
 21: ([L(I+'birkenau_1948.jpg', dark=True), L(I+'alb_bosque_mujeres.jpg', 'los primeros transportes',
       cap='Mujeres y niños esperando junto a una cámara de gas · Álbum de Auschwitz, 1944')], {'shade': True}),
 22: ([L(C+'planos_crematorio.mp4', cap='Planos de los crematorios de Birkenau hallados en 1945'), L(I+'aereo_lw.jpg', 'birkenau es ya')], {'shade': True}),
 23: ([L(I+'vagon.jpg', cap='Presos en un vagón de deportación'), L(I+'lodz_deport.jpg', 'guetos de polonia'),
       L(I+'alb_bajan_tren.jpg', 'el viaje dura dias', cap='Judíos de Rutenia bajando del tren en Birkenau · Álbum de Auschwitz, 1944')], {'shade': True}),
 24: ([L(C+'maletas.mp4', cap='Maletas de deportados halladas en Auschwitz, 1945'),
       L(I+'alb_madre_hijo.jpg', 'nadie les ha dicho', cap='Una madre y su hijo en el andén · Álbum de Auschwitz, 1944')], {}),
 25: ([L(I+'alb_hombres_anden.jpg'), L(I+'alb_mujeres_ninos.jpg', 'hombres a un lado'),
       L(I+'alb_seleccion1.jpg', 'entonces llega la seleccion', cap='La selección en la rampa · Álbum de Auschwitz, 1944'),
       L(I+'alb_seleccion_medico.jpg', 'un medico de las ss')], {'shade': True}),
 26: ([L(I+'alb_ninos_camino.jpg', cap='Niños camino de las cámaras de gas · Álbum de Auschwitz, 1944'),
       L(I+'alb_madres_camino.jpg', 'segun el museo')], {'shade': True}),
 27: ([L(I+'alb_bosque_hombres.jpg', cap='Hombres esperando junto a la cámara de gas 4 · Álbum de Auschwitz, 1944'), L(C+'puerta_gas.mp4', 'les piden que recuerden'), L(I+'camara_gas_a1.jpg', 'todo es parte del engano', cap='La cámara de gas del crematorio I de Auschwitz')], {'shade': True}),
 28: ([L(I+'rampa_ninos.jpg'), L(I+'alb_anciana.jpg', 'por eso')], {}),
 29: ([L(I+'aereo_zona.jpg', dark=True), L(I+'alb_crematorio_camino.jpg', 'cada cierto tiempo', dark=True)], {}),
 30: ([L(I+'alb_canada_clasificar.jpg', cap='Presos clasificando las pertenencias de los deportados · Álbum de Auschwitz'), L(I+'gafas_1945.jpg', 'las gafas', cap='Gafas de las víctimas halladas en Auschwitz, 1945'), L(I+'alb_canada_ropa.jpg', 'los presos los llamaban')], {'shade': True}),
 31: ([L(I+'alb_presas.jpg'), L(I+'pruebas_12.jpg', 'les quitaban todo', cap='Uniformes de presos de Auschwitz, hoy en el museo'), L(C+'tatuaje.mp4', 'y aqui hay un dato', cap='Supervivientes muestran su número tatuado, 1945')], {'shade': True}),
 32: ([L(I+'retratos_presos.jpg', cap='Retratos de presos de Auschwitz, expuestos en el museo'), L(I+'alb_mujeres_trabajo.jpg', 'es decir', cap='Mujeres seleccionadas para el trabajo · Álbum de Auschwitz, 1944')], {'shade': True}),
 33: ([L(I+'alb_presos_barracones.jpg'), L(C+'sup_rayas.mp4', 'jornadas de once'), L(C+'sup_caras.mp4', 'esqueletos vivientes')], {}),
 34: ([L(I+'buna.jpg'), L(P+'himmler_auschwitz_1942.jpg', 'la llamaban buna', cap='Himmler visita la obra de IG Farben en Auschwitz, julio de 1942')], {}),
 35: ([L(I+'buna_obra.jpg'), L(I+'buna_rohrbrucke.jpg', 'la empresa pagaba')], {'side': None}),
 36: ([L(I+'aereo_usaf44b.jpg', dark=True), L(C+'birk_panorama.mp4', 'entre cuarenta', dark=True)], {}),
 37: ([L(I+'buna_canal.jpg'), L(P+'primo_levi.jpg', 'primo levi', fy=0.3, who=who('Primo Levi', 'Químico italiano, preso en Monowitz'))], {'side': 'right'}),
 38: ([L(I+'alb_seleccion2.jpg', cap='Selección en la rampa · Álbum de Auschwitz, 1944'),
       L(P+'mengele.jpg', 'josef mengele', fy=0.3, who=who('Josef Mengele', 'Médico de las SS en Auschwitz'))], {'side': 'right'}),
 39: ([L(P+'mengele_grupo.jpg', cap='Mengele, con otros oficiales de las SS de Auschwitz, 1944'),
       L(I+'lib_ninos.jpg', 'sobre todo a gemelos', cap='Niños supervivientes de Auschwitz, febrero de 1945')], {'shade': True}),
 40: ([L(I+'sinti_mujer.jpg')], {}),
 42: ([L(I+'sinti_ninos.jpg', dark=True)], {}),
 44: ([L(I+'puerta_birkenau.jpg'), L(P+'hoss_2.jpg', 'rudolf hoss', fy=0.3, who=who('Rudolf Höss', 'Vuelve a Auschwitz en 1944'))], {}),
 45: ([L(I+'alb_llegada_mayo.jpg', cap='Judíos de Hungría llegan a Birkenau, mayo de 1944 · Álbum de Auschwitz'),
       L(C+'via_tren.mp4', 'casi todos van')], {'shade': True}),
 47: ([L(I+'lodz_valla.jpg', cap='Gueto de Lodz'), L(I+'lodz_anciano.jpg', 'personas como este anciano')], {'side': None}),
 48: ([L(I+'westerbork.jpg', cap='Westerbork (Países Bajos), 1944: Settela Steinbach, niña sinti, en un tren hacia Auschwitz'), L(P+'ana_frank_1939.jpg', 'ana frank', who=who('Ana Frank', '15 años · deportada desde Westerbork')), L(P+'ana_frank.jpg', 'sobrevivio a auschwitz', fy=0.3)], {'shade': True}),
 49: ([L(C+'barracones_vista.mp4'), L(I+'informe_vrba.jpg', 'se esconden', cap='Telegrama de las SS sobre la fuga de Vrba y Wetzler, 8 de abril de 1944')], {'side': None, 'shade': True}),
 50: ([L(I+'aereo_usaf44.jpg', cap='Birkenau desde el aire, 1944'), L(I+'informe_vrba.jpg', 'ese informe llego')], {'shade': True}),
 51: ([L(I+'aereo_lw.jpg', dark=True)], {}),
 52: ([L(C+'mujer_manta.mp4'), L(C+'dos_mujeres.mp4', 'cuatro de las mujeres')], {'shade': True}),
 53: ([L(I+'aereo.jpg'), L(I+'birkenau_1948.jpg', 'volar los crematorios')], {}),
 54: ([L(C+'sup_nieve.mp4'), L(C+'sup_salen.mp4', 'quien se queda atras')], {'shade': True}),
 55: ([L(I+'lib_1945.jpg', cap='Supervivientes de Auschwitz tras la liberación, enero de 1945'), L(C+'ninos_salen.mp4', 'entre ellos, ninos'), L(P+'primo_levi.jpg', 'y primo levi', fy=0.3)], {}),
 56: ([L(C+'ropa.mp4'), L(C+'pelo_saco.mp4', 'toneladas de pelo', cap='Fardos de pelo humano hallados en Auschwitz, 1945')], {}),
 57: ([L(C+'zapatos.mp4', dark=True)], {}),
 58: ([L(C+'sup_multitud.mp4', dark=True)], {}),
 59: ([L(C+'cepillos.mp4', dark=True)], {}),
 60: ([L(P+'hoss_1947.jpg', fy=0.3, who=who('Rudolf Höss', 'Excomandante de Auschwitz, ante el tribunal')), L(I+'muro_muerte_1975.jpg', 'el 16 de abril de 1947', dark=True)], {'side': 'right'}),
 61: ([L(I+'memorial70.jpg'), L(I+'alambrada_flor.jpg', 'en 1979'), L(C+'mujeres_salen.mp4', 'caminan por los mismos')], {}),
 62: ([L(I+'solahutte2.jpg', cap='Personal de las SS de Auschwitz de descanso en Solahütte, 1944'), L(I+'alb_ss_rampa.jpg', 'personas normales', cap='Un guardia de las SS en la rampa · Álbum de Auschwitz, 1944')], {'shade': True}),
 63: ([L(C+'ninos_salen2.mp4'), L(I+'lib_ninos2.jpg', 'para recordar a cada una', cap='Niños supervivientes de Auschwitz, 1945')], {'shade': True}),
 64: ([L('../04_noche-cristales-rotos/img/sinagoga_quemada.jpg', dark=True)], {}),
}

def find(src):
    return src if ok(src) or ok(src) else None

for i, (layers, opts) in M.items():
    sc = S[i]
    layers = [x for x in layers if ok(x.get('img') or x.get('clip'))]
    if not layers: continue
    if all(x.get('dark') for x in layers): pass
    for k in ('img', 'bg', 'kb', 'fx', 'fy', 'clip', 'cap'): sc.pop(k, None)
    side = opts.get('side', sc.get('side'))
    sc.pop('side', None)
    if side: sc['side'] = side
    if 'shade' in opts and not all(x.get('dark') for x in layers): sc['shade'] = opts['shade']
    if all(x.get('dark') for x in layers): sc.pop('shade', None)
    sc['imgs'] = layers
    # con retrato a la derecha, el texto va a la izquierda
    if side == 'right' and 'html' in sc: sc['html'] = sc['html'].replace('class="ov center"', 'class="ov left"')
    if not side and 'html' in sc: sc['html'] = sc['html'].replace('class="ov left"', 'class="ov center"').replace('class="ov right"', 'class="ov center"')

json.dump(spec, open(os.path.join(here, 'spec.json'), 'w'), ensure_ascii=False, indent=1)
n = sum(len(s.get('imgs', [])) or (1 if s.get('img') or s.get('bg') else 0) for s in S)
print(f'OK spec.json · {len(S)} escenas · {n} imágenes/clips')
