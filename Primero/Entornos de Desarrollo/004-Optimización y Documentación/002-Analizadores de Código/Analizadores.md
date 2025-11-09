La idea es preparar un mini-proyecto web sobre natación: validar un archivo JSON con datos (nadador, distancia, tiempos por vuelta), abrirlo en el editor para formatearlo bien.
Esto mezcla habilidades básicas de datos (JSON) y despliegue estático en la web, que es justo lo que se pide para un portafolio sencillo.

El siguiente paso es validar JSON con JSONLint:

Abro el archivo JSON, Pega tu JSON y pulsa Validate JSON.

A continuación tecleamos el código que guardaremos en el archivo;

JSON de ejemplo (válido)

Guárdalo como natacion.json y valídalo en JSONLint:

{
  "nadador": "Laura Serrano",
  "fecha": "2025-11-07",
  "piscina_m": 25,
  "distancia_m": 1500,
  "vueltas": [
    { "numero": 1, "tiempo_s": 92.4 },
    { "numero": 2, "tiempo_s": 91.9 },
    { "numero": 3, "tiempo_s": 93.2 },
    { "numero": 4, "tiempo_s": 92.0 }
  ],
  "notas": "Entrenamiento a ritmo constante."
}


Con esta actividad validé un JSON real, lo integré en una página estática y lo publiqué con GitHub Pages.
A partir de aquí, puedes ampliar el JSON y mejorar la interfaz manteniendo la misma estructura básica.
