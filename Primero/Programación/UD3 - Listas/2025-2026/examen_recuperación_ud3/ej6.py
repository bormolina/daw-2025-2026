def movimientos_torre(coord: str) -> list[str]:
    letra = coord[0]
    num = int(coord[1])
    
    movimientos = []

    # Casillas de la misma fila, dejamos fijo el número e iteramos la letra
    for l in 'abcdefgh':
        if l != letra:
            movimientos.append(f'{l}{num}')

    # Casillas de la misma columna, dejamos fija la letra e iteramos el número
    for n in range(1, 9):
        if n != num:
            movimientos.append(f'{letra}{n}')

    return movimientos

while True:
    coord = input('Inserta la posición de la torre (por ejemplo a4): ')
    print(f'La torre puede moverse a: {movimientos_torre(coord)}')
