"""Ilustraciones SVG propias (viewBox 0 0 100 100)."""
from .estilo import INK, W

ICONS = {
"zorro": f'''
<path d="M14 14 L38 36 L62 36 L86 14 L82 50 Q78 64 60 74 L50 90 L40 74 Q22 64 18 50 Z" fill="{INK}"/>
<path d="M20 22 L34 36 L26 40 Z M80 22 L66 36 L74 40 Z" fill="{W}" opacity=".85"/>
<path d="M20 50 Q34 56 44 72 L50 90 L40 74 Q26 66 20 50 Z M80 50 Q66 56 56 72 L50 90 L60 74 Q74 66 80 50 Z" fill="{W}"/>
<path d="M32 50 Q38 45 44 50 Q38 52 32 50 Z M56 50 Q62 45 68 50 Q62 52 56 50 Z" fill="{W}"/>
<ellipse cx="50" cy="86" rx="5" ry="4" fill="{INK}"/>''',
"gato": f'''
<path d="M22 44 L18 10 L42 28 Q50 26 58 28 L82 10 L78 44 Q84 74 50 84 Q16 74 22 44 Z" fill="{INK}"/>
<path d="M24 20 L36 30 L26 36 Z M76 20 L64 30 L74 36 Z" fill="{W}" opacity=".8"/>
<ellipse cx="37" cy="50" rx="8" ry="6" fill="{W}"/><ellipse cx="63" cy="50" rx="8" ry="6" fill="{W}"/>
<ellipse cx="37" cy="50" rx="2" ry="5.5" fill="{INK}"/><ellipse cx="63" cy="50" rx="2" ry="5.5" fill="{INK}"/>
<path d="M46 62 L54 62 L50 67 Z" fill="{W}"/>
<path d="M50 67 Q46 72 42 70 M50 67 Q54 72 58 70" stroke="{W}" stroke-width="1.8" fill="none"/>
<path d="M30 64 L4 60 M30 68 L6 72 M70 64 L96 60 M70 68 L94 72" stroke="{INK}" stroke-width="1.6"/>''',
"sapo": f'''
<ellipse cx="50" cy="64" rx="40" ry="24" fill="{INK}"/>
<circle cx="30" cy="42" r="13" fill="{INK}"/><circle cx="70" cy="42" r="13" fill="{INK}"/>
<circle cx="30" cy="41" r="8" fill="{W}"/><circle cx="70" cy="41" r="8" fill="{W}"/>
<ellipse cx="30" cy="42" rx="5" ry="3" fill="{INK}"/><ellipse cx="70" cy="42" rx="5" ry="3" fill="{INK}"/>
<path d="M24 64 Q50 76 76 64" stroke="{W}" stroke-width="2.2" fill="none"/>
<circle cx="40" cy="78" r="2" fill="{W}" opacity=".7"/><circle cx="60" cy="80" r="2.5" fill="{W}" opacity=".7"/><circle cx="50" cy="84" r="1.6" fill="{W}" opacity=".7"/>
<ellipse cx="22" cy="88" rx="12" ry="5" fill="{INK}"/><ellipse cx="78" cy="88" rx="12" ry="5" fill="{INK}"/>''',
"arana": f'''
<line x1="50" y1="0" x2="50" y2="26" stroke="{INK}" stroke-width="1.2"/>
<g stroke="{INK}" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round">
<polyline points="44,38 26,24 14,34"/><polyline points="44,42 22,38 8,52"/><polyline points="44,48 24,56 14,74"/><polyline points="45,54 30,70 26,90"/>
<polyline points="56,38 74,24 86,34"/><polyline points="56,42 78,38 92,52"/><polyline points="56,48 76,56 86,74"/><polyline points="55,54 70,70 74,90"/>
</g>
<circle cx="50" cy="36" r="10" fill="{INK}"/><ellipse cx="50" cy="64" rx="17" ry="20" fill="{INK}"/>
<circle cx="46" cy="34" r="2.2" fill="{W}"/><circle cx="54" cy="34" r="2.2" fill="{W}"/>
<path d="M50 54 L56 62 L50 70 L44 62 Z" fill="{W}" opacity=".8"/>''',
"buho": f'''
<path d="M22 30 L26 8 L42 22 Q50 20 58 22 L74 8 L78 30 Q90 62 72 84 Q50 96 28 84 Q10 62 22 30 Z" fill="{INK}"/>
<circle cx="38" cy="40" r="12" fill="{W}"/><circle cx="62" cy="40" r="12" fill="{W}"/>
<circle cx="38" cy="41" r="5.5" fill="{INK}"/><circle cx="62" cy="41" r="5.5" fill="{INK}"/>
<circle cx="36.5" cy="39" r="1.6" fill="{W}"/><circle cx="60.5" cy="39" r="1.6" fill="{W}"/>
<path d="M45 52 L55 52 L50 62 Z" fill="{W}"/>
<g stroke="{W}" stroke-width="1.8" fill="none" opacity=".8">
<path d="M36 68 l4 4 l4 -4 M48 68 l4 4 l4 -4 M60 68 l4 4 l4 -4 M42 78 l4 4 l4 -4 M54 78 l4 4 l4 -4"/></g>''',
"liebre": f'''
<ellipse cx="38" cy="26" rx="7" ry="24" transform="rotate(-12 38 26)" fill="{INK}"/>
<ellipse cx="62" cy="26" rx="7" ry="24" transform="rotate(12 62 26)" fill="{INK}"/>
<ellipse cx="38" cy="26" rx="3" ry="17" transform="rotate(-12 38 26)" fill="{W}" opacity=".8"/>
<ellipse cx="62" cy="26" rx="3" ry="17" transform="rotate(12 62 26)" fill="{W}" opacity=".8"/>
<ellipse cx="50" cy="66" rx="24" ry="22" fill="{INK}"/>
<circle cx="40" cy="60" r="4" fill="{W}"/><circle cx="60" cy="60" r="4" fill="{W}"/>
<circle cx="40.5" cy="60.5" r="2" fill="{INK}"/><circle cx="60.5" cy="60.5" r="2" fill="{INK}"/>
<ellipse cx="50" cy="76" rx="9" ry="7" fill="{W}"/>
<path d="M46 72 L54 72 L50 76 Z" fill="{INK}"/><path d="M50 76 L50 80 M50 80 Q47 83 44 81 M50 80 Q53 83 56 81" stroke="{INK}" stroke-width="1.4" fill="none"/>''',
"urraca": f'''
<path d="M58 54 L96 80 L92 86 L52 66 Z" fill="{INK}"/>
<ellipse cx="46" cy="56" rx="22" ry="15" transform="rotate(-18 46 56)" fill="{INK}"/>
<circle cx="26" cy="36" r="11" fill="{INK}"/>
<path d="M16 34 L4 38 L16 40 Z" fill="{INK}"/>
<circle cx="24" cy="34" r="2.2" fill="{W}"/>
<path d="M30 58 Q42 72 58 64 Q46 64 36 52 Z" fill="{W}"/>
<path d="M44 46 Q56 44 62 52 Q54 52 46 50 Z" fill="{W}"/>
<path d="M40 70 L36 88 M48 70 L48 88 M32 88 L40 88 M44 88 L52 88" stroke="{INK}" stroke-width="2.2"/>''',
"cuervo": f'''
<path d="M62 54 L92 64 L94 72 L88 76 L58 66 Z" fill="{INK}"/>
<ellipse cx="48" cy="54" rx="24" ry="17" transform="rotate(-12 48 54)" fill="{INK}"/>
<circle cx="26" cy="34" r="13" fill="{INK}"/>
<path d="M16 28 L0 36 L16 42 Z" fill="{INK}"/>
<circle cx="24" cy="31" r="2.6" fill="{W}"/>
<path d="M44 46 Q60 44 70 58" stroke="{W}" stroke-width="1.6" fill="none" opacity=".7"/>
<path d="M48 52 Q60 52 66 62" stroke="{W}" stroke-width="1.6" fill="none" opacity=".7"/>
<path d="M42 70 L38 90 M52 70 L52 90 M32 90 L42 90 M46 90 L56 90" stroke="{INK}" stroke-width="2.4"/>''',
"perro": f'''
<ellipse cx="50" cy="48" rx="24" ry="26" fill="{INK}"/>
<ellipse cx="22" cy="50" rx="10" ry="22" transform="rotate(18 22 50)" fill="{INK}"/>
<ellipse cx="78" cy="50" rx="10" ry="22" transform="rotate(-18 78 50)" fill="{INK}"/>
<ellipse cx="50" cy="68" rx="16" ry="13" fill="{W}"/>
<ellipse cx="50" cy="62" rx="7" ry="5" fill="{INK}"/>
<path d="M50 67 L50 73 M50 73 Q44 78 40 74 M50 73 Q56 78 60 74" stroke="{INK}" stroke-width="1.6" fill="none"/>
<circle cx="39" cy="44" r="4.5" fill="{W}"/><circle cx="61" cy="44" r="4.5" fill="{W}"/>
<circle cx="39.5" cy="44.5" r="2.4" fill="{INK}"/><circle cx="61.5" cy="44.5" r="2.4" fill="{INK}"/>
<path d="M50 80 L50 92" stroke="{INK}" stroke-width="0"/>
<path d="M34 34 Q40 30 44 34 M56 34 Q60 30 66 34" stroke="{W}" stroke-width="1.6" fill="none"/>''',
"rata": f'''
<path d="M78 66 Q96 70 92 86 Q88 96 70 92 Q54 88 40 94" stroke="{INK}" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<path d="M8 56 Q20 40 44 38 Q70 36 80 56 Q84 70 70 74 L30 74 Q18 70 8 56 Z" fill="{INK}"/>
<circle cx="34" cy="36" r="10" fill="{INK}"/><circle cx="34" cy="36" r="5.5" fill="{W}" opacity=".8"/>
<circle cx="20" cy="50" r="2.4" fill="{W}"/>
<circle cx="7" cy="56" r="2.4" fill="{INK}"/>
<path d="M12 58 L0 54 M12 60 L0 62" stroke="{INK}" stroke-width="1.2"/>
<path d="M30 74 L28 82 M62 74 L64 82" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>''',
# --- iconos de historia ---
"pueblo": f'''
<path d="M10 90 L10 52 L28 36 L46 52 L46 90 Z" fill="{INK}"/>
<path d="M40 90 L40 44 L64 20 L88 44 L88 90 Z" fill="{INK}"/>
<rect x="70" y="18" width="8" height="16" fill="{INK}"/>
<rect x="56" y="66" width="14" height="24" fill="{W}"/><rect x="50" y="48" width="9" height="9" fill="{W}"/><rect x="70" y="48" width="9" height="9" fill="{W}"/>
<rect x="21" y="60" width="10" height="10" fill="{W}"/>''',
"ladron": f'''
<path d="M28 58 L34 14 L66 14 L72 58 Z" fill="{INK}"/>
<ellipse cx="50" cy="62" rx="44" ry="10" fill="{INK}"/>
<rect x="30" y="44" width="40" height="8" fill="{W}"/>
<rect x="43" y="42" width="14" height="12" fill="{INK}" stroke="{W}" stroke-width="2.4"/>
<path d="M18 82 L82 82 M50 74 L50 90" stroke="{INK}" stroke-width="3"/>
<path d="M18 82 Q50 70 82 82" stroke="{INK}" stroke-width="2" fill="none"/>''',
"giro": f'''
<path d="M6 50 Q50 6 94 50 Q50 94 6 50 Z" fill="{INK}"/>
<circle cx="50" cy="50" r="18" fill="{W}"/><circle cx="50" cy="50" r="9" fill="{INK}"/>
<circle cx="46" cy="46" r="3" fill="{W}"/>
<path d="M50 6 L50 16 M24 14 L30 22 M76 14 L70 22" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>''',
"hechizo": f'''
<path d="M50 6 L58 38 L90 44 L62 58 L70 92 L50 70 L30 92 L38 58 L10 44 L42 38 Z" fill="{INK}"/>
<circle cx="50" cy="50" r="8" fill="{W}"/>
<path d="M84 12 l3 7 l7 3 l-7 3 l-3 7 l-3 -7 l-7 -3 l7 -3 z M16 70 l2 5 l5 2 l-5 2 l-2 5 l-2 -5 l-5 -2 l5 -2 z" fill="{INK}"/>''',
"caldero": f'''
<path d="M14 42 L86 42 Q92 80 64 86 L36 86 Q8 80 14 42 Z" fill="{INK}"/>
<rect x="8" y="36" width="84" height="8" rx="4" fill="{INK}"/>
<path d="M26 86 L20 96 M74 86 L80 96" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<circle cx="40" cy="26" r="6" fill="none" stroke="{INK}" stroke-width="2.4"/><circle cx="58" cy="16" r="4" fill="none" stroke="{INK}" stroke-width="2.2"/><circle cx="62" cy="30" r="3" fill="none" stroke="{INK}" stroke-width="2"/>
<path d="M30 58 Q40 52 50 58 Q60 64 70 58" stroke="{W}" stroke-width="2.4" fill="none"/>''',
"dado": f'''
<path d="M50 6 L90 30 L90 72 L50 96 L10 72 L10 30 Z" fill="{INK}"/>
<path d="M50 6 L50 40 M10 30 L50 40 L90 30 M50 40 L28 84 M50 40 L72 84 M28 84 L72 84 M10 72 L28 84 M90 72 L72 84 M50 96 L28 84 M50 96 L72 84" stroke="{W}" stroke-width="1.8" fill="none"/>
<text x="50" y="72" text-anchor="middle" font-size="18" font-family="Lora" font-weight="700" fill="{W}">10</text>''',
}

def icon(name, cls="ico"):
    vb = "0 8 100 100" if name in ("urraca", "cuervo", "rata") else "0 0 100 100"
    return f'<svg class="{cls}" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg">{ICONS[name]}</svg>'
