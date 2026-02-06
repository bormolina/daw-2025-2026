const contenedor = document.getElementById('contenedor')
const btn_rojo = document.getElementById('btn-rojo')
const btn_azul = document.getElementById('btn-azul')
const btn_verde = document.getElementById('btn-verde')

btn_rojo.addEventListener('click', () =>{
    contenedor.style.backgroundColor = 'red'
})

btn_azul.addEventListener('click', () =>{
    contenedor.style.backgroundColor = 'blue'
})

btn_verde.addEventListener('click', () =>{
    contenedor.style.backgroundColor = 'peru'
})