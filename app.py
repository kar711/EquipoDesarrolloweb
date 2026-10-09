from flask import Flask, render_template

app = Flask(__name__)

# ---------- DATOS DE LA PÁGINA (todo el contenido vive aquí) ----------
SITE = {
    "name": "Facultad de Contaduría y Administración",
    "menu": [
        {"label": "Home", "url": "/"},
        {"label": "FCA", "url": "#", "dropdown": True},
        {"label": "🎉 65th Anniversary", "url": "#"},
        {"label": "Educational Offer", "url": "#", "dropdown": True},
        {"label": "Students", "url": "#"},
    ],
}

BANNER = {
    "title": "Conquer your dreams",
    "text": "Develop yourself in the professional world with the tools "
            "of the present and future, be competitive and innovative.",
    "actions": [
        {"group": "Students", "label": "Send Ticket", "url": "#"},
        {"group": "Teachers", "label": "Check notices", "url": "#"},
    ],
}

PROGRAMS = [
    {"name": "Degree", "icon": "👥"},
    {"name": "Postgraduate", "icon": "📖"},
    {"name": "Graduate Studies", "icon": "🖥️"},
]

EVENTS = [
    {
        "poster": "lectura", "title": "A pause to read, share, and discover new ideas",
        "text": "The FCA invites you to the Reading Circle, a space to connect through words and enjoy reading in community.",
        "detail": "<strong>Day and time:</strong> Every Friday, 1:00 to 2:00 p.m.",
        "link": None, "link_label": None,
    },
    {
        "poster": "meritus", "title": "Graduates from UABC who have made their mark in their professional field. It is time to recognize them.",
        "text": "Meritus Call 2026, with which the trajectory of graduates is recognized. Applications are by third parties; self-applications are not accepted.",
        "detail": None, "link": "#", "link_label": "Apply",
    },
    {
        "poster": "inmobiliario", "title": "Boost your professional development in the real estate sector!",
        "text": "The FCA UABC invites you to the 3rd Real Estate Diploma, with a hybrid format and certification valid for the licensing process.",
        "detail": None, "link": "#", "link_label": "Download the call",
    },
    {
        "poster": "paz", "title": "Daily Steps for Peace – October 2026",
        "text": "The Gender, Diversity, and Education Unit (UGDIE) invites the community to consult the October edition of <strong>“Daily Steps for Peace”</strong>, an initiative of the UABC. Participate!",
        "detail": None, "link": "#", "link_label": "Download calendar",
    },
]

NEWS = [
    {"title": "Fortaleciendo la FCA", "date": "Oct 1, 2026", "color": "#cfa35a"},
    {"title": "Practicando y argumentando", "date": "Oct 1, 2026", "color": "#8a8a8a"},
    {"title": "Una noche para celebrar 65 años …", "date": "Sep 30, 2026", "color": "#2b2b2b"},
    {"title": "Una pausa para leer, compartir y …", "date": "Sep 30, 2026", "color": "#00703c"},
    {"title": "65 años de historia que seguimos…", "date": "Sep 24, 2026", "color": "#2e7fd6"},
    {"title": "El talento también es parte de nu…", "date": "Sep 24, 2026", "color": "#111111"},
    {"title": "¡Celebramos 65 años corriendo i…", "date": "Sep 24, 2026", "color": "#d9392b"},
    {"title": "Viendo realidades a los 20…", "date": "Sep 23, 2026", "color": "#0b1d3a"},
]

ACCREDITATIONS = ["ACBSP", "CONAHCYT", "CACECA"]

FOOTER = {
    "columns": [
        {"title": "FCA", "links": ["Start", "Our Faculty"]},
        {"title": "Students", "links": ["Help ticket", "School calendar"]},
        {"title": "Teachers", "links": ["Check notifications"]},
        {"title": "Institutional", "links": ["Development plan 2023-2027", "Program for a culture of peace"]},
    ],
    "social": ["f", "ig", "tt", "yt", "in"],
    "school": "School of Accounting and Administration",
    "campus": "UABC - Tijuana Campus",
    "address": "Calzada Universidad 14418, Mesa de Otay, Tijuana, B.C., Mexico, C.P. 22427",
    "university_line": "+52 (664) 979-7500",
    "faculty_line": "+52 (664) 683-3174",
}


@app.route("/")
def index():
    return render_template(
        "index.html", site=SITE, banner=BANNER, programs=PROGRAMS,
        events=EVENTS, news=NEWS, accreditations=ACCREDITATIONS, footer=FOOTER,
    )


if __name__ == "__main__":
    # host 0.0.0.0 para que Codespaces pueda reenviar el puerto
    app.run(host="0.0.0.0", port=5000, debug=True)
