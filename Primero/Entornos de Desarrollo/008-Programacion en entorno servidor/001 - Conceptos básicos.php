<?php

Impresión en pantalla:

echo "Hola mundo";


Variables

No se declara el tipo y siempre llevan $ delante.

PHP termina líneas con ;

$nombre = "Javier";
$edad = 20;


Arrays (listas/diccionarios):

$numeros = array(1, 2, 3);

Diccionario en PHP:

$persona = ["nombre" => "Javier", "edad" => 20];

Condiciones:

if ($edad > 18) {
    echo "Mayor";
} else {
    echo "Menor";
}


Funciones:

function sumar($a, $b) {
    return $a + $b;
}


?>
