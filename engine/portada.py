# Elige el fotograma de portada de un vídeo hecho con el motor: la escena crema más visual
# (barras, columnas o gráfico), en el momento en que ya está completa.
# Uso: python3 engine/portada.py videos/<carpeta>   → imprime los ms y guarda portada.jpg
import json, sys, subprocess, os
d = sys.argv[1]
spec = json.load(open(f"{d}/spec.json")); al = json.load(open(f"{d}/align.json"))
starts, ends = al["character_start_times_seconds"], al["character_end_times_seconds"]
off, bounds = 0, []
for i, s in enumerate(spec["scenes"]):
    t0 = 0 if i == 0 else max(0, starts[min(off, len(starts)-1)] - 0.12)
    bounds.append(t0); off += len(s["say"].strip()) + 1
bounds.append(ends[-1])
def score(s):
    h = s.get("html", "")
    if s.get("dark") or not s.get("title"): return -1
    return 3*('class="cols' in h) + 3*('class="bars' in h) + 3*("<svg" in h) + h.count('class="card') + 0.5*h.count('class="pill')
best = max(range(len(spec["scenes"])), key=lambda i: (score(spec["scenes"][i]), -i))
if "coverMs" in spec: ms = spec["coverMs"]
else: ms = int((bounds[best+1] - 0.6) * 1000)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(ms/1000), "-i", f"{d}/video.mp4", "-frames:v", "1", "-q:v", "3", f"{d}/portada.jpg"], check=True)
print(ms)
