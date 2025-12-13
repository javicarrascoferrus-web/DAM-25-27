Para gestionar ficheros y guardarlos en una base de datos ligera, Python trae herramientas muy útiles

Tkinter para una interfaz gráfica sencilla (Labels, Entry y Button).

os.walk() para recorrer todos los archivos de una carpeta.

sqlite3 para almacenar información en una base de datos SQLite (un único archivo .db).


En este ejercicio detallaré cada uno de estos apartados:

**Interfaz:** dos Entry (carpeta y disco) y un Button que llama a procesar().
**Validación:** comprobar que la carpeta existe con os.path.isdir.
**Base de datos:** conexión a discos.db, creación de tabla si no existe, e inserciones parametrizadas para evitar problemas.



**Código**:

import os
import sqlite3
import tkinter as tk
from tkinter import messagebox

DB_FILE = "discos.db"

def asegurar_tabla(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS archivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disco TEXT NOT NULL,
            ruta TEXT NOT NULL,
            nombre TEXT NOT NULL,
            extension TEXT,
            tamano INTEGER,
            mtime REAL
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_archivos_disco ON archivos(disco)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_archivos_ruta ON archivos(ruta)")

def procesar():
    carpeta = entrada_carpeta.get().strip()
    disco = entrada_disco.get().strip()
		

**Validaciones básicas**
    if not carpeta:
        messagebox.showwarning("Dato faltante", "Introduce la carpeta a procesar.")
        return
    if not os.path.isdir(carpeta):
        messagebox.showerror("Carpeta no válida", f"La ruta no existe o no es una carpeta:\n{carpeta}")
        return
    if not disco:
        messagebox.showwarning("Dato faltante", "Introduce el nombre del disco (etiqueta).")
        return

    try:
        con = sqlite3.connect(DB_FILE)
        cur = con.cursor()
        asegurar_tabla(cur)

        cont = 0
        for root, dirs, files in os.walk(carpeta):
            for fname in files:
                path = os.path.join(root, fname)
                try:
                    st = os.stat(path)
                    size = st.st_size
                    mtime = st.st_mtime
                except OSError:
                    # Si no se puede leer el stat, lo salto
                    continue
                ext = os.path.splitext(fname)[1].lower().lstrip(".")
                cur.execute(
                    "INSERT INTO archivos (disco, ruta, nombre, extension, tamano, mtime) VALUES (?,?,?,?,?,?)",
                    (disco, root, fname, ext, size, mtime)
                )
                cont += 1

        con.commit()
        con.close()

        msg = f"Proceso completado. {cont} archivos indexados en '{os.path.abspath(carpeta)}' (disco='{disco}')."
        print(msg)
        messagebox.showinfo("Listo", msg)

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un problema durante el procesado:\n{e}")
				

**Interfaz gráfica (Tkinter)**
ventana = tk.Tk()
ventana.title("Indexador de archivos -> SQLite")


**Label + Entry: carpeta**
tk.Label(ventana, text="Nombre de la carpeta (ruta):").grid(row=0, column=0, sticky="w", padx=8, pady=(10, 2))
entrada_carpeta = tk.Entry(ventana, width=50)
entrada_carpeta.grid(row=1, column=0, padx=8, pady=(0, 10))


**Label + Entry: disco**
tk.Label(ventana, text="Nombre del disco (etiqueta):").grid(row=2, column=0, sticky="w", padx=8, pady=(0, 2))
entrada_disco = tk.Entry(ventana, width=30)
entrada_disco.grid(row=3, column=0, padx=8, pady=(0, 10))


**Botón: procesar**
tk.Button(ventana, text="Procesar e insertar en SQLite", command=procesar)\
    .grid(row=4, column=0, padx=8, pady=(0, 12), sticky="we")

ventana.mainloop()



Con esta mini-app se integran GUI con Tkinter, recorrido de archivos con os.walk() y almacenamiento persistente en SQLite.
