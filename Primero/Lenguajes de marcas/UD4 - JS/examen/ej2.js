const form = document.getElementById("formGasolina")
const kmInput = document.getElementById("km")
const litrosInput = document.getElementById("litros")
const precioInput = document.getElementById("precio")

const outConsumo = document.getElementById("consumo")
const outCoste = document.getElementById("coste")

form.addEventListener("submit", (e) => {
  e.preventDefault()

  const km = parseFloat(kmInput.value)
  const litros = parseFloat(litrosInput.value)
  const precio = parseFloat(precioInput.value)

  const consumo = (litros / km) * 100
  const coste = litros * precio

  outConsumo.textContent = consumo.toFixed(2) + " L/100 km"
  outCoste.textContent = coste.toFixed(2) + " €"
})