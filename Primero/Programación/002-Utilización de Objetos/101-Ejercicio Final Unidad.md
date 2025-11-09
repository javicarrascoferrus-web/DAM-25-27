Ahora que he terminado la unidad, he aprendido a trabajar con Python y a manejar estructuras básicas como listas, funciones y objetos. En esta nueva parte, damos un paso más y conectamos Python con una base de datos MySQL, lo que nos permite trabajar con información almacenada de forma más organizada y persistente.

Para realizar este ejercicio, primero hay que tener instalada la librería mysql.connector, que permite que Python se comunique con MySQL.
A continuación, se crea un objeto de conexión, y a partir de él, un cursor para ejecutar consultas SQL.
Después, se realiza un SELECT sobre una tabla existente y se muestran los resultados en la consola.


**A continuación voy a escribir el código que conectará la base de datos con el código Python:**



import mysql.connector  (Con este comando importamos la librería MySQL)


#### 1. Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)



#### 2. Crear un cursor para ejecutar consultas
cursor = conexion.cursor()


 
#### 3. Realizar una consulta SELECT sobre la tabla 'libros'
cursor.execute("SELECT titulo, autor, paginas FROM libros")



#### 4. Obtener los resultados
resultados = cursor.fetchall()



#### 5. Mostrar los datos por pantalla
print("Listado de libros en la base de datos:\n")
for libro in resultados:
    print(f"Título: {libro[0]}, Autor: {libro[1]}, Páginas: {libro[2]}")



#### 6. Cerrar la conexión
cursor.close()
conexion.close()



Si la base de datos contiene registros, al ejecutar el programa se mostrará algo como esto:

Listado de libros en la base de datos:

Título: 1984, Autor: George Orwell, Páginas: 328
Título: El Quijote, Autor: Miguel de Cervantes, Páginas: 863
Título: Cien años de soledad, Autor: Gabriel García Márquez, Páginas: 471



Con este ejercicio he aprendido a conectar un programa de Python con una base de datos MySQL usando la librería mysql.connector.
También he visto cómo ejecutar una consulta SQL desde Python y cómo mostrar los resultados en pantalla de forma ordenada.
