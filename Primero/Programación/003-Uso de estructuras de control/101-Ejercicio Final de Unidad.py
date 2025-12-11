Vamos a relacionar ejercicios de anteriores unidades para realizar este, en este caso el de la Unidad 1.
Para ello vamos a realizar la siguiente estructura:

Estructura principal: while True (bucle infinito).

Entrada de usuario: input() para leer la opción y los datos.

Selección: if/elif para discriminar entre crear, listar, actualizar, eliminar.


Ahora escribiremos el Código en relacion a lo anterior:

**Código**:





while True:
    print("\nOpciones: crear | listar | actualizar | eliminar | salir")
    opcion = input("Elige una opción: ").lower()

    if opcion == "crear":
        nuevo = input("Introduce un nuevo registro: ")
        registros.append(nuevo)
        print("Registro añadido.")

    elif opcion == "listar":
        print("\nRegistros actuales:")
        for i, r in enumerate(registros, start=1):
            print(i, "-", r)

    elif opcion == "actualizar":
        indice = int(input("Número del registro a actualizar: ")) - 1
        nuevo = input("Nuevo valor: ")
        registros[indice] = nuevo
        print("Registro actualizado.")

    elif opcion == "eliminar":
        indice = int(input("Número del registro a eliminar: ")) - 1
        registros.pop(indice)
        print("Registro eliminado.")

    elif opcion == "salir":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")



Este patrón es el primer paso hacia una aplicación completa: más adelante podría validar mejor los datos, persistirlos en ficheros o base de datos o separar en funciones.
Con este ejercicio he unido el input de la U1 con la gestión de datos de la U2, construyendo un menú CRUD continuo con while True y selección por if/elif.
