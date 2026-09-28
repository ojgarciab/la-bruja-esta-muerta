"""Documento A4: coloca tarjetas en rejillas de 2x3 y lo exporta a HTML o PDF."""
from pathlib import Path

from .estilo import CSS_BASE, FONTS
from .tarjetas import Tarjeta

POR_PAGINA = 6


class Documento:
    """Colección ordenada de tarjetas agrupadas en secciones.

    Cada sección empieza en una página nueva y rotula el pie de sus hojas
    ("Personajes 1/2 · recorta por la línea discontinua").
    """

    def __init__(self, titulo="La bruja está muerta · Tarjetas"):
        self.titulo = titulo
        self._secciones = [["", []]]

    def seccion(self, etiqueta):
        """Empieza una sección nueva (y por tanto una página nueva)."""
        if self._secciones[-1][1]:
            self._secciones.append([etiqueta, []])
        else:
            self._secciones[-1][0] = etiqueta
        return self

    def add(self, *tarjetas):
        """Añade tarjetas o iterables de tarjetas a la sección actual."""
        for t in tarjetas:
            if isinstance(t, Tarjeta):
                self._secciones[-1][1].append(t)
            else:
                self.add(*t)
        return self

    def _paginas(self):
        secciones = [(e, ts) for e, ts in self._secciones if ts]
        total = sum(-(-len(ts) // POR_PAGINA) for _, ts in secciones)
        n = 0
        for etiqueta, ts in secciones:
            trozos = [ts[i:i + POR_PAGINA] for i in range(0, len(ts), POR_PAGINA)]
            for i, trozo in enumerate(trozos, 1):
                n += 1
                if not etiqueta:
                    rotulo = f"Página {n}/{total}"
                elif len(trozos) > 1:
                    rotulo = f"{etiqueta} {i}/{len(trozos)}"
                else:
                    rotulo = etiqueta
                yield rotulo, trozo

    def html(self):
        estilos = {}
        for _, ts in self._secciones:
            for t in ts:
                estilos.update(t.estilos)
        css = CSS_BASE + "\n".join(estilos.values())
        body = "".join(
            f'<section class="page">{"".join(t.html for t in trozo)}'
            f'<div class="credit">{rotulo} · recorta por la línea discontinua</div></section>'
            for rotulo, trozo in self._paginas())
        return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{self.titulo}</title>'
                f'{FONTS}<style>{css}</style></head><body>{body}</body></html>')

    def render(self, ruta):
        """Escribe el documento; la extensión (.pdf o .html) decide el formato."""
        ruta = Path(ruta)
        if ruta.suffix.lower() == ".html":
            ruta.write_text(self.html(), encoding="utf-8")
        elif ruta.suffix.lower() == ".pdf":
            _a_pdf(self.html(), ruta)
        else:
            raise ValueError(f"Formato no soportado: {ruta.suffix!r} (usa .pdf o .html)")
        print(f"Generado: {ruta}")
        return ruta


def _a_pdf(documento_html, ruta):
    """Imprime el HTML a PDF A4 con Chrome (vía Playwright)."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(channel="chrome")
        except Exception:
            browser = p.chromium.launch()  # requiere `playwright install chromium`
        pg = browser.new_page()
        pg.set_content(documento_html, wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        pg.pdf(path=str(ruta), format="A4", print_background=True,
               prefer_css_page_size=True, margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
        browser.close()
