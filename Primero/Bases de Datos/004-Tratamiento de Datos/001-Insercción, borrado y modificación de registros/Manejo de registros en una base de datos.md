En administración de bases de datos, cada acción que modifica o elimina información debe ir precedida de una copia de seguridad fiable. Hoy vas a (1) crear un backup de la base de datos empresarial, (2) ejecutar un script que elimina registros de la tabla clientes, y (3) modificar un registro concreto con UPDATE.

mysqldump es la utilidad de línea de comandos de MySQL para volcar la estructura y los datos de una o varias bases de datos a un archivo de texto SQL.


DELETE FROM <tabla> borra filas. Sin WHERE, borra todas las filas de la tabla (no la estructura).
	
UPDATE cambia valores de columnas en filas que cumplan una condición. 
La cláusula WHERE es crucial para acotar la modificación a las filas correctas.

	He creado una copia de seguridad fiable con mysqldump, has ejecutado un script de eliminación masiva de registros con criterio y, por último, has realizado una modificación puntual con UPDATE … WHERE
