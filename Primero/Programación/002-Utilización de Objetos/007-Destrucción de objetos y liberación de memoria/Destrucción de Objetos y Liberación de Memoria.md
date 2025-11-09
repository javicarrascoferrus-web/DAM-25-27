En programación, cada vez que se crea un objeto en memoria, el sistema reserva un espacio para guardar su información. Sin embargo, cuando ese objeto ya no se necesita, es importante liberar la memoria que estaba usando.

En Python, la liberación de memoria se gestiona de forma automática gracias al recolector de basura (garbage collector). Aun así, también podemos eliminar objetos manualmente con la instrucción del, que destruye una variable y libera su espacio de memoria.


A continuación, muestro un ejemplo sencillo usando solo objetos:



#### Creamos un objeto (una lista con varios valores)
numeros = [1, 2, 3, 4, 5]
print("Lista original:", numeros)



#### Usamos el objeto
suma = sum(numeros)
print("La suma de los números es:", suma)



#### Eliminamos el objeto para liberar memoria
del    numeros


Liberar la memoria después de usar un objeto es una parte esencial de la programación, ya que permite mantener el rendimiento del sistema y evitar errores por consumo excesivo de recursos.

En este ejercicio he aprendido que en Python esto se gestiona de forma automática, aunque también se puede hacer manualmente con del cuando se necesita más control.
