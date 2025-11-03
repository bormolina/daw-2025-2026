const API = "http://localhost:5058";

// Carga todos los mensajes de adopción y los muestra en la tabla correspondiente
async function loadMessages() {
    return 0
}

// Carga todas las mascotas y las muestra en la tabla con su estado de adopción
async function loadPets() {
    const res = await fetch(`${API}/pets/`);
    const data = await res.json();
    const tbody = document.querySelector("#petsTable tbody");
    tbody.innerHTML = "";
    data.forEach(p => {
    const tr = document.createElement("tr");
    tr.className = p.adopted ? "adopted" : "";
    tr.innerHTML = `
        <td>${p.id}</td>
        <td>${p.name}</td>
        <td>${p.category}</td>
        <td>${p.age ?? ""}</td>
        <td>${p.adopted ? "Sí" : "Ní"}</td>
        <td>
        ${p.adopted ? "" : `<button data-id="${p.id}">Marcar adoptado</button>`}
        </td>
    `;
    tbody.appendChild(tr);
    });
}

// Detecta clics en los botones de "Marcar adoptado" y actualiza la mascota mediante una petición PATCH
document.addEventListener("click", async e => {
    return 0;
});

async function init() {
    await loadMessages();
    await loadPets();
}

init();