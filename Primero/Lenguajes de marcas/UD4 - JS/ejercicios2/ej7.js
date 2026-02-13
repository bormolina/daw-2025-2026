const formulario = document.getElementById('form-imc')
const resultado_p = document.getElementById('resultado')

formulario.addEventListener('submit', (event) => {
    event.preventDefault()
    const altura = document.getElementById('atr-altura').value
    const peso = document.getElementById('atr-peso').value
    const imc = peso / (altura * altura)

    let imc_resultado = ''

    if(imc <= 18.5){
        imc_resultado = 'Bajo peso'
    }
    else if(imc > 18.5 && imc <= 24.9){
        imc_resultado = 'Normal'
    }
    else if(imc > 24.9 && imc <= 29.9){
        imc_resultado = 'Sobrepeso'
    }
    else{
        imc_resultado = 'Obesidad'
    }

    resultado.textContent = imc_resultado
})