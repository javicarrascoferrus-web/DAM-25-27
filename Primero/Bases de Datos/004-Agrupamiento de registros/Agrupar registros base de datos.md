Trabajar con la tabla clientes nunca fué fácil, ya que siempre hay datos que rellenar, ya sean clientes nuevos, clientes viejos o clientes que están de paso, el objetivo es trabajar con la tabla clientes para:

1. listar todos los registros,

2. añadir una columna localidad,

3. rellenar esa columna con los datos correctos, 

4. agrupar por localidad para contar cuántos clientes hay en cada una.

Vamos a aplicar SQL para cada tabla:

**Paso 1. Seleccionar todos los clientes (estado inicial)**
SELECT *
FROM clientes;

**Paso 2. Añadir la columna localidad**
ALTER TABLE clientes
  ADD localidad VARCHAR(255) NOT NULL AFTER email;

**Paso 3. Rellenar localidad**

UPDATE clientes,  localidad = 'Madrid'   WHERE Identificador = 1;
UPDATE clientes,  localidad = 'Sevilla'  WHERE Identificador = 2;
UPDATE clientes, localidad = 'Valencia' WHERE Identificador = 3;
UPDATE clientes,  localidad = 'Madrid'   WHERE Identificador = 4;
UPDATE clientes, localidad = 'Bilbao'   WHERE Identificador = 5;

**Paso 4. Consulta final: agrupar y contar por localidad**
SELECT
  localidad,
  COUNT(Identificador) AS num_clientes
FROM clientes
GROUP BY localidad;


He listado los clientes, añadido la columna localidad, cargado los datos y generado un resumen por localidad con GROUP BY y COUNT(). Esto refuerza conceptos básicos de consulta, definición y actualización en SQL, y conecta con contenidos de la unidad sobre agregación y preparación de datos para informes sencillos.
