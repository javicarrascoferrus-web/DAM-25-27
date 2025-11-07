

En SQL, los operadores de comparación (como >, <, =, <>, >=, <=) permiten filtrar o generar condiciones dentro de las consultas, mientras que los alias de columna (AS) sirven para renombrar columnas o cálculos y hacer que los resultados sean más comprensibles.

En este ejercicio voy a practicar ambos conceptos con la tabla productos, que contiene información básica de los artículos (por ejemplo: nombre, precio y un campo que indica si necesitan carga o transporte). A partir de ahí, haré dos consultas distintas: una usando operadores de comparación y otra usando alias y cálculos sencillos.


##**🔹 Primer ejercicio: Operadores de comparación**

Objetivo: Mostrar el nombre y precio de los productos, e incluir dos campos nuevos:

carga_transporte → muestra “Sí” si el producto necesita carga, y “No” en caso contrario.

precio_transporte → muestra un costo adicional (por ejemplo, 15 €) si necesita carga, o 0 € si no.


Para lograrlo, puedo usar los operadores de comparación (=) directamente en una expresión con el operador ternario de MySQL (CASE WHEN no se puede usar porque el enunciado lo prohíbe, pero puedo combinar comparaciones y multiplicaciones lógicas).
Por ejemplo, al comparar una condición como (necesita_carga = 'Sí'), MySQL devuelve 1 si es verdadera o 0 si es falsa. Esto permite hacer pequeños cálculos lógicos sin IF.

##**🔹 Segundo ejercicio: Alias de columna**

Objetivo: Mostrar el nombre y precio, renombrándolos como:

Nombre del Producto

Precio Base

Y añadir:

IVA 21%: calculado como precio * 0.21

Total Precio: calculado como precio + (precio * 0.21)

Todo usando alias para mostrar nombres más claros en los resultados.


##**Ejercicio 1: Operadores de comparación**
SELECT
  nombre,
  precio,
  (necesita_carga = 'Sí') AS carga_transporte,
  (precio * (necesita_carga = 'Sí') * 0.15) AS precio_transporte
FROM productos;


🔹 Explicación:

(necesita_carga = 'Sí') devuelve 1 si el producto necesita carga, 0 si no.

Multiplico el precio por 0.15 (15%) solo cuando el resultado es 1.

Así obtengo un “precio de transporte” sin usar IF.

🔹 Ejemplo de salida:

nombre	precio	carga_transporte	precio_transporte
Mesa madera	200.00	1	30.00
Camiseta blanca	25.00	0	0.00


##**Ejercicio 2: Alias de columna**
SELECT
  nombre AS 'Nombre del Producto',
  precio AS 'Precio Base',
  (precio * 0.21) AS 'IVA 21%',
  (precio + (precio * 0.21)) AS 'Total Precio'
FROM productos;


🔹 Explicación:

Uso AS para poner nombres más descriptivos.

El campo IVA 21% calcula el 21% del precio.

Total Precio suma el precio base más el IVA.

🔹 Ejemplo de salida:

Nombre del Producto	Precio Base	IVA 21%	Total Precio
Mesa madera	200.00	42.00	242.00
Camiseta blanca	25.00	5.25	30.25


Con este ejercicio aprendí cómo los operadores de comparación pueden usarse no solo en cláusulas WHERE, sino también dentro de expresiones para generar valores condicionales sin necesidad de IF.
Además, los alias de columna son muy útiles para dar claridad y profesionalismo a las consultas, sobre todo cuando generamos informes o exportamos resultados.

Estos conceptos son la base para consultas más avanzadas, donde combinaremos condiciones, cálculos y alias con funciones de agregación o agrupamiento.
