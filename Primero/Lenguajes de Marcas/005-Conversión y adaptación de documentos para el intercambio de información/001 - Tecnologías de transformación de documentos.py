La idea general de ejercicio es:
Conectarnos a una base de datos local llamada blog2526, donde tenemos nuestras notas/entradas.
Recuperar los datos en forma de diccionario para trabajar más cómodo en Python.
Usar Flask y templates para enseñar esas notas en una página web (index.html).



#### 001-me conecto a la base de datos.py
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",            # tu usuario de MySQL
    password="tu_password", # tu contraseña
    database="blog2526"     # nombre de la base de datos
)

if conexion.is_connected():
    print("Conectado correctamente a la base de datos blog2526")
else:
    print("No se ha podido conectar a la base de datos")
		

#### Añadir un poco de Flask – 004-le pongo un poco de flask.py

Aquí es donde empezamos a servir algo por navegador.
Este archivo puede ser una versión sencilla: solo define la ruta principal / y renderiza una plantilla.


from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def obtener_notas():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_password",
        database="blog2526"
    )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT id, titulo, contenido, fecha FROM notas ORDER BY fecha DESC")
    notas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return notas

@app.route("/")
def index():
    notas = obtener_notas()
    return render_template("index.html", notas=notas)

if __name__ == "__main__":
    app.run(debug=True)



Trabajo con templates – 005-trabajo con templates.py + templates/index.html

Aquí ya “formalizamos” el tema de los templates.
El archivo Python será parecido al anterior, pero lo dejo un poco más organizado:

from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_password",
        database="blog2526"
    )



Primero pruebas 001-me conecto a la base de datos.py para asegurarte de que te conectas bien a blog2526.
Luego ejecutas 002-quiero un diccionario.py para ver por consola que las notas salen bien en forma de diccionario.
Después lanzas el servidor Flask con python 005-trabajo con templates.py.

Con este ejercicio he hecho el recorrido completo que se suele hacer en aplicaciones web:
Capa de datos: conexión a MySQL (blog2526) y consultas con mysql.connector.
Capa lógica: convertir los resultados a diccionarios y preparar funciones en Python que obtienen las notas.
Capa de presentación: usar Flask + templates para mostrar esos datos de forma amigable en HTML.
