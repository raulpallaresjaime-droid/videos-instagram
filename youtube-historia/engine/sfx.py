# Sintetiza los efectos de sonido del canal (100 % propios, sin derechos de terceros):
#   tecla_0..7.wav  pulsación de máquina de escribir (8 variantes)
#   espacio.wav     barra espaciadora
#   golpe.wav       impacto grave para sellos y revelaciones
# Uso: python3 sfx.py <carpeta_salida>
import numpy as np, wave, sys, os
SR = 44100
rng = np.random.default_rng(7)

def save(name, x):
    x = x / (np.max(np.abs(x)) + 1e-9) * 0.9
    with wave.open(os.path.join(out, name), 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())

def bandnoise(n, lo, hi):
    """ruido filtrado por banda (FFT)"""
    X = np.fft.rfft(rng.standard_normal(n)); f = np.fft.rfftfreq(n, 1 / SR)
    X[(f < lo) | (f > hi)] = 0
    return np.fft.irfft(X, n)

def env(n, attack, decay):
    t = np.arange(n) / SR
    return np.minimum(t / attack, 1) * np.exp(-t / decay)

def key(seed_shift=0, heavy=1.0):
    n = int(0.16 * SR); t = np.arange(n) / SR
    clack = bandnoise(n, 1800 + 300 * rng.random(), 7000) * env(n, 0.0004, 0.006)          # golpe del tipo
    body = bandnoise(n, 250, 1400) * env(n, 0.001, 0.02) * 0.7 * heavy                     # cuerpo de madera/metal
    ping = np.sin(2 * np.pi * (2600 + 900 * rng.random()) * t) * env(n, 0.0005, 0.012) * 0.25  # resonancia metálica
    thump = np.sin(2 * np.pi * 95 * t) * env(n, 0.002, 0.03) * 0.5 * heavy                # golpe sobre la mesa
    # rebote de la tecla al volver (~35 ms después)
    d = int(0.035 * SR); rel = np.zeros(n); rel[d:] = bandnoise(n - d, 1500, 6000) * env(n - d, 0.0004, 0.004) * 0.35
    return clack + body + ping + thump + rel

out = sys.argv[1]; os.makedirs(out, exist_ok=True)
for i in range(8): save(f'tecla_{i}.wav', key(i))
save('espacio.wav', key(heavy=1.8) * 0.8)
# golpe: barrido grave + ruido sordo + cola
n = int(2.2 * SR); t = np.arange(n) / SR
f = 70 * np.exp(-t * 1.5) + 32
boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.003, 0.55)
boom += bandnoise(n, 40, 400) * env(n, 0.002, 0.25) * 0.6 + bandnoise(n, 400, 3000) * env(n, 0.001, 0.05) * 0.25
save('golpe.wav', boom)
print('OK efectos en', out)
