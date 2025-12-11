En este ejercicio estamos dando un paso más con XML, pero ahora entra en juego un compañero nuevo: el XSD (XML Schema Definition).
El XML es el documento con los datos.
El XSD es el “contrato” o “plantilla” que dice cómo tiene que ser ese XML:
qué elemento raíz debe tener,
qué etiquetas hijas son obligatorias,
qué tipos de datos lleva cada una (cadena, número, fecha…),

Voy a crear un documento con información de natación, en el que va a llevar: 
El elemento raíz, que se llama <entrenamiento>.
Dentro lleva, en este orden, los elementos:
<nadador> (texto)
<estilo> (texto)
<metros> (entero)
<tiempo> (texto, por ejemplo "00:45.23").
	
	Ejemplo:
	
<?xml version="1.0" encoding="UTF-8"?>
<entrenamiento fecha="2025-05-10">
  <nadador>Javier Carrasco</nadador>
  <estilo>Crol</estilo>
  <metros>1500</metros>
  <tiempo>00:32:45</tiempo>
</entrenamiento>

	
	El elemento raíz es exactamente <entrenamiento>.
El atributo fecha está presente y con un formato tipo YYYY-MM-DD.
El orden de los hijos respeta el XSD:
<nadador>
<estilo>
<metros>
<tiempo>
	
	

En este ejercicio he visto cómo:

El XSD actúa como una “plantilla estricta” que define la forma correcta de un documento XML.

A partir de 002-plantilla.xsd hemos creado un XML (nuevo-documento.xml) ajustándonos a los elementos, atributos y tipos de datos que marca el esquema.

Usando un script en Python (005-validar de nuevo.py) hemos comprobado si nuestro XML es válido
