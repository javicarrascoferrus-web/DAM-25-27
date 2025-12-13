En Python, el manejo de directorios y archivos se realiza principalmente con el módulo os, que permite interactuar con el sistema operativo.
En este ejercicio aprenderemos a crear un directorio nuevo con os.mkdir() y luego eliminarlo con os.rmdir(). Estas funciones son útiles cuando un programa necesita generar carpetas para guardar información temporal o separar datos de diferentes procesos.

**os.mkdir(nombre_directorio)** < Crea un nuevo directorio en la ubicación actual.
Si el directorio ya existe, se produce un error (FileExistsError).

**os.rmdir(nombre_directorio)** < Elimina el directorio especificado, pero solo si está vacío.




**Código**:

import os (añadir el archivo creado)




**Cear un Directorio**

carpeta = "mi_nueva_carpeta"


**Verificamos si la carpeta no existe antes de crearla** 
if not os.path.exists(carpeta):
    os.mkdir(carpeta)
    print(f"Carpeta '{carpeta}' creada correctamente.")
else:
    print(f"La carpeta '{carpeta}' ya existe.")



### Eliminar un Directorio

**Verificamos si la carpeta existe antes de eliminarla**

if os.path.exists(carpeta):
    os.rmdir(carpeta)
    print(f"Carpeta '{carpeta}' eliminada correctamente.")
else:
    print(f"La carpeta '{carpeta}' no existe.")
		
		

En resumen, con el módulo "os" podemos crear y eliminar directorios fácilmente usando mkdir() y rmdir().
