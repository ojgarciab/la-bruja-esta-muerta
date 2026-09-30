"""Datos del juego: especies, rasgos y tablas d10."""

ESPECIES = [  # (d10, nombre, icono, In, Fu, As, Ra)
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
    ("FUE", "Fuerza", "asustar, arrastrar, empujar, cargar"),
    ("AST", "Astucia", "escabullirse, esconderse, despistar"),
    ("RAP", "Rapidez", "superar, escalar, evadir"),
]
PUEBLO = ["Gobernado por un barón gruñón", "Lleno de alegres gnomos", "Controlado por un club secreto",
          "Obsesionado con las normas", "Increíblemente supersticioso", "Enfadado con los animales del bosque",
          "Construido alrededor de una academia de magos", "Lleno de mineros", "Oscuro y lleno de niebla",
          "Tan perfecto que resulta sospechoso"]
LADRON = ["Grandullón y forzudo", "Viejo y sabio", "Torpe y gruñón", "Educado y tramposo",
          "Escondido y miedica", "Mágico y celoso", "Listísimo y presumido", "Disfrazado y escurridizo",
          "Alegre y bienintencionado", "Testarudo y alborotador"]
GIRO = ["El pueblo está involucrado", "Una bruja rival le tendió una trampa", "El ladrón no lo hizo",
        "El ladrón te está esperando", "El pueblo celebra un festival", "Al ladrón se le ha perdido el medallón",
        "Hay dos ladrones (rivales) en el pueblo", "El pueblo está abandonado",
        "El alguacil acusa del robo a un inocente", "Todo el pueblo lo adora"]
HECHIZO = ["Mano invisible", "Conjurar luz", "Hablar humano", "Bloquear / desbloquear, abrir / cerrar",
           "Conjurar comida", "Hacer burbujas de colores", "Ordenar, limpiar y reparar", "Hacer crecer una planta",
           "Distraer / confundir", "Hacer que un libro se lea en voz alta solo"]
