"""Datos del juego: especies, rasgos y tablas d10."""

ESPECIES = [  # (d10, nombre, icono, In, Fi, As, Ra)
    (1, "Zorro", "zorro", 2, 2, 1, 1),
    (2, "Gato", "gato", 0, 2, 3, 2),
    (3, "Sapo", "sapo", 1, 0, 2, 1),
    (4, "Araña", "arana", 2, 0, 3, 1),
    (5, "Búho", "buho", 3, 1, 1, 2),
    (6, "Liebre", "liebre", 0, 0, 2, 3),
    (7, "Urraca", "urraca", 2, 1, 1, 2),
    (8, "Cuervo", "cuervo", 2, 1, 2, 1),
    (9, "Perro", "perro", 1, 3, 0, 1),
    (10, "Rata", "rata", 1, 0, 2, 2),
]
RASGOS = [
    ("INT", "Inteligencia", "hablar con humanos, entenderlos"),
    ("FIE", "Fiereza", "asustar, arrastrar, empujar, morder"),
    ("AST", "Astucia", "escabullirse, robar, esconderse"),
    ("RAP", "Rapidez", "superar, escalar, evadir"),
]
PUEBLO = ["Bajo el yugo de un barón", "Lleno de alegres gnomos", "Controlado por un siniestro culto",
          "Devotamente religioso", "Increíblemente supersticioso", "En guerra con las tribus del bosque",
          "Construido alrededor de una academia de magos", "Lleno de mineros", "Sombrío y peligroso",
          "Ofensivamente perfecto"]
CAZADOR = ["Fuerte y armado", "Viejo y sabio", "Borracho y violento", "Piadoso y agresivo",
           "Oculto y cobarde", "Mágico y celoso", "Inteligente y cruel", "Clonado y oculto",
           "Alegre y bienintencionado", "Testarudo y salvaje"]
GIRO = ["El pueblo está involucrado", "Una bruja rival le tendió una trampa", "El cazador no lo hizo",
        "El cazador te está esperando", "El pueblo celebra un festival", "El cazador murió y lo están enterrando",
        "Hay dos cazadores (rivales) en la ciudad", "El pueblo está abandonado",
        "El cazador atrapó a un sospechoso y lo está interrogando", "El pueblo lo odia"]
HECHIZO = ["Mano invisible", "Conjurar luz", "Hablar humano", "Bloquear / desbloquear, abrir / cerrar",
           "Conjurar comida", "Crear fuego", "Ordenar, limpiar y reparar", "Hacer crecer una planta",
           "Distraer / confundir", "Hacer que un libro se lea en voz alta solo"]
