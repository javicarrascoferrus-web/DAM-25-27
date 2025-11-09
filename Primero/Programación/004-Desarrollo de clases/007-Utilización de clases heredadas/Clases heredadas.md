En la programación orientada a objetos, la herencia permite crear nuevas clases basadas en otras ya existentes, compartiendo atributos y métodos.
Este concepto es muy útil cuando varios objetos comparten características comunes, como ocurre con los animales, que pueden tener color, edad o comportamientos similares.

Se define la clase Animal con los atributos color y edad.

Se añade un constructor (__init__) que inicializa estos valores.

Se crean los métodos de acceso setEdad() y getEdad() para modificar y consultar la edad.

Se implementa el método descripcion(), que devuelve una cadena con la información del animal.


**Código**


class Animal:
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def descripcion(self):
        return f"Color: {self.color}, Edad: {self.edad} años"

class Gato(Animal):
    def __init__(self, color, edad, nombre):
        super().__init__(color, edad)
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, color, edad, nombre):
        super().__init__(color, edad)
        self.nombre = nombre

#### Crear instancias

gato1 = Gato("blanco", 2, "Luna")
perro1 = Perro("marrón", 4, "Rocky")



#### Mostrar información

print("Gato:", gato1.nombre, "-", gato1.descripcion())
print("Perro:", perro1.nombre, "-", perro1.descripcion())



#### Modificar edad
gato1.setEdad(3)
print("\nNueva edad del gato:", gato1.getEdad(), "años")



Con este ejercicio he aprendido cómo crear una clase base y cómo hacer que otras clases hereden sus propiedades y métodos.
También he comprobado que super().__init__() permite inicializar los atributos heredados sin tener que repetir código
