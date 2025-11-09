En la programación orientada a objetos, las clases son la base para crear estructuras que representan objetos del mundo real.
Un ejemplo claro son los animales domésticos, como los perros, que pueden describirse mediante sus características.

Definición de la clase: se crea la clase Perro usando la palabra clave class.

Constructor básico: se define el método __init__ que no recibe parámetros (además de self) y asigna valores por defecto a las propiedades


**Código:**



class Perro:

   #### Constructor básico con valores por defecto 
		
    def __init__(self, color="Marrón", edad=0, raza="Desconocida", nombre="Sin nombre"):
        self.color = color
        self.edad = edad
        self.raza = raza
        self.nombre = nombre
				

   #### Método getter para obtener la edad
    def get_edad(self):
        return self.edad
				

  ####  Método setter para modificar la edad
    def set_edad(self, nueva_edad):
        self.edad = nueva_edad



Con este ejercicio he practicado cómo crear clases con constructores y métodos de acceso, una base esencial en la programación orientada a objetos.
