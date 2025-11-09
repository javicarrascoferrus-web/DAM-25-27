**BD:** CREATE DATABASE … con utf8mb4 para acentos.

**Tablas:** autores con datos de autor y PK; entradas con PK y columna autor_id.

**Claves:** PK en ambas y FK entradas.autor_id → autores.id_autor con ON UPDATE CASCADE.

**Inserción:** primero autores (desde el fichero de muestra), luego libros.

**Consulta:** LEFT JOIN para ver libros con nombre y email del autor (si faltara autor, el libro sigue saliendo).



3) Aplicación práctica (SQL listo para ejecutar) (25%)
### 1) Crear la base de datos
CREATE DATABASE IF NOT EXISTS biblioteca_carlos
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;
USE biblioteca_carlos;



### 2) Crear tablas
CREATE TABLE IF NOT EXISTS autores (
  id_autor   INT AUTO_INCREMENT PRIMARY KEY,
  nombre     VARCHAR(120) NOT NULL,
  email      VARCHAR(150) UNIQUE,
  web        VARCHAR(200)
) ENGINE=InnoDB;



CREATE TABLE IF NOT EXISTS entradas (
  id_entrada INT AUTO_INCREMENT PRIMARY KEY,
  titulo     VARCHAR(200) NOT NULL,
  anio       INT,
  genero     VARCHAR(80),
  autor_id   INT NOT NULL,
  -- 3) Clave foránea (relación con autores)
  CONSTRAINT fk_entradas_autor
    FOREIGN KEY (autor_id)
    REFERENCES autores(id_autor)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;



### 4) Insertar datos en AUTORES
-- (Usa aquí los valores del archivo "005-insercion de datos de muestra.sql")
-- Ejemplo mínimo por si necesitas probar rápido:
INSERT INTO autores (nombre, email, web) VALUES
  ('Isabel Allende', 'isabel@example.com', 'https://isabel-allende.test'),
  ('Haruki Murakami', 'murakami@example.com', 'https://murakami.test'),
  ('Ursula K. Le Guin', 'ursula@example.com', 'https://le-guin.test');



### 5) Insertar datos en ENTRADAS (algunos ejemplos)
INSERT INTO entradas (titulo, anio, genero, autor_id) VALUES
  ('La casa de los espíritus', 1982, 'Realismo mágico', 1),
  ('Tokio Blues', 1987, 'Ficción', 2),
  ('Los desposeídos', 1974, 'Ciencia ficción', 3);

  

### 6) Consulta compleja con LEFT JOIN
SELECT
  e.id_entrada,
  e.titulo,
  e.anio,
  e.genero,
  a.nombre AS autor,
  a.email  AS email_autor
FROM entradas e
LEFT JOIN autores a ON a.id_autor = e.autor_id
ORDER BY e.titulo;


El fichero con los INSERT de autores, puedes importarlo así:

mysql -u tu_usuario -p biblioteca_carlos < 005-insercion\ de\ datos\ de\ muestra.sql


**Errores comunes (y cómo evitarlos):**

Insertar libros antes de autores → falla la FK. Solución: primero autores.

Emails duplicados en autores → hay UNIQUE. Cambia el email.

Borrar un autor con libros → ON DELETE RESTRICT. Borra/mueve libros antes o cambia la política si te interesa.



He creado la BD biblioteca_carlos, definido autores y entradas con PK y la relación mediante FK, insertado datos (autores desde el fichero de muestra) y preparado un LEFT JOIN que lista los libros junto con el nombre y email del autor. Con esto se enlaza lo visto de modelo relacional, claves, integridad referencial y consultas JOIN.
