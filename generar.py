#!/usr/bin/env python3
"""Genera las tarjetas A4 de 'La bruja está muerta'.

    python generar.py              -> tarjetas.html + tarjetas.pdf (diseños actuales)
    python generar.py --sin-pdf    -> solo tarjetas.html
    python generar.py --media      -> tablas de tiradas de historia a media altura
                                      (12 por hoja) y --copias N para repetirlas
    python generar.py --resultados -> añade una tarjeta de media altura por cada
                                      resultado de las tablas (40 tarjetas)
    python generar.py --catalogo   -> catalogo.pdf con todos los diseños de cada modelo
"""
import sys
from pathlib import Path

from bruja import Documento, Tarjetas

AQUI = Path(__file__).parent


def mazo(media=False, copias=1, resultados=False):
    """El mazo de juego con los diseños elegidos de cada tarjeta.

    media=True imprime las cuatro tablas d10 a media altura; copias repite
    esas tablas (p. ej. 3 copias llenan una hoja de 12). resultados=True añade
    las tablas partidas en una tarjeta por resultado.
    """
    pj, tb = Tarjetas.Personajes, Tarjetas.Tablas
    doc = Documento()
    doc.seccion("Personajes")
    doc.add(p.con_tiradas_de_inicio() for p in pj.todos())
    doc.add(pj.EnBlanco.con_tiradas_de_inicio(), pj.EnBlanco.con_tiradas_de_inicio())
    doc.seccion("Tiradas de historia")
    doc.add(Tarjetas.Historia.Introduccion.simple(), Tarjetas.Reglas.ComoJugar.con_peligro_mortal())
    tablas = (tb.Pueblo, tb.Cazador, tb.Giro, tb.Hechizo)
    doc.add((t.media_altura() if media else t.simple()) for _ in range(copias) for t in tablas)
    if resultados:
        doc.seccion("Resultados")
        doc.add(t.por_resultado() for t in tablas)
    return doc


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
    if "--catalogo" in sys.argv:
        catalogo().render(AQUI / "catalogo.pdf")
    else:
        copias = int(sys.argv[sys.argv.index("--copias") + 1]) if "--copias" in sys.argv else 1
        doc = mazo(media="--media" in sys.argv, copias=copias, resultados="--resultados" in sys.argv)
        doc.render(AQUI / "tarjetas.html")
        if "--sin-pdf" not in sys.argv:
            doc.render(AQUI / "tarjetas.pdf")
