GET:

Los datos viajan por la URL.

Se usan para consultas, búsquedas, cosas no sensibles.

Se reciben con $_GET.

Ejemplo de URL:
pagina.php?nombre=Javier&edad=20

PHP:

$nombre = $_GET["nombre"];
$edad = $_GET["edad"];
echo $nombre;


POST:

Los datos no aparecen en la URL.

Se usan para formularios, contraseñas, registros, etc.

Se reciben con $_POST.



PHP (procesar.php):

$usuario = $_POST["usuario"];

echo $usuario;
