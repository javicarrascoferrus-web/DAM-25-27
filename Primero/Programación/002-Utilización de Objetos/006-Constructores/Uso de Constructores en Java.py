En este ejercicio voy a crear una clase llamada Libro, que tendrá tres atributos principales: el título, el autor y el número de páginas.
Este ejercicio hago entender cómo funcionan los constructores, los métodos de acceso (getters y setters) y el método __str__() en Python.

Primero defino la clase Libro con sus tres atributos: titulo, autor y paginas

Después añado los métodos getter y setter para poder acceder y modificar cada atributo de forma controlada.
Después implemento el método especial __str__(), que sirve para devolver una descripción legible del objeto en forma de texto.


**Código:**

class Libro:

    def __init__(self, titulo="Desconocido", autor="Desconocido", paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


A continuación los metodos **getter y setter:**



**Getter**:
def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_paginas(self):
        return self.paginas]
				
				
				
				
**Setter**:
				
 def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor

    def set_paginas(self, nuevas_paginas):
        self.paginas = nuevas_paginas
				
				
				
**Método __str__ para mostrar los datos del libro**

 def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"
				
				
				
En este ejercicio he aprendido a crear una clase en Python con atributos, constructores, getters, setters y un método especial __str__().
He comprobado cómo se pueden crear objetos distintos a partir de la misma clase, con o sin valores iniciales.
