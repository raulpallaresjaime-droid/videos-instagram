# Genera spec.json del episodio 7 (mini documental 15-20 min). Uso: python3 build_spec.py
import json, os
here = os.path.dirname(os.path.abspath(__file__))
has = lambda n: os.path.exists(os.path.join(here, 'img', n + '.jpg'))

S = []
def sc(say, mood='inquietud', **kw):
    if 'img' in kw and not has(kw['img']):
        fb = kw.pop('fallback', 'stalingrado_vista'); fb = fb if has(fb) else 'schleswig1'; kw.pop('img'); kw.pop('side', None); kw.pop('kb', None); kw.pop('cap', None)
        kw['bg'] = f'img/{fb}.jpg'
    elif 'img' in kw:
        kw['img'] = f"img/{kw['img']}.jpg"; kw.pop('fallback', None)
    if 'bg' in kw and not kw['bg'].startswith('img/'):
        b = kw['bg'] if has(kw['bg']) else kw.pop('fallback', 'stalingrado_vista')
        b = b if has(b) else 'schleswig1'
        kw['bg'] = f"img/{b}.jpg"
    kw.pop('fallback', None)
    S.append(dict(say=say, mood=mood, **kw))

def timeline(items, title=None):
    ev = ''.join(f'<div class="e in" data-cue="{c}"><div class="d">{d}</div><div class="t">{t}</div></div>' for d, t, c in items)
    head = f'<div class="h3 dim in" data-t="0" style="margin-bottom:80px">{title}</div>' if title else ''
    return f'<div class="ov center">{head}<div class="tl">{ev}</div></div>'

def anio(y, sub, cue):
    return (f'<div class="ov center"><div class="big in" data-t="0.2" style="font-size:260px">{y}</div>'
            f'<div class="h3 amber in" data-cue="{cue}" style="margin-top:20px">{sub}</div></div>')

T, I, M = 'tension', 'inquietud', 'melancolia'

# ======================= GANCHO =======================
sc("Seis años y un día. Eso duró la guerra más mortífera de la historia de la humanidad. Empezó una madrugada de septiembre de 1939 en un puerto del Báltico y terminó en la cubierta de un acorazado en la bahía de Tokio. "
   "Por el camino murieron más de 60 millones de personas. La mayoría, civiles.", T,
   img='schleswig1', kb='in', shade=True,
   html='<div class="ov center"><div class="big in" data-t="0" style="font-size:150px">6 años y 1 día</div>'
        '<div class="h3 in" data-cue="un puerto del baltico" style="margin-top:30px">1 sept. 1939 · Danzig</div><div class="h3 in" data-cue="bahia de tokio">2 sept. 1945 · Tokio</div>'
        '<div class="h2 red in" data-cue="mas de 60 millones" style="margin-top:30px">+60 millones de muertos</div></div>')
sc("Hoy te la voy a contar entera. De Polonia a Hiroshima. Las batallas que la decidieron, los errores que la cambiaron y el precio que pagó el mundo. Toda la Segunda Guerra Mundial, en unos veinte minutos.", M,
   img='stalingrado_vista', kb='in', shade=True,
   html='<div class="ov center"><div class="tag in" data-t="0.4">Capítulo 7</div>'
        '<div class="h1 in" data-t="0.6">Toda la Segunda<br>Guerra Mundial</div>'
        '<div class="date in" data-cue="en unos veinte minutos" style="margin-top:30px">En 20 minutos</div></div>')

# ======================= 1939 =======================
sc("Empecemos por el principio. En 1939, Adolf Hitler llevaba seis años en el poder. Había rearmado Alemania, se había anexionado Austria y había ocupado Checoslovaquia sin disparar un tiro. Las democracias europeas habían cedido una y otra vez.", I,
   img='hitler', kb='in', side='right',
   html='<div class="ov left"><div class="date in" data-t="0.2">1933-1939</div><div class="h3 in" data-cue="rearmado">Rearme</div>'
        '<div class="h3 in" data-cue="austria">Austria, 1938</div><div class="h3 in" data-cue="checoslovaquia">Checoslovaquia, 1939</div>'
        '<div class="h3 red in" data-cue="una y otra vez" style="margin-top:20px">Nadie le frena</div></div>')
sc("En agosto de 1939 firmó con Stalin un pacto de no agresión. Y en secreto, los dos dictadores se repartieron Europa del Este. Con las espaldas cubiertas, Hitler ya podía atacar.", T,
   img='pacto', kb='in', fy=0.35, cap='Moscú, agosto de 1939: la firma del pacto germano-soviético',
   html='<div class="ov left"><div class="date in" data-t="0.2">23 de agosto de 1939</div><div class="h2 in tw" data-cue="pacto de no agresion">Hitler y Stalin</div>'
        '<div class="stamp in" data-cue="en secreto" style="margin-top:30px">Protocolo secreto</div></div>', shade=True)
sc("El 1 de septiembre de 1939, Alemania invade Polonia. Dos días después, el Reino Unido y Francia le declaran la guerra. Y el 17 de septiembre, la Unión Soviética entra en Polonia por el este. En poco más de un mes, Polonia desaparece del mapa.", T,
   bg='panzer1',
   html=timeline([('1 sept.', 'Alemania invade Polonia', 'alemania invade polonia'), ('3 sept.', 'R. Unido y Francia declaran la guerra', 'le declaran la guerra'),
                  ('17 sept.', 'La URSS entra por el este', 'por el este'), ('Octubre', 'Polonia desaparece', 'desaparece del mapa')], '1939'))
sc("Y entonces, algo extraño. Durante meses, en el frente occidental casi no pasa nada. Franceses y británicos esperan detrás de sus fortificaciones. Los periodistas lo llamaron la guerra de broma.", I,
   img='varsovia_ruinas', kb='left', shade=True,
   html='<div class="ov center"><div class="h3 dim in" data-t="0.3">Otoño e invierno de 1939</div><div class="h1 in tw" data-cue="algo extrano">«La guerra<br>de broma»</div></div>')

# ======================= 1940 =======================
sc("En la primavera de 1940, la broma se acaba. En abril, Alemania ocupa Dinamarca y Noruega. Y el 10 de mayo lanza su gran ataque al oeste: Holanda, Bélgica, Luxemburgo y Francia. Ese mismo día, Winston Churchill se convierte en primer ministro británico.", T,
   bg='stuka',
   html=anio('1940', 'Mayo: el ataque al oeste', 'su gran ataque'))
sc("El ejército francés era uno de los más grandes del mundo. Pero los generales alemanes hicieron algo que nadie esperaba: lanzaron sus tanques a través de los bosques de las Ardenas, que se consideraban casi impracticables. Rompieron el frente y llegaron al mar en unos diez días.", T,
   img='panzer1', kb='right', cap='Tanquista alemán, 1939',
   html='<div class="ov left"><div class="h2 in tw" data-cue="las ardenas">Las Ardenas</div><div class="h3 dim in" data-cue="casi impracticables">«Casi impracticables»</div>'
        '<div class="h3 red in" data-cue="llegaron al mar" style="margin-top:30px">Frente roto. Hasta el mar.</div></div>', shade=True)
sc("Cientos de miles de soldados británicos y franceses quedan atrapados en la playa de Dunkerque. Y entonces ocurre lo que los británicos llamarían un milagro: con buques de guerra, pesqueros y barcos de recreo, en nueve días rescatan a más de 338.000 hombres.", I,
   img='dunkerque', kb='in', cap='Dunkerque, 1940: vehículos y barcos abandonados en la playa',
   html='<div class="ov right"><div class="h1 in" data-cue="dunkerque">Dunkerque</div><div class="big amber in" data-cue="mas de 338.000" style="font-size:130px">338.000</div>'
        '<div class="h3 in" data-cue="mas de 338.000" data-d="0.4">soldados rescatados en 9 días</div></div>', shade=True)
sc("El 14 de junio, los alemanes entran en París. Ocho días después, Francia firma el armisticio en Compiègne, en el mismo vagón de tren donde Alemania se había rendido en 1918. Hitler quiso que la humillación fuera completa.", T,
   img='paris_desfile', kb='up', fy=0.3, cap='París, junio de 1940: desfile alemán en el Arco del Triunfo',
   html='<div class="ov left"><div class="date in" data-t="0.2">14 de junio de 1940</div><div class="h2 in tw" data-cue="entran en paris">París cae</div>'
        '<div class="h3 in" data-cue="compiegne" style="margin-top:30px">22 de junio: armisticio en Compiègne</div><div class="h3 dim in" data-cue="mismo vagon">El mismo vagón de 1918</div></div>', shade=True)
sc("Al amanecer del 23 de junio, Hitler visitó París durante unas pocas horas. Se hizo fotografiar delante de la torre Eiffel. Francia, la gran potencia militar, había caído en seis semanas.", M,
   img='hitler_paris', kb='in', side='right', cap='Hitler en París, 23 de junio de 1940',
   html='<div class="ov left"><div class="h2 in tw" data-cue="torre eiffel">Hitler<br>en París</div><div class="h3 red in" data-cue="seis semanas" style="margin-top:30px">Francia cae en 6 semanas</div></div>')
sc("El Reino Unido se quedó solo. Hitler pensó que pediría la paz, pero Churchill se negó. Alemania necesitaba dominar el cielo para poder invadir la isla. Así empezó la batalla de Inglaterra, la primera batalla de la historia librada casi solo en el aire.", T,
   img='heinkel_londres', kb='left', cap='Bombarderos alemanes Heinkel He 111 sobre el canal de la Mancha',
   html='<div class="ov right"><div class="h3 dim in" data-t="0.3">Verano de 1940</div><div class="h2 in tw" data-cue="la batalla de inglaterra">La batalla<br>de Inglaterra</div></div>', shade=True)
sc("Los pilotos de la Royal Air Force, con la ayuda del radar, resistieron. Churchill lo resumió en una frase famosa: nunca tantos debieron tanto a tan pocos. En septiembre, Hitler aplazó la invasión. Fue su primera derrota.", I,
   img='heinkel_londres', kb='in', shade=True,
   html='<div class="ov center"><div class="q in" data-cue="nunca tantos">«Nunca tantos debieron<br>tanto a tan pocos»</div><div class="who in" data-cue="nunca tantos" data-d="1">Winston Churchill, 1940</div>'
        '<div class="h3 amber in" data-cue="su primera derrota" style="margin-top:40px">La primera derrota de Hitler</div></div>')
sc("Entonces, Alemania cambió de táctica y bombardeó las ciudades británicas noche tras noche. Fue el Blitz. Entre septiembre de 1940 y mayo de 1941, más de 40.000 civiles británicos murieron bajo las bombas. Pero el país no se rindió.", M,
   bg='heinkel_londres',
   html='<div class="ov center"><div class="h1 in tw" data-cue="fue el blitz">El Blitz</div><div class="big red in" data-cue="mas de 40.000" style="font-size:140px">+40.000</div>'
        '<div class="h3 in" data-cue="mas de 40.000" data-d="0.4">civiles muertos en Reino Unido</div></div>')
sc("¿Y España? El 23 de octubre de 1940, Hitler y Franco se reunieron en la estación de Hendaya. Franco pidió a cambio de entrar en la guerra Gibraltar, buena parte del norte de África y armas que Alemania no podía darle. No hubo acuerdo. España, arruinada por su propia guerra civil, se quedó fuera.", I,
   img='hendaya', kb='in', cap='Hendaya, 23 de octubre de 1940: Hitler y Franco',
   html='<div class="ov left"><div class="date in" data-t="0.2">23 de octubre de 1940</div><div class="h2 in tw" data-cue="hendaya">Hendaya</div>'
        '<div class="h3 in" data-cue="no hubo acuerdo" style="margin-top:30px">No hubo acuerdo</div></div>', shade=True)
sc("Mientras tanto, la guerra se extendía. En junio de 1940, la Italia de Mussolini había entrado en la guerra junto a Hitler. Pero sus ataques en Grecia y en el norte de África salieron mal, y Alemania tuvo que acudir en su ayuda.", I,
   img='africa', kb='right', cap='Norte de África: oficiales del Afrikakorps',
   html='<div class="ov right"><div class="date in" data-t="0.2">10 de junio de 1940</div><div class="h2 in tw" data-cue="la italia de mussolini">Italia entra<br>en la guerra</div>'
        '<div class="h3 dim in" data-cue="salieron mal" style="margin-top:30px">Grecia · norte de África</div></div>', shade=True)
sc("En febrero de 1941 desembarcó en Libia un general alemán que se haría famoso en el desierto: Erwin Rommel, el Zorro del Desierto. Durante dos años, sus tanques y los británicos se persiguieron arriba y abajo por las arenas de Libia y Egipto.", I,
   img='rommel', kb='in', side='right', cap='Erwin Rommel',
   html='<div class="ov left"><div class="h1 in" data-cue="erwin rommel">Rommel</div><div class="h3 amber in" data-cue="el zorro del desierto">«El Zorro del Desierto»</div>'
        '<div class="h3 dim in" data-cue="libia y egipto" style="margin-top:30px">Libia · Egipto · 1941-1943</div></div>')

# ======================= 1941 =======================
sc("Y llegamos a 1941, el año en que la guerra se hizo de verdad mundial. Hitler dominaba casi toda Europa. Pero nunca había olvidado su gran objetivo, el que había escrito años antes en Mi lucha: conquistar espacio vital en el este.", I,
   bg='vormarsch_panzer',
   html=anio('1941', 'El objetivo: el este', 'espacio vital en el este'))
sc("El 22 de junio de 1941, más de 3 millones de soldados alemanes, junto con sus aliados, invaden la Unión Soviética. Es la Operación Barbarroja, la mayor invasión terrestre de la historia. Stalin, que no había querido creer los avisos, queda desconcertado.", T,
   img='vormarsch_panzer', kb='right', cap='Unión Soviética, junio de 1941: tanques alemanes en el avance',
   html='<div class="ov left"><div class="date in" data-t="0.2">22 de junio de 1941</div><div class="h1 in tw" data-cue="operacion barbarroja">Barbarroja</div>'
        '<div class="big red in" data-cue="mas de 3 millones" style="font-size:120px">+3 millones</div><div class="h3 in" data-cue="mas de 3 millones" data-d="0.4">de soldados alemanes</div></div>', shade=True)
sc("Al principio, el avance es arrollador. Ejércitos soviéticos enteros quedan rodeados y millones de soldados caen prisioneros. La mayoría morirían de hambre, frío y enfermedades en los campos alemanes.", M,
   img='prisioneros_col', kb='in', cap='Prisioneros soviéticos, 1941',
   html='<div class="ov right"><div class="h2 in tw" data-cue="millones de soldados caen prisioneros">Millones de<br>prisioneros</div>'
        '<div class="h3 red in" data-cue="la mayoria moririan" style="margin-top:30px">La mayoría morirían</div></div>', shade=True)
sc("Entre los invasores había también españoles. Franco no entró en la guerra, pero envió a la División Azul, decenas de miles de voluntarios que combatieron en el frente ruso, junto a Leningrado. Muchos no volvieron.", M,
   img='division_azul', kb='in', cap='Voluntarios españoles de la División Azul en el frente del este',
   html='<div class="ov right"><div class="h1 in tw" data-cue="la division azul">División Azul</div><div class="h3 dim in" data-cue="junto a leningrado">Frente de Leningrado</div></div>', shade=True)
sc("Leningrado quedó cercada. El asedio duró 872 días. Sin comida ni calefacción, cientos de miles de civiles murieron de hambre y de frío. Muchas estimaciones hablan de unos 800.000 muertos, solo en esa ciudad.", M,
   img='leningrad_winter', kb='in', shade=True, cap='Frente de Leningrado, invierno',
   html='<div class="ov center"><div class="h1 in" data-cue="leningrado quedo cercada">Leningrado</div><div class="big in" data-cue="872 dias" style="font-size:150px">872 días</div>'
        '<div class="h3 red in" data-cue="unos 800.000">≈ 800.000 civiles muertos</div></div>')
sc("Pero los alemanes no llegaron a Moscú. Las lluvias del otoño convirtieron los caminos en barro y luego llegó un invierno terrible, para el que no estaban preparados. El 5 de diciembre, el Ejército Rojo contraatacó. Por primera vez, la Wehrmacht retrocedía.", T,
   img='schnee_moskau', kb='left', cap='Ante Moscú, invierno de 1941',
   html='<div class="ov left"><div class="h2 in tw" data-cue="no llegaron a moscu">Moscú resiste</div><div class="h3 in" data-cue="en barro">Barro</div><div class="h3 in" data-cue="un invierno terrible">Hielo</div>'
        '<div class="h3 red in" data-cue="la wehrmacht retrocedia" style="margin-top:30px">5 de diciembre: contraataque</div></div>', shade=True)
sc("Detrás del frente, en el verano de 1941 empezó otra guerra: la que los nazis libraban contra los judíos. Unidades especiales de las SS, los Einsatzgruppen, fusilaban a pueblos enteros. Era el comienzo del Holocausto.", M,
   img='dorf_brennt', kb='in', shade=True,
   html='<div class="ov center"><div class="h3 dim in" data-t="0.3">Detrás del frente</div><div class="h2 in tw" data-cue="einsatzgruppen">Einsatzgruppen</div>'
        '<div class="h2 red in" data-cue="el comienzo del holocausto" style="margin-top:30px">Empieza el Holocausto</div></div>')
sc("En enero de 1942, en una villa a orillas del lago Wannsee, en Berlín, quince altos cargos nazis coordinaron lo que llamaban la solución final. En campos como Auschwitz, Treblinka o Sobibor se asesinó a escala industrial. Al final de la guerra, unos 6 millones de judíos habían sido asesinados.", M,
   img='puerta_birkenau', kb='in', shade=True, cap='Auschwitz-Birkenau',
   html='<div class="ov center"><div class="date in" data-cue="wannsee">20 de enero de 1942 · Wannsee</div><div class="h2 in tw" data-cue="la solucion final">«La solución final»</div>'
        '<div class="big red in" data-cue="unos 6 millones" style="font-size:150px;margin-top:20px">6 millones</div><div class="h3 in" data-cue="unos 6 millones" data-d="0.4">de judíos asesinados</div></div>')

# ======================= PEARL HARBOR =======================
sc("Mientras tanto, al otro lado del mundo, Japón llevaba años en guerra. Había invadido China en 1937. Para millones de chinos, la Segunda Guerra Mundial no empezó en 1939, sino dos años antes.", I,
   bg='refugiados',
   html='<div class="ov center"><div class="date in" data-t="0.2">Asia</div><div class="h1 in tw" data-cue="invadido china">Japón invade China</div>'
        '<div class="big amber in" data-cue="en 1937" style="font-size:150px">1937</div></div>')
sc("Japón quería los recursos del sudeste asiático, sobre todo el petróleo. El único que podía impedírselo era Estados Unidos. Así que el 7 de diciembre de 1941, sin declaración de guerra, sus aviones atacaron la base naval estadounidense de Pearl Harbor, en Hawái.", T,
   img='pearl', kb='in', cap='Pearl Harbor, 7 de diciembre de 1941: el acorazado USS Arizona en llamas', fallback='schleswig1',
   html='<div class="ov left"><div class="date in" data-t="0.2">7 de diciembre de 1941</div><div class="h1 in tw" data-cue="pearl harbor">Pearl Harbor</div></div>', shade=True)
sc("Murieron 2.403 estadounidenses. El presidente Roosevelt lo llamó una fecha que vivirá en la infamia. Cuatro días después, Hitler cometió otro error enorme: declaró la guerra a Estados Unidos. Ahora sí, era una guerra mundial.", T,
   img='pearl', kb='out', shade=True, fallback='schleswig1',
   html='<div class="ov center"><div class="big red in" data-cue="murieron 2.403" style="font-size:160px">2.403</div><div class="h3 in" data-cue="murieron 2.403" data-d="0.4">estadounidenses muertos</div>'
        '<div class="h3 amber in" data-cue="declaro la guerra a estados unidos" style="margin-top:40px">11 de diciembre: Hitler declara la guerra a EE. UU.</div></div>')

# ======================= 1942 =======================
sc("En los primeros meses de 1942, Japón parece imparable. Conquista Filipinas, Malasia, Birmania y las Indias Orientales Holandesas. En Singapur, más de 80.000 soldados británicos y de la Commonwealth se rinden. Churchill lo llamó el peor desastre de la historia militar británica.", T,
   bg='midway', fallback='schleswig1',
   html=anio('1942', 'Japón, imparable', 'parece imparable'))
sc("Pero en junio de 1942, junto al atolón de Midway, la marina estadounidense, que había descifrado los códigos japoneses, tiende una emboscada. En un solo día, Japón pierde cuatro portaaviones. Ya nunca recuperaría la iniciativa en el Pacífico.", T,
   img='midway', kb='in', cap='Midway, junio de 1942: bombarderos en picado estadounidenses', fallback='schleswig1',
   html='<div class="ov left"><div class="date in" data-t="0.2">Junio de 1942</div><div class="h1 in tw" data-cue="midway">Midway</div>'
        '<div class="h3 red in" data-cue="cuatro portaaviones" style="margin-top:30px">Japón pierde 4 portaaviones</div></div>', shade=True)
sc("En Europa, en el verano de 1942, Hitler vuelve a atacar en la Unión Soviética. Esta vez hacia el sur, hacia el petróleo del Cáucaso. Y en el camino, una ciudad que llevaba el nombre del dictador soviético: Stalingrado.", T,
   img='stalingrado_ruinas', kb='in', cap='Stalingrado, 1942',
   html='<div class="ov right"><div class="h3 dim in" data-cue="hacia el sur">Hacia el petróleo del Cáucaso</div><div class="h1 in tw" data-cue="y en el camino">Stalingrado</div></div>', shade=True)
sc("Fue la batalla más feroz de la guerra. Se luchó calle por calle, casa por casa, a veces habitación por habitación. Los soldados alemanes la llamaban la guerra de las ratas. La ciudad quedó reducida a escombros.", T,
   img='stalingrado_fabrica', kb='right', cap='Soldados alemanes en las ruinas de una fábrica de Stalingrado',
   html='<div class="ov left"><div class="h3 in" data-cue="calle por calle">Calle por calle</div><div class="h3 in" data-cue="casa por casa">Casa por casa</div>'
        '<div class="h2 red in tw" data-cue="la guerra de las ratas" style="margin-top:30px">«La guerra<br>de las ratas»</div></div>', shade=True)
sc("En noviembre, el Ejército Rojo lanza una contraofensiva y rodea por completo al Sexto Ejército alemán. Hitler prohíbe retirarse. Durante el invierno, cientos de miles de hombres quedan atrapados en el hielo, sin comida ni munición suficiente.", T,
   img='stalingrado_lanzallamas', kb='in', cap='Stalingrado, 1942',
   html='<div class="ov right"><div class="date in" data-t="0.2">19 de noviembre de 1942</div><div class="h2 in tw" data-cue="rodea por completo">El cerco</div>'
        '<div class="stamp in" data-cue="prohibe retirarse" style="margin-top:30px">Prohibido retirarse</div></div>', shade=True)
sc("A principios de febrero de 1943, los últimos alemanes se rinden. Unos 91.000 hombres caen prisioneros. Solo unos 5.000 o 6.000 volverían algún día a Alemania, años después de la guerra. Stalingrado fue el principio del fin para Hitler.", M,
   img='stalingrado_prisioneros', kb='in', cap='Stalingrado, 1943: un soldado soviético y un prisionero alemán',
   html='<div class="ov right"><div class="big in" data-cue="unos 91.000" style="font-size:140px">91.000</div><div class="h3 in" data-cue="unos 91.000" data-d="0.3">prisioneros</div>'
        '<div class="big red in" data-cue="solo unos 5.000" style="font-size:100px;margin-top:20px">≈ 5.000-6.000</div><div class="h3 in" data-cue="volverian" >volvieron a casa</div></div>', shade=True)
sc("Al mismo tiempo, en Egipto, los británicos del general Montgomery derrotaban a Rommel en El Alamein. Y en noviembre de 1942, tropas estadounidenses y británicas desembarcaban en Marruecos y Argelia. Churchill dijo entonces: esto no es el final, ni siquiera el principio del final. Pero quizá sea el final del principio.", I,
   img='africa', kb='out', shade=True,
   html='<div class="ov center"><div class="h1 in" data-cue="el alamein">El Alamein</div>'
        '<div class="q in" data-cue="esto no es el final" style="margin-top:30px">«No es el final… pero quizá<br>sea el final del principio»</div><div class="who in" data-cue="el final del principio">Winston Churchill, noviembre de 1942</div></div>')

# ======================= 1943 =======================
sc("1943 es el año en que la guerra cambia de dirección. En el Atlántico, los submarinos alemanes, que habían hundido miles de barcos mercantes, empiezan a perder la batalla frente a los convoyes aliados, el radar y los aviones de largo alcance.", I,
   bg='stalingrado_vista',
   html=anio('1943', 'La guerra cambia de dirección', 'cambia de direccion'))
sc("En julio, Hitler lanza su última gran ofensiva en el este, en Kursk. Fue una de las mayores batallas de tanques de la historia. Los soviéticos, que sabían lo que se avecinaba, la esperaban con defensas enormes. Desde entonces, en el frente del este, Alemania ya solo retrocede.", T,
   img='kursk', kb='right', cap='Carro Tiger alemán, junio de 1943',
   html='<div class="ov left"><div class="date in" data-t="0.2">Julio de 1943</div><div class="h1 in tw" data-cue="en kursk">Kursk</div>'
        '<div class="h3 in" data-cue="batallas de tanques">Duelo de tanques</div><div class="h3 red in" data-cue="ya solo retrocede" style="margin-top:30px">Alemania ya solo retrocede</div></div>', shade=True)
sc("Ese mismo mes, los aliados desembarcan en Sicilia. El 25 de julio, Mussolini es destituido y detenido. En septiembre, Italia firma el armisticio, pero los alemanes ocupan el país y la lucha en la península se alarga casi dos años más.", I,
   bg='kursk',
   html=timeline([('10 jul.', 'Desembarco en Sicilia', 'en sicilia'), ('25 jul.', 'Cae Mussolini', 'mussolini es destituido'),
                  ('Sept.', 'Armisticio de Italia', 'el armisticio'), ('1943-45', 'Lucha en Italia', 'casi dos anos')], 'Italia'))
sc("Y desde el aire, las ciudades alemanas pagan ahora el precio. Los bombarderos británicos de noche y los estadounidenses de día arrasan Hamburgo, Colonia, Berlín. Decenas de miles de civiles mueren en una sola semana en Hamburgo.", M,
   img='reichstag_ruina', kb='in', shade=True,
   html='<div class="ov center"><div class="h2 in tw" data-cue="las ciudades alemanas">Las ciudades alemanas</div><div class="h3 in" data-cue="arrasan hamburgo">Hamburgo · Colonia · Berlín</div></div>')

# ======================= 1944 =======================
sc("El 6 de junio de 1944 llega el día más esperado: el Día D. Más de 150.000 soldados aliados desembarcan en las playas de Normandía. Es la mayor invasión anfibia de la historia. Con miles de barcos y aviones.", T,
   img='dday', kb='in', cap='Normandía, 6 de junio de 1944', fallback='normandia_playa',
   html='<div class="ov left"><div class="date in" data-t="0.2">6 de junio de 1944</div><div class="h1 in tw" data-cue="el dia d">El Día D</div>'
        '<div class="big amber in" data-cue="mas de 150.000" style="font-size:120px">+150.000</div><div class="h3 in" data-cue="mas de 150.000" data-d="0.4">soldados en un día</div></div>', shade=True)
sc("En la playa de Omaha, los estadounidenses sufrieron muchísimas bajas bajo el fuego de las ametralladoras alemanas. Pero al caer la noche, los aliados habían abierto un frente en Francia. Hitler tenía ahora lo que siempre había temido: una guerra en dos frentes.", T,
   img='normandia_lancha', kb='in', cap='Lancha de desembarco británica abandonada en una playa de Normandía, 1944',
   html='<div class="ov right"><div class="h2 in tw" data-cue="omaha">Omaha</div><div class="h3 red in" data-cue="una guerra en dos frentes" style="margin-top:30px">Guerra en dos frentes</div></div>', shade=True)
sc("Dos semanas después, el Ejército Rojo lanzó la Operación Bagration. En pocas semanas destrozó al Grupo de Ejércitos Centro alemán. Fue una de las peores derrotas de la historia militar alemana, y en España casi nadie la conoce.", T,
   bg='schnee_marsch',
   html='<div class="ov center"><div class="date in" data-t="0.2">22 de junio de 1944</div><div class="h1 in tw" data-cue="operacion bagration">Bagration</div>'
        '<div class="h3 dim in" data-cue="casi nadie la conoce" style="margin-top:30px">La gran desconocida</div></div>')
sc("El 25 de agosto de 1944, París es liberada. Y los primeros soldados en entrar en la ciudad, la noche anterior, fueron españoles: republicanos exiliados de la Nueve, una compañía de la división del general Leclerc. Sus blindados llevaban nombres como Guadalajara, Teruel o Brunete.", I,
   bg='paris_desfile',
   html='<div class="ov center"><div class="date in" data-t="0.2">24-25 de agosto de 1944</div><div class="h1 in tw" data-cue="paris es liberada">París, liberada</div>'
        '<div class="h3 amber in" data-cue="la nueve" style="margin-top:30px">La Nueve: republicanos españoles</div><div class="h3 dim in" data-cue="guadalajara">Guadalajara · Teruel · Brunete</div></div>')
sc("Hubo intentos de acabar con Hitler desde dentro. El 20 de julio de 1944, un oficial, Claus von Stauffenberg, colocó una bomba en su cuartel general. Hitler sobrevivió con heridas leves. La guerra siguió casi un año más, y en ese año murieron millones de personas.", T,
   img='hitler', kb='in', side='right',
   html='<div class="ov left"><div class="date in" data-t="0.2">20 de julio de 1944</div><div class="h2 in tw" data-cue="stauffenberg">Stauffenberg</div>'
        '<div class="h3 red in" data-cue="sobrevivio" style="margin-top:30px">Hitler sobrevive</div></div>')
sc("En diciembre, Hitler lanza un último golpe desesperado en las Ardenas, el mismo bosque de 1940. Tras semanas de combates en la nieve, la ofensiva fracasa. Alemania ha gastado sus últimas reservas.", I,
   img='schnee_marsch', kb='left', shade=True,
   html='<div class="ov center"><div class="date in" data-t="0.2">Diciembre de 1944</div><div class="h2 in tw" data-cue="las ardenas">Las Ardenas, otra vez</div>'
        '<div class="h3 red in" data-cue="la ofensiva fracasa" style="margin-top:30px">Fracaso</div></div>')
sc("En el Pacífico, los estadounidenses avanzan isla por isla hacia Japón. En el golfo de Leyte, en octubre de 1944, se libra una de las mayores batallas navales de la historia. Y aparecen los kamikazes: pilotos japoneses que estrellan sus aviones contra los barcos enemigos.", T,
   bg='iwojima', fallback='schleswig1',
   html='<div class="ov center"><div class="h3 in" data-cue="isla por isla">Isla por isla</div><div class="h2 in tw" data-cue="golfo de leyte">Leyte</div>'
        '<div class="h2 red in" data-cue="kamikazes" style="margin-top:30px">Kamikazes</div></div>')

# ======================= 1945 =======================
sc("Y llegamos a 1945. El 27 de enero, soldados soviéticos llegan a Auschwitz. Encuentran a unos 7.000 prisioneros, la mayoría enfermos y agotados. El mundo empieza a ver con sus propios ojos lo que había ocurrido.", M,
   img='rampa_ninos', kb='in', shade=True, fallback='puerta_birkenau',
   html=anio('1945', '27 de enero: liberación de Auschwitz', 'llegan a auschwitz'))
sc("En febrero, Roosevelt, Churchill y Stalin se reúnen en Yalta, en Crimea, para decidir cómo será Europa después de la guerra. Allí se dibuja el mapa de la posguerra.", I,
   img='yalta', kb='in', cap='Yalta, febrero de 1945: Churchill, Roosevelt y Stalin', fallback='pacto',
   html='<div class="ov left"><div class="date in" data-t="0.2">Febrero de 1945</div><div class="h1 in tw" data-cue="yalta">Yalta</div></div>', shade=True)
sc("En abril, el Ejército Rojo llega a Berlín. Roosevelt muere el 12 de abril, sin ver el final. El 28, Mussolini es fusilado por partisanos italianos. Y el 30 de abril, en su búnker bajo la cancillería, Adolf Hitler se suicida.", T,
   bg='reichstag_ruina',
   html=timeline([('12 abr.', 'Muere Roosevelt', 'roosevelt muere'), ('28 abr.', 'Mussolini, fusilado', 'mussolini es fusilado'),
                  ('30 abr.', 'Hitler se suicida', 'se suicida')], 'Abril de 1945'))
sc("Berlín se rinde el 2 de mayo. Los soldados soviéticos izan su bandera sobre el Reichstag. El 7 de mayo, Alemania firma la rendición incondicional, que entra en vigor el 8. En Europa, la guerra ha terminado.", I,
   img='reichstag_bandera', kb='in', cap='Berlín, mayo de 1945: bandera soviética sobre el Reichstag', fallback='reichstag_ruina',
   html='<div class="ov left"><div class="date in" data-cue="entra en vigor">8 de mayo de 1945</div><div class="h2 in tw" data-cue="rendicion incondicional">Rendición<br>incondicional</div></div>', shade=True)
sc("Pero en el Pacífico seguía. En Iwo Jima y en Okinawa, los japoneses lucharon casi hasta el último hombre. Los mandos estadounidenses calculaban que invadir Japón costaría cientos de miles de vidas aliadas.", T,
   img='iwojima', kb='in', cap='Iwo Jima, febrero de 1945', fallback='midway',
   html='<div class="ov left"><div class="h2 in tw" data-cue="iwo jima">Iwo Jima</div><div class="h2 in tw" data-cue="okinawa">Okinawa</div></div>', shade=True)
sc("El 6 de agosto de 1945, un bombardero estadounidense lanzó sobre Hiroshima la primera bomba atómica usada en una guerra. Tres días después, otra cayó sobre Nagasaki. A finales de año habían muerto en torno a 140.000 personas en Hiroshima y unas 74.000 en Nagasaki.", M,
   img='atomica', kb='in', cap='Las nubes de las bombas de Hiroshima y Nagasaki', fallback='hiroshima_ruinas',
   html='<div class="ov right"><div class="date in" data-t="0.2">6 y 9 de agosto de 1945</div><div class="h2 in tw" data-cue="hiroshima">Hiroshima</div>'
        '<div class="h3 red in" data-cue="140.000">≈ 140.000 muertos</div><div class="h2 in tw" data-cue="nagasaki" style="margin-top:20px">Nagasaki</div><div class="h3 red in" data-cue="74.000">≈ 74.000 muertos</div></div>', shade=True)
sc("Entre las dos bombas, la Unión Soviética declaró la guerra a Japón. El 15 de agosto, el emperador Hirohito habló por radio a su pueblo por primera vez y anunció la rendición. Muchos japoneses nunca habían oído su voz.", M,
   img='hiroshima_ruinas', kb='left', shade=True, fallback='atomica',
   html='<div class="ov center"><div class="date in" data-t="0.2">15 de agosto de 1945</div><div class="h2 in tw" data-cue="hablo por radio">Hirohito<br>habla por radio</div></div>')
sc("Y el 2 de septiembre de 1945, a bordo del acorazado Missouri, en la bahía de Tokio, Japón firmó la rendición. Seis años y un día después de los primeros disparos en Polonia, la Segunda Guerra Mundial había terminado.", M,
   img='rendicion', kb='in', cap='Bahía de Tokio, 2 de septiembre de 1945', fallback='hiroshima_ruinas',
   html='<div class="ov left"><div class="date in" data-t="0.2">2 de septiembre de 1945</div><div class="h2 in tw" data-cue="acorazado missouri">USS Missouri</div>'
        '<div class="h3 amber in" data-cue="habia terminado" style="margin-top:30px">Fin de la guerra</div></div>', shade=True)

# ======================= BALANCE =======================
sc("El precio fue inimaginable. Nadie sabe la cifra exacta, pero la mayoría de estimaciones hablan de más de 60 millones de muertos, y algunas superan los 70. Más que en ninguna otra guerra de la historia.", M,
   bg='varsovia_ruinas',
   html='<div class="ov center"><div class="h3 dim in" data-t="0.3">El balance</div><div class="big red in" data-cue="mas de 60 millones" style="font-size:200px">+60 millones</div>'
        '<div class="h3 in" data-cue="mas de 60 millones" data-d="0.4">de muertos (estimaciones)</div></div>')
sc("La Unión Soviética perdió unos 27 millones de personas. China, millones. Polonia, alrededor de una sexta parte de su población. Y por primera vez en una gran guerra, murieron muchos más civiles que soldados.", M,
   bg='varsovia_ruinas',
   html='<div class="ov center"><div class="row" style="gap:60px">'
        '<div class="box in" data-cue="la union sovietica"><div class="lab">URSS</div><div class="val red">≈ 27 M</div></div>'
        '<div class="box in" data-cue="china"><div class="lab">China</div><div class="val">Millones</div></div>'
        '<div class="box in" data-cue="polonia"><div class="lab">Polonia</div><div class="val">≈ 1/6</div></div></div>'
        '<div class="h3 amber in" data-cue="mas civiles que soldados" style="margin-top:50px">Más civiles que soldados</div></div>')
sc("De sus cenizas nació el mundo en el que todavía vivimos. En octubre de 1945 se fundaron las Naciones Unidas. En noviembre empezaron los juicios de Núremberg contra los jefes nazis. Y Europa quedó partida en dos por lo que Churchill llamó el telón de acero. Empezaba la Guerra Fría.", I,
   bg='reichstag_ruina',
   html='<div class="ov center"><div class="h3 in" data-cue="naciones unidas">1945 · Naciones Unidas</div><div class="h3 in" data-cue="nuremberg">1945 · Juicios de Núremberg</div>'
        '<div class="h2 in tw" data-cue="el telon de acero" style="margin-top:30px">El telón de acero</div><div class="h3 red in" data-cue="la guerra fria">Empieza la Guerra Fría</div></div>')

# ======================= CIERRE =======================
sc("Mirada desde hoy, la Segunda Guerra Mundial parece una sucesión de fechas, mapas y batallas. Pero detrás de cada cifra había una persona. Un soldado de diecinueve años en Stalingrado. Una niña en un tren hacia Auschwitz. Una familia en Hiroshima a las ocho y cuarto de la mañana.", M,
   img='stalingrado_vista', kb='out', shade=True,
   html='<div class="ov center"><div class="h3 in" data-cue="un soldado">Un soldado en Stalingrado</div><div class="h3 in" data-cue="una nina">Una niña camino de Auschwitz</div>'
        '<div class="h3 in" data-cue="una familia">Una familia en Hiroshima</div></div>')
sc("Seis años y un día. Más de 60 millones de historias que se cortaron de golpe. Por eso seguimos contándola. Porque una guerra así no empieza de repente. Empieza cuando demasiada gente decide mirar hacia otro lado.", M,
   img='schleswig1', kb='out', shade=True,
   html='<div class="ov center"><div class="q in" data-cue="mirar hacia otro lado">Empieza cuando demasiada gente<br>decide mirar hacia otro lado.</div></div>')
sc("En el próximo capítulo nos quedamos en el momento que lo cambió todo: la Operación Barbarroja, el mayor error de Hitler. Si no quieres perdértelo, suscríbete. "
   "Y cuéntame en los comentarios: ¿cuál crees que fue el momento decisivo de la guerra?", M,
   bg='vormarsch_panzer',
   html='<div class="ov center"><div class="tag in" data-t="0.2">Próximo capítulo</div><div class="h2 in tw" data-t="0.4">Operación Barbarroja:<br>el mayor error de Hitler</div>'
        '<div class="rule in" data-t="0.6"></div><div class="h3 dim in" data-cue="suscribete">Suscríbete para no perdértelo</div>'
        '<div class="who in" data-cue="suscribete" data-d="1.5" style="font-size:24px;margin-top:80px">Fuentes: Britannica, Imperial War Museum, USHMM, The National WWII Museum, Archivos Nacionales de EE. UU. '
        'Imágenes: Bundesarchiv y Wikimedia Commons (créditos en la descripción).</div></div>')

thumb_img = 'dday' if has('dday') else 'stalingrado_vista'
spec = dict(title='Toda la Segunda Guerra Mundial en 20 minutos', brand='Sombras del 39', voice='hyKxCTlAqtnW188CgltM', model='eleven_v4',
            voice_settings=dict(stability=0.5, similarity_boost=0.75), tail=4, scenes=S,
            thumb={'img': 'img/dday.jpg', 'fy': 0.45, 'l1': 'En 6 años', 'l2': '60 millones', 'l2size': 118, 'l3': 'de muertos'})
json.dump(spec, open(os.path.join(here, 'spec.json'), 'w'), ensure_ascii=False, indent=1)
txt = ' '.join(s['say'] for s in S)
print(len(S), 'escenas ·', len(txt), 'caracteres · ~%.1f min' % (len(txt) / 13.8 / 60), '· sin foto:', [i for i, s in enumerate(S) if 'img' not in s and 'bg' not in s])
open(os.path.join(here, 'guion.txt'), 'w').write('\n\n'.join(s['say'] for s in S) + '\n')
