En programación, los objetos pueden tener propiedades que guardan información sobre su estado. Un buen ejemplo de esto lo encontramos en el módulo math de Python, que incluye muchas funciones y constantes matemáticas.

Para comenzar, importo el módulo math con un alias para hacerlo más cómodo de usar, en este caso matematicas.
Después, pido al usuario que introduzca el radio de la circunferencia con la función input().


**Código**:


import math as matematicas    (Importamos el módulo math con alias)

radio = float(input("Introduce el radio de la circunferencia: "))

area = matematicas.pi * (radio ** 2)    (Fórmula del área: π * r²)

print("El área de la circunferencia es:", round(area, 2))


Después de teclear esto y añadirle por ejemplo el número 5 al valor del radio, se mostrará lo siguiente:

Introduce el radio de la circunferencia: 5
El área de la circunferencia es: 78.54


Este ejercicio muestra cómo acceder a la propiedad pi del módulo math y aplicarla en un caso práctico: calcular el área de una circunferencia.
Aquí se combina el uso de módulos, propiedades y operaciones matemáticas básicas en Python
