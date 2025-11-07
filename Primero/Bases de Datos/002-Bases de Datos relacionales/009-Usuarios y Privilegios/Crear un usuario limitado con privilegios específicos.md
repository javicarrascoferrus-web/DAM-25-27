En un SGBD como MySQL, crear usuarios y darles solo los permisos necesarios es clave para la seguridad. En este caso, quiero un usuario llamado usuarioempresarial que se conecte desde localhost, no tenga permisos globales peligrosos y solo pueda trabajar dentro de la base de datos empresarial.

Los siguientes comandos SQL se utilizan para:

**CREATE USER:** crea la cuenta y define desde dónde puede conectarse (localhost) y su contraseña.

**GRANT USAGE ON**  : concede “uso” global sin privilegios reales.

**Limitar acceso:** no dar privilegios globales; solo a empresarial.

**Privilegios específicos:** SELECT, INSERT, UPDATE sobre todas las tablas de empresarial.


a continuación te escribo un ejemplo de como utilizar estos comandos:

**Paso 1: crear el usuario local**
 
CREATE USER 'usuarioempresarial'@'localhost'
IDENTIFIED BY 'PASWWORD';

**Paso 2: privilegios generales mínimos (sin poderes sobre objetos)**
GRANT USAGE ON 
TO 'usuarioempresarial'@'localhost'

**Paso 3: limitar acceso => no damos privilegios globales adicionales**

REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'usuarioempresarial'@'localhost'

**Paso 4: privilegios específicos en la base de datos empresarial**
GRANT SELECT, INSERT, UPDATE
ON empresarial.
TO 'usuarioempresarial'@'localhost'


Con estos pasos, usuarioempresarial existe, puede autenticarse y solo tiene SELECT, INSERT y UPDATE dentro de empresarial. No posee privilegios globales, así que queda limitado al ámbito que necesitamos
