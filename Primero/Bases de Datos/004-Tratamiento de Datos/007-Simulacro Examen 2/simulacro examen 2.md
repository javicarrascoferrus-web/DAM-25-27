Voy a montar una BD para un portafolio personal con dos tablas: autores (quién crea) y piezas (qué se publica). Las vinculo con una clave foránea para poder listar piezas junto con su autor y crearé una vista que ya devuelve todo unido.

La asignacion de los nombres llevará lo siguiente:

**BD** portafolio con utf8mb4.

**autores:** Identificador (PK), nombre, apellidos, email (único).

**piezas:** id (PK), titulo, descripcion, fecha, imagen (URL) y autor_id para relacionar con autores.

**FK** piezas.autor_id → autores.Identificador.

**Vista** piezas_con_autores con JOIN.



**crear la base de datos:**

CREATE DATABASE IF NOT EXISTS portafolio
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;
USE portafolio;




**Tablas**


CREATE TABLE IF NOT EXISTS autores (

  `Identificador` INT AUTO_INCREMENT PRIMARY KEY,
	
  nombre    VARCHAR(100) NOT NULL,
	
  apellidos VARCHAR(150) NOT NULL,
	
  email     VARCHAR(150) UNIQUE
	
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS piezas (

  id         INT AUTO_INCREMENT PRIMARY KEY,
	
  titulo     VARCHAR(200) NOT NULL,
	

  descripcion TEXT,
	
  fecha      DATE,
	
  imagen     VARCHAR(300),   -- URL de la imagen
	
  autor_id   INT NOT NULL,
	
  CONSTRAINT fk_piezas_autor
	
    FOREIGN KEY (autor_id) REFERENCES autores(`Identificador`)
		
    ON UPDATE CASCADE
		
    ON DELETE RESTRICT
		
	
) ENGINE=InnoDB;






**Insertar datos**:

INSERT INTO autores (nombre, apellidos, email)

VALUES ('Carlos', 'Pérez López', 'carlos@example.com');


INSERT INTO piezas (titulo, descripcion, fecha, imagen, autor_id)

VALUES (
  'Cartel tipográfico',
	
  'Cartel A2 hecho en Illustrator con paleta limitada.',
	
  '2024-10-15',





**Vista cruzada*:

CREATE OR REPLACE VIEW piezas_con_autores AS

SELECT

  p.id,
	
  p.titulo,
	
  p.descripcion,
	
  p.fecha,
	
  p.imagen,
	
	a.`Identificador`                  AS autor_id,
	 a.nombre                          AS autor_nombre,
 a.apellidos                          AS autor_apellidos,
 a.email                                AS autor_email
 
FROM piezas p

JOIN autores a ON a.`Identificador` = p.autor_id;


**Consultar la tabla de datos**:

SELECT * FROM piezas_con_autores ORDER BY fecha DESC, id DESC;


Queda creada la BD portafolio, con autores y piezas, claves primarias y una foránea para relacionarlas. Se cargan registros de ejemplo y se construye la vista piezas_con_autores para consultar todas las piezas con los datos del autor de una vez
