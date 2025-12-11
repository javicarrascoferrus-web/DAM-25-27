Gestionar el tiempo es clave para aprender mejor. Cuando tenemos un hobby en mi caso, la natación es más fácil mantener la constancia porque disfrutamos del proceso.

Propiedades privadas (con name mangling __atributo) 

Constructor para iniciar el objeto con un hobby y un objetivo.

Métodos para registrar tiempo, consultar y modificar el objetivo, y generar un resumen.

**Código**:



apr = Aprendizaje(hobby="Natación", objetivo_horas=10)

#### Registro de sesiones (minutos)

apr.registrar_sesion(45)    (día 1)
apr.registrar_sesion(60)    (día 2)
apr.registrar_sesion(30)    (día 3)



print(apr.resumen())                  (ver estado general)
print("Hobby actual:", apr.hobby)     (acceder propiedad (getter))
print("Tiempo total (h):", apr.tiempo_total_horas)
print("Progreso (%):", apr.progreso())



#### Cambio de objetivo y nuevo resumen


apr.objetivo_horas = 8                (usar setter para ajustar objetivo)
print("Nuevo objetivo (h):", apr.objetivo_horas)
print(apr.resumen())



Con este ejercicio he practicado el diseño de una clase con propiedades privadas, constructor y métodos, además de @property para un acceso controlado.
