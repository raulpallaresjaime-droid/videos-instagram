import sys, math
sys.path.insert(0, "engine")
from nuevo import *

def cue(c=None, t=None, d=None):
    s = ""
    if c is not None: s += f' data-cue="{c}"'
    if t is not None: s += f' data-t="{t}"'
    if d is not None: s += f' data-d="{d}"'
    return s
def pill(txt, cls="", c=None, t=None, d=None, lg=False):
    return f'<span class="pill {cls}{" lg" if lg else ""} in"{cue(c,t,d)}>{txt}</span>'
def row(*items, style=""):
    return f'<div class="row" style="{style}">' + "".join(items) + "</div>"
def col(*items, style=""):
    return f'<div class="col" style="{style}">' + "".join(items) + "</div>"
def card(lab, body, cls="", c=None, t=None, val=False, style="width:100%"):
    inner = f'<div class="val">{body}</div>' if val else f'<div class="txt">{body}</div>'
    return f'<div class="card {cls} in"{cue(c,t)} style="{style}"><div class="lab">{lab}</div>{inner}</div>'
def bars(*items, style=""):
    out = f'<div class="bars" style="{style}">'
    for lab, cls, w, txt, c in items:
        short = " short" if w < 22 else ""
        out += f'<div class="b in"{cue(c)}><span>{lab}</span><i class="{cls} grow{short}" style="--w:{w}%">{txt}</i></div>'
    return out + "</div>"
def cols(*items, h=520, w=170, style=""):
    out = f'<div class="cols" style="height:{h}px;{style}">'
    for b, cls, hh, span, c in items:
        out += f'<div class="c in"{cue(c)} style="width:{w}px"><b>{b}</b><i class="{cls} grow" style="--h:{hh}%"></i><span>{span}</span></div>'
    return out + "</div>"
def steps(*items, style=""):
    out = f'<div class="steps" style="{style}">'
    for n, t, d, cls, c in items:
        out += f'<div class="step {cls} in"{cue(c)}><div class="n">{n}</div><div><div class="t">{t}</div>' + (f'<div class="d">{d}</div>' if d else "") + "</div></div>"
    return out + "</div>"
def q(txt, c=None, t=None, style=""):
    return f'<div class="q in"{cue(c,t)} style="{style}">{txt}</div>'
def note(txt, c=None, t=None, style="margin-top:30px"):
    return f'<div class="note in"{cue(c,t)} style="{style}">{txt}</div>'
def big(txt, c=None, t=None, cls="", style=""):
    return f'<div class="big {cls} in"{cue(c,t)} style="{style}">{txt}</div>'
def esc(title, say, html, sub=None, layout=None):
    e = {"title": title, "say": say, "html": html}
    if sub: e["sub"] = sub
    if layout: e["layout"] = layout
    return e
def hook(say, html): return {"dark": True, "say": say, "html": html}

HB = "#finanzaspersonales #bolsa #educacionfinanciera #inversion"
ILU7 = "Ejemplo ilustrativo: aportaciones mensuales al 7 % anual, rentabilidad no garantizada."

# ───────────── 1. Dom 3 ene · nadie · coste de oportunidad
guardar("2027-01-03_nadie_coste-oportunidad", "nadie", NADIE, "Lo que de verdad te cuesta tu coche", [
 hook("Un paquete de tabaco al día. Unos cinco euros. Parece poco, ¿verdad? Pues en treinta años te puede costar más de ciento setenta y cinco mil euros.",
      big("5 €/día", t=0, cls="c-orange") + q('En 30 años: <em class="c-orange">+175.000 €</em>', c="ciento setenta y cinco")),
 portada("nadie", 'Lo que de verdad te <em class="c-orange">cuesta</em>', "Esto es lo que nadie te cuenta sobre el coste de oportunidad: lo que de verdad te cuestan las cosas."),
 esc('El coste de <em class="c-teal">oportunidad</em>', "Cada euro que gastas tiene dos precios. El que pagas hoy, y en lo que ese euro se podría haber convertido si lo hubieras invertido. Ese segundo precio se llama coste de oportunidad. Y casi nunca lo vemos.",
     row(card("Precio 1", "Lo que pagas hoy", "navy", c="el que pagas", style="min-width:420px"), card("Precio 2", "Lo que dejas de ganar", "orange", c="se podría haber", style="min-width:420px"), style="gap:30px") + note("El que casi nunca vemos", c="casi nunca")),
 esc('1 · El <em class="c-orange">tabaco</em>', "Vamos con los números. Un paquete al día son unos ciento cincuenta euros al mes. Si ese dinero lo invirtieras cada mes durante treinta años, con una rentabilidad del siete por ciento anual, parecida a la media histórica de la bolsa mundial, tendrías más de ciento setenta y cinco mil euros. Y solo habrías puesto cincuenta y cuatro mil.",
     row(pill("150 €/mes · 30 años", "sand", c="ciento cincuenta euros", lg=True)) + bars(("Lo que pones", "ink", 31, "54.000 €", "cincuenta y cuatro mil"), ("Lo que tendrías", "teal", 100, "175.000 €", "tendrías más"), style="margin-top:40px")),
 esc('2 · El <em class="c-navy">coche</em>', "Ahora el coche. Imagina que dudas entre uno de treinta mil euros y otro de quince mil que te lleva igual de bien. La diferencia, quince mil euros, invertida durante treinta años al siete por ciento, se convierte en unos ciento catorce mil.",
     row(card("Coche A", "30.000 €", "navy", c="treinta mil euros", val=True, style="min-width:400px"), card("Coche B", "15.000 €", "teal", c="quince mil que", val=True, style="min-width:400px"), style="gap:30px") +
     col(pill("Diferencia: 15.000 €", "", c="la diferencia", lg=True), f'<span class="arrow in"{cue("invertida")}>↓ 30 años</span>', pill("≈ 114.000 €", "teal", c="ciento catorce", lg=True), style="margin-top:30px")),
 esc('3 · Las <em class="c-orange">suscripciones</em>', "Y lo más silencioso de todo: las suscripciones. Plataformas, el gimnasio que no usas, apps que ni recuerdas. Cincuenta euros al mes no se notan. Invertidos durante treinta años, son unos cincuenta y ocho mil euros.",
     row(pill("Plataformas", "sand", c="plataformas"), pill("Gimnasio", "sand", c="gimnasio"), pill("Apps", "sand", c="apps")) +
     col(pill("50 €/mes", "", c="cincuenta euros al mes", lg=True), f'<span class="arrow in"{cue("invertidos")}>↓ 30 años</span>', pill("≈ 58.000 €", "teal", c="cincuenta y ocho", lg=True), style="margin-top:30px")),
 esc('No es dejar de <em class="c-teal">vivir</em>', "Ojo, que la idea no es dejar de disfrutar. Si algo te hace feliz, adelante. La idea es saber lo que te cuesta de verdad, para decidir tú, y no por inercia. Porque gastar sin pensar sale mucho más caro de lo que parece. Y lo mismo vale para lo pequeño: el café de cada mañana, la comida a domicilio, las compras por impulso.",
     card("La pregunta", '¿Esto me compensa… <em style="color:#7CC4BF">a 30 años vista</em>?', c="saber lo que") + note("Decidir tú, no por inercia", c="por inercia")),
 final('Cada euro que gastas hoy es un euro que <em class="c-teal">no trabaja para ti</em> mañana.', "Porque cada euro que gastas hoy es un euro que no trabaja para ti mañana.", ILU7),
], """
Un paquete de tabaco al día puede costarte más de 175.000 € 😳

No por lo que pagas, sino por lo que dejas de ganar. Se llama coste de oportunidad: 150 € al mes invertidos 30 años al 7 % se convierten en más de 175.000 €. Con el coche o las suscripciones pasa lo mismo.

No se trata de dejar de disfrutar, sino de saber lo que te cuesta de verdad.

Guárdalo y compártelo con quien diga que «son solo cinco euros» 📌

Ejemplo ilustrativo, rentabilidad no garantizada.

#finanzaspersonales #ahorro #inversion #educacionfinanciera #loquenadietecuenta""")

# ───────────── 2. Mar 5 ene · bolsa · balance I
guardar("2027-01-05_bolsa_balance-1", "bolsa", 'El <span class="c-teal">balance</span>', "El balance I", [
 hook("¿Qué tiene una empresa? ¿Y qué debe? Hay un documento que te lo cuenta todo en una sola foto.",
      q('¿Qué <em class="c-teal">tiene</em>…<br>y qué <em class="c-orange">debe</em>?', t=0, style="font-size:64px") + note("En una sola foto", c="una sola foto")),
 portada("bolsa", 'El <em class="c-teal">balance</em>', "Hoy, en finanzas desde cero: el balance."),
 esc('Una <em class="c-navy">foto</em>, no una película', "Si la cuenta de resultados es una película de todo un año, el balance es una foto de un día concreto. Y muestra dos cosas: todo lo que tiene la empresa, y de dónde ha salido el dinero para tenerlo.",
     row(card("Cuenta de resultados", "Una película: todo el año", "navy", c="una película", style="min-width:420px"), card("Balance", "Una foto: un día", "teal", c="una foto", style="min-width:420px"), style="gap:30px") +
     row(pill("Lo que tiene", "sand", c="todo lo que tiene", lg=True), pill("De dónde sale el dinero", "sand", c="de dónde ha salido", lg=True), style="margin-top:40px")),
 esc('Lo que tiene: el <em class="c-navy">activo</em>', "Volvamos a Café Lumen, nuestra cafetería inventada. Lo que tiene se llama activo. La reforma del local y las máquinas, sesenta mil euros. El café y la leche del almacén, cinco mil. Y el dinero en la cuenta, quince mil. En total, ochenta mil euros.",
     bars(("Local y máquinas", "navy", 100, "60.000 €", "sesenta mil"), ("Existencias", "navy", 8, "5.000 €", "cinco mil"), ("Caja", "navy", 25, "15.000 €", "quince mil")) +
     row(pill("Activo: 80.000 €", "navy", c="ochenta mil", lg=True), style="margin-top:40px"), sub="Café Lumen · ejemplo"),
 esc('De dónde sale: el <em class="c-orange">pasivo</em>', "Pero ese dinero tuvo que salir de algún sitio. Una parte se la deben a otros: un préstamo del banco de treinta mil euros, y diez mil que todavía no ha pagado a sus proveedores. Eso es el pasivo: cuarenta mil euros.",
     bars(("Préstamo del banco", "orange", 100, "30.000 €", "un préstamo"), ("Proveedores", "orange", 33, "10.000 €", "diez mil")) +
     row(pill("Pasivo: 40.000 €", "orange", c="eso es el pasivo", lg=True), style="margin-top:40px")),
 esc('Lo de los dueños: el <em class="c-teal">patrimonio neto</em>', "El resto es de los dueños. Los treinta mil euros que pusieron al empezar, más diez mil de beneficios que han ido dejando dentro. Eso es el patrimonio neto: cuarenta mil euros.",
     bars(("Capital inicial", "teal", 100, "30.000 €", "treinta mil euros"), ("Beneficios retenidos", "teal", 33, "10.000 €", "diez mil de beneficios")) +
     row(pill("Patrimonio neto: 40.000 €", "teal", c="patrimonio neto", lg=True), style="margin-top:40px")),
 esc('Por qué siempre <em class="c-teal">cuadra</em>', "Y aquí está la magia: el balance siempre cuadra. Lo que tiene la empresa es exactamente igual a lo que debe, más lo que es de sus dueños. Ochenta mil de activo, igual a cuarenta mil de pasivo más cuarenta mil de patrimonio. Siempre.",
     col(pill("Activo 80.000", "navy", c="ochenta mil de activo", lg=True), f'<span class="arrow in"{cue("igual a cuarenta")}>=</span>', row(pill("Pasivo 40.000", "orange", c="pasivo más", lg=True), f'<span class="arrow in"{cue("pasivo más")}>+</span>', pill("Patrimonio 40.000", "teal", c="de patrimonio", lg=True))) +
     row(pill("Activo = Pasivo + Patrimonio neto", "", c="siempre.", lg=True), style="margin-top:40px")),
 esc('Por qué te <em class="c-orange">importa</em>', "¿Y para qué te sirve? Porque dos empresas pueden ganar lo mismo, pero si una lo hace con mucha deuda y la otra casi sin deber nada, el riesgo no tiene nada que ver. Y eso solo lo ves en el balance. Por eso, cuando analices una empresa, nunca te quedes solo con cuánto gana.",
     row(card("Empresa A", "Casi sin deuda", "teal", c="casi sin deber", style="min-width:420px"), card("Empresa B", "Mucha deuda", "orange", c="mucha deuda", style="min-width:420px"), style="gap:30px") + note("Mismo beneficio, distinto riesgo", c="no tiene nada que ver")),
 final('La cuenta de resultados te dice cuánto <em class="c-teal">gana</em>. El balance, cuánto <em class="c-orange">aguanta</em>.', "La cuenta de resultados te dice cuánto gana una empresa. El balance, cuánto aguanta."),
], f"""
¿Qué tiene una empresa… y qué debe? 🏢

El balance es la foto de un día: lo que tiene la empresa (activo) y de dónde ha salido el dinero para tenerlo (pasivo y patrimonio neto). Y siempre cuadra: activo = pasivo + patrimonio neto.

Te lo explico con Café Lumen, nuestra cafetería inventada.

En mi perfil tienes el carrusel con la explicación completa 👆

Guárdalo y compártelo con quien quiera aprender a leer las cuentas de una empresa 📌

{HB} #balance""")

# ───────────── 3. Jue 7 ene · fondo · duration y convexity
# curva precio-rentabilidad (bono 20 años, cupón 4 %) y tangente en 4 %
def price(y, c=4, n=20): return sum(c/(1+y)**t for t in range(1, n+1)) + 100/(1+y)**n
ys = [0.01 + 0.0025*k for k in range(29)]
W, H = 860, 420
X = lambda y: 40 + (y-0.01)/(0.08-0.01)*(W-80)
pmin, pmax = price(0.08), price(0.01)
Y = lambda p: 30 + (pmax-p)/(pmax-pmin)*(H-80)
curve = "M" + " L".join(f"{X(y):.0f},{Y(price(y)):.0f}" for y in ys)
p0 = price(0.04); dp = (price(0.0401)-price(0.0399))/0.0002
tan = f"M{X(0.015):.0f},{Y(p0+dp*(0.015-0.04)):.0f} L{X(0.075):.0f},{Y(p0+dp*(0.075-0.04)):.0f}"
svg_conv = (f'<svg width="{W}" height="{H+40}" viewBox="0 0 {W} {H+40}">'
 f'<line x1="40" y1="{H-30}" x2="{W-40}" y2="{H-30}" stroke="#cfcabd" stroke-width="3"/>'
 f'<text x="{W-210}" y="{H+5}" font-family="IN" font-size="24" fill="#77766E">tipos de interés →</text>'
 f'<text x="40" y="22" font-family="IN" font-size="24" fill="#77766E">precio</text>'
 f'<path class="draw" data-cue="línea recta" d="{tan}" fill="none" stroke="#B65920" stroke-width="4" stroke-dasharray="12 10"/>'
 f'<text class="in" data-cue="línea recta" x="{X(0.07):.0f}" y="{Y(p0+dp*0.03)+50:.0f}" font-family="IN" font-size="26" font-weight="600" fill="#B65920">duración</text>'
 f'<path class="draw" data-cue="es una curva" d="{curve}" fill="none" stroke="#0C585D" stroke-width="6"/>'
 f'<text class="in" data-cue="es una curva" x="{X(0.017):.0f}" y="{Y(price(0.017))-18:.0f}" font-family="IN" font-size="26" font-weight="600" fill="#0C585D">precio real</text></svg>')
mac = sum(t*4/1.04**t for t in range(1, 11)) + 10*100/1.04**10
mac /= price(0.04, 4, 10)
guardar("2027-01-07_fondo_duration-convexity", "fondo", 'Duration <span class="k">y</span> <span class="c-orange">convexity</span>', "Duration y convexity", [
 hook("En 2022 pasó algo que casi nadie esperaba: los bonos, que se supone que son lo seguro, se hundieron. El gran índice de bonos de Estados Unidos cayó un trece por ciento, su peor año desde 1976. Y los bonos más largos, más de un veinticinco.",
      card("Bonos de EE. UU. · 2022", "−13 %", "orange", t=0, val=True) + q('Su peor año desde <em class="c-orange">1976</em>', c="peor año") + row(pill("Bonos largos: más de −25 %", "orange", c="más de un veinticinco", lg=True), style="margin-top:30px")),
 portada("fondo", 'Duration y <em class="c-orange">convexity</em>', "¿Por qué? Por algo llamado duración. Hoy, en finanzas a fondo: duration y convexity."),
 esc('Ya sabemos el <em class="c-navy">qué</em>', "Ya vimos que cuando los tipos de interés suben, el precio de los bonos baja. La pregunta es cuánto. Y la respuesta depende, sobre todo, de un número: la duración.",
     row(pill("Tipos ↑", "", c="tipos de interés suben", lg=True), f'<span class="arrow in"{cue("el precio")}>→</span>', pill("Precio ↓", "orange", c="el precio", lg=True)) + q('¿<em class="c-navy">Cuánto</em>?', c="cuánto", style="color:#1A1A17") + row(pill("La duración", "navy", c="un número", lg=True), style="margin-top:30px")),
 esc('1 · Macaulay <em class="c-navy">duration</em>', "La duración de Macaulay es, más o menos, cuántos años tardas de media en recuperar tu dinero, contando los cupones y el pago final. Un bono a diez años que paga cupones tiene una duración algo menor que diez, porque parte del dinero lo cobras antes.",
     cols(*[("4", "teal", 8, f"{t}", "contando los cupones") for t in range(1, 10)], ("104", "navy", 100, "10", "el pago final"), h=440, w=70, style="gap:14px") +
     row(pill(f"Duración ≈ {mac:.1f} años".replace(".", ","), "navy", c="algo menor que diez", lg=True), style="margin-top:70px"), sub="Bono a 10 años · cupón del 4 %"),
 esc('2 · Modified <em class="c-orange">duration</em>', "La duración modificada es la que se usa en el día a día, porque te dice cuánto cae el precio si los tipos suben un punto. Con una duración de dos, cae más o menos un dos por ciento. Con una de quince, un quince. Por eso los bonos largos sufrieron tanto en 2022.",
     row(pill("Δ precio ≈ − duración × Δ tipos", "", c="cuánto cae", lg=True)) +
     bars(("Duración 2", "orange", 13, "−2 %", "duración de dos"), ("Duración 7", "orange", 47, "−7 %", "un dos por ciento"), ("Duración 15", "orange", 100, "−15 %", "una de quince"), style="margin-top:40px"), sub="Si los tipos suben un 1 %"),
 esc('3 · <em class="c-teal">Convexity</em>', "Pero esa regla es solo una aproximación en línea recta, y el precio de un bono es una curva. Esa curvatura se llama convexidad, y en un bono normal juega a tu favor: cuando los tipos bajan, el precio sube un poco más de lo que dice la duración, y cuando suben, cae un poco menos.",
     f'<div class="in" data-t="0.2">{svg_conv}</div>' + note("La curva siempre queda por encima de la recta", c="juega a tu favor", style="margin-top:10px")),
 esc('¿Y en la <em class="c-navy">práctica</em>?', "¿Y en la práctica? Los fondos de renta fija publican su duración. Si esperas que los tipos suban, una duración corta te protege. Si crees que van a bajar, una duración larga te hará ganar más. Es tu riesgo de tipos en un solo número. Y recuerda: si aguantas el bono hasta el vencimiento, cobras lo pactado; la duración importa sobre todo si necesitas vender antes.",
     steps(("↑", "Esperas tipos al alza", "Duración corta: te protege", "teal", "duración corta"), ("↓", "Esperas tipos a la baja", "Duración larga: ganas más", "navy", "duración larga"))),
 final('Antes de comprar un bono, mira su <em class="c-orange">duración</em>: es tu riesgo de tipos en un número.', "Antes de comprar un bono, mira su duración: es tu riesgo de tipos en un solo número.", "Datos 2022: Bloomberg US Aggregate. Resto, ejemplo ilustrativo."),
], """
¿Por qué algunos bonos cayeron más que la bolsa en 2022? 📉

Cuando los tipos suben, los bonos bajan. Pero cuánto bajan depende de un número: la duración.
🔸 Macaulay duration → cuándo recuperas tu dinero, de media
🔹 Modified duration → cuánto cae el precio si los tipos suben un 1 %
🔸 Convexity → el ajuste que juega a tu favor

Un bono a 2 años apenas lo nota. Uno con duración 15 puede caer un 15 %.

Guárdalo para repasar 📌

#finanzas #bonos #rentafija #educacionfinanciera #finanzasafondo""")

# ───────────── 4. Dom 10 ene · nadie · revolving
guardar("2027-01-10_nadie_revolving", "nadie", NADIE, "La trampa del pago mínimo de las revolving", [
 hook("Compras algo de mil euros con una tarjeta revolving y pagas veinte euros al mes. Parece cómodo. Pero vas a tardar casi once años en terminar de pagarlo.",
      card("Compra con tarjeta revolving", "1.000 €", "", t=0, val=True) + row(pill("20 €/mes", "sand", c="veinte euros al mes", lg=True), style="margin-top:30px") + q('Casi <em class="c-orange">11 años</em> pagando', c="once años")),
 portada("nadie", 'La trampa del <em class="c-orange">pago mínimo</em>', "Esto es lo que nadie te cuenta sobre la trampa del pago mínimo en las tarjetas revolving."),
 esc('¿Qué es una <em class="c-orange">revolving</em>?', "Una tarjeta revolving es un crédito que se renueva solo. Gastas, y en vez de pagarlo todo a final de mes, devuelves una cuota pequeña. Lo que no pagas sigue generando intereses. Y esos intereses suelen rondar el veinte por ciento al año, o más. Como la cuota es tan cómoda, es muy fácil seguir usándola sin darte cuenta de todo lo que debes.",
     col(pill("Gastas", "sand", c="gastas", lg=True), f'<span class="arrow in"{cue("cuota pequeña")}>↓</span>', pill("Pagas una cuota pequeña", "", c="cuota pequeña", lg=True), f'<span class="arrow in"{cue("sigue generando")}>↓</span>', pill("El resto genera intereses", "orange", c="sigue generando", lg=True)) +
     row(pill("≈ 20 % TAE o más", "orange", c="veinte por ciento", lg=True), style="margin-top:30px")),
 esc('Hagamos la <em class="c-orange">cuenta</em>', "Hagamos la cuenta con un veinticuatro por ciento TAE. Pagando treinta euros al mes, tardas más de cuatro años y pagas unos mil quinientos cincuenta euros. Pagando veinticinco, seis años y unos mil ochocientos. Y pagando veinte, casi once años y más de dos mil seiscientos. Por una compra de mil.",
     bars(("30 €/mes · 4,3 años", "orange", 59, "1.546 €", "pagando treinta"), ("25 €/mes · 6 años", "orange", 68, "1.793 €", "pagando veinticinco"), ("20 €/mes · 11 años", "orange", 100, "2.619 €", "pagando veinte")) +
     row(pill("Compra: 1.000 €", "", c="por una compra", lg=True), style="margin-top:40px"), sub="Ejemplo ilustrativo · 24 % TAE"),
 esc('¿Por qué <em class="c-orange">pasa</em>?', "¿Por qué pasa esto? Porque con una cuota tan baja, casi todo lo que pagas se va en intereses. El primer mes, de tus veinte euros, unos dieciocho son intereses. Y solo dos reducen la deuda.",
     row(card("Tu cuota", "20 €", "", c="el primer mes", val=True, style="min-width:400px")) + bars(("Intereses", "orange", 90, "≈ 18 €", "dieciocho"), ("Reduce la deuda", "teal", 10, "≈ 2 €", "solo dos"), style="margin-top:40px")),
 esc('¿Y esto es <em class="c-navy">legal</em>?', "¿Y esto es legal? Depende. En 2023, el Tribunal Supremo estableció que el interés de estas tarjetas es usurario si supera en más de seis puntos el tipo medio del mercado. Muchos clientes han recuperado dinero en los tribunales. Pero lo mejor es no llegar ahí.",
     card("Tribunal Supremo · 2023", 'Usura si supera en <em style="color:#E8915A">más de 6 puntos</em> el tipo medio', "", c="tribunal supremo") + note("Muchos clientes han recuperado su dinero", c="han recuperado")),
 esc('Cómo <em class="c-teal">evitarla</em>', "Así que, si tienes una revolving: sube la cuota todo lo que puedas, o cámbiala por un préstamo personal más barato para quitártela de encima. Y si no la necesitas, mejor una tarjeta de débito. Y revisa tu contrato: si el interés es muy alto, puede que tengas derecho a reclamar.",
     steps(("1", "Sube la cuota", "Todo lo que puedas", "teal", "sube la cuota"), ("2", "Cámbiala por un préstamo más barato", None, "navy", "préstamo personal"), ("3", "Usa débito", "Si no necesitas crédito", "ink", "tarjeta de débito"))),
 final('Una cuota pequeña <em class="c-orange">no es</em> una deuda pequeña.', "Porque una cuota pequeña no es una deuda pequeña.", "Ejemplo ilustrativo: 24 % TAE, cuota fija. Tribunal Supremo, STS 258/2023."),
], """
Compras algo de 1.000 € con una revolving, pagas 20 € al mes… y tardas casi 11 años en terminar 😬

Con intereses que suelen rondar el 20 % o más, casi toda tu cuota se va en intereses: acabas pagando más de 2.600 € por una compra de 1.000.

Sube la cuota, cámbiala por un préstamo más barato o usa débito.

Guárdalo y compártelo con quien pague «solo el mínimo» 📌

Contenido educativo, no es recomendación de inversión.

#finanzaspersonales #ahorro #deudas #educacionfinanciera #loquenadietecuenta""")

# ───────────── 5. Mar 12 ene · bolsa · balance II
guardar("2027-01-12_bolsa_balance-2", "bolsa", 'El <span class="c-teal">balance</span> II', "El balance II", [
 hook("Una empresa puede tener beneficios… y aun así quebrar porque no puede pagar las facturas del mes que viene. Y el balance te avisa antes de que pase.",
      q('Beneficios…<br>y <em class="c-orange">quiebra</em>', t=0, style="font-size:70px") + note("El balance te avisa antes", c="te avisa")),
 portada("bolsa", 'El balance <em class="c-teal">II</em>', "Hoy, segunda parte del balance: qué mirar para saber si una empresa está sana.", q('Qué mirar', c="qué mirar", style="font-size:46px")),
 esc('Corto y <em class="c-navy">largo plazo</em>', "En el balance, tanto lo que tienes como lo que debes se separa en corto y largo plazo. A corto plazo, lo que se convierte en dinero, o hay que pagar, en menos de un año. A largo plazo, todo lo demás.",
     row(card("Corto plazo", "Menos de un año", "teal", c="en menos de un año", style="min-width:420px"), card("Largo plazo", "Todo lo demás", "navy", c="todo lo demás", style="min-width:420px"), style="gap:30px")),
 esc('1 · ¿Puede pagar el <em class="c-teal">mes que viene</em>?', "Lo primero: ¿puede pagar lo que vence pronto? Compara lo que tiene a corto plazo con lo que debe a corto plazo. Café Lumen tiene veinte mil euros a corto y debe diez mil: cubre sus pagos dos veces. Si tuviera menos de lo que debe, tendría un problema de liquidez.",
     bars(("Tiene a corto", "teal", 100, "20.000 €", "veinte mil"), ("Debe a corto", "orange", 50, "10.000 €", "debe diez mil")) + row(pill("Liquidez: × 2", "teal", c="dos veces", lg=True), style="margin-top:40px"), sub="Café Lumen"),
 esc('2 · ¿Cuánta <em class="c-orange">deuda</em> tiene?', "Lo segundo: cuánto debe frente a lo que han puesto sus dueños. Café Lumen debe cuarenta mil, y su patrimonio es de cuarenta mil: un euro de deuda por cada euro propio. Ni mucho, ni poco. Pero si debiera cinco veces su patrimonio, un mal año podría hundirla.",
     row(pill("Deuda ÷ patrimonio", "", c="cuánto debe", lg=True)) + bars(("Café Lumen", "teal", 20, "× 1", "un euro de deuda"), ("Muy endeudada", "orange", 100, "× 5", "cinco veces"), style="margin-top:40px")),
 esc('3 · ¿Qué hay <em class="c-navy">dentro</em> del activo?', "Y lo tercero: mira qué hay dentro del activo. No es lo mismo tener dinero en el banco que un fondo de comercio, que es lo que una empresa pagó de más al comprar otra. Si esa compra sale mal, ese activo puede desaparecer de un plumazo.",
     row(card("Caja", "Dinero real", "teal", c="dinero en el banco", style="min-width:420px"), card("Fondo de comercio", "Puede evaporarse", "orange", c="fondo de comercio", style="min-width:420px"), style="gap:30px") + note("Lo que se pagó de más al comprar otra empresa", c="pagó de más")),
 esc('Siempre en <em class="c-teal">contexto</em>', "Eso sí, nunca mires un dato suelto. Compáralo con años anteriores y con empresas del mismo sector. Un supermercado y una eléctrica tienen balances muy distintos, y los dos pueden estar perfectamente sanos. Y fíjate en la tendencia: una empresa cuya deuda crece año tras año más rápido que su negocio te está enviando una señal.",
     row(pill("Años anteriores", "sand", c="años anteriores", lg=True), pill("Mismo sector", "sand", c="mismo sector", lg=True)) + row(pill("Supermercado", "navy", c="un supermercado"), pill("Eléctrica", "teal", c="una eléctrica"), style="margin-top:40px")),
 final('Un buen negocio con un mal balance puede <em class="c-orange">no llegar</em> a final de año.', "Porque un buen negocio con un mal balance puede no llegar a final de año."),
], f"""
Una empresa puede tener beneficios… y quebrar 😳

El balance te avisa antes. Tres cosas que mirar:
🔸 ¿Puede pagar lo que vence este año? (liquidez)
🔹 ¿Cuánto debe frente a lo que han puesto sus dueños? (endeudamiento)
🔸 ¿Qué hay dentro del activo? (no es lo mismo caja que fondo de comercio)

Y siempre en contexto: con años anteriores y con su sector.

Guárdalo y compártelo con quien quiera aprender a analizar empresas 📌

{HB} #balance""")

# ───────────── 6. Jue 14 ene · fondo · DCF I
guardar("2027-01-14_fondo_dcf-1", "fondo", 'DCF <span class="c-teal">I</span>', "DCF I", [
 hook("¿Cuánto vale una empresa? No lo que dice la bolsa hoy. Lo que vale de verdad. Hay un método que intenta calcularlo desde cero.",
      q('¿Cuánto <em class="c-teal">vale</em><br>una empresa?', t=0, style="font-size:66px") + note("Desde cero", c="desde cero")),
 portada("fondo", 'DCF <em class="c-teal">I</em>', "Hoy, en finanzas a fondo, primera parte del DCF: el descuento de flujos de caja.", q('Proyectar la <em class="c-teal">caja</em>', c="descuento de flujos", style="font-size:46px")),
 esc('La <em class="c-navy">idea</em>', "La idea es muy sencilla: una empresa vale todo el dinero que va a generar en el futuro, traído a valor de hoy. Así que lo primero es estimar cuánta caja libre le quedará cada año. Lo haremos con Nova Industrial, una empresa inventada.",
     row(pill("Caja futura", "teal", c="va a generar", lg=True), f'<span class="arrow in"{cue("valor de hoy")}>→</span>', pill("Valor de hoy", "navy", c="valor de hoy", lg=True)) + row(card("Empresa inventada", "Nova Industrial", "", c="nova industrial"), style="margin-top:40px")),
 esc('1 · Las <em class="c-navy">hipótesis</em>', "Empezamos por las hipótesis. Nova vende mil millones de euros. Suponemos que crece un ocho por ciento el primer año, y cada vez menos, hasta un cuatro. Un margen EBITDA del veinte por ciento. Amortizaciones del cuatro por ciento de las ventas. Inversión, del cinco. Y un impuesto del veinticinco.",
     steps(("€", "Ventas: 1.000 M€", "Crecen del 8 % al 4 %", "navy", "mil millones"), ("%", "Margen EBITDA: 20 %", None, "teal", "margen ebitda"), ("A", "Amortizaciones: 4 % de ventas", "Inversión (CAPEX): 5 %", "ink", "amortizaciones"), ("T", "Impuesto: 25 %", None, "orange", "un impuesto"))),
 esc('2 · De ventas a <em class="c-teal">EBIT</em>', "Con eso, el primer año vende mil ochenta millones. El EBITDA, el veinte por ciento, son doscientos dieciséis. Le restamos las amortizaciones, cuarenta y tres, y llegamos al EBIT: ciento setenta y tres. Lo que gana el negocio con su actividad.",
     row(pill("Ventas año 1: 1.080 M€", "navy", c="mil ochenta", lg=True)) + bars(("EBITDA", "teal", 100, "216", "doscientos dieciséis"), ("− Amortizaciones", "orange", 20, "43", "cuarenta y tres"), ("= EBIT", "teal", 80, "173", "ciento setenta y tres"), style="margin-top:40px"), sub="Año 1 · millones de euros"),
 esc('3 · De EBIT a <em class="c-teal">caja libre</em>', "Ahora, de beneficio a caja. Al EBIT le quitamos los impuestos y queda el NOPAT: ciento treinta. Le sumamos las amortizaciones, que no son salida de dinero. Le restamos la inversión en activos, cincuenta y cuatro, y lo que crece el circulante, ocho. Resultado: ciento once millones de flujo de caja libre.",
     bars(("NOPAT", "teal", 100, "130", "nopat"), ("+ Amortizaciones", "teal", 33, "43", "le sumamos"), ("− CAPEX", "orange", 42, "54", "cincuenta y cuatro"), ("− Circulante", "orange", 6, "8", "ocho"), ("= FCFF", "navy", 85, "111", "ciento once")), sub="Año 1 · millones de euros"),
 esc('Cinco años de <em class="c-navy">flujos</em>', "Repetimos lo mismo cada año y obtenemos cinco flujos: ciento once, ciento veinte, ciento veintiocho, ciento treinta y cinco y ciento cuarenta y dos millones. Ese es el dinero que la empresa podrá repartir entre todos los que la financian.",
     cols(("111", "navy", 78, "Año 1", "ciento once"), ("120", "navy", 85, "Año 2", "ciento veinte"), ("128", "navy", 90, "Año 3", "veintiocho"), ("135", "navy", 95, "Año 4", "treinta y cinco"), ("142", "navy", 100, "Año 5", "cuarenta y dos"), h=480, w=130) + note("FCFF en millones de euros", c="repartir", style="margin-top:70px")),
 esc('Los <em class="c-orange">sanity checks</em>', "Antes de seguir, toca comprobar que todo tiene sentido. ¿La inversión cubre al menos el desgaste de los activos? ¿El crecimiento es coherente con lo que invierte? Un DCF con números imposibles da valoraciones imposibles.",
     steps(("✓", "CAPEX ≥ amortizaciones", "54 ≥ 43", "teal", "desgaste"), ("✓", "Crecimiento coherente con la inversión", None, "teal", "coherente")) + note("Números imposibles, valoración imposible", c="imposibles")),
 final('Una empresa no vale lo que <em class="c-orange">ganó</em>. Vale lo que va a <em class="c-teal">generar</em>.', "Una empresa no vale lo que ganó. Vale lo que va a generar. En la segunda parte, calculamos cuánto vale Nova, y cada una de sus acciones.", "Empresa inventada. Ejemplo ilustrativo."),
], """
¿Cómo se calcula cuánto vale una empresa? 📊 Parte 1

Una empresa vale el dinero que va a generar en el futuro. Así que lo primero es estimar cuánta caja libre le quedará cada año:
🔸 Las hipótesis: cuánto crece, cuánto gana, cuánto invierte
🔹 De las ventas al EBIT
🔸 Del EBIT al flujo de caja libre (FCFF)

Con Nova Industrial, una empresa inventada. En la parte 2, cuánto vale y cuánto vale cada acción.

Guárdalo para repasar 📌

#finanzas #valoraciondeempresas #inversion #educacionfinanciera #finanzasafondo""")

# ───────────── 7. Dom 17 ene · nadie · TIN o TAE
guardar("2027-01-17_nadie_tin-tae", "nadie", NADIE, "TIN o TAE", [
 hook("Dos préstamos de diez mil euros. Uno al siete por ciento y otro al seis. ¿Cuál es más barato? Spoiler: el del seis te sale más caro.",
      row(card("Préstamo A", "7 %", "navy", t=0, val=True, style="min-width:380px"), card("Préstamo B", "6 %", "teal", t=0, val=True, style="min-width:380px"), style="gap:30px") + q('¿Cuál es más <em class="c-teal">barato</em>?', c="más barato") + row(pill("El del 6 % es más caro", "orange", c="spoiler", lg=True), style="margin-top:30px")),
 portada("nadie", 'TIN o <em class="c-orange">TAE</em>', "Esto es lo que nadie te cuenta sobre el TIN y la TAE."),
 esc('El <em class="c-navy">TIN</em>', "El TIN, el tipo de interés nominal, es solo el precio del dinero: el interés que te cobran por lo que debes. Pero no incluye las comisiones, ni tiene en cuenta cada cuánto te cobran los intereses.",
     card("TIN · tipo de interés nominal", "Solo el precio del dinero", "navy", c="tipo de interés nominal") + row(pill("Comisiones ✗", "grey", c="comisiones", lg=True), pill("Frecuencia de pago ✗", "grey", c="cada cuánto", lg=True), style="margin-top:40px")),
 esc('La <em class="c-teal">TAE</em>', "La TAE, la tasa anual equivalente, lo mete todo: el interés, la frecuencia de los pagos y las comisiones obligatorias. Por eso es el número que sirve para comparar. Y el banco está obligado a dártela.",
     card("TAE · tasa anual equivalente", "Lo mete todo", "teal", c="tasa anual equivalente") + row(pill("Interés ✓", "teal", c="el interés"), pill("Frecuencia ✓", "teal", c="la frecuencia"), pill("Comisiones ✓", "teal", c="comisiones obligatorias"), style="margin-top:40px") + note("El número para comparar", c="para comparar")),
 esc('La frecuencia también <em class="c-navy">cuenta</em>', "Y la frecuencia también cuenta. Un siete por ciento que se cobra una vez al año es un siete. Pero si se cobra cada mes, los intereses de un mes generan intereses al mes siguiente, y la TAE sube al siete coma veintitrés. Por eso dos préstamos con el mismo TIN pueden tener distinta TAE.",
     bars(("TIN 7 % · pago anual", "navy", 97, "TAE 7,00 %", "una vez al año"), ("TIN 7 % · pago mensual", "teal", 100, "TAE 7,23 %", "siete coma veintitrés")) + note("Mismo TIN, distinta TAE", c="mismo tin")),
 esc('Hagamos la <em class="c-orange">cuenta</em>', "Vamos con los dos préstamos, a tres años. El A, al siete por ciento y sin comisiones, tiene una TAE del siete coma dos. El B, al seis por ciento, pero con una comisión de apertura del tres por ciento: trescientos euros que pagas al principio. Su TAE sube al ocho coma cuatro.",
     row(card("A · TIN 7 % · sin comisión", "TAE 7,23 %", "teal", c="el a,", val=True, style="min-width:430px"), card("B · TIN 6 % + 3 % comisión", "TAE 8,36 %", "orange", c="ocho coma cuatro", val=True, style="min-width:430px"), style="gap:24px") +
     row(pill("Comisión: 300 €", "orange", c="trescientos euros", lg=True), style="margin-top:40px"), sub="10.000 € · 3 años · ejemplo ilustrativo"),
 esc('Lo que pagas de <em class="c-orange">verdad</em>', "En total, con el A pagas mil ciento dieciséis euros de intereses. Con el B, entre intereses y comisión, mil doscientos cincuenta y dos. El préstamo con el interés más bajo es el más caro.",
     bars(("Préstamo A", "teal", 89, "1.116 €", "mil ciento dieciséis"), ("Préstamo B", "orange", 100, "1.252 €", "doscientos cincuenta y dos")) + note("Coste total en 3 años", c="el préstamo con")),
 esc('Y la letra <em class="c-orange">pequeña</em>', "Y pregunta siempre por los productos vinculados, como seguros que te obligan a contratar para darte un tipo mejor, porque pueden encarecerlo. Lo más claro de todo: pide el coste total del préstamo, en euros.",
     steps(("1", "Compara la TAE", None, "teal", "pregunta siempre"), ("2", "Ojo con los productos vinculados", "Seguros obligatorios para mejorar el tipo", "orange", "productos vinculados"), ("3", "Pide el coste total en euros", None, "navy", "coste total"))),
 final('Para comparar, mira la <em class="c-teal">TAE</em>. Para decidir, mira el <em class="c-orange">coste total</em>.', "Para comparar préstamos, mira la TAE. Para decidir, mira el coste total.", "Ejemplo ilustrativo: 10.000 €, 36 meses."),
], """
Un préstamo al 6 % puede salirte más caro que uno al 7 % 🤔

El TIN es solo el interés. La TAE lo mete todo: interés, frecuencia de pago y comisiones obligatorias. Con una comisión de apertura del 3 %, un préstamo al 6 % acaba con una TAE del 8,36 %.

Para comparar, mira la TAE. Para decidir, el coste total en euros.

Guárdalo para la próxima vez que pidas un préstamo 📌

#finanzaspersonales #prestamos #ahorro #educacionfinanciera #loquenadietecuenta""")

# ───────────── 8. Mar 19 ene · bolsa · flujo de caja
guardar("2027-01-19_bolsa_flujo-caja", "bolsa", 'El <span class="c-teal">flujo de caja</span>', "El flujo de caja", [
 hook("Una empresa puede ganar dinero todos los años… y quedarse sin un euro en la cuenta. Parece imposible, pero pasa mucho más de lo que crees.",
      q('Gana dinero…<br>y se queda <em class="c-orange">sin un euro</em>', t=0, style="font-size:62px")),
 portada("bolsa", 'El flujo de <em class="c-teal">caja</em>', "Hoy, en finanzas desde cero: el estado de flujos de caja."),
 esc('Beneficio no es <em class="c-orange">dinero</em>', "La cuenta de resultados apunta las ventas cuando se hacen, no cuando se cobran. Si Café Lumen sirve un catering de cinco mil euros a una empresa que paga a noventa días, hoy ya cuenta como beneficio. Pero el dinero todavía no está en la cuenta. Y si ese cliente no paga nunca, el beneficio se queda en el papel.",
     row(card("Venta: 5.000 €", "✓ Ya es beneficio", "teal", c="cuenta como beneficio", style="min-width:420px"), card("Cobro: en 90 días", "✗ Aún no hay dinero", "orange", c="todavía no está", style="min-width:420px"), style="gap:30px"), sub="Café Lumen · ejemplo"),
 esc('Las tres <em class="c-navy">partes</em>', "El estado de flujos de caja cuenta el dinero que entra y sale de verdad, y lo separa en tres partes. La operativa: lo que genera el negocio del día a día. La de inversión: lo que se gasta en máquinas o en comprar otras empresas. Y la de financiación: préstamos, devoluciones y dividendos.",
     steps(("1", "Operativa", "El negocio del día a día", "teal", "la operativa"), ("2", "Inversión", "Máquinas, otras empresas…", "navy", "la de inversión"), ("3", "Financiación", "Préstamos, devoluciones, dividendos", "ink", "la de financiación"))),
 esc('Lo que quieres <em class="c-teal">ver</em>', "Lo ideal es una empresa cuyo negocio genera caja, que usa parte de esa caja para invertir, y que con lo que le sobra devuelve deuda o paga dividendos. Operativa positiva, inversión negativa y financiación negativa.",
     row(pill("Operativa +", "teal", c="operativa positiva", lg=True), pill("Inversión −", "navy", c="inversión negativa", lg=True), pill("Financiación −", "ink", c="financiación negativa", lg=True)) + note("El negocio se paga a sí mismo", c="devuelve deuda")),
 esc('La señal de <em class="c-orange">alarma</em>', "La alarma salta al revés: cuando el negocio no genera caja y la empresa vive de pedir prestado o de emitir acciones nuevas. Puede aguantar un tiempo, pero si se cierra el grifo de la financiación, se acabó. Le ha pasado a muchas empresas que, sobre el papel, ganaban dinero.",
     row(pill("Operativa −", "orange", c="no genera caja", lg=True), pill("Financiación +", "orange", c="pedir prestado", lg=True)) + note("Vive del dinero de otros", c="emitir acciones") + row(pill("Se cierra el grifo → se acabó", "", c="se cierra el grifo", lg=True), style="margin-top:30px")),
 esc('El flujo de caja <em class="c-teal">libre</em>', "Y de aquí sale el número favorito de muchos inversores: el flujo de caja libre. La caja que genera el negocio, menos lo que necesita invertir para mantenerse y crecer. Es el dinero que de verdad queda, y el más difícil de maquillar.",
     bars(("Caja operativa", "teal", 100, "100", "la caja que genera"), ("− Inversión", "orange", 40, "40", "necesita invertir"), ("= Caja libre", "navy", 60, "60", "de verdad queda")) + note("El más difícil de maquillar", c="maquillar"), sub="Ejemplo ilustrativo"),
 final('El beneficio es una <em class="c-orange">opinión</em>. La caja es un <em class="c-teal">hecho</em>.', "Porque, como se dice en finanzas, el beneficio es una opinión, pero la caja es un hecho."),
], f"""
Una empresa puede ganar dinero… y quedarse sin un euro 😳

Porque beneficio no es lo mismo que dinero. El estado de flujos de caja cuenta el dinero que entra y sale de verdad:
🔸 Operativa → lo que genera el negocio
🔹 Inversión → máquinas, otras empresas…
🔸 Financiación → préstamos y dividendos

El beneficio es una opinión. La caja es un hecho.

Guárdalo y compártelo con quien quiera aprender a analizar empresas 📌

{HB} #flujodecaja""")

# ───────────── 9. Jue 21 ene · fondo · DCF II
guardar("2027-01-21_fondo_dcf-2", "fondo", 'DCF <span class="c-teal">II</span>', "DCF II", [
 hook("La semana pasada proyectamos la caja de Nova Industrial para cinco años. Ahora, la pregunta del millón: ¿cuánto vale la empresa? ¿Y cada acción?",
      cols(("111", "navy", 78, "A1", None), ("120", "navy", 85, "A2", None), ("128", "navy", 90, "A3", None), ("135", "navy", 95, "A4", None), ("142", "navy", 100, "A5", None), h=320, w=110).replace('class="c in"', 'class="c in" data-t="0"') + q('¿Cuánto <em class="c-teal">vale</em>?', c="la pregunta del millón", style="margin-top:70px")),
 portada("fondo", 'DCF <em class="c-teal">II</em>', "Hoy, en finanzas a fondo, segunda parte del DCF."),
 esc('1 · Traer el dinero a <em class="c-navy">hoy</em>', "Un euro dentro de cinco años vale menos que un euro hoy. Así que cada flujo se descuenta al WACC, el coste medio del dinero de la empresa, que para Nova es del ocho coma tres por ciento. Los cinco flujos, traídos a hoy, suman unos cuatrocientos noventa y nueve millones.",
     row(pill("÷ (1 + 8,3 %) ^ año", "", c="se descuenta", lg=True)) + card("Valor hoy de los 5 flujos", "499 M€", "navy", c="cuatrocientos noventa", val=True, style="margin-top:40px;width:100%"), sub="WACC de Nova: 8,3 %"),
 esc('2 · El valor <em class="c-teal">terminal</em>', "Pero la empresa no se acaba en el año cinco. Para todo lo que viene después se calcula el valor terminal: suponemos que, a partir de ahí, los flujos crecen un dos por ciento para siempre. Eso da unos dos mil trescientos millones en el año cinco, que traídos a hoy son unos mil quinientos cuarenta.",
     row(pill("FCF año 6 ÷ (WACC − g)", "", c="valor terminal", lg=True)) + row(pill("g = 2 % para siempre", "sand", c="para siempre", lg=True), style="margin-top:24px") +
     bars(("En el año 5", "teal", 100, "2.299 M€", "dos mil trescientos"), ("Traído a hoy", "teal", 67, "1.543 M€", "mil quinientos cuarenta"), style="margin-top:40px")),
 esc('3 · El <em class="c-navy">Enterprise Value</em>', "Sumamos las dos partes y tenemos el Enterprise Value: unos dos mil cuarenta y dos millones. Y fíjate en algo: el setenta y seis por ciento del valor viene del valor terminal. De lo que pasará después del año cinco.",
     bars(("Flujos años 1 – 5", "navy", 24, "499", "sumamos"), ("Valor terminal", "teal", 76, "1.543", "las dos partes"), ("Enterprise Value", "navy", 100, "2.042 M€", "dos mil cuarenta y dos")) + row(pill("76 % = valor terminal", "orange", c="setenta y seis", lg=True), style="margin-top:40px")),
 esc('4 · Del EV al <em class="c-teal">precio por acción</em>', "Ahora le restamos la deuda neta, trescientos millones, y queda el valor para los accionistas: mil setecientos cuarenta y dos. Nova tiene cincuenta millones de acciones. Así que cada una vale unos treinta y cuatro euros con ochenta. Y si hubiera opciones sobre acciones o bonos convertibles, habría que contar también esas acciones nuevas.",
     bars(("Enterprise Value", "navy", 100, "2.042", "le restamos"), ("− Deuda neta", "orange", 15, "300", "trescientos millones"), ("= Equity Value", "teal", 85, "1.742", "setecientos cuarenta y dos")) +
     row(pill("÷ 50 M acciones", "", c="cincuenta millones de acciones", lg=True), pill("34,8 €/acción", "teal", c="treinta y cuatro euros", lg=True), style="margin-top:40px"), sub="Millones de euros"),
 esc('5 · La <em class="c-orange">sensibilidad</em>', "Y ahora lo importante. Si el WACC fuera un punto más bajo, el valor subiría un diecinueve por ciento. Si fuera un punto más alto, bajaría un catorce. Por eso un DCF nunca da un número exacto, sino un rango.",
     bars(("WACC 7,3 %", "teal", 100, "42,7 € (+19 %)", "más bajo"), ("WACC 8,3 %", "navy", 82, "34,8 €", "ahora lo importante"), ("WACC 9,3 %", "orange", 68, "29,1 € (−14 %)", "más alto")) + note("Un rango, no un número", c="un rango"), sub="Precio por acción"),
 final('Un DCF no te da el precio exacto. Te dice <em class="c-teal">de qué depende</em>.', "Un DCF no te da el precio exacto. Te dice de qué depende.", "Empresa inventada. Ejemplo ilustrativo."),
], """
¿Cuánto vale Nova Industrial? 📊 Parte 2

Descontamos sus flujos al WACC (8,3 %), calculamos el valor terminal y pasamos del Enterprise Value al precio por acción: 34,8 €.

Pero ojo: el 76 % del valor viene del valor terminal, y con ±1 punto de WACC el precio se mueve entre un −14 % y un +19 %. Por eso un DCF da un rango, no un número.

Guárdalo para repasar 📌

#finanzas #valoraciondeempresas #inversion #educacionfinanciera #finanzasafondo""")

# ───────────── 10. Dom 24 ene · nadie · lotería
guardar("2027-01-24_nadie_loteria", "nadie", NADIE, "Lotería o invertir", [
 hook("Diez euros a la semana en el Euromillones, durante treinta años. ¿Sabes cuánto tendrías si los hubieras invertido? Más de cincuenta mil euros.",
      card("Euromillones", "10 €/semana", "", t=0, val=True) + q('Invertidos 30 años: <em class="c-teal">+50.000 €</em>', c="cincuenta mil")),
 portada("nadie", 'Lotería o <em class="c-teal">invertir</em>', "Esto es lo que nadie te cuenta sobre la lotería."),
 esc('Las <em class="c-orange">probabilidades</em>', "Empecemos por las probabilidades. Para ganar el bote del Euromillones tienes que acertar cinco números y dos estrellas. La probabilidad es de una entre casi ciento cuarenta millones.",
     row(pill("5 números", "sand", c="cinco números", lg=True), pill("2 estrellas", "sand", c="dos estrellas", lg=True)) + big("1 entre<br>139.838.160", c="una entre", cls="c-orange", style="font-size:80px;text-align:center;margin-top:40px")),
 esc('Para que te hagas una <em class="c-navy">idea</em>', "Para que te hagas una idea: si jugaras una apuesta en cada sorteo, dos a la semana, tardarías de media más de un millón de años en que te tocara.",
     row(pill("1 apuesta × 2 sorteos/semana", "sand", c="dos a la semana", lg=True)) + big("+1.000.000<br>de años", c="un millón de años", cls="c-navy", style="font-size:90px;text-align:center;margin-top:40px")),
 esc('Lo que <em class="c-orange">pones</em>', "Ahora, los números de verdad. Cada apuesta cuesta dos euros con cincuenta. Cuatro apuestas a la semana son diez euros. Y en treinta años, habrás puesto quince mil seiscientos euros.",
     row(pill("2,50 € por apuesta", "sand", c="dos euros con cincuenta", lg=True), pill("× 4 = 10 €/semana", "", c="cuatro apuestas", lg=True)) + card("En 30 años", "15.600 €", "orange", c="quince mil seiscientos", val=True, style="margin-top:40px;width:100%")),
 esc('Lo que podrías <em class="c-teal">tener</em>', "Si esos diez euros a la semana los invirtieras, con una rentabilidad del siete por ciento anual, parecida a la media histórica de la bolsa mundial, en treinta años tendrías unos cincuenta mil euros. Y eso no depende de la suerte. Depende del tiempo.",
     bars(("Lo que pones", "ink", 31, "15.600 €", "si esos diez"), ("Invertido al 7 %", "teal", 100, "≈ 50.700 €", "cincuenta mil")) + note("No depende de la suerte, sino del tiempo", c="depende del tiempo"), sub=ILU7.replace("Ejemplo ilustrativo: ", "")),
 esc('¿Quién gana <em class="c-orange">siempre</em>?', "¿Y sabes quién gana siempre? Quien organiza el juego. De cada euro que se apuesta, una buena parte nunca vuelve a los jugadores en forma de premios. Por eso, a la larga, el jugador medio siempre pierde. Y la probabilidad es la misma hayas jugado diez años o ninguno: el sorteo no tiene memoria.",
     card("Quien siempre gana", "El que organiza el juego", "", c="quien organiza") + note("A la larga, el jugador medio pierde", c="siempre pierde") + row(pill("El sorteo no tiene memoria", "orange", c="no tiene memoria", lg=True), style="margin-top:30px")),
 esc('Soñar no está <em class="c-navy">prohibido</em>', "Ojo, jugar de vez en cuando por ilusión no es ningún drama. El problema es jugar todas las semanas como si fuera un plan para salir adelante. Porque el plan más fiable para ganar dinero no es el que más promete, sino el que más tiempo tiene.",
     row(card("Por ilusión", "De vez en cuando, ✓", "teal", c="por ilusión", style="min-width:420px"), card("Como plan", "Cada semana, ✗", "orange", c="como si fuera un plan", style="min-width:420px"), style="gap:30px") + note("El mejor plan es el que más tiempo tiene", c="más tiempo tiene")),
 final('La lotería depende de la <em class="c-orange">suerte</em>. Invertir, del <em class="c-teal">tiempo</em>.', "La lotería depende de la suerte. Invertir, del tiempo.", "Probabilidad: Euromillones (5 + 2). " + ILU7),
], """
Ganar el bote del Euromillones: 1 entre 139.838.160 🎰

Jugando una apuesta en cada sorteo, tardarías de media más de un millón de años. En cambio, esos 10 € a la semana invertidos 30 años al 7 % se convierten en unos 50.000 €.

La lotería depende de la suerte. Invertir, del tiempo.

Guárdalo y compártelo con quien juegue «por si acaso» cada semana 📌

Ejemplo ilustrativo, rentabilidad no garantizada.

#finanzaspersonales #ahorro #inversion #educacionfinanciera #loquenadietecuenta""")

# ───────────── 11. Mar 26 ene · bolsa · resultados trimestrales
guardar("2027-01-26_bolsa_resultados-trimestrales", "bolsa", 'Resultados <span class="c-orange">trimestrales</span>', "Cómo leer los resultados trimestrales", [
 hook("Una empresa presenta resultados récord… y al día siguiente su acción cae un diez por ciento. ¿Cómo puede ser?",
      card("Resultados", "Récord ✓", "teal", t=0, val=True) + row(pill("Acción: −10 %", "orange", c="cae un diez", lg=True), style="margin-top:30px") + q('¿Cómo puede <em class="c-orange">ser</em>?', c="cómo puede ser")),
 portada("bolsa", 'Resultados <em class="c-orange">trimestrales</em>', "Hoy, en finanzas desde cero: cómo leer los resultados trimestrales."),
 esc('Cada tres <em class="c-navy">meses</em>', "Las empresas cotizadas publican sus resultados cada trimestre: cuánto han vendido, cuánto han ganado y cómo está su balance. Y la bolsa reacciona en segundos.",
     row(pill("T1", "navy", c="cada trimestre", lg=True), pill("T2", "navy", c="cada trimestre", d=0.2, lg=True), pill("T3", "navy", c="cada trimestre", d=0.4, lg=True), pill("T4", "navy", c="cada trimestre", d=0.6, lg=True)) +
     row(pill("Ventas", "sand", c="cuánto han vendido"), pill("Beneficio", "sand", c="cuánto han ganado"), pill("Balance", "sand", c="su balance"), style="margin-top:40px") + note("La bolsa reacciona en segundos", c="en segundos")),
 esc('1 · Contra las <em class="c-orange">expectativas</em>', "Lo primero que mira el mercado no es si la empresa gana mucho o poco, sino si gana más o menos de lo esperado. Los analistas publican sus previsiones, y la media se llama consenso. Si la empresa bate el consenso, suele subir. Si se queda corta, aunque sea un récord, suele bajar.",
     bars(("Consenso", "navy", 100, "100", "consenso"), ("Real", "orange", 95, "95 · récord, pero por debajo", "se queda corta")) + row(pill("Bate el consenso → suele subir", "teal", c="bate el consenso"), style="margin-top:40px"), sub="Ejemplo ilustrativo"),
 esc('El <em class="c-teal">BPA</em>', "La cifra que verás en todos los titulares es el BPA, el beneficio por acción: el beneficio dividido entre el número de acciones. Es lo que se suele comparar con el consenso. Pero ojo: puede subir solo porque la empresa recompra sus propias acciones, sin que el negocio haya mejorado nada.",
     row(pill("BPA = beneficio ÷ nº de acciones", "", c="beneficio por acción", lg=True)) + row(pill("Recompra acciones → BPA ↑", "orange", c="recompra", lg=True), style="margin-top:40px") + note("…sin que el negocio mejore", c="sin que el negocio")),
 esc('2 · Mismo trimestre, año <em class="c-navy">anterior</em>', "Lo segundo: compara siempre con el mismo trimestre del año anterior. Muchas empresas venden mucho más en Navidad o en verano, así que compararlo con el trimestre justo anterior te puede engañar.",
     steps(("✓", "T4 2026 vs T4 2025", "Mismo trimestre, año anterior", "teal", "mismo trimestre"), ("✗", "T4 vs T3", "Navidad frente a otoño: engaña", "orange", "te puede engañar"))),
 esc('3 · Márgenes y <em class="c-teal">caja</em>', "Lo tercero: no te quedes en las ventas. Mira si los márgenes suben o bajan, y si el beneficio se convierte en caja. Vender más ganando menos por cada euro no es buena señal.",
     row(pill("Ventas ↑", "teal", c="las ventas", lg=True), pill("Margen ↓", "orange", c="los márgenes", lg=True)) + note("Vender más ganando menos por cada euro: mala señal", c="no es buena señal") + row(pill("¿El beneficio se convierte en caja?", "", c="se convierte en caja", lg=True), style="margin-top:30px")),
 esc('4 · Lo que <em class="c-navy">viene</em>', "Y lo cuarto, que a veces es lo más importante: las previsiones de la propia empresa para los próximos meses, lo que se llama guidance. La bolsa mira hacia el futuro. Un buen trimestre con malas previsiones puede hundir la acción.",
     card("Guidance", "Lo que la empresa espera para los próximos meses", "navy", c="guidance") + note("La bolsa mira hacia el futuro", c="mira hacia el futuro") + row(pill("Buen trimestre + malas previsiones = caída", "orange", c="malas previsiones", lg=True), style="margin-top:30px")),
 final('La bolsa no premia los buenos resultados. Premia los resultados <em class="c-teal">mejores de lo esperado</em>.', "La bolsa no premia los buenos resultados. Premia los resultados mejores de lo esperado.", "Ejemplo ilustrativo."),
], f"""
Resultados récord… y la acción cae un 10 % 🤯

Porque el mercado no mira si una empresa gana mucho, sino si gana más de lo esperado. Cuatro cosas para leer unos resultados trimestrales:
🔸 Compara con el consenso
🔹 Compara con el mismo trimestre del año anterior
🔸 Mira márgenes y caja, no solo ventas
🔹 Escucha las previsiones (guidance)

Guárdalo para la próxima temporada de resultados 📌

{HB} #resultados""")

# ───────────── 12. Jue 28 ene · fondo · EV vs Equity
guardar("2027-01-28_fondo_ev-vs-equity", "fondo", 'Enterprise Value <span class="k">vs</span> <span class="c-teal">Equity Value</span>', "Enterprise Value vs Equity Value", [
 hook("Una casa que vale cuatrocientos mil euros. Te quedan doscientos veinte mil de hipoteca. ¿Cuánto de esa casa es tuyo de verdad?",
      card("La casa vale", "400.000 €", "navy", t=0, val=True) + row(pill("Hipoteca: 220.000 €", "orange", c="doscientos veinte mil", lg=True), style="margin-top:30px") + q('¿Cuánto es <em class="c-teal">tuyo</em>?', c="tuyo de verdad")),
 portada("fondo", 'Enterprise Value vs <em class="c-teal">Equity Value</em>', "Hoy, en finanzas a fondo: Enterprise Value frente a Equity Value."),
 esc('Empecemos por la <em class="c-navy">casa</em>', "La casa vale cuatrocientos mil, pero lo tuyo son ciento ochenta mil. El resto es del banco. Con las empresas pasa exactamente lo mismo. Solo que con nombres más raros.",
     bars(("La casa", "navy", 100, "400.000 €", "la casa vale"), ("Del banco", "orange", 55, "220.000 €", "el resto"), ("Tuyo", "teal", 45, "180.000 €", "ciento ochenta mil")) + note("Con las empresas, igual", c="exactamente lo mismo")),
 esc('<em class="c-navy">Enterprise Value</em>', "El Enterprise Value es lo que vale el negocio entero, para todos los que lo financian: accionistas y bancos. Es el valor de la casa. Y no depende de cómo se haya pagado.",
     card("Enterprise Value", "El negocio entero", "navy", c="el negocio entero") + row(pill("Accionistas", "teal", c="accionistas", lg=True), pill("Bancos", "orange", c="y bancos", lg=True), style="margin-top:40px") + note("Como el valor de la casa", c="el valor de la casa")),
 esc('<em class="c-teal">Equity Value</em>', "El Equity Value es lo que vale solo la parte de los accionistas. Es lo que ves en bolsa: la capitalización. Como la parte de la casa que es tuya.",
     card("Equity Value", "Solo los accionistas", "teal", c="solo la parte") + row(pill("= capitalización en bolsa", "", c="la capitalización", lg=True), style="margin-top:40px") + note("Como la parte de la casa que es tuya", c="que es tuya")),
 esc('El <em class="c-orange">puente</em>', "Para pasar de uno a otro se construye un puente. Al Enterprise Value le restas la deuda, le sumas la caja que tiene la empresa, y le restas lo que no es de los accionistas, como los minoritarios: la parte de sus filiales que pertenece a otros socios.",
     bars(("Enterprise Value", "navy", 100, "1.000", "al enterprise"), ("− Deuda", "orange", 40, "400", "le restas la deuda"), ("+ Caja", "teal", 10, "100", "le sumas la caja"), ("− Minoritarios", "orange", 5, "50", "minoritarios"), ("= Equity Value", "teal", 65, "650", "otros socios")), sub="Ejemplo ilustrativo · millones"),
 esc('Y de ahí, al precio por <em class="c-teal">acción</em>', "Y si divides el Equity Value entre el número de acciones, tienes lo que vale cada una. Pero ojo: hay que contar también las acciones que pueden aparecer más adelante, por ejemplo por las opciones de los directivos. Si te las saltas, el precio por acción te saldrá más alto de lo que es en realidad.",
     row(pill("Equity Value ÷ acciones", "", c="divides", lg=True), pill("= precio por acción", "teal", c="lo que vale cada una", lg=True)) + row(pill("+ acciones que pueden aparecer", "orange", c="opciones de los directivos", lg=True), style="margin-top:40px") + note("Si las olvidas, sobrevaloras el precio", c="más alto")),
 esc('Por qué <em class="c-navy">importa</em>', "¿Y por qué importa? Porque dos empresas con el mismo negocio pueden valer lo mismo como empresa, pero si una tiene mucha más deuda, sus acciones valen mucho menos. Por eso, para comparar negocios, los profesionales usan múltiplos sobre el Enterprise Value, como el EV entre EBITDA, y no solo el PER.",
     row(card("Empresa A · poca deuda", "Equity alto", "teal", c="dos empresas", style="min-width:420px"), card("Empresa B · mucha deuda", "Equity bajo", "orange", c="mucha más deuda", style="min-width:420px"), style="gap:30px") + row(pill("EV / EBITDA", "navy", c="ev entre ebitda", lg=True), pill("no solo el PER", "sand", c="solo el per", lg=True), style="margin-top:40px")),
 final('Lo que vale la empresa no es lo que valen sus acciones. <em class="c-orange">La diferencia es la deuda</em>.', "Lo que vale una empresa no es lo que valen sus acciones. La diferencia es la deuda.", "Ejemplo ilustrativo."),
], """
¿Lo que vale una empresa es lo mismo que lo que valen sus acciones? 🏠

No. Si una casa vale 400.000 € y te quedan 220.000 de hipoteca, lo tuyo son 180.000. Con las empresas pasa igual:
🔸 Enterprise Value → lo que vale el negocio entero
🔹 Deuda neta y otros ajustes → lo que es de otros
🔸 Equity Value → lo que es de los accionistas

Guárdalo para repasar 📌

#finanzas #valoraciondeempresas #inversion #educacionfinanciera #finanzasafondo""")

# ───────────── 13. Dom 31 ene · nadie · dividendos reinvertidos
guardar("2027-01-31_nadie_dividendos-reinvertidos", "nadie", NADIE, "Dividendos reinvertidos", [
 hook("Diez mil dólares en el S&P 500 en 1960, sin tocarlos. En 2024 tendrías casi un millón. O seis millones cuatrocientos mil. La diferencia es una sola decisión.",
      card("S&amp;P 500 · 1960", "10.000 $", "", t=0, val=True) + row(pill("≈ 1 millón", "navy", c="casi un millón", lg=True), pill("o 6,4 millones", "teal", c="seis millones", lg=True), style="margin-top:30px") + q('Una sola <em class="c-orange">decisión</em>', c="una sola decisión")),
 portada("nadie", 'El poder de los <em class="c-teal">dividendos</em>', "Esto es lo que nadie te cuenta sobre reinvertir los dividendos."),
 esc('¿Qué es <em class="c-teal">reinvertir</em>?', "Muchas empresas reparten cada año parte de sus beneficios: los dividendos. Puedes gastártelos, o usarlos para comprar más acciones. Si los reinviertes, al año siguiente cobras dividendos sobre más acciones. Y así, año tras año.",
     col(pill("Dividendo", "sand", c="los dividendos", lg=True), f'<span class="arrow in"{cue("comprar más acciones")}>↓</span>', pill("Compras más acciones", "teal", c="comprar más acciones", lg=True), f'<span class="arrow in"{cue("al año siguiente")}>↓</span>', pill("Más dividendos", "teal", c="al año siguiente", lg=True), f'<span class="arrow in"{cue("año tras año")}>↻</span>')),
 esc('La <em class="c-teal">diferencia</em>', "Según datos de FactSet y de la Universidad de Nueva York recogidos por CNBC, esos diez mil dólares de 1960 se habrían convertido en unos novecientos ochenta y dos mil solo con la subida del precio. Reinvirtiendo los dividendos, en unos seis millones cuatrocientos mil. Más de seis veces más.",
     bars(("Solo el precio", "navy", 15, "982.000 $", "novecientos ochenta y dos"), ("Reinvirtiendo", "teal", 100, "6.420.000 $", "reinvirtiendo los dividendos")) + row(pill("× 6,5", "teal", c="seis veces", lg=True), style="margin-top:40px"), sub="S&amp;P 500 · 10.000 $ en 1960 · hasta 2024"),
 esc('El <em class="c-orange">85 %</em>', "Hartford Funds lo calculó de otra forma: desde 1960, alrededor del ochenta y cinco por ciento de la rentabilidad total acumulada del S&P 500 se explica por los dividendos reinvertidos y el interés compuesto.",
     big("≈ 85 %", c="ochenta y cinco", cls="c-teal", style="text-align:center;font-size:150px") + note("de la rentabilidad total acumulada desde 1960", c="rentabilidad total") + row(pill("Dividendos reinvertidos + interés compuesto", "", c="interés compuesto"), style="margin-top:30px"), sub="Hartford Funds"),
 esc('Lo que no <em class="c-navy">ves</em>', "El problema es que cuando oyes cuánto ha subido un índice, casi siempre te hablan solo del precio. Los dividendos no salen en el gráfico de las noticias. Por eso tanta gente subestima lo que han aportado. Y cuantos más años pasan, más pesa esa diferencia, porque el interés compuesto necesita tiempo para hacer su magia.",
     row(card("Lo que te enseñan", "Solo el precio", "navy", c="solo del precio", style="min-width:420px"), card("Lo que falta", "Los dividendos", "teal", c="no salen", style="min-width:420px"), style="gap:30px")),
 esc('Cómo hacerlo <em class="c-teal">fácil</em>', "La forma más sencilla de aprovecharlo es usar fondos o ETFs de acumulación, que reinvierten los dividendos automáticamente, sin que tengas que hacer nada. Y no pagas impuestos por esos dividendos hasta que vendas.",
     card("Fondos y ETFs de acumulación", "Reinvierten solos", "teal", c="acumulación") + row(pill("Sin hacer nada", "sand", c="sin que tengas", lg=True), pill("Impuestos al vender", "sand", c="hasta que vendas", lg=True), style="margin-top:40px")),
 final('El dividendo que reinviertes hoy es el que <em class="c-teal">trabaja para ti</em> dentro de treinta años.', "El dividendo que reinviertes hoy es el que trabaja para ti dentro de treinta años.", "Datos: CNBC (FactSet, NYU Stern), 1960–2024; Hartford Funds."),
], """
10.000 $ en el S&P 500 en 1960: casi 1 millón… o 6,4 millones 🤯

La diferencia es reinvertir los dividendos. Según Hartford Funds, alrededor del 85 % de la rentabilidad total del S&P 500 desde 1960 viene de los dividendos reinvertidos y el interés compuesto.

Lo más fácil: fondos o ETFs de acumulación, que los reinvierten solos.

Guárdalo y compártelo con quien solo mira el precio de las acciones 📌

Contenido educativo, no es recomendación de inversión.

#finanzaspersonales #dividendos #bolsa #educacionfinanciera #loquenadietecuenta""")
