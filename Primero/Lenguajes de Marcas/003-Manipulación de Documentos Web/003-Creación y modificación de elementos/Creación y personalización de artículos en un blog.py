Vamos a montar un mini “motor” de blog en HTML + JS: cargaremos un blog.json con fetch, clonaremos una plantilla HTML (<template></template>), rellenaremos cada artículo con sus datos (título, fecha, texto) y lo insertaremos en el DOM
	
	Para crea el siguiente blog, escribiremos:
	
**comando fetch:**

	fetch("blog.json")
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos cargados
  });

	
	
**Clonar la plantilla del articulo con cloneNode**:
	const template = document.getElementById("articulo");
const fragment = template.content.cloneNode(true);


**Personalización de artículos:**
data.forEach(article => {
  const h3 = fragment.querySelector("h3");
  h3.textContent = article.titulo;

  const time = fragment.querySelector("time");
  time.textContent = article.fecha;

  const p = fragment.querySelector("p");
  p.textContent = article.texto;

  const img = fragment.querySelector("img");
  img.src = article.imagen;
});



**Insertar los artículos en DOM con el comadno appenChild**:
const main = document.querySelector("main");
data.forEach(article => {
  const fragment = template.content.cloneNode(true);
  // Personalizar el artículo aquí...
  main.appendChild(fragment);
});


Con fetch cargamos el JSON, con cloneNode(true) duplicamos la plantilla, y con appendChild inyectamos cada artículo en el <main>.
Es un patrón muy útil para listas (posts, tarjetas de productos, noticias). Se relaciona con contenidos de la unidad como promesas, APIs del DOM, y plantillas HTML.
