En el ejercicio original de la unidad 3 los registros se guardaban solo en una lista en memoria, lo que significa que se perdían al cerrar el programa.
En esta versión, cada acción del menú (crear, listar, actualizar, eliminar) usará sentencias SQL para que los datos queden guardados en una base de datos SQLite.
Esto permite practicar la persistencia de la información, mantener la misma estructura de control con while True.

Para ello voy a llevarlo a la práctica con los siguientes comandos:


**Código**:

import sqlite3

with sqlite3.connect("unidad3.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS registros (id INTEGER PRIMARY KEY, texto TEXT)")

while True:
    op = input("\nOpciones: crear | listar | actualizar | eliminar | salir\n> ").lower()

    if op == "crear":
        t = input("Nuevo registro: ")
        with sqlite3.connect("unidad3.db") as c:
            c.execute("INSERT INTO registros (texto) VALUES (?)", (t,))
            c.commit()
        print("Registro añadido.")

    elif op == "listar":
        with sqlite3.connect("unidad3.db") as c:
            for i, (id_, txt) in enumerate(c.execute("SELECT id, texto FROM registros"), 1):
                print(f"{i}. [{id_}] {txt}") or None

    elif op == "actualizar":
        try:
            i = int(input("ID a actualizar: "))
            t = input("Nuevo texto: ")
            with sqlite3.connect("unidad3.db") as c:
                c.execute("UPDATE registros SET texto=? WHERE id=?", (t, i))
                print("Actualizado." if c.total_changes else "No existe ese ID.")
                c.commit()
        except ValueError:
            print("ID inválido.")

    elif op == "eliminar":
        try:
            i = int(input("ID a eliminar: "))
            with sqlite3.connect("unidad3.db") as c:
                c.execute("DELETE FROM registros WHERE id=?", (i,))
                print("Eliminado." if c.total_changes else "No existe ese ID.")
                c.commit()
        except ValueError:
            print("ID inválido.")

    elif op == "salir":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")




Este ejercicio es la evolución natural del CRUD con listas de la unidad 3, ahora con almacenamiento persistente usando SQL y SQLite.
Refuerza el uso de estructuras de control (while, if/elif), variables, y operaciones CRUD reales.
