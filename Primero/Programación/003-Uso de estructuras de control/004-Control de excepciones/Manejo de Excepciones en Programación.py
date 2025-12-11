Voy a crear una función llamada calcular_promedio que reciba la suma de las calificaciones y el número de estudiantes. Primero la haré sin control de errores, y después añadiré un bloque try-except para manejar el caso en el que el número de estudiantes sea cero.

En primer lugar, defino la función calcular_promedio con dos parámetros: suma_calificaciones y num_estudiantes.
La función divide la suma entre el número de estudiantes y devuelve el resultado.

Después, modifico la función añadiendo un bloque try-except para capturar el error en caso de que num_estudiantes sea cero.

Según las restricciones, no se puede usar if, elif ni else, por lo que todo el control se realiza dentro del try-except.


**Código**:



def calcular_promedio(suma_calificaciones, num_estudiantes):
    try:
        promedio = suma_calificaciones / num_estudiantes
        return promedio
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero. El número de estudiantes no puede ser 0."



Este ejercicio me ha servido para comprender cómo se usa el manejo de excepciones en Python mediante try y except.
