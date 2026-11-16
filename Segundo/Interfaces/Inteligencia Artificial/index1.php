<?php
  if(isset($_GET['prompt'])){
  	$sistema = "-Resume en un párrafo. - Da respuestas breves. -Responde a lo siguiente: ";
    $datos = json_encode([
        "model" => "phi3:mini",
        "prompt" => $sistema.$_GET['prompt'],
        "stream" => false
    ]);

    $ch = curl_init("http://localhost:11434/api/generate");
    curl_setopt($ch, CURLOPT_POSTFIELDS, $datos);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    echo json_decode(curl_exec($ch), true)["response"];
    curl_close($ch);
    die();
  }
?>
<!doctype html>
<html>
	<head>
		<style>
      body,html{width:100%;height:100%;}
      body{display:flex;flex-direction:column;justify-content:center;align-items:center;gap:15px;}
      input{padding:15px;outline:none;border:1px solid grey;border-radius:50px;width:300px;}
      section{width:300px;height:300px;padding:15px;border-radius:20px;border:1px solid grey;display:flex;flex-direction:column;gap:15px;}
      .ia,.humano{padding:10px;background:grey;border-radius:10px;width:80%;}
      .ia{background:rgb(200,255,200);float:left;align-self:flex-start;}
      .humano{background:rgb(200,200,255);float:right;align-self:flex-end;}
    </style>
	</head>
	<body>
		<section></section>
		<input type="text">
		<script>
    	let entrada = document.querySelector("input")
      let seccion = document.querySelector("section")
      entrada.onkeyup = function(tecla){
        if(tecla.code == 'Enter'){
          let valor = entrada.value
          fetch("?prompt="+encodeURI(valor))
          .then(function(respuesta){return respuesta.text()})
          .then(function(datos){
            seccion.innerHTML += `
              <article class="humano">
                `+valor+`
              </article>
            `
            seccion.innerHTML += `
              <article class="ia">
                `+datos+`
              </article>
            `
            entrada.value = ""
          })

        }
      }
    </script>
	</body>
</html>
