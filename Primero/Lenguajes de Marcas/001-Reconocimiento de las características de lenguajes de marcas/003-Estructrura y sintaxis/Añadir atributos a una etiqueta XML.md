En este ejercicio vamos a practicar las etiquetas en formato XML para guardar información adicional.
Por ejemplo, si una etiqueta informa del nombre, en ella mismo vamos a poner otra etiqueta que añada la edad de esa misma persona que se describe.
Para ellos vamos a teclear el siguiente cçodigo:

<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre id="propio">Javier</nombre>
  <nombre id="mote">JC</nombre>
  <edad medida="años">28</edad>
  <profesion>Nadador</profesion>
</persona>

Este es un código con etiquetas XML, pero sin añadirle lo que nos pide el enunciado, para ello, vamos a añadir la etiiqueta "edad" para que se sepa. Quedaría tal que así:

<persona>
  <nombre id="propio" edad="28">Javier</nombre>
  <nombre id="mote">JC</nombre>
  <profesion>Nadador</profesion>
</persona>

Aquí eliminamos la etiqueta:  " <edad medida="años">28</edad> " porque esta información ya la hemos puesto dentro de la etiqueta "nombre"

Como consejo, también es importante añadir que;  el orden de los atributos dentro de una etiqueta no importa. Esto significa que <nombre id="propio" edad="28"> es funcionalmente idéntico a <nombre edad="28" id="propio">
	
	Para terminar, guardamos el archivo en .html para que podamos visualizarlo correctamente en el navegador
