const form = document.getElementById("formDatos")
const resultado = document.getElementById("resultado")

form.addEventListener("submit", (event) => {
    event.preventDefault() // Evita que la página se recargue

    const nombre = document.getElementById("nombre").value   
    const edad = document.getElementById("edad").value

    resultado.textContent = `Te llamas ${nombre} y tienes ${edad} años`;
})
