En una base de datos relacional, una vista sirve para mostrar datos combinados de varias tablas sin tener que escribir la misma consulta cada vez. Es como una “ventana” a la información.
En este caso, quiero crear una vista que muestre los pedidos de los clientes que tienen como hobby la natación, incluyendo datos del cliente, del producto y del pedido.

Voy a usar tres tablas:

clientes → tiene el nombre, apellidos y hobby del cliente.

productos → guarda el nombre, precio e IVA del producto.

pedidos → relaciona los clientes con los productos comprados y la fecha del pedido

Para eso, se unen las tablas por sus claves:

pedidos.id_cliente = clientes.id_cliente

pedidos.id_producto = productos.id_producto


Para ver todo esto, se teclea el siguiente comando SQL:

CREATE VIEW vw_pedidos_natacion AS
SELECT
  p.fecha AS fecha_pedido,
  c.nombre AS nombre_cliente,
  c.apellidos AS apellidos_cliente,
  pr.nombre AS producto,
  pr.precio AS precio,
  pr.iva AS iva,
  ROUND(pr.precio * (1 + pr.iva), 2) AS total
FROM pedidos p
JOIN clientes c ON c.id_cliente = p.id_cliente
JOIN productos pr ON pr.id_producto = p.id_producto
WHERE c.hobby = 'Natación';

Con esta vista podemos ver fácilmente los pedidos de los clientes que practican natación sin tener que escribir toda la consulta cada vez.
Usar vistas hace que el trabajo con bases de datos sea más ordenado y claro
