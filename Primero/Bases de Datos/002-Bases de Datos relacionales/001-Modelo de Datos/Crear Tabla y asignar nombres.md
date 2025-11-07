CREATE TABLE Clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    apellidos VARCHAR(50),
    telefono VARCHAR(15),
    email VARCHAR(100)
);
CREATE TABLE Productos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    descripcion TEXT,
    precio DECIMAL(10, 2),
    tamaño VARCHAR(20),
    peso DECIMAL(10, 2)
);
CREATE TABLE Pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE,
    numero_pedido VARCHAR(20),
    Cliente_id INT,
    Productos_id INT,
    impuestos DECIMAL(10, 2),
    total DECIMAL(10, 2),
    FOREIGN KEY (Cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (Productos_id) REFERENCES Productos(id)
);
