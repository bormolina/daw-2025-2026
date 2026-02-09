function aleatorioEntero(n, m) {
    return Math.floor(Math.random() * (m - n + 1)) + n
}

const b_d4 = document.getElementById('b-d4')
const r_d4 = document.getElementById('r-d4')
const b_d6 = document.getElementById('b-d6')
const r_d6 = document.getElementById('r-d6')

// Os dejo el resto a vosotros

b_d4.addEventListener('click', () => {
    r_d4.textContent = aleatorioEntero(1, 4)
})

b_d6.addEventListener('click', () => {
    r_d6.textContent = aleatorioEntero(1, 6)
})

