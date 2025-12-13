En Python, el manejo de archivos es fundamental para guardar y recuperar información. Los archivos pueden abrirse en distintos modos, según la operación que se quiera realizar: lectura, escritura, o añadir.

A continuación voy a escribir una serie de comandos para dar ejemplo:

**Código**:


**Se abre el archivo "clientes.txt" en modo lectura binaria**

archivo = open("clientes.txt", "rb")

**Se lee la primera línea del archivo**
linea = archivo.readline()

**Se imprime la línea decodificada en formato UTF-8**
print("Primera línea (modo binario):", linea.decode("utf-8"))

**Cerramos el archivo**
archivo.close()



Leer todas las líneas de un archivo:
**Se abre nuevamente el archivo, ahora en modo texto normal**
archivo = open("clientes.txt", "r")

**Se leen todas las líneas y se guardan en una lista**
lineas = archivo.readlines()

**Se imprime la lista completa de líneas**
print("Todas las líneas:", lineas)

**Cerramos el archivo**
archivo.close()



Escribir información en un archivo binario:
**Se abre el archivo en modo escritura binaria**
archivo = open("clientes.txt", "wb")

**Se escribe una cadena, pero primero hay que codificarla a bytes**
archivo.write("Información de cliente".encode("utf-8"))

**Cerramos el archivo**
archivo.close()



Agregar una nueva línea a un archivo existente:

**Se abre el archivo en modo "a" (append o añadir)**
archivo = open("clientes.txt", "a")

**Se escribe una nueva línea con salto de línea al final**:
archivo.write("Información de cliente\n")


**Cerramos el archivo**
archivo.close()
