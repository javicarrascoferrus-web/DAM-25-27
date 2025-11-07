Una base de datos es una colección organizada y estructurada de información o datos que se almacenan electrónicamente en un sistema informático.
En este ejercicio vamos a realizar cambios respecto a los números de teléfono y los correos electronicos.
Una vez seleccionada la tabla clientes, utilizaremos la instrucción ALTER TABLE para agregar las restricciones CHECK a las columnas.
Para seleccionar la tabla clientes:
ALTER TABLE clientes

Esta restricción asegura que el campo telefono contenga exactamente 9 dígitos numéricos y nada más:
ADD CONSTRAINT chk_telefono_9digitos

Ahora, teclearemos lo mismo pero para los emails:
ADD CONSTRAINT chk_email_formato


Intentaremos insertar un cliente con un número de teléfono que tiene solo 8 dígitos .
La inserción fallará. El Sistema de Gestión de Bases de Datos rechazará la operación y devolverá un error:
ERROR 3819 (HY000): Check constraint 'chk_telefono_9digitos' is violated.


La restricción CHECK ha cumplido su propósito al garantizar que la regla de negocio (9 dígitos exactos) se aplique a nivel de la base de datos, impidiendo la entrada de datos corruptos.

De otra forma, intentaremos insertar un cliente con un correo que no tiene una extensión de dominio válida (le falta el .com, .es, etc.), violando la restricción chk_email_formato

La inserción también fallará, mostrando el siguiente error:
ERROR 3819 (HY000): Check constraint 'chk_email_formato' is violated.


Hemos completado la implementación y prueba de las restricciones CHECK, reforzando un concepto crucial de la unidad: la Integridad de Datos.
La capacidad de la base de datos para rechazar activamente datos incorrectos no solo simplifica el código de la aplicación, sino que proporciona una capa de seguridad fundamental que mantiene nuestro sistema funcionando con información confiable y coherente.
