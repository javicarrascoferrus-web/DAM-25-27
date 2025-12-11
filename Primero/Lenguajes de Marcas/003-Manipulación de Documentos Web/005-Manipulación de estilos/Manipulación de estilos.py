
En este ejercicio se trabaja con HTML, CSS y JavaScript, aplicando estilos dinámicos según el contenido que el usuario introduce en un campo de entrada.
El objetivo es hacer que el programa solo realice un cálculo (en este caso, la función calculaLetra() ) cuando el dato introducido sea correcto, y al mismo tiempo ofrecer retroalimentación visual al usuario mediante colores.

Vamos a ubicar nuestro archivo "012-supedito el calculo a solo cuando es correcto.html" y le vamos a dar tono y estructura con el siguiente código que nos proporciona el enunciado:

**Código*:

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Validación dinámica</title>
  <style>
		
		
**Estilo básico del campo de entrada**
		
    input {
      background: lightsteelblue;
      border: none;
      padding: 5px;
      font-size: 16px;
      transition: all 0.3s ease-in-out;
    }

  **Clases dinámicas**
    .error {
      background: lightcoral;
      border-color: red;
    }

    .correcto {
      background: lightgreen;
      border-color: green;
    }
  </style>
</head>
<body>
  <h2>Comprobación del campo de entrada</h2>
  <input type="text" id="entrada" placeholder="Introduce 8 caracteres">
  <p id="salida"></p>

  <script>
		
**Simulación de la función calculaLetra()**
    function calculaLetra(dato) {
      return "Letra calculada para " + dato;
    }
		

 **Referencias al DOM**
    let entrada = document.getElementById("entrada");
    let salida = document.getElementById("salida");

		
**Evento para reaccionar al escribir**
    entrada.onkeyup = function() {
      let contenido = this.value;
      if (contenido.length == 8) {
        entrada.classList.remove("error");
        entrada.classList.add("correcto");
        salida.textContent = calculaLetra(contenido);
      } else {
        entrada.classList.remove("correcto");
        entrada.classList.add("error");
        salida.textContent = "";
      }
    };
  </script>
</body>
</html>

Con este ejercicio aprendí a aplicar estilos dinámicos según la validación de un campo, mejorando la interacción con el usuario.
