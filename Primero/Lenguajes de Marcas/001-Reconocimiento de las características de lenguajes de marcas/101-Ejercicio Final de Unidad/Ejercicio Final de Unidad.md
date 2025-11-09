La idea es construir un CV en JSON con una estructura realista: datos personales, formación, experiencia profesional, idiomas, vehículos, aficiones y hobbies. JSON es perfecto porque es legible, portable y se integra fácil con webs o apps.

El CV contendrá los siguientes apartados:

Elementos singulares (objetos): datos_personales, perfil.

Colecciones: formacion, experiencia, idiomas, vehiculos, aficiones, hobbies.

Objetos dentro de objetos: en experiencia, cada empresa contiene varios puestos con fechas y logros.

Este es el documento JSON que va a contener la información:
{
  "cv": {
    "version": "1.0",
    "ultima_actualizacion": "2025-11-07",
    "datos_personales": {
      "nombre": "Javier",
      "apellidos": "Carrasco Ferrús",
      "email": "javicarrascoferrus@gmail.com",
      "telefono": "+34 685573959",
      "localidad": "Valencia, España",
      "enlaces": {
        "github": "-",
        "linkedin": "-"
      },
      "fotografia": "javier_carrasco.jpg"
    },
    "perfil": "Técnico superior en desarrollo a aplicaciones multiplataforma. Me gusta escribir código claro, automatizar tareas y documentar bien los proyectos.",
    "formacion": [
      {
        "titulo": "CFGS Desarrollo de Aplicaciones Multiplataforma",
        "centro": "IES TAME",
        "ciudad": "Valencia",
        "fecha_inicio": "2024-09",
        "fecha_fin": "2026-06",
        "asignaturas_destacadas": [
          "Programación",
          "Bases de datos",
          "Entornos de desarrollo"
        ]
      },
		
			"aficiones": [
      "Natación",
      "Lectura técnica",
      "Senderismo"
    ],
    "hobbies": [
      { "nombre": "Natación", "frecuencia_semana": 3 },
      { "nombre": "Impresión 3D", "frecuencia_semana": 1 }
    ],
			
Con este JSON tengo un CV estructurado y escalable: puedo añadir proyectos, certificaciones o más puestos sin romper el formato. Este enfoque encaja con lo visto en la unidad  y te permite reutilizar el CV en una web o en scripts.
