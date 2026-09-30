"""Tarjetas imprimibles A4 para 'El medallón de la bruja'.

    from bruja import Documento, Tarjetas

    doc = Documento()
    doc.add(Tarjetas.Personajes.Buho.simple())
    doc.add(Tarjetas.Personajes.Gato.con_notas())
    doc.add(Tarjetas.Personajes.Buho.con_tiradas_de_inicio())
    doc.render("documento.pdf")
"""
from .documento import Documento
from .tarjetas import Modelo, Tarjeta, Tarjetas, diseno

__all__ = ["Documento", "Modelo", "Tarjeta", "Tarjetas", "diseno"]
