En clase vimos que ciertas operaciones “revientan” con errores típicos (por ejemplo, división por cero, tipos no válidos, o conversiones fallidas). La idea de esta práctica es partir de una función que falla, identificar por qué falla y luego robustecerla con try/except para capturar casos y responder de forma controlada, en lugar de que el programa se caiga.

Yo voy a usar un ejemplo muy común: una mini “calculadora” que recibe dos operandos y una operación ("suma", "resta", "multiplicacion", "division"). Primero mostraré la versión frágil (que lanza errores), y después la versión protegida con manejo extensivo de excepciones.

Versión frágil (provoca errores)

Problemas que aparecen:

Si paso 'a' en lugar de 2, hay ValueError al convertir.

Si hago división con 0, aparece ZeroDivisionError.

Si paso None o una operación desconocida, puedo tener TypeError o lógicas incorrectas.

A continuación tecleamos el siguiente código:


def calc_fragil(op1, op2, operacion):

    op1 = float(op1)     # ValueError si no es convertible
    op2 = float(op2)     # ValueError si no es convertible

    if operacion == "suma":
        return op1 + op2
    elif operacion == "resta":
        return op1 - op2
    elif operacion == "multiplicacion":
        return op1 * op2
    elif operacion == "division":
        return op1 / op2  # ZeroDivisionError si op2 == 0
    else:
        # operación desconocida: devuelve algo incorrecto o None
        return None


Empecé con una función “ingenua” que fallaba ante entradas reales
Este patrón es justo lo que vimos en la unidad: anticipar errores habituales, encapsular validaciones y manejar excepciones para que la aplicación sea robusta y mantenible.
