**Entidades → Tablas**

Cada entidad del diagrama se convierte en una tabla.
Los atributos pasan a ser columnas.
La clave primaria (PK) de la entidad será la PK de la tabla.

Ejemplo:
Entidad Alumno(DNI, Nombre, Edad) → Tabla ALUMNO con esas columnas.

** Relaciones 1 : N → Clave ajena (FK)**

En una relación uno a muchos, la clave primaria de la entidad del lado 1 pasa como clave ajena (FK) a la tabla del lado N.

Ejemplo:
Profesor (1) — (N) Curso
→ En la tabla CURSO aparece ProfesorID como FK.

**Relaciones N : M → Nueva tabla**

Las relaciones muchos a muchos se convierten en una tabla intermedia.
Esta tabla contiene las PK de las dos entidades como FK, y juntas son su PK.

Ejemplo:
Alumno (N) — (M) Curso
→ Tabla Matricula(AlumnoID, CursoID).

**Relaciones 1 : 1**

Se puede poner la PK de una entidad como FK en la otra, normalmente donde tenga más sentido o más dependencia.

**Atributos multivalorados**

Se crean en una tabla aparte, con una FK hacia la entidad original.
