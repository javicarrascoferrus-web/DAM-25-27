EEn Python, los bucles for se utilizan para repetir una acción un número determinado de veces.
En este ejercicio, voy a generar diferentes bucles for que simulan el paso del tiempo: primero los días de un mes, luego los meses de un año y, por último, los años dentro de un rango.

Para empezar, se crea un bucle for que va del 1 al 31, representando los días de un mes.
Después, se añade un segundo bucle for anidado que recorre los meses del año, del 1 al 12.
Finalmente, se agrega un tercer bucle for que recorre los años desde 1978 hasta 2026, mostrando un mensaje completo con día, mes y año.


**Código**:


#### Primer bucle: días del mes

for dia in range(1, 32):
    print("Hoy es el día", dia, "del mes")

print("\n--- Segundo bucle: días y meses ---\n")



#### Segundo bucle: días y meses
for mes in range(1, 13):
    for dia in range(1, 32):
        print("Hoy es el día", dia, "del mes", mes)

print("\n--- Tercer bucle: días, meses y años ---\n")



#### Tercer bucle: días, meses y años
for año in range(1978, 2027):
    for mes in range(1, 13):
        for dia in range(1, 32):
            print("Hoy es el día", dia, "del mes", mes, "del año", año)


Este ejercicio me ha servido para practicar los bucles for anidados en Python y entender cómo se puede recorrer un conjunto de datos que dependen unos de otros, como días, meses y años.
