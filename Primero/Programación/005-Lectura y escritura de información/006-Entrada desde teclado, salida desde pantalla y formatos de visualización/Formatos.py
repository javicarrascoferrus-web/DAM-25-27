Para centrar texto en la terminal hay que saber cuántas columnas y filas tiene la consola y, a partir de ahí, calcular la posición donde debe empezar el texto.

Vamos a estructurarlo de la siguiente manera:

Medir la terminal: shutil.get_terminal_size(fallback=(80, 24)) → columns, rows.

Texto a centrar: "Natación".

Cálculo de inicio (columna): col = max(1, (columns - len(texto)) // 2 + 1).
(ANSI usa posiciones 1-basadas).


Ahora vamos a detallarlo con código:

**Código**:


Averiguar caracteres de consola.py: 

**averiguar caracteres de consola.py** 

import shutil

def obtener_tamano_terminal():
    size = shutil.get_terminal_size(fallback=(80, 24))
    # Devolvemos columnas y filas
    return size.columns, size.lines

if __name__ == "__main__":
    cols, rows = obtener_tamano_terminal()
    print(f"Columnas: {cols}, Filas: {rows}")
		
		
		
		
Escribir texto centrado.py: 

**escribir texto centrado.py** 

import shutil

def posicion_centrada(texto: str):
    size = shutil.get_terminal_size(fallback=(80, 24))
    cols, rows = size.columns, size.lines
    # Calcular inicio horizontal (col) y vertical (row)
    col = max(1, (cols - len(texto)) // 2 + 1)   # ANSI es 1-based
    row = max(1, rows // 2)
    return row, col, rows, cols

def imprimir_centrado(texto: str):
    row, col, _, _ = posicion_centrada(texto)

if __name__ == "__main__":
    imprimir_centrado("Natación")


Con shutil.get_terminal_size() y los códigos ANSI, es fácil centrar un texto en consola.
Este ejercicio conecta con otros contenidos de la unidad: E/S por consola, escape codes, y control básico del cursor.
