En una base de datos, antes de poder trabajar con tablas o modificar datos, lo primero es establecer una conexión con el sistema gestor de bases de datos.
Uno de los pasos habituales al trabajar con bases de datos es modificar la estructura de las tablas, por ejemplo, cambiar el tipo de una columna o permitir valores nulos.

El comando principal utilizado en este ejercicio es:

ALTER TABLE clientes
  MODIFY COLUMN apellidos VARCHAR(100) NULL;
	
Después de modificar la tabla, se insertan algunos registros con el comando INSERT INTO:

INSERT INTO clientes (nombre, apellidos)
VALUES ('Juan', NULL),
       ('María', 'García'),
       ('Pedro', 'López');
			 
			 
Este comando muestra todas las filas de la tabla, incluyendo aquellas donde apellidos es NULL.

En este ejercicio he aprendido cómo modificar la estructura de una tabla usando ALTER TABLE y cómo insertar registros con valores NULL en una base de datos.
