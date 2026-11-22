// Uso: node engine/tts.js <carpeta_del_video>
// Lee spec.json, manda el guion completo a ElevenLabs con la voz "Raúl's voice"
// y guarda audio.mp3 + align.json (tiempos de cada carácter para sincronizar).
// La clave la inyecta el proxy del entorno; aquí no se usa ninguna clave.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const VOICE = process.env.VOICE_ID || 'qZBD95GE6BZToWCjEQiK'; // Raúl's voice
const MODEL = process.env.TTS_MODEL || 'eleven_v4'; // el mismo modelo que usa Raúl en ElevenLabs
const dir = path.resolve(process.argv[2]);
const spec = JSON.parse(fs.readFileSync(path.join(dir, 'spec.json'), 'utf8'));
const text = spec.scenes.map(s => s.say.trim()).join(' ');

const body = { text, model_id: MODEL };
if (spec.voice_settings) body.voice_settings = spec.voice_settings;
const bodyPath = path.join(dir, '.tts_body.json');
fs.writeFileSync(bodyPath, JSON.stringify(body));
const raw = execFileSync('curl', ['-sS', '--fail-with-body', '-X', 'POST',
  `https://api.elevenlabs.io/v1/text-to-speech/${VOICE}/with-timestamps?output_format=mp3_44100_128`,
  '-H', 'Content-Type: application/json', '--data-binary', '@' + bodyPath], { maxBuffer: 200 * 1024 * 1024 }).toString();
fs.unlinkSync(bodyPath);
const res = JSON.parse(raw);
fs.writeFileSync(path.join(dir, 'audio.mp3'), Buffer.from(res.audio_base64, 'base64'));
fs.writeFileSync(path.join(dir, 'align.json'), JSON.stringify(res.alignment));
const a = res.alignment;
console.log(`OK audio ${a.character_end_times_seconds.at(-1).toFixed(1)} s · ${text.length} caracteres`);
