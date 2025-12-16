from random import randint

elementos = [
    ["Hidrógeno", "H"],
    ["Helio", "He"],
    ["Litio", "Li"],
    ["Berilio", "Be"],
    ["Boro", "B"],
    ["Carbono", "C"],
    ["Nitrógeno", "N"],
    ["Oxígeno", "O"],
    ["Flúor", "F"],
    ["Neón", "Ne"]
]

vidas = 3

print('=== JUEGO DE LOS ELEMENTOS QUÍMICOS ===')

while vidas > 0 and len(elementos) > 0:
    elegida = randint(0, len(elementos)-1)
    elemento = elementos[elegida]
    nombre = elemento[0]
    simbolo = elemento[1]
    print(f'Adivina el símbolo del elemento: {nombre}')
    respuesta = input('Tu respuesta: ')
    if respuesta == elemento[1]:
        print('Correcto!')
    else:
        vidas -= 1
        print(f'Has fallado. El símbolo correcot era {simbolo}. Vidas restantes: {vidas}')
       
    elementos.pop(elegida)


