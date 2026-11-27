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
     bars(("Socios (equity)", "teal", 100, "75.000 € · 75 %", "setenta y cinco mil"), ("Banco (deuda)", "navy", 33, "25.000 € · 25 %", "veinticinco mil")), sub="Ejemplo ilustrativo"),
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
