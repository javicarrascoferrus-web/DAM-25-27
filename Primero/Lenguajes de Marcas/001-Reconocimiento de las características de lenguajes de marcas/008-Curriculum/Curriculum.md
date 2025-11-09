En este ejercicio, el objetivo es organizar información personal en formato JSON, que es un tipo de estructura de datos muy común para intercambiar información entre aplicaciones.
José Vicente quiere tener sus datos personales bien ordenados en una sola variable llamada datosPersonales.
El formato JSON nos permite representar los datos de forma limpia, estructurada y legible, usando pares clave–valor dentro de llaves.

Para crear un objeto JSON en Python, usamos una estructura tipo diccionario, donde cada campo tiene su nombre (clave) y su valor.
Los campos que se deben incluir son:

nombre

apellidos

email

telefono

fotografia

**Aquí está el código completo y funcional:**


datosPersonales = {
    "nombre": "Jose Vicente",
    "apellidos": "Carratalá Sanchis",
    "email": "info@josevicentecarratala.com",
    "telefono": "620891718",
    "fotografia": "josevicentecarratala.jpg"
}


print(datosPersonales)



Con este ejercicio aprendí a representar información personal en un formato JSON usando Python, entendiendo cómo se estructuran los datos con pares clave–valor.
Esta práctica está relacionada con los contenidos de la unidad sobre estructuras de datos y almacenamiento, ya que el formato JSON es una forma muy usada para guardar o enviar información en páginas web.
