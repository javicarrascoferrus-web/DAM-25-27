En este trabajo se va a crear una base de datos llamada tienda_online.
La idea es organizar la información de forma ordenada, igual que en la natación cada movimiento tiene que estar bien coordinado para avanzar.


CREATE DATABASE tienda_online

CREATE TABLE productos (
Identificador (tipo INT, no nulo)
nombre (tipo VARCHAR(50), no nulo)
descripcion (tipo TEXT, no nulo)
precio (tipo DOUBLE(10,2), no nulo)
peso (tipo DOUBLE(10,2), no nulo)
)

CREATE TABLE  clientes (
Identificador (tipo INT, no nulo)
nombre (tipo VARCHAR(50), no nulo)
apellidos (tipo VARCHAR(100), no nulo)
telefono (tipo VARCHAR(50), no nulo)
email (tipo VARCHAR(100), no nulo)
)

SELECT PRODCUTOS
SELECT CLIENTES 

Con esta base de datos se podría gestionar una tienda online sencilla.
Los productos guardan nombre, descripción, precio y peso.
Los clientes guardan sus datos de contacto para que se les pueda vender y enviar lo que compren.

Este ejercicio ayuda a entender cómo organizar los datos en tablas usando SQL.
