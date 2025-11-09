Para este ejercicio crearé dos tablas, una llamada lineas-pedido y la otra pedidos-con-linea.
Además de crear e insertar datos, quiero consultar la información combinada para ver fecha, cliente, unidades, producto y el importe total

**Tabla pedidosconlineas:** pedido con PK Identificador, fecha e id_cliente.

**Tabla lineaspedido:** cada fila representa un producto en el pedido, con PK Identificador, FK pedidos_id → pedidosconlineas.Identificador, producto_id y unidades.

Voy a insertar el código SQL para crear las tablas asignadas:

CREATE TABLE `empresarial`.`pedidosconlineas` (`Identificador` INT NOT NULL AUTO_INCREMENT , `fecha` DATE NOT NULL , `id_cliente` INT NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;

CREATE TABLE `empresarial`.`lineaspedido` (`Identificador` INT NOT NULL AUTO_INCREMENT , `producto_id` INT NOT NULL , `unidades` INT NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;


En ella, vamos a insertar los datos simulando que un cliente realiza un pedido:

-- el cliente hace un pedido
INSERT INTO `pedidosconlineas` (`Identificador`, `fecha`, `id_cliente`) VALUES (NULL, '2025-09-25', '12');

-- insertamos lineas de pedido
INSERT INTO `lineaspedido` (`Identificador`, `producto_id`, `unidades`) VALUES (NULL, '1', '2'), (NULL, '2', '3');


Por ultimo, vamos a realizar las consultas necesarias en las tablas creadas:

SELECT 
pedidosconlineas.fecha,
clientes.nombre,
clientes.apellidos,
lineaspedido.unidades,
productos.nombre,
productos.precio,
productos.precio*lineaspedido.unidades AS Subtotal,
productos.precio*lineaspedido.unidades * 0.16 AS IVA,
productos.precio*lineaspedido.unidades * 1.16 AS Total

FROM `pedidosconlineas`

LEFT JOIN clientes 
ON pedidosconlineas.id_cliente = clientes.Identificador

LEFT JOIN lineaspedido
ON lineaspedido.pedidos_id = pedidosconlineas.Identificador

LEFT JOIN productos
ON lineaspedido.producto_id = productos.Identificador;
