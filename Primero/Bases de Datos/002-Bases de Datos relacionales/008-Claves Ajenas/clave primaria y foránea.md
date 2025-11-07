En una base de datos relacional, la información se organiza en tablas relacionadas entre sí mediante claves primarias y foráneas.
En el caso de una tienda online, por ejemplo, es común tener una tabla de clientes, otra de productos y una tercera de pedidos.
Para representar correctamente esta relación, se utilizan las llamadas relaciones entre tablas, donde una clave foránea (foreign key) enlaza una tabla con otra.

**Clave primaria (PRIMARY KEY):** identifica de forma única cada registro dentro de una tabla.

**Clave foránea (FOREIGN KEY):** es un campo en una tabla que hace referencia a la clave primaria de otra tabla, creando así la relación entre ambas.

**Relación entre tablas:** define cómo se conectan los datos. En este caso, la relación entre clientes y pedidos


Imaginemos que ya existen las tablas clientes y productos con los siguientes datos:

Tabla clientes:

id_cliente                   nombre
12	                              Laura
13	                              Miguel


Tabla productos:

id_producto	                      nombre_producto
19	                                    Camiseta azul
20	                                    Pantalón negro


Para registrar la relacion del producto con el cliente, El comando SQL sería:

INSERT INTO pedidos (fecha, id_cliente, id_producto)
VALUES ('2025-11-07', 12, 19);


Este ejercicio muestra cómo las relaciones entre tablas permiten conectar información de manera lógica dentro de una base de datos.
La tabla pedidos actúa como puente entre clientes y productos, garantizando que cada pedido esté asociado a datos válidos.
Las claves primarias aseguran la unicidad, y las claves foráneas mantienen la integridad referencial.
