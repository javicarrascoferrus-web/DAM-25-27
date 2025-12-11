En Python, las funciones permiten agrupar instrucciones que realizan una tarea específica, facilitando la organización y reutilización del código.
En este ejercicio, el objetivo es crear una función llamada creaDivision que realice una división entre dos números, controlando los posibles errores que puedan surgir.

Se define la función creaDivision que recibe dos parámetros: dividendo y divisor.

Se utiliza un bloque try-except para manejar errores comunes, como dividir entre cero o pasar valores no numéricos.


**Código**:

def creaDivision(dividendo, divisor):

    """
    Función que realiza la división entre dos números.
    Parámetros:
        dividendo (float/int): número que se va a dividir.
        divisor (float/int): número por el cual se divide.
    Retorna:
        float: resultado de la división si es válida.
        str: mensaje de error si ocurre una excepción.
				
				
    """
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        return "infinidad"
    except TypeError:
        return "Error: valores no válidos"



Este ejercicio me ha servido para practicar la creación de funciones con manejo de errores y la documentación mediante docstrings.
He aprendido que usar bloques try-except permite anticipar problemas y evitar que el programa se detenga inesperadamente
