const chistes = [
  "—¿Cuál es el colmo de un jardinero? —Que siempre lo dejen plantado.",
  "—¿Cuál es el animal más antiguo? —La cebra, porque está en blanco y negro.",
  "—¿Por qué el libro de matemáticas estaba triste? —Porque tenía demasiados problemas.",
  "—¿Qué le dice un semáforo a otro? —No me mires, que me estoy cambiando.",
  "—¿Qué hace un pez? —Nada.",
  "—¿Qué hace un perro con un taladro? —Taladrando.",
  "—¿Cómo se despiden los químicos? —Ácido un placer."
]

const btn = document.getElementById("btnChiste")
const salida = document.getElementById("chiste")

function chisteAleatorio(chistes) {
  const i = Math.floor(Math.random() * chistes.length)
  return chistes[i]
}

btn.addEventListener("click", () => {
  salida.textContent = chisteAleatorio(chistes)
})