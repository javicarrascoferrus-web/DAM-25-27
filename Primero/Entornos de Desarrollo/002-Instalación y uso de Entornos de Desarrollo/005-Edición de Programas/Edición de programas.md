En esta práctica he trabajado con GitHub Copilot dentro de Visual Studio Code, un asistente de inteligencia artificial que ayuda a escribir código más rápido y entender estructuras comunes de programación.
El objetivo de esta actividad fue practicar iteraciones (con for) y estructuras condicionales (con if-else) utilizando Copilot para generar sugerencias automáticas.

**Parte 1: Iteración diaria con Copilot**

Abrí Visual Studio Code y creé un nuevo archivo llamado dias_mes.py.

Activé GitHub Copilot (ya instalado como extensión).

Escribí el comentario:
Imprimir los días del 1 al 31

Acto seguido obtuve el siguiente código:
for dia in range(1, 32):
    print("Día", dia)

Ejecuté el código y el resultado fue una lista numerada del 1 al 31, que representa los días de un mes.


**Parte 2: Condición de edad con Copilot**

Creé otro archivo llamado edad_persona.py.

Escribí el comentario:
Verificar si una persona es mayor de edad

Copilot propuso automáticamente:

edad = 22

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


Ejecuté el código en la terminal integrada y el resultado fue:
Eres mayor de edad.

Copilot no solo completó la estructura if-else, sino que también usó nombres de variables adecuados y una condición lógica coherente (edad >= 18).


Con esta práctica aprendí a usar GitHub Copilot como apoyo en la escritura de código, especialmente para estructuras básicas como bucles y condiciones.
La herramienta no solo acelera la escritura, sino que también me permite entender la lógica detrás de las sugerencias.
