En administración de bases de datos, cada acción que modifica o elimina información debe ir precedida de una copia de seguridad fiable. Hoy vas a crear un backup de la base de datos empresarial, ejecutar un script que elimina registros de la tabla clientes, y modificar un registro concreto con UPDATE.

**mysqldump** es la utilidad de línea de comandos de MySQL para volcar la estructura y los datos de una o varias bases de datos a un archivo de texto SQL.


**DELETE FROM** <tabla> borra filas. Sin **WHERE**, borra todas las filas de la tabla (no la estructura).
	
**UPDATE** cambia valores de columnas en filas que cumplan una condición. 
La cláusula WHERE es crucial para acotar la modificación a las filas correctas.


