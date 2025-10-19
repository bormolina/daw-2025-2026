// Función que simula una tirada lenta (devuelve una promesa)
function tirarDadoLento() {
  return new Promise((resolve) => {
    const resultado = Math.floor(Math.random() * 6) + 1;
    setTimeout(() => resolve(resultado), 1000 + Math.random() * 1000); // entre 1 y 2 s
  });
}

// Diccionario de emojis para cada cara del dado
const emojis = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"];

// Función asíncrona principal
async function lanzarDados() {
  const cantidad = parseInt(document.querySelector("#numDados").value);
  const resultadosDiv = document.querySelector("#resultados");
  let tiradas = "";

  for (let i = 0; i < cantidad; i++) {
    const resultado = await tirarDadoLento(); // Espera a cada tirada
    tiradas += emojis[resultado - 1] + " ";
    resultadosDiv.textContent = tiradas.trim(); // actualiza progresivamente
  }
}

// Enlazamos el evento del botón
document.querySelector("#btnLanzar").addEventListener("click", lanzarDados);