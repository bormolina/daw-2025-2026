/**
 * Carga el archivo paises.json y muestra su contenido en la página.
 */
async function cargarPaises() {
    const contenedor = document.getElementById("contenedor-paises");

    try {
        // Solicita el archivo JSON
        // await sirve para esperar el resultado de una operación asíncrona sin bloquear el código 
        const respuesta = await fetch("paises.json");

        // Comprueba si la respuesta ha sido correcta
        if (!respuesta.ok) {
            throw new Error("No se pudo cargar el archivo JSON.");
        }

        // Convierte la respuesta a objeto JavaScript
        const datos = await respuesta.json();

        // Extrae la lista de países
        const paises = datos.paises.pais;

        // Borra el mensaje inicial
        contenedor.innerHTML = "";

        // Recorre todos los países y crea una tarjeta para cada uno
        paises.forEach((pais) => {
            const tarjeta = document.createElement("article");
            tarjeta.className = "tarjeta-pais";

            tarjeta.innerHTML = `
                <h2>${pais.nombre}</h2>
                <p><strong>Siglas:</strong> ${pais.siglas}</p>
                <p><strong>Población:</strong> ${pais.poblacion}</p>
                <p><strong>Área:</strong> ${pais.area} km²</p>
                <div class="capital">
                    <h3>Capital</h3>
                    <p><strong>Nombre:</strong> ${pais.capital.nombre}</p>
                    <p><strong>Habitantes:</strong> ${pais.capital.habitantes}</p>
                </div>
            `;

            contenedor.appendChild(tarjeta);
        });

    } catch (error) {
        // Muestra un mensaje si ocurre algún error
        contenedor.innerHTML = `<p class="error">Error: ${error.message}</p>`;
    }
}

// Ejecuta la función principal
cargarPaises();