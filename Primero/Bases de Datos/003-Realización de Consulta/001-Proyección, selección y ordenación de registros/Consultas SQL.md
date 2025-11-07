

Hoy practico consultas SQL centradas en proyección (elegir columnas), selección (filtrar filas con WHERE) y ordenación (usar ORDER BY). Para los filtros por texto, usaré comodines con LIKE, especialmente el de inicio ('texto%') para encontrar apellidos que empiecen por un prefijo.

Asumo una tabla clientes con las columnas: nombre, apellidos, telefono, email.



Selección con comodín de inicio: WHERE apellidos LIKE 'Castro%' devuelve filas donde el apellido empieza por “Castro”.

**Ordenación descendente:** ORDER BY apellidos DESC coloca de Z→A.

**Proyección de columnas:** SELECT nombre, apellidos devuelve solo esas columnas.

**Ordenación por varios criterios:** ORDER BY apellidos ASC, nombre ASC aplica orden alfabético por apellido y, en empates, por nombre.

Detalles a tener en cuenta:

Colaciones/acentos pueden afectar el orden y la comparación (p. ej. “Álvarez”).

LIKE distingue o no mayúsculas según la colación; si hay dudas, normalizar o usar funciones (LOWER()).


**Ejercicio 1: Comodín de inicio (apellidos que empiecen por “Castro”)**
SELECT nombre, apellidos, telefono, email
FROM clientes
WHERE apellidos LIKE 'Castro%';

**Ejercicio 2: Ordenar por apellidos en orden descendente**
SELECT nombre, apellidos, telefono, email
FROM clientes
ORDER BY apellidos DESC;

**Ejercicio 3: Proyección (solo nombres y apellidos)**
SELECT nombre, apellidos
FROM clientes;

**Ejercicio 4: Varios criterios (apellidos ASC, nombre ASC)**
SELECT nombre, apellidos, telefono, email
FROM clientes
ORDER BY apellidos ASC, nombre ASC;

Errores comunes y cómo evitarlos:

Olvidar el % en el comodín → LIKE 'Castro' solo encuentra coincidencia exacta, no prefijos.

Espacios extra en apellidos (p. ej., ' Castro') → pueden romper el filtro. Se puede limpiar datos o usar TRIM(apellidos).

Ordenación inesperada por tildes → revisar la colación de la BD (ideal utf8mb4_unicode_ci o similar).

Selección de columnas: si solo quieres ver ciertos campos, usa proyección (no SELECT *).


Con WHERE ... LIKE 'Castro%' filtro por prefijo; 
con ORDER BY controlo la dirección del orden; 
con proyección (SELECT columnas) muestro solo lo necesario; 
y con varios criterios en ORDER BY resuelvo empates de forma consistente. Estas tres ideas (selección, proyección y ordenación) son la base para consultas más completas que luego combinaremos con JOINs y funciones de agregado.
