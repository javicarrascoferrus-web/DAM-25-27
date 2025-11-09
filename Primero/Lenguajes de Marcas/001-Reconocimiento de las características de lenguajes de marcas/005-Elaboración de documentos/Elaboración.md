En este archivo de texto, vamos a crear una etiqueta llamada "<persona>" en la que vamos a describir cosas de esa persona.
	Para ellos abrimos nuestro editor de texto, llamado Gedit y escribimos lo siguiente:
	
	Al principio del documento tenemos que edeclarar la version y tipo de codificación que debe de tener el documento, asi que tecleamos lo siguiente:
	
	<?xml version="1.0" encoding="UTF-8"?>
	
	Después, añadiremos la etiqueta <personas> para describir
	
	Dentro de la etiqueta <personas> habrá una sub-etiqueta que diga <persona>  en la que se describirá una persona en concreto
	
	El código deberá estar tal como así:
	<!doctype html>
	<html>
		<head>
		</head>
			<body>
				<personas>
						<persona>
							<persona xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:noNamespaceSchemaLocation="006-validar xml.xsd">
								
								<nombre id="propio">Javier <nombre>
								<nombre id="mote">JC</nombre>
								<edad medida="años">28</edad>
								<profesion>Nadador</profesion>
							
						</persona>
				</personas>
		
			</body>
	</html>
	
					Una vez escrito este codigo, debemos fijarnos que hemos descrito a una persona en el que se describe su edad, su nombre y su profesión.
					Al igual que hemos descrito una persona, también podemos describir a tantas personas como queramos, siempre y cuando se abra la etiqueta <persona> y se cierre </persona>
