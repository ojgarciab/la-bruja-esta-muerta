#!/usr/bin/env python3
"""Genera las tarjetas A4 de 'La bruja está muerta'.

    python generar.py              -> tarjetas.html + tarjetas.pdf (diseños actuales),
                                      con una hoja 2x5 por tabla de resultados al final
    python generar.py --sin-pdf    -> solo tarjetas.html
    python generar.py --media      -> tablas de tiradas de historia a media altura
                                      (12 por hoja) y --copias N para repetirlas
    python generar.py --resultados -> tarjetas por resultado en 2x6 (media altura)
                                      en vez de 2x5
    python generar.py --sin-resultados -> sin las tarjetas por resultado
    python generar.py --catalogo   -> catalogo.pdf con todos los diseños de cada modelo
    python generar.py --publicacion [DIR] -> los PDF de EDICIONES en DIR (por defecto, dist/)
"""
import sys
from pathlib import Path

from bruja import Documento, Tarjetas

AQUI = Path(__file__).parent


def mazo(media=False, copias=1, resultados="por_resultado_5x2"):
    """El mazo de juego con los diseños elegidos de cada tarjeta.

    media=True imprime las cuatro tablas d10 a media altura; copias repite
    esas tablas (p. ej. 3 copias llenan una hoja de 12). resultados es el
    diseño con el que añadir las tablas partidas en una tarjeta por resultado
    ("por_resultado" o "por_resultado_5x2"); None no las añade.
    """
    pj, tb = Tarjetas.Personajes, Tarjetas.Tablas
    doc = Documento()
    doc.seccion("Tiradas de historia")  # primero: descripción, reglas y chuletas de las tablas
    doc.add(Tarjetas.Historia.Introduccion.simple(), Tarjetas.Reglas.ComoJugar.con_peligro_mortal())
    tablas = (tb.Pueblo, tb.Cazador, tb.Giro, tb.Hechizo)
    doc.add((t.media_altura() if media else t.simple()) for _ in range(copias) for t in tablas)
    doc.seccion("Personajes")
    doc.add(p.con_tiradas_de_inicio() for p in pj.todos())
    doc.add(pj.EnBlanco.con_tiradas_de_inicio(), pj.EnBlanco.con_tiradas_de_inicio())
    if resultados == "por_resultado_5x2":
        for t in tablas:  # 10 tarjetas = una hoja justa por tabla
            doc.seccion(t.titulo).add(t.por_resultado_5x2())
    elif resultados:
        doc.seccion("Resultados")
        doc.add(t.diseno(resultados) for t in tablas)
    return doc


def _tiradas_de_historia(doc):
    """Primera hoja: descripción del juego, reglas y las cuatro tablas d10 completas."""
    tb = Tarjetas.Tablas
    doc.seccion("Tiradas de historia")
    doc.add(Tarjetas.Historia.Introduccion.simple(), Tarjetas.Reglas.ComoJugar.con_peligro_mortal())
    doc.add(t.simple() for t in (tb.Pueblo, tb.Cazador, tb.Giro, tb.Hechizo))
    return doc


def edicion_personajes_para_rellenar():
    """Tiradas de historia y fichas con líneas para apuntar pueblo, cazador y hechizo.

    Se escribe en ellas en cada partida, así que suelen durar una o dos partidas.
    """
    pj = Tarjetas.Personajes
    doc = _tiradas_de_historia(Documento()).seccion("Personajes")
    doc.add(p.con_tiradas_de_inicio() for p in pj.todos())
    doc.add(pj.EnBlanco.con_tiradas_de_inicio(), pj.EnBlanco.con_tiradas_de_inicio())
    return doc


def edicion_personajes_reutilizables():
    """Tiradas de historia, fichas sin campos de partida y una hoja 2x5 por tabla.

    Pueblo, cazador y hechizo se reparten con las tarjetas de resultados en vez de
    escribirse en la ficha, así que las fichas sirven para muchas partidas.
    """
    pj, tb = Tarjetas.Personajes, Tarjetas.Tablas
    doc = _tiradas_de_historia(Documento()).seccion("Personajes")
    doc.add(p.simple() for p in pj.todos())
    doc.add(pj.EnBlanco.simple(), pj.EnBlanco.simple())  # para crear dos personajes propios
    for t in (tb.Pueblo, tb.Cazador, tb.Giro, tb.Hechizo):
        doc.seccion(t.titulo).add(t.por_resultado_5x2())
    return doc


# Los PDF que se publican en cada versión (GitHub Releases): nombre de fichero -> generador
EDICIONES = {
    "la-bruja-esta-muerta-tarjetas-de-personajes-para-rellenar.pdf": edicion_personajes_para_rellenar,
    "la-bruja-esta-muerta-tarjetas-de-personajes-reutilizables.pdf": edicion_personajes_reutilizables,
}


def catalogo():
    """Una muestra de cada diseño disponible, para compararlos."""
    doc = Documento("La bruja está muerta · Catálogo de diseños")
    for grupo, modelos in Tarjetas.modelos().items():
        if grupo == "Personajes":
            disenos = Tarjetas.Personajes.Buho.disenos()
            for d in disenos:
                doc.seccion(f"Personajes · {d}")
                doc.add(Tarjetas.Personajes.Buho.diseno(d), Tarjetas.Personajes.EnBlanco.diseno(d))
            continue
        doc.seccion(grupo)
        disenos = sorted({d for m in modelos.values() for d in m.disenos()})
        doc.add(m.diseno(d) for d in disenos for m in modelos.values() if d in m.disenos())
    return doc


if __name__ == "__main__":
    if "--publicacion" in sys.argv:
        i = sys.argv.index("--publicacion") + 1
        destino = Path(sys.argv[i]) if i < len(sys.argv) and not sys.argv[i].startswith("--") else AQUI / "dist"
        destino.mkdir(parents=True, exist_ok=True)
        for nombre, generador in EDICIONES.items():
            generador().render(destino / nombre)
    elif "--catalogo" in sys.argv:
        catalogo().render(AQUI / "catalogo.pdf")
    else:
        copias = int(sys.argv[sys.argv.index("--copias") + 1]) if "--copias" in sys.argv else 1
        resultados = (None if "--sin-resultados" in sys.argv
                      else "por_resultado" if "--resultados" in sys.argv else "por_resultado_5x2")
        doc = mazo(media="--media" in sys.argv, copias=copias, resultados=resultados)
        doc.render(AQUI / "tarjetas.html")
        if "--sin-pdf" not in sys.argv:
            doc.render(AQUI / "tarjetas.pdf")
