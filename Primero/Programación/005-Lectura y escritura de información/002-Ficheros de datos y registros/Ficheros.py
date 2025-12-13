Para gestionar datos de forma sencilla en consola, Python nos permite definir clases para representar entidades (por ejemplo, un Cliente) y combinar eso con un menú para operar sobre una lista: insertar, listar, actualizar o eliminar.
Para que los datos no se pierdan al cerrar el programa, se puede usar pickle y guardar la lista de clientes en un archivo binario. Además, con códigos ANSI podemos “limpiar” la pantalla y que el menú se vea más ordenado.

**Código*:

import os, pickle

FICHERO = "clientes.pickle"

class Cliente:
    def __init__(self, n, a, e): self.n, self.a, self.e = n, a, e
    def __str__(self): return f"{self.n} {self.a} <{self.e}>"

def clear(): print("\033[2J\033[H", end="")
def cargar(): return pickle.load(open(FICHERO,"rb")) if os.path.exists(FICHERO) else []
def guardar(c): pickle.dump(c, open(FICHERO,"wb"))

def insertar(c):
    n=input("Nombre: "); a=input("Apellidos: "); e=input("Email: ")
    if n and a and e: c.append(Cliente(n,a,e)); guardar(c); print("✔ Insertado.")
    else: print("Campos obligatorios.")

def listar(c):
    if not c: print("(Vacío)"); return
    for i,x in enumerate(c,1): print(f"{i}. {x}")

def buscar(c,n): return next((i for i,x in enumerate(c) if x.n.lower()==n.lower()),-1)

def actualizar(c):
    n=input("Nombre a actualizar: "); i=buscar(c,n)
    if i==-1: print("No encontrado."); return
    a=input("Nuevos apellidos: ") or c[i].a
    e=input("Nuevo email: ") or c[i].e
    c[i]=Cliente(c[i].n,a,e); guardar(c); print("✔ Actualizado.")

def eliminar(c):
    n=input("Nombre a eliminar: "); i=buscar(c,n)
    if i==-1: print("No encontrado."); return
    if input(f"¿Eliminar {c[i]}? (s/N): ").lower()=="s":
        c.pop(i); guardar(c); print("✔ Eliminado.")

def main():
    c=cargar()
    while True:
        clear()
        op=input("1)Insertar 2)Listar 3)Actualizar 4)Eliminar 0)Salir\nOpción: ")
        clear()
        if op=="1": insertar(c)
        elif op=="2": listar(c)
        elif op=="3": actualizar(c)
        elif op=="4": eliminar(c)
        elif op=="0": break
        else: print("Opción inválida.")
        input("\nEnter...")

if __name__=="__main__": main()


Con este programa se cubren los conceptos clave: clases y objetos, bucle para menú, operaciones CRUD, estética de consola con ANSI y persistencia con pickle.
