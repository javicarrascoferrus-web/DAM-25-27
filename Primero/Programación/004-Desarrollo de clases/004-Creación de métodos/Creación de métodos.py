En la programación orientada a objetos, las clases nos permiten representar cosas reales mediante atributos (características) y métodos (acciones o comportamientos).
En este ejercicio se crea una clase llamada Gato con algunas propiedades básicas como su color, edad, raza, nombre y color de ojos.

Para construir la clase Gato, se sigue esta estructura:

Definición de la clase con class.

Creación del método constructor __init__, que inicializa los atributos públicos: color, edad, raza, nombre y color_ojos.

Definición de un método llamado mostrar_color_ojos() que devuelve el color de los ojos del gato.


**Código**:


class Gato:
    def __init__(self, color, edad, raza, nombre, color_ojos):
        self.color = color
        self.edad = edad
        self.raza = raza
        self.nombre = nombre
        self.color_ojos = color_ojos

    def mostrar_color_ojos(self):
        """Devuelve el color de los ojos del gato."""
        return self.color_ojos




En este ejercicio he aprendido a definir una clase en Python, a usar su constructor y a crear métodos que devuelven información específica del objeto.
La clase Gato es un ejemplo sencillo, pero representa bien los principios de la programación orientada a objetos
