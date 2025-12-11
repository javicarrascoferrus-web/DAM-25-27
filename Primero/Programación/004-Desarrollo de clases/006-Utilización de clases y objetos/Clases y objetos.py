En programación, las clases y los objetos permiten representar entidades del mundo real dentro de un programa.
En este caso, voy a crear una clase llamada Cliente para simular el registro de datos de un cliente, como su nombre, correo electrónico y dirección.

Definición de la clase Cliente:
Se crea la clase con un constructor __init__ que recibe tres parámetros: nuevonombre, nuevoemail y nuevadireccion.

Entrada de datos con input():
Se piden los tres datos al usuario y se guardan en variables.

Creación de la instancia:
Se crea un objeto cliente1 usando los valores introducidos.

Recorrido del objeto:
Con un bucle for, se recorren las claves del objeto mediante el método __dict__



**Código**:



class Cliente:
    def __init__(self, nuevonombre, nuevoemail, nuevadireccion):
        self.nombre = nuevonombre
        self.email = nuevoemail
        self.direccion = nuevadireccion

#### Pedir datos al usuario
nombre = input("Introduce el nombre del cliente: ")
email = input("Introduce el email del cliente: ")
direccion = input("Introduce la dirección del cliente: ")


#### Crear una instancia del objeto Cliente
cliente1 = Cliente(nombre, email, direccion)


#### Recorrer las claves del objeto y mostrar sus valores
print("\nDatos del cliente registrado:")
for clave, valor in cliente1.__dict__.items():
    print(clave + ":", valor)
		
		
		
Con este ejercicio he aprendido a combinar la entrada de datos por teclado con la creación de objetos y a recorrer sus propiedades usando un bucle for.
También he entendido mejor cómo los objetos en Python almacenan su información internamente en un diccionario (__dict__).
