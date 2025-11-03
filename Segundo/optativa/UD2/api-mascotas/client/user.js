// Se hace en variables por si en el futuro cambia un endpoint no tener que cambiarlo en el código entero
const API_URL = "http://localhost:5058";
const ENDPOINT_MESSAGES = `${API_URL}/messages/`;
const ENDPOINT_TYPES = `${API_URL}/types/`;
const ENDPOINT_PETS  = `${API_URL}/pets/`;

// De classic one de definir todos los elementos del HTML que vamos a acceder ZzZ
const selectTipo = document.getElementById("tipo");
const tbody = document.querySelector("#tablaMascotas tbody");
const form = document.getElementById("formContacto");
const resultado = document.getElementById("resultado");
const inputPetId = document.getElementById("petId");

// Emojis ftw
const emojiMapa = { perro:"🐶", gato:"🐱", conejo:"🐰", loro:"🦜", tortuga:"🐢", pez:"🐠" };
const emojiDe = (tipo) => emojiMapa[(tipo || "").toLowerCase()] || "🐙";

function setCargando() {
    tbody.innerHTML = `<tr><td colspan="5">Cargando…</td></tr>`;
}
function setMensaje(msg) {
    tbody.innerHTML = `<tr><td colspan="5" >${msg}</td></tr>`;
}

// Accedemos a los distintos tipos de animalejos para  establecr las opciones del select
async function cargarTipos() {
  // Tienes que hacer tú lol XD jejeje
  return 0;
}

// Carga todas las mascotas del tipo especificado
// Sino se especifica tipo pues carga todas
async function cargarMascotas(tipo = "") {
    setCargando();
    try {
        const url =`${ENDPOINT_PETS}`;
        const res = await fetch(url);
        const mascotas = await res.json();
        const disponibles = mascotas.filter(p => !p.adopted);
        if (!disponibles.length) return setMensaje("No hay mascotas disponibles.");

        const frag = document.createDocumentFragment();
        disponibles.forEach(p => {
            const tr = document.createElement("tr");
            tr.classList.add("clickable");
            tr.dataset.petId = p.id;
            tr.innerHTML = `
            <td>${p.id}</td>
            <td>${p.name}</td>
            <td>${emojiDe(p.category)} ${p.category}</td>
            <td>${p.age ?? "-"}</td>
            <td>${p.adopted ? "Adoptado" : "Disponible"}</td>
            `;
            // Al pulasar la fila de una mascota ponemos el id en el campo del mensaje y hacemos focus (nos llevamos el ratón ahí)
            tr.addEventListener("click", () => {
                inputPetId.value = p.id;           
                inputPetId.focus();
            });
            frag.appendChild(tr);
        });
        tbody.innerHTML = "";
        tbody.appendChild(frag);
    } catch (err) {
        console.error(err);
        setMensaje("No se pudo cargar la lista. Comprueba que la API está activa y con CORS permitido.");
    }
}

async function init() {
    await cargarTipos();
    await cargarMascotas();
}

init();