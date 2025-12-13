El manejo de archivos en Python permite guardar, leer y modificar información de manera permanente. Esto es muy útil en programas que necesitan conservar datos entre ejecuciones, como registros o configuraciones.
En este ejercicio vamos a crear, leer, escribir, añadir y eliminar archivos de texto, utilizando las funciones integradas de Python como open, write, read y os.remove.

Para ello, voy a realizar un ejemplo práctico de cada una de las funciones:

**Código**:

import os (Para añadir el archivo creado)


### Crear un archivo
**Se crea un nuevo archivo llamado "informacion.txt" y se escribe una línea**

archivo = open("informacion.txt", "w")
archivo.write("Hola, soy un estudiante de FP.\n")
archivo.close()
print("Archivo 'informacion.txt' creado correctamente.")

**Leer el contenido del archivo**
def leer_archivo():
    with open("informacion.txt", "r") as f:
        contenido = f.read()
        print("Contenido de informacion.txt:")
        print(contenido)



### Se llama a la función para comprobar que el archivo se ha creado y leído bien

leer_archivo()


**Escribir en un nuevo archivo**
nuevo = open("nuevo_archivo.txt", "w")
nuevo.write("Estoy interesado en aprender sobre Programación.\n")
nuevo.close()
print("Archivo 'nuevo_archivo.txt' creado y escrito correctamente.")




#### Añadir contenido a un archivo existente
**Se abre informacion.txt en modo append para añadir una nueva línea**
archivo = open("informacion.txt", "a")
archivo.write("Esta actividad me está ayudando mucho.\n")
archivo.close()
print("Línea añadida al archivo 'informacion.txt'.")



**Comprobamos nuevamente su contenido**
leer_archivo()


#### Eliminar un archivo
**Se elimina el archivo nuevo_archivo.txt**
if os.path.exists("nuevo_archivo.txt"):
    os.remove("nuevo_archivo.txt")
    print("Archivo 'nuevo_archivo.txt' eliminado correctamente.")
else:
    print("El archivo 'nuevo_archivo.txt' no existe.")
	
	
	
Para finalizar, este ejercicio demuestra cómo crear, leer, modificar y eliminar archivos usando Python.
Con estas operaciones básicas se puede empezar a trabajar con datos persistentes.
