El objetivo es preparar una plantilla de CV en HTML + CSS que pueda reutilizar y actualizar fácilmente. La maquetación usa Flexbox para organizar el contenido en dos columnas (izquierda: datos personales; derecha: contenido profesional), con especial cuidado por la accesibilidad, la legibilidad y la estructura semántica.

**Utilizaremos:**

**HTML semántico:** header, aside, main, section, ul/li, time, etc.

**Flexbox:** contenedor principal con display:flex; para dos columnas, con gap y “stack” en móvil.

**Accesibilidad:** idioma lang="es", alt en imágenes, jerarquía de encabezados (h1, h2).

**CSS escalable:** variables (:root) para colores, radio, sombra; tipografía del sistema; tamaños fluidos.

Utilizaremos dos códigos para darle forma y color a nuestro CV:

**Este es el código básico HTML:**

<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>CV — Javier Carrasco</title>
  <link rel="stylesheet" href="styles.css" />
  <meta name="description" content="Currículum vitae de Javier Carrasco: formación, experiencia, idiomas y más." />
</head>
<body>
  <header class="cabecera" role="banner">
    <div class="identidad">
      <img class="fotojavier" src="fotojavier.jpg" alt="Foto de perfil de Javier Carrasco" />
      <div>
        <h1>Javier Carrasco</h1>
        <p class="claim">Desarrollo · Bases de datos · Frontend</p>
      </div>
    </div>
    <ul class="contacto">
      <li><strong>Email:</strong> javicarrascoferrus@gmail.com</li>
      <li><strong>Tel:</strong> +34 685 573 959</li>
      <li><strong>Ubicación:</strong> Valencia, España</li>
      <li><strong>GitHub:</strong>https://github.com/javicarrascoferrus-web/DAM-25-27.git</li>
    
    </ul>
  </header>

  <div class="cv">

		
    <aside class="col izquierda" aria-label="Datos personales y resúmenes">
      <section class="panel">
        <h2>Datos personales</h2>
        <ul class="lista">
          <li><strong>Nombre:</strong> Javier Carrasco</li>
          <li><strong>DNI:</strong> 20853285J</li>
          <li><strong>Fecha de nacimiento:</strong> <time datetime="1997-04-23">23/04/1997</time></li>
        </ul>
      </section>

      <section class="panel">
        <h2>Idiomas</h2>
        <ul class="lista">
          <li>Español — Nativo (C2)</li>
          <li>Inglés — B2</li>
        </ul>
      </section>

      <section class="panel">
        <h2>Vehículos</h2>
        <ul class="lista">
          <li>Permiso B — Propio</li>
          <li>Bicicleta urbana</li>
        </ul>
      </section>

      <section class="panel">
        <h2>Aficiones</h2>
        <ul class="lista">
          <li>Natación (3 días/semana)</li>
          <li>Leer (técnica y narrativa)</li>
        </ul>
      </section>

      <section class="panel">
        <h2>Hobbies</h2>
        <ul class="lista">
          <li>Impresión 3D</li>
          <li>Senderismo</li>
        </ul>
      </section>
    </aside>


    <main class="col derecha" role="main">
      <section class="panel">
        <h2>Perfil</h2>
        <p>Soy técnico en desarrollo con interés en backend y datos. Me gusta escribir código claro, automatizar tareas y documentar procesos. Trabajo con Python, SQL y HTML/CSS, aplicando buenas prácticas y control de versiones con Git.</p>
      </section>

      <section class="panel">
        <h2>Formación</h2>
        <ul class="timeline">
          <li>
            <div class="fila">
              <div>
                <strong>CFGS Desarrollo de Aplicaciones Multiplataforma</strong> — IES TAME
              </div>
              <div class="fechas">
                <time datetime="2024-09">09/2024</time> — <time datetime="2027-06">06/2027</time>
              </div>
            </div>
            <p>Asignaturas destacadas: Programación, Bases de datos, Entornos de desarrollo.</p>
          </li>
          <li>
            <div class="fila">
        
         
            </div>
          </li>
        </ul>
      </section>

      <section class="panel">
        <h2>Experiencia profesional</h2>
        <ul class="timeline">
          <li>
            <div class="fila">
              <div>
                <strong>Tienda Online Microsoft S.L.</strong> — Prácticas (Desarrollo)
              </div>
              <div class="fechas">
                <time datetime="2025-02">02/2025</time> — <time datetime="2025-07">07/2025</time>
              </div>
            </div>
            <ul class="lista">
              <li>Creación de vistas SQL para informes de ventas.</li>
              <li>Automatización de backups con Python.</li>
              <li>Maquetación de páginas internas con HTML/CSS (Flexbox).</li>
            </ul>
          </li>
        </ul>
      </section>

			

  <footer class="pie" role="contentinfo">
    <small>© 2025 Javier Carrasco — Plantilla de CV (HTML/CSS) — Flexbox</small>
  </footer>
</body>
</html>

	
	 **Este es el código CSS**:
	

:root{
  --fondo: #f6f8fb;
  --panel: #ffffff;
  --borde: #e5e7eb;
  --texto: #0f172a;
  --muted: #64748b;
  --acento: #2563eb;
  --shadow: 0 8px 24px rgba(2, 6, 23, .08);
  --radius: 16px;
  --gap: 24px;
}

* { box-sizing: border-box; }
html, body { height: 100%; }
body {
  margin: 0;
  background: var(--fondo);
  color: var(--texto);
  font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  line-height: 1.55;
}


.cabecera {
  max-width: 1100px;
  margin: 0 auto;
  padding: 24px 16px 8px;
}
.identidad {
  display: flex; align-items: center; gap: 16px;
}
.avatar {
  width: 96px; height: 96px; border-radius: 50%;
  object-fit: cover; box-shadow: var(--shadow);
}
.cabecera h1 { margin: 0; font-size: 1.75rem; }
.claim { margin: 4px 0 0; color: var(--muted); }
.contacto {
  display: flex; flex-wrap: wrap; gap: 12px 24px;
  list-style: none; padding: 12px 0 0; margin: 0;
  color: var(--muted);
}
.contacto li { white-space: nowrap; }


.cv {
  display: flex; gap: var(--gap);
  max-width: 1100px; margin: 12px auto 32px; padding: 0 16px;
}
.col { display: flex; flex-direction: column; gap: var(--gap); }
.izquierda { flex: 0 0 320px; }
.derecha { flex: 1 1 auto; }


.panel {
  background: var(--panel);
  border: 1px solid var(--borde);
  border-radius: var(--radius);
  padding: 20px;
  box-shadow: var(--shadow);
}
.panel h2 {
  margin: 0 0 8px;
  color: var(--acento);
  font-size: 1.1rem;
}
.lista { margin: 0; padding-left: 18px; }
.lista li { margin: 6px 0; }

/* Timeline (formación/experiencia) */
.timeline { list-style: none; margin: 0; padding: 0; }
.timeline li { padding: 12px 0; border-bottom: 1px dashed var(--borde); }
.timeline li:last-child { border-bottom: 0; }
.fila { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; }
.fechas { color: var(--muted); white-space: nowrap; }


.pie { text-align: center; padding: 16px; color: var(--muted); }


@media (max-width: 860px) {
  .cv { flex-direction: column; }
  .izquierda { flex-basis: auto; }
  .identidad { align-items: flex-start; }
  .contacto { gap: 8px 16px; }
}

	He construido una plantilla de CV profesional y reutilizable con HTML semántico y CSS Flexbox, respetando los apartados trabajados en clase. El diseño es limpio, accesible y responsive, y las variables CSS te permiten ajustar rápidamente colores, radios o sombras.
