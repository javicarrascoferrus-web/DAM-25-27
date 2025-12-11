En este ejercicio se crea una pequeña calculadora básica con HTML y JavaScript.
El objetivo es practicar la manipulación del DOM (Document Object Model) y el uso de eventos en JavaScript.

#### **Código HTML**:

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Calculadora básica</title>
  <style>
    body { font-family: Arial; text-align: center; margin-top: 40px; }
    input, select, button { margin: 5px; padding: 5px; }
    #resultado { margin-top: 15px; font-weight: bold; }
  </style>
</head>
<body>
  <h2>Calculadora con JavaScript</h2>
 

 **Inputs para los números**
  <input type="number" id="num1" placeholder="Primer número">
  <input type="number" id="num2" placeholder="Segundo número">

**Select con las operaciones**
 <select id="operacion">
    <option value="suma">Suma</option>
    <option value="resta">Resta</option>
    <option value="multiplicacion">Multiplicación</option>
    <option value="division">División</option>
  </select>

  **Botón para ejecutar la operación**
  <button id="btnCalcular">Calcular</button>

  
	**Div para mostrar el resultado**
 <div id="resultado">Resultado: </div>
	

 #### Código JavaScript
	
 **Seleccionar los elementos del DOM**
    const num1 = document.getElementById("num1");
    const num2 = document.getElementById("num2");
    const operacion = document.getElementById("operacion");
    const btnCalcular = document.getElementById("btnCalcular");
    const resultado = document.getElementById("resultado");

	
 **Asignar función al evento click del botón**
    btnCalcular.addEventListener("click", function() {
      const a = parseFloat(num1.value);
      const b = parseFloat(num2.value);
      const op = operacion.value;
      let res;

     **Validar datos**
      if  {
        resultado.textContent = "Introduce ambos números correctamente.";
        return;
      }

      **Realizar la operación seleccionada**
      switch (op) {
        case "suma": res = a + b; break;
        case "resta": res = a - b; break;
        case "multiplicacion": res = a * b; break;
        case "division":
          res = b !== 0 ? a / b : "Error: división por 0";
          break;
      }

    **Mostrar resultado**
      resultado.textContent = "Resultado: " + res;
    });
  </script>
</body>
</html>


Con este ejercicio aprendí a combinar HTML y JavaScript para crear una pequeña aplicación interactiva.
Este tipo de práctica es útil porque representa la base de cualquier aplicación web: entrada de datos, procesamiento y salida en pantalla.
