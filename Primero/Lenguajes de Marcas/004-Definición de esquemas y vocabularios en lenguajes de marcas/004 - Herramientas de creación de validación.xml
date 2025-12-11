En esta práctica estamos mezclando varias piezas que ya han ido saliendo en la unidad:
XSD → define la “plantilla” de cómo tiene que ser un XML.
XML → guarda los datos reales (en este caso, de una persona).
Python → lo usamos como “pegamento” para leer el XSD, preguntarle datos al usuario y generar el XML final.

Voy a plantear un único script “completo” que junta la idea de:
001-generador esquema.py (leer el XSD y sacar los campos de <persona>),
003-guardar xml.py (pedir valores y guardar el XML bonito).
Lo haré con lxml, que es lo típico que se usa cuando se quiere algo cómodo para XML/XSD.
	
Cargar el XSD y encontrar el elemento <persona>
Suponiendo que el XSD se llama 002-plantilla.xsd.
	
El código en Python para cargarlo y extraer la definición de <persona> sería algo así:
	
	from lxml import etree

XS = "{http://www.w3.org/2001/XMLSchema}"

xsd_file = "002-plantilla.xsd"
	
	
#Pedimos los valores de los elementos
valores_elementos = {}
print("Introduce los datos de la persona:\n")
	
	for campo in campos:
    nombre_campo = campo.get("name")
    tipo_campo = campo.get("type") 
    valor = input(f"- {nombre_campo} ({tipo_campo}): ")
    valores_elementos[nombre_campo] = valor
	
Por último, creamos el árbol y lo guardamos en un archivo, por ejemplo:
	
# Creamos el árbol y lo guardamos
xml_tree = etree.ElementTree(persona_xml)

nombre_salida = "persona_generada.xml"
xml_tree.write(
    nombre_salida,
    encoding="utf-8",
    xml_declaration=True,
    pretty_print=True 
)

print(f"\nXML generado y guardado en '{nombre_salida}'.")
	
	
	
Al terminar este ejercicio terminamos con entender que el XSD no es solo “documentación”, sino que se puede leer desde código para saber qué campos tiene que tener un XML.

Automatizar la creación de XML de instancia a partir de los datos que introduce un usuario.

Ver cómo Python y lxml permiten trabajar de forma cómoda con esquemas y documentos XML.
