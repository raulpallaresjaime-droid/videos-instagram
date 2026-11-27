# Lote de febrero 2027 · ejecutar desde la raíz del repo: python3 engine/lotes/2027-02.py
import sys
sys.path.insert(0, "engine")
from nuevo import *

HB = "#finanzaspersonales #bolsa #educacionfinanciera #inversion"

# ───────────── Mar 2 feb · bolsa · moats
guardar("2027-02-02_bolsa_moats", "bolsa", 'Moats: ventajas <span class="c-teal">competitivas</span>', "Moats: ventajas competitivas", [
 hook("¿Por qué tanta gente sigue pagando más por una Coca-Cola que por un refresco de marca blanca que sabe casi igual? Esa pregunta esconde una de las ideas más importantes para invertir.",
      q('¿Por qué pagas <em class="c-orange">más</em><br>por lo mismo?', t=0, style="font-size:64px") + note("Una de las ideas clave para invertir", c="más importantes")),
 portada("bolsa", 'Los <em class="c-teal">moats</em>', "Hoy, en finanzas desde cero: los moats, o ventajas competitivas.", q('Ventajas <em class="c-teal">competitivas</em>', c="ventajas competitivas", style="font-size:46px")),
 esc('Un <em class="c-navy">foso</em> alrededor del castillo', "Moat, en inglés, significa foso: el agua que rodeaba los castillos para que nadie pudiera entrar. Warren Buffett popularizó la idea. En 1999 dijo que la clave para invertir es encontrar la ventaja competitiva de una empresa y, sobre todo, cuánto le va a durar.",
     row(pill("Moat = foso", "navy", c="significa foso", lg=True)) + card("Warren Buffett · Fortune, 1999", 'La clave: la ventaja competitiva… y <em style="color:#7CC4BF">cuánto dura</em>', "", c="la clave para invertir", style="margin-top:40px;width:100%")),
 esc('Por qué <em class="c-orange">importa</em>', "Porque cuando un negocio gana mucho dinero, enseguida llegan competidores a copiarlo. Bajan los precios y los beneficios se evaporan. Una empresa con foso puede seguir ganando mucho durante años, porque a los demás les cuesta entrar.",
     steps(("1", "Un negocio gana mucho", None, "teal", "gana mucho dinero"), ("2", "Llegan competidores", "Bajan los precios", "orange", "llegan competidores"), ("3", "Sin foso: el beneficio se evapora", "Con foso: se defiende durante años", "navy", "se evaporan"))),
 esc('1 · La <em class="c-teal">marca</em>', "El primer foso es la marca. Hay gente que paga más por algo solo por el nombre que lleva. Coca-Cola, Apple o Ferrari pueden cobrar más que sus rivales sin perder clientes.",
     row(pill("Coca-Cola", "sand", c="coca-cola", lg=True), pill("Apple", "sand", c="apple", lg=True), pill("Ferrari", "sand", c="ferrari", lg=True)) + note("Cobran más sin perder clientes", c="sin perder clientes")),
 esc('2 · Lo que cuesta <em class="c-navy">cambiarse</em>', "El segundo, lo que cuesta cambiarse. Si toda una empresa trabaja con un programa, cambiar a otro es caro, lento y arriesgado. Por eso muchos clientes se quedan aunque les suban el precio. Piensa en el software de gestión de una empresa, o en tu propio banco.",
     row(pill("Caro", "orange", c="caro", lg=True), pill("Lento", "orange", c="lento", lg=True), pill("Arriesgado", "orange", c="arriesgado", lg=True)) + card("Resultado", "Los clientes se quedan aunque suba el precio", "navy", c="se quedan", style="margin-top:40px;width:100%")),
 esc('3 · El efecto <em class="c-teal">red</em>', "El tercero, el efecto red: el producto vale más cuanta más gente lo usa. Nadie quiere una red social sin amigos, ni un sistema de pago que no acepta nadie. Por eso Visa, Mastercard o WhatsApp son tan difíciles de desbancar.",
     card("Efecto red", "Más usuarios → más valor → más usuarios", "teal", c="el efecto red") + row(pill("Visa", "sand", c="visa"), pill("Mastercard", "sand", c="mastercard"), pill("WhatsApp", "sand", c="whatsapp"), style="margin-top:40px")),
 esc('4 · Costes más <em class="c-orange">bajos</em>', "Y el cuarto, poder producir más barato que nadie, por tamaño o por eficiencia. Si tú ganas dinero vendiendo al precio al que tu rival pierde, tienes una ventaja enorme. Es lo que hacen Costco o Amazon con su escala.",
     bars(("Tú: coste", "teal", 60, "60 €", "más barato"), ("Tu rival: coste", "orange", 100, "100 €", "tu rival pierde")) + row(pill("Precio de venta: 80 €", "", c="vendiendo al precio", lg=True), style="margin-top:40px") + note("Tú ganas 20 €, tu rival pierde 20 €", c="ventaja enorme"), sub="Ejemplo ilustrativo"),
 esc('¿Cómo se <em class="c-navy">ve</em> en los números?', "¿Y cómo se ve un foso en los números? Una empresa con foso suele tener márgenes altos y estables durante muchos años, y una rentabilidad sobre lo que invierte por encima de la de su sector. Si los márgenes se hunden en cuanto llega un competidor, es que no había foso.",
     steps(("✓", "Márgenes altos y estables", "Durante muchos años", "teal", "márgenes altos"), ("✓", "Rentabilidad sobre lo invertido alta", "Por encima de su sector", "teal", "rentabilidad sobre"), ("✗", "Márgenes que se hunden con la competencia", "No había foso", "orange", "se hunden"))),
 final('No busques solo empresas que ganan mucho. Busca las que pueden <em class="c-teal">seguir haciéndolo</em>.', "No busques solo empresas que ganan mucho. Busca las que pueden seguir haciéndolo.", "Cita: Warren Buffett, Fortune (1999). Empresas citadas como ejemplo."),
], f"""
¿Por qué pagas más por una Coca-Cola que por un refresco de marca blanca? 🏰

Por su «moat», su foso: la ventaja competitiva que la protege de la competencia. Hay cuatro grandes:
🔸 La marca
🔹 Lo que cuesta cambiarse
🔸 El efecto red
🔹 Costes más bajos que nadie

No busques solo empresas que ganan mucho. Busca las que pueden seguir haciéndolo.

Guárdalo y compártelo con quien esté empezando a analizar empresas 📌

{HB} #ventajacompetitiva""")

# ───────────── Jue 4 feb · fondo · WACC
guardar("2027-02-04_fondo_wacc", "fondo", 'El <span class="c-orange">WACC</span>', "El WACC", [
 hook("¿Cuánto le cuesta a una empresa el dinero que usa? Un solo punto de diferencia en esa cifra puede cambiar lo que vale casi un veinte por ciento.",
      q('¿Cuánto le cuesta<br>el <em class="c-orange">dinero</em> a una empresa?', t=0, style="font-size:60px") + row(pill("± 1 punto → valor ± 20 %", "orange", c="un solo punto", lg=True), style="margin-top:40px")),
 portada("fondo", 'El <em class="c-orange">WACC</em>', "Hoy, en finanzas a fondo: el WACC, el coste medio del capital.", q('Coste medio del <em class="c-teal">capital</em>', c="coste medio", style="font-size:46px")),
 esc('Dos tipos de <em class="c-navy">dinero</em>', "Una empresa se financia con dos tipos de dinero. El de los socios, que es el equity, y el de los bancos y los bonistas, que es la deuda. Y ninguno de los dos es gratis.",
     row(card("Equity", "Los socios", "teal", c="de los socios", style="min-width:420px"), card("Deuda", "Bancos y bonistas", "navy", c="la deuda", style="min-width:420px"), style="gap:30px") + note("Ninguno de los dos es gratis", c="ninguno")),
 esc('1 · El coste del <em class="c-teal">equity</em>', "Los socios esperan ganar más que con algo sin riesgo, porque arriesgan más. Se suele calcular con el CAPM: la rentabilidad sin riesgo, más la beta de la empresa por la prima de riesgo del mercado. En nuestro ejemplo, un diez por ciento.",
     row(pill("Ke = Rf + β × prima de mercado", "", c="el capm", lg=True)) + card("Coste del equity (Ke)", "10 %", "teal", c="un diez por ciento", val=True, style="margin-top:40px;width:100%"), sub="Ejemplo ilustrativo"),
 esc('2 · El coste de la <em class="c-navy">deuda</em>', "La deuda es más barata, porque el banco cobra antes que los socios si algo va mal. Además, los intereses se pagan antes de impuestos, así que Hacienda pone una parte. Un préstamo al seis por ciento, con un impuesto del veinticinco, cuesta en realidad un cuatro y medio.",
     bars(("Interés del préstamo", "navy", 100, "6 %", "seis por ciento"), ("Tras impuestos (25 %)", "teal", 75, "4,5 %", "cuatro y medio")) + row(pill("Kd × (1 − t)", "", c="antes de impuestos", lg=True), style="margin-top:40px")),
 esc('3 · Los <em class="c-orange">pesos</em>', "Ahora, los pesos. Imagina un negocio de cien mil euros: setenta y cinco mil los ponen los socios y veinticinco mil los presta el banco. El equity pesa un setenta y cinco por ciento y la deuda, un veinticinco.",
     bars(("Socios · 75 %", "teal", 100, "75.000 €", "setenta y cinco mil"), ("Banco · 25 %", "navy", 33, "25.000 €", "veinticinco mil")), sub="Ejemplo ilustrativo"),
 esc('El <em class="c-orange">WACC</em>', "El WACC es la media ponderada: setenta y cinco por ciento por diez, más veinticinco por ciento por cuatro y medio. Sale un ocho coma seis por ciento. Es la rentabilidad mínima que tiene que conseguir la empresa para que todos los que la financian queden contentos.",
     row(pill("75 % × 10 %", "teal", c="por diez", lg=True), pill("+ 25 % × 4,5 %", "navy", c="por cuatro y medio", lg=True)) + card("WACC", "≈ 8,6 %", "orange", c="ocho coma seis", val=True, style="margin-top:40px;width:100%") + note("La rentabilidad mínima que tiene que conseguir", c="rentabilidad mínima")),
 esc('Por qué importa <em class="c-navy">tanto</em>', "Y aquí está lo importante. En un DCF, los flujos futuros se descuentan al WACC. En el ejemplo de Nova Industrial, bajar el WACC un punto subía el valor un diecinueve por ciento, y subirlo un punto lo bajaba un catorce. Por eso es la cifra que más se discute en cualquier valoración.",
     bars(("WACC − 1 punto", "teal", 100, "+19 %", "subía el valor"), ("WACC + 1 punto", "orange", 74, "−14 %", "lo bajaba")) + note("La cifra que más se discute", c="más se discute"), sub="Nova Industrial · ejemplo de los DCF"),
 esc('El error más <em class="c-orange">común</em>', "Un error típico es usar la deuda neta para calcular los pesos. En empresas con más caja que deuda, eso da pesos absurdos, incluso un WACC negativo. Los pesos se calculan con el valor de mercado del equity y con la deuda bruta.",
     steps(("✗", "Pesos con la deuda neta", "Puede dar un WACC negativo", "orange", "deuda neta"), ("✓", "Valor de mercado del equity + deuda bruta", None, "teal", "valor de mercado"))),
 final('El WACC es el listón: si la empresa no lo <em class="c-teal">supera</em>, <em class="c-orange">destruye valor</em>.', "El WACC es el listón: si la empresa no lo supera, destruye valor.", "Ejemplo ilustrativo."),
], """
¿Cuánto le cuesta a una empresa su dinero? 🧮

Imagina un negocio: 75.000 € los ponen socios que esperan ganar un 10 % y 25.000 € te los presta el banco al 6 %. Tras impuestos, el coste medio de tu dinero ronda el 8,6 %. Eso es el WACC.

🔸 Coste del equity → lo que esperan ganar los socios
🔹 Coste de la deuda → lo que cuesta el préstamo, tras impuestos
🔸 Pesos → qué parte pone cada uno

Un solo punto de WACC puede mover el valor de una empresa casi un 20 %.

Guárdalo para repasar 📌

#finanzas #valoraciondeempresas #inversion #educacionfinanciera #finanzasafondo""")

# ───────────── Dom 7 feb · nadie · regla del 4 %
guardar("2027-02-07_nadie_regla-4", "nadie", NADIE, "La regla del 4 %", [
 hook("Si quieres vivir de rentas con dos mil euros al mes, ¿cuánto dinero necesitas tener invertido? Hay una regla muy famosa que te da la respuesta en un segundo.",
      card("Quieres vivir de rentas con", "2.000 €/mes", "", t=0, val=True) + q('¿Cuánto necesitas <em class="c-teal">invertido</em>?', c="cuánto dinero")),
 portada("nadie", 'La regla del <em class="c-teal">4 %</em>', "Esto es lo que nadie te cuenta sobre la regla del cuatro por ciento."),
 esc('La <em class="c-teal">regla</em>', "La regla dice que puedes retirar cada año un cuatro por ciento de lo que tenías al jubilarte, subiéndolo con la inflación, y que el dinero te durará al menos treinta años. Dicho al revés: necesitas veinticinco veces lo que gastas en un año.",
     row(pill("Retiras un 4 % al año", "teal", c="un cuatro por ciento", lg=True)) + row(pill("+ inflación", "sand", c="con la inflación"), pill("≥ 30 años", "sand", c="treinta años"), style="margin-top:24px") + card("Dicho al revés", "Necesitas × 25 lo que gastas al año", "", c="dicho al revés", style="margin-top:40px;width:100%")),
 esc('Hagamos la <em class="c-orange">cuenta</em>', "Si quieres dos mil euros al mes, son veinticuatro mil al año. Por veinticinco, seiscientos mil euros. Si te basta con mil quinientos al mes, cuatrocientos cincuenta mil.",
     bars(("2.000 €/mes", "teal", 100, "600.000 €", "seiscientos mil"), ("1.500 €/mes", "navy", 75, "450.000 €", "cuatrocientos cincuenta mil")) + row(pill("24.000 €/año × 25", "", c="veinticuatro mil", lg=True), style="margin-top:40px")),
 esc('¿De dónde <em class="c-navy">sale</em>?', "La regla viene de un estudio de 1994 de William Bengen, un asesor financiero de Estados Unidos. Miró los datos históricos de su bolsa y sus bonos, y buscó cuánto podías retirar sin quedarte sin dinero en treinta años, incluso empezando en los peores momentos. En 1998, el llamado estudio Trinity llegó a conclusiones parecidas.",
     steps(("1", "William Bengen · 1994", "Datos históricos de EE. UU.", "navy", "william bengen"), ("2", "Peor momento posible", "El máximo sin quedarte sin dinero en 30 años", "teal", "peores momentos"), ("3", "Estudio Trinity · 1998", "Conclusiones parecidas", "ink", "estudio trinity"))),
 esc('La letra <em class="c-orange">pequeña</em>', "Pero tiene letra pequeña. Está hecha con datos de Estados Unidos, uno de los mercados que mejor ha ido del mundo. Cuando se repitió el cálculo en otros países desarrollados, el cuatro por ciento solo habría aguantado en una minoría. Y Morningstar llegó a calcular una tasa segura de alrededor del tres coma tres.",
     card("Hecha con datos de", "EE. UU.: de los que mejor han ido", "orange", c="datos de estados unidos") + row(pill("Otros países: solo en una minoría", "sand", c="otros países"), style="margin-top:30px") + row(pill("Morningstar: ≈ 3,3 %", "navy", c="tres coma tres", lg=True), style="margin-top:24px")),
 esc('Y lo que no <em class="c-navy">cuenta</em>', "Además, la regla no cuenta ni impuestos ni comisiones. Si pagas un uno y medio por ciento al año en comisiones, te comes buena parte de ese cuatro. Y treinta años se quedan cortos si te retiras a los cincuenta.",
     row(pill("Impuestos ✗", "grey", c="impuestos", lg=True), pill("Comisiones ✗", "grey", c="comisiones", lg=True)) + bars(("Retiras", "teal", 100, "4 %", "te comes"), ("Comisiones", "orange", 38, "1,5 %", "uno y medio"), style="margin-top:40px") + note("Si te retiras a los 50, 30 años se quedan cortos", c="a los cincuenta")),
 esc('Entonces, ¿<em class="c-teal">sirve</em>?', "¿Entonces no sirve? Sí, pero como punto de partida, no como garantía. Es una forma muy rápida de ponerle número a tu objetivo. Y a partir de ahí, ser prudente: retirar algo menos, o gastar menos en los años malos.",
     row(card("Sirve como", "Punto de partida", "teal", c="punto de partida", style="min-width:420px"), card("No es", "Una garantía", "orange", c="no como garantía", style="min-width:420px"), style="gap:30px") + note("Retira algo menos y ajusta en los años malos", c="ser prudente")),
 final('Para vivir de rentas, multiplica lo que gastas por <em class="c-teal">25</em>… y luego sé <em class="c-orange">prudente</em>.', "Para vivir de rentas, multiplica lo que gastas por veinticinco. Y luego, sé prudente.", "Fuentes: Bengen (1994), estudio Trinity (1998), Morningstar. Ejemplos ilustrativos."),
], """
¿Cuánto necesitas para vivir de rentas con 2.000 € al mes? 🤔

La famosa regla del 4 % dice: multiplica lo que gastas al año por 25. Con 24.000 € al año, 600.000 €.

Pero tiene letra pequeña: está hecha con datos de EE. UU., no cuenta impuestos ni comisiones y Morningstar llegó a calcular una tasa segura más cerca del 3,3 %. Úsala como punto de partida, no como garantía.

Guárdalo y compártelo con quien sueñe con vivir de rentas 📌

Contenido educativo, no es recomendación de inversión.

#finanzaspersonales #jubilacion #inversion #educacionfinanciera #loquenadietecuenta""")

# ───────────── Mar 9 feb · bolsa · calidad del beneficio
guardar("2027-02-09_bolsa_calidad-beneficio", "bolsa", 'Calidad del <span class="c-orange">beneficio</span>', "Calidad del beneficio", [
 hook("En 2018, una empresa alemana llegó a valer en bolsa más que el Deutsche Bank. Dos años después reconoció que mil novecientos millones de euros de su caja, probablemente, no existían.",
      card("Empresa alemana · 2018", "Vale más que el Deutsche Bank", "teal", t=0) + row(pill("1.900 M€ que no existían", "orange", c="mil novecientos millones", lg=True), style="margin-top:30px")),
 portada("bolsa", 'Calidad del <em class="c-orange">beneficio</em>', "Hoy, en finanzas desde cero: la calidad del beneficio."),
 esc('No todo beneficio <em class="c-orange">vale</em> igual', "El beneficio que ves en las cuentas no siempre es dinero de verdad. Las normas contables dejan margen para decidir cuándo se apunta un ingreso o un gasto. Por eso, dos empresas que ganan lo mismo pueden ser muy distintas por dentro.",
     row(card("Empresa A", "Gana 100", "teal", c="dos empresas", val=True, style="min-width:400px"), card("Empresa B", "Gana 100", "orange", c="ganan lo mismo", val=True, style="min-width:400px"), style="gap:30px") + note("…y pueden ser muy distintas por dentro", c="por dentro")),
 esc('1 · ¿Se convierte en <em class="c-teal">caja</em>?', "La primera prueba: compara el beneficio con el flujo de caja de las operaciones. Si una empresa gana cien millones, pero su negocio solo genera veinte de caja, año tras año, algo no cuadra. En un negocio sano, la caja suele ser parecida al beneficio, o mayor.",
     bars(("Beneficio", "navy", 100, "100", "gana cien millones"), ("Caja operativa", "orange", 20, "20 ✗", "solo genera veinte")) + note("En un negocio sano, la caja ≈ el beneficio o más", c="negocio sano"), sub="Ejemplo ilustrativo · millones"),
 esc('2 · Lo que no se <em class="c-navy">repite</em>', "La segunda: quita lo extraordinario. Vender un edificio, cobrar una indemnización o un cambio contable pueden inflar un año concreto. Lo que importa es lo que el negocio gana de forma recurrente: lo que se va a repetir el año que viene.",
     row(pill("Venta de un edificio", "sand", c="vender un edificio"), pill("Indemnización", "sand", c="indemnización"), pill("Cambio contable", "sand", c="cambio contable")) + card("Lo que importa", "El beneficio recurrente", "teal", c="recurrente", style="margin-top:40px;width:100%")),
 esc('3 · Clientes que no <em class="c-orange">pagan</em>', "La tercera: mira lo que te deben los clientes. Si las ventas suben un diez por ciento, pero las facturas pendientes de cobro suben un cuarenta, puede que la empresa esté vendiendo a quien no paga, o apuntando ventas antes de tiempo.",
     bars(("Ventas", "teal", 25, "+10 %", "las ventas suben"), ("Pendiente de cobro", "orange", 100, "+40 %", "suben un cuarenta")) + note("¿Vende a quien no paga?", c="a quien no paga"), sub="Ejemplo ilustrativo"),
 esc('El caso <em class="c-orange">Wirecard</em>', "Esa empresa era Wirecard, que llegó a estar en el principal índice de la bolsa alemana. En junio de 2020, su auditora se negó a firmar las cuentas porque no pudo confirmar unos mil novecientos millones de euros que debían estar en bancos de Asia. Días después, la empresa admitió que probablemente no existían, y se declaró insolvente.",
     card("Wirecard · junio de 2020", "La auditora no puede confirmar <em style=\"color:#E8915A\">1.900 M€</em>", "", c="su auditora") + row(pill("“Probablemente no existían”", "orange", c="probablemente no existían", lg=True), style="margin-top:30px") + row(pill("Insolvencia", "", c="insolvente", lg=True), style="margin-top:24px")),
 esc('Las señales de <em class="c-orange">alarma</em>', "Así que desconfía cuando veas beneficios que no se convierten en caja, extraordinarios positivos todos los años, cobros pendientes que crecen más que las ventas, o retrasos en las cuentas y problemas con el auditor.",
     steps(("1", "Beneficio sin caja", None, "orange", "no se convierten"), ("2", "Extraordinarios todos los años", None, "orange", "todos los años"), ("3", "Cobros que crecen más que las ventas", None, "orange", "cobros pendientes"), ("4", "Retrasos y problemas con el auditor", None, "ink", "retrasos"))),
 final('No preguntes solo cuánto gana una empresa. Pregunta cuánto de eso es <em class="c-teal">real</em>.', "No preguntes solo cuánto gana una empresa. Pregunta cuánto de eso es real.", "Caso Wirecard: prensa internacional, junio de 2020. Resto, ejemplos ilustrativos."),
], f"""
Llegó a valer más que el Deutsche Bank… y 1.900 millones de su caja no existían 😳

Fue Wirecard, en 2020. Por eso no basta con mirar cuánto gana una empresa: hay que mirar la calidad de ese beneficio.
🔸 ¿Se convierte en caja?
🔹 ¿Se repite o es extraordinario?
🔸 ¿Los clientes pagan?

No preguntes solo cuánto gana. Pregunta cuánto de eso es real.

Guárdalo y compártelo con quien solo mira el beneficio 📌

{HB} #analisisfundamental""")

# ───────────── Jue 11 feb · fondo · múltiplos
guardar("2027-02-11_fondo_multiplos", "fondo", 'Valoración por <span class="c-teal">múltiplos</span>', "Valoración por múltiplos", [
 hook("¿Cómo sabe un tasador lo que vale tu piso sin abrir ni una hoja de cálculo? Mirando lo que se ha pagado por los de al lado. Con las empresas se hace exactamente igual.",
      q('¿Cómo sabe un tasador<br>lo que <em class="c-teal">vale</em> tu piso?', t=0, style="font-size:60px") + note("Mirando lo que se paga por los de al lado", c="los de al lado")),
 portada("fondo", 'Valoración por <em class="c-teal">múltiplos</em>', "Hoy, en finanzas a fondo: la valoración por múltiplos."),
 esc('Como un <em class="c-navy">tasador</em>', "Si los pisos parecidos de tu barrio se venden a cuatro mil euros el metro, el tuyo de ochenta metros vale unos trescientos veinte mil. Eso es un múltiplo: el precio dividido entre algo que se pueda comparar.",
     row(pill("4.000 €/m²", "sand", c="cuatro mil euros", lg=True), pill("× 80 m²", "sand", c="ochenta metros", lg=True)) + card("Tu piso", "≈ 320.000 €", "navy", c="trescientos veinte mil", val=True, style="margin-top:40px;width:100%") + note("Múltiplo = precio ÷ algo comparable", c="eso es un múltiplo")),
 esc('Los más <em class="c-teal">usados</em>', "En empresas, los más usados son el PER, que compara el precio con el beneficio, y el EV entre EBITDA, que compara el valor de todo el negocio con lo que genera su actividad. El segundo no depende de cuánta deuda tenga la empresa, y por eso es el favorito para comparar.",
     row(card("PER", "Precio ÷ beneficio", "navy", c="el per", style="min-width:420px"), card("EV / EBITDA", "Valor del negocio ÷ EBITDA", "teal", c="ev entre ebitda", style="min-width:420px"), style="gap:30px") + note("EV/EBITDA no depende de la deuda", c="no depende")),
 esc('1 · Compara lo <em class="c-navy">comparable</em>', "La primera regla: compara con empresas parecidas de verdad. Mismo sector, tamaño parecido, crecimiento parecido. Comparar una eléctrica con una tecnológica es como tasar tu piso mirando lo que vale un chalé con piscina.",
     row(pill("Mismo sector", "teal", c="mismo sector"), pill("Tamaño parecido", "teal", c="tamaño parecido"), pill("Crecimiento parecido", "teal", c="crecimiento parecido")) + card("Error", "Eléctrica ↔ tecnológica = piso ↔ chalé con piscina", "orange", c="una eléctrica", style="margin-top:40px;width:100%")),
 esc('2 · Cada sector, su <em class="c-orange">múltiplo</em>', "La segunda: usa el múltiplo adecuado. En los bancos se mira el precio frente a su valor en libros. En empresas de software que aún no ganan dinero, el valor frente a las ventas. Y en las aerolíneas, un EBITDA que incluye el alquiler de los aviones.",
     steps(("B", "Bancos", "Precio ÷ valor en libros", "navy", "los bancos"), ("S", "Software sin beneficios", "Valor ÷ ventas", "teal", "software"), ("A", "Aerolíneas", "EV ÷ EBITDAR (incluye alquiler de aviones)", "orange", "aerolíneas"))),
 esc('3 · La mediana, no la <em class="c-teal">media</em>', "La tercera: usa la mediana, no la media. Imagina cinco comparables que cotizan entre ocho y doce veces su EBITDA, y uno raro a treinta. La media sube a trece coma tres. La mediana se queda en diez y medio. Con un EBITDA de cien millones, esa diferencia infla el valor más de un veinticinco por ciento.",
     cols(("8", "navy", 27, "", "entre ocho"), ("9", "navy", 30, "", "entre ocho"), ("10", "navy", 33, "", "entre ocho"), ("11", "navy", 37, "", "doce veces"), ("12", "navy", 40, "", "doce veces"), ("30", "orange", 100, "el raro", "uno raro"), h=300, w=110) +
     bars(("Media", "orange", 100, "13,3 ×", "la media"), ("Mediana", "teal", 79, "10,5 ×", "la mediana se queda"), style="margin-top:70px") + row(pill("Valor inflado +27 %", "orange", c="más de un veinticinco", lg=True), style="margin-top:30px"), sub="Ejemplo ilustrativo · EV/EBITDA"),
 esc('4 · Un rango, no un <em class="c-navy">número</em>', "Y la cuarta: da un rango, no un número exacto. Los múltiplos te dicen cuánto paga hoy el mercado por negocios parecidos, no cuánto vale de verdad la empresa. Por eso los profesionales los combinan con un DCF.",
     row(card("Múltiplos", "Lo que paga el mercado hoy", "navy", c="los múltiplos te dicen", style="min-width:420px"), card("DCF", "Lo que vale el negocio", "teal", c="un dcf", style="min-width:420px"), style="gap:30px") + row(pill("Un rango, no un número", "", c="un rango", lg=True), style="margin-top:40px")),
 final('Los múltiplos te dicen el <em class="c-navy">precio</em>. El DCF, el <em class="c-teal">valor</em>. Un buen análisis usa los dos.', "Los múltiplos te dicen el precio. El DCF, el valor. Un buen análisis usa los dos.", "Ejemplo ilustrativo."),
], """
¿Cómo saber si una empresa está cara o barata? 🔍

Igual que un tasador con un piso: si los parecidos se venden a 4.000 € el metro, el tuyo de 80 m² vale unos 320.000 €. Con las empresas se hace comparándolas con otras parecidas.

🔸 Compara lo comparable
🔹 Cada sector, su múltiplo
🔸 Usa la mediana, no la media
🔹 Da un rango, no un número

Un solo comparable «raro» puede inflar la valoración más de un 25 %.

Guárdalo para repasar 📌

#finanzas #valoraciondeempresas #inversion #educacionfinanciera #finanzasafondo""")

# ───────────── Dom 14 feb · nadie · hipoteca o invertir
guardar("2027-02-14_nadie_hipoteca-o-invertir", "nadie", NADIE, "¿Amortizar la hipoteca o invertir?", [
 hook("Te sobran diez mil euros. ¿Los usas para amortizar la hipoteca o los inviertes? Es la duda de casi todas las familias. Y la respuesta tiene más matices de lo que parece.",
      card("Te sobran", "10.000 €", "", t=0, val=True) + row(pill("¿Amortizar?", "navy", c="amortizar la hipoteca", lg=True), pill("¿Invertir?", "teal", c="los inviertes", lg=True), style="margin-top:30px")),
 portada("nadie", '¿Amortizar o <em class="c-teal">invertir</em>?', "Esto es lo que nadie te cuenta sobre amortizar la hipoteca o invertir."),
 esc('La cuenta <em class="c-navy">rápida</em>', "La cuenta rápida es comparar dos números. Amortizar te da una rentabilidad segura: el interés que dejas de pagar. Si tu hipoteca está al tres por ciento, amortizar es como ganar un tres por ciento sin riesgo. Invertir puede dar más, pero no está garantizado.",
     bars(("Amortizar", "navy", 43, "3 % seguro", "sin riesgo"), ("Invertir", "teal", 100, "¿7 %? sin garantía", "no está garantizado")), sub="Ejemplo ilustrativo"),
 esc('Hagamos la <em class="c-orange">cuenta</em>', "Con esos diez mil euros, a veinte años vista: amortizar al tres por ciento equivale a tener unos dieciocho mil. Invertirlos, si la bolsa diera un siete de media, unos treinta y ocho mil. Sobre el papel, gana invertir. Pero esa es solo la mitad de la historia.",
     bars(("Amortizar al 3 %", "navy", 47, "≈ 18.000 €", "dieciocho mil"), ("Invertir al 7 %", "teal", 100, "≈ 38.700 €", "treinta y ocho mil")) + note("Solo la mitad de la historia", c="la mitad"), sub="10.000 € · 20 años · ejemplo ilustrativo"),
 esc('Lo que no sale en la <em class="c-orange">cuenta</em>', "Porque la cuenta rápida se deja cosas. Lo que ahorras al amortizar es seguro y no paga impuestos. Lo que ganas invirtiendo sí paga, y la inversión puede caer un treinta por ciento justo cuando más la necesitas.",
     row(card("Amortizar", "Seguro y sin impuestos", "navy", c="es seguro", style="min-width:420px"), card("Invertir", "Paga impuestos y puede caer", "orange", c="sí paga", style="min-width:420px"), style="gap:30px") + row(pill("−30 % justo cuando lo necesitas", "orange", c="treinta por ciento", lg=True), style="margin-top:40px")),
 esc('Cuándo suele tener sentido <em class="c-navy">amortizar</em>', "Amortizar suele tener más sentido si tu hipoteca tiene un tipo alto, si es variable y te quita el sueño, o si vivir sin deudas vale mucho para ti. Y siempre después de pagar otras deudas más caras, como tarjetas o préstamos personales.",
     steps(("1", "Tipo de interés alto", None, "navy", "tipo alto"), ("2", "Variable y te quita el sueño", None, "navy", "te quita el sueño"), ("3", "Vivir sin deudas vale mucho para ti", None, "navy", "sin deudas"), ("!", "Antes: deudas más caras", "Tarjetas, préstamos personales", "orange", "más caras"))),
 esc('Cuándo suele tener sentido <em class="c-teal">invertir</em>', "Invertir suele tener más sentido si tu hipoteca está a un tipo bajo, si tienes muchos años por delante, y si aguantas ver tu inversión en rojo sin vender. Y siempre con un colchón de emergencia aparte.",
     steps(("1", "Tipo de interés bajo", None, "teal", "tipo bajo"), ("2", "Muchos años por delante", None, "teal", "muchos años"), ("3", "Aguantas ver números rojos", None, "teal", "en rojo"), ("✓", "Con un colchón de emergencia aparte", None, "ink", "colchón"))),
 esc('Y no es todo o <em class="c-orange">nada</em>', "Y no tiene por qué ser todo o nada. Mucha gente hace las dos cosas: una parte a amortizar y otra a invertir. Y si amortizas, pregunta si te conviene reducir la cuota o el plazo: reducir el plazo suele ahorrar más intereses.",
     row(pill("Una parte → amortizar", "navy", c="una parte", lg=True), pill("Otra → invertir", "teal", c="otra a invertir", lg=True)) + card("Si amortizas", "Reducir plazo suele ahorrar más intereses", "", c="reducir el plazo", style="margin-top:40px;width:100%")),
 final('No es solo una cuenta: es cuánto <em class="c-orange">riesgo</em> puedes soportar.', "Porque no es solo una cuenta. Es cuánto riesgo puedes soportar.", "Ejemplo ilustrativo; rentabilidades no garantizadas."),
], """
Te sobran 10.000 €: ¿amortizas la hipoteca o inviertes? 🏠

Amortizar al 3 % es como ganar un 3 % seguro y sin impuestos. Invertir puede dar más, pero paga impuestos y puede caer justo cuando lo necesitas. La respuesta depende de tu tipo de interés, de tus años por delante… y de cuánto riesgo soportas.

Y no tiene por qué ser todo o nada.

Guárdalo y compártelo con quien tenga esta duda 📌

Contenido educativo, no es recomendación de inversión.

#finanzaspersonales #hipoteca #inversion #educacionfinanciera #loquenadietecuenta""")

# ───────────── Mar 16 feb · bolsa · value vs growth
guardar("2027-02-16_bolsa_value-vs-growth", "bolsa", 'Value <span class="k">vs</span> <span class="c-teal">growth</span>', "Value vs growth", [
 hook("Hay inversores que solo compran empresas baratas, y otros que pagan lo que haga falta por las que más crecen. ¿Quién gana a largo plazo? Depende mucho de la década que mires.",
      row(card("Value", "Comprar barato", "navy", t=0, style="min-width:400px"), card("Growth", "Comprar crecimiento", "teal", t=0, style="min-width:400px"), style="gap:30px") + q('¿Quién <em class="c-orange">gana</em>?', c="quién gana")),
 portada("bolsa", 'Value vs <em class="c-teal">growth</em>', "Hoy, en finanzas desde cero: value frente a growth."),
 esc('Value: comprar <em class="c-navy">barato</em>', "El value, o inversión en valor, busca empresas que cotizan baratas respecto a lo que ganan o a lo que tienen. Suelen ser negocios maduros, que crecen poco y reparten dividendos: bancos, energéticas, aseguradoras. La idea es comprar un euro pagando setenta céntimos.",
     row(pill("Bancos", "sand", c="bancos"), pill("Energéticas", "sand", c="energéticas"), pill("Aseguradoras", "sand", c="aseguradoras")) + card("La idea", "Comprar 1 € pagando 0,70 €", "navy", c="setenta céntimos", style="margin-top:40px;width:100%")),
 esc('Growth: comprar <em class="c-teal">crecimiento</em>', "El growth, o inversión en crecimiento, busca empresas que aumentan ventas y beneficios muy rápido, aunque coticen caras. Las tecnológicas, por ejemplo. Aquí pagas mucho hoy por lo que esperas que ganen mañana.",
     card("Growth", "Ventas y beneficios que crecen muy rápido", "teal", c="muy rápido") + row(pill("Pagas hoy por lo que ganará mañana", "", c="pagas mucho", lg=True), style="margin-top:40px")),
 esc('Cómo <em class="c-navy">distinguirlos</em>', "Una forma sencilla de distinguirlos es el PER. Una empresa value puede cotizar a diez veces su beneficio. Una growth, a cuarenta. Un PER de cuarenta significa que, si el beneficio no creciera nada, tardarías cuarenta años en recuperar lo pagado. Por eso el growth necesita crecer, y mucho.",
     bars(("Value", "navy", 25, "PER 10", "diez veces"), ("Growth", "teal", 100, "PER 40", "a cuarenta")) + note("PER 40 = 40 años de beneficios si no crece", c="cuarenta años"), sub="Ejemplo ilustrativo"),
 esc('¿Quién <em class="c-orange">gana</em>?', "Durante buena parte del siglo veinte, las acciones baratas lo hicieron mejor que las caras: lo documentaron Eugene Fama y Kenneth French en los años noventa. Pero en la década de 2010, el growth arrasó, empujado por las grandes tecnológicas. Y en 2022, con la subida de los tipos de interés, el value volvió a ganar.",
     steps(("XX", "Siglo XX: gana el value", "Fama y French", "navy", "siglo veinte"), ("10s", "Años 2010: gana el growth", "Grandes tecnológicas", "teal", "década de 2010"), ("22", "2022: vuelve el value", "Subida de tipos", "navy", "en 2022"))),
 esc('La trampa de cada <em class="c-orange">estilo</em>', "Cada estilo tiene su trampa. En el value, la trampa de valor: algo barato que lo es porque el negocio se está muriendo. En el growth, pagar tanto que, aunque la empresa crezca, la acción no suba. Ni lo barato es siempre una ganga, ni lo caro siempre un error.",
     row(card("Trampa del value", "Barato porque se muere", "orange", c="trampa de valor", style="min-width:420px"), card("Trampa del growth", "Pagar demasiado", "orange", c="pagar tanto", style="min-width:420px"), style="gap:30px")),
 esc('¿Hay que <em class="c-teal">elegir</em>?', "¿Hay que elegir? No necesariamente. Un fondo indexado global ya lleva de los dos. Lo importante es saber qué estás comprando y por qué.",
     card("Fondo indexado global", "Value + growth", "teal", c="indexado global") + note("Sabe qué compras y por qué", c="por qué")),
 final('No importa si una acción es barata o cara, sino si <em class="c-teal">vale más</em> de lo que pagas por ella.', "Lo que importa no es si una acción es barata o cara, sino si vale más de lo que pagas por ella.", "Fama y French (1992). Ejemplos ilustrativos."),
], f"""
¿Comprar barato o comprar crecimiento? 🤔

🔸 Value → empresas baratas respecto a lo que ganan (bancos, energéticas…)
🔹 Growth → empresas que crecen muy rápido, aunque coticen caras (tecnológicas)

Cada uno ha tenido sus décadas: el value ganó buena parte del siglo XX, el growth arrasó en los años 2010 y en 2022 volvió el value. Y cada uno tiene su trampa.

Guárdalo y compártelo con quien esté eligiendo su estilo de inversión 📌

{HB} #valueinvesting""")

# ───────────── Jue 18 feb · fondo · ROE, ROA, ROCE, ROIC
guardar("2027-02-18_fondo_roe-roa-roce-roic", "fondo", 'ROE, ROA, ROCE <span class="k">y</span> <span class="c-teal">ROIC</span>', "ROE, ROA, ROCE y ROIC", [
 hook("Dos empresas tienen el mismo ROE: un veinte por ciento. Una es un gran negocio. La otra, una bomba de relojería. ¿Cómo las distingues?",
      row(card("Empresa A", "ROE 20 %", "teal", t=0, val=True, style="min-width:400px"), card("Empresa B", "ROE 20 %", "orange", t=0, val=True, style="min-width:400px"), style="gap:30px") + q('¿Cómo las <em class="c-orange">distingues</em>?', c="cómo las distingues")),
 portada("fondo", 'ROE, ROA, ROCE y <em class="c-teal">ROIC</em>', "Hoy, en finanzas a fondo: ROE, ROA, ROCE y ROIC."),
 esc('Empecemos por un <em class="c-navy">piso</em>', "Imagina que compras un piso de doscientos mil euros poniendo cincuenta mil tuyos, y el resto con una hipoteca al tres por ciento. Lo alquilas y te deja diez mil euros al año. El piso rinde un cinco por ciento. Pero, después de pagar cuatro mil quinientos de intereses, tu dinero rinde un once.",
     bars(("Piso", "navy", 100, "200.000 €", "doscientos mil"), ("Tu dinero", "teal", 25, "50.000 €", "cincuenta mil tuyos")) + row(pill("El piso rinde 5 %", "navy", c="rinde un cinco", lg=True), pill("Tu dinero rinde 11 %", "teal", c="rinde un once", lg=True), style="margin-top:40px"), sub="Ejemplo ilustrativo"),
 esc('1 · <em class="c-teal">ROE</em>', "Eso es el ROE: lo que gana el accionista sobre el dinero que ha puesto. El once por ciento del piso. Y fíjate: la hipoteca lo ha inflado. Con deuda, el ROE sube… pero el riesgo también.",
     card("ROE", "Beneficio ÷ dinero del accionista", "teal", c="lo que gana el accionista") + row(pill("Deuda ↑ → ROE ↑ … y riesgo ↑", "orange", c="el riesgo también", lg=True), style="margin-top:40px")),
 esc('2 · <em class="c-navy">ROA</em>', "El ROA mide lo que rinde todo lo que tiene la empresa, se haya pagado como se haya pagado. Es el cinco por ciento del piso. No se deja engañar por la deuda.",
     card("ROA", "Beneficio ÷ todos los activos", "navy", c="todo lo que tiene") + note("No se deja engañar por la deuda", c="no se deja engañar")),
 esc('3 · ROCE y <em class="c-teal">ROIC</em>', "El ROCE mide lo que rinde el negocio, antes de impuestos, sobre el capital que usa. Y el ROIC, lo mismo después de impuestos, sobre el dinero invertido en el negocio. El ROIC es el más importante: si es mayor que el WACC, la empresa crea valor. Si es menor, lo destruye.",
     row(card("ROCE", "Antes de impuestos", "navy", c="el roce", style="min-width:420px"), card("ROIC", "Después de impuestos", "teal", c="y el roic", style="min-width:420px"), style="gap:30px") +
     steps(("✓", "ROIC > WACC", "Crea valor", "teal", "crea valor"), ("✗", "ROIC < WACC", "Destruye valor", "orange", "lo destruye"), style="margin-top:30px")),
 esc('Mismo ROE, dos <em class="c-orange">historias</em>', "Volvamos al principio. La empresa A tiene un ROE del veinte por ciento con poca deuda: su negocio es muy rentable. La empresa B llega al mismo veinte, pero con cinco veces más deuda que capital propio. Si llega un año malo, la primera aguanta. La segunda puede romperse.",
     bars(("A · deuda", "teal", 20, "× 1", "poca deuda"), ("B · deuda", "orange", 100, "× 5", "cinco veces")) + row(pill("A aguanta", "teal", c="la primera aguanta", lg=True), pill("B puede romperse", "orange", c="puede romperse", lg=True), style="margin-top:40px"), sub="Ejemplo ilustrativo"),
 esc('Para no <em class="c-navy">olvidarlo</em>', "Para no olvidarlo: el ROE, para el accionista. El ROA, para todo lo que tiene la empresa. El ROCE y el ROIC, para saber si el negocio en sí es bueno. Y siempre, mirar cuánta deuda hay detrás.",
     steps(("E", "ROE", "Para el accionista", "teal", "el roe"), ("A", "ROA", "Todo lo que tiene la empresa", "navy", "el roa"), ("I", "ROCE · ROIC", "¿El negocio en sí es bueno?", "ink", "el negocio en sí"))),
 final('El ROE te dice cuánto gana el <em class="c-teal">accionista</em>. El ROIC, si el negocio <em class="c-orange">merece la pena</em>.', "El ROE te dice cuánto gana el accionista. El ROIC, si el negocio merece la pena.", "Ejemplo ilustrativo."),
], """
ROE, ROA, ROCE y ROIC: ¿cuál miras tú? 📊

Los cuatro miden cuánto rinde una empresa, pero cada uno sobre un dinero distinto. Imagina un piso de 200.000 € comprado con 50.000 tuyos: el piso rinde un 5 %, pero tu dinero un 11 %. ¿La diferencia? La hipoteca.

🔸 ROE → lo que gana el accionista
🔹 ROA → lo que rinde todo lo que tiene la empresa
🔸 ROCE y ROIC → si el negocio en sí es bueno

Guárdalo para repasar 📌

#finanzas #analisisfundamental #inversion #educacionfinanciera #finanzasafondo""")

# ───────────── Dom 21 feb · nadie · no invertir solo en tu país
guardar("2027-02-21_nadie_no-solo-tu-pais", "nadie", NADIE, "No invertir solo en tu país", [
 hook("Si hubieras invertido en la bolsa japonesa en su máximo de 1989, ¿cuánto habrías tardado en recuperar tu dinero? Treinta y cuatro años.",
      card("Bolsa japonesa · máximo de 1989", "¿Cuánto tardas en recuperarlo?", "", t=0) + big("34 años", c="treinta y cuatro", cls="c-orange", style="text-align:center;margin-top:40px")),
 portada("nadie", 'No inviertas solo en <em class="c-orange">tu país</em>', "Esto es lo que nadie te cuenta sobre invertir solo en tu país."),
 esc('Japón, <em class="c-orange">1989</em>', "El 29 de diciembre de 1989, el Nikkei, el principal índice de la bolsa japonesa, cerró en casi treinta y nueve mil puntos. Japón parecía imparable. Después llegó el pinchazo: el índice llegó a caer más de un ochenta por ciento, y no volvió a superar aquel máximo hasta febrero de 2024.",
     cols(("38.916", "navy", 100, "dic 1989", "29 de diciembre"), ("7.055", "orange", 18, "mar 2009", "ochenta por ciento"), ("39.099", "teal", 100, "feb 2024", "febrero de 2024"), h=480, w=200) + note("Nikkei 225 · cierre", c="pinchazo", style="margin-top:70px")),
 esc('España, <em class="c-orange">2007</em>', "Y no hace falta irse tan lejos. El IBEX 35 marcó su máximo en noviembre de 2007, cerca de los dieciséis mil puntos. No lo superó hasta octubre de 2025: dieciocho años después. Eso sí, hablamos del índice sin dividendos. Con ellos, la espera habría sido bastante más corta.",
     row(pill("Nov 2007: 15.946", "navy", c="noviembre de 2007", lg=True), pill("Oct 2025: 16.000", "teal", c="octubre de 2025", lg=True)) + big("18 años", c="dieciocho años", cls="c-orange", style="text-align:center;margin-top:30px") + note("Índice sin dividendos", c="sin dividendos")),
 esc('El sesgo <em class="c-navy">local</em>', "Aun así, casi todo el mundo invierte sobre todo en su propio país. Se llama sesgo local: nos fiamos más de las empresas que conocemos. Pero España pesa menos del uno por ciento de la bolsa mundial.",
     card("Sesgo local · home bias", "Invertimos en lo que conocemos", "navy", c="sesgo local") + row(pill("España: < 1 % de la bolsa mundial", "orange", c="menos del uno por ciento", lg=True), style="margin-top:40px")),
 esc('Comprar el <em class="c-teal">mundo</em>', "Por eso, en vez de apostarlo todo a un país, muchos inversores compran el mundo entero con un fondo indexado global. Si a un país le va mal durante una década, otros lo compensan. Así, tu dinero no depende de lo que haga una sola economía, una sola moneda o un solo gobierno.",
     card("Fondo indexado global", "Miles de empresas, decenas de países", "teal", c="el mundo entero") + note("Si a un país le va mal, otros lo compensan", c="otros lo compensan")),
 esc('Pero <em class="c-orange">ojo</em>', "Eso no significa que invertir en tu país sea mala idea. Significa no poner todos los huevos en la misma cesta. Y fíjate en que hoy el riesgo es justo el contrario: la bolsa de Estados Unidos ya pesa más del sesenta por ciento del índice mundial.",
     row(pill("No todos los huevos en la misma cesta", "", c="misma cesta", lg=True)) + bars(("EE. UU.", "navy", 100, "> 60 %", "estados unidos"), ("Resto del mundo", "teal", 60, "< 40 %", "índice mundial"), style="margin-top:40px"), sub="Peso aproximado en el índice mundial"),
 final('Tu país puede tener una década perdida. El mundo entero, es <em class="c-teal">mucho menos probable</em>.', "Tu país puede tener una década perdida. Que la tenga el mundo entero es mucho menos probable.", "Datos: Nikkei 225 e IBEX 35, índices de precios; pesos aproximados."),
], """
Si invertiste en Japón en el máximo de 1989, tardaste 34 años en recuperar tu dinero 😳

Y en España, el IBEX 35 tardó 18 años en superar su máximo de 2007 (sin contar dividendos). Aun así, casi todo el mundo invierte sobre todo en su propio país.

No se trata de no invertir en tu país, sino de no poner todos los huevos en la misma cesta.

Guárdalo y compártelo con quien solo invierta en el IBEX 📌

Contenido educativo, no es recomendación de inversión.

#finanzaspersonales #bolsa #diversificacion #educacionfinanciera #loquenadietecuenta""")

# ───────────── Mar 23 feb · bolsa · cíclicos vs defensivos
guardar("2027-02-23_bolsa_ciclicos-defensivos", "bolsa", 'Cíclicos vs <span class="c-teal">defensivos</span>', "Cíclicos vs defensivos", [
 hook("En 2008, la bolsa de Estados Unidos cayó casi un cuarenta por ciento. Pero algunas empresas apenas lo notaron. ¿Sabes cuáles?",
      big("−38 %", t=0, cls="c-orange", style="text-align:center") + note("S&amp;P 500 · 2008", t=0.3) + q('¿Quién <em class="c-teal">aguantó</em>?', c="sabes cuáles")),
 portada("bolsa", 'Cíclicas vs <em class="c-teal">defensivas</em>', "Hoy, en finanzas desde cero: empresas cíclicas y empresas defensivas."),
 esc('Las <em class="c-orange">cíclicas</em>', "Imagina que la economía va bien. Tienes trabajo, te suben el sueldo y te das caprichos: cenas fuera, viajas, cambias de coche. Las empresas que venden esas cosas son las cíclicas. Cuando la economía crece, ganan mucho. Cuando se frena, son lo primero que recortamos.",
     row(pill("Coches", "orange", c="cambias de coche", lg=True), pill("Viajes", "orange", c="viajas", lg=True), pill("Restaurantes", "orange", c="cenas fuera", lg=True)) +
     steps(("↑", "Economía crece", "Ganan mucho", "teal", "ganan mucho"), ("↓", "Economía se frena", "Lo primero que recortamos", "orange", "lo primero"), style="margin-top:40px")),
 esc('Las <em class="c-teal">defensivas</em>', "Las defensivas venden lo que compras pase lo que pase. Aunque haya crisis, sigues comprando comida, pasta de dientes y medicinas, y sigues pagando la luz. Sus ventas casi no dependen de cómo vaya la economía.",
     row(pill("Comida", "teal", c="comida", lg=True), pill("Higiene", "teal", c="pasta de dientes", lg=True), pill("Salud", "teal", c="medicinas", lg=True), pill("Luz", "teal", c="la luz", lg=True)) +
     note("Venden casi lo mismo con crisis o sin ella", c="casi no dependen")),
 esc('Qué pasó en <em class="c-orange">2008</em>', "Mira lo que pasó en 2008. El S&P 500 cayó un treinta y ocho por ciento. Las empresas de consumo básico, como las de alimentación, cayeron alrededor de un dieciocho. El consumo no básico, como coches o tiendas, más de un treinta y cinco. Y los bancos, más de la mitad.",
     bars(("S&amp;P 500", "navy", 67, "−38 %", "treinta y ocho"), ("Consumo básico", "teal", 32, "≈ −18 %", "dieciocho"), ("Consumo no básico", "orange", 63, "≈ −36 %", "treinta y cinco"), ("Bancos", "orange", 100, "≈ −55 %", "la mitad")), sub="Sectores del S&amp;P 500 · datos aproximados"),
 esc('Pero luego <em class="c-teal">rebotan</em>', "Pero la historia no acaba ahí. En 2009, cuando la bolsa se recuperó, el consumo no básico subió cerca de un cuarenta por ciento. El básico, en torno a un quince. Las cíclicas caen más… pero también rebotan más.",
     cols(("≈ +40 %", "orange", 100, "No básico", "cuarenta por ciento"), ("≈ +15 %", "teal", 38, "Básico", "quince"), h=480, w=260) + note("Rebote de 2009 · datos aproximados", c="rebotan más", style="margin-top:70px")),
 esc('La <em class="c-orange">trampa</em> de las cíclicas', "Y aquí viene la trampa. Una cíclica parece más barata justo en lo mejor del ciclo, cuando gana más que nunca. Su PER es bajísimo… pero porque esos beneficios no van a durar. Muchas veces, el mejor momento para comprarlas es cuando peor pintan.",
     card("PER bajo en lo mejor del ciclo", 'Parece una ganga… y suele ser <em style="color:#E8915A">una trampa</em>', "", c="la trampa") + note("Los beneficios récord no duran", c="no van a durar")),
 esc('¿Y las <em class="c-teal">defensivas</em>?', "Las defensivas tampoco son perfectas. Como crecen menos, en las buenas épocas suelen quedarse atrás. Y si todo el mundo corre a refugiarse en ellas, se pueden poner muy caras. Por eso muchos inversores tienen de los dos tipos.",
     steps(("1", "Crecen menos", "En las buenas épocas se quedan atrás", "navy", "crecen menos"), ("2", "Se pueden poner caras", "Si todos buscan refugio", "orange", "muy caras"), ("3", "Mejor tener de las dos", None, "teal", "de los dos tipos"))),
 final('Las cíclicas te hacen ganar cuando todo va <em class="c-teal">bien</em>. Las defensivas, perder menos cuando va <em class="c-orange">mal</em>.', "Las cíclicas te hacen ganar cuando todo va bien. Las defensivas, perder menos cuando todo va mal.", "Datos aproximados: sectores del S&amp;P 500, 2008-2009 (S&amp;P Dow Jones Indices)."),
], f"""
En 2008 la bolsa de EE. UU. cayó casi un 40 %… pero no todas las empresas igual 📉

🔸 Cíclicas → coches, viajes, bancos: ganan mucho cuando la economía crece y caen fuerte cuando se frena
🔹 Defensivas → comida, salud, luz: venden casi lo mismo pase lo que pase

Ojo con la trampa: una cíclica parece más barata justo cuando más gana.

Guárdalo y compártelo con quien esté empezando a invertir 📌

{HB} #sectores""")

# ───────────── Jue 25 feb · fondo · ratios de deuda
guardar("2027-02-25_fondo_ratios-deuda", "fondo", 'Ratios de <span class="c-teal">deuda</span>', "Ratios de deuda", [
 hook("Una empresa debe trescientos mil euros. ¿Es mucho o es poco? Depende. Y solo hacen falta tres cuentas para saberlo.",
      big("300.000 €", t=0, cls="c-orange", style="text-align:center") + note("de deuda", t=0.3) + q('¿Mucho o <em class="c-teal">poco</em>?', c="mucho o es poco")),
 portada("fondo", 'Ratios de <em class="c-teal">deuda</em>', "Hoy, en finanzas a fondo: los ratios de deuda. ¿Puede una empresa pagar lo que debe?"),
 esc('Café <em class="c-navy">Lumen</em>', "Volvamos a nuestra cafetería inventada, Café Lumen. Debe trescientos mil euros al banco y tiene cincuenta mil en caja. Su EBITDA, lo que genera su negocio antes de intereses, impuestos y amortizaciones, es de cien mil euros al año.",
     row(card("Deuda", "300.000 €", "orange", c="trescientos mil", val=True, style="min-width:280px"), card("Caja", "50.000 €", "teal", c="cincuenta mil", val=True, style="min-width:280px"), card("EBITDA", "100.000 €", "navy", c="cien mil", val=True, style="min-width:280px"), style="gap:20px"), sub="Ejemplo ilustrativo"),
 esc('1 · Deuda neta / <em class="c-teal">EBITDA</em>', "Primera cuenta: la deuda neta, que es la deuda menos la caja, dividida entre el EBITDA. Doscientos cincuenta mil entre cien mil: dos coma cinco veces. Dicho fácil: con todo lo que genera, tardaría unos dos años y medio en pagar su deuda. Como orientación, por encima de tres o cuatro veces, muchos analistas empiezan a preocuparse.",
     card("Deuda neta ÷ EBITDA", "250.000 ÷ 100.000 = 2,5×", "teal", c="dividida entre") + row(pill("≈ 2,5 años para pagarla", "navy", c="dos años y medio", lg=True), pill("&gt; 3-4× → cuidado", "orange", c="preocuparse", lg=True), style="margin-top:40px")),
 esc('2 · Cobertura de <em class="c-navy">intereses</em>', "Segunda: la cobertura de intereses. El beneficio de explotación, el EBIT, dividido entre los intereses que paga. Café Lumen gana setenta mil y paga quince mil de intereses. Los cubre casi cinco veces. Cuanto más alto, más margen tiene si las cosas se tuercen.",
     card("EBIT ÷ intereses", "70.000 ÷ 15.000 ≈ 4,7×", "navy", c="dividido entre") + note("Cuanto más alto, más margen", c="más margen")),
 esc('3 · El <em class="c-teal">DSCR</em>', "Tercera, la que más miran los bancos: el DSCR, la cobertura del servicio de la deuda. Es el EBITDA entre todo lo que hay que pagar en el año: intereses y devolución del préstamo. Café Lumen paga quince mil de intereses y devuelve sesenta mil. Cien mil entre setenta y cinco mil: uno coma tres. Le sobra algo.",
     bars(("EBITDA", "teal", 100, "100.000 €", "es el ebitda"), ("Pagos del año", "orange", 75, "75.000 €", "setenta y cinco mil")) + row(pill("DSCR = 1,33", "teal", c="uno coma tres", lg=True), style="margin-top:40px"), sub="Ejemplo ilustrativo"),
 esc('Ahora, un año <em class="c-orange">malo</em>', "Pero ahora llega un año malo y el EBITDA cae un treinta por ciento, hasta setenta mil. Los pagos siguen siendo setenta y cinco mil. El DSCR baja de uno: ya no le llega para pagar el banco. Y la deuda neta sube a tres coma seis veces el EBITDA. La misma deuda que parecía cómoda, ahora aprieta.",
     bars(("EBITDA", "orange", 93, "70.000 €", "hasta setenta mil"), ("Pagos del año", "navy", 100, "75.000 €", "siguen siendo")) + row(pill("DSCR &lt; 1", "orange", c="baja de uno", lg=True), pill("Deuda neta 3,6×", "orange", c="tres coma seis", lg=True), style="margin-top:40px"), sub="EBITDA −30 %"),
 esc('Para no <em class="c-navy">olvidarlo</em>', "Para no olvidarlo: la deuda neta entre EBITDA te dice cuánto debe. La cobertura, si puede pagar los intereses. Y el DSCR, si puede pagarlo todo. Y haz siempre la prueba del año malo.",
     steps(("1", "Deuda neta / EBITDA", "¿Cuánto debe?", "teal", "cuánto debe"), ("2", "Cobertura de intereses", "¿Paga los intereses?", "navy", "la cobertura"), ("3", "DSCR", "¿Puede pagarlo todo?", "ink", "pagarlo todo"), ("!", "Prueba del año malo", None, "orange", "año malo"))),
 final('La deuda no hunde a una empresa en los años buenos. La hunde en el <em class="c-orange">primer año malo</em>.', "La deuda no hunde a una empresa en los años buenos. La hunde en el primer año malo.", "Ejemplo ilustrativo; los umbrales son orientativos."),
], """
Una empresa debe 300.000 €: ¿es mucho o poco? 🧮

Depende de lo que genere. Con tres cuentas lo sabes:
🔸 Deuda neta / EBITDA → cuántos años tardaría en pagarla
🔹 Cobertura de intereses → si puede pagar los intereses
🔸 DSCR → si puede pagarlo todo: intereses y préstamo

Y haz siempre la prueba del año malo: con un EBITDA un 30 % más bajo, una deuda cómoda puede empezar a apretar.

Guárdalo para repasar 📌

#finanzas #analisisfundamental #inversion #educacionfinanciera #finanzasafondo""")

# ───────────── Dom 28 feb · nadie · Buffett después de los 50
guardar("2027-02-28_nadie_buffett-despues-50", "nadie", NADIE, "Buffett hizo casi toda su fortuna después de los 50", [
 hook("Warren Buffett compró su primera acción con once años. Y aun así, casi toda su fortuna llegó después de cumplir los cincuenta. ¿Cómo es posible?",
      row(pill("11 años · 1.ª acción", "sand", t=0, lg=True)) + big("≈ 99 %", c="casi toda", cls="c-orange", style="text-align:center;margin-top:40px") + note("de su fortuna, después de los 50", c="cincuenta")),
 portada("nadie", 'La fortuna de Buffett llegó <em class="c-orange">después de los 50</em>', "Esto es lo que nadie te cuenta sobre la fortuna de Warren Buffett."),
 esc('El dato de <em class="c-navy">Housel</em>', "Lo cuenta Morgan Housel en su libro La psicología del dinero. Cuando lo escribió, Buffett tenía unos ochenta y cuatro mil quinientos millones de dólares. De ellos, unos ochenta y cuatro mil doscientos los ganó después de cumplir cincuenta años. Y la gran mayoría, después de los sesenta y cinco.",
     cols(("≈ 0,3", "navy", 2, "Antes de los 50", "cuando lo escribió"), ("≈ 84.200", "teal", 100, "Después de los 50", "ochenta y cuatro mil doscientos"), h=480, w=300) + note("Miles de millones de dólares · datos aproximados", c="sesenta y cinco", style="margin-top:70px"), sub="La psicología del dinero, Morgan Housel"),
 esc('No es solo <em class="c-orange">talento</em>', "Buffett es un inversor buenísimo, eso nadie lo duda. Pero lo que de verdad explica su fortuna es otra cosa: lleva más de setenta y cinco años invirtiendo. Como dice Housel, su habilidad es invertir, pero su secreto es el tiempo.",
     card("Morgan Housel", 'Su habilidad es invertir. Su secreto es <em style="color:#7CC4BF">el tiempo</em>.', "", c="su secreto") + row(pill("+75 años invirtiendo", "teal", c="setenta y cinco años", lg=True), style="margin-top:40px")),
 esc('Hagamos la <em class="c-teal">cuenta</em>', "Míralo con números sencillos. Pones diez mil euros a los veinticinco años y te dan un siete por ciento al año. A los treinta y cinco tienes casi veinte mil. A los cuarenta y cinco, casi treinta y nueve mil. A los cincuenta y cinco, unos setenta y seis mil. Y a los sesenta y cinco, casi ciento cincuenta mil.",
     cols(("19.672", "sand", 13, "35 años", "casi veinte mil"), ("38.697", "sand", 26, "45 años", "treinta y nueve"), ("76.123", "navy", 51, "55 años", "setenta y seis"), ("149.745", "teal", 100, "65 años", "ciento cincuenta"), h=480, w=200) + note("10.000 € al 7 % anual · ejemplo ilustrativo", c="siete por ciento", style="margin-top:70px")),
 esc('Lo mejor llega al <em class="c-orange">final</em>', "Fíjate en lo que pasa. En los primeros diez años ganas menos de diez mil euros. En los últimos diez, más de setenta mil. Con el interés compuesto, lo grande siempre llega al final. Por eso lo que más importa no es cuánto ganas cada año, sino cuántos años aguantas.",
     bars(("Primeros 10 años", "sand", 13, "+9.672 €", "primeros diez"), ("Últimos 10 años", "teal", 100, "+73.622 €", "últimos diez")) + note("Lo grande llega al final", c="llega al final", style="margin-top:40px")),
 esc('¿Y si hubiera <em class="c-navy">empezado tarde</em>?', "Housel hace otra cuenta. Si Buffett hubiera empezado a invertir a los treinta y lo hubiera dejado a los sesenta, con la misma rentabilidad, tendría unos doce millones de dólares. Un buen patrimonio, sí. Pero miles de veces menos que su fortuna real.",
     row(card("De los 30 a los 60", "≈ 12 M$", "navy", c="a los treinta", val=True, style="min-width:420px"), card("Fortuna real", "≈ 84.500 M$", "teal", c="fortuna real", val=True, style="min-width:420px"), style="gap:30px"), sub="Cálculo de Morgan Housel · datos aproximados"),
 final('El interés compuesto no premia al más listo. Premia al que <em class="c-teal">más aguanta</em>.', "El interés compuesto no premia al más listo. Premia al que más aguanta.", "Datos aproximados: Morgan Housel, La psicología del dinero (2020)."),
], """
Buffett compró su primera acción con 11 años… y aun así casi toda su fortuna llegó después de los 50 😳

Según Morgan Housel, en «La psicología del dinero», de unos 84.500 millones de dólares, unos 84.200 los ganó después de cumplir 50. Su habilidad es invertir, pero su secreto es el tiempo.

Con el interés compuesto, lo grande siempre llega al final. Lo que más importa no es cuánto ganas cada año, sino cuántos años aguantas.

Guárdalo y compártelo con quien crea que ya es tarde para empezar 📌

Contenido educativo, no es recomendación de inversión.

#finanzaspersonales #interescompuesto #inversion #educacionfinanciera #loquenadietecuenta""")
