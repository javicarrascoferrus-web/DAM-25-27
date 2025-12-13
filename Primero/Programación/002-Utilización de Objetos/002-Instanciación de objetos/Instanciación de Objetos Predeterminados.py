En Python existen muchos módulos que amplían sus funciones básicas. Uno de los más importantes es el módulo math, que incluye herramientas matemáticas muy útiles.
En este ejercicio voy a usar el módulo math para calcular el área de un círculo a partir de su radio y, además, aprenderé a redondear números con la función round().


En Python, el valor de π se obtiene con math.pi.
También usaré la función round() para redondear el resultado a dos decimales.

**Código**:


import math    (Importamos el módulo math)

radio = 5   (Radio del círculo en unidades)
area = math.pi * (radio ** 2)   (Fórmula del área)


(Redondeamos el resultado a dos decimales):
area_redondeada = round(area, 2)

print("El área del círculo con radio", radio, "es:", area_redondeada)


Con este ejercicio he aprendido a trabajar con el módulo math y a usar sus funciones principales, como math.pi. También he visto cómo redondear resultados con round() para mostrar valores más limpios.
