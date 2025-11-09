Crear una base de datos con todos los datos que hemos visto en este trimestre es un poco complejo, porque tiene mucha información relevante, para ello vamos a empezar con:

BD: blog_portafolio

**Tablas mínimas:**

autores(id_autor, nombre, apellidos, email)

piezas(id_pieza, titulo, descripcion, fecha, imagen, autor_id) (FK → autores.id_autor)

**Vista existente:**

vw_piezas_autores(id_pieza, titulo, fecha, imagen, autor, email_autor)

**Operaciones:**

Insertar varias piezas (fechas distintas).

Seleccionar con orden ascendente y descendente por fecha.

Seleccionar desde la vista creada.

## **Creación de la tabla**##

**Empezamos utilizando la base de datos del blog:**
USE blog_portafolio;


**Ver autores de la tabla:**
SELECT * FROM autores;

**Insertar número representativo de atrticulos:**
INSERT INTO piezas (titulo, descripcion, fecha, imagen, autor_id) VALUES


**Comprobar inserciones:**
SELECT id_pieza, titulo, fecha, autor_id FROM piezas;


**Orden ascendente:**
SELECT id_pieza, titulo, fecha
FROM piezas
ORDER BY fecha ASC;


**Orden descendente:**
SELECT id_pieza, titulo, fecha
FROM piezas
ORDER BY fecha DESC;


**Limite:**
SELECT id_pieza, titulo, fecha
FROM piezas
ORDER BY fecha DESC
LIMIT 3;


**Filtro+Orden:**
FROM piezas
WHERE YEAR(fecha) = 2025
ORDER BY fecha DESC;

**Vista creada:**
SELECT
  id_pieza,
  titulo,
  fecha,
  autor,
  email_autor
FROM vw_piezas_autores
ORDER BY fecha DESC;


Con estas inserciones y consultas comprobé cómo cargar contenido real y listarlo ordenado (asc/desc), además de reutilizar la vista para obtener pieza + autor sin repetir JOINS.
