Un menú CRUD es una estructura que se usa mucho en programación para manejar datos. Cada opción permite crear, leer, actualizar o eliminar información.
En este caso, vamos a hacer un programa en Python que muestre un menú con estas opciones, pida al usuario que elija una y después muestre por pantalla cuál ha elegido

**Create**: crear nuevos datos.

**Read:** leer o mostrar datos existentes.

**Update:** modificar datos.

**Delete:** eliminar datos



#### **Para hacer el programa se usan principalmente dos funciones de Python:**

**print()** para mostrar mensajes en pantalla.

**input()** para pedir datos al usuario.




## **Para resolver el ejercicio, seguimos estos pasos:**

Imprimir un mensaje de bienvenida con print().

Mostrar un menú de opciones CRUD usando varios print() seguidos.

Pedir una opción al usuario mediante la función input(), que captura texto desde el teclado.

Mostrar la opción elegida con otro print().




Voy a escribir un código breve para mostrar cada una de las opciones:




### 1. Mensaje de bienvenida:

print("Bienvenido al programa de gestión CRUD")



### 2. Mostrar menú de opciones:

print("\nPor favor, selecciona una opción:")
print("1. Crear (Create)")
print("2. Leer (Read)")
print("3. Actualizar (Update)")
print("4. Eliminar (Delete)")



### 3. Recibir la opción del usuario

opcion = input("\nIntroduce el número de la opción deseada: ")



### 4. Mostrar la opción escogida
print(f"\nHas elegido la opción: {opcion}")



Este ejercicio muestra cómo crear un menú simple en Python usando print() e input(). Es una base para hacer programas más completos, donde cada opción ejecute una función diferente.
