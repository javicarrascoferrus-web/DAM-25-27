SQLite es una base de datos ligera que guarda todo en un único fichero (empresa.db). Para gestionarla desde Python usaremos el módulo estándar sqlite3. El objetivo es conectar con la BD, mostrar las entidades disponibles (clientes y pedidos) y ofrecer un menú en bucle con operaciones CRUD.

Esquema propuesto:

**clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellidos TEXT, telefono TEXT, email TEXT UNIQUE)**

**pedidos(id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id INTEGER, fecha TEXT, total REAL)**

Para conectar el SQLite con el programa teclearemos lo siguiente:

**import sqlite3**

basededatos = sqlite3.connect("empresa.db")
cursor = basededatos.cursor()
