# El medallón de la bruja · Tarjetas imprimibles

[![Licencia: CC BY-SA 4.0](https://img.shields.io/badge/Licencia-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)

Generador en Python de tarjetas A4 recortables para *El medallón de la bruja*, una **versión infantil** (a partir de 7 años) de *La bruja está muerta*, la versión en castellano de *The Witch is Dead*, el rol de una página de Grant Howitt. En esta versión nadie muere: un ladrón ha robado el medallón mágico de la bruja, que ha caído en un sueño encantado, y los animalitos del bosque deben recuperarlo antes de la próxima luna llena (ver [Versión infantil](#versión-infantil)). Produce un PDF listo para imprimir con:

- La descripción del juego, las reglas y las tablas d10 de la historia.
- Una ficha por cada especie de animalito del bosque, más fichas en blanco.
- Una tarjeta por cada resultado de las tablas, para repartirlas o sacarlas al azar.

Cada tarjeta tiene varios **diseños** seleccionables, así que puedes probar diseños nuevos sin perder los anteriores.

## Requisitos

- Python 3.10 o superior.
- [Playwright](https://playwright.dev/python/), que imprime el HTML a PDF con Chrome.
- Google Chrome instalado. Si no lo tienes, Playwright puede usar su propio Chromium (ver abajo).

Las fuentes (Lora y Caladea, con licencia OFL) están incluidas en `bruja/fuentes/` y van incrustadas en el HTML. Por eso, **para generar el PDF no hace falta conexión a internet**.

## Instalación

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Si no tienes Google Chrome, instala el Chromium de Playwright:

```bash
.venv/bin/playwright install chromium
```

## Uso rápido

```bash
.venv/bin/python generar.py
```

Genera `tarjetas.html` y `tarjetas.pdf`, con 7 hojas A4:

| Hoja | Contenido | Rejilla |
|---|---|---|
| 1 | Tiradas de historia: introducción, cómo jugar, y las tablas del pueblo, el ladrón, el giro y el hechizo | 2×3 |
| 2–3 | Personajes: las 10 especies y 2 fichas en blanco | 2×3 |
| 4 | El pueblo es…: una tarjeta por resultado | 2×5 |
| 5 | El ladrón es…: una tarjeta por resultado | 2×5 |
| 6 | El giro: una tarjeta por resultado | 2×5 |
| 7 | Tu bruja te enseñó…: una tarjeta por resultado | 2×5 |

### Opciones de `generar.py`

| Opción | Efecto |
|---|---|
| *(ninguna)* | El mazo completo descrito arriba |
| `--sin-pdf` | Genera solo `tarjetas.html` |
| `--sin-resultados` | Omite las hojas de tarjetas por resultado (queda un mazo de 3 hojas) |
| `--resultados` | Tarjetas por resultado a media altura (2×6) en vez de 2×5 |
| `--media` | Las cuatro tablas de la hoja 1 a media altura (tabla completa en 99×47,5 mm) |
| `--copias N` | Repite las cuatro tablas N veces; por ejemplo, `--media --copias 3` llena una hoja de 12 |
| `--catalogo` | Genera `catalogo.pdf` con una muestra de **todos** los diseños disponibles, para compararlos |
| `--publicacion [DIR]` | Genera en `DIR` (por defecto `dist/`) los PDF que se publican en cada versión (ver [Publicación en releases](#publicación-en-releases)) |

Ejemplos:

```bash
.venv/bin/python generar.py --sin-resultados         # solo reglas, tablas y personajes
.venv/bin/python generar.py --media --copias 3       # una hoja de tablas por jugador
.venv/bin/python generar.py --catalogo               # comparar todos los diseños
```

### Publicación en releases

El workflow [`.github/workflows/publicar-pdf.yml`](.github/workflows/publicar-pdf.yml) genera con `generar.py --publicacion` los PDF del diccionario `EDICIONES` de `generar.py`:

| PDF | Contenido |
|---|---|
| `el-medallon-de-la-bruja-tarjetas-de-personajes-para-rellenar.pdf` | Hoja 1 con la descripción del juego, las reglas y las cuatro tablas d10; personajes `con_tiradas_de_inicio()` (con líneas para apuntar pueblo, ladrón y hechizo) y 2 fichas en blanco |
| `el-medallon-de-la-bruja-tarjetas-de-personajes-reutilizables.pdf` | La misma hoja 1; personajes `simple()`, sin campos para rellenar, y 2 fichas en blanco con ese mismo diseño; después, una hoja 2×5 por tabla con una tarjeta por resultado |

#### ¿Qué PDF elegir?

- **Personajes reutilizables:** las fichas no tienen nada que escribir en cada partida. La tirada inicial (el pueblo, el ladrón y el hechizo que te enseñó la bruja) se resuelve con las tarjetas de resultados: se coloca junto a la ficha la tarjeta que ha salido y, al terminar, se devuelve a su montón. Así, la misma ficha sirve para partida tras partida. Las 2 fichas en blanco permiten crear dos personajes propios una sola vez y reutilizarlos igual.
- **Personajes para rellenar:** cada ficha tiene líneas para apuntar el pueblo, el ladrón y el hechizo. Aunque se puede escribir con lápiz y borrar, con el uso el papel se estropea, así que suelen servir para **una o dos partidas**. Es la opción cómoda si vas a jugar una vez o no quieres recortar las 40 tarjetas de resultados.

**Para marcar el peligro, en las dos versiones**, es mejor no pintar los círculos con lápiz y borrarlos después: pon encima **fichas, cuentas, monedas o piedrecitas**. Puedes colocar una en el círculo del nivel actual, o tantas como puntos de peligro tengas. Así las fichas duran mucho más.

- En cada petición de fusión y en `master`, los PDF quedan como artefacto `pdf` de la ejecución, para revisarlos.
- Al subir una etiqueta `v*` (`git tag v1.0 && git push origin v1.0`), se adjuntan a la release de esa etiqueta, que se crea si no existe.
- También puede lanzarse a mano desde la pestaña *Actions* ("Run workflow"), indicando la etiqueta de la release. Si la etiqueta ya existe, los PDF se generan desde su commit; si no, se crea en el commit de la rama elegida.

Para publicar otro PDF, añade al diccionario `EDICIONES` su nombre de fichero y la función que construye su `Documento`.

### Consejos de impresión

- Imprime a **tamaño real / escala 100 %**, sin "ajustar a la página", para que las tarjetas tengan su medida exacta.
- Recorta por la línea discontinua gris. El marco morado de cada tarjeta deja margen de corte.

## Uso desde Python

```python
from bruja import Documento, Tarjetas

doc = Documento()
doc.add(Tarjetas.Personajes.Buho.simple())
doc.add(Tarjetas.Personajes.Gato.con_notas())
doc.add(Tarjetas.Personajes.Buho.con_tiradas_de_inicio())
doc.render("documento.pdf")        # o "documento.html"
```

La forma general es siempre `Tarjetas.<Grupo>.<Modelo>.<diseño>()`. La llamada devuelve una tarjeta, o una lista de tarjetas, lista para `Documento.add()`.

### `Documento`

| Método | Descripción |
|---|---|
| `Documento(titulo=…)` | Crea un documento vacío. El título es el del HTML o PDF. |
| `.add(*tarjetas)` | Añade tarjetas, listas o generadores de tarjetas. Devuelve el documento, así que admite encadenar llamadas. |
| `.seccion("Etiqueta")` | Empieza una sección nueva en página nueva. La etiqueta aparece en el pie de sus hojas ("Personajes 1/2 · recorta por la línea discontinua"). Sin secciones, el pie dice "Página n/N". |
| `.render("ruta.pdf")` | Escribe el documento. La extensión (`.pdf` o `.html`) decide el formato. |
| `.html()` | Devuelve el HTML completo como texto. |

El documento coloca las tarjetas en hojas según su **formato**. Tarjetas de formatos distintos nunca comparten hoja: al cambiar de formato se pasa a una página nueva.

| Formato | Tamaño | Rejilla por hoja A4 |
|---|---|---|
| `completa` | 99 × 95 mm | 2 × 3 = 6 |
| `media` | 99 × 47,5 mm | 2 × 6 = 12 |
| `quinta` | 99 × 57 mm | 2 × 5 = 10 |

### Elegir diseño por nombre

Cada modelo sabe qué diseños tiene. Así puedes elegirlos desde un bucle o un texto:

```python
Tarjetas.Personajes.Buho.disenos()
# ['con_notas', 'con_tiradas_de_inicio', 'simple']

Tarjetas.Personajes.Buho.diseno("con_notas")   # equivale a .con_notas()
```

Si el nombre no existe, se lanza un `ValueError` que indica los diseños disponibles.

## Tarjetas y diseños disponibles

### Personajes: `Tarjetas.Personajes.<Especie>`

Especies, en orden de d10: `Zorro`, `Gato`, `Sapo`, `Arana`, `Buho`, `Liebre`, `Urraca`, `Cuervo`, `Perro`, `Rata`. Además está `EnBlanco`, una ficha para rellenar a mano con la especie, el retrato y los rasgos. `Tarjetas.Personajes.todos()` devuelve las 10 especies, sin las fichas en blanco.

| Diseño | Formato | Descripción |
|---|---|---|
| `con_notas()` | completa | Diseño original: retrato, especie, líneas para nombre y hechizo, rasgos, peligro y notas del plan de rescate |
| `simple()` | completa | Retrato y rasgos grandes, y un recuadro de peligro con la regla de desgracia |
| `con_tiradas_de_inicio()` | completa | Rasgos junto al retrato, número del d10 en la esquina, y líneas para apuntar pueblo, ladrón y hechizo. **Es el que usa el mazo por defecto.** |

### Historia: `Tarjetas.Historia.Introduccion`

| Diseño | Formato | Descripción |
|---|---|---|
| `simple()` | completa | La historia de la bruja y el objetivo de la partida |

### Reglas: `Tarjetas.Reglas.ComoJugar`

| Diseño | Formato | Descripción |
|---|---|---|
| `simple()` | completa | Reglas originales: tirada, dificultades y peligro |
| `con_lios()` | completa | Añade que sacar igual o menos que tu peligro te mete en un lío: te atrapan, te pierdes o vuelves a casa a descansar. **Por defecto.** |

### Tablas d10: `Tarjetas.Tablas.<Tabla>`

Tablas: `Pueblo`, `Ladron`, `Giro` (solo para el GM, con números morados y línea discontinua) y `Hechizo`.

| Diseño | Formato | Devuelve | Descripción |
|---|---|---|---|
| `simple()` | completa | 1 tarjeta | La tabla completa con sus 10 resultados. **Por defecto** (hoja 1) |
| `media_altura()` | media | 1 tarjeta | La tabla completa en media altura |
| `por_resultado()` | media | 10 tarjetas | Una tarjeta por resultado, 12 por hoja |
| `por_resultado_5x2()` | quinta | 10 tarjetas | Una tarjeta por resultado, 10 por hoja: cada tabla ocupa una hoja justa. **Por defecto** (hojas 4–7) |

Para una sola tarjeta de resultado usa `resultado(n, formato)`, con `n` entre 1 y 10 y `formato` igual a `"media"` o `"quinta"`:

```python
Tarjetas.Tablas.Giro.resultado(7, "quinta")
```

## Más ejemplos

**Todas las especies con un diseño concreto, más dos fichas en blanco:**

```python
from bruja import Documento, Tarjetas

pj = Tarjetas.Personajes
doc = Documento().seccion("Personajes")
doc.add(p.simple() for p in pj.todos())
doc.add(pj.EnBlanco.simple(), pj.EnBlanco.simple())
doc.render("personajes.pdf")
```

**Una hoja por tabla de resultados, cada una con su nombre en el pie:**

```python
tb = Tarjetas.Tablas
doc = Documento()
for t in (tb.Pueblo, tb.Ladron, tb.Giro, tb.Hechizo):
    doc.seccion(t.titulo).add(t.por_resultado_5x2())
doc.render("resultados.pdf")
```

**Mezclar diseños y formatos en un mismo documento:**

```python
doc = Documento()
doc.add(Tarjetas.Historia.Introduccion.simple(),
        Tarjetas.Reglas.ComoJugar.simple())            # hoja 2×3
doc.add(Tarjetas.Tablas.Pueblo.media_altura())        # pasa a una hoja 2×6
doc.render("mezcla.pdf")
```

**Comparar dos diseños de la misma especie:**

```python
doc = Documento()
doc.add(Tarjetas.Personajes.Buho.diseno(d) for d in Tarjetas.Personajes.Buho.disenos())
doc.render("buho.pdf")
```

## Estructura del proyecto

```
.
├── LICENSE               # Texto legal de CC BY-SA 4.0
├── requirements.txt      # Dependencias (Playwright), también clave de la caché de pip en Actions
├── generar.py            # Script principal: mazo por defecto, ediciones publicadas, opciones de línea de órdenes y catálogo
├── .github/workflows/    # publicar-pdf.yml: genera los PDF y los adjunta a las releases
├── bruja/                # Paquete con toda la lógica
│   ├── __init__.py       # Exporta Documento, Tarjetas, Tarjeta, Modelo y diseno
│   ├── documento.py      # Documento: paginación por formato y secciones, exportación a HTML y PDF
│   ├── tarjetas.py       # Modelos (Personaje, Tabla, ComoJugar…), sus diseños y el catálogo Tarjetas
│   ├── estilo.py         # Paleta de colores y CSS común (hoja, marco, tablas, texto)
│   ├── iconos.py         # Ilustraciones SVG propias (animales e iconos de las tablas)
│   ├── datos.py          # Datos del juego: especies, rasgos y tablas d10
│   ├── tipografia.py     # Incrusta las fuentes en el HTML (y las descarga si faltan)
│   └── fuentes/          # Lora y Caladea (woff2, latin y latin-ext), fuentes.css y sus licencias OFL
├── tarjetas.html / .pdf  # Resultado del mazo por defecto
└── catalogo.pdf          # Resultado de --catalogo
```

## Añadir un diseño nuevo

1. En `bruja/tarjetas.py`, añade un método al modelo (por ejemplo, a `Personaje`) y márcalo con `@diseno`:

   ```python
   CSS_PJ_MINI = f'''
   & {{ padding: 2mm; }}
   .sp {{ font-size: 18pt; }}
   '''

   class Personaje(Modelo):
       ...
       @diseno
       def mini(self):
           """Descripción corta del diseño (aparece en disenos())."""
           return _tarjeta("pj-mini", CSS_PJ_MINI, f'<div class="sp">{self.nombre}</div>')
   ```

2. El primer argumento de `_tarjeta()` es el **ámbito**: una clase única del diseño bajo la que se aísla su CSS. Cada selector se prefija con `.pj-mini`, y `&` se refiere al propio marco de la tarjeta. Así, un diseño nuevo puede reutilizar nombres de clase (`.sp`, `.stats`…) sin romper los anteriores.

3. Para otro tamaño de tarjeta, pasa `formato="media"` o `formato="quinta"` a `_tarjeta()`. Si necesitas un formato nuevo, añádelo en `POR_PAGINA` (`documento.py`) y define su rejilla `.page.<formato>` en `estilo.py`.

4. Comprueba el resultado con `.venv/bin/python generar.py --catalogo`. El nuevo diseño aparece automáticamente en el catálogo.

## Historial de diseños

Los diseños de las fichas de personaje salen del historial de git:

| Commit | Diseño |
|---|---|
| `d22bb11` | `con_notas()` y `ComoJugar.simple()` |
| `fb165c5` | `simple()` y `ComoJugar.con_peligro_mortal()` (hoy `con_lios()`) |
| `fc46144` | `con_tiradas_de_inicio()`, versión con el dado recolocado y las líneas más espaciadas |

Se reprodujeron con las clases de la rama `master` y se compararon píxel a píxel con los PDF de cada commit: son idénticos. En esta versión infantil los diseños son los mismos, pero cambian los textos.

## Versión infantil

Esta rama adapta la historia y los textos para jugar con niños a partir de 7 años. Las mecánicas (tiradas, dificultades, peligro y magia) no cambian.

| Original | Versión infantil |
|---|---|
| *La bruja está muerta* · "Un RPG acerca de la muerte" | *El medallón de la bruja* · "Un juego de rol para animalitos valientes" |
| Un cazador de brujas asesina a la bruja | Un ladrón le roba su medallón mágico y ella cae en un sueño encantado |
| Vengarse, matar al cazador y llevar sus ojos al cuerpo en una semana | Recuperar el medallón y ponérselo al cuello antes de la próxima luna llena |
| Tabla "El cazador es…" (`Tablas.Cazador`) | Tabla "El ladrón es…" (`Tablas.Ladron`) |
| Peligro: "grave desgracia, atrapado… o muerte" (`con_peligro_mortal()`) | Peligro: "te atrapan, te pierdes… ¡o vuelves a casa a descansar!" (`con_lios()`) |
| Rasgo Fiereza (FIE): "…morder" | Rasgo Fuerza (FUE): "…cargar" |
| Astucia: "escabullirse, robar, esconderse" | Astucia: "escabullirse, esconderse, despistar" |
| Notas · Plan de venganza | Notas · Plan de rescate |

Cambios en las tablas d10:

| Tabla | Nº | Original | Versión infantil |
|---|---|---|---|
| Pueblo | 1 | Bajo el yugo de un barón | Gobernado por un barón gruñón |
| Pueblo | 3 | Controlado por un siniestro culto | Controlado por un club secreto |
| Pueblo | 4 | Devotamente religioso | Obsesionado con las normas |
| Pueblo | 6 | En guerra con las tribus del bosque | Enfadado con los animales del bosque |
| Pueblo | 9 | Sombrío y peligroso | Oscuro y lleno de niebla |
| Pueblo | 10 | Ofensivamente perfecto | Tan perfecto que resulta sospechoso |
| Ladrón | 1 | Fuerte y armado | Grandullón y forzudo |
| Ladrón | 3 | Borracho y violento | Torpe y gruñón |
| Ladrón | 4 | Piadoso y agresivo | Educado y tramposo |
| Ladrón | 5 | Oculto y cobarde | Escondido y miedica |
| Ladrón | 7 | Inteligente y cruel | Listísimo y presumido |
| Ladrón | 8 | Clonado y oculto | Disfrazado y escurridizo |
| Ladrón | 10 | Testarudo y salvaje | Testarudo y alborotador |
| Giro | 3, 4, 7 | El cazador… | El ladrón… |
| Giro | 6 | El cazador murió y lo están enterrando | Al ladrón se le ha perdido el medallón |
| Giro | 9 | El cazador atrapó a un sospechoso y lo está interrogando | El alguacil acusa del robo a un inocente |
| Giro | 10 | El pueblo lo odia | Todo el pueblo lo adora |
| Hechizo | 6 | Crear fuego | Hacer burbujas de colores |

## Licencia

© 2026 Óscar García. Este trabajo de diseño se distribuye bajo la licencia **[Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)**. El texto legal completo está en [`LICENSE`](LICENSE).

La licencia cubre el trabajo propio de este proyecto:

- El código Python (`generar.py` y el paquete `bruja/`).
- La maquetación y el diseño de las tarjetas (estilos, composición y formatos).
- Las ilustraciones SVG de `bruja/iconos.py`.
- Los PDF y HTML generados, **en lo que respecta a esos elementos**.

Puedes copiar, redistribuir, adaptar y usar este material para cualquier fin, incluso comercial, siempre que:

- **Atribución:** cites la autoría, enlaces a la licencia e indiques si has hecho cambios.
- **CompartirIgual:** si remezclas, transformas o creas a partir de él, distribuyas tu contribución bajo la misma licencia.

## Licencias de los trabajos relacionados

La licencia CC BY-SA 4.0 de este proyecto **no se aplica** a los siguientes trabajos, que conservan sus propias condiciones:

| Trabajo | Autoría | Condiciones |
|---|---|---|
| *[The Witch is Dead](https://gshowitt.itch.io/the-witch-is-dead)*: reglas, historia, tablas d10, especies y rasgos | Grant Howitt | Descarga gratuita ("paga lo que quieras") en itch.io. La página no indica ninguna licencia explícita, así que sus derechos pertenecen a su autor. |
| Traducción al castellano *La bruja está muerta*, en la que se basan los textos de las tarjetas | Traducción no acreditada en el documento de origen | Sujeta a los derechos del juego original |
| Fuentes [Lora](https://fonts.google.com/specimen/Lora) y [Caladea](https://fonts.google.com/specimen/Caladea), en `bruja/fuentes/` | © 2011 The Lora Project Authors (Cyreal); © 2012 The Caladea Project Authors (Huerta Tipográfica) | [SIL Open Font License 1.1](https://openfontlicense.org): textos completos en [`OFL-Lora.txt`](bruja/fuentes/OFL-Lora.txt) y [`OFL-Caladea.txt`](bruja/fuentes/OFL-Caladea.txt) |
| [Playwright](https://playwright.dev/python/), dependencia para generar el PDF (no se redistribuye) | Microsoft | [Apache 2.0](https://github.com/microsoft/playwright-python/blob/main/LICENSE) |

Por tanto, los textos del juego que aparecen en las tarjetas (historia, reglas, resultados de las tablas y estadísticas de las especies) son obra de Grant Howitt y se reproducen como material de ayuda para jugar. Si quieres **publicar o vender** tarjetas generadas con este proyecto, además de cumplir la CC BY-SA 4.0 deberás contar con el permiso del autor del juego para su contenido.

## Agradecimientos

Muchas gracias a **Grant Howitt** por *The Witch is Dead*. Con una sola página consiguió un juego lleno de humor, ternura y venganza, que se explica en un minuto y se recuerda durante años, y lo compartió generosamente con quien quisiera jugarlo. Su trabajo es la inspiración de este proyecto: estas tarjetas solo pretenden ser un homenaje y una ayuda para llevar su juego a la mesa en castellano.

Si te gusta el juego, visita su página en [itch.io](https://gshowitt.itch.io/the-witch-is-dead) y apoya su trabajo.

Gracias también a quien tradujo el juego al castellano, y a los autores de las fuentes Lora y Caladea por publicarlas bajo una licencia libre.
