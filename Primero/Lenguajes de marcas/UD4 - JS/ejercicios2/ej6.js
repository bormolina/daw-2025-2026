function aleatorioEntero(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const form = document.getElementById("formDados");
const resultado = document.getElementById("resultado");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const ids = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"];
    const caras = [4, 6, 8, 10, 12, 20, 100];

    let bloquesResultado = [];

    for (let i = 0; i < ids.length; i++) {
        const cantidad = parseInt(document.getElementById(ids[i]).value);

        if (cantidad > 0) {
            let tiradas = [];
            for (let j = 0; j < cantidad; j++) {
                tiradas.push(aleatorioEntero(1, caras[i]));
            }
            bloquesResultado.push(`${ids[i]}: ${tiradas.join(", ")}`);
        }
    }

    resultado.textContent = bloquesResultado.length > 0
        ? bloquesResultado.join(" — ")
        : "No se ha tirado ningún dado.";
});