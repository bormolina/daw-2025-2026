const resultado = document.getElementById("resultado")

document.getElementById("tablaForm").addEventListener("submit", (event) => {
    event.preventDefault()
    const numero = parseInt(document.getElementById("numero").value)
    let tabla = `Tabla del ${numero}:\n`

    for (let i = 1; i <= 10; i++) {
        tabla += `${numero} x ${i} = ${numero*i}\n`
    }

    resultado.textContent = tabla
})
