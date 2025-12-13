Para crear interfaces sencillas en Python suelo usar Tkinter, que viene con la instalación estándar. Con unos cuantos widgets puedo pedir datos al usuario y luego persistirlos en un archivo CSV.
En este ejercicio la idea es: el usuario escribe nombre, apellidos y email, pulsa un botón, y el programa añade esa fila a clientes.csv

Vamos a empezar impotando el archivo en Python y después introduciendo los datos correspondientes:



**Código:



import tkinter as tk
from tkinter import messagebox
import csv
import os


**Ventana principal
root = tk.Tk()
root.title("Gestión de Clientes (mini)")


**Etiqueta y Entry: Nombre**
tk.Label(root, text="Introduce el nombre del cliente").grid(row=0, column=0, sticky="w", padx=8, pady=(10, 2))
nombre = tk.Entry(root, width=35)
nombre.grid(row=1, column=0, padx=8, pady=(0, 10))



**Etiqueta y Entry: Apellidos**
tk.Label(root, text="Introduce los apellidos del cliente").grid(row=2, column=0, sticky="w", padx=8, pady=(0, 2))
apellidos = tk.Entry(root, width=35)
apellidos.grid(row=3, column=0, padx=8, pady=(0, 10))


**Etiqueta y Entry: Email**

tk.Label(root, text="Introduce el email del cliente").grid(row=4, column=0, sticky="w", padx=8, pady=(0, 2))
email = tk.Entry(root, width=35)
email.grid(row=5, column=0, padx=8, pady=(0, 10))


**Text (log)**
texto = tk.Text(root, height=5, width=30)
texto.grid(row=7, column=0, padx=8, pady=(6, 10), sticky="we")


def insertaCliente():
    n = nombre.get().strip()
    a = apellidos.get().strip()
    e = email.get().strip()


**Validación sencilla**
    if not n or not a or not e:
        messagebox.showwarning("Campos obligatorios", "Rellena nombre, apellidos y email.")
        return
    if "@" not in e:
        messagebox.showwarning("Email no válido", "Introduce un email con '@'.")
        return


**Abrir en modo de anexión y escribir separado por comas**
    try:
		
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow([n, a, e])


**Limpiar entradas y registrar en el Text**
        nombre.delete(0, tk.END)
        apellidos.delete(0, tk.END)
        email.delete(0, tk.END)

        texto.insert(tk.END, f"Insertado: {n} {a} <{e}>\n")
        texto.see(tk.END)  # auto-scroll

    except Exception as err:
        messagebox.showerror("Error", f"No se pudo guardar: {err}")


**Botón: Insertar un cliente**
btn = tk.Button(root, text="Insertar un cliente", command=insertaCliente)
btn.grid(row=6, column=0, padx=8, pady=(0, 4), sticky="we")

root.mainloop()


Con Tkinter es rápido montar una GUI básica para capturar datos y guardarlos en CSV.
Hemos usado Label, Entry, Button y Text, además de una validación mínima y escritura append para no perder registros anteriores.
