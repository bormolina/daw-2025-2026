// Primer bloque (variables): declaramos las variables de estado
let contador = 0

// Segundo bloque (DOM): Declaramos las variables que hacen referencia a elementos de web
const spanContador = document.getElementById("contador")
const boton = document.getElementById("btnIncrementar")

// Tercer bloque (lógica): establecemos el comportamiento de los botones
boton.addEventListener("click", () => {
    contador++;
    spanContador.textContent = contador
})
