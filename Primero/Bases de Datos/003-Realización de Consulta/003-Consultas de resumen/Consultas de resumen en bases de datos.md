En este ejercicio se trabaja con una vista llamada vista_pedidos, que contiene la información de los pedidos realizados (por ejemplo, identificador, fecha, cliente, producto y precio total).
El objetivo es practicar el uso de funciones de agregación en SQL: MAX(), SUM(), COUNT() y AVG().

**Las funciones que se van a usar son:**

MAX(campo) → Devuelve el valor máximo de una columna numérica.

SUM(campo) → Suma todos los valores numéricos de una columna.

COUNT → Cuenta el número total de registros o filas

AVG(campo) → Calcula el promedio (media aritmética) de los valores numéricos

Vamos a llevarlo a cabo y aplicarlo en el ejercicio:


**Ejercicio 1: Pedido con el precio total más alto:**

SELECT MAX(precio_total) AS precio_maximo
FROM vista_pedidos;



**Ejercicio 2: Suma total de todos los pedidos**
SELECT SUM(precio_total) AS suma_total_pedidos
FROM vista_pedidos;


**Ejercicio 3: Número total de pedidos realizados**
SELECT COUNT AS numero_pedidos
FROM vista_pedidos;


**Ejercicio 4: Promedio del precio total de los pedidos**
SELECT AVG(precio_total) AS promedio_precio_total
FROM vista_pedidos;


Con estas consultas, pude extraer información resumida de la vista vista_pedidos de forma sencilla.
Usé funciones de agregación (MAX, SUM, COUNT, AVG) para calcular el pedido más caro, la suma total de los precios, el número de pedidos y el promedio del precio total.
