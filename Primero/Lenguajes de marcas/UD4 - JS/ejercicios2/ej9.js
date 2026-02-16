const form = document.getElementById("formDatos")
const resultado = document.getElementById("resultado")

form.addEventListener("submit", (event) => {
    event.preventDefault()

    let numero = parseInt(document.getElementById("numero").value)
    let cuentaAtras = "";
    while (numero >= 0) {
        cuentaAtras += numero + " ";
        numero--;
    }

    resultado.textContent = cuentaAtras;
})