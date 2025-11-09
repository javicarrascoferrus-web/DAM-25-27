En este ejercicio vamos a aprender cómo Flexbox nos ayuda a organizar los elementos de una página web de forma ordenada, flexible y adaptativa, algo muy útil al diseñar un currículum vitae digital.
En mi caso, aprovecharé este ejercicio para diseñar un CV sencillo donde pueda incluir mis aficiones, como natación y lectura, que me ayudan a mantener la constancia y la concentración tanto en los estudios como en la programación.

**Para que la página sea clara y accesible:**

1. Usamos las etiquetas HTML semánticas (<header>, <section>, <ul>, <img>, etc.).

2. Aplicamos Flexbox en el contenedor principal para dividir la página en dos columnas:

3. Una columna izquierda con los datos personales y la foto.

4. Una columna derecha con la formación, experiencia y hobbies.
	
	Aquí tecleo una serie de comandos funcional de CV en HTML:
	
	<!doctype html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Currículum de Javier Carrasco</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      background-color: #f4f4f4;
    }
    .contenedor {
      display: flex;
      flex-direction: row;
      min-height: 100vh;
    }
    .izquierda {
      background-color: #2c3e50;
      color: white;
      width: 30%;
      padding: 20px;
    }
    .derecha {
      background-color: white;
      width: 70%;
      padding: 20px;
    }
    img {
      width: 100%;
      border-radius: 10px;
      margin-bottom: 15px;
    }
    h1, h2 {
      margin-top: 0;
    }
    ul {
      list-style-type: square;
      padding-left: 20px;
    }
  </style>
</head>
<body>
  <div class="contenedor">
    <div class="izquierda">
      <img src="javier.jpg" alt="Foto de Javier">
      <h1>Javier García</h1>
      <p><strong>Email:</strong> javicarrascoferrus@gmail.com</p>
      <p><strong>Teléfono:</strong> +34 6685 573 959</p>
    </div>
    <div class="derecha">
      <section>
        <h2>Formación</h2>
        <ul>
          <li>CFGS Desarrollo de Aplicaciones Multiplataforma - IES TAME (2025–2027)</li>
        </ul>
      </section>

      <section>
        <h2>Experiencia Profesional</h2>
        <ul>
          <li>Prácticas en Tienda Online Demo - Desarrollo y mantenimiento web</li>
        </ul>
      </section>

      <section>
        <h2>Hobbies y Aficiones</h2>
        <ul>
          <li>Natación: me ayuda a mantener la disciplina y el equilibrio.</li>
          <li>Leer: me inspira nuevas ideas y mejora mi concentración.</li>
        </ul>
      </section>
    </div>
  </div>
</body>
</html>

	
	
	
	Gracias al uso de Flexbox, he aprendido a crear una disposición visual más ordenada y responsiva, ideal para presentar un currículum de forma profesional.
Este ejercicio me permitió aplicar conceptos de estructuración HTML y estilos CSS, además de integrar aspectos personales como mis hobbies de natación y lectura, que reflejan mi capacidad de organización y constancia.
