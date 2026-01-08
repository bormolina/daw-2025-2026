def coordenadas(coord: str) -> tuple[int, int]:
    letra = coord[0]
    num = int(coord[1])

    col = 'abcdefgh'.index(letra)
    fila = 8 - num

    return (fila, col)


while True:
    coord = input('Inserta una coordenada: ')
    resultado = coordenadas(coord)
    print(f'Fila: {resultado[0]}, columna: {resultado[1]}')
