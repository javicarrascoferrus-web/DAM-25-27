En este ejercicio como final de unidad voy a montar la base de datos de un blog/portafolio con dos tablas: 
piezas (noticias o trabajos del portafolio) y autores. 
La idea es relacionarlas mediante una clave foránea para saber quién escribió cada pieza. 
Además, haré una consulta cruzada (LEFT JOIN), crearé una vista para simplificar consultas y un usuario con permisos.

Desarrollo detallado y preciso

Base de datos: blog_portafolio

Tablas:

autores (PK: id_autor): nombre, apellidos, email (puede ser UNIQUE).

piezas (PK: id_pieza): titulo, descripcion, fecha, imagen, autor_id (FK → autores.id_autor).

Relación: 1 autor → N piezas (1:N) mediante autor_id.

Claves:

Primarias con PRIMARY KEY.

Foránea con FOREIGN KEY ... REFERENCES ... ON UPDATE CASCADE ON DELETE RESTRICT.

Vamos a teclear los siguientes codigos y llevarlo a la práctica:

1- Crear la base de datos y usarla

CREATE DATABASE IF NOT EXISTS blog_portafolio
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE blog_portafolio;

2-  Crear tabla autores

CREATE TABLE autores (
	id_autor     INT AUTO_INCREMENT PRIMARY KEY,
  nombre       VARCHAR(80)  NOT NULL,
  apellidos    VARCHAR(120) NOT NULL,
  email        VARCHAR(150) NOT NULL UNIQUE


3-  Crear tabla piezas (noticias/portafolio)

CREATE TABLE piezas (
  id_pieza     INT AUTO_INCREMENT PRIMARY KEY,
  titulo       VARCHAR(150) NOT NULL,
  descripcion  TEXT         NOT NULL,
  fecha        DATE         NOT NULL,
  imagen       VARCHAR(255) NULL,
  autor_id     INT          NOT NULL,
  CONSTRAINT fk_piezas_autor
    FOREIGN KEY (autor_id) REFERENCES autores(id_autor)
    ON UPDATE CASCADE
    ON DELETE RESTRICT


4-  Insertar un registro en cada tabla
INSERT INTO autores (nombre, apellidos, email)
VALUES ('Laura', 'Serrano Ruiz', 'laura.serrano@example.com');

INSERT INTO piezas (titulo, descripcion, fecha, imagen, autor_id)
VALUES (
  'Rediseño de identidad visual',
  'Caso de estudio del rediseño de marca para una startup tech.',
  '2025-11-07',
  'https://cdn.ejemplo.com/img/redisenyo.jpg',
  1
);

5-  Petición cruzada (LEFT JOIN): piezas con sus autores
SELECT
  p.id_pieza,
  p.titulo,
  p.fecha,
  CONCAT(a.nombre, ' ', a.apellidos) AS autor,
  a.email
FROM piezas p
LEFT JOIN autores a ON a.id_autor = p.autor_id;

6-  Crear una vista para consultas frecuentes
CREATE OR REPLACE VIEW vw_piezas_autores AS
SELECT
  p.id_pieza                   AS id_pieza,
  p.titulo                     AS titulo,
  p.fecha                      AS fecha,
  p.imagen                     AS imagen,
  CONCAT(a.nombre, ' ', a.apellidos) AS autor,
  a.email                      AS email_autor
FROM piezas p
JOIN autores a ON a.id_autor = p.autor_id;

7-  Crear un usuario con permisos para acceder al esquema
-- (ajusta la contraseña a tu política)
CREATE USER IF NOT EXISTS 'user_blog'@'localhost'
IDENTIFIED BY 'PASSWORD';

8- Permisos mínimos útiles para gestionar el blog (lectura/escritura básica)
GRANT SELECT, INSERT, UPDATE
ON blog_portafolio.* TO 'user_blog'@'localhost';
