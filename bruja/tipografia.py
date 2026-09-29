"""Fuentes Lora y Caladea (licencia OFL) incrustadas en el HTML.

Se guardan en bruja/fuentes/ para que generar el PDF no dependa de la red:
si faltan, se descargan una vez de Google Fonts (subconjuntos latin y latin-ext).
"""
import base64
import re
import urllib.request
from pathlib import Path

DIR = Path(__file__).with_name("fuentes")
CSS_LOCAL = DIR / "fuentes.css"
URL = ("https://fonts.googleapis.com/css2?family=Caladea:ital,wght@0,400;0,700;1,400;1,700"
       "&family=Lora:ital,wght@0,400;0,700;1,400;1,700&display=block")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
SUBCONJUNTOS = ("latin", "latin-ext")


def _get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30) as r:
        return r.read()


def descargar():
    """Descarga las fuentes a bruja/fuentes/ y escribe un fuentes.css con rutas locales."""
    DIR.mkdir(exist_ok=True)
    css = _get(URL).decode()
    bloques = re.findall(r"/\* ([\w-]+) \*/\s*(@font-face \{.*?\})", css, re.S)
    salida = []
    for subconjunto, bloque in bloques:
        if subconjunto not in SUBCONJUNTOS:
            continue
        url = re.search(r"url\((https://[^)]+)\)", bloque).group(1)
        familia = re.search(r"font-family: '([^']+)'", bloque).group(1).lower()
        estilo = re.search(r"font-style: (\w+)", bloque).group(1)
        peso = re.search(r"font-weight: (\d+)", bloque).group(1)
        nombre = f"{familia}-{estilo}-{peso}-{subconjunto}.woff2"
        if not (DIR / nombre).exists():
            (DIR / nombre).write_bytes(_get(url))
        salida.append(f"/* {subconjunto} */\n" + bloque.replace(url, nombre))
    CSS_LOCAL.write_text("\n".join(salida) + "\n", encoding="utf-8")


def css_incrustado():
    """@font-face con las fuentes como data: URI (descarga la primera vez si faltan)."""
    if not CSS_LOCAL.exists():
        descargar()
    css = CSS_LOCAL.read_text(encoding="utf-8")

    def a_data_uri(m):
        datos = base64.b64encode((DIR / m.group(1)).read_bytes()).decode()
        return f"url(data:font/woff2;base64,{datos})"

    return re.sub(r"url\(([\w.-]+\.woff2)\)", a_data_uri, css)
