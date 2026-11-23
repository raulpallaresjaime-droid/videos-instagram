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
