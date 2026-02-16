const formulario = document.getElementById('form-par')
const resultado_p = document.getElementById('resultado')

formulario.addEventListener('submit', (event) => {
    event.preventDefault()

    const num = document.getElementById('input-number').value

    let resultado = "Es par"
    if(num % 2 !== 0){
        resultado = "Es impar"
    }

    resultado_p.textContent = resultado
})