# Ayudas para escribir spec.json + caption.txt con comprobaciones.
# Uso: from nuevo import *  → escena(), final(), guardar()
import json, os, re, unicodedata

NADIE = '<span class="k">Lo que</span> <span class="c-orange">nadie te cuenta</span>'
KICK = {"bolsa": "Finanzas desde cero", "fondo": "Finanzas a fondo", "nadie": "Lo que nadie te cuenta"}
DISC = "Contenido educativo, no es recomendación de inversión."

def _base(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()

def portada(serie, hero, say, extra=""):
    return {"dark": True, "say": say,
            "html": f'<div class="kicker in" data-t="0">{KICK[serie]}</div><div class="hero sm in" data-t="0.2">{hero}</div>{extra}'}

def final(txt, say, fuente="Ejemplo ilustrativo."):
    return {"dark": True, "say": say,
            "html": f'<div class="final in" data-t="0">{txt}</div><div class="rule in" data-t="1"></div><div class="disc in" data-t="1">{fuente}<br>{DISC}</div>'}

def guardar(carpeta, serie, topic, titulo, escenas, caption):
    # 1) cada data-cue tiene que aparecer en el say de su escena
    for i, e in enumerate(escenas):
        for cue in re.findall(r'data-cue="([^"]+)"', e.get("html", "")):
            if _base(cue) not in _base(e["say"]):
                raise SystemExit(f"{carpeta}: escena {i}: cue «{cue}» no está en el texto")
    # 2) la primera escena tiene que enseñar algo desde el segundo 0
    if 'data-t="0"' not in escenas[0]["html"]:
        raise SystemExit(f"{carpeta}: la primera escena no muestra nada en el segundo 0")
    spec = {"series": serie, "topic": topic, "title_post": titulo, "coverScene": 1, "scenes": escenas}
    os.makedirs(f"videos/{carpeta}", exist_ok=True)
    json.dump(spec, open(f"videos/{carpeta}/spec.json", "w"), ensure_ascii=False, indent=1)
    open(f"videos/{carpeta}/caption.txt", "w").write(caption.strip() + "\n")
    n = sum(len(e["say"]) for e in escenas)
    print(f"{carpeta}: {n} caracteres ≈ {n/16.5:.0f} s")

# ── piezas de HTML para escribir escenas (mismo estilo que los vídeos de enero) ──
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

