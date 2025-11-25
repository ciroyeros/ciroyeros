Proyecto Flask listo para ejecutar.

Estructura:
- app.py
- cursos.db
- templates/
  - base.html
  - index.html
- static/
  - css/styles.css
  - img/curso1.png
  - img/default-course.png

Cómo ejecutar (Windows):
1. Asegúrate de tener Python 3 instalado.
2. (Opcional) crea y activa un virtualenv:
   python -m venv venv
   venv\Scripts\activate
3. Instala Flask:
   pip install Flask pillow
4. Ejecuta:
   python app.py
5. Abrí en el navegador: http://127.0.0.1:5000/

Nota: la base de datos ya está incluida con datos de ejemplo y las imágenes están en static/img/.
