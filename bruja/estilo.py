"""Paleta, fuentes y CSS común a todas las tarjetas (hoja A4 con rejilla 2x3)."""

INK = "#2f2340"
ACC = "#6b3f8f"
TINT = "#efe8f4"
W = "#ffffff"

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caladea:ital,wght@0,400;0,700;1,400;1,700&family=Lora:ital,wght@0,400;0,700;1,400;1,700&display=block">'

FOOT = '<div class="foot">La bruja está muerta · un RPG acerca de la muerte</div>'

CSS_BASE = f'''
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ background: #fff; color: {INK}; font-family: "Caladea", "Liberation Serif", serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.page {{ width: 210mm; height: 297mm; padding: 6mm; display: grid; grid-template-columns: 99mm 99mm; grid-template-rows: repeat(3, 95mm); page-break-after: always; position: relative; }}
.page:last-child {{ page-break-after: auto; }}
.card {{ outline: 0.25mm dashed #9a9a9a; outline-offset: -0.125mm; padding: 2.6mm; overflow: hidden; }}
.frame {{ height: 100%; border: 0.6mm solid {INK}; border-radius: 3mm; padding: 2.6mm 3mm 2mm; position: relative; display: flex; flex-direction: column; box-shadow: inset 0 0 0 0.8mm #fff, inset 0 0 0 1.05mm {ACC}; }}
.foot {{ margin-top: auto; padding-top: 0.8mm; text-align: center; font-size: 5.6pt; letter-spacing: .06em; color: {ACC}; font-family: Lora; font-style: italic; }}
.credit {{ position: absolute; bottom: 1.6mm; left: 0; right: 0; text-align: center; font-size: 5.5pt; color: #999; }}
/* tarjetas de texto y tablas */
.head {{ display: flex; align-items: center; gap: 2.5mm; border-bottom: 0.4mm solid {INK}; padding-bottom: 1.8mm; margin-bottom: 2mm; }}
.hico {{ width: 13mm; height: 13mm; flex: none; }}
.head > div:nth-child(2) {{ flex: 1; }}
.ht {{ font-family: Lora; font-weight: 700; font-size: 14pt; line-height: 1.05; }}
.hs {{ font-size: 7pt; color: {ACC}; font-style: italic; margin-top: .6mm; }}
.d10 {{ font-family: Lora; font-weight: 700; font-size: 10pt; color: #fff; background: {ACC}; border-radius: 1.5mm; padding: 1mm 2mm; }}
.grid {{ list-style: none; display: grid; grid-template-columns: 1fr 1fr; grid-auto-flow: column; grid-template-rows: repeat(5, 1fr); column-gap: 3mm; row-gap: 1.1mm; flex: 1; margin-bottom: 1.5mm; }}
.grid li {{ display: flex; align-items: center; gap: 1.8mm; font-size: 9.4pt; line-height: 1.12; border-bottom: 0.2mm dotted #bbb; }}
.grid .n {{ flex: none; width: 5.6mm; height: 5.6mm; border-radius: 50%; background: {INK}; color: #fff; font-family: Lora; font-weight: 700; font-size: 7.5pt; display: flex; align-items: center; justify-content: center; }}
.secret .head {{ border-bottom-style: dashed; }}
.secret .grid .n {{ background: {ACC}; }}
.prose {{ font-size: 8.7pt; line-height: 1.3; margin-bottom: 2mm; text-align: justify; hyphens: auto; }}
.prose.big {{ font-size: 9.2pt; font-style: italic; text-align: left; }}
.prose.small {{ font-size: 7.7pt; color: #444; }}
.cap {{ float: left; font-family: Lora; font-weight: 700; font-size: 22pt; line-height: .9; margin: .6mm 1.2mm 0 0; color: {ACC}; }}
.chips {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 1.2mm; margin-bottom: 2mm; }}
.chip {{ border: 0.35mm solid {INK}; border-radius: 1.5mm; text-align: center; padding: .6mm .3mm; }}
.chip b {{ display: block; font-family: Lora; font-size: 12pt; line-height: 1.1; }}
.chip span {{ font-size: 5.6pt; display: block; line-height: 1.1; }}
'''
