// Función "lenta" que tarda 5 segundos en resolver
function obtenerTiempo() {
 return new Promise((resolve) => {
   setTimeout(() => {
     resolve("🌧️ Lloverá");
   }, 5000);
 });
}
// Versión con .then(), sin async ni await
function mostrarTiempo() {
 console.log("Obteniendo tiempo...");
 obtenerTiempo()
   .then((resultado) => {
     console.log("Resultado:", resultado);
     document.querySelector("#tiempo").textContent = resultado;
   })
   .catch((error) => {
     console.error("Error:", error);
   });
}
document.addEventListener("DOMContentLoaded", mostrarTiempo);