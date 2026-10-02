from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------
# Contenido tomado de la página del 65 Aniversario de FCA Tijuana.
# Los textos marcados con [EDITAR] son de relleno: cámbialos por
# la información real.
# ---------------------------------------------------------------

# Egresados de "Voces que inspiran". Las fotos van en static/img/egresados/
EGRESADOS = [
    {"id": 1, "nombre": "José Alberto Mejía", "carrera": "Lic. Contaduría Pública", "img": "egresados/jose-alberto.jpg"},
    {"id": 2, "nombre": "María Olivia Ortíz López", "carrera": "Lic. Administración de Empresas", "img": "egresados/maria-olivia.jpg"},
    {"id": 3, "nombre": "Ricardo Osorio Miranda", "carrera": "Lic. Administración de Empresas", "img": "egresados/ricardo.jpg"},
    {"id": 4, "nombre": "María Guadalupe López Martínez", "carrera": "Lic. Informática", "img": "egresados/maria-guadalupe.jpg"},
    {"id": 5, "nombre": "Juan Pablo Ussel Enríquez", "carrera": "Lic. en Negocios Internacionales", "img": "egresados/juan-pablo.jpg"},
    {"id": 6, "nombre": "Juan Carlos Escárrega Rojo", "carrera": "Lic. Contaduría Pública", "img": "egresados/juan-carlos.jpg"},
]
for e in EGRESADOS:
    e.setdefault("testimonio", f"[EDITAR] Aquí va el testimonio de {e['nombre']}: qué le dejó su paso por la FCA y a qué se dedica hoy.")
    e.setdefault("generacion", "[EDITAR] Generación")
    e.setdefault("video", "https://youtu.be/isR7S_0SBHY")

# Cifras de "65 Años de Historia"
CIFRAS = [
    {"valor": 678, "prefijo": "+", "texto": "Egresados cada año"},
    {"valor": 12,  "prefijo": "+", "texto": "Programas educativos ofertados"},
    {"valor": 149, "prefijo": "+", "texto": "Convenios con empresas e instituciones"},
    {"valor": 65,  "prefijo": "",  "texto": "Años formando líderes"},
]

# "Próximos eventos" (en el sitio original se cargan desde el blog)
EVENTOS = [
    {"fecha": "[EDITAR] 15 oct", "titulo": "[EDITAR] Ceremonia conmemorativa", "lugar": "Auditorio FCA", "img": "eventos/evento1.jpg"},
    {"fecha": "[EDITAR] 22 oct", "titulo": "[EDITAR] Encuentro de egresados", "lugar": "Explanada FCA", "img": "eventos/evento2.jpg"},
    {"fecha": "[EDITAR] 5 nov",  "titulo": "[EDITAR] Carrera del 65 Aniversario", "lugar": "Campus Tijuana", "img": "eventos/evento3.jpg"},
]

FOOTER_LINKS = {
    "Institucional": [
        ("Plan de Desarrollo 2023-2027", "https://fca.tij.uabc.mx/plandedesarrollo"),
        ("Programa para la Cultura de Paz", "https://www.uabc.mx/wp-content/uploads/bsk-pdf-manager/2023/10/Programa-Institucional-para-la-Cultura-de-Paz-UABC_.pdf"),
    ],
    "Docentes": [("Consultar avisos", "https://fca.tij.uabc.mx/docentes-infogral")],
    "Estudiantes": [
        ("Ticket de ayuda", "https://fca.tij.uabc.mx/ticketayuda"),
        ("Calendario escolar", "https://drive.google.com/file/d/1KZwB3fAkZ_88xWOL-iM0gBYVRuFws4oo/view"),
    ],
    "FCA": [
        ("Inicio", "https://fca.tij.uabc.mx/"),
        ("Nuestra Facultad", "https://fca.tij.uabc.mx/acerca-de"),
    ],
}

REDES = [
    ("Facebook", "https://fca.tij.uabc.mx/website/social/facebook"),
    ("Instagram", "https://fca.tij.uabc.mx/website/social/instagram"),
    ("TikTok", "https://fca.tij.uabc.mx/website/social/tiktok"),
    ("YouTube", "https://fca.tij.uabc.mx/website/social/youtube"),
    ("LinkedIn", "https://fca.tij.uabc.mx/website/social/linkedin"),
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        egresados=EGRESADOS,
        destacado=EGRESADOS[2],   # egresado que aparece al centro por defecto
        cifras=CIFRAS,
        eventos=EVENTOS,
        footer_links=FOOTER_LINKS,
        redes=REDES,
    )


if __name__ == "__main__":
    app.run(debug=True)