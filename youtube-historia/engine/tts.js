// Uso: node youtube-historia/engine/tts.js <carpeta_del_video>
// Manda el guion (todas las "say" del spec) a ElevenLabs en trozos de ~2.500 caracteres, cortando
// siempre entre escenas, y une el resultado en audio.mp3 + align.json (tiempos de cada carácter).
// Voz por defecto: «Salva - The Spanish Narrator». La clave la inyecta el proxy del entorno.
// Cada trozo se guarda en tts_parts/, así que si algo falla a mitad no se vuelve a pagar lo ya generado.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const dir = path.resolve(process.argv[2]);
const spec = JSON.parse(fs.readFileSync(path.join(dir, 'spec.json'), 'utf8'));
const VOICE = spec.voice || 'hyKxCTlAqtnW188CgltM'; // Salva
const MODEL = spec.model || 'eleven_v4';
const SETTINGS = spec.voice_settings || { stability: 0.5, similarity_boost: 0.75 };
const says = spec.scenes.map(s => s.say.trim());

const chunks = []; let cur = [];
for (const s of says) {
  if (cur.length && cur.join(' ').length + s.length + 1 > 2500) { chunks.push(cur.join(' ')); cur = []; }
  cur.push(s);
}
if (cur.length) chunks.push(cur.join(' '));

const pdir = path.join(dir, 'tts_parts'); fs.mkdirSync(pdir, { recursive: true });
const dur = f => +execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]).toString();
const chars = [], st = [], en = []; let offset = 0; const wavs = [];
chunks.forEach((text, i) => {
  const mp3 = path.join(pdir, `p${i}.mp3`), aj = path.join(pdir, `p${i}.json`);
  if (!fs.existsSync(aj) || JSON.parse(fs.readFileSync(aj)).text !== text) {
    const body = path.join(pdir, 'body.json');
    fs.writeFileSync(body, JSON.stringify({ text, model_id: MODEL, voice_settings: SETTINGS }));
    const raw = execFileSync('curl', ['-sS', '--fail-with-body', '-X', 'POST',
      `https://api.elevenlabs.io/v1/text-to-speech/${VOICE}/with-timestamps?output_format=mp3_44100_128`,
      '-H', 'Content-Type: application/json', '--data-binary', '@' + body], { maxBuffer: 500 * 1024 * 1024 }).toString();
    fs.unlinkSync(body);
    const res = JSON.parse(raw);
    fs.writeFileSync(mp3, Buffer.from(res.audio_base64, 'base64'));
    fs.writeFileSync(aj, JSON.stringify({ text, alignment: res.alignment }));
    console.log(`  trozo ${i + 1}/${chunks.length}: ${text.length} caracteres`);
  }
  const a = JSON.parse(fs.readFileSync(aj)).alignment;
  if (i > 0) { chars.push(' '); st.push(offset); en.push(offset); }
  a.characters.forEach((c, k) => { chars.push(c); st.push(a.character_start_times_seconds[k] + offset); en.push(a.character_end_times_seconds[k] + offset); });
  const wav = path.join(pdir, `p${i}.wav`);
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', mp3, '-ar', '44100', '-ac', '1', wav]);
  wavs.push(wav); offset += dur(wav);
});
const list = path.join(pdir, 'list.txt');
fs.writeFileSync(list, wavs.map(w => `file '${w}'`).join('\n'));
execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', list, '-c:a', 'libmp3lame', '-b:a', '160k', path.join(dir, 'audio.mp3')]);
wavs.forEach(w => fs.unlinkSync(w)); fs.unlinkSync(list);
fs.writeFileSync(path.join(dir, 'align.json'), JSON.stringify({ characters: chars, character_start_times_seconds: st, character_end_times_seconds: en }));
console.log(`OK audio ${offset.toFixed(1)} s · ${says.join(' ').length} caracteres en ${chunks.length} trozos`);
