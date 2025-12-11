En este ejercicio voy a realizar una serie de onjetivos, los cuales serán:
Conectarte a una base de datos MySQL desde Python.
Pasar los datos de todas las tablas a un diccionario y luego a JSON.
Montar una mini API en Flask con un endpoint /api que devuelva ese JSON.
Y finalmente, una página en / que consuma esa API y muestre los datos en el navegador.

En principio: 

Script convertir_a_json.py
Este script se encarga de:
Conectarse a MySQL.
Hacer SHOW TABLES;.
Para cada tabla, hacer SELECT * FROM tabla;.
Montar un diccionario
Convertir todo eso a JSON y guardarlo en un archivo.

**Código**:

import mysql.connector
import json
from datetime import date, datetime, time

def obtener_datos_bd():
    conexion = mysql.connector.connect(**DB_CONFIG)
    cursor = conexion.cursor()
		
		
		
#### Script creo_dos_endpoints.py con Flask
from flask import Flask, jsonify, Response
import mysql.connector
from datetime import date, datetime, time

app = Flask(__name__)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "123456789",
    "database": "blog2526",
}

def obtener_datos_bd():
    conexion = mysql.connector.connect(DB_CONFIG)
    cursor = conexion.cursor()
    cursor.execute("SHOW TABLES;")
    tablas = [fila[0] for fila in cursor.fetchall()]


Una vez escrito todo le código, lo probaremos paso a paso:

Primero prueba la conexión y el JSON “offline”

Ejecuta:
python convertir_a_json.py

Si todo va bien, deberías ver el mensaje de conexión OK y el archivo datos_bd.json en la carpeta.

Puedes abrirlo con cualquier editor para ver cómo se ha formateado:

{
    "notas": [
        {
            "id": 1,
            "titulo": "Primera nota",
            "contenido": "Texto de prueba",
            "fecha": "2025-05-01T12:34:56"
        }
    ],
    "otra_tabla": [
        ...
    ]
}

Arranca el servidor Flask

Ejecuta:
python creo_dos_endpoints.py


Flask te dirá algo tipo:
Running on http://127.0.0.1:5000/ 

Prueba el endpoint /api

En el navegador, entra en:
http://127.0.0.1:5000/api

Verás el JSON con todas las tablas y sus registros.
		
		
		
Con este ejercicio he unido varias piezas importante:

Acceso a MySQL desde Python para leer estructura (SHOW TABLES) y datos (SELECT ).
Transformar todo eso a un diccionario y luego a JSON, que es el formato estándar para APIs.
Crear una pequeña API REST con Flask y una página HTML que consume esa API con JavaScript.
