En programación, las aserciones son una herramienta muy útil para detectar errores antes de que el programa avance.
Una aserción es una instrucción que evalúa una condición lógica y, si no se cumple, lanza un error automáticamente, deteniendo la ejecución.

La función se llamará dividir y recibirá dos parámetros: num1 y num2.
Antes de realizar la operación de división, se usará una aserción (assert) para comprobar que el divisor (num2) no sea cero.


**Código**:



def dividir(num1, num2):

    (Aserción para comprobar que el divisor no sea cero): 
		
    assert num2 != 0, "Error: División por cero"
    return num1 / num2



Una vez ejecutamos esto escrito, el resultado será:
5.0
3.0

Pero cuando se intenta dividir entre cero, el programa se detiene y muestra el siguiente mensaje de error:

AssertionError: Error: División por cero


Este ejercicio me ha hecho entender cómo usar aserciones (assert) para controlar errores antes de que ocurran.
