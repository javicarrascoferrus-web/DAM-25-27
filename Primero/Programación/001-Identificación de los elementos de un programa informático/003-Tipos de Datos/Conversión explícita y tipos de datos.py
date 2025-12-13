Las variables en programación son espacios de almacenamiento a los que se les asigna un nombre, un datos o  un valor.

Vamos a declarar las variables de (edad) y (nados), asegurándonos de usar el tipo de dato correcto para cada una.

Variable 'edad' como una CADENA de texto (String) 

El valor se envuelve en comillas para indicar que es texto, no un número.
edad = "28"

Después de declarar las variables, el siguiente paso crucial es verificar su tipo de dato. Esto nos confirma como el programa interpretará la información que contienen.

edad	print(type(edad))
nados	print(type(nados))


Vamos a aplicar las operaciones básicas de concatenación y multiplicación, que son fundamentales para trabajar con texto.

nombre = "Alex"
frase = " ha nadado"

**Concatenación: nombre + frase**
resultado_concatenacion = nombre + frase

print(resultado_concatenacion)

Cuando ejecutemos este comando, saldrá tal como asi: "Alex ha nadado"

La multiplicación de una cadena por un número entero repite la cadena ese número de veces:
saludo = "¡Hola!"

**Multiplicación: saludo * 2**
resultado_multiplicacion = saludo * 2

print(resultado_multiplicacion)

Cuando ejecutemos este código, en pantalla saldrá: ¡Hola!¡Hola!

Ahora que tenemos la variable edad almacenada como una cadena de texto ("30"), vamos a realizar una conversión explícita de tipo:

edad = "30" # La variable original (String)

**Conversión: int("30") > 30**
edad_entero = int(edad)

print("El valor de edad_entero es: {edad_entero}")

Vamos a multiplicar la variable edad_entero (que ahora contiene el número 30) por 2 y mostrar el resultado:

edad_entero = 30 # Asumiendo la conversión anterior

Multiplicamos e imprimimos el resultado directamente
print(edad_entero * 2)

En este esquema he aprendido a definir variables, a declarar una variable, a verficar un tipo de dato, a operar y convertir un texto.
 Todo ello necesario y útil para la información de un programa.
