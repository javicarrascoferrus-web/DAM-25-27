El programa original está “todo junto” en una única función principal, lo que complica leerlo, mantenerlo y ampliarlo. La idea es refactorizar: separar la lógica en funciones pequeñas y claras.

Variable global: CLIENTES (lista de strings).

**Funciones:**

imprimir_bienvenida(): muestra un saludo y una breve descripción.

mostrar_menu(): pinta las opciones y devuelve la opción elegida.

insertarCliente(): pide un nombre por teclado y lo añade a CLIENTES si es válido.

listadoClientes(): recorre CLIENTES y muestra los nombres con numeración.

main(): bucle principal que coordina el flujo del programa.



Tecleamos el siguiente código para ver que funciona la teoría:



def imprimir_bienvenida():
    print("=" * 40)
    print("      AGENDA DE CLIENTES (BÁSICA)     ")
    print("=" * 40)
    print("Opciones: añadir clientes y listar la agenda.\n")

def mostrar_menu():
    print("Menú principal:")
    print("  1) Insertar cliente")
    print("  2) Listar clientes")
    print("  3) Salir")
    opcion = input("Elige una opción (1-3): ").strip()
    return opcion

def insertarCliente():
    global CLIENTES
    print("\n-- Insertar cliente --")
    nombre = input("Introduce el nombre del nuevo cliente: ").strip()

   **Validaciones simples**
		 
    if nombre == "":
        print("No se ha añadido: el nombre está vacío.\n")
        return



   **Mostrar con numeración**
    indice = 1
    for c in CLIENTES:
        print(f"{indice}. {c}")
        indice += 1
    print("")  # línea en blanco final

def main():
    imprimir_bienvenida()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            insertarCliente()
        elif opcion == "2":
            listadoClientes()
        elif opcion == "3":
            print("\nSaliendo... ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")
						
						
Al dividir el programa en funciones pequeñas, el código queda más claro, mantenible y ampliable.
Esta práctica conecta con la unidad de estructuración y buenas prácticas: separar responsabilidades, usar estado compartido controlado y construir un bucle de interacción sencillo con entradas del usuario
