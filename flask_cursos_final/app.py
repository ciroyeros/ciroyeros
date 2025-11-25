from flask import Flask, render_template, g
import sqlite3
import os

DATABASE = os.path.join(os.path.dirname(__file__), "cursos.db")

app = Flask(__name__, static_folder="static", template_folder="templates")


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT Inscripciones.id_inscripcion, Inscripciones.id_curso, Cursos.nombre AS curso_nombre,
               Inscripciones.nombre_alumno, Inscripciones.email_alumno, Inscripciones.fecha_inscripcion,
               Inscripciones.image_url
        FROM Inscripciones
        INNER JOIN Cursos ON Inscripciones.id_curso = Cursos.id_curso
        ORDER BY Inscripciones.id_inscripcion DESC
    """)
    inscripciones = cursor.fetchall()

    injected_css = """
    .card { border-radius: 12px; padding: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); margin-bottom:12px; }
    .course-img { max-width:150px; height:auto; border-radius:8px; }
    """

    return render_template("index.html", inscripciones=inscripciones, injected_css=injected_css)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
