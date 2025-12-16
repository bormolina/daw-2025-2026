def obtener_columna(m: list[list[int]], c: int) -> list[int]:
    col = []
    for fila in m:
        col.append(fila[c])
    return col

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(obtener_columna(matriz, 2))
