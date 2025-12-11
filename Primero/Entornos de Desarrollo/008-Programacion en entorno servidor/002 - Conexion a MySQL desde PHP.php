
-Conectarse a una base de datos MySQL.
-Listar automáticamente las tablas que hay en esa base de datos mediante botones.
-Dar un mínimo de estilo al menú con CSS.
-Mostrar el contenido de una tabla formateado de forma más “presentable”

Conectar a la base de datos – 001-conecto a la base de datos.php

Lo primero es la conexión a MySQL. Aquí lo hago con mysqli orientado a objetos, que es sencillo.

<?php
#001-conecto a la base de datos.php

$servidor   = "localhost";       
$usuario    = "mi_usuario";       
$contrasena = "mi_contrasena";   
$basedatos  = "mi_base_de_datos"; 

$conexion = new mysqli($servidor, $usuario, $contrasena, $basedatos);

# Comprobamos si hay errores de conexión
if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}
# Opcional pero recomendable: poner charset en UTF-8
$conexion->set_charset("utf8");
?>



-SHOW TABLES devuelve un listado de todas las tablas de la base de datos actual.
-$fila[0] contiene el nombre de la tabla.
-Cada botón se envía a 002-formateo algo mejor.php con el nombre de la tabla en el parámetro GET tabla.


**Codigo**:

<?php

require_once "001-conecto a la base de datos.php";

$sql = "SHOW TABLES";
$resultado = $conexion->query($sql);

if (!$resultado) {
    die("Error al obtener las tablas: " . $conexion->error);



A continuacion, para que la tabla no quede muy sosa y simple, le añadimos algo de personalización con CSS:
Se centra el contenido del menú con text-align: center.
Se da un color de fondo al body y otro a los botones.
Se ponen márgenes y paddings para que no quede todo pegado y feo.


<?php
// 007-un poco de estilo para el menu.php
header("Content-type: text/css");
?>

body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
    margin: 0;
    padding: 0;
}

.menu-tablas {
    text-align: center;
    margin-top: 50px;
}

.menu-tablas h1 {
    margin-bottom: 30px;
}

.form-tabla {
    display: inline-block;
    margin: 10px;
}

.form-tabla button {
    padding: 10px 20px;
    border: none;
    background-color: #3498db;
    color: #fff;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
}

.form-tabla button:hover {
    background-color: #2980b9;
}


Con estos archivos ya tenemos un mini sistema que:
Se conecta a MySQL (001-conecto a la base de datos.php)
Muestra un menú con las tablas (006-pongo los botones.php)
Aplica un estilo básico al menú (007-un poco de estilo para el menu.php)
Muestra los datos de cada tabla en una tabla HTML bonita (002-formateo algo mejor.php)
