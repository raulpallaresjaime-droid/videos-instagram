# Genera spec.json del episodio 3 (mini documental 15-20 min). Uso: python3 build_spec.py
import json, os
here = os.path.dirname(os.path.abspath(__file__))
has = lambda n: os.path.exists(os.path.join(here, 'img', n + '.jpg'))

S = []
def sc(say, **kw):
    if 'img' in kw and not has(kw['img']):
        fb = kw.pop('fallback', 'birkenau'); kw.pop('img'); kw.pop('side', None); kw.pop('kb', None); kw.pop('cap', None)
        kw['bg'] = f'img/{fb}.jpg'
    elif 'img' in kw:
        kw['img'] = f"img/{kw['img']}.jpg"; kw.pop('fallback', None)
    if 'bg' in kw and not kw['bg'].startswith('img/'): kw['bg'] = f"img/{kw['bg']}.jpg"
    S.append(dict(say=say, **kw))

def timeline(items, title=None, extra=''):
    ev = ''.join(f'<div class="e in" data-cue="{c}"><div class="d">{d}</div><div class="t">{t}</div></div>' for d, t, c in items)
    head = f'<div class="h3 dim in" data-t="0" style="margin-bottom:80px">{title}</div>' if title else ''
    return f'<div class="ov center">{head}<div class="tl">{ev}</div>{extra}</div>'

def bars(rows, title, maxv):
    # rows: (etiqueta, valor, texto, cue, color)
    out = ''
    for lab, v, txt, cue, col in rows:
        w = max(1.2, 100 * v / maxv)
        out += (f'<div class="in" data-cue="{cue}" style="display:flex;align-items:center;gap:30px;margin:16px 0;width:1500px">'
                f'<div class="h3" style="width:430px;text-align:right;font-size:42px">{lab}</div>'
                f'<div style="flex:1;height:58px;position:relative"><i class="grow" data-cue="{cue}" style="--w:{w:.1f}%;display:block;height:100%;width:0;background:{col}"></i></div>'
                f'<div class="mono" style="width:300px;font-size:44px">{txt}</div></div>')
    return f'<div class="ov center"><div class="h3 dim in" data-t="0" style="margin-bottom:50px">{title}</div>{out}</div>'

def plain(t, cue='', size=48, cls=''):
    return f'<div class="txt in {cls}" data-cue="{cue}" style="font-size:{size}px;max-width:1400px;text-align:center;margin-top:26px">{t}</div>'

# ======================= GANCHO =======================
sc("Al menos un millón trescientas mil personas fueron deportadas a un mismo lugar del sur de Polonia. Más de un millón cien mil nunca salieron de allí. "
   "Ningún otro sitio de la historia concentra tanta muerte. Se llamaba Auschwitz. Y hoy vamos a entrar en él para entender cómo funcionaba.",
   bg='puerta_birkenau',
   html='<div class="ov center"><div class="h3 dim in" data-t="0">Deportadas a Auschwitz</div>'
        '<div class="big in" data-t="0.2"><span data-count="1300000">0</span></div>'
        '<div class="h3 dim in" data-cue="mas de un millon cien mil" style="margin-top:40px">Nunca salieron</div>'
        '<div class="big red in" data-cue="mas de un millon cien mil"><span data-count="1100000">0</span></div></div>')
sc("Un complejo de campos que fue, a la vez, cárcel, fábrica de esclavos y centro de exterminio. Esta es su historia.",
   img='puerta_birkenau', kb='in', shade=True,
   html='<div class="ov center"><div class="tag in" data-t="0.4">Capítulo 3</div>'
        '<div class="h1 in" data-t="0.6">Auschwitz<br>por dentro</div>'
        '<div class="date in" data-cue="esta es su historia" style="margin-top:30px">1940 — 1945</div></div>')

# ======================= 1940: EL ORIGEN =======================
sc("Para entender Auschwitz hay que volver a 1939. Alemania invade Polonia y se anexiona su parte occidental. Entre los territorios anexionados está una pequeña ciudad, Oswiecim. "
   "Los alemanes la llaman Auschwitz.",
   img='polonia', kb='right', cap='Polonia, septiembre de 1939: judíos detenidos por la policía alemana',
   html='<div class="ov left"><div class="date in" data-t="0.2">Septiembre de 1939</div><div class="h2 in tw" data-cue="los alemanes la llaman">Oswiecim<br>= Auschwitz</div></div>', shade=True)
sc("En los primeros meses de ocupación, las cárceles polacas se llenan de detenidos: profesores, sacerdotes, soldados, miembros de la resistencia. "
   "Las SS necesitan un nuevo campo, y Heinrich Himmler aprueba uno junto a esa ciudad, en un antiguo cuartel del ejército polaco.",
   img='himmler', side='right', kb='in', fy=0.3,
   html='<div class="ov left"><div class="date in" data-t="0.2">Abril de 1940</div><div class="h2 in" data-cue="heinrich himmler">Himmler<br>aprueba<br>el campo</div>'
        '<div class="h3 dim in" data-cue="antiguo cuartel" style="margin-top:20px">Un antiguo cuartel polaco</div></div>')
sc("Lo elige por algo muy concreto: está en un cruce de líneas de ferrocarril. Desde allí se puede llegar en tren a casi cualquier rincón de Europa. Esa decisión técnica será, años después, una condena para millones.",
   bg='vagon',
   html='<div class="ov center"><div class="h1 in tw" data-cue="cruce de lineas">Un nudo<br>ferroviario</div>'
        '<div class="h3 amber in" data-cue="casi cualquier rincon" style="margin-top:40px">Conectado por tren con toda Europa</div></div>')
sc("Para dirigirlo, Himmler elige a un oficial formado en Dachau, el primer campo de las SS, del que hablamos en el capítulo anterior: Rudolf Höss. En mayo de 1940 se convierte en el primer comandante de Auschwitz.",
   bg='dachau1',
   html='<div class="ov center"><div class="date in" data-t="0.2">Mayo de 1940</div><div class="h1 in" data-cue="rudolf hoss">Rudolf Höss</div>'
        '<div class="h3 dim in" data-cue="primer comandante" style="margin-top:30px">Primer comandante de Auschwitz</div></div>')
sc("El 14 de junio de 1940 llega el primer transporte: 728 presos políticos polacos, desde la cárcel de Tarnów. Reciben los números del 31 al 758. "
   "Los treinta primeros números se habían dado a delincuentes comunes alemanes, traídos para vigilar al resto.",
   img='sachs_polacos', kb='left', cap='Presos polacos llegando a un campo de concentración (Sachsenhausen)',
   html='<div class="ov right"><div class="date in" data-t="0.2">14 de junio de 1940</div><div class="big in" data-cue="728"><span data-count="728">0</span></div>'
        '<div class="h3 in" data-cue="728" data-d="0.4">presos polacos</div></div>', shade=True)
sc("Durante su primer año y medio, Auschwitz es eso: un campo de concentración sobre todo para polacos. Un lugar de terror, de hambre y de trabajo forzado. "
   "Todavía no es lo que llegará a ser.",
   img='puerta_ai', kb='up', fy=0.35, cap='Auschwitz I: la puerta del campo principal (fotografía de 1955)')

# ======================= AUSCHWITZ I =======================
sc("Sobre la puerta del campo principal, los presos tuvieron que forjar un lema de hierro: Arbeit macht frei. El trabajo os hará libres. "
   "Una de las mentiras más crueles del siglo veinte.",
   bg='puerta_ai',
   html='<div class="ov center"><div class="h1 in tw" data-cue="arbeit macht frei" style="font-family:TY;letter-spacing:6px">ARBEIT MACHT FREI</div>'
        '<div class="h3 dim in" data-cue="el trabajo os hara libres" style="margin-top:30px">«El trabajo os hará libres»</div>'
        '<div class="stamp in" data-cue="mentiras" style="margin-top:50px">Mentira</div></div>')
sc("Dentro hay una cuadrícula de bloques de ladrillo de dos pisos. Cada bloque está pensado para unos cientos de presos, pero a menudo se amontonan muchos más. "
   "Duermen en el suelo, sobre paja, o en literas de madera compartidas.",
   img='barracon', kb='in', cap='Literas de madera en un barracón de Auschwitz')
sc("El día empieza antes del amanecer. Después viene el recuento: todos los presos formados en la plaza, a veces durante horas, bajo la lluvia o la nieve. "
   "Si falta uno, nadie se mueve hasta que aparece. Vivo o muerto.",
   img='sachsenhausen', kb='left', cap='Recuento de presos en un campo de concentración nazi (Sachsenhausen)',
   html='<div class="ov right low"><div class="h2 in tw" data-cue="el recuento">El recuento</div><div class="h3 red in" data-cue="vivo o muerto">Vivo o muerto</div></div>', shade=True)
sc("Y en medio del campo, un edificio que todos temen: el bloque 11, la prisión dentro de la prisión. En sus sótanos hay celdas de castigo. "
   "Algunas son tan pequeñas que el preso tiene que pasar la noche de pie.",
   bg='letrinas',
   html='<div class="ov center"><div class="tag in" data-t="0.3">Auschwitz I</div><div class="h1 in tw" data-cue="el bloque 11">Bloque 11</div>'
        '<div class="h3 dim in" data-cue="la prision dentro" style="margin-top:30px">La prisión dentro de la prisión</div>'
        '<div class="h3 amber in" data-cue="de pie" style="margin-top:30px">Celdas en las que solo se podía estar de pie</div>'
        '<div class="h2 red in" data-cue="muro de la muerte" style="margin-top:50px">El muro de la muerte</div></div>')
sc("Junto a él, en el patio, está el llamado muro de la muerte. Allí las SS fusilaron a miles de presos, la mayoría polacos.",
   bg='torre',
   html='<div class="ov center"><div class="h2 in tw" data-cue="muro de la muerte">El muro<br>de la muerte</div>'
        '<div class="h3 dim in" data-cue="fusilaron a miles" style="margin-top:30px">Miles de fusilados, la mayoría polacos</div></div>')

# ======================= PILECKI =======================
sc("En septiembre de 1940 ocurre algo casi increíble. Un oficial de la resistencia polaca, Witold Pilecki, se deja detener a propósito en una redada en Varsovia. "
   "Quiere entrar en Auschwitz. Es, que se sepa, el único hombre que se presentó voluntario para ser preso allí.",
   bg='sachs_polacos',
   html='<div class="ov center"><div class="date in" data-t="0.2">19 de septiembre de 1940</div><div class="h1 in" data-cue="witold pilecki">Witold Pilecki</div>'
        '<div class="h3 amber in" data-cue="unico hombre" style="margin-top:30px">El hombre que entró en Auschwitz voluntario</div></div>')
sc("Dentro organiza una red clandestina, y a través de presos liberados y mensajeros hace llegar informes a la resistencia polaca, que los transmite a Londres. "
   "En abril de 1943 consigue escapar. Después de la guerra, el régimen comunista polaco lo detuvo, lo juzgó y lo ejecutó en 1948.",
   img='torre', side='left', kb='up',
   html='<div class="ov right"><div class="box in" data-cue="red clandestina"><div class="lab">1940-1943</div><div class="val" style="font-size:58px">Red clandestina</div></div>'
        '<div class="box in" data-cue="consigue escapar" style="margin-top:30px"><div class="lab">Abril de 1943</div><div class="val" style="font-size:58px">Fuga</div></div>'
        '<div class="box in" data-cue="lo ejecuto" style="margin-top:30px;border-color:var(--red)"><div class="lab">1948</div><div class="val red" style="font-size:58px">Ejecutado</div></div></div>')

# ======================= 1941: EL GIRO =======================
sc("En junio de 1941, Alemania invade la Unión Soviética. Y a Auschwitz empiezan a llegar prisioneros de guerra soviéticos, a los que los nazis tratan con una brutalidad especial.",
   bg='vagon',
   html='<div class="ov center"><div class="date in" data-t="0.2">22 de junio de 1941</div><div class="h2 in tw" data-cue="prisioneros de guerra sovieticos">Prisioneros<br>soviéticos</div></div>')
sc("A principios de septiembre de 1941, en los sótanos del bloque 11, las SS encierran a unos 600 prisioneros soviéticos y a unos 250 presos enfermos sacados del hospital del campo. "
   "Y usan contra ellos un pesticida que se empleaba para matar piojos: el Zyklon B.",
   bg='letrinas',
   html='<div class="ov center"><div class="date in" data-t="0.2">Septiembre de 1941 · Bloque 11</div>'
        '<div class="row" style="margin-top:20px"><div class="box in" data-cue="600"><div class="lab">Prisioneros soviéticos</div><div class="val">≈ 600</div></div>'
        '<div class="box in" data-cue="250"><div class="lab">Presos enfermos</div><div class="val">≈ 250</div></div></div>'
        '<div class="h1 red in tw" data-cue="zyklon b" style="margin-top:50px">Zyklon B</div></div>')
sc("Mueren todos. Para las SS, la prueba ha funcionado.",
   bg='birkenau',
   html='<div class="ov center"><div class="q in" data-cue="la prueba ha funcionado">«La prueba ha funcionado»</div>'
        '<div class="h3 dim in" data-cue="acaban de encontrar" style="margin-top:40px">Así empezó el exterminio con gas en Auschwitz</div></div>')

# ======================= BIRKENAU =======================
sc("En octubre de 1941 empiezan las obras de un segundo campo, a unos tres kilómetros del primero, junto a la aldea de Brzezinka. En alemán, Birkenau: el bosque de abedules.",
   img='birkenau', kb='left', cap='Auschwitz II-Birkenau: los barracones después de la guerra',
   html='<div class="ov right"><div class="date in" data-t="0.2">Octubre de 1941</div><div class="h1 in tw" data-cue="en aleman, birkenau">Birkenau</div>'
        '<div class="h3 dim in" data-cue="bosque de abedules">«El bosque de abedules»</div></div>', shade=True)
sc("Lo construyen los propios prisioneros, muchos de ellos soldados soviéticos. Trabajan con frío, sin ropa adecuada y casi sin comida. De los miles de soldados soviéticos que llegaron en el otoño de 1941, la gran mayoría había muerto en pocos meses.",
   img='buna_presos', kb='right', cap='Auschwitz, 1941: presos trabajando en una obra')
sc("El plan es enorme. Birkenau está pensado para ocupar unas 175 hectáreas, el tamaño de unos 250 campos de fútbol. En unas 140 se levantaron alrededor de 300 barracones y edificios. "
   "Fue, con diferencia, el mayor campo de todo el sistema nazi.",
   img='aereo', kb='in', fx=0.5, fy=0.5, cap='Auschwitz-Birkenau desde el aire: foto de reconocimiento de EE. UU., diciembre de 1944',
   html='<div class="ov left"><div class="big in" data-cue="175 hectareas" style="font-size:170px">175 ha</div>'
        '<div class="h3 in" data-cue="250 campos">≈ 250 campos de fútbol</div>'
        '<div class="h3 amber in" data-cue="300 barracones" style="margin-top:30px">≈ 300 barracones y edificios</div></div>', shade=True)
sc("Muchos barracones eran, en origen, cuadras de caballos prefabricadas. Estaban diseñadas para 52 caballos. Las SS metían en cada una a varios cientos de personas.",
   img='barracon', kb='left', cap='Interior de un barracón de Birkenau',
   html='<div class="ov right low"><div class="box in" data-cue="52 caballos"><div class="lab">Diseñadas para</div><div class="val">52 caballos</div></div>'
        '<div class="box in" data-cue="varios cientos" style="margin-top:24px;border-color:var(--red)"><div class="lab">Las SS metían</div><div class="val red">cientos de personas</div></div></div>')
sc("Sin agua corriente al principio, con letrinas colectivas de cemento y suelos de barro. El tifus, la disentería y el hambre mataban cada día a decenas de presos.",
   img='letrinas', kb='in', cap='Letrinas de un barracón de Birkenau (fotografía de 1955)')

# ======================= 1942: LA SOLUCIÓN FINAL =======================
sc("En enero de 1942, en la conferencia de Wannsee, los altos cargos nazis coordinan lo que llaman la solución final: el asesinato de todos los judíos de Europa. "
   "Y Auschwitz-Birkenau, con su red de ferrocarriles, se convierte en una pieza central.",
   bg='deportacion',
   html='<div class="ov center"><div class="date in" data-t="0.2">20 de enero de 1942 · Wannsee</div>'
        '<div class="h2 in tw" data-cue="solucion final">«La solución final»</div>'
        '<div class="h3 amber in" data-cue="pieza central" style="margin-top:40px">Auschwitz-Birkenau, pieza central</div></div>')
sc("En la primavera de 1942, las SS convierten dos casas de campesinos, a las afueras de Birkenau, en cámaras de gas. Los presos las llamaban la casita roja y la casita blanca. "
   "Los primeros transportes de judíos asesinados allí llegan de Alta Silesia, de Eslovaquia y de Francia.",
   bg='birkenau',
   html='<div class="ov center"><div class="date in" data-t="0.2">Primavera de 1942</div><div class="row" style="margin-top:30px">'
        '<div class="box in" data-cue="la casita roja" style="border-color:var(--red)"><div class="lab">Búnker 1</div><div class="val red" style="font-size:66px">«Casita roja»</div></div>'
        '<div class="box in" data-cue="la casita blanca"><div class="lab">Búnker 2</div><div class="val" style="font-size:66px">«Casita blanca»</div></div></div></div>')
sc("Pero para las SS eso no es suficiente. Entre marzo y junio de 1943 entran en funcionamiento cuatro grandes edificios que reúnen, bajo un mismo techo, vestuario, cámara de gas y hornos crematorios."
   "",
   img='aereo_lw', kb='in', fx=0.55, fy=0.45, cap='Auschwitz-Birkenau desde el aire (Luftwaffe, febrero de 1945)',
   html='<div class="ov left"><div class="date in" data-t="0.2">Marzo-junio de 1943</div><div class="h2 in tw" data-cue="cuatro grandes edificios">4 crematorios<br>con cámara de gas</div></div>', shade=True)
sc("Birkenau es ya, a la vez, un campo de prisioneros y una fábrica de muerte.",
   bg='aereo',
   html='<div class="ov center"><div class="row" style="gap:80px;align-items:stretch">'
        '<div class="box in" data-cue="campo de prisioneros" style="width:640px"><div class="lab">Campo de concentración</div><div class="txt" style="margin-top:14px">Trabajo forzado, hambre, enfermedades</div></div>'
        '<div class="box in" data-cue="fabrica de muerte" style="width:640px;border-color:var(--red)"><div class="lab">Centro de exterminio</div><div class="txt" style="margin-top:14px">Asesinato en masa nada más llegar</div></div></div></div>')

# ======================= LOS TRENES =======================
sc("Los trenes llegan desde toda Europa. Desde Francia y Bélgica. Desde los Países Bajos. Desde Grecia, Italia, Checoslovaquia, Yugoslavia, Noruega. Y desde los guetos de Polonia.",
   bg='vagon',
   html='<div class="ov center"><div class="h3 dim in" data-t="0" style="margin-bottom:40px">Trenes hacia Auschwitz desde…</div><div class="row" style="flex-wrap:wrap;justify-content:center;gap:28px 50px;max-width:1500px">'
        + ''.join(f'<div class="h2 in" data-cue="{c}">{n}</div>' for n, c in [('Francia', 'francia'), ('Bélgica', 'belgica'), ('Países Bajos', 'paises bajos'), ('Grecia', 'grecia'), ('Italia', 'italia'),
                                                                        ('Checoslovaquia', 'checoslovaquia'), ('Yugoslavia', 'yugoslavia'), ('Noruega', 'noruega'), ('Polonia', 'guetos de polonia')])
        + '</div></div>')
sc("El viaje dura días. Hasta cien personas en un vagón de mercancías cerrado, con un cubo como letrina y casi sin agua. Los más débiles mueren por el camino.",
   img='vagon', kb='in', cap='Presos en un vagón de mercancías cerrado con alambre de espino',
   html='<div class="ov right low"><div class="h2 in" data-cue="hasta cien personas">Hasta 100 personas<br>por vagón</div></div>', shade=True)
sc("Muchos creen que van a ser reasentados en el este para trabajar. Llevan maletas con su nombre escrito, sus mejores ropas, joyas cosidas en el forro de los abrigos. Nadie les ha dicho adónde van.",
   img='lodz_deport', kb='left', cap='Polonia, 1940: deportación de judíos en Lodz',
   html='<div class="ov left low"><div class="h3 in tw" data-cue="nadie les ha dicho">Nadie les ha dicho adónde van</div></div>', shade=True)

# ======================= LA SELECCIÓN =======================
sc("Al abrirse las puertas, todo es gritos, perros y golpes. Raus, raus. Fuera. Hombres a un lado, mujeres y niños al otro. Las familias se separan en segundos, muchas para siempre.",
   img='llegada_hungria', kb='in', fy=0.4, cap='Auschwitz-Birkenau, mayo de 1944: llegada de judíos de Hungría',
   html='<div class="ov right"><div class="h1 red in tw" data-cue="raus, raus">RAUS!</div><div class="h3 in" data-cue="fuera">«¡Fuera!»</div></div>', shade=True)
sc("Entonces llega la selección. Un médico de las SS mira a cada persona durante unos segundos y, con un gesto de la mano, decide. A un lado, el trabajo. Al otro, la muerte.",
   bg='llegada_hungria',
   html='<div class="ov center"><div class="h1 in tw" data-cue="la seleccion">La selección</div><div class="row" style="margin-top:50px;gap:100px">'
        '<div class="box in" data-cue="el trabajo"><div class="lab">Un lado</div><div class="val" style="font-size:70px">Trabajo</div></div>'
        '<div class="box in" data-cue="la muerte" style="border-color:var(--red)"><div class="lab">El otro</div><div class="val red" style="font-size:70px">Muerte</div></div></div></div>')
sc("Los niños pequeños, sus madres, los ancianos, los enfermos: casi todos van directamente a las cámaras de gas. Según el Museo de Auschwitz, de media solo uno de cada cinco recién llegados era elegido para trabajar.",
   bg='rampa_ninos',
   html='<div class="ov center"><div class="h3 dim in" data-t="0" style="margin-bottom:40px">De cada 5 deportados judíos, de media…</div><div class="row" style="gap:40px">'
        + ''.join(f'<div class="in" data-cue="{"uno de cada cinco" if k == 0 else "directamente"}" data-d="{0.15 * k}" style="width:150px;height:260px;border-radius:75px 75px 20px 20px;background:{"var(--paper)" if k == 0 else "var(--red)"};opacity:.9"></div>' for k in range(5))
        + '</div><div class="row" style="gap:120px;margin-top:40px"><div class="h3 in" data-cue="uno de cada cinco">1 a trabajar</div><div class="h3 red in" data-cue="uno de cada cinco" data-d="0.5">4 a la cámara de gas</div></div></div>')
sc("Las víctimas de la selección no saben lo que les espera. Les dicen que van a ducharse y a desinfectarse. Les piden que recuerden el número del gancho donde dejan su ropa, para recogerla después. "
   "Todo es parte del engaño, para evitar el pánico.",
   bg='birkenau',
   html='<div class="ov center"><div class="q in" data-cue="van a ducharse">«Vais a ducharos»</div>'
        '<div class="h3 dim in" data-cue="recuerden el numero" style="margin-top:40px">«Recordad el número de vuestro gancho»</div>'
        '<div class="stamp in" data-cue="el engano" style="margin-top:50px">Engaño</div></div>')
sc("Quienes eran elegidos para morir nunca quedaban registrados. No recibían número ni ficha. Por eso, durante décadas, fue tan difícil calcular cuántas personas murieron en Auschwitz.",
   img='rampa_ninos', kb='right', cap='Auschwitz-Birkenau, 1944: mujeres y niños en el andén',
   html='<div class="ov left low"><div class="h3 in tw" data-cue="nunca quedaban registrados">Sin número. Sin nombre. Sin ficha.</div></div>', shade=True)
sc("El trabajo más terrible lo hacían otros presos, casi todos judíos: el Sonderkommando, el comando especial. Los obligaban a vaciar las cámaras de gas y a quemar los cuerpos. "
   "Cada cierto tiempo, las SS los asesinaban también, para que no quedaran testigos.",
   bg='aereo_lw',
   html='<div class="ov center"><div class="h1 in tw" data-cue="el sonderkommando">Sonderkommando</div>'
        '<div class="h3 dim in" data-cue="comando especial" style="margin-top:30px">«Comando especial»</div>'
        '<div class="h3 red in" data-cue="no quedaran testigos" style="margin-top:40px">Asesinados también, para no dejar testigos</div></div>')
sc("Nada se desperdiciaba. Las maletas, la ropa, las gafas, los zapatos, hasta el pelo de las víctimas se clasificaba en unos almacenes enormes. "
   "Los presos los llamaban Canadá, porque para ellos Canadá era el país de la abundancia.",
   bg='budapest',
   html='<div class="ov center"><div class="h1 in tw" data-cue="los llamaban canada">«Canadá»</div>'
        '<div class="row" style="flex-wrap:wrap;justify-content:center;gap:20px 50px;margin-top:40px;max-width:1500px">'
        + ''.join(f'<div class="h3 dim in" data-cue="{c}">{n}</div>' for n, c in [('Maletas', 'las maletas'), ('Ropa', 'la ropa'), ('Gafas', 'las gafas'), ('Zapatos', 'los zapatos'), ('Pelo', 'el pelo')])
        + '</div></div>')

# ======================= LOS QUE ENTRABAN AL CAMPO =======================
sc("¿Y los que eran elegidos para trabajar? Para ellos empezaba otro infierno. Les quitaban todo: la ropa, el pelo, el nombre.",
   img='buna_canal', side='right', kb='up',
   html='<div class="ov left"><div class="h2 in tw" data-cue="otro infierno">Otro<br>infierno</div>'
        '<div class="h3 dim in" data-cue="la ropa" style="margin-top:30px">La ropa</div><div class="h3 dim in" data-cue="el pelo">El pelo</div><div class="h3 red in" data-cue="el nombre">El nombre</div></div>')
sc("En su lugar, un número. Y aquí hay un dato que pocos conocen: Auschwitz fue el único campo nazi donde ese número se tatuaba en la piel de forma sistemática, normalmente en el antebrazo izquierdo.",
   bg='letrinas',
   html='<div class="ov center"><div class="big mono in" data-cue="un numero" style="font-size:190px;letter-spacing:10px">A-15729</div>'
        '<div class="h3 amber in" data-cue="el unico campo" style="margin-top:30px">El único campo con tatuaje sistemático</div>'
        '<div class="txt dim in" data-cue="antebrazo izquierdo" style="font-size:32px;margin-top:20px">(número de ejemplo)</div></div>')
sc("Los números nunca se volvían a usar, aunque el preso muriera. Gracias a eso sabemos que se registró a algo más de 400.000 personas. "
   "Es decir: de cada tres deportados, dos ni siquiera llegaron a tener un número.",
   bg='barracon',
   html='<div class="ov center"><div class="h3 dim in" data-t="0">Presos registrados con número</div><div class="big in" data-cue="400.000"><span data-count="400000">0</span></div>'
        '<div class="h3 red in" data-cue="de cada tres" style="margin-top:30px">2 de cada 3 deportados nunca tuvieron número</div></div>')
sc("La vida en el campo era una carrera contra la muerte. Una sopa aguada al mediodía, un trozo de pan por la noche. Jornadas de once o doce horas.",
   img='buna_presos', kb='left', cap='Auschwitz: presos y obreros en la construcción de una carretera',
   html='<div class="ov right low"><div class="h3 in" data-cue="una sopa aguada">Sopa aguada</div><div class="h3 in" data-cue="un trozo de pan">Un trozo de pan</div>'
        '<div class="h3 red in" data-cue="once o doce horas">11-12 horas de trabajo</div></div>', shade=True)
sc("Muchos presos perdían tanto peso que se volvían esqueletos vivientes. En la jerga del campo los llamaban musulmanes. Y en cada selección dentro del campo, los más débiles eran enviados también a las cámaras de gas.",
   img='sachsenhausen', kb='in', fy=0.4, shade=True,
   html='<div class="ov center"><div class="h2 in tw" data-cue="esqueletos vivientes">Esqueletos<br>vivientes</div>'
        '<div class="h3 red in" data-cue="los mas debiles" style="margin-top:40px">Nuevas selecciones dentro del campo</div></div>')

# ======================= EL NEGOCIO =======================
sc("Porque Auschwitz también era un negocio. A unos siete kilómetros, la empresa química IG Farben construyó una gigantesca fábrica para producir caucho y combustible sintéticos. La llamaban Buna.",
   img='buna', kb='right', cap='Auschwitz, 1941: obras de la fábrica Buna de IG Farben',
   html='<div class="ov left"><div class="tag in" data-t="0.3">IG Farben</div><div class="h1 in tw" data-cue="la llamaban buna">Buna</div>'
        '<div class="h3 dim in" data-cue="caucho y combustible">Caucho y combustible sintéticos</div></div>', shade=True)
sc("Para alojar a los presos que trabajaban allí, en octubre de 1942 se abrió un tercer campo: Monowitz, también llamado Auschwitz tres. La empresa pagaba a las SS por cada preso que alquilaba.",
   img='buna_obra', side='right', kb='up',
   html='<div class="ov left"><div class="date in" data-t="0.2">Octubre de 1942</div><div class="h2 in" data-cue="monowitz">Monowitz</div>'
        '<div class="h3 dim in" data-cue="auschwitz tres">Auschwitz III</div><div class="h3 amber in" data-cue="la empresa pagaba" style="margin-top:30px">Presos alquilados a las SS</div></div>')
sc("Y alrededor fueron surgiendo decenas de campos más pequeños, junto a minas, fundiciones, granjas y fábricas. Entre cuarenta y cincuenta subcampos, según las fuentes. Auschwitz ya no era un campo. Era una red.",
   bg='aereo_zona',
   html='<div class="ov center"><div class="row" style="gap:60px;align-items:stretch">'
        '<div class="box in" data-t="0.3"><div class="lab">Auschwitz I</div><div class="val" style="font-size:52px">Campo principal</div></div>'
        '<div class="box in" data-t="0.6" style="border-color:var(--red)"><div class="lab">Auschwitz II</div><div class="val" style="font-size:52px">Birkenau</div></div>'
        '<div class="box in" data-t="0.9"><div class="lab">Auschwitz III</div><div class="val" style="font-size:52px">Monowitz</div></div></div>'
        '<div class="h2 amber in" data-cue="entre cuarenta y cincuenta" style="margin-top:60px">+ 40-50 subcampos</div></div>')
sc("Uno de los presos de Monowitz fue un joven químico italiano, judío, llamado Primo Levi. Llegó en febrero de 1944. Sobrevivió, en parte, porque lo pusieron a trabajar en un laboratorio. "
   "Años después escribiría uno de los libros más importantes sobre el Holocausto: Si esto es un hombre.",
   bg='buna',
   html='<div class="ov center"><div class="date in" data-t="0.2">Monowitz · febrero de 1944</div><div class="h1 in" data-cue="primo levi">Primo Levi</div>'
        '<div class="q in" data-cue="si esto es un hombre" style="margin-top:40px">«Si esto es un hombre»</div></div>')

# ======================= MENGELE =======================
sc("En mayo de 1943 llega a Birkenau un médico de las SS de 32 años: Josef Mengele. Participa en las selecciones del andén, a menudo con una tranquilidad que los supervivientes nunca olvidaron.",
   bg='rampa_ninos',
   html='<div class="ov center"><div class="date in" data-t="0.2">Mayo de 1943</div><div class="h1 in" data-cue="josef mengele">Josef Mengele</div>'
        '<div class="h3 dim in" data-cue="medico de las ss" style="margin-top:30px">Médico de las SS</div></div>')
sc("Mengele usaba a presos como cobayas humanas, sobre todo a gemelos, muchos de ellos niños. No fue el único médico que lo hizo.",
   bg='barracon',
   html='<div class="ov center"><div class="h2 in tw" data-cue="cobayas humanas">Cobayas<br>humanas</div>'
        '<div class="h3 amber in" data-cue="gemelos" style="margin-top:40px">Gemelos, muchos de ellos niños</div>'
        '<div class="stamp in" data-cue="nunca fue juzgado" style="margin-top:50px">Nunca juzgado</div></div>')
sc("Tras la guerra, Mengele huyó a Sudamérica. Nunca fue juzgado. Murió en Brasil en 1979, ahogado mientras se bañaba en el mar.",
   bg='aereo',
   html='<div class="ov center"><div class="h2 in" data-cue="huyo a sudamerica">Huyó a Sudamérica</div>'
        '<div class="stamp in" data-cue="nunca fue juzgado" style="margin-top:40px">Nunca juzgado</div>'
        '<div class="h3 dim in" data-cue="murio en brasil" style="margin-top:40px">Brasil, 1979</div></div>')

# ======================= GITANOS =======================
sc("Hay víctimas de Auschwitz que muchas veces se olvidan. En febrero de 1943 llegan a Birkenau los primeros transportes de gitanos, sinti y roma, desde Alemania y otros países. "
   "Los encierran en una sección propia, el llamado campo de familias gitano.",
   img='sinti_mujer', kb='in', cap='Colonia, 1937: campo forzoso para sinti y roma',
   html='<div class="ov right"><div class="date in" data-t="0.2">Febrero de 1943</div><div class="h2 in" data-cue="campo de familias gitano">El campo<br>de familias<br>gitano</div></div>', shade=True)
sc("Estos niños sinti vivían en un orfanato del sur de Alemania. Un equipo de supuestos científicos raciales los fotografió y los estudió. En 1944 fueron deportados a Auschwitz. Casi ninguno sobrevivió.",
   img='sinti_ninos', side='right', kb='in', fy=0.4,
   html='<div class="ov left"><div class="date in" data-t="0.2">Mulfingen · Alemania</div><div class="h2 in" data-cue="deportados a auschwitz">Deportados<br>en 1944</div>'
        '<div class="h3 red in" data-cue="casi ninguno" style="margin-top:30px">Casi ninguno sobrevivió</div></div>')
sc("De unos 23.000 gitanos deportados a Auschwitz, unos 21.000 murieron allí. En la noche del 2 al 3 de agosto de 1944, las SS liquidaron el campo gitano y asesinaron en las cámaras de gas a los miles que todavía quedaban vivos.",
   bg='sinti_mujer',
   html='<div class="ov center"><div class="row"><div class="box in" data-cue="23.000"><div class="lab">Gitanos deportados</div><div class="val">≈ 23.000</div></div>'
        '<div class="box in" data-cue="21.000" style="border-color:var(--red)"><div class="lab">Murieron</div><div class="val red">≈ 21.000</div></div></div>'
        '<div class="date in" data-cue="2 al 3 de agosto" style="margin-top:50px">2-3 de agosto de 1944</div></div>')

# ======================= HUNGRÍA 1944 =======================
sc("1944. La guerra ya está perdida para Alemania, pero la maquinaria de Auschwitz funciona más rápido que nunca. En marzo, Alemania ocupa Hungría, que hasta entonces era su aliada.",
   img='budapest', kb='right', cap='Budapest, octubre de 1944: soldados detienen a judíos',
   html='<div class="ov left"><div class="date in" data-t="0.2">Marzo de 1944</div><div class="h2 in tw" data-cue="alemania ocupa hungria">Alemania<br>ocupa Hungría</div></div>', shade=True)
sc("Para prepararse, las SS prolongan la vía del tren hasta el interior de Birkenau, casi hasta la puerta de las cámaras de gas. Y Rudolf Höss vuelve a Auschwitz para dirigir la operación.",
   img='puerta_birkenau', kb='in', fy=0.45, cap='La puerta de Birkenau y la vía que entraba en el campo (1945)',
   html='<div class="ov left"><div class="h2 in tw" data-cue="hasta el interior de birkenau">La vía<br>entra en<br>el campo</div></div>', shade=True)
sc("Entre el 15 de mayo y el 9 de julio de 1944, la policía húngara, guiada por las SS, deporta a unos 440.000 judíos de Hungría. Casi todos van a Auschwitz. "
   "La gran mayoría muere en las cámaras de gas nada más llegar.",
   bg='llegada_hungria',
   html='<div class="ov center"><div class="date in" data-t="0.2">15 de mayo - 9 de julio de 1944</div><div class="big in" data-cue="440.000"><span data-count="440000">0</span></div>'
        '<div class="h3 in" data-cue="440.000" data-d="0.3">judíos deportados desde Hungría</div>'
        '<div class="h3 red in" data-cue="la gran mayoria" style="margin-top:30px">En menos de 8 semanas</div></div>')
sc("Esta fotografía es de esos días. Es parte del llamado Álbum de Auschwitz, tomado por las propias SS. Mujeres y niños recién bajados del tren, esperando en el andén. No sabían que estaban a unos cientos de metros del final.",
   img='llegada_hungria', kb='in', fy=0.35, cap='Álbum de Auschwitz, mayo de 1944: judíos de Hungría en el andén de Birkenau')
sc("Y del gueto de Lodz, en Polonia, llegan en el verano de 1944 decenas de miles de judíos más. Personas como este anciano, fotografiado en el gueto años antes, con la estrella amarilla en el pecho.",
   img='lodz_anciano', side='right', kb='in', fy=0.3,
   html='<div class="ov left"><div class="date in" data-t="0.2">Gueto de Lodz</div><div class="h2 in" data-cue="decenas de miles">Verano<br>de 1944</div>'
        '<div class="h3 dim in" data-cue="la estrella amarilla" style="margin-top:30px">La estrella amarilla</div></div>')
sc("A principios de septiembre de 1944, otro tren llega desde los Países Bajos con más de mil judíos. Entre ellos, una chica de 15 años y su familia. Se llamaba Ana Frank. "
   "Sobrevivió a Auschwitz, pero murió meses después en otro campo, Bergen-Belsen.",
   bg='vagon',
   html='<div class="ov center"><div class="date in" data-t="0.2">Septiembre de 1944</div><div class="h1 in" data-cue="se llamaba ana frank">Ana Frank</div>'
        '<div class="h3 dim in" data-cue="bergen-belsen" style="margin-top:30px">Auschwitz · Bergen-Belsen</div></div>')

# ======================= RESISTENCIA =======================
sc("Pero Auschwitz no fue solo un lugar de víctimas. También fue un lugar de resistencia. En abril de 1944, dos presos judíos eslovacos, Rudolf Vrba y Alfred Wetzler, se esconden durante tres días en una pila de madera dentro del recinto.",
   img='torre', side='left', kb='up',
   html='<div class="ov right"><div class="date in" data-t="0.2">Abril de 1944</div><div class="h2 in" data-cue="rudolf vrba">Rudolf Vrba</div><div class="h2 in" data-cue="alfred wetzler">Alfred Wetzler</div>'
        '<div class="h3 amber in" data-cue="tres dias" style="margin-top:30px">3 días escondidos</div></div>')
sc("Cuando las SS dejan de buscarlos, escapan y llegan a Eslovaquia. Allí dictan un informe detallado: cómo funciona el campo, los trenes, las cámaras de gas. Ese informe llegó a los aliados y a la prensa internacional, "
   "y aumentó la presión que, en julio de 1944, llevó a detener las deportaciones desde Hungría.",
   bg='aereo_zona',
   html='<div class="ov center"><div class="h2 in tw" data-cue="un informe detallado">El informe<br>Vrba-Wetzler</div>'
        '<div class="h3 amber in" data-cue="detener las deportaciones" style="margin-top:40px">Ayudó a frenar las deportaciones de Hungría</div></div>')
sc("Y el 7 de octubre de 1944, los presos del Sonderkommando se rebelan. Con martillos, hachas y explosivos que unas presas judías habían sacado a escondidas de una fábrica, prenden fuego al crematorio cuatro.",
   bg='aereo_lw',
   html='<div class="ov center"><div class="date in" data-t="0.2">7 de octubre de 1944</div><div class="h1 in tw" data-cue="se rebelan">La revuelta</div>'
        '<div class="h3 red in" data-cue="crematorio cuatro" style="margin-top:30px">Arde el crematorio IV</div></div>')
sc("La revuelta fue aplastada. Más de 400 presos murieron. Cuatro de las mujeres que habían pasado la pólvora fueron ahorcadas en enero de 1945, pocas semanas antes de la liberación. Pero habían demostrado algo: incluso allí, se podía luchar.",
   bg='torre',
   html='<div class="ov center"><div class="h3 red in" data-cue="mas de 400">Más de 400 presos muertos</div>'
        '<div class="h3 dim in" data-cue="cuatro de las mujeres" style="margin-top:30px">4 mujeres ahorcadas en enero de 1945</div>'
        '<div class="q in" data-cue="se podia luchar" style="margin-top:50px">Incluso allí, se podía luchar.</div></div>')

# ======================= EL FINAL =======================
sc("En noviembre de 1944, con el ejército soviético cada vez más cerca, Himmler ordena parar los gaseamientos. Las SS empiezan a desmontar y volar los crematorios y a quemar documentos. Quieren borrar las pruebas.",
   img='aereo', kb='out', cap='Birkenau desde el aire, 21 de diciembre de 1944',
   html='<div class="ov left"><div class="date in" data-t="0.2">Noviembre de 1944</div><div class="h2 in tw" data-t="0.6">Borrar<br>las pruebas</div></div>', shade=True)
sc("Entre el 17 y el 21 de enero de 1945, las SS sacan a pie a unos 56.000 presos de Auschwitz y sus subcampos, en pleno invierno, hacia el oeste. Son las marchas de la muerte. "
   "Quien se queda atrás, es fusilado. Murieron al menos 9.000, y probablemente hasta 15.000.",
   bg='torre',
   html='<div class="ov center"><div class="date in" data-t="0.2">17-21 de enero de 1945</div><div class="h2 in tw" data-cue="marchas de la muerte">Las marchas<br>de la muerte</div>'
        '<div class="row" style="margin-top:40px"><div class="box in" data-cue="56.000"><div class="lab">Evacuados a pie</div><div class="val">≈ 56.000</div></div>'
        '<div class="box in" data-cue="al menos 9.000" style="border-color:var(--red)"><div class="lab">Muertos</div><div class="val red">9.000-15.000</div></div></div></div>')
sc("El 27 de enero de 1945, soldados soviéticos entran en Auschwitz. Encuentran a unos 7.000 presos, la mayoría enfermos y agotados, demasiado débiles para caminar. Entre ellos, niños. Y Primo Levi.",
   img='puerta_birkenau', kb='out', cap='Birkenau tras la liberación, 1945',
   html='<div class="ov left"><div class="date in" data-t="0.2">27 de enero de 1945</div><div class="h2 in tw" data-t="0.6">La liberación</div>'
        '<div class="h3 in" data-cue="unos 7.000" style="margin-top:20px">≈ 7.000 supervivientes en el campo</div></div>', shade=True)
sc("En los almacenes que las SS no llegaron a quemar, los soldados encuentran cientos de miles de prendas de ropa de hombre y de mujer, y toneladas de pelo humano. Las pruebas que querían borrar seguían allí.",
   img='birkenau', kb='right', shade=True,
   html='<div class="ov center"><div class="h2 in tw" data-cue="las pruebas que querian borrar">Las pruebas<br>seguían allí</div></div>')

# ======================= LAS CIFRAS =======================
sc("Hagamos balance. Según las investigaciones del Museo de Auschwitz, fueron deportadas allí al menos un millón trescientas mil personas. Al menos un millón cien mil fueron asesinadas o murieron en el campo. Una de cada seis víctimas judías del Holocausto murió allí.",
   bg='birkenau',
   html='<div class="ov center"><div class="row" style="gap:80px"><div class="box in" data-cue="un millon trescientas mil"><div class="lab">Deportadas</div><div class="val">1.300.000</div></div>'
        '<div class="box in" data-cue="un millon cien mil" style="border-color:var(--red)"><div class="lab">Asesinadas o muertas</div><div class="val red">1.100.000</div></div></div>'
        '<div class="h3 amber in" data-cue="una de cada seis" style="margin-top:50px">1 de cada 6 víctimas judías del Holocausto</div></div>')
sc("¿Quiénes eran? Alrededor de un millón eran judíos. Entre 70.000 y 75.000, polacos. Unos 21.000, gitanos. Unos 15.000, prisioneros de guerra soviéticos. Y entre 10.000 y 15.000 personas de otros países y grupos.",
   bg='aereo_zona',
   html=bars([('Judíos', 1000000, '≈ 1.000.000', 'un millon eran judios', 'var(--red)'), ('Polacos', 72500, '70-75.000', 'polacos', 'var(--amber)'),
              ('Gitanos', 21000, '≈ 21.000', 'gitanos', 'var(--amber)'), ('Soviéticos', 15000, '≈ 15.000', 'prisioneros de guerra sovieticos', 'var(--amber)'),
              ('Otros', 12500, '10-15.000', 'otros paises', 'var(--dim)')], 'Víctimas de Auschwitz (estimaciones)', 1000000))
sc("Durante décadas circularon cifras mucho más altas, de hasta cuatro millones, que venían de la propaganda soviética. El cálculo actual, más bajo pero basado en documentos de los trenes, es el que aceptan hoy los historiadores. Y sigue siendo inabarcable.",
   bg='memorial70',
   html='<div class="ov center"><div class="row" style="gap:80px;align-items:center"><div class="box in" data-cue="cuatro millones"><div class="lab">Cifra soviética</div><div class="val dim" style="text-decoration:line-through">4.000.000</div></div>'
        '<div class="box in" data-cue="el calculo actual" style="border-color:var(--red)"><div class="lab">Estimación actual</div><div class="val red">1.100.000</div></div></div>'
        '<div class="h3 amber in" data-cue="sigue siendo inabarcable" style="margin-top:50px">Inabarcable</div></div>')

# ======================= DESPUÉS =======================
sc("¿Y Rudolf Höss? Huyó con un nombre falso y trabajó como peón en una granja del norte de Alemania. En marzo de 1946, los británicos lo encontraron.",
   bg='dachau1',
   html='<div class="ov center"><div class="h1 in" data-cue="rudolf hoss">Rudolf Höss</div><div class="h3 dim in" data-cue="nombre falso" style="margin-top:30px">Escondido con un nombre falso</div>'
        '<div class="date in" data-cue="marzo de 1946" style="margin-top:40px">Detenido en marzo de 1946</div>'
        '<div class="h2 red in tw" data-cue="lo ahorcaron" style="margin-top:40px">Ahorcado en Auschwitz · 1947</div></div>')
sc("Declaró como testigo en Núremberg y fue juzgado en Polonia. El 16 de abril de 1947 lo ahorcaron en Auschwitz, junto a la primera cámara de gas del campo que él mismo había dirigido.",
   img='puerta_ai', kb='in', fy=0.4, shade=True,
   html='<div class="ov center"><div class="date in" data-t="0.2">16 de abril de 1947</div><div class="h2 in tw" data-cue="lo ahorcaron en auschwitz">Ahorcado<br>en Auschwitz</div></div>')
sc("Ese mismo año, en 1947, el Parlamento polaco convirtió los restos de Auschwitz y Birkenau en un museo y memorial. En 1979, la UNESCO lo declaró Patrimonio de la Humanidad.",
   img='memorial70', kb='right', cap='Birkenau, 1970: visita oficial al monumento a las víctimas',
   html='<div class="ov right"><div class="box in" data-cue="en 1947"><div class="lab">1947</div><div class="val" style="font-size:60px">Museo y memorial</div></div>'
        '<div class="box in" data-cue="en 1979" style="margin-top:30px"><div class="lab">1979</div><div class="val" style="font-size:60px">Patrimonio UNESCO</div></div>'
        '<div class="box in" data-cue="en 2024" style="margin-top:30px"><div class="lab">Visitantes en 2024</div><div class="val" style="font-size:60px">1.830.000</div></div></div>', shade=True)
sc("En 2024 lo visitaron más de un millón ochocientas mil personas. Caminan por los mismos andenes, entre las mismas alambradas, en silencio.",
   img='torre', side='left', kb='up',
   html='<div class="ov right"><div class="h3 dim in" data-t="0.2">Visitantes en 2024</div><div class="big in" data-cue="un millon ochocientas mil" style="font-size:160px"><span data-count="1830000">0</span></div></div>')

# ======================= CIERRE =======================
sc("Auschwitz no lo construyeron monstruos de otro planeta. Lo diseñaron arquitectos, lo planificaron funcionarios, lo pagaron empresas y lo hicieron funcionar miles de personas normales que cada noche volvían a casa a cenar.",
   bg='birkenau',
   html='<div class="ov center"><div class="h3 in" data-cue="lo disenaron arquitectos">Arquitectos</div><div class="h3 in" data-cue="lo planificaron funcionarios">Funcionarios</div>'
        '<div class="h3 in" data-cue="lo pagaron empresas">Empresas</div><div class="h2 red in" data-cue="personas normales" style="margin-top:30px">Personas normales</div></div>')
sc("Por eso el 27 de enero, el día de su liberación, es hoy el Día Internacional en Memoria de las Víctimas del Holocausto. Para recordar a cada una de ellas. Y para recordar de lo que somos capaces.",
   img='puerta_birkenau', kb='out', shade=True,
   html='<div class="ov center"><div class="date in" data-cue="27 de enero">27 de enero</div>'
        '<div class="h3 in" data-cue="dia internacional" style="max-width:1300px">Día Internacional en Memoria de las Víctimas del Holocausto</div>'
        '<div class="q in" data-cue="de lo que somos capaces" style="margin-top:50px">Para recordar de lo que somos capaces.</div></div>')
sc("En el próximo capítulo viajaremos unos años atrás, a la noche del 9 de noviembre de 1938, cuando ardieron las sinagogas de Alemania y el odio salió a la calle a la vista de todos. "
   "Si no quieres perdértelo, suscríbete. Y cuéntame en los comentarios: ¿has visitado Auschwitz?",
   bg='birkenau',
   html='<div class="ov center"><div class="tag in" data-t="0.2">Próximo capítulo</div><div class="h2 in tw" data-t="0.4">La Noche de los<br>cristales rotos</div>'
        '<div class="rule in" data-t="0.6"></div><div class="h3 dim in" data-cue="suscribete">Suscríbete para no perdértelo</div>'
        '<div class="who in" data-cue="suscribete" data-d="1.5" style="font-size:24px;margin-top:80px">Fuentes: Memorial y Museo de Auschwitz-Birkenau, USHMM, Britannica. '
        'Imágenes: Bundesarchiv (créditos en la descripción). Cifras de víctimas: estimaciones de F. Piper (Museo de Auschwitz).</div></div>')

MERGE = {12: 'keep', 17: 'keep', 22: 'keep', 26: 'next', 28: 'keep', 31: 'next', 38: 'next', 41: 'keep', 48: 'keep', 70: 'keep', 72: 'keep'}
TENSION = {0, 13, 14, 15, 25, 26, 27, 28, 29, 30, 31, 47, 48, 49, 50, 51, 52, 53}
MELAN = {32, 37, 40, 41, 42, 43, 44, 45, 46, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65}
for i, s_ in enumerate(S): s_['mood'] = 'tension' if i in TENSION else 'melancolia' if i in MELAN else 'inquietud'
# escenas cortas fusionadas con la anterior (50-65 escenas de 15-25 s): 'keep' = imagen de la primera, 'next' = de la segunda
for i in sorted(MERGE, reverse=True):
    a, b = S[i - 1], S.pop(i)
    if MERGE[i] == 'next':
        for k in ('img', 'bg', 'html', 'cap', 'side', 'kb', 'fx', 'fy', 'shade'): a.pop(k, None)
        a.update({k: v for k, v in b.items() if k not in ('say', 'mood')})
    a['say'] = a['say'] + ' ' + b['say']

spec = dict(title='Auschwitz por dentro', brand='Sombras del 39', voice='hyKxCTlAqtnW188CgltM', model='eleven_v4',
            voice_settings=dict(stability=0.5, similarity_boost=0.75), tail=4, scenes=S,
            thumb={'img': 'img/lib_ninos.jpg', 'fy': 0.35, 'l1': 'Auschwitz', 'l2': 'por dentro', 'l2size': 118})
json.dump(spec, open(os.path.join(here, 'spec.json'), 'w'), ensure_ascii=False, indent=1)
txt = ' '.join(s['say'] for s in S)
print(len(S), 'escenas ·', len(txt), 'caracteres · ~%.1f min' % (len(txt) / 13.8 / 60), '· sin foto:', [i for i, s in enumerate(S) if 'img' not in s and 'bg' not in s])
open(os.path.join(here, 'guion.txt'), 'w').write('\n\n'.join(s['say'] for s in S) + '\n')
