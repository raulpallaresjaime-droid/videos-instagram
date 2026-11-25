# Genera spec.json del episodio 2. Uso: python3 build_spec.py
import json, os
here = os.path.dirname(os.path.abspath(__file__))
has = lambda n: os.path.exists(os.path.join(here, 'img', n + '.jpg'))

S = []
def sc(say, **kw):
    # foto opcional: si no se ha podido descargar, la escena pasa a fondo oscuro con otra foto
    if 'img' in kw and not has(kw['img']):
        fb = kw.pop('fallback', 'birkenau48'); kw.pop('img'); kw.pop('side', None); kw.pop('kb', None); kw.pop('cap', None)
        kw['bg'] = f'img/{fb}.jpg'
    elif 'img' in kw:
        kw['img'] = f"img/{kw['img']}.jpg"; kw.pop('fallback', None)
    if 'bg' in kw and not kw['bg'].startswith('img/'): kw['bg'] = f"img/{kw['bg']}.jpg"
    S.append(dict(say=say, **kw))

TRI = [('#c0392b', 'Rojo', 'Presos políticos'), ('#3f8f3f', 'Verde', 'Delincuentes comunes'), ('#7d4fa0', 'Morado', 'Testigos de Jehová'),
       ('#e48fb0', 'Rosa', 'Homosexuales'), ('#151412', 'Negro', '«Asociales»'), ('#e2b62c', 'Amarillo', 'Judíos')]
CUE = ['rojo', 'verde', 'morado', 'rosa', 'negro', 'amarillos']
def triangles():
    out = []
    for (col, name, who), cue in zip(TRI, CUE):
        star = name == 'Amarillo'
        shape = (f'<div style="position:relative;width:110px;height:96px">'
                 f'<div style="position:absolute;width:0;height:0;border-left:55px solid transparent;border-right:55px solid transparent;border-top:96px solid {col}"></div>'
                 + (f'<div style="position:absolute;top:0;width:0;height:0;border-left:55px solid transparent;border-right:55px solid transparent;border-bottom:96px solid {col};opacity:.85"></div>' if star else '')
                 + '</div>')
        border = 'filter:drop-shadow(0 0 2px #ebe3cf) drop-shadow(0 0 1px #ebe3cf);' if name == 'Negro' else ''
        out.append(f'<div class="in" data-cue="{cue}" style="display:flex;flex-direction:column;align-items:center;width:230px">'
                   f'<div style="{border}padding:4px">{shape}</div><div class="h3" style="font-size:36px;margin-top:18px">{name}</div>'
                   f'<div class="dim" style="font-size:28px;text-align:center">{who}</div></div>')
    return '<div class="ov center"><div class="h3 dim in" data-t="0" style="margin-bottom:60px">El código de los triángulos</div><div class="row" style="gap:30px;align-items:flex-start">' + ''.join(out) + '</div></div>'

def timeline(items, title=None, extra=''):
    ev = ''.join(f'<div class="e in" data-cue="{c}"><div class="d">{d}</div><div class="t">{t}</div></div>' for d, t, c in items)
    head = f'<div class="h3 dim in" data-t="0" style="margin-bottom:80px">{title}</div>' if title else ''
    return f'<div class="ov center">{head}<div class="tl">{ev}</div>{extra}</div>'

# ---------- GANCHO ----------
sc("22 de marzo de 1933. A las afueras de Múnich, en una antigua fábrica de pólvora y municiones, llegan unos 200 presos. Casi todos son comunistas y socialistas. "
   "Es el primer día de Dachau. Doce años después, solo en Auschwitz habrían sido asesinadas más de 1,1 millones de personas. ¿Cómo se pasa de una cosa a la otra?",
   bg='dachau1',
   html='<div class="ov center"><div class="date in" data-t="0">22 de marzo de 1933 · Dachau</div>'
        '<div class="big in" data-t="0.3"><span data-count="200">0</span> <span class="h2">presos</span></div>'
        '<div class="h3 dim in" data-cue="doce anos despues" style="margin-top:40px">12 años después, solo en Auschwitz:</div>'
        '<div class="big red in" data-cue="1,1 millones"><span data-count="1100000">0</span></div>'
        '<div class="h3 in" data-cue="asesinadas">personas asesinadas</div></div>')
sc("Esta es la historia de cómo nació el sistema de campos nazi. No apareció de golpe: se construyó paso a paso, durante doce años, y casi siempre a la vista de todos.",
   img='birkenau48', kb='out', shade=True,
   html='<div class="ov center"><div class="tag in" data-t="0.5">Capítulo 2</div>'
        '<div class="h1 in" data-t="0.6">De Dachau<br>a Auschwitz</div>'
        '<div class="date in" data-cue="paso a paso" style="margin-top:30px">1933 — 1945</div></div>')

# ---------- 1933 ----------
sc("En el capítulo anterior vimos cómo, tras el incendio del Reichstag, un decreto de emergencia suspendió los derechos básicos en Alemania. "
   "Ese decreto permitía algo terrible: encerrar a cualquiera por tiempo indefinido, sin juicio y sin abogado. Lo llamaron custodia protectora.",
   img='detenidos', kb='in', cap='Berlín, marzo de 1933: detenidos vigilados por las SA',
   html='<div class="ov right low"><div class="box in" data-cue="custodia protectora"><div class="lab">«Schutzhaft»</div><div class="val" style="font-size:64px">Custodia protectora</div></div></div>')
sc("En las semanas siguientes, la policía y miles de hombres de las SA, convertidos en policías auxiliares, detienen a decenas de miles de opositores. Las cárceles se llenan. "
   "Y empiezan a aparecer centros improvisados en sótanos, almacenes y fábricas abandonadas. Son los llamados campos salvajes, donde los presos son golpeados y humillados sin ningún control.",
   img='hilfspolizei', kb='left', cap='Berlín, 1933: redada de la policía y de las SA',
   html='<div class="ov left"><div class="h2 in tw" data-cue="campos salvajes">Los campos<br>salvajes</div></div>', shade=True)
sc("Uno de esos primeros campos estaba en Oranienburg, al norte de Berlín, en una antigua fábrica de cerveza. Por toda Alemania surgieron muchos como este.",
   img='oranienburg', kb='right', cap='Campo de Oranienburg, agosto de 1933')
sc("Pero en Baviera, un hombre tenía otro plan. Heinrich Himmler, jefe de las SS y nuevo presidente de la policía de Múnich, quería algo más organizado. "
   "El 20 de marzo de 1933 anuncia en la prensa la apertura de un campo de concentración en Dachau, el primero para presos políticos.",
   img='himmler', side='right', kb='in', fy=0.3,
   html='<div class="ov left"><div class="date in" data-t="0.2">20 de marzo de 1933</div><div class="h2 in" data-cue="heinrich himmler">Heinrich<br>Himmler</div>'
        '<div class="h3 dim in" data-cue="jefe de las ss">Jefe de las SS</div></div>')
sc("Dos días después llegan los primeros presos. Al principio los vigila la policía bávara, pero en abril el control pasa a las SS. Y en junio de 1933 llega un nuevo comandante: Theodor Eicke.",
   img='dachau1', kb='in', cap='Dachau, 1933: presos de camino al rancho',
   html='<div class="ov right"><div class="date in" data-t="0.2">22 de marzo de 1933</div><div class="h1 in tw" data-t="0.4">Dachau</div></div>')
sc("Eicke escribe un reglamento que lo cambia todo: palizas con bastones, celdas de aislamiento, y la pena de muerte para quien intente rebelarse o agitar a otros presos. "
   "Y entrena a sus guardias con una idea: el preso es un enemigo, y la compasión, una debilidad.",
   img='eicke', kb='left', shade=True, cap='Dachau, diciembre de 1933: el comandante habla a presos que van a ser liberados',
   html='<div class="ov center"><div class="date in" data-t="0.2">Theodor Eicke · comandante de Dachau</div>'
        '<div class="q in" data-cue="el preso es un enemigo" style="margin-top:30px">«El preso es un enemigo.<br>La compasión, una debilidad.»</div></div>')
sc("En esos primeros años, muchos presos salían en libertad tras unas semanas o unos meses. El objetivo era aterrorizar a la oposición: quien salía de Dachau, no volvía a abrir la boca.",
   img='dachau2', kb='right', cap='Dachau, 1933: presos pelando patatas')
sc("El modelo de Dachau funciona. En 1934, Himmler nombra a Eicke inspector de todos los campos de concentración, y las SS toman el control del sistema entero. "
   "Muchos futuros comandantes se formaron allí. Entre ellos, el hombre que años después dirigiría Auschwitz: Rudolf Höss.",
   bg='eicke',
   html='<div class="ov center"><div class="tag in" data-t="0.4">1934</div><div class="h1 in" data-t="0.6">La escuela<br>de Dachau</div>'
        '<div class="h3 amber in" data-cue="rudolf hoss" style="margin-top:40px">Rudolf Höss: de guardia en Dachau a comandante de Auschwitz</div></div>')
sc("Dentro, cada preso llevaba un número y un triángulo de color cosido en el uniforme. Rojo, para los presos políticos. Verde, para los delincuentes comunes. "
   "Morado, para los testigos de Jehová. Rosa, para los homosexuales. Negro, para los llamados asociales. Y para los judíos, dos triángulos amarillos que formaban una estrella de David.",
   bg='sachsenhausen', html=triangles())
sc("Estos triángulos todavía se ven en las fotos. Aquí, presos de Sachsenhausen, formados en el patio para el recuento diario.",
   img='sachsenhausen', kb='in', fy=0.4, cap='Sachsenhausen: presos con uniforme de rayas y triángulo')

# ---------- 1936-1939 ----------
sc("A partir de 1936, el sistema se profesionaliza. Se cierran muchos campos pequeños y se construyen campos grandes, pensados para durar: Sachsenhausen, junto a Berlín, en 1936. "
   "Buchenwald, cerca de Weimar, en 1937. Flossenbürg y Mauthausen, en 1938. Y en 1939, Ravensbrück, el primer gran campo para mujeres.",
   bg='sachs_polacos',
   html=timeline([('1936', 'Sachsenhausen', 'sachsenhausen, junto'), ('1937', 'Buchenwald', 'buchenwald'), ('1938', 'Flossenbürg', 'flossenburg'),
                  ('1938', 'Mauthausen', 'mauthausen'), ('1939', 'Ravensbrück', 'ravensbruck')], 'Los grandes campos'))
sc("Muchos se construyen junto a canteras y fábricas: el trabajo forzado se convierte en un negocio para las SS. En Mauthausen, en Austria, "
   "los presos subían bloques de granito por una escalera de 186 escalones. La llamaban la escalera de la muerte.",
   img='mauthausen', side='right', kb='up', fy=0.4,
   html='<div class="ov left"><div class="date in" data-t="0.2">Mauthausen · Austria</div><div class="big in" data-cue="186">186</div>'
        '<div class="h3 in" data-cue="186" data-d="0.3">escalones</div><div class="h2 red in tw" data-cue="escalera de la muerte" style="margin-top:30px">La escalera<br>de la muerte</div></div>')
sc("Y en Mauthausen hay una historia que nos toca muy de cerca. A partir de agosto de 1940 llegaron miles de republicanos españoles, que habían huido a Francia tras la Guerra Civil. "
   "Más de dos tercios murieron allí. Su historia merece un capítulo propio, y lo tendrá.",
   bg='mauthausen',
   html='<div class="ov center"><div class="date in" data-t="0.2">Mauthausen · agosto de 1940</div><div class="h2 in tw" data-cue="republicanos espanoles">Los españoles<br>de Mauthausen</div>'
        '<div class="h3 red in" data-cue="mas de dos tercios" style="margin-top:40px">Más de 2 de cada 3 murieron</div></div>')
sc("En Ravensbrück, las presas eran obligadas a hacer trabajos durísimos, como empujar vagonetas cargadas de tierra, con frío, hambre y golpes.",
   img='ravensbruck', kb='left', cap='Ravensbrück, 1939: presas empujando una vagoneta')

# ---------- 1938 ----------
sc("En noviembre de 1938 llega un punto de inflexión: la Noche de los cristales rotos. Los nazis queman más de 250 sinagogas y destrozan unos 7.000 negocios, casas y escuelas judías.",
   img='kristall', kb='in', fallback='deportacion', cap='Magdeburgo, noviembre de 1938: un comercio judío destrozado',
   html='<div class="ov left"><div class="date in" data-t="0.2">9-10 de noviembre de 1938</div><div class="h2 in tw" data-t="0.6">La Noche de los<br>cristales rotos</div></div>')
sc("La policía detiene a unos 30.000 hombres judíos y los envía a Dachau, Buchenwald y Sachsenhausen. Por primera vez, el régimen encierra a judíos de forma masiva solo por ser judíos. "
   "La mayoría salió semanas después, con una condición: abandonar Alemania y dejar atrás casi todo lo que tenían.",
   bg='dachau1',
   html='<div class="ov center"><div class="h3 dim in" data-t="0">Hombres judíos detenidos</div><div class="big red in" data-t="0.4"><span data-count="30000">0</span></div>'
        '<div class="h3 in" data-cue="por primera vez" style="margin-top:30px">Por primera vez, encerrados solo por ser judíos</div></div>')

# ---------- GUERRA ----------
sc("El 1 de septiembre de 1939, Alemania invade Polonia y empieza la guerra. Con ella, el sistema de campos se dispara: en los territorios ocupados hay millones de nuevas personas a las que perseguir.",
   img='polonia', kb='right', cap='Polonia, septiembre de 1939: judíos detenidos por la policía alemana',
   html='<div class="ov left"><div class="date in" data-t="0.2">1 de septiembre de 1939</div><div class="h2 in" data-cue="empieza la guerra">Empieza<br>la guerra</div></div>', shade=True)
sc("En la primavera de 1940, las SS eligen un antiguo cuartel del ejército polaco, junto a la ciudad polaca de Oswiecim. Los alemanes la llaman Auschwitz. "
   "El 14 de junio de 1940 llega el primer transporte: 728 presos políticos polacos. Al principio, Auschwitz es eso: un campo para polacos.",
   img='auschwitz_puerta', kb='in', fallback='sachs_polacos',
   html='<div class="ov left"><div class="date in" data-t="0.2">14 de junio de 1940</div><div class="h1 in tw" data-cue="los alemanes la llaman auschwitz">Auschwitz</div>'
        '<div class="h3 in" data-cue="728" style="margin-top:20px">Primer transporte: 728 presos polacos</div></div>', shade=True)
sc("Sobre su puerta, el mismo lema que en Dachau: Arbeit macht frei. El trabajo os hará libres. Era mentira.",
   bg='dachau2',
   html='<div class="ov center"><div class="h1 in tw" data-t="0.5" style="font-family:TY;letter-spacing:6px">ARBEIT MACHT FREI</div>'
        '<div class="h3 dim in" data-cue="el trabajo os hara libres" style="margin-top:30px">«El trabajo os hará libres»</div>'
        '<div class="stamp in" data-cue="era mentira" style="margin-top:50px">Mentira</div></div>')
sc("En septiembre de 1941, en el sótano del bloque 11, las SS prueban por primera vez un pesticida, el Zyklon B, para matar personas. "
   "Las víctimas son cientos de prisioneros de guerra soviéticos y de presos enfermos.",
   bg='birkenau48',
   html='<div class="ov center"><div class="date in" data-t="0.2">Septiembre de 1941 · Bloque 11</div><div class="h1 in tw" data-t="0.6">Zyklon B</div>'
        '<div class="h3 dim in" data-cue="las victimas" style="margin-top:30px">Primeras víctimas: prisioneros soviéticos y presos enfermos</div></div>')
sc("Un mes después empiezan a construir un segundo campo, a unos tres kilómetros: Auschwitz-Birkenau. Será mucho más grande que el primero.",
   img='birkenau48', kb='left', cap='Auschwitz-Birkenau, 1948: los barracones después de la guerra',
   html='<div class="ov right"><div class="date in" data-t="0.2">Octubre de 1941</div><div class="h2 in" data-cue="auschwitz-birkenau">Birkenau</div></div>', shade=True)

# ---------- EXTERMINIO ----------
sc("Y aquí hay que entender una diferencia clave. Hasta entonces, los campos de concentración eran lugares de encierro, trabajo forzado y muerte por hambre, palizas y enfermedades. "
   "Pero a partir de diciembre de 1941 aparece algo nuevo: los centros de exterminio. Lugares construidos con un único objetivo: asesinar a la gente nada más llegar.",
   bg='deportacion',
   html='<div class="ov center"><div class="row" style="gap:80px;align-items:stretch">'
        '<div class="box in" data-t="0.4" style="width:640px"><div class="lab">Campo de concentración</div><div class="txt" style="margin-top:14px">Encierro, trabajo forzado, muerte por hambre, palizas y enfermedades</div></div>'
        '<div class="box in" data-cue="centros de exterminio" style="width:640px;border-color:var(--red)"><div class="lab">Centro de exterminio</div><div class="txt" style="margin-top:14px">Asesinato nada más llegar</div></div></div></div>')
sc("El primero fue Chelmno, en diciembre de 1941. En 1942 llegarían Belzec, Sobibor y Treblinka. Solo en estos tres, las SS asesinaron a alrededor de un millón y medio de judíos en menos de dos años. "
   "Muy pocos sobrevivieron para contarlo.",
   bg='deportacion',
   html=timeline([('Dic. 1941', 'Chelmno', 'chelmno'), ('Mar. 1942', 'Belzec', 'belzec'), ('May. 1942', 'Sobibor', 'sobibor'), ('Jul. 1942', 'Treblinka', 'treblinka')],
                 'Centros de exterminio', extra='<div class="h2 red in" data-cue="un millon y medio" style="margin-top:80px">≈ 1.500.000 judíos asesinados</div>'))
sc("El 20 de enero de 1942, quince altos cargos nazis se reúnen en una villa a orillas del lago Wannsee, en Berlín. En una reunión de apenas hora y media, "
   "coordinan lo que llaman la solución final de la cuestión judía: el asesinato de todos los judíos de Europa.",
   img='wannsee', kb='in', fallback='deportacion', cap='La villa de Wannsee, hoy un museo y memorial',
   html='<div class="ov left"><div class="date in" data-t="0.2">20 de enero de 1942</div><div class="h2 in tw" data-t="0.6">Conferencia<br>de Wannsee</div></div>', shade=True)
sc("Auschwitz-Birkenau se convierte en las dos cosas a la vez: campo de concentración y centro de exterminio. Al llegar los trenes, médicos de las SS hacen una selección en el andén. "
   "Unos pocos son elegidos para trabajar. La mayoría, incluidos casi todos los niños y los ancianos, van directamente a las cámaras de gas.",
   img='rampa', kb='in', fallback='deportacion', cap='Auschwitz-Birkenau, 1944: llegada de judíos de Hungría',
   html='<div class="ov right low"><div class="h2 in tw" data-cue="hacen una seleccion">La selección</div></div>', shade=True)
sc("En total, en Auschwitz fueron asesinadas más de 1,1 millones de personas. Casi un millón eran judíos. También murieron allí polacos, gitanos, prisioneros de guerra soviéticos y presos de muchos otros países.",
   bg='birkenau48',
   html='<div class="ov center"><div class="h3 dim in" data-t="0">Asesinados en Auschwitz</div><div class="big red in" data-t="0.4"><span data-count="1100000">0</span></div>'
        '<div class="h3 in" data-cue="casi un millon" style="margin-top:20px">Casi 1.000.000 eran judíos</div>'
        '<div class="txt dim in" data-cue="tambien murieron" style="margin-top:30px;max-width:1300px;text-align:center">También polacos, gitanos, prisioneros soviéticos y presos de otros países</div></div>')
sc("En enero de 1945, el sistema tenía registrados más de 700.000 presos, repartidos en decenas de campos principales y cientos de campos secundarios.",
   bg='sachsenhausen',
   html='<div class="ov center"><div class="date in" data-t="0.2">Enero de 1945</div><div class="big in" data-t="0.4"><span data-count="700000">0</span></div>'
        '<div class="h3 in" data-cue="presos">presos registrados en los campos</div></div>')

# ---------- LIBERACIÓN ----------
sc("El 27 de enero de 1945, soldados soviéticos llegan a Auschwitz. Encuentran a unos 7.000 presos, enfermos y agotados. "
   "Días antes, las SS habían obligado a cerca de 60.000 a marchar hacia el oeste, en las llamadas marchas de la muerte.",
   img='liberacion', kb='in', fallback='birkenau48', cap='Auschwitz, enero de 1945: presos liberados',
   html='<div class="ov left"><div class="date in" data-t="0.2">27 de enero de 1945</div><div class="h2 in tw" data-t="0.6">Liberación<br>de Auschwitz</div>'
        '<div class="h3 in" data-cue="unos 7.000">7.000 supervivientes en el campo</div></div>', shade=True)
sc("Y el 29 de abril de 1945, tropas estadounidenses liberan Dachau, el campo donde empezó todo. Por él habían pasado más de 200.000 presos. Al menos 40.000 murieron allí.",
   bg='dachau1',
   html='<div class="ov center"><div class="date in" data-t="0.2">29 de abril de 1945 · Dachau</div>'
        '<div class="row" style="margin-top:30px"><div class="box in" data-cue="200.000"><div class="lab">Presos</div><div class="val">+200.000</div></div>'
        '<div class="box in" data-cue="40.000"><div class="lab">Muertos</div><div class="val red">+40.000</div></div></div></div>')

# ---------- CIERRE ----------
sc("Ningún campo nació como una fábrica de muerte. Empezaron como cárceles para opositores, sin juicio, y con la excusa de proteger al país. Cada paso hizo posible el siguiente. "
   "Por eso, desde 2005, el 27 de enero es el Día Internacional en Memoria de las Víctimas del Holocausto.",
   bg='birkenau48',
   html='<div class="ov center"><div class="q in" data-t="0.4">Ningún campo nació como una fábrica de muerte.</div>'
        '<div class="h3 amber in" data-cue="cada paso" style="margin-top:50px">Cada paso hizo posible el siguiente</div>'
        '<div class="date in" data-cue="27 de enero" style="margin-top:50px">27 de enero · Día Internacional en Memoria de las Víctimas del Holocausto</div></div>')
sc("En el próximo capítulo entraremos en Auschwitz por dentro: cómo funcionaba, quién lo dirigía y cómo algunos lograron sobrevivir. Si no quieres perdértelo, suscríbete. "
   "Y cuéntame en los comentarios: ¿conocías la historia de Dachau?",
   bg='birkenau48',
   html='<div class="ov center"><div class="tag in" data-t="0.2">Próximo capítulo</div><div class="h2 in tw" data-t="0.4">Auschwitz por dentro</div>'
        '<div class="rule in" data-t="0.6"></div><div class="h3 dim in" data-cue="suscribete">Suscríbete para no perdértelo</div>'
        '<div class="who in" data-cue="suscribete" data-d="1.5" style="font-size:24px;margin-top:80px">Fuentes: USHMM, Memorial y Museo de Auschwitz-Birkenau. '
        'Imágenes: Bundesarchiv y Wikimedia Commons (créditos en la descripción).</div></div>')

MOOD = {**{i: 'tension' for i in (0, 6, 7, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28)}, **{i: 'melancolia' for i in (14, 29, 30, 31, 32)}}
for i, s_ in enumerate(S): s_['mood'] = MOOD.get(i, 'inquietud')

spec = dict(title='De Dachau a Auschwitz', brand='Sombras del 39', voice='hyKxCTlAqtnW188CgltM', model='eleven_v4',
            voice_settings=dict(stability=0.5, similarity_boost=0.75), tail=4, scenes=S,
            thumb=dict(img='img/dachau1.jpg', fy=0.45, l1='Así empezó<br>el horror', l2='1933', l3='De Dachau a Auschwitz'))
json.dump(spec, open(os.path.join(here, 'spec.json'), 'w'), ensure_ascii=False, indent=1)
txt = ' '.join(s['say'] for s in S)
print(len(S), 'escenas ·', len(txt), 'caracteres · ~%.1f min' % (len(txt) / 13.8 / 60), '· sin foto:', [i for i, s in enumerate(S) if 'img' not in s and 'bg' not in s])
open(os.path.join(here, 'guion.txt'), 'w').write('\n\n'.join(s['say'] for s in S) + '\n')
