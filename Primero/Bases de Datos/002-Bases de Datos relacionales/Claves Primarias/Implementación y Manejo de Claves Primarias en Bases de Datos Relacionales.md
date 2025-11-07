El concepto de Clave Primaria es el pilar fundamental de la integridad de datos en el Modelo Relacional de bases de datos.

Una Clave Primaria es un campo o un conjunto de campos dentro de una tabla cuyo valor permite identificar de forma única cada registro.

#### Clave primaria a tabla productos
ALTER TABLE productos
ADD Identificador INT;

ALTER TABLE productos
MODIFY COLUMN Identificador INT NOT NULL AUTO_INCREMENT;

ALTER TABLE productos
ADD PRIMARY KEY; (identificador)


#### Clave primaria tabla clientes
ALTER TABLE clientes
ADD Identificador INT;

ALTER TABLE clientes
MODIFY COLUMN Identificador INT NOT NULL AUTO_INCREMENT;

ALTER TABLE clientes
ADD PRIMARY KEY; (identificador)

El objetivo es verificar que las claves primarias (Identificador) con **AUTO_INCREMENT** se configuraron correctamente en las tablas *productos* y *clientes* mediante la inserción de datos

## Funcionamiento


INSERT INTO productos VALUES ('Laptop', 999.99);


INSERT INTO productos VALUES ('Monitor Curvo', 299.99);


Al configurar la PK en productos y clientes con AUTO_INCREMENT, no solo estás haciendo que la inserción sea más fácil, sino que estás aplicando las reglas fundamentales del modelo relacional.
