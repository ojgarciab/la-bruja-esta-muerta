"""Modelos de tarjeta y sus diseños.

Cada modelo (un personaje, una tabla, las reglas…) expone un método por diseño,
marcado con @diseno. Llamarlo devuelve una Tarjeta lista para Documento.add():

    Tarjetas.Personajes.Buho.con_tiradas_de_inicio()
    Tarjetas.Reglas.ComoJugar.con_lios()

El CSS de cada diseño se aísla bajo una clase propia (p. ej. .pj-notas), así que
un diseño nuevo puede reutilizar nombres de clase sin romper los antiguos.
"""
import html
from dataclasses import dataclass, field

from .datos import ESPECIES, GIRO, HECHIZO, LADRON, PUEBLO, RASGOS
from .estilo import ACC, FOOT, INK, TINT, W
from .iconos import icon


@dataclass(frozen=True)
class Tarjeta:
    html: str
    estilos: dict = field(default_factory=dict)  # {ámbito: css ya aislado}
    formato: str = "completa"  # "completa" (99x95 mm, 2x3), "media" (99x47.5 mm, 2x6) o "quinta" (99x57 mm, 2x5)


def aislar(ambito, css):
    """Prefija cada selector con .ambito; '&' se refiere al propio marco."""
    out = []
    for linea in css.strip().splitlines():
        sel, sep, cuerpo = linea.partition("{")
        if not sep:
            out.append(linea)
            continue
        sels = [s.strip() for s in sel.split(",")]
        sels = [s.replace("&", f".{ambito}", 1) if s.startswith("&") else f".{ambito} {s}" for s in sels]
        out.append(", ".join(sels) + " {" + cuerpo)
    return "\n".join(out)


def diseno(metodo):
    """Marca un método de un Modelo como diseño seleccionable."""
    metodo.es_diseno = True
    return metodo


class Modelo:
    def disenos(self):
        """Nombres de los diseños disponibles para este modelo."""
        return [n for n in dir(type(self)) if getattr(getattr(type(self), n), "es_diseno", False)]

    def diseno(self, nombre):
        """Elige un diseño por nombre: útil en bucles o desde la línea de órdenes."""
        if nombre not in self.disenos():
            raise ValueError(f"{self!r} no tiene el diseño {nombre!r}; disponibles: {', '.join(self.disenos())}")
        return getattr(self, nombre)()


def _tarjeta(ambito, css, interior, clases="", formato="completa"):
    return Tarjeta(f'<div class="card"><div class="frame {ambito} {clases}">{interior}</div></div>',
                   {ambito: aislar(ambito, css)}, formato)


# ---------------------------------------------------------------- personajes

CSS_PJ_NOTAS = f'''
.top {{ display: flex; gap: 3mm; align-items: center; }}
.portrait {{ width: 29mm; height: 29mm; flex: none; border-radius: 50%; background: {TINT}; border: 0.5mm solid {ACC}; display: flex; align-items: center; justify-content: center; }}
.portrait .ico {{ width: 22mm; height: 22mm; }}
.portrait.blank {{ background: #fff; border-style: dashed; }}
.portrait.blank span {{ font-size: 7pt; color: #999; font-style: italic; }}
.ttl {{ flex: 1; min-width: 0; }}
.sp {{ font-family: Lora; font-weight: 700; font-size: 21pt; line-height: 1; color: {INK}; }}
.sp.blankline {{ font-size: 11pt; display: flex; align-items: flex-end; gap: 1.5mm; padding-top: 3mm; }}
.sub {{ font-size: 7pt; color: {ACC}; font-style: italic; margin: 1mm 0 3mm; }}
.line {{ display: flex; align-items: flex-end; gap: 1.5mm; font-size: 8.5pt; margin-top: 1.2mm; }}
.line b, .notes b, .danger .lbl {{ font-family: Lora; font-weight: 700; font-size: 8pt; text-transform: uppercase; letter-spacing: .04em; }}
.fill {{ flex: 1; border-bottom: 0.3mm solid {INK}; height: 4.5mm; }}
.stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.6mm; margin: 2.6mm 0 0.8mm; }}
.stat {{ border: 0.4mm solid {INK}; border-radius: 2mm; text-align: center; padding: 1mm 0.8mm 1.1mm; background: #fff; }}
.stat .ab {{ font-family: Lora; font-weight: 700; font-size: 7.5pt; background: {INK}; color: #fff; border-radius: 1mm; padding: .3mm 0; letter-spacing: .05em; }}
.stat .val {{ font-family: Lora; font-weight: 700; font-size: 17pt; line-height: 1.15; height: 7.4mm; }}
.stat .hint {{ font-size: 5.3pt; line-height: 1.12; color: #555; height: 4.4mm; }}
.danger {{ display: flex; align-items: center; gap: 1.5mm; margin-top: 2mm; }}
.danger .lbl {{ margin-right: 1mm; }}
.danger i {{ width: 4.6mm; height: 4.6mm; border: 0.4mm solid {INK}; border-radius: 50%; display: inline-block; }}
.notes {{ margin-top: 1.8mm; }}
.rule {{ border-bottom: 0.25mm solid #aaa; height: 4.1mm; }}
'''

CSS_PJ_SIMPLE = f'''
& {{ padding-top: 2.6mm; }}
.top {{ display: flex; gap: 4mm; align-items: center; }}
.portrait {{ width: 33mm; height: 33mm; flex: none; border-radius: 50%; background: {TINT}; border: 0.6mm solid {ACC}; display: flex; align-items: center; justify-content: center; }}
.portrait .ico {{ width: 25mm; height: 25mm; }}
.portrait.blank {{ background: #fff; border-style: dashed; }}
.portrait.blank span {{ font-size: 8pt; color: #999; font-style: italic; }}
.ttl {{ flex: 1; min-width: 0; }}
.sp {{ font-family: Lora; font-weight: 700; font-size: 26pt; line-height: 1; color: {INK}; }}
.sp.blankline {{ font-size: 12pt; display: flex; align-items: flex-end; gap: 1.5mm; }}
.sub {{ font-size: 8pt; color: {ACC}; font-style: italic; margin-top: 1.6mm; }}
.fill {{ flex: 1; border-bottom: 0.3mm solid {INK}; height: 5mm; }}
.stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 2mm; margin: 3mm 0 0; }}
.stat {{ border: 0.45mm solid {INK}; border-radius: 2mm; text-align: center; padding: 1.2mm 1mm 1.4mm; background: #fff; }}
.stat .ab {{ font-family: Lora; font-weight: 700; font-size: 8.5pt; background: {INK}; color: #fff; border-radius: 1mm; padding: .4mm 0; letter-spacing: .05em; }}
.stat .val {{ font-family: Lora; font-weight: 700; font-size: 24pt; line-height: 1.1; height: 10.5mm; }}
.stat .hint {{ font-size: 6.2pt; line-height: 1.15; color: #555; height: 7.4mm; }}
.danger {{ margin-top: 3mm; border: 0.45mm solid {ACC}; border-radius: 2mm; background: {TINT}; padding: 2mm 2.6mm 1.8mm; }}
.dtop {{ display: flex; align-items: center; justify-content: space-between; }}
.danger .lbl {{ font-family: Lora; font-weight: 700; font-size: 10pt; text-transform: uppercase; letter-spacing: .05em; }}
.danger i {{ width: 6mm; height: 6mm; border: 0.45mm solid {INK}; border-radius: 50%; display: inline-block; background: #fff; }}
.dnote {{ font-size: 6.8pt; font-style: italic; color: {INK}; margin-top: 1.4mm; text-align: center; }}
'''

CSS_PJ_TIRADAS = f'''
& {{ padding: 2.8mm 3mm 2.6mm; justify-content: space-between; }}
.badge {{ position: absolute; top: 1.2mm; right: 2mm; width: 11mm; height: 11mm; }}
.top {{ display: flex; gap: 3mm; align-items: center; }}
.portrait {{ width: 32mm; height: 32mm; flex: none; border-radius: 50%; background: {TINT}; border: 0.6mm solid {ACC}; display: flex; align-items: center; justify-content: center; }}
.portrait .ico {{ width: 24mm; height: 24mm; }}
.portrait.blank {{ background: #fff; border-style: dashed; }}
.portrait.blank span {{ font-size: 8pt; color: #999; font-style: italic; }}
.ttl {{ flex: 1; min-width: 0; }}
.sp {{ font-family: Lora; font-weight: 700; font-size: 21pt; line-height: 1; color: {INK}; height: 10mm; padding-right: 11mm; }}
.sp.blankline {{ display: flex; align-items: flex-end; height: 8mm; margin-bottom: 1mm; }}
.fill {{ flex: 1; border-bottom: 0.3mm solid {INK}; height: 5mm; }}
.stats {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.4mm; }}
.stat {{ display: flex; align-items: stretch; border: 0.45mm solid {INK}; border-radius: 1.8mm; overflow: hidden; height: 10.6mm; background: #fff; }}
.stat .val {{ flex: none; width: 8mm; background: {INK}; color: #fff; font-family: Lora; font-weight: 700; font-size: 18pt; display: flex; align-items: center; justify-content: center; }}
.stat .txt {{ flex: 1; min-width: 0; padding: .7mm .8mm; display: flex; flex-direction: column; justify-content: center; }}
.stat .ab {{ font-family: Lora; font-weight: 700; font-size: 5.8pt; text-transform: uppercase; letter-spacing: 0; line-height: 1.1; white-space: nowrap; }}
.stat .hint {{ font-size: 5.3pt; line-height: 1.12; color: #555; margin-top: .3mm; }}
.choices {{ flex: 1; display: flex; flex-direction: column; justify-content: space-evenly; padding: 1mm 0 2mm; }}
.choice {{ display: flex; align-items: flex-end; gap: 1.8mm; height: 8.4mm; }}
.choice b {{ font-family: Lora; font-weight: 700; font-size: 8.8pt; white-space: nowrap; padding-bottom: .4mm; }}
.choice .fill {{ height: 7mm; }}
.choice .num {{ flex: none; width: 7mm; height: 7mm; border: 0.4mm solid {ACC}; border-radius: 1.2mm; }}
.danger {{ border: 0.45mm solid {ACC}; border-radius: 2mm; background: {TINT}; padding: 1.8mm 2.6mm 1.6mm; }}
.dtop {{ display: flex; align-items: center; justify-content: space-between; }}
.danger .lbl {{ font-family: Lora; font-weight: 700; font-size: 10pt; text-transform: uppercase; letter-spacing: .05em; }}
.danger i {{ width: 6mm; height: 6mm; border: 0.45mm solid {INK}; border-radius: 50%; display: inline-block; background: #fff; }}
.dnote {{ font-size: 6.8pt; font-style: italic; color: {INK}; margin-top: 1.2mm; text-align: center; }}
&.blankchar .stat .val {{ background: #fff; border-right: 0.45mm solid {INK}; }}
'''

ELECCIONES = ["El pueblo es", "El ladrón es", "La bruja te enseñó"]


def _peligro(n=8):
    return ('<div class="danger"><div class="dtop"><span class="lbl">Peligro</span>' + '<i></i>' * n + '</div>'
            '<div class="dnote">Si tu tirada es <b>igual o menor</b> que tu peligro: te atrapan, te pierdes… ¡o vuelves a casa a descansar!</div></div>')


def _dado_d10(n=None):
    num = "" if n is None else n
    body, face, line = (ACC, INK, W) if n is not None else (W, W, ACC)
    outline = "" if n is not None else f' stroke="{ACC}" stroke-width="3.5" stroke-linejoin="round"'
    return f'''<svg class="badge" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
<path d="M50 3 L95 38 L95 62 L50 97 L5 62 L5 38 Z" fill="{body}"{outline}/>
<path d="M50 3 L80 56 L50 74 L20 56 Z" fill="{face}" opacity=".35"/>
<path d="M50 3 L80 56 L50 74 L20 56 Z M80 56 L95 62 M20 56 L5 62 M50 74 L50 97" stroke="{line}" stroke-width="2.6" fill="none" stroke-linejoin="round"/>
<text x="50" y="59" text-anchor="middle" font-size="{30 if n == 10 else 36}" font-family="Lora" font-weight="700" fill="{W}">{num}</text></svg>'''


class Personaje(Modelo):
    """Ficha de un animal; especie=None da una ficha en blanco."""

    def __init__(self, especie=None):
        self.especie = especie
        if especie:
            self.d10, self.nombre, self.icono, *self.valores = especie
        else:
            self.d10, self.nombre, self.icono, self.valores = None, None, None, [None] * 4

    def __repr__(self):
        return f"Personaje({self.nombre or 'en blanco'})"

    def _retrato(self):
        if self.especie:
            return f'<div class="portrait">{icon(self.icono)}</div>'
        return '<div class="portrait blank"><span>Retrato</span></div>'

    def _valores(self):
        return ["" if v is None else v for v in self.valores]

    @diseno
    def con_notas(self):
        """Diseño original: nombre, hechizo, peligro y notas del plan de rescate."""
        if self.especie:
            title = f'<div class="sp">{self.nombre}</div><div class="sub">Lindo animalito del bosque · d10 = {self.d10}</div>'
        else:
            title = '<div class="sp blankline">Especie: <span class="fill"></span></div><div class="sub">Lindo animalito del bosque</div>'
        stats = "".join(
            f'<div class="stat"><div class="ab">{a}</div><div class="val">{v}</div><div class="hint">{h}</div></div>'
            for (a, _, h), v in zip(RASGOS, self._valores()))
        return _tarjeta("pj-notas", CSS_PJ_NOTAS, f'''
  <div class="top">{self._retrato()}<div class="ttl">{title}
    <div class="line"><b>Nombre</b><span class="fill"></span></div></div></div>
  <div class="stats">{stats}</div>
  <div class="line"><b>Hechizo</b><span class="fill"></span></div>
  <div class="danger"><span class="lbl">Peligro</span>{'<i></i>' * 8}</div>
  <div class="notes"><b>Notas · Plan de rescate</b><div class="rule"></div><div class="rule"></div><div class="rule"></div></div>
  {FOOT}''')

    @diseno
    def simple(self):
        """Retrato, rasgos grandes y recuadro de peligro con la regla de desgracia."""
        if self.especie:
            title = f'<div class="sp">{self.nombre}</div><div class="sub">Lindo animalito del bosque · d10 = {self.d10}</div>'
        else:
            title = '<div class="sp blankline">Especie: <span class="fill"></span></div><div class="sub">Lindo animalito del bosque</div>'
        stats = "".join(
            f'<div class="stat"><div class="ab">{a}</div><div class="val">{v}</div><div class="hint">{h}</div></div>'
            for (a, _, h), v in zip(RASGOS, self._valores()))
        return _tarjeta("pj-simple", CSS_PJ_SIMPLE, f'''
  <div class="top">{self._retrato()}<div class="ttl">{title}</div></div>
  <div class="stats">{stats}</div>
  {_peligro()}
  {FOOT}''')

    @diseno
    def con_tiradas_de_inicio(self):
        """Rasgos junto al retrato, d10 en la esquina y líneas para pueblo, ladrón y hechizo."""
        title = f'<div class="sp">{self.nombre}</div>' if self.especie else '<div class="sp blankline"><span class="fill"></span></div>'
        stats = "".join(
            f'<div class="stat"><div class="val">{v}</div><div class="txt"><div class="ab">{nom}</div><div class="hint">{h}</div></div></div>'
            for (_, nom, h), v in zip(RASGOS, self._valores()))
        choices = "".join(f'<div class="choice"><b>{c}</b><span class="fill"></span><span class="num"></span></div>' for c in ELECCIONES)
        return _tarjeta("pj-tiradas", CSS_PJ_TIRADAS, f'''
  {_dado_d10(self.d10)}
  <div class="top">{self._retrato()}<div class="ttl">{title}<div class="stats">{stats}</div></div></div>
  <div class="choices">{choices}</div>
  {_peligro()}''', "" if self.especie else "blankchar")


# ------------------------------------------------------------ historia y reglas

class Introduccion(Modelo):
    def __repr__(self):
        return "Introduccion"

    @diseno
    def simple(self):
        return _tarjeta("tx-intro", "", f'''
  <div class="head">{icon("caldero", "hico")}<div><div class="ht">El medallón de la bruja</div><div class="hs">Un juego de rol para animalitos valientes</div></div></div>
  <p class="prose"><span class="cap">É</span>rase una vez una bruja amable, sabia y hermosa que vivía en el bosque con su familiar, y su vida era pacífica y feliz… hasta que un <b>ladrón</b> se coló de noche en su cabaña y le robó su <b>medallón mágico</b>. Sin él, la bruja ha caído en un <b>SUEÑO ENCANTADO</b> y no puede despertar.</p>
  <p class="prose">Pero si recuperas el medallón y se lo pones otra vez al cuello antes de <b>la próxima luna llena</b>, ella despertará. O eso has oído. Y quizás el ladrón aprenda que robar no está bien.</p>
  <p class="prose big">Eres un lindo animalito del bosque. El ladrón se ha escondido en el pueblo, el muy granuja. <b>¡Encuéntralo!</b></p>
  {FOOT}''')


class ComoJugar(Modelo):
    DIFICULTADES = [(6, "Simple"), (7, "Básica"), (8, "Desafiante"), (9, "Difícil"), (10, "Casi imposible")]

    def __repr__(self):
        return "ComoJugar"

    def _tarjeta(self, ambito, extra=""):
        chips = "".join(f'<div class="chip"><b>{n}</b><span>{t}</span></div>' for n, t in self.DIFICULTADES)
        return _tarjeta(ambito, "", f'''
  <div class="head">{icon("dado", "hico")}<div><div class="ht">Cómo jugar</div><div class="hs">Tira 1d10 + tu rasgo más relevante</div></div></div>
  <p class="prose">El GM te dice qué número debes <b>igualar o superar</b>:</p>
  <div class="chips">{chips}</div>
  <p class="prose">Si la tarea es peligrosa y fallas, ganas <b>1 punto de PELIGRO</b>. <b>Usar magia SIEMPRE es peligroso.</b> Los PNJ no tiran dados: tú estás obligado a tirar. Reduce tu peligro resolviendo tus problemas o huyendo de ellos.</p>{extra}
  <p class="prose small">Recuerda: casi todo lo que es normal para un humano es muy difícil para un animal, salvo que lo dividas en pasos pequeños. No tienes pulgares oponibles y solo sabes del mundo humano lo que te enseñó la bruja. Puedes hablar con animales de tu especie o similares.</p>
  {FOOT}''')

    @diseno
    def simple(self):
        """Reglas originales."""
        return self._tarjeta("rg-simple")

    @diseno
    def con_lios(self):
        """Añade que sacar igual o menos que el peligro te mete en un buen lío."""
        return self._tarjeta("rg-lios", '''
  <p class="prose">Si sacas una tirada <b>igual o menor</b> que tus puntos de peligro, te metes en un <b>buen lío</b>: te <b>atrapan</b>, te <b>pierdes</b> o tienes que <b>volver a casa</b> a descansar.</p>''')


CSS_TB_MEDIA = f'''
& {{ padding: 1.5mm 2.4mm 1.3mm; border-radius: 2.6mm; }}
.head {{ gap: 1.8mm; padding-bottom: .8mm; margin-bottom: .6mm; border-bottom: 0.35mm solid {INK}; }}
.hico {{ width: 7mm; height: 7mm; }}
.ht {{ font-size: 10.5pt; line-height: 1; }}
.hs {{ font-size: 5.8pt; margin-top: .3mm; }}
.d10 {{ font-size: 7pt; padding: .4mm 1.3mm; border-radius: 1.1mm; }}
.grid {{ column-gap: 2.4mm; row-gap: 0; margin-bottom: 0; min-height: 0; }}
.grid li {{ gap: 1.2mm; font-size: 7pt; line-height: 1.04; min-height: 0; }}
.grid .n {{ width: 4mm; height: 4mm; font-size: 5.8pt; }}
.grid li:nth-child(5n) {{ border-bottom: none; }}
&.secret .head {{ border-bottom-style: dashed; }}
&.secret .grid .n {{ background: {ACC}; }}
'''

CSS_TB_RESULTADO = f'''
& {{ padding: 1.8mm 3mm 2mm; }}
.head {{ gap: 2mm; padding-bottom: 1mm; margin-bottom: 0; border-bottom: 0.35mm solid {INK}; }}
.hico {{ width: 8mm; height: 8mm; }}
.ht {{ font-size: 12pt; line-height: 1; }}
.hs {{ font-size: 6pt; margin-top: .3mm; }}
.res {{ flex: 1; display: flex; align-items: center; gap: 3.5mm; min-height: 0; }}
.badge {{ flex: none; width: 19mm; height: 19mm; }}
.txt {{ flex: 1; font-size: 16pt; line-height: 1.15; }}
.txt.largo {{ font-size: 14pt; }}
&.secret .head {{ border-bottom-style: dashed; }}
'''

CSS_TB_RESULTADO_5X2 = f'''
& {{ padding: 2.2mm 3.4mm 2.4mm; }}
.head {{ gap: 2.2mm; padding-bottom: 1.2mm; margin-bottom: 0; border-bottom: 0.4mm solid {INK}; }}
.hico {{ width: 9.5mm; height: 9.5mm; }}
.ht {{ font-size: 13pt; line-height: 1; }}
.hs {{ font-size: 6.6pt; margin-top: .4mm; }}
.res {{ flex: 1; display: flex; align-items: center; gap: 4mm; min-height: 0; }}
.badge {{ flex: none; width: 24mm; height: 24mm; }}
.txt {{ flex: 1; font-size: 18pt; line-height: 1.15; }}
.txt.largo {{ font-size: 15.5pt; }}
&.secret .head {{ border-bottom-style: dashed; }}
'''


class Tabla(Modelo):
    """Tabla d10 de diez entradas en dos columnas."""

    def __init__(self, titulo, icono, entradas, subtitulo, secreta=False):
        self.titulo, self.icono, self.entradas, self.subtitulo, self.secreta = titulo, icono, entradas, subtitulo, secreta

    def __repr__(self):
        return f"Tabla({self.titulo})"

    @diseno
    def simple(self):
        rows = "".join(f'<li><span class="n">{i}</span><span>{html.escape(t)}</span></li>' for i, t in enumerate(self.entradas, 1))
        return _tarjeta("tb-simple", "", f'''
  <div class="head">{icon(self.icono, "hico")}<div><div class="ht">{self.titulo}</div><div class="hs">{self.subtitulo}</div></div><div class="d10">d10</div></div>
  <ol class="grid">{rows}</ol>
  {FOOT}''', "tbl secret" if self.secreta else "tbl")

    @diseno
    def media_altura(self):
        """Mitad de alto (99x47.5 mm, 12 por hoja): cabecera compacta y sin pie."""
        rows = "".join(f'<li><span class="n">{i}</span><span>{html.escape(t)}</span></li>' for i, t in enumerate(self.entradas, 1))
        return _tarjeta("tb-media", CSS_TB_MEDIA, f'''
  <div class="head">{icon(self.icono, "hico")}<div><div class="ht">{self.titulo}</div><div class="hs">{self.subtitulo}</div></div><div class="d10">d10</div></div>
  <ol class="grid">{rows}</ol>''', "tbl secret" if self.secreta else "tbl", formato="media")

    def resultado(self, n, formato="media"):
        """Tarjeta con un único resultado (n = 1..10): formato "media" (2x6) o "quinta" (2x5)."""
        texto = self.entradas[n - 1]
        largo = " largo" if len(texto) > 40 else ""
        ambito, css = ("tb-resultado", CSS_TB_RESULTADO) if formato == "media" else ("tb-resultado-5x2", CSS_TB_RESULTADO_5X2)
        return _tarjeta(ambito, css, f'''
  <div class="head">{icon(self.icono, "hico")}<div><div class="ht">{self.titulo}</div><div class="hs">{self.subtitulo}</div></div></div>
  <div class="res">{_dado_d10(n)}<div class="txt{largo}">{html.escape(texto)}</div></div>''',
                        "tbl secret" if self.secreta else "tbl", formato=formato)

    @diseno
    def por_resultado(self):
        """La tabla partida en 10 tarjetas de media altura (2x6 por hoja), una por resultado."""
        return [self.resultado(n) for n in range(1, len(self.entradas) + 1)]

    @diseno
    def por_resultado_5x2(self):
        """La tabla partida en 10 tarjetas de 99x57 mm (2x5): cada tabla ocupa una hoja justa."""
        return [self.resultado(n, "quinta") for n in range(1, len(self.entradas) + 1)]


# ------------------------------------------------------------------- catálogo

class Tarjetas:
    """Punto de entrada: Tarjetas.<grupo>.<modelo>.<diseño>()."""

    class Personajes:
        Zorro, Gato, Sapo, Arana, Buho, Liebre, Urraca, Cuervo, Perro, Rata = (Personaje(e) for e in ESPECIES)
        EnBlanco = Personaje(None)

        @classmethod
        def todos(cls):
            """Las diez especies en orden de d10 (sin fichas en blanco)."""
            return [cls.Zorro, cls.Gato, cls.Sapo, cls.Arana, cls.Buho,
                    cls.Liebre, cls.Urraca, cls.Cuervo, cls.Perro, cls.Rata]

    class Historia:
        Introduccion = Introduccion()

    class Reglas:
        ComoJugar = ComoJugar()

    class Tablas:
        Pueblo = Tabla("El pueblo es…", "pueblo", PUEBLO, "Tirad para saber cómo es el pueblo")
        Ladron = Tabla("El ladrón es…", "ladron", LADRON, "Tirad para conocer a quien robó el medallón")
        Giro = Tabla("El giro", "giro", GIRO, "Solo para el GM · tira en secreto", secreta=True)
        Hechizo = Tabla("Tu bruja te enseñó…", "hechizo", HECHIZO, "Un hechizo · usar magia siempre es peligroso")

    @classmethod
    def modelos(cls):
        """Todos los modelos, agrupados: {'Personajes': {'Zorro': …}, …}."""
        grupos = {}
        for g in ("Personajes", "Historia", "Reglas", "Tablas"):
            ns = getattr(cls, g)
            grupos[g] = {n: m for n, m in vars(ns).items() if isinstance(m, Modelo)}
        return grupos
