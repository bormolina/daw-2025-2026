let visible = true

const texto = document.getElementById('texto-ocultable')
const boton = document.getElementById('btn-ocultador')

boton.addEventListener('click', () => {
    if(visible){
        texto.style.visibility = 'hidden'
        visible = false
        boton.textContent = 'Mostrar texto'
    }
    else{
        texto.style.visibility = 'visible'
        visible = true
        boton.textContent = 'Ocultar texto'
    }
    
})