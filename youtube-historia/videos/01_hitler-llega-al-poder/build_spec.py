# Genera spec.json del episodio 1. Uso: python3 build_spec.py
import json, os

ELEC = [('1928', 2.6, 12), ('1930', 18.3, 107), ('JUL 1932', 37.3, 230), ('NOV 1932', 33.1, 196), ('MAR 1933', 43.9, 288)]

def chart(n, cue, majority=False):
    """Gráfico con las elecciones 0..n; la n-ésima crece cuando se dice `cue`."""
    cols = []
    for i, (yr, pct, seats) in enumerate(ELEC[:n + 1]):
        new = i == n
        h = f'{pct * 10:.0f}px'
        grow = f' class="grow" data-cue="{cue}" style="--h:{h};height:0"' if new else f' style="height:{h}"'
        lab = f'<b class="in" data-cue="{cue}" data-d="0.4">{str(pct).replace(".", ",")} %</b>' if new else f'<b>{str(pct).replace(".", ",")} %</b>'
        cols.append(f'<div class="c{" hi" if new else ""}">{lab}<i{grow}></i><div class="yr">{yr}</div></div>')
    maj = ('<div class="majority in" data-t="0.3" style="bottom:500px"><span>MAYORÍA ABSOLUTA · 50 %</span></div>' if majority else '')
    return (f'<div class="ov center"><div class="h3 dim in" data-t="0" style="margin-bottom:50px">Votos del partido nazi en las elecciones al Reichstag</div>'
            f'<div class="chart" style="position:relative">{maj}{"".join(cols)}</div></div>')

S = []
def sc(say, **kw): S.append(dict(say=say, **kw))

# ---------- GANCHO ----------
sc("Adolf Hitler nunca ganó la mayoría absoluta en unas elecciones libres. Ni una sola vez. Su mejor resultado, con otros partidos en las urnas, fue un 43,9 % de los votos. "
   "Y aun así, en solo 18 meses, pasó de ser un canciller vigilado por los conservadores a convertirse en el dueño absoluto de Alemania.",
   img='img/hitler.jpg', side='right', kb='in', fy=0.35,
   html='<div class="ov left"><div class="h2 in" data-t="0">Nunca ganó<br>la mayoría</div><div class="rule in" data-t="0"></div>'
        '<div class="big red in" data-cue="43,9"><span data-count="43.9" data-dec="1" data-fmt=" %">0 %</span></div>'
        '<div class="h3 in" data-cue="18 meses">18 meses para<br>el poder absoluto</div></div>')
sc("¿Cómo es posible que una de las democracias más modernas de Europa acabara en manos de un dictador? Esta es la historia de cómo Hitler llegó al poder. Paso a paso.",
   img='img/reichstag.jpg', kb='out', shade=True,
   html='<div class="ov center"><div class="tag in" data-t="0.5">Capítulo 1</div>'
        '<div class="h1 in" data-t="0.6">Cómo Hitler<br>llegó al poder</div>'
        '<div class="date in" data-cue="paso a paso" style="margin-top:30px">1918 — 1934</div></div>')

# ---------- 1918-1923 ----------
sc("Para entenderlo hay que volver a 1918. Alemania pierde la Primera Guerra Mundial. Y en 1919, en el Tratado de Versalles, los vencedores le imponen condiciones durísimas: "
   "pierde territorio y colonias, su ejército queda reducido a 100.000 hombres y tiene que pagar enormes reparaciones de guerra.",
   img='img/versalles.jpg', kb='left', cap='Versalles, 28 de junio de 1919',
   html='<div class="ov right low"><div class="box in" data-cue="100.000"><div class="lab">Ejército permitido</div><div class="val">100.000 hombres</div></div></div>')
sc("Muchos alemanes no lo aceptan. Al acabar la guerra, ningún soldado enemigo había llegado a pisar Berlín. Y nace un mito venenoso: la puñalada por la espalda. "
   "La idea de que Alemania no perdió en el campo de batalla, sino que fue traicionada desde dentro por políticos, socialistas y judíos. Era mentira. Pero se convertirá en una de las armas favoritas de Hitler.",
   html='<div class="ov center"><div class="q in" data-cue="punalada">«La puñalada por la espalda»</div>'
        '<div class="who in" data-cue="traicionada">El mito que culpaba a políticos, socialistas y judíos de la derrota</div>'
        '<div class="stamp in" data-cue="era mentira" style="margin-top:60px">Falso</div></div>')
sc("Mientras tanto nace la República de Weimar, la primera democracia de la historia de Alemania. Nace débil, en plena crisis, y odiada tanto por la extrema derecha como por la extrema izquierda.",
   img='img/weimar.jpg', kb='in', cap='Weimar, 1919: diputados de la Asamblea Nacional')
sc("En Múnich, un antiguo cabo del ejército, nacido en Austria, entra en 1919 en un pequeño partido de extrema derecha. Se llama Adolf Hitler. Descubre que tiene un talento especial: "
   "sabe hablar a las masas. En 1921 ya es el jefe de ese partido, que ahora se llama Partido Nacionalsocialista Obrero Alemán. El partido nazi.",
   img='img/burgerbrau.jpg', kb='right', cap='Mitin del partido nazi en Múnich, 1923',
   html='<div class="ov left low"><div class="tag in" data-cue="partido nacionalsocialista">NSDAP</div></div>')
sc("Y en 1923 llega el desastre. La economía alemana entra en una hiperinflación brutal. Los precios se disparan cada hora. En noviembre de ese año, un solo dólar llega a valer unos 4,2 billones de marcos. "
   "Los ahorros de toda una vida ya no sirven ni para comprar pan.",
   img='img/cola1923.jpg', kb='in', cap='Berlín, 1923: cola ante una tienda de comestibles',
   html='<div class="ov center"><div class="box in" data-cue="un solo dolar"><div class="lab">1 dólar = </div>'
        '<div class="val mono"><span data-count="4200000000000" data-fmt=" marcos">0</span></div></div></div>')
sc("Hay billetes de millones y de billones de marcos. Algunos alemanes llegan a usarlos para empapelar las paredes, porque valen menos que el papel pintado.",
   img='img/inflacion.jpg', kb='up', fy=0.3, side='right',
   html='<div class="ov left"><div class="date in" data-t="0.2">Noviembre de 1923</div><div class="h2 in" data-cue="empapelar">El dinero vale<br>menos que el papel</div></div>')

# ---------- PUTSCH Y CÁRCEL ----------
sc("Hitler cree que ha llegado su momento. La noche del 8 de noviembre de 1923 irrumpe con sus hombres en una cervecería de Múnich y proclama una revolución nacional. "
   "Al día siguiente marcha con unos dos mil seguidores hacia el centro de la ciudad. La policía abre fuego. Mueren cuatro policías y dieciséis nazis. El golpe fracasa.",
   img='img/putsch.jpg', kb='left', shade=True, cap='Múnich, noviembre de 1923: golpistas armados',
   html='<div class="ov right"><div class="date in" data-t="0.2">8-9 de noviembre de 1923</div><div class="h2 in" data-t="0.4">El golpe de<br>la cervecería</div>'
        '<div class="stamp in" data-cue="el golpe fracasa" style="margin-top:40px">Fracasa</div></div>')
sc("Hitler es detenido y juzgado por alta traición. Pero el juicio se convierte en su escaparate: durante semanas, los periódicos de toda Alemania publican sus discursos. "
   "El tribunal le condena a 5 años de cárcel, la pena mínima. Y en diciembre de 1924 ya está en la calle, tras menos de un año entre rejas.",
   img='img/juicio.jpg', kb='in', cap='Múnich, 1924: el juicio a Hitler y Ludendorff',
   html='<div class="ov right low"><div class="row"><div class="box in" data-cue="5 anos"><div class="lab">Condena</div><div class="val">5 años</div></div>'
        '<div class="box in" data-cue="menos de un ano"><div class="lab">Cumple</div><div class="val red">&lt; 1 año</div></div></div></div>')
sc("Su celda en la prisión de Landsberg es casi una habitación de hotel. Recibe visitas, regalos y periódicos. Allí dicta Mi lucha, el libro en el que deja por escrito su odio a los judíos "
   "y su sueño de conquistar espacio vital en el Este.",
   img='img/landsberg.jpg', kb='right', cap='Prisión de Landsberg, 1924')
sc("Y saca una lección que lo cambiará todo: el poder no se toma por la fuerza. Se conquista desde dentro, usando las reglas de la propia democracia. A través de las urnas.",
   html='<div class="ov left"><div class="q in" data-cue="el poder no se toma">El poder no se toma por la fuerza.</div>'
        '<div class="h3 amber in" data-cue="a traves de las urnas" style="margin-top:40px">Se conquista en las urnas</div></div>')

# ---------- 1924-1932 ----------
sc("Pero al principio, las urnas no le quieren. Entre 1924 y 1929, la economía se recupera gracias a los créditos de Estados Unidos, y Alemania vive sus años dorados. "
   "En las elecciones de 1928, el partido nazi saca un ridículo 2,6 % de los votos.",
   html=chart(0, 'pero al principio'))
sc("Entonces, en octubre de 1929, se hunde la Bolsa de Nueva York. Los bancos estadounidenses reclaman sus préstamos y la crisis golpea a Alemania como a casi ningún otro país.",
   img='img/wallstreet.jpg', kb='in', cap='Nueva York, 24 de octubre de 1929')
sc("El paro pasa de menos de 1,3 millones de personas en 1929 a más de 6 millones a principios de 1932. Casi uno de cada cuatro trabajadores alemanes no tiene empleo.",
   img='img/parados.jpg', kb='left', cap='Berlín, 1932: hombres de las SA sin trabajo', shade=True,
   html='<div class="ov center"><div class="h3 dim in" data-t="0.2">Parados en Alemania</div>'
        '<div class="big in" data-cue="mas de 6 millones"><span data-count="6000000">0</span></div>'
        '<div class="h3 red in" data-cue="uno de cada cuatro">1 de cada 4 trabajadores</div></div>')
sc("Y aquí Hitler encuentra su oportunidad. Promete trabajo, orden y orgullo. Culpa de todo a los judíos, a los comunistas y a los políticos de Weimar. "
   "Su jefe de propaganda, Joseph Goebbels, inunda el país de carteles, mítines y desfiles. Hitler llega a recorrer Alemania en avión para dar varios discursos en un mismo día, algo nunca visto.",
   img='img/mitin.jpg', kb='right', cap='Berlín, abril de 1932: mitin nazi en el Lustgarten')
sc("En septiembre de 1930, el resultado es un terremoto: los nazis pasan del 2,6 al 18,3 %, y de 12 a 107 diputados. Ya son la segunda fuerza del Parlamento.",
   html=chart(1, 'septiembre de 1930'))
sc("El Parlamento queda bloqueado. Ningún gobierno consigue una mayoría estable, y el país se gobierna a golpe de decretos firmados por el presidente: "
   "el mariscal Paul von Hindenburg, héroe de la Primera Guerra Mundial, que ya tiene más de 80 años.",
   img='img/hindenburg.jpg', side='right', kb='in', fy=0.3,
   html='<div class="ov left"><div class="date in" data-cue="presidente">Presidente del Reich</div><div class="h2 in" data-cue="hindenburg">Paul von<br>Hindenburg</div>'
        '<div class="h3 dim in" data-cue="mas de 80">Más de 80 años</div></div>')
sc("En 1932, Hitler se atreve a presentarse a las elecciones a presidente contra él. Pierde. Hindenburg gana con el 53 % en la segunda vuelta. "
   "Pero Hitler consigue casi un 37 %: más de 13 millones de alemanes le han votado.",
   img='img/cartel.jpg', side='left', kb='up', fy=0.3,
   html='<div class="ov right"><div class="date in" data-t="0.2">Elecciones presidenciales · abril de 1932</div>'
        '<div class="row" style="justify-content:flex-end"><div class="box in" data-cue="53"><div class="lab">Hindenburg</div><div class="val">53 %</div></div>'
        '<div class="box in" data-cue="casi un 37"><div class="lab">Hitler</div><div class="val red">36,8 %</div></div></div></div>')
sc("Y en julio de 1932 llega su gran triunfo. El partido nazi saca el 37,3 % de los votos y 230 diputados. Es, con diferencia, el partido más votado de Alemania. "
   "Hitler exige que le nombren canciller. Hindenburg se niega: desprecia a ese cabo bohemio, como le llama.",
   html=chart(2, 'julio de 1932', majority=True))
sc("En noviembre hay nuevas elecciones. Y ocurre algo que casi nadie recuerda: los nazis bajan. Pierden unos dos millones de votos y se quedan en el 33,1 %. "
   "El partido está endeudado y agotado. Algunos creen que Hitler ya ha tocado techo.",
   html=chart(3, 'nuevas elecciones', majority=True))

# ---------- ENERO 1933 ----------
sc("Pero lo que no le dan las urnas, se lo darán los despachos. El ex canciller Franz von Papen y otros políticos conservadores convencen a Hindenburg de un plan: "
   "nombrar a Hitler canciller, pero rodeado de ministros conservadores. Creen que podrán controlarlo.",
   img='img/papen.jpg', side='right', kb='in', fy=0.3,
   html='<div class="ov left"><div class="date in" data-t="0.2">Enero de 1933</div><div class="h2 in" data-cue="franz von papen">Franz<br>von Papen</div>'
        '<div class="h3 amber in" data-cue="podran controlarlo" style="margin-top:30px">«Podemos controlarlo»</div></div>')
sc("En el nuevo gobierno solo habrá 3 nazis entre 11 ministros. A Papen se le atribuye una frase que pasará a la historia: en dos meses lo habremos arrinconado tanto que chillará.",
   img='img/gabinete.jpg', kb='right', cap='Berlín, 30 de enero de 1933: el gobierno de Hitler',
   html='<div class="ov center low"><div class="q in" data-cue="en dos meses" style="font-size:52px;background:rgba(13,12,10,.75);padding:24px 40px">«En dos meses lo habremos arrinconado tanto que chillará»</div></div>')
sc("El 30 de enero de 1933, Hindenburg nombra a Adolf Hitler canciller de Alemania. Esa noche, miles de nazis desfilan con antorchas por Berlín. "
   "Hitler ha llegado al poder de forma legal. Y ahora va a destruir, desde dentro, la democracia que se lo ha permitido.",
   img='img/antorchas.jpg', kb='in', cap='Berlín, noche del 30 de enero de 1933',
   html='<div class="ov left"><div class="date in" data-t="0.2">30 de enero de 1933</div><div class="h1 in" data-cue="canciller de alemania">Canciller</div></div>')

# ---------- DESMONTAR LA DEMOCRACIA ----------
sc("Solo cuatro semanas después, la noche del 27 de febrero, arde el Reichstag, el edificio del Parlamento. En el lugar detienen a un joven comunista holandés, Marinus van der Lubbe. "
   "Hitler lo presenta como el comienzo de una revolución comunista.",
   img='img/incendio.jpg', kb='up', fy=0.35, side='right',
   html='<div class="ov left"><div class="date in" data-t="0.2">27 de febrero de 1933</div><div class="h2 in" data-cue="arde el reichstag">Arde el<br>Reichstag</div></div>')
sc("Al día siguiente, Hindenburg firma un decreto de emergencia que suspende los derechos básicos: la libertad de expresión, de prensa y de reunión. "
   "Miles de comunistas y opositores son detenidos. Ese decreto seguirá en vigor hasta el final del régimen nazi.",
   img='img/palco.jpg', kb='in', shade=True, cap='El interior del Reichstag tras el incendio',
   html='<div class="ov center"><div class="h3 in" data-cue="libertad de expresion">Libertad de expresión</div>'
        '<div class="h3 in" data-cue="de prensa">Libertad de prensa</div><div class="h3 in" data-cue="de reunion">Libertad de reunión</div>'
        '<div class="stamp in" data-cue="detenidos" style="margin-top:40px">Suspendidas</div></div>')
sc("Con la oposición perseguida y las calles llenas de matones de las SA, se celebran las elecciones del 5 de marzo de 1933. Y aun así, los nazis no consiguen la mayoría: se quedan en el 43,9 %. "
   "Es su mejor resultado. Nunca pasarán de ahí en unas elecciones con varios partidos.",
   html=chart(4, '5 de marzo', majority=True))
sc("Ese mismo mes, el 22 de marzo de 1933, abre sus puertas Dachau, cerca de Múnich. Es uno de los primeros campos de concentración. Sus primeros presos son opositores políticos. "
   "Solo es el principio de lo que vendrá.",
   img='img/dachau.jpg', kb='in', shade=True, cap='Dachau, 1933: presos de camino al rancho',
   html='<div class="ov left"><div class="date in" data-t="0.2">22 de marzo de 1933</div><div class="h2 in" data-cue="dachau">Dachau</div></div>')
sc("Y el 23 de marzo llega el golpe definitivo: la Ley Habilitante. Permite al gobierno de Hitler aprobar leyes sin pasar por el Parlamento, incluso leyes que van contra la Constitución. "
   "Para aprobarla, hacen falta dos tercios de los votos.",
   img='img/kroll.jpg', kb='in', shade=True, cap='Berlín, 23 de marzo de 1933: Hitler defiende la ley',
   html='<div class="ov left"><div class="date in" data-t="0.2">23 de marzo de 1933</div><div class="h2 in" data-cue="ley habilitante">Ley<br>Habilitante</div></div>')
sc("La votación se celebra en la Ópera Kroll, con el edificio rodeado por hombres de las SA y de las SS. Los diputados comunistas están detenidos o han huido. "
   "Los demás partidos ceden entre promesas y miedo. Resultado: 444 votos a favor y 94 en contra. Solo los socialdemócratas votan que no. El Parlamento acaba de votar su propia desaparición.",
   html='<div class="ov center"><div class="date in" data-t="0.2">23 de marzo de 1933 · Ópera Kroll</div><div class="h2 in" data-t="0.3" style="margin-bottom:50px">La votación</div><div class="row"><div class="box in" data-cue="444"><div class="lab">A favor</div><div class="val">444</div></div>'
        '<div class="box in" data-cue="94 en contra"><div class="lab">En contra</div><div class="val red">94</div></div></div>'
        '<div class="h3 amber in" data-cue="su propia desaparicion" style="margin-top:50px">El Parlamento vota su propio final</div></div>')
sc("A partir de ahí, todo va muy rápido. En mayo, los sindicatos son disueltos. El resto de partidos son prohibidos o se disuelven. "
   "Y en julio de 1933, una ley convierte al partido nazi en el único partido legal de Alemania. En apenas seis meses, la democracia ha desaparecido.",
   html='<div class="ov center"><div class="tl">'
        '<div class="e in" data-cue="en mayo"><div class="d">Mayo 1933</div><div class="t">Sindicatos disueltos</div></div>'
        '<div class="e in" data-cue="el resto de partidos"><div class="d">Junio 1933</div><div class="t">Partidos prohibidos</div></div>'
        '<div class="e in" data-cue="julio de 1933"><div class="d">Julio 1933</div><div class="t">Partido único</div></div></div>'
        '<div class="h2 red in" data-cue="seis meses" style="margin-top:90px">6 meses</div></div>')

# ---------- 1934 ----------
sc("Solo le quedaba un peligro, y estaba dentro de su propio movimiento: las SA de Ernst Röhm, que ya tenían millones de miembros. El ejército las veía como una amenaza. "
   "Entre el 30 de junio y el 2 de julio de 1934, en la Noche de los cuchillos largos, Hitler ordena asesinar a Röhm y a decenas de rivales, quizá cientos. Nadie es juzgado.",
   img='img/rohm.jpg', side='right', kb='in', fy=0.3,
   html='<div class="ov left"><div class="date in" data-cue="30 de junio">30 de junio de 1934</div><div class="h2 in" data-cue="cuchillos largos">La Noche de<br>los cuchillos largos</div>'
        '<div class="stamp in" data-cue="nadie es juzgado" style="margin-top:40px">Sin juicio</div></div>')
sc("El 2 de agosto de 1934 muere Hindenburg, a los 86 años. Ese mismo día, Hitler une los cargos de presidente y canciller. Ya no es solo el jefe del gobierno: es el Führer.",
   img='img/potsdam.jpg', kb='in', fx=0.45, cap='Hitler y Hindenburg en Potsdam, marzo de 1933',
   html='<div class="ov left low"><div class="date in" data-t="0.2">2 de agosto de 1934</div><div class="h1 in" data-cue="es el fuhrer">Führer</div></div>')
sc("Y los soldados ya no juran lealtad a la Constitución. Ahora juran obediencia personal a Adolf Hitler. "
   "El 19 de agosto, un plebiscito sin oposición posible lo aprueba con cerca del 90 % de los votos. Han pasado unos 18 meses desde que fue nombrado canciller.",
   img='img/juramento.jpg', kb='right', cap='Agosto de 1934: soldados juran lealtad a Hitler',
   html='<div class="ov right"><div class="box in" data-cue="unos 18 meses"><div class="lab">De canciller a dictador</div><div class="val">18 meses</div></div></div>')

# ---------- CIERRE ----------
sc("Hitler nunca ganó la mayoría absoluta en unas elecciones libres. No le hizo falta. Le bastaron una crisis brutal, el miedo, una propaganda incansable, "
   "y unos políticos que creyeron que podrían usarlo y controlarlo. La democracia alemana no cayó en un solo día: la fueron desmontando, ley a ley, mientras muchos miraban hacia otro lado.",
   img='img/antorchas.jpg', kb='out', shade=True,
   html='<div class="ov center"><div class="h3 in" data-cue="una crisis brutal">Una crisis brutal</div><div class="h3 in" data-cue="el miedo">El miedo</div>'
        '<div class="h3 in" data-cue="una propaganda">La propaganda</div><div class="h3 amber in" data-cue="unos politicos">Políticos que creyeron que podrían controlarlo</div>'
        '<div class="q in" data-cue="ley a ley" style="margin-top:50px">La democracia no cayó en un día.<br>La desmontaron ley a ley.</div></div>')
sc("Lo que vino después, la guerra, los campos de concentración y el Holocausto, lo veremos en los próximos capítulos. Si no quieres perdértelos, suscríbete. "
   "Y cuéntame en los comentarios: ¿qué momento de esta historia te parece el más decisivo?",
   html='<div class="ov center"><div class="tag in" data-t="0.2">Próximo capítulo</div><div class="h2 in" data-t="0.4">De Dachau a Auschwitz</div>'
        '<div class="rule in" data-t="0.6"></div><div class="h3 dim in" data-cue="suscribete">Suscríbete para no perdértelo</div>'
        '<div class="who in" data-cue="suscribete" data-d="1.5" style="font-size:24px;margin-top:80px">Fuentes: USHMM, Bundestag, Britannica, Deutsches Historisches Museum. '
        'Imágenes: Bundesarchiv, NARA, Biblioteca Nacional de Francia y Wikimedia Commons (créditos en la descripción).</div></div>')

# ---------- ambiente, fondos y máquina de escribir ----------
MOOD = {**{i: 'tension' for i in (0, 1, 8, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33)}, **{i: 'melancolia' for i in (34, 35)}}
BG = {3: 'img/versalles.jpg', 11: 'img/landsberg.jpg', 12: 'img/weimar.jpg', 16: 'img/mitin.jpg', 19: 'img/cartel.jpg',
      20: 'img/parados.jpg', 26: 'img/antorchas.jpg', 29: 'img/kroll.jpg', 30: 'img/gabinete.jpg', 35: 'img/reichstag.jpg'}
TW = (1, 8, 23, 24, 27, 28, 31, 32, 35)  # títulos que se teclean
for i, sc_ in enumerate(S):
    sc_['mood'] = MOOD.get(i, 'inquietud')
    if i in BG and 'img' not in sc_: sc_['bg'] = BG[i]
    if i in TW: sc_['html'] = sc_['html'].replace('class="h1 in"', 'class="h1 in tw"').replace('class="h2 in"', 'class="h2 in tw"')

spec = dict(title='Cómo Hitler llegó al poder', brand='Archivo 39·45', voice='hyKxCTlAqtnW188CgltM', model='eleven_v4',
            voice_settings=dict(stability=0.5, similarity_boost=0.75), tail=3, scenes=S,
            thumb=dict(img='img/hitler.jpg', fy=0.25, l1='Nunca ganó<br>la mayoría', l2='43,9 %', l3='Cómo llegó al poder'))
here = os.path.dirname(os.path.abspath(__file__))
json.dump(spec, open(os.path.join(here, 'spec.json'), 'w'), ensure_ascii=False, indent=1)
txt = ' '.join(s['say'] for s in S)
print(len(S), 'escenas ·', len(txt), 'caracteres · ~%.1f min' % (len(txt) / 13.8 / 60))
open(os.path.join(here, 'guion.txt'), 'w').write('\n\n'.join(s['say'] for s in S) + '\n')
