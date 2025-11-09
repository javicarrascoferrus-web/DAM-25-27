En este ejercicio voy a combinar dos conceptos importantes de la programación en Python: el uso de funciones y los bucles de repetición.
El objetivo es mostrar un saludo cada día, hasta llegar al día 31, sin utilizar estructuras de control como if o else.

Defino una función llamada saludar que recibe dos parámetros: nombre y edad.
Declaro una variable llamada dia con valor inicial 1, que servirá para contar los días del mes.
Escribo un bucle while True, que se repetirá constantemente hasta que la variable dia supere 31.


**Código**:


####  Definimos la función saludar
def saludar(nombre, edad):
    return f"Hola {nombre}, tienes {edad} años. ¡Que tengas un gran día!"



#### Inicializamos la variable del día
dia = 1


#### Bucle while que se ejecuta hasta el día 31
while True:
    print("Hoy es el día", dia, "del mes")
    print(saludar("Javier", 21))      (Llamada a la función dentro del bucle)
    print()      (Línea en blanco para separar cada día)

    dia += 1       (Aumenta el número de día)

    if dia > 31:      (Condición para salir del bucle)
        break
				
				
				
Este programa combina dos estructuras fundamentales de Python: las funciones y los bucles.
He aprendido cómo crear una función que devuelve un texto y cómo integrarla dentro de un while para ejecutar acciones repetitivas.
Además, he practicado el uso de la variable de control dia para limitar la repetición sin depender de condicionales if o else.
