###  Creación tablas
CREATE TABLE atletas_natacion (
    id_atleta INT 
    nombre VARCHAR(100) 
    apellidos VARCHAR(100)
    tiempo_100m INT                
);

El tipo INT se usa para almacenar números enteros y el tipo VARCHAR se utiliza para almacenar cadenas de texto

##  Insertar datos 

INSERT INTO atletas_natacion 
(Juan Pérez 50), (VARCHAR)
(Ana López 52), (VARCHAR)
(Carlos Rodríguez 48); (VARCHAR)

Para insertar datos en la tabla, se utiliza el comando INSERT INTO con los tipos de datos más adecuados para el contexto.

## Consulta de datos
SELECT
    nombre,
    apellidos,
    tiempo_100m
FROM
    atletas_natacion;
		
	La consulta solicita seleccionar y mostrar solo las columnas nombre, apellidos y tiempo de todos los atletas.
	
	
El ejercicio de crear la tabla atletas_natacion es una demostración de la importancia de la correcta elección de los tipos de datos en el diseño de cualquier base de datos, juntando asi por atleta el nombre, apellido y tiempo.

La correcta aplicación de tipos de datos como INT y VARCHAR es el primer paso para construir una base de datos que no solo almacene los datos de los atletas de manera organizada, sino que también garantice que los datos son correctos.
