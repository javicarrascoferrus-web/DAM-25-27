En este ejercicio se monta una mini-aplicación web muy típica con PHP + MySQL:
Crear una base de datos llamada discos con su tabla.
Un formulario HTML para insertar nuevos discos.
Un script PHP que procese ese formulario y guarde los datos.
Una página que liste todos los discos y permita eliminarlos con un botón.

Crear la base de datos y la tabla
Con el script SQL:

CREATE DATABASE IF NOT EXISTS discos
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE discos;

CREATE TABLE IF NOT EXISTS discos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    artista VARCHAR(255) NOT NULL,
    anio INT NOT NULL,
    genero VARCHAR(100) NOT NULL
);


Conexión a la base de datos:

<?php
// conexion.php

$host = "localhost";
$user = "root";
$pass = "tu_password";
$db   = "discos";

$conexion = new mysqli($host, $user, $pass, $db);

if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

$conexion->set_charset("utf8mb4");
?>


**Script PHP que inserta en la base de datos**

<?php

require_once "conexion.php";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $titulo  = trim($_POST["titulo"] ?? "");
    $artista = trim($_POST["artista"] ?? "");
    $anio    = (int)($_POST["anio"] ?? 0);
    $genero  = trim($_POST["genero"] ?? "");

    if ($titulo === "" || $artista === "" || $anio === 0 || $genero === "") {
        die("Faltan datos. <a href='insertar_disco.php'>Volver</a>");
    }


    $sql = "INSERT INTO discos (titulo, artista, anio, genero)


    $stmt = $conexion->prepare($sql);
    if (!$stmt) {
        die("Error en la preparación de la consulta: " . $conexion->error);
    }

    $stmt->bind_param("ssis", $titulo, $artista, $anio, $genero);

    if ($stmt->execute()) {
        header("Location: listar_discos.php");
        exit;
    } else {
        echo "Error al insertar el disco: " . $stmt->error;
    }

    $stmt->close();
} else {
    echo "Método no permitido.";
}

$conexion->close();
?>



**Script para eliminar discos**
<?php

require_once "conexion.php";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $id = (int)($_POST["id"] ?? 0);

    if ($id <= 0) {
        die("ID no válido. <a href='listar_discos.php'>Volver</a>");
    }

    $sql = "DELETE FROM discos WHERE id = ?";
    $stmt = $conexion->prepare($sql);

    if (!$stmt) {
        die("Error en la preparación de la consulta: " . $conexion->error);
    }

    $stmt->bind_param("i", $id);

    if ($stmt->execute()) {
        header("Location: listar_discos.php");
        exit;
    } else {
        echo "Error al eliminar el disco: " . $stmt->error;
    }

    $stmt->close();
} else {
    echo "Método no permitido.";
}

$conexion->close();
?>


Ejecutas el script SQL en MySQL para crear la base de datos discos y la tabla.
Copias todos los archivos PHP (conexion.php, insertar_disco.php, procesar_insertar.php, listar_discos.php, eliminar_disco.php) en la carpeta de tu servidor (por ejemplo htdocs/discos/ en XAMPP).


Con todo esto has montado un pequeño CRUD parcial:
Create: formulario + INSERT (insertar_disco + procesar_insertar).
Read: listado de todos los discos (listar_discos).
Delete: botón de eliminar + DELETE (eliminar_disco).
Esto se relaciona directamente con otros contenidos de la unidad:
Conexión de PHP a MySQL y uso de consultas SQL.
Manejo de formularios HTML, métodos GET/POST y variables $_POST.
Generación dinámica de HTML (la tabla de discos se construye en un while).
