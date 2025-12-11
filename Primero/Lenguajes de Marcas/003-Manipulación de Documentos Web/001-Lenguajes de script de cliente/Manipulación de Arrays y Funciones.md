​
**Declaración de arrays:**
let especiesAnimales = ["Perro", "Gato", "Elefante", "Tigre", "León"];

console.log("Contenido del array:", especiesAnimales);
​
​
​
**Función para mostrar especies**

function mostrarEspecies(array) {

    console.log("Especies en el array:"
    
    
    
**Llamada a la función mostrarEspecies**

mostrarEspecies(especiesAnimales);
​
​
**Operadores de comparación**:

console.log("Número de especies:", especiesAnimales.length);

console.log("¿Hay menos de 5 especies?", especiesAnimales.length < 5);

console.log("¿Hay 5 o menos especies?", especiesAnimales.length <= 5);

console.log("¿Hay más de 5 especies?", especiesAnimales.length > 5);

console.log("¿Hay 5 o más especies?", especiesAnimales.length >= 5);
​
​
**Función para contar especies**:

function contarEspecies(array) {

    return array.length;
​
​
**Función para agregar una nueva especie**
function agregarEspecie(array, nuevaEspecie) {
    array.push(nuevaEspecie);
​
​
​
En este ejercicio he trabajado con arrays y funciones para gestionar listas de datos en JavaScript.
Aprendí a declarar un array, recorrerlo, contar sus elementos, compararlos con un número fijo y modificar su contenido con nuevas especies.
