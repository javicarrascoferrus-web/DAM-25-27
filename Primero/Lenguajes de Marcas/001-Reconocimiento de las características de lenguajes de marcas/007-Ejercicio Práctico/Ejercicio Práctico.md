Un archivo XML es un tipo de archivo de texto que se utiliza para almacenar y transportar datos de manera estructurada y legible tanto por humanos como por máquinas.
En el lenguaje de marcas significa que utiliza etiquetas para describir la estructura y el significado de los datos que contiene.

En el ejercicio 002-telefono.xml vemos que dentro de la etiqueta <persona> se ha descrito a una persona que le atribuye la siguiente información:
1.  	Nombre
2.  	Apellidos
3.  	Telefono
4.   	Correo electrónico

	En este documento, podemos atribuir información de la persona, ya que está dentro de la etiqueta <persona>
	Pero si quisieramos atribur otra informacion, tan solo tendriamos que añadir la etiqueta correspondiente. Por ejemplo:
	Para añadir un nuevo registro respecto un libro;
	
	<?xml version="1.0" encoding="UTF-8"?>
<lista_libros>
   <libro> <titulo>Don Quijote de la Mancha</titulo>
    <autor>Miguel de Cervantes</autor>
    <año>1605</año>
  </libro>
</lista_libros>
	
	
	En resumen, la edición de XML no es solo escribir texto, se trata de manipular los elementos y sus contenidos para reflejar con precisión los cambios en la estructura o en los valores de los datos.
