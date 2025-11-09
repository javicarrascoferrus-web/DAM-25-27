En este ejercicio se busca aplicar las estructuras de control condicional (if, elif, else) para clasificar a una persona según su edad.
El programa pedirá al usuario que introduzca su edad y, en función del valor, mostrará a qué categoría de natación pertenece.

Para resolver el problema, primero pedimos al usuario que introduzca su edad mediante la función input().
Como los datos introducidos por teclado son de tipo texto, es necesario convertirlos a número entero usando int().
Después, mediante las estructuras if, elif y else, comparamos la edad introducida con los rangos definidos para cada categoría.


A continuación tecleo el código con los comandos anteriormente indicados:



**Código**:



#### Pedir al usuario su edad

edad = int(input("Introduce tu edad: "))

#### Clasificación según la edad

if edad < 10:
    print("Categoría: Nadador infantil")
elif edad >= 10 and edad <= 15:
    print("Categoría: Nadador juvenil")
elif edad >= 16 and edad <= 20:
    print("Categoría: Nadador juvenil avanzado")
else:
    print("Categoría: Nadador adulto")




Cuando ejecutamos, el resultado es este:


Introduce tu edad: 14
Categoría: Nadador juvenil


En conclusión, este programa permite clasificar a los nadadores por edad utilizando estructuras condicionales básicas (if, elif, else).

Este ejercicio se relaciona con otros temas del temario, como el uso de entradas de datos y las estructuras de control de flujo, que son fundamentales para crear programas que respondan de forma dinámica a las acciones del usuario.
