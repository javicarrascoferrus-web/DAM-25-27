Vamos a crear un CV que tenga todo tipo de detalles, en él utilizaremos código de CSS y HTML para hacerlo lo más completo y visible posible.
Además, cargar fuentes personalizadas con @font-face (LemonBold y LemonRegular) y aplicar estilos (bordes redondeados, sombras, centrado) para mejorar legibilidad y estética.

**Estructura semántica:** header, aside (columna izquierda), main (columna derecha), section, ul.

**Flexbox:**  contenedor principal con display:flex; para columnas, con gap y comportamiento responsive.

**Fuentes personalizadas:** @font-face apuntando a /fonts/LemonBold.woff2|.woff y /fonts/LemonRegular.woff2|.woff (inclúyelas en tu proyecto).

**Estilo y alineación:4** uso de box-shadow, border-radius, espaciados coherentes y contraste correcto.



**Código HTML:**




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
