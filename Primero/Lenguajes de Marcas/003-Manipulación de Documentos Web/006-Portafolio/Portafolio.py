En este ejercicio se parte del trabajo realizado por Jose Vicente, quien diseñó una galería de imágenes con CSS Grid para su portafolio.
El objetivo es añadir una ventana modal que muestre cada imagen ampliada cuando el usuario hace clic sobre ella.

De esta forma, se practica la interacción entre HTML, CSS y JavaScript, aplicando conceptos de estilos dinámicos, eventos del DOM y manipulación de atributos CSS desde JavaScript.


**Código**


<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>Galería de imágenes - Jose Vicente</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      background: #f4f4f4;
    }

		
    **Galería con CSS Grid**
    .galeria {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 10px;
      padding: 20px;
    }

    .galeria img {
      width: 100%;
      border-radius: 8px;
      cursor: pointer;
      transition: transform 0.3s;
    }

    .galeria img:hover {
      transform: scale(1.05);
    }

  **Estilo de la ventana modal (oculta por defecto**
    .modal {
      display: none;                /* Oculta al cargar */
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: rgba(0,0,0,0.8);
      justify-content: center;
      align-items: center;
      z-index: 999;
    }

    .modal img {
      max-width: 80%;
      max-height: 80%;
      border: 4px solid white;
      border-radius: 10px;
    }

    .cerrar {
      position: absolute;
      top: 15px;
      right: 20px;
      color: white;
      font-size: 30px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h1 style="text-align:center;">Galería de Jose Vicente</h1>
	

**Contenedor principal**
    <img src="img1.jpg" alt="Imagen 1">
    <img src="img2.jpg" alt="Imagen 2">
    <img src="img3.jpg" alt="Imagen 3">
  </section>

	
**Ventana modal oculta**
  <div class="modal" id="ventanaModal">
    <span class="cerrar" id="cerrarModal">&times;</span>
    <img id="imagenAmpliada" src="" alt="Imagen ampliada">
  </div>

	
  <script>
**Seleccionar todas las imágenes**
    const imagenes = document.querySelectorAll(".galeria img");
    const modal = document.getElementById("ventanaModal");
    const imgAmpliada = document.getElementById("imagenAmpliada");
    const cerrar = document.getElementById("cerrarModal");

    // Evento de clic para cada imagen
    imagenes.forEach(img => {
      img.addEventListener("click", function() {
        imgAmpliada.src = this.src;       // Cambia la imagen dentro del modal
        modal.style.display = "flex";     // Muestra el modal
        console.log("Imagen mostrada:", this.alt);
      });
    });

    // Cerrar la ventana modal
    cerrar.addEventListener("click", function() {
      modal.style.display = "none";
      console.log("Modal cerrado");
    });

    // También cerrar haciendo clic fuera de la imagen
    modal.addEventListener("click", function(e) {
      if (e.target === modal) {
        modal.style.display = "none";
      }
    });
  </script>
</body>
</html>

En este ejercicio aprendí a combinar CSS Grid para la estructura y JavaScript para la interactividad, creando un efecto de galería con ventana modal.
Con display: none y display: flex se controla la visibilidad del modal, y mediante eventos click se logra la interacción con las imágenes.
