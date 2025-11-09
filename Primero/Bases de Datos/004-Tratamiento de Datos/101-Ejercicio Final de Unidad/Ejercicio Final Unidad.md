En esta actividad verifico que sé actualizar y eliminar datos en una base relacional real. Las actualizaciones permiten corregir o mejorar campos y las eliminaciones sirven para limpiar registros que ya no aplican.

**UPDATE**: modifica columnas con SET y filtro WHERE (siempre imprescindible).

**DELETE:** borra filas con WHERE. Con FK RESTRICT, no se puede borrar un autor si hay piezas vinculadas.

**Transacciones:** START TRANSACTION → validación → COMMIT (o ROLLBACK).


**Asumo el esquema previo:**

autores(Identificador PK, nombre, apellidos, email, …)

piezas(id PK, titulo, descripcion, fecha, imagen, autor_id FK)


**Actualizaciones en base de datos**:

START TRANSACTION;


SELECT id, titulo FROM piezas WHERE id = 3;


UPDATE piezas

SET titulo = 'Cartel tipográfico (edición revisada)'

WHERE id = 3;




**Eliminaciones **:

START TRANSACTION;


SELECT id, titulo FROM piezas WHERE id = 4;


DELETE FROM piezas

WHERE id = 4;

COMMIT;


**Verificación**

Para Comprobar estado actual:

SELECT * FROM autores ORDER BY Identificador;

SELECT * FROM piezas ORDER BY id;


He demostrado operaciones de actualización (UPDATE simple y con JOIN) y eliminación (DELETE controlado) sobre la BD de portafolio/blog, respetando la integridad referencial.
