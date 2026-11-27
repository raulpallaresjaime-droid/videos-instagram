# Genera spec.json del episodio 8 (mini documental 15-20 min). Uso: python3 build_spec.py
import json, os
here = os.path.dirname(os.path.abspath(__file__))
has = lambda n: os.path.exists(os.path.join(here, 'img', n + '.jpg'))

S = []
def sc(say, mood='inquietud', **kw):
    if 'img' in kw and not has(kw['img']):
        fb = kw.pop('fallback', 'vormarsch_panzer'); fb = fb if has(fb) else 'vormarsch_panzer'
        kw.pop('img'); kw.pop('side', None); kw.pop('kb', None); kw.pop('cap', None)
        kw['bg'] = f'img/{fb}.jpg'
    elif 'img' in kw:
        kw['img'] = f"img/{kw['img']}.jpg"; kw.pop('fallback', None)
    if 'bg' in kw and not kw['bg'].startswith('img/'):
        b = kw['bg'] if has(kw['bg']) else kw.pop('fallback', 'vormarsch_panzer')
        b = b if has(b) else 'vormarsch_panzer'
        kw['bg'] = f"img/{b}.jpg"
    kw.pop('fallback', None)
    S.append(dict(say=say, mood=mood, **kw))

def timeline(items, title=None):
    ev = ''.join(f'<div class="e in" data-cue="{c}"><div class="d">{d}</div><div class="t">{t}</div></div>' for d, t, c in items)
    head = f'<div class="h3 dim in" data-t="0" style="margin-bottom:80px">{title}</div>' if title else ''
    return f'<div class="ov center">{head}<div class="tl">{ev}</div></div>'

T, I, M = 'tension', 'inquietud', 'melancolia'

# ======================= GANCHO =======================
sc("Son las tres y cuarto de la madrugada del 22 de junio de 1941. A lo largo de casi 3.000 kilómetros de frontera, del mar Báltico al mar Negro, miles de cañones alemanes abren fuego a la vez. "
   "Más de 3 millones de soldados cruzan la frontera de la Unión Soviética. Es la mayor invasión terrestre de la historia.", T,
   img='vormarsch_panzer', kb='in', shade=True,
   html='<div class="ov center"><div class="date in" data-t="0">22 de junio de 1941</div><div class="big in" data-t="0.4" style="font-size:200px">3:15</div>'
        '<div class="h3 in" data-cue="casi 3.000 kilometros">≈ 3.000 km de frente</div><div class="h2 red in" data-cue="mas de 3 millones" style="margin-top:30px">+3 millones de soldados</div></div>')
sc("Hitler estaba convencido de que la Unión Soviética se derrumbaría en pocas semanas. Seis meses después, su ejército estaba congelándose a las puertas de Moscú. Esta es la historia de la Operación Barbarroja. Y de por qué fue, probablemente, el mayor error de Hitler.", M,
   img='schnee_moskau', kb='in', shade=True,
   html='<div class="ov center"><div class="tag in" data-t="0.4">Capítulo 8</div>'
        '<div class="h1 in" data-cue="operacion barbarroja">Operación<br>Barbarroja</div>'
        '<div class="date in" data-cue="el mayor error de hitler" style="margin-top:30px">El mayor error de Hitler</div></div>')

# ======================= EL SUEÑO DEL ESTE =======================
sc("Para entenderlo hay que volver a los años veinte. En Mi lucha, el libro que escribió en la cárcel, Hitler ya decía que el futuro de Alemania estaba en el este. Que los alemanes necesitaban espacio vital, y que ese espacio estaba en Rusia.", I,
   img='hitler', kb='in', side='right',
   html='<div class="ov left"><div class="h3 dim in" data-cue="mi lucha">Mi lucha, 1925</div><div class="h1 in tw" data-cue="espacio vital">«Espacio<br>vital»</div>'
        '<div class="h3 red in" data-cue="estaba en rusia" style="margin-top:30px">En el este</div></div>')
sc("En su ideología, los pueblos eslavos eran inferiores y el comunismo soviético era una conspiración judía. La guerra contra la Unión Soviética no iba a ser una guerra normal. Iba a ser una guerra de exterminio.", T,
   bg='hitler_polonia',
   html='<div class="ov center"><div class="h3 in" data-cue="eran inferiores">Racismo</div><div class="h3 in" data-cue="conspiracion judia">Antisemitismo</div>'
        '<div class="h1 red in tw" data-cue="una guerra de exterminio" style="margin-top:30px">Guerra de<br>exterminio</div></div>')
sc("Por eso sorprendió tanto lo de agosto de 1939. Hitler y Stalin, enemigos a muerte, firmaron un pacto de no agresión y se repartieron Polonia. Durante casi dos años, la Unión Soviética envió a Alemania petróleo, cereales y materias primas.", I,
   img='pacto', kb='in', fy=0.35, cap='Moscú, agosto de 1939: Mólotov, Stalin y Ribbentrop',
   html='<div class="ov left"><div class="date in" data-t="0.2">Agosto de 1939</div><div class="h2 in tw" data-cue="pacto de no agresion">El pacto</div>'
        '<div class="h3 in" data-cue="petroleo" style="margin-top:30px">Petróleo · cereales · materias primas</div></div>', shade=True)
sc("Pero para Hitler aquel pacto siempre fue temporal. En el verano de 1940, con Francia derrotada, ordenó a sus generales preparar el ataque. Y el 18 de diciembre firmó la directiva número 21. Su nombre en clave: Barbarroja.", T,
   img='lagebesprechung', kb='in', cap='Hitler con sus generales, 1941',
   html='<div class="ov left"><div class="date in" data-cue="el 18 de diciembre">18 de diciembre de 1940</div><div class="h2 in tw" data-cue="la directiva numero 21">Directiva n.º 21</div>'
        '<div class="h1 red in" data-cue="barbarroja" style="margin-top:20px">Barbarroja</div></div>', shade=True)
sc("Barbarroja era el apodo del emperador Federico Primero, que según la leyenda duerme bajo una montaña y despertará para salvar a Alemania. La directiva lo decía sin rodeos: las fuerzas armadas debían aplastar a la Rusia soviética en una campaña rápida.", I,
   bg='lagebesprechung',
   html='<div class="ov center"><div class="h3 dim in" data-cue="federico primero">Federico I «Barbarroja»</div>'
        '<div class="q in" data-cue="aplastar a la rusia sovietica" style="margin-top:30px">«Aplastar a la Rusia soviética<br>en una campaña rápida»</div><div class="who in" data-cue="campana rapida">Directiva n.º 21</div></div>')
sc("¿Por qué tanta confianza? En 1940, la Wehrmacht había derrotado a Francia en seis semanas. Y en el invierno de 1939, el Ejército Rojo había hecho el ridículo contra la pequeña Finlandia. Además, Stalin había fusilado o encarcelado a miles de sus propios oficiales en las purgas.", I,
   img='hitler_paris', kb='in', side='right', cap='Hitler en París, junio de 1940',
   html='<div class="ov left"><div class="h3 in" data-cue="seis semanas">Francia, en 6 semanas</div><div class="h3 in" data-cue="finlandia">El fiasco soviético en Finlandia</div>'
        '<div class="h3 red in" data-cue="las purgas">Las purgas de Stalin</div></div>')
sc("Hitler resumió su idea con una frase que se le atribuye: basta con dar una patada a la puerta y toda la estructura podrida se vendrá abajo. Sus generales calculaban que la campaña duraría unas pocas semanas. Casi nadie pensó en ropa de invierno.", T,
   img='hitler', kb='out', side='right',
   html='<div class="ov left"><div class="q in" data-cue="una patada a la puerta">«Una patada a la puerta<br>y todo se vendrá abajo»</div>'
        '<div class="h3 red in" data-cue="ropa de invierno" style="margin-top:40px">¿Ropa de invierno? No.</div></div>')
sc("Y había otro plan, mucho más siniestro. En mayo de 1941, altos funcionarios nazis acordaron que el ejército se alimentaría con la comida de los territorios ocupados. Sabían lo que significaba. En sus propias actas escribieron que decenas de millones de personas morirían de hambre.", M,
   bg='dorf_brennt',
   html='<div class="ov center"><div class="date in" data-t="0.2">Mayo de 1941</div><div class="h1 in tw" data-cue="mucho mas siniestro">El plan del hambre</div>'
        '<div class="h3 red in" data-cue="decenas de millones" style="margin-top:30px">«Decenas de millones» morirían de hambre</div></div>')
sc("Y en junio, el alto mando alemán dio otra orden: los comisarios políticos del Ejército Rojo capturados debían ser fusilados en el acto. Era la primera vez que un ejército moderno planeaba por escrito violar las leyes de la guerra a esa escala.", T,
   bg='lagebesprechung',
   html='<div class="ov center"><div class="date in" data-t="0.2">6 de junio de 1941</div><div class="stamp in" data-cue="los comisarios politicos">Orden de los comisarios</div>'
        '<div class="h3 in" data-cue="fusilados en el acto" style="margin-top:30px">Fusilarlos en el acto</div></div>')

# ======================= STALIN NO QUIERE CREERLO =======================
sc("Lo más asombroso es que Stalin fue avisado. Muchas veces. Los británicos le advirtieron. Su espía en Tokio, Richard Sorge, le envió información sobre el ataque. Y sus propios servicios de inteligencia detectaron cómo se acumulaban tropas alemanas en la frontera.", I,
   img='stalin', kb='in', side='right', fallback='pacto',
   html='<div class="ov left"><div class="h2 in tw" data-cue="stalin fue avisado">Stalin fue<br>avisado</div><div class="h3 in" data-cue="los britanicos">Londres</div>'
        '<div class="h3 in" data-cue="richard sorge">Richard Sorge, desde Tokio</div><div class="h3 in" data-cue="servicios de inteligencia">Su propio espionaje</div></div>')
sc("Pero Stalin no quiso creerlo. Pensaba que eran provocaciones británicas para arrastrarle a la guerra. Prohibió cualquier movimiento que los alemanes pudieran interpretar como una provocación. La víspera del ataque, un soldado alemán desertó y cruzó la frontera para avisar. Tampoco sirvió de nada.", T,
   bg='bug_stug',
   html='<div class="ov center"><div class="h2 in tw" data-cue="no quiso creerlo">No quiso creerlo</div>'
        '<div class="h3 in" data-cue="provocaciones britanicas" style="margin-top:30px">«Provocaciones británicas»</div><div class="h3 red in" data-cue="un soldado aleman deserto">21 de junio: un desertor avisa</div></div>')
sc("Mientras tanto, al otro lado, se preparaba el mayor ejército de la historia. Junto con sus aliados, Finlandia, Rumanía, Hungría, Italia y Eslovaquia, el Eje reunió cerca de 3,7 millones de soldados, más de 3.000 tanques y unos 2.500 aviones.", T,
   img='bug_stug', kb='up', cap='Junto al río Bug, junio de 1941: cañón de asalto alemán',
   html='<div class="ov right"><div class="row" style="gap:30px;flex-direction:column;align-items:flex-end">'
        '<div class="box in" data-cue="3,7 millones"><div class="lab">Soldados</div><div class="val">≈ 3,7 M</div></div>'
        '<div class="box in" data-cue="mas de 3.000 tanques"><div class="lab">Tanques</div><div class="val">+3.000</div></div>'
        '<div class="box in" data-cue="2.500 aviones"><div class="lab">Aviones</div><div class="val">≈ 2.500</div></div></div></div>', shade=True)
sc("Se dividió en tres grandes grupos de ejércitos. El del norte iría hacia Leningrado. El del centro, hacia Moscú. Y el del sur, hacia Ucrania, con su trigo, y más allá, el petróleo del Cáucaso.", I,
   bg='panzer3',
   html=timeline([('Norte', 'Leningrado', 'hacia leningrado'), ('Centro', 'Moscú', 'hacia moscu'), ('Sur', 'Ucrania y el Cáucaso', 'hacia ucrania')], 'Tres grupos de ejércitos'))

# ======================= 22 DE JUNIO =======================
sc("El ataque empezó casi el mismo día en que Napoleón había invadido Rusia, 129 años antes. En las primeras horas, la aviación alemana atacó los aeródromos soviéticos. Los aviones estaban alineados en tierra, sin camuflar. Según las cifras más citadas, unos 1.200 aviones soviéticos fueron destruidos solo el primer día.", T,
   img='dnjestr_fuego', kb='in', cap='Unión Soviética, verano de 1941',
   html='<div class="ov right"><div class="h3 dim in" data-cue="napoleon">Napoleón: junio de 1812</div><div class="big red in" data-cue="unos 1.200" style="font-size:150px">≈ 1.200</div>'
        '<div class="h3 in" data-cue="unos 1.200" data-d="0.4">aviones soviéticos destruidos el primer día</div></div>', shade=True)
sc("En Moscú, nadie sabía qué hacer. Stalin no habló a su pueblo. Fue su ministro de Exteriores, Viacheslav Mólotov, quien anunció la invasión por la radio a mediodía. Terminó con una frase que se repetiría durante toda la guerra: nuestra causa es justa. El enemigo será derrotado. La victoria será nuestra.", I,
   bg='pacto',
   html='<div class="ov center"><div class="date in" data-t="0.2">22 de junio · mediodía · Radio Moscú</div>'
        '<div class="q in" data-cue="nuestra causa es justa" style="margin-top:30px">«Nuestra causa es justa.<br>El enemigo será derrotado.<br>La victoria será nuestra.»</div><div class="who in" data-cue="la victoria sera nuestra">Viacheslav Mólotov</div></div>')
sc("Stalin no se dirigió a los soviéticos hasta el 3 de julio, once días después. Empezó de una forma que nadie esperaba de él: camaradas, ciudadanos, hermanos y hermanas. Pidió que, si había que retirarse, no se dejara al enemigo ni un kilo de grano, ni una locomotora. Tierra quemada.", I,
   img='stalin', kb='out', side='right', fallback='pacto',
   html='<div class="ov left"><div class="date in" data-t="0.2">3 de julio de 1941</div><div class="q in" data-cue="hermanos y hermanas">«Hermanos<br>y hermanas»</div>'
        '<div class="h2 red in" data-cue="tierra quemada" style="margin-top:30px">Tierra quemada</div></div>')

# ======================= LA GRAN OLA =======================
sc("Los primeros días fueron un desastre total para el Ejército Rojo. Las divisiones blindadas alemanas avanzaban a toda velocidad, se metían por detrás de las líneas soviéticas y cerraban enormes cercos, mientras la infantería, a pie y con carros de caballos, los seguía como podía.", T,
   img='tross', kb='left', cap='Lituania, junio de 1941: infantería alemana con carros de caballos',
   html='<div class="ov right"><div class="h2 in tw" data-cue="un desastre total">Un desastre total</div>'
        '<div class="h3 in" data-cue="enormes cercos" style="margin-top:30px">Cercos gigantes</div><div class="h3 dim in" data-cue="carros de caballos">La mayoría, a pie y a caballo</div></div>', shade=True)
sc("Muchos olvidan ese detalle. La Wehrmacht no era un ejército totalmente motorizado. Invadió la Unión Soviética con cientos de miles de caballos. Los tanques iban delante, pero la mayor parte del ejército avanzaba al mismo ritmo que el de Napoleón.", I,
   img='tross', kb='in', shade=True,
   html='<div class="ov center"><div class="h1 in tw" data-cue="cientos de miles de caballos">Cientos de miles<br>de caballos</div></div>')
sc("En la fortaleza de Brest, en la frontera, un puñado de soldados soviéticos resistió durante semanas, aislados, sin agua y sin esperanza. Pero eran excepciones. A finales de junio, Minsk, la capital de Bielorrusia, ya había caído.", T,
   img='minsk_ruinas', kb='in', cap='Minsk, 1941',
   html='<div class="ov left"><div class="h2 in tw" data-cue="la fortaleza de brest">La fortaleza<br>de Brest</div><div class="h3 dim in" data-cue="durante semanas">Resiste semanas</div>'
        '<div class="h3 red in" data-cue="minsk" style="margin-top:30px">Cae Minsk</div></div>', shade=True)
sc("En el cerco de Bialystok y Minsk, los alemanes capturaron a cientos de miles de soldados. Columnas interminables de prisioneros caminaban hacia el oeste. Nadie estaba preparado para alimentarlos. Y nadie en el mando alemán tenía intención de hacerlo.", M,
   img='prisioneros_col', kb='in', cap='Columna de prisioneros soviéticos, 1941',
   html='<div class="ov right"><div class="h2 in tw" data-cue="cientos de miles de soldados">Cientos de miles<br>de prisioneros</div>'
        '<div class="h3 red in" data-cue="intencion de hacerlo" style="margin-top:30px">Sin comida. A propósito.</div></div>', shade=True)
sc("Su destino fue uno de los grandes crímenes de la guerra. A lo largo del conflicto, unos 5,7 millones de soldados soviéticos cayeron prisioneros de los alemanes. Según el Museo del Holocausto de Estados Unidos, unos 3,3 millones murieron. La mayoría, de hambre, de frío y de enfermedades, en campos al aire libre.", M,
   img='prisioneros_dnjepr', kb='up', side='right', cap='Prisioneros soviéticos en un campo de Ucrania, 1941',
   html='<div class="ov left"><div class="big in" data-cue="5,7 millones" style="font-size:130px">5,7 M</div><div class="h3 in" data-cue="5,7 millones" data-d="0.4">prisioneros soviéticos</div>'
        '<div class="big red in" data-cue="3,3 millones" style="font-size:130px;margin-top:20px">3,3 M</div><div class="h3 in" data-cue="3,3 millones" data-d="0.4">murieron</div></div>')
sc("En julio, la ofensiva llegó a Smolensk, a unos 400 kilómetros de Moscú. El camino parecía abierto. Pero allí, por primera vez, el Ejército Rojo contraatacó con fuerza. Los combates duraron semanas y frenaron el avance alemán.", T,
   img='smolensk', kb='in', cap='Smolensk, 1941',
   html='<div class="ov left"><div class="date in" data-t="0.2">Julio de 1941</div><div class="h1 in tw" data-cue="smolensk">Smolensk</div>'
        '<div class="h3 amber in" data-cue="400 kilometros">≈ 400 km de Moscú</div><div class="h3 red in" data-cue="frenaron el avance" style="margin-top:30px">El primer frenazo</div></div>', shade=True)
sc("Y los generales alemanes descubrieron algo inquietante. El general Franz Halder, jefe del Estado Mayor, lo escribió en su diario en agosto: al principio de la guerra contábamos con unas 200 divisiones enemigas. Ya hemos contado 360.", I,
   img='guderian', kb='in', side='right', cap='Los generales Guderian y Hoth, 1941',
   html='<div class="ov left"><div class="h3 dim in" data-cue="franz halder">Diario de Franz Halder, agosto de 1941</div>'
        '<div class="big in" data-cue="unas 200 divisiones" style="font-size:140px">200</div><div class="big red in" data-cue="ya hemos contado 360" style="font-size:140px">360</div></div>')
sc("La Unión Soviética era mucho más grande y mucho más resistente de lo que Hitler había imaginado. Por cada ejército que los alemanes destruían, aparecía otro. Y detrás del frente, los soviéticos estaban haciendo algo extraordinario.", I,
   bg='wjasma_panzer',
   html='<div class="ov center"><div class="h2 in tw" data-cue="mucho mas grande">Más grande.<br>Más resistente.</div>'
        '<div class="h3 amber in" data-cue="aparecia otro" style="margin-top:30px">Cada ejército destruido, otro nuevo</div></div>')
sc("Desmontaron más de 1.500 grandes fábricas y las cargaron en trenes rumbo a los montes Urales y Siberia, a miles de kilómetros. Allí, en algunos casos a la intemperie y en pleno invierno, las volvieron a montar y siguieron fabricando tanques y aviones.", I,
   bg='schnee_marsch',
   html='<div class="ov center"><div class="big amber in" data-cue="mas de 1.500" style="font-size:180px">+1.500</div><div class="h3 in" data-cue="grandes fabricas" >fábricas trasladadas al este</div>'
        '<div class="h3 dim in" data-cue="montes urales" style="margin-top:30px">Rumbo a los Urales y Siberia</div></div>')

# ======================= KIEV =======================
sc("Entonces, Hitler tomó una decisión que todavía se discute. En lugar de lanzarse directamente sobre Moscú, como querían sus generales, desvió parte de los tanques del centro hacia el sur, hacia Kiev. Quería el trigo de Ucrania y el carbón de la cuenca del Donets.", T,
   img='lagebesprechung', kb='right', cap='Hitler con Keitel y Brauchitsch, 1941',
   html='<div class="ov left"><div class="h2 in tw" data-cue="todavia se discute">Una decisión<br>polémica</div>'
        '<div class="h3 in" data-cue="hacia kiev" style="margin-top:30px">Moscú puede esperar: primero, Kiev</div></div>', shade=True)
sc("En septiembre de 1941, las tenazas alemanas se cerraron detrás de Kiev. Stalin había prohibido retirarse. Fue uno de los mayores cercos de la historia militar. Según las cifras alemanas, unos 665.000 soldados soviéticos cayeron prisioneros.", T,
   img='kiew', kb='in', cap='Kiev, 1941',
   html='<div class="ov right"><div class="date in" data-t="0.2">Septiembre de 1941</div><div class="h1 in tw" data-cue="detras de kiev">Kiev</div>'
        '<div class="big red in" data-cue="unos 665.000" style="font-size:130px">665.000</div><div class="h3 in" data-cue="unos 665.000" data-d="0.4">prisioneros (cifras alemanas)</div></div>', shade=True)
sc("Pocos días después, en un barranco a las afueras de Kiev llamado Babi Yar, unidades alemanas asesinaron a tiros a 33.771 judíos en solo dos días, el 29 y el 30 de septiembre. Lo sabemos por los informes que ellos mismos enviaron a Berlín.", M,
   bg='kiew',
   html='<div class="ov center"><div class="date in" data-t="0.2">29-30 de septiembre de 1941</div><div class="h1 in tw" data-cue="babi yar">Babi Yar</div>'
        '<div class="big red in" data-cue="33.771" style="font-size:160px">33.771</div><div class="h3 in" data-cue="en solo dos dias">judíos asesinados en dos días</div></div>')
sc("Porque detrás del frente avanzaban los Einsatzgruppen, los escuadrones de la muerte de las SS. Ciudad por ciudad, pueblo por pueblo, reunían a los judíos y los fusilaban junto a fosas. Antes de que existieran las cámaras de gas, el Holocausto empezó así, a tiros, en la Unión Soviética ocupada.", M,
   img='dorf_reiter', kb='in', shade=True,
   html='<div class="ov center"><div class="h2 in tw" data-cue="einsatzgruppen">Einsatzgruppen</div>'
        '<div class="h3 red in" data-cue="el holocausto empezo asi" style="margin-top:30px">El Holocausto empieza a tiros</div></div>')

# ======================= LENINGRADO =======================
sc("En el norte, el 8 de septiembre, los alemanes y sus aliados finlandeses cerraron el cerco de Leningrado. Hitler no quería tomar la ciudad. Quería algo peor: rendirla por hambre y borrarla del mapa.", T,
   img='leningrad_winter', kb='in', cap='Frente de Leningrado, invierno',
   html='<div class="ov left"><div class="date in" data-t="0.2">8 de septiembre de 1941</div><div class="h1 in tw" data-cue="el cerco de leningrado">Leningrado</div>'
        '<div class="h3 red in" data-cue="rendirla por hambre" style="margin-top:30px">Rendirla por hambre</div></div>', shade=True)
sc("El asedio duró 872 días. Durante el primer invierno, para muchos la ración de pan llegó a ser de 125 gramos al día. Muchas estimaciones hablan de unos 800.000 civiles muertos, la mayoría de hambre. Solo por el lago Ladoga helado, el llamado camino de la vida, llegaban algunos suministros.", M,
   img='leningrad_winter', kb='out', shade=True,
   html='<div class="ov center"><div class="big in" data-cue="872 dias" style="font-size:150px">872 días</div><div class="h3 amber in" data-cue="125 gramos">125 g de pan al día</div>'
        '<div class="h3 red in" data-cue="unos 800.000">≈ 800.000 civiles muertos</div><div class="h3 dim in" data-cue="camino de la vida" style="margin-top:20px">«El camino de la vida»</div></div>')
sc("Y frente a Leningrado combatían también españoles. La División Azul, formada por voluntarios que Franco envió en el verano de 1941, llegó al frente del río Vóljov en octubre. Allí descubrieron lo que era el invierno ruso.", I,
   img='division_azul', kb='in', cap='Voluntarios españoles de la División Azul en el frente del este',
   html='<div class="ov right"><div class="h1 in tw" data-cue="la division azul">División Azul</div><div class="h3 dim in" data-cue="rio voljov">Frente del Vóljov, octubre de 1941</div></div>', shade=True)

# ======================= TIFÓN =======================
sc("A finales de septiembre, Hitler volvió a mirar hacia Moscú. El 2 de octubre lanzó la Operación Tifón. Y otra vez, al principio, todo pareció salirle bien. En los cercos de Viazma y Briansk cayeron prisioneros cientos de miles de soldados soviéticos más.", T,
   img='wjasma_fuego', kb='in', cap='Viazma, octubre de 1941',
   html='<div class="ov left"><div class="date in" data-t="0.2">2 de octubre de 1941</div><div class="h1 in tw" data-cue="la operacion tifon">Operación Tifón</div>'
        '<div class="h3 red in" data-cue="viazma y briansk" style="margin-top:30px">Viazma y Briansk</div></div>', shade=True)
sc("En Moscú cundió el pánico. A mediados de octubre, el gobierno empezó a evacuar ministerios hacia el este, y miles de moscovitas intentaron huir. Pero Stalin decidió quedarse. Y llamó a un general duro y eficaz para defender la capital: Gueorgui Zhúkov.", T,
   img='zhukov', kb='in', side='right', fallback='wjasma_panzer',
   html='<div class="ov left"><div class="h2 in tw" data-cue="cundio el panico">Pánico<br>en Moscú</div><div class="h3 in" data-cue="decidio quedarse" style="margin-top:30px">Stalin se queda</div>'
        '<div class="h2 amber in" data-cue="zhukov">Zhúkov</div></div>')
sc("Y entonces llegó la lluvia. Los rusos la llaman rasputitsa: la época del barro. Los caminos de tierra se convirtieron en lodazales donde se hundían camiones, cañones y caballos. El avance alemán se arrastraba a pocos kilómetros al día.", I,
   img='schlamm2', kb='in', cap='Unión Soviética, otoño de 1941: soldados empujando un carro en el barro',
   html='<div class="ov right"><div class="h1 in tw" data-cue="rasputitsa">Rasputitsa</div><div class="h3 dim in" data-cue="la epoca del barro">La época del barro</div></div>', shade=True)
sc("Hitler y sus generales culparon después al barro y al frío de su derrota. Pero el barro afectaba a los dos bandos, y el invierno ruso llegaba todos los años. El verdadero problema era que la campaña rápida que habían planeado ya no existía.", I,
   img='schlamm1', kb='up', side='right', cap='Soldados alemanes sacando un coche del barro, octubre de 1941',
   html='<div class="ov left"><div class="h3 in" data-cue="culparon despues">¿La culpa? El barro.</div><div class="h3 in" data-cue="el invierno ruso">¿El frío?</div>'
        '<div class="h2 red in tw" data-cue="el verdadero problema" style="margin-top:30px">La guerra rápida<br>había fracasado</div></div>')
sc("El 7 de noviembre, aniversario de la revolución, Stalin organizó un desfile militar en la Plaza Roja, con la nieve cayendo y el enemigo a las puertas. Muchos de los soldados que desfilaron se fueron directamente desde la plaza al frente.", I,
   img='desfile', kb='in', cap='Moscú, 7 de noviembre de 1941: desfile en la Plaza Roja', fallback='schnee_marsch',
   html='<div class="ov left"><div class="date in" data-t="0.2">7 de noviembre de 1941</div><div class="h2 in tw" data-cue="la plaza roja">Desfile en<br>la Plaza Roja</div>'
        '<div class="h3 red in" data-cue="directamente desde la plaza al frente" style="margin-top:30px">De la plaza, al frente</div></div>', shade=True)
sc("Cuando el suelo se heló, los alemanes volvieron a avanzar. A finales de noviembre y principios de diciembre, algunas unidades llegaron a unos 30 kilómetros del Kremlin. Dicen que con prismáticos podían ver las torres de la ciudad. Fue lo más cerca que estuvieron nunca.", T,
   img='schnee_moskau', kb='left', cap='Ante Moscú, finales de 1941',
   html='<div class="ov right"><div class="big red in" data-cue="unos 30 kilometros" style="font-size:180px">≈ 30 km</div><div class="h3 in" data-cue="del kremlin">del Kremlin</div>'
        '<div class="h3 dim in" data-cue="lo mas cerca" style="margin-top:30px">Nunca llegaron más cerca</div></div>', shade=True)

# ======================= EL INVIERNO =======================
sc("Y entonces llegó el frío de verdad. En diciembre, los termómetros bajaron de los 30 grados bajo cero. Los motores no arrancaban, el aceite se congelaba y las armas se encasquillaban. Los soldados alemanes seguían con sus uniformes de verano.", M,
   img='schnee_schlitten', kb='in', cap='Unión Soviética, invierno: soldados alemanes con un coche sobre un trineo',
   html='<div class="ov left"><div class="big in" data-cue="30 grados bajo cero" style="font-size:180px">-30 °C</div>'
        '<div class="h3 in" data-cue="los motores no arrancaban">Motores congelados</div><div class="h3 red in" data-cue="uniformes de verano">Uniformes de verano</div></div>', shade=True)
sc("Decenas de miles sufrieron congelaciones. En Alemania, Goebbels tuvo que organizar una colecta de ropa de abrigo entre la población: abrigos de piel, guantes, esquís. Llegó tarde. La propaganda que había prometido una victoria rápida ya no podía esconder la verdad.", M,
   img='schnee_marsch', kb='left', shade=True,
   html='<div class="ov center"><div class="h2 in tw" data-cue="congelaciones">Congelaciones</div><div class="h3 in" data-cue="una colecta de ropa" style="margin-top:30px">Colecta de abrigos en Alemania</div>'
        '<div class="h3 red in" data-cue="llego tarde">Demasiado tarde</div></div>')
sc("Mientras tanto, Stalin guardaba un as en la manga. Su espía Sorge le había informado de que Japón no pensaba atacar a la Unión Soviética por el este. Así que Stalin pudo traer hacia Moscú tropas de Siberia y del Lejano Oriente, frescas y equipadas para el invierno.", I,
   img='stalin', kb='in', side='right', fallback='leningrad_winter',
   html='<div class="ov left"><div class="h2 in tw" data-cue="un as en la manga">Un as<br>en la manga</div><div class="h3 in" data-cue="japon no pensaba atacar" style="margin-top:30px">Japón no atacará</div>'
        '<div class="h3 amber in" data-cue="tropas de siberia">Tropas de Siberia, hacia Moscú</div></div>')
sc("El 5 de diciembre de 1941, con temperaturas de hasta 40 grados bajo cero en algunas zonas, el Ejército Rojo lanzó su contraofensiva ante Moscú. Por primera vez en toda la guerra, la Wehrmacht tuvo que retroceder de verdad. Y en algunos sectores, a la desbandada.", T,
   img='wjasma_gefang', kb='in', side='right', cap='Combates en la región de Viazma',
   html='<div class="ov left"><div class="date in" data-t="0.2">5 de diciembre de 1941</div><div class="h1 in tw" data-cue="su contraofensiva">La contra-<br>ofensiva</div>'
        '<div class="h3 red in" data-cue="tuvo que retroceder" style="margin-top:30px">La Wehrmacht retrocede</div></div>')
sc("Dos días después, Japón atacó Pearl Harbor. Y el 11 de diciembre, Hitler cometió otro error colosal: declaró la guerra a Estados Unidos. En menos de una semana, Alemania había perdido la ocasión de ganar la guerra rápida en el este y se había enfrentado a la mayor potencia industrial del planeta.", T,
   bg='lagebesprechung',
   html=timeline([('5 dic.', 'Contraofensiva ante Moscú', 'dos dias despues'), ('7 dic.', 'Pearl Harbor', 'pearl harbor'),
                  ('11 dic.', 'Alemania declara la guerra a EE. UU.', 'declaro la guerra a estados unidos')], 'Diciembre de 1941'))
sc("Hitler destituyó al comandante en jefe del ejército, Walther von Brauchitsch, y asumió él mismo el mando. Y dio una orden: ni un paso atrás. Los soldados debían resistir donde estaban, pasara lo que pasara.", T,
   img='lagebesprechung', kb='in', cap='Hitler con Keitel y Brauchitsch, 1941',
   html='<div class="ov left"><div class="h3 dim in" data-cue="brauchitsch">Brauchitsch, destituido</div><div class="h2 in tw" data-cue="asumio el mismo el mando">Hitler toma<br>el mando</div>'
        '<div class="stamp in" data-cue="ni un paso atras" style="margin-top:30px">Ni un paso atrás</div></div>', shade=True)

# ======================= BALANCE =======================
sc("Cuando terminó el invierno, Moscú seguía en manos soviéticas. Leningrado seguía resistiendo. El ejército alemán había sufrido cerca de un millón de bajas entre muertos, heridos, desaparecidos y enfermos. La Wehrmacht nunca volvería a ser tan fuerte como el 22 de junio.", M,
   bg='schnee_schlitten',
   html='<div class="ov center"><div class="h3 in" data-cue="moscu seguia">Moscú resiste</div><div class="h3 in" data-cue="leningrado seguia">Leningrado resiste</div>'
        '<div class="big red in" data-cue="cerca de un millon" style="font-size:150px;margin-top:20px">≈ 1 millón</div><div class="h3 in" data-cue="cerca de un millon" data-d="0.4">de bajas alemanas</div></div>')
sc("Las pérdidas soviéticas fueron muchísimo mayores. Millones de muertos y prisioneros solo en 1941. Pero la Unión Soviética tenía algo que Alemania no tenía: un territorio inmenso, una población enorme y un régimen dispuesto a sacrificarlas sin límite.", M,
   img='prisioneros_marcha', kb='in', shade=True, cap='Prisioneros soviéticos, octubre de 1941',
   html='<div class="ov center"><div class="h2 in tw" data-cue="muchisimo mayores">Pérdidas soviéticas:<br>millones</div>'
        '<div class="h3 amber in" data-cue="un territorio inmenso" style="margin-top:30px">Territorio inmenso · población enorme</div></div>')

# ======================= POR QUÉ FUE EL MAYOR ERROR =======================
sc("¿Por qué decimos que fue el mayor error de Hitler? Primero, porque abrió el frente que acabaría destruyendo a su ejército. La mayoría de los soldados alemanes muertos en toda la guerra cayeron en el frente del este.", I,
   img='stalingrado_vista', kb='in', shade=True,
   html='<div class="ov center"><div class="h3 dim in" data-t="0.3">¿Por qué fue su mayor error?</div><div class="h2 in tw" data-cue="primero">1 · El frente que le destruyó</div>'
        '<div class="h3 red in" data-cue="la mayoria de los soldados alemanes" style="margin-top:30px">La mayoría de los muertos alemanes cayeron en el este</div></div>')
sc("Segundo, porque convirtió en enemigo a quien le estaba suministrando petróleo y cereales. Y tercero, porque se lanzó a una guerra larga y de desgaste contra la Unión Soviética, el Reino Unido y, muy pronto, Estados Unidos. Una guerra que Alemania, con sus recursos, no podía ganar.", I,
   bg='stalingrado_vista',
   html='<div class="ov center"><div class="h2 in tw" data-cue="segundo">2 · Su proveedor, su enemigo</div>'
        '<div class="h2 in tw" data-cue="y tercero" style="margin-top:20px">3 · Una guerra imposible</div>'
        '<div class="h3 dim in" data-cue="no podia ganar" style="margin-top:30px">URSS + Reino Unido + EE. UU.</div></div>')
sc("Y Barbarroja tuvo otra consecuencia, la más terrible. La guerra de exterminio en el este fue el escenario donde el Holocausto pasó de la persecución al asesinato en masa. Los fusilamientos de 1941 abrieron el camino a Auschwitz.", M,
   bg='dorf_brennt',
   html='<div class="ov center"><div class="h2 red in tw" data-cue="la mas terrible">La consecuencia<br>más terrible</div>'
        '<div class="h3 in" data-cue="abrieron el camino a auschwitz" style="margin-top:30px">De los fusilamientos de 1941, a Auschwitz</div></div>')

# ======================= CIERRE =======================
sc("Napoleón entró en Rusia en junio de 1812 con el ejército más grande que Europa había visto. Seis meses después, lo que quedaba de él se arrastraba por la nieve de vuelta a casa. Hitler conocía esa historia. Y aun así, la repitió.", M,
   img='schnee_marsch', kb='out', shade=True,
   html='<div class="ov center"><div class="h3 in" data-cue="napoleon entro en rusia">1812 · Napoleón</div><div class="h3 in" data-cue="hitler conocia">1941 · Hitler</div>'
        '<div class="h2 red in tw" data-cue="conocia esa historia" style="margin-top:30px">La misma historia</div></div>')
sc("Barbarroja no fue derrotada por el barro ni por el frío. Fue derrotada por la soberbia de un hombre que creyó que bastaba con dar una patada a la puerta. Porque el error más peligroso no es equivocarse. Es estar tan seguro de tener razón que nadie se atreve a decirte que no.", M,
   img='schnee_moskau', kb='out', shade=True,
   html='<div class="ov center"><div class="q in" data-cue="el error mas peligroso">El error más peligroso es estar tan seguro<br>de tener razón que nadie se atreve<br>a decirte que no.</div></div>')
sc("En el próximo capítulo viajamos a la batalla que cambió el rumbo de la guerra: Stalingrado. Si no quieres perdértelo, suscríbete. "
   "Y cuéntame en los comentarios: ¿crees que Hitler podría haber tomado Moscú si no se hubiera desviado hacia Kiev?", M,
   bg='stalingrado_vista',
   html='<div class="ov center"><div class="tag in" data-t="0.2">Próximo capítulo</div><div class="h2 in tw" data-t="0.4">Stalingrado</div>'
        '<div class="rule in" data-t="0.6"></div><div class="h3 dim in" data-cue="suscribete">Suscríbete para no perdértelo</div>'
        '<div class="who in" data-cue="suscribete" data-d="1.5" style="font-size:24px;margin-top:80px">Fuentes: Britannica, USHMM, German History in Documents (GHI), Deutsches Historisches Museum, World History Encyclopedia. '
        'Imágenes: Bundesarchiv y Wikimedia Commons (créditos en la descripción).</div></div>')

spec = dict(title='Operación Barbarroja', brand='Sombras del 39', voice='hyKxCTlAqtnW188CgltM', model='eleven_v4',
            voice_settings=dict(stability=0.5, similarity_boost=0.75), tail=4, scenes=S,
            thumb=dict(img='img/schlamm2.jpg', fy=0.4, l1='El mayor error<br>de Hitler', l2='1941', l3='Operación Barbarroja'))
json.dump(spec, open(os.path.join(here, 'spec.json'), 'w'), ensure_ascii=False, indent=1)
txt = ' '.join(s['say'] for s in S)
print(len(S), 'escenas ·', len(txt), 'caracteres · ~%.1f min' % (len(txt) / 13.8 / 60), '· sin foto:', [i for i, s in enumerate(S) if 'img' not in s and 'bg' not in s])
open(os.path.join(here, 'guion.txt'), 'w').write('\n\n'.join(s['say'] for s in S) + '\n')
