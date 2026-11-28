# Imágenes v2 del capítulo 4 (normas de imagen de Raúl: más imágenes, caras con rótulo, clips, sin repetir para rellenar).
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
SYN = 'Sinagoga en llamas, 10 de noviembre de 1938'

M = {
 0: ([L(I+'k_wiesbaden_arde.jpg', cap='Wiesbaden: la sinagoga arde, 10 de noviembre de 1938'),
      L(I+'k_ludwigsburg_arde.jpg', 'unos 7.500', cap='Ludwigsburg, 10 de noviembre de 1938'),
      L(I+'k_stadthagen_detenidos.jpg', 'unos 30.000', cap='Judíos detenidos en Stadthagen, noviembre de 1938')], {'shade': True}),
 1: ([L(I+'tienda_magdeburgo.jpg'), L(I+'k_borneplatz_arde.jpg', 'pogromo', cap='Fráncfort: arde la sinagoga de Börneplatz')], {'shade': True}),
 2: ([L(I+'hitler.jpg', fy=0.25, who=who('Adolf Hitler', 'Canciller desde el 30 de enero de 1933'))], {}),
 3: ([L(I+'viena_templo.jpg'), L(I+'k_tora.jpg', cap='Fragmento de una Torá quemada en 1938')], {}),
 4: ([L(I+'boicot_sa.jpg', cap='Boicot a los comercios judíos, 1 de abril de 1933'), L(I+'boicot_cartel.jpg'), L(I+'boicot.jpg')], {}),
 5: ([L(I+'boicot_camion.jpg'), L(C+'reichstag.mp4', 'leyes de nuremberg', cap='El Reichstag, reunido en Núremberg')], {}),
 6: ([L(C+'hitler_discurso.mp4', cap='Hitler en un discurso, años treinta'), L(I+'aviso_dachau.jpg', dark=True)], {'shade': True}),
 7: ([L(C+'anschluss_viena.mp4', cap='Tropas alemanas en Austria, marzo de 1938 · «Why We Fight»'), L(I+'viena_templo2.jpg', 'en viena')], {'side': None}),
 8: ([L(I+'viena_fregar.jpg', cap='Viena, 1938: judíos obligados a fregar las aceras'), L(I+'viena_templo.jpg', 'las ss registran')], {'shade': True}),
 9: ([L(I+'kennkarte_j.jpg', dark=True)], {}),
 10: ([L(I+'evian.jpg', cap='Conferencia de Évian, julio de 1938'), L(C+'diplomaticos.mp4', 'todos lamentan', cap='Delegados en una conferencia internacional, años treinta')], {'shade': True}),
 11: ([L(I+'streicher.jpg'), L(I+'k_munich_ohel.jpg', 'sinagoga de munich', cap='Sinagoga destruida en Múnich, 1938')], {}),
 12: ([L(I+'kennkarte_j.jpg', cap='Documento de una judía alemana marcado con la J, 1939')], {}),
 13: ([L(I+'judios_polacos.jpg', cap='Judíos polacos'), L(I+'polonia.jpg')], {}),
 14: ([L(I+'deportacion.jpg', dark=True)], {}),
 15: ([L(I+'vagon.jpg')], {}),
 16: ([L(I+'k_stadthagen2.jpg', dark=True)], {}),
 17: ([L(I+'grynszpan.jpg', fy=0.3, who=who('Herschel Grynszpan', '17 años · vive en París'))], {}),
 18: ([L(I+'vomrath.jpg', 'ernst vom rath', fy=0.3, who=who('Ernst vom Rath', 'Diplomático de la embajada alemana en París'))], {}),
 19: ([L(I+'grynszpan_policia.jpg', cap='Herschel Grynszpan, detenido en París')], {}),
 20: ([L(I+'goebbels.jpg', fy=0.3, who=who('Joseph Goebbels', 'Ministro de Propaganda'))], {}),
 22: ([L(I+'munich.jpg'), L(I+'putsch.jpg', 'golpe de estado', cap='Múnich, 9 de noviembre de 1923')], {}),
 23: ([L(I+'burgerbrau.jpg'), L(C+'hitler_discurso.mp4', 'hacia las nueve')], {}),
 24: ([L(P+'goebbels.jpg', fy=0.3)], {}),
 26: ([L(P+'heydrich.jpg', 'reinhard heydrich', fy=0.25, who=who('Reinhard Heydrich', 'Jefe de la policía de seguridad')), L(I+'antorchas.jpg', dark=True)], {'side': 'right'}),
 27: ([L(I+'sinagoga_danada.jpg'), L(I+'k_frankfurt.jpg', cap=SYN)], {}),
 28: ([L(I+'antorchas.jpg'), L(I+'k_chemnitz.jpg', cap='Chemnitz: ruinas de la sinagoga')], {}),
 29: ([L(I+'sinagoga_interior.jpg'), L(I+'k_freiburg.jpg', cap='Friburgo: la sinagoga destruida, 10 de noviembre de 1938')], {}),
 30: ([L(I+'sinagoga_quemada.jpg'), L(I+'k_dia_despues.jpg', cap='La mañana siguiente')], {}),
 31: ([L(I+'k_fasanenstrasse.jpg', 'fasanenstrasse'), L(I+'k_worms.jpg', 'en viena', cap='Ruinas de la sinagoga de Worms')], {}),
 32: ([L(I+'k_mannheim.jpg', dark=True)], {}),
 33: ([L(I+'k_magdeburgo2.jpg', cap='Magdeburgo, 10 de noviembre de 1938'), L(I+'tienda_magdeburgo.jpg')], {}),
 34: ([L(I+'kristall.jpg'), L(I+'k_uhlfelder.jpg', cap='Múnich: grandes almacenes Uhlfelder destrozados')], {}),
 35: ([L(I+'tienda_rota.jpg')], {}),
 36: ([L(I+'k_loerrach.jpg', dark=True)], {}),
 37: ([L(I+'sinagoga_danada.jpg', dark=True)], {}),
 38: ([L(I+'badenbaden.jpg', cap='Baden-Baden, 10 de noviembre de 1938'), L(I+'k_stadthagen_detenidos.jpg')], {}),
 39: ([L(I+'badenbaden.jpg'), L(I+'k_stadthagen2.jpg', cap='Detenidos en Stadthagen, noviembre de 1938')], {}),
 40: ([L(I+'aviso_dachau.jpg', cap='Aviso en un comercio cerrado: su dueño, «en custodia» en Dachau'), L(I+'dachau1.jpg')], {}),
 41: ([L(I+'sachsenhausen.jpg')], {}),
 42: ([L(I+'eicke.jpg'), L(I+'dachau2.jpg')], {}),
 43: ([L(P+'goring.jpg', fy=0.3, who=who('Hermann Göring', 'Encargado del Plan Cuatrienal'))], {'side': 'right'}),
 44: ([L(I+'k_magdeburgo2.jpg', dark=True)], {}),
 45: ([L(I+'goring.jpg')], {}),
 47: ([L(I+'boicot.jpg', dark=True)], {}),
 48: ([L(I+'roosevelt.jpg', 'roosevelt', fy=0.3, who=who('Franklin D. Roosevelt', 'Presidente de Estados Unidos'))], {'shade': True}),
 49: ([L(I+'evian.jpg', dark=True)], {}),
 50: ([L(I+'kindertransport.jpg', cap='Niños refugiados judíos llegan a Inglaterra')], {'shade': True}),
 51: ([L(I+'kindertransport.jpg', dark=True)], {}),
 53: ([L(I+'puerta_birkenau.jpg', dark=True)], {}),
 54: ([L(I+'grynszpan_policia.jpg')], {}),
 58: ([L(C+'reichstag.mp4'), L(C+'hitler_discurso.mp4', 'una profecia')], {'shade': True}),
 59: ([L(I+'lodz_anciano.jpg')], {}),
 61: ([L(I+'tienda_rota.jpg'), L(I+'k_dia_despues.jpg', 'los que miraron')], {}),
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
