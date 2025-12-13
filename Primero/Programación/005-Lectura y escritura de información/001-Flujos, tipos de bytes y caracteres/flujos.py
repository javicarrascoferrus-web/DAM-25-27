En Python, el manejo de archivos es una parte muy importante cuando queremos guardar información o leer datos de forma permanente. Los archivos pueden ser de texto o binarios, y se usan para almacenar datos que luego pueden recuperarse en otros momentos.
Para trabajar con archivos en Python se usan las funciones integradas open(), write(), read() y close().

El módulo pickle tiene dos funciones principales:

pickle.dump(obj, archivo) para guardar un objeto en formato binario.

pickle.load(archivo) para cargar un objeto previamente guardado.

A continuación escribiré una serie de comandos sencillo para dar ejemplo:

**Código**:

**Escribir en un archivo**

archivo = open("nuevo_archivo.txt", "w")
archivo.write("Esto es una nueva línea de texto")
archivo.close()


**Leer desde un archivo**

archivo = open("nuevo_archivo.txt", "r")
linea = archivo.readline()
print("Contenido del archivo:", linea)
archivo.close()


**Uso del módulo pickle**
import pickle


lenguajes = ["Python", "Java", "C++"]


**Guardar archivo**
archivo_binario = open("objetos.pickle", "wb")
pickle.dump(lenguajes, archivo_binario)
archivo_binario.close()

En resumen, el manejo de archivos en Python permite guardar y recuperar información de manera sencilla. Los archivos de texto son útiles para datos simples, mientras que los binarios con pickle permiten almacenar estructuras de datos más complejas.
