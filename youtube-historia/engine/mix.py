# Mezcla final: voz + música de fondo (por "mood" de escena, con fundidos y bajando bajo la voz)
# + tecleo de máquina de escribir + golpes en los sellos. Normaliza a -14 LUFS (YouTube).
# Uso: python3 mix.py <carpeta_del_video>   (lee eventos.json, audio.mp3 y spec.json; escribe mezcla.wav)
import numpy as np, json, os, sys, subprocess, wave
SR = 44100
HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, '..', 'audio')
d = os.path.abspath(sys.argv[1])
ev = json.load(open(os.path.join(d, 'eventos.json')))
spec = json.load(open(os.path.join(d, 'spec.json')))
rng = np.random.default_rng(3)

def load(p):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
def rms(x): return float(np.sqrt(np.mean(x ** 2)) + 1e-9)
def db(v): return 10 ** (v / 20)

n = int((ev['total'] + 0.5) * SR)
voice = np.zeros((n, 2), np.float32); v = load(os.path.join(d, 'audio.mp3')); voice[:len(v)] = v[:n]
# nivel de referencia de la voz (solo partes habladas)
fr = SR // 20
blocks = np.sqrt(np.mean(voice[:len(voice) // fr * fr, 0].reshape(-1, fr) ** 2, axis=1))
speech = blocks > np.percentile(blocks, 40) * 0.5
vref = float(np.sqrt(np.mean(blocks[speech] ** 2)))

# --- música: tramos de escenas consecutivas con el mismo "mood" ---
moods = [s.get('mood') or spec.get('mood', 'inquietud') for s in spec['scenes']]
runs = []
for i, s in enumerate(ev['scenes']):
    if runs and runs[-1][0] == moods[i]: runs[-1][2] = s['end']
    else: runs.append([moods[i], s['start'], s['end']])
tracks, pos = {}, {}
music = np.zeros((n, 2), np.float32)
XF = int(2.5 * SR)
for k, (mood, a, b) in enumerate(runs):
    if mood not in tracks:
        tr = load(os.path.join(LIB, 'musica', mood + '.mp3'))
        tracks[mood] = tr / rms(tr); pos[mood] = 0
    tr = tracks[mood]
    i0 = max(0, int(a * SR) - (XF // 2 if k else 0)); i1 = min(n, int(b * SR) + (XF // 2 if k < len(runs) - 1 else 0))
    L = i1 - i0
    idx = (pos[mood] + np.arange(L)) % len(tr); pos[mood] = int(idx[-1]) + 1  # continúa donde se quedó; si se acaba, vuelve a empezar
    seg = tr[idx].copy()
    # fundido de entrada/salida en cada tramo (equal power)
    f = np.ones(L)
    if k: f[:XF] = np.sin(np.linspace(0, np.pi / 2, min(XF, L)))[:L] if L >= XF else f[:L]
    if k < len(runs) - 1 and L > XF: f[-XF:] *= np.cos(np.linspace(0, np.pi / 2, XF))
    music[i0:i1] += seg * f[:, None]
# fade in al principio y fade out al final
fi = int(1.5 * SR); music[:fi] *= np.linspace(0, 1, fi)[:, None]
fo = int(4 * SR); music[-fo:] *= np.linspace(1, 0, fo)[:, None]
# bajar la música mientras habla el narrador (envolvente suave)
act = np.repeat(speech.astype(np.float32), fr)[:n]; act = np.pad(act, (0, n - len(act)))
k = int(0.35 * SR); act = np.convolve(act, np.ones(k) / k, mode='same')
lvl = spec.get('music_db', [-17, -23])  # [sin voz, con voz] respecto a la voz
gain = db(lvl[0]) + (db(lvl[1]) - db(lvl[0])) * np.clip(act, 0, 1)
music *= (vref * gain)[:, None]

# --- efectos ---
sfxdir = os.path.join(LIB, 'sfx')
keys = [load(os.path.join(sfxdir, f'tecla_{i}.wav')) for i in range(8)]
space = load(os.path.join(sfxdir, 'espacio.wav')); boom = load(os.path.join(sfxdir, 'golpe.wav'))
fx = np.zeros((n, 2), np.float32)
def put(x, t, g):
    i = int(t * SR)
    if i >= n: return
    m = min(len(x), n - i); fx[i:i + m] += x[:m] * g
for e in ev['typing']:
    for j, ch in enumerate(e['text']):
        t = e['t'] + j / e['cps'] + rng.uniform(-0.012, 0.012)
        if ch == ' ': put(space, t, vref * db(-6) / rms(space[:2000]) * 0.15)
        else: put(keys[rng.integers(8)], t, vref * db(-4) / rms(keys[0][:2000]) * rng.uniform(0.11, 0.17))
for t in ev['hits']: put(boom, t, vref * db(-2) / rms(boom) * 0.5)

mixed = voice + music + fx
tmp = os.path.join(d, '_mezcla_raw.wav')
with wave.open(tmp, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mixed / max(1.0, np.max(np.abs(mixed)) * 1.05), -1, 1) * 32767).astype(np.int16).tobytes())
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', tmp, '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', str(SR),
                os.path.join(d, 'mezcla.wav')], check=True)
os.unlink(tmp)
print(f"OK mezcla.wav · tramos de música: {', '.join(f'{m} {a:.0f}-{b:.0f}s' for m, a, b in runs)}")
