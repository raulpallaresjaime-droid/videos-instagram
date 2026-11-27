# Recorta un clip de archivo para usarlo en una escena con `clip`.
# Uso:
#   python3 clip.py <origen.webm|mp4> <inicio_s> <duracion_s> <salida.mp4> [fy]
#     → 1280x720 (lo que usa el render), 30 fps, sin audio, H.264 ligero, máximo 20 s.
#   fy (0-1, por defecto 0.5) = qué parte se conserva al recortar en vertical un vídeo 4:3.
#   python3 clip.py sheet <origen> <inicio_s> <duracion_s> <hoja.jpg> [cada_s=10]
#     → hoja de contactos (un fotograma cada N s, con el segundo encima) para elegir tramos.
# <origen> puede ser un archivo o la URL de Wikimedia (commons.py vurl): ffmpeg lee solo el tramo pedido.
# Quita solo las bandas negras (cropdetect) antes de encuadrar a 16:9.
import re, subprocess, sys

UA = ['-user_agent', 'HistoriaDocBot/1.0 (https://claude.ai/code; educational documentary video tool)']
if sys.argv[1] == 'sheet':
    src, start, dur, out = sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
    step = float(sys.argv[6]) if len(sys.argv) > 6 else 10
    ua = UA if src.startswith('http') else []
    n = max(1, int(dur // step)); rows = -(-n // 6)
    # select = el primer fotograma de cada tramo de N s, con su segundo exacto encima
    vf = (f"select='isnan(prev_selected_t)+gte(t-prev_selected_t\\,{step}-0.02)',scale=360:-2,"
          f"drawtext=text='%{{eif\\:t+{start}\\:d}} s':x=8:y=8:fontsize=26:fontcolor=yellow:box=1:boxcolor=black@0.6,"
          f"tile=6x{rows}")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *ua, '-ss', str(start), '-t', str(dur), '-i', src, '-an',
                    '-vf', vf, '-vsync', 'vfr', '-frames:v', '1', out], check=True, stdin=subprocess.DEVNULL)
    print('OK', out); sys.exit()
src, start, dur, out = sys.argv[1], float(sys.argv[2]), min(20.0, float(sys.argv[3])), sys.argv[4]
fy = float(sys.argv[5]) if len(sys.argv) > 5 else 0.5
ua = UA if src.startswith('http') else []

# bandas negras: cropdetect sobre el tramo elegido (la detección más repetida)
det = subprocess.run(['ffmpeg', '-hide_banner', *ua, '-ss', str(start), '-t', str(dur), '-i', src, '-vf', 'cropdetect=limit=24:round=2:reset=0',
                      '-an', '-f', 'null', '-'], capture_output=True, text=True, stdin=subprocess.DEVNULL).stderr
crops = re.findall(r'crop=(\d+:\d+:\d+:\d+)', det)
pre = f'crop={max(set(crops), key=crops.count)},' if crops else ''

vf = (f'{pre}scale=1280:720:force_original_aspect_ratio=increase,'
      f'crop=1280:720:(iw-1280)/2:(ih-720)*{fy},setsar=1,fps=30')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *ua, '-ss', str(start), '-t', str(dur), '-i', src, '-an', '-vf', vf,
                '-c:v', 'libx264', '-preset', 'slow', '-crf', '28', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], check=True, stdin=subprocess.DEVNULL)
import os, urllib.parse
with open(os.path.join(os.path.dirname(os.path.abspath(out)), 'creditos.txt'), 'a') as f:  # crédito del clip
    f.write(f"{os.path.basename(out)}\tFile:{urllib.parse.unquote(src.rsplit('/', 1)[-1])}\tdesde {start:g} s, {dur:g} s\tPublic domain (comprobar en Commons)\n")
print('OK', out, os.path.getsize(out) // 1024, 'KB', pre.rstrip(',') or 'sin bandas', f'{dur:.1f} s')
