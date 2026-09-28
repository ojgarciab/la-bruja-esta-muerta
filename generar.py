#!/usr/bin/env python3
"""Genera las tarjetas A4 de 'La bruja está muerta'.

    python generar.py              -> tarjetas.html + tarjetas.pdf (diseños actuales)
    python generar.py --sin-pdf    -> solo tarjetas.html
    python generar.py --catalogo   -> catalogo.pdf con todos los diseños de cada modelo
"""
import sys
from pathlib import Path

from bruja import Documento, Tarjetas

AQUI = Path(__file__).parent


def mazo():
    """El mazo de juego con los diseños elegidos de cada tarjeta."""
    pj, tb = Tarjetas.Personajes, Tarjetas.Tablas
    doc = Documento()
    doc.seccion("Personajes")
    doc.add(p.con_tiradas_de_inicio() for p in pj.todos())
    doc.add(pj.EnBlanco.con_tiradas_de_inicio(), pj.EnBlanco.con_tiradas_de_inicio())
    doc.seccion("Tiradas de historia")
    doc.add(Tarjetas.Historia.Introduccion.simple(),
            Tarjetas.Reglas.ComoJugar.con_peligro_mortal(),
            tb.Pueblo.simple(), tb.Cazador.simple(), tb.Giro.simple(), tb.Hechizo.simple())
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
        doc.add(m.diseno(d) for m in modelos.values() for d in m.disenos())
    return doc


if __name__ == "__main__":
    if "--catalogo" in sys.argv:
        catalogo().render(AQUI / "catalogo.pdf")
    else:
        doc = mazo()
        doc.render(AQUI / "tarjetas.html")
        if "--sin-pdf" not in sys.argv:
            doc.render(AQUI / "tarjetas.pdf")
