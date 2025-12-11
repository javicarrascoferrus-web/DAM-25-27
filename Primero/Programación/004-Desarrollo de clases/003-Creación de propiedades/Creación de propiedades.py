En la programación orientada a objetos, las clases permiten representar elementos del mundo real mediante propiedades (características) y métodos (acciones).
En este ejercicio se define una clase llamada Gato, que modela las características básicas de un gato.

Defino la clase Gato con un constructor __init__() que recibe los parámetros: color, edad, raza, nombre y color_ojos.

Todas las propiedades son públicas, es decir, se pueden acceder directamente desde fuera de la clase.

Dentro de la clase, creo un método llamado maulla() que imprime la palabra "miau", simulando el sonido del gato.


**Código**:


class Gato:
    def __init__(self, color, edad, raza, nombre, color_ojos):
        self.color = color
        self.edad = edad
        self.raza = raza
        self.nombre = nombre
        self.color_ojos = color_ojos

    def maulla(self):
        print("miau")


Con este ejercicio he aprendido a crear una clase con propiedades públicas y métodos en Python, y a generar objetos a partir de ella.
Este tipo de estructura es fundamental para representar elementos reales dentro de un programa.
