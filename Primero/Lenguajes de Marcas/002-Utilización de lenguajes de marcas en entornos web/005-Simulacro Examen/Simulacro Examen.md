Vamos a crear un CV que tenga todo tipo de detalles, en él utilizaremos código de CSS y HTML para hacerlo lo más completo y visible posible.
Además, cargar fuentes personalizadas con @font-face (LemonBold y LemonRegular) y aplicar estilos (bordes redondeados, sombras, centrado) para mejorar legibilidad y estética.

**Estructura semántica:** header, aside (columna izquierda), main (columna derecha), section, ul.

**Flexbox:**  contenedor principal con display:flex; para columnas, con gap y comportamiento responsive.

**Fuentes personalizadas:** @font-face apuntando a /fonts/LemonBold.woff2|.woff y /fonts/LemonRegular.woff2|.woff (inclúyelas en tu proyecto).

**Estilo y alineación:4** uso de box-shadow, border-radius, espaciados coherentes y contraste correcto.



**Código HTML:**

<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>CV — Javier Carraso Ferrús</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header class="cabecera" role="banner">
    <h1 class="titulo">Javier Carrasco</h1>
    <p class="subtitulo">Desarrollador · Bases de Datos · Frontend</p>
  </header>

  <div class="cv">

    <aside class="col izquierda" aria-label="Información personal">
      <img class="avatar" src="avatar.jpg" alt="Foto de Javier" />
      <div class="bloque">
        <h2>Contacto</h2>
        <ul class="lista">
          <li>Email: javicarrascoferrus@gmail.com</li>
          <li>Tel: +34 685 573 959</li>
          <li>Ciudad: Valencia</li>
          <li>GitHub: https://github.com/javicarrascoferrus-web/DAM-25-27.git</li>
        </ul>
      </div>
      <div class="bloque">
        <h2>Habilidades</h2>
        <ul class="lista">
          <li>Python · SQL · Git</li>
          <li>HTML · CSS · Flexbox</li>
          <li>Vistas/Consultas BD</li>
        </ul>
      </div>
      <div class="bloque">
        <h2>Idiomas</h2>
        <ul class="lista">
          <li>Español (nativo)</li>
          <li>Inglés (B2)</li>
        </ul>
      </div>
    </aside>


    <main class="col derecha" role="main">
      <section class="panel">
        <h2>Perfil</h2>
        <p>Me gusta escribir código claro, automatizar tareas y documentar. Disfruto aprendiendo y aplicando buenas prácticas.</p>
      </section>

      <section class="panel">
        <h2>Formación</h2>
        <ul class="lista">
          <li><strong>CFGS DAM</strong> — IES TAME (2025–2027)</li>
        </ul>
      </section>

      <section class="panel">
        <h2>Experiencia</h2>
        <ul class="lista">
          <li><strong>Tienda Online Microsoft</strong> — Prácticas (2025): SQL para informes y automatización simple con Python.</li>
        </ul>
      </section>

      <section class="panel">
        <h2>Aficiones</h2>
        <ul class="lista">
          <li><strong>Natación</strong>: me ayuda a organizar rutinas y ser constante, lo aplico al diseño del CV (orden y claridad).</li>
          <li><strong>Leer</strong>: mejora mi foco y la estructura de ideas, útil para jerarquizar contenido en la maquetación.</li>
        </ul>
      </section>
    </main>
  </div>

  <footer class="pie" role="contentinfo">
    <small>© 2025 Javier Carrasco — CV de ejemplo con Flexbox y fuentes personalizadas</small>
  </footer>
</body>
</html>


**Código de CSS**:


@font-face {
  font-family: "Lemon";
  src: url("fonts/LemonRegular.woff2") format("woff2"),
       url("fonts/LemonRegular.woff") format("woff");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: "Lemon";
  src: url("fonts/LemonBold.woff2") format("woff2"),
       url("fonts/LemonBold.woff") format("woff");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}


:root{
  --fondo: #f5f7fb;
  --primario: #0f172a;   /* casi negro */
  --acento: #2563eb;     /* azul */
  --borde: #e2e8f0;
  --panel: #ffffff;
  --sombra: 0 8px 24px rgba(15,23,42,.08);
  --radio: 16px;
  --gap: 24px;
}

* { box-sizing: border-box; }
html, body { height: 100%; }
body {
  margin: 0;
  background: var(--fondo);
  color: var(--primario);
  font-family: "Lemon", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  line-height: 1.55;
}


.cabecera {
  text-align: center;
  padding: 32px 16px 16px;
}
.titulo {
  margin: 0;
  font-size: 2rem;
  font-weight: 700; /* LemonBold */
}
.subtitulo {
  margin: 6px 0 0;
  opacity: .75;
}


.cv {
  display: flex;
  flex-direction: row;
  gap: var(--gap);
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 16px 32px;
}
.col {
  display: flex;
  flex-direction: column;
  gap: var(--gap);
}
.izquierda {
  flex: 0 0 320px;             /* columna fija aprox */
}
.derecha {
  flex: 1 1 auto;              /* columna fluida */
}


.izquierda, .panel {
  background: var(--panel);
  border: 1px solid var(--borde);
  border-radius: var(--radio);
  box-shadow: var(--sombra);
  padding: 20px;
}


.avatar {
  width: 100%;
  border-radius: 12px;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  margin-bottom: 12px;
  box-shadow: 0 6px 18px rgba(0,0,0,.08);
}
.bloque h2, .panel h2 {
  margin: 0 0 8px;
  font-size: 1.15rem;
  font-weight: 700; /* LemonBold */
  color: var(--acento);
}
.lista {
  margin: 0;
  padding-left: 18px;
}
.lista li { margin: 6px 0; }

.pie {
  text-align: center;
  padding: 16px;
  opacity: .7;
}


@media (max-width: 860px) {
  .cv { flex-direction: column; }
  .izquierda { flex-basis: auto; }
}


En este CV apliqué Flexbox para una maquetación de dos columnas clara y adaptable, y usé @font-face para dar una identidad visual coherente. Los estilos (bordes redondeados, sombras, contraste y espaciados) mejoran la legibilidad y la experiencia de usuario, justo lo visto en la unidad de lenguajes de marcas y CSS.
