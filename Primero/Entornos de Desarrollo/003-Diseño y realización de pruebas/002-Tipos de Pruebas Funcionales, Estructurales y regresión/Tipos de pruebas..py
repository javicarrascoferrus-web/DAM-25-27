En este ejercicio trabajé con el archivo operacionMatematica.py, cuyo objetivo es realizar operaciones matemáticas básicas entre dos números.
Inicialmente, la función solo permitía realizar sumas y restas, pero la práctica consiste en ampliar su funcionalidad para que también pueda realizar multiplicaciones y divisiones.

El proceso comenzó analizando el código original del archivo operacionMatematica.py.
La función recibía tres parámetros:

**operando1: primer número.**

**operando2: segundo número.**

**operacion: tipo de operación a realizar ("suma" o "resta").**

Este el código que teclee para que Python diera respuesta:
# Archivo: operacionMatematica.py

def operacionMatematica(operando1, operando2, operacion=None):
    if operacion == "suma":
        suma = operando1 + operando2
        return suma
    elif operacion == "resta":
        resta = operando1 - operando2
        return resta
    elif operacion == "multiplicacion":
        multiplicacion = operando1 * operando2
        return multiplicacion
    elif operacion == "division":
        if operando2 != 0:
            division = operando1 / operando2
            return division
        else:
            return "Error: División por cero"
    else:
        return 0



**Con resultado asi:**

ejecucion 1
3
ejecucion 2
-1
ejecucion 3
2
ejecucion 4
2.0
ejecucion 5
Error: División por cero


Con esta práctica aprendí a modificar y ampliar una función existente para que acepte nuevos casos, además de implementar control de errores (en este caso, la división entre cero).
La función ahora es más completa y flexible, y puede servir como base para una futura calculadora más compleja.
