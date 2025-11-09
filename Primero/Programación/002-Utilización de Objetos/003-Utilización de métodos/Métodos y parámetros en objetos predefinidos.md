En Python existen bibliotecas que amplían las funciones básicas del lenguaje. Una de las más importantes es la biblioteca math, que incluye muchas herramientas matemáticas, como potencias, raíces o el valor de π.
En este ejercicio voy a utilizar esta biblioteca para calcular la raíz cuadrada de un número.

El primer paso es importar la biblioteca math, pero en este caso le pondré un alias más corto o más fácil de recordar, usando la palabra clave as.
Después, definiré una variable con el nombre metros_natacion, donde guardaré el número que representa los metros nadados.
Luego, con el método sqrt() calcularé su raíz cuadrada y la guardaré en otra variable llamada raiz_natacion.


**Código**:


import math as matematicas    (Importamos la biblioteca math con un alias)

metros_natacion = 100   (Número de metros nadados)
raiz_natacion = matematicas.sqrt(metros_natacion)   (Calculamos la raíz cuadrada)

print("La raíz cuadrada de", metros_natacion, "es:", raiz_natacion)


**Resultado**:
La raíz cuadrada de 100 es: 10.0


Con este ejercicio he aprendido a importar la biblioteca math y a usar su método sqrt() para calcular raíces cuadradas.
También he practicado el uso de alias con as, lo que hace el código más claro y cómodo de leer.
