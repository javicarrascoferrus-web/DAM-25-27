En este ejercicio voy a crear una página con tres contenedores y dos botones que permitan mover a papelera el primero y eliminar definitivamente el segundo.

Para conjuntar y resumir el ejercicio, voy a escribir un archivo de código HTML + CSS + JS:

**Código**:

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>Contenedores y papelera</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 800px; margin: 2rem auto; }
    .fila { display: flex; gap: 10px; margin-bottom: 1rem; }
    .contenedor { padding: .75rem 1rem; border: 1px solid #ccc; border-radius: 8px; }
    .acciones { display: flex; gap: 10px; }
    
  </style>
</head>
<body>
  <h1>Gestión de contenedores</h1>

  <section class="fila" id="zona-contenedores">
    <div id="c1" class="contenedor">Yo soy el contenedor 1</div>
    <div id="c2" class="contenedor">Yo soy el contenedor 2</div>
    <div id="c3" class="contenedor">Yo soy el contenedor 3</div>
  </section>

  <section class="acciones">
    <button id="btnPapelera">Mover contenedor 1 a la papelera</button>
    <button id="btnEliminar">Eliminar definitivamente el contenedor 2</button>
  </section>


  <script>
    // Botones
    const btnPapelera = document.getElementById("btnPapelera");
    const btnEliminar  = document.getElementById("btnEliminar");
    const papelera     = document.getElementById("papelera");

		
**Mover contenedor 1 a la papelera (mantener en DOM, pero oculto)**:
		
		
    btnPapelera.addEventListener("click", () => {
      const c1 = document.getElementById("c1");
      if (!c1) {
        console.log("El contenedor 1 ya no está disponible (posiblemente en papelera).");
        return;
      }
      console.log("Movido a papelera:", c1.textContent.trim());
      papelera.appendChild(c1); 
		
     
		
	**Eliminar definitivamente el contenedor 2**
		
		
	
    btnEliminar.addEventListener("click", () => {
      const c2 = document.getElementById("c2");
      if (!c2) {
        console.log("El contenedor 2 ya no existe.");
        return;
      }
      console.log("Eliminado definitivamente:", c2.textContent.trim());
      c2.remove(); // desaparece del DOM y no vuelve a mostrarse
    });
  </script>
</body>
</html>



Con este ejercicio practiqué eventos, selección de nodos, mover elementos en el DOM (con appendChild) y eliminación definitiva (con remove()
