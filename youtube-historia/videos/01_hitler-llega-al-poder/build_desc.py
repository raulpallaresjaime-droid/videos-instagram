# Genera descripcion.txt (título, descripción con capítulos, fuentes y créditos de imágenes, etiquetas)
import os
here = os.path.dirname(os.path.abspath(__file__))
titulo = 'Cómo Hitler llegó al poder sin ganar nunca la mayoría | Documental'
cap = """0:00 Nunca ganó la mayoría
0:33 Versalles y el mito de la puñalada
1:57 1923: la hiperinflación
2:27 El golpe de la cervecería
3:40 Años dorados: el 2,6 %
4:00 El crack del 29 y 6 millones de parados
4:50 El ascenso nazi (1930-1932)
6:18 Enero de 1933: los despachos
7:05 El incendio del Reichstag
8:12 La Ley Habilitante
9:15 La Noche de los cuchillos largos
9:41 Führer: el poder absoluto
10:14 Conclusión"""
cred = []
for l in open(os.path.join(here, 'img', 'creditos.txt')):
    n, t, lic, art = (l.rstrip('\n').split('\t') + ['', '', '', ''])[:4]
    cred.append(f"- {t.replace('File:', '')} ({lic}{', ' + art if art else ''})")
desc = f"""Adolf Hitler nunca ganó la mayoría absoluta en unas elecciones libres. Su mejor resultado fue un 43,9 %. Y aun así, en solo 18 meses pasó de canciller vigilado a dictador absoluto de Alemania. Esta es la historia, paso a paso, de cómo una democracia se desmontó desde dentro.

📌 Capítulo 1 de la serie sobre el nazismo y la Segunda Guerra Mundial. Próximo capítulo: de Dachau a Auschwitz.

⏱️ Capítulos
{cap}

📚 Fuentes
- United States Holocaust Memorial Museum (USHMM), Enciclopedia del Holocausto
- Deutscher Bundestag: historia del Parlamento en el Tercer Reich
- Encyclopaedia Britannica: Weimar Republic, Enabling Act
- Deutsches Historisches Museum (LeMO)
- Dimsdale, Horsewood y Van Riel: Unemployment in interwar Germany (Universidad de Oxford)
Algunas cifras (víctimas, porcentajes) varían ligeramente según la fuente.

🖼️ Imágenes: Bundesarchiv (licencia CC BY-SA 3.0 DE), National Archives (NARA), Biblioteca Nacional de Francia y Wikimedia Commons.
{chr(10).join(cred)}

Contenido histórico y educativo. Este canal no hace apología de ninguna ideología: contamos la historia para que no se repita.

#historia #segundaguerramundial #hitler #nazismo #documental"""
tags = 'historia, segunda guerra mundial, hitler, nazismo, alemania nazi, república de weimar, documental, historia de alemania, ley habilitante, incendio del reichstag, holocausto'
open(os.path.join(here, 'descripcion.txt'), 'w').write(f"TÍTULO\n{titulo}\n\nDESCRIPCIÓN\n{desc}\n\nETIQUETAS\n{tags}\n")
print('OK descripcion.txt')
