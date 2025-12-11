Una copia de seguridad de una base de datos sirve para poder restaurar la información si hay un fallo, borrado accidental o migración. 

En MySQL, la utilidad clásica para esto es mysqldump, que genera un fichero .sql con las sentencias necesarias para volver a crear la estructura y los datos.

La conexión desde python se hace de la siguiente manera:

**Driver:** mysql-connector-python.

**Conexión:** mysql.connector.connect(host, port, user, password, database).

**Cursor:** objeto para ejecutar sentencias SQL con parámetros (evitar inyecciones).

**Transacción:** llamadas de escritura requieren commit().

Esto enlaza con otros contenidos de la unidad como transacciones, modelo relacional, tipos de datos y buenas prácticas de seguridad.
