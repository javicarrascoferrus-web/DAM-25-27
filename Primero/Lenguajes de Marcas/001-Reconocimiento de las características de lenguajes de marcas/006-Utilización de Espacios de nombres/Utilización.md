En el editor de texto, vamos a teclear código en el cual vamos a añadir una nueva etiqueta llamada <nat>
	En este documento XML, llamado "competidores.xml" vamos a describir el nombre de los mismos.
	Para ellos vamos a empezar el documento atribuyendole la version y codificación tecleando el siguiente comando para empezar:
	<?xml version="1.0" encoding="UTF-8"?>
	
	a continuación, con la utilización de la etiqueta <nat> vamos a describir a los nadadores competidores:
	<competidores>
	<nat:competidor>
  <nat:nombre id="propio">Javier</nat:nombre>
  <nat:edad medida="años">28</nat:edad>
  <nat:nacionalidad>Española</nat:nacionalidad>
</nat:competidor>

<nat:competidor>
  <nat:nombre id="propio">Miriam</nat:nombre>
  <nat:edad medida="años">23</nat:edad>
  <nat:nacionalidad>Japonesa</nat:nacionalidad>
</nat:competidor>
	
	<nat:competidor>
  <nat:nombre id="propio">Eusebio</nat:nombre>
  <nat:edad medida="años">29</nat:edad>
  <nat:nacionalidad> Inglesa</nat:nacionalidad>
</nat:competidor>
	</competidores>
	Aquí demostramos como la etiqueta <nat> describe la información de cada competidor, en la cual dentro de la misma se puede visualizar el nombre, el año y la nacionalidad de cada competidor.
	
	Una vez hemos añadido y descrito a los competidores correpondientes, cerraremos la etiqueta </nat> y a su vez la etiqueta </competidores>
	Ésta última se utiliza para agrupar la información de todos ellos.
