let entrada = document.querySelector("input")
let seccion = document.querySelector("section")
entrada.onkeyup = function(tecla){
	if(tecla.code == 'Enter'){
  	let valor = entrada.value
    fetch("ia.php?prompt="+encodeURI(valor))
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
