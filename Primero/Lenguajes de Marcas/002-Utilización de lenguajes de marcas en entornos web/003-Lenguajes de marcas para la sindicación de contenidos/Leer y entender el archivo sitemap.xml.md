Un sitemap.xml describe las URLs de un sitio y ayuda a buscadores a descubrir y rastrear contenido. 

En este ejercicio voy a:

1- Leer el sitemap.xml

2- Identificar sus secciones principales (espacio de nombres y elementos <url>),

3- Extraer cada <loc> junto con <lastmod> y <changefreq>,

4- Exportar todo a un archivo de texto lista_enlaces.txt en el mismo directorio que el sitemap.
	
	
	**Estructura típica de un sitemap.xml:**

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.ejemplo.com/</loc>
    <lastmod>2025-09-29</lastmod>
    <changefreq>weekly</changefreq>
  </url>

</urlset>
	
	
	Con este flujo:

Comprendí la estructura del sitemap.xml (namespace y <url>),

Extraje <loc>, <lastmod>, <changefreq>,

Generé una lista legible en lista_enlaces.txt en el mismo directorio.

Esto encaja con la unidad de lenguajes de marcas y gestión de información, porque aplicamos parsing XML, atención a namespaces, y exportación de datos para su análisis o documentación
