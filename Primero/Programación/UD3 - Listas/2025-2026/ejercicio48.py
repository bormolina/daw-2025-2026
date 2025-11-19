matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, 5]
]

for i, fila in enumerate(matriz):
    for j, n in enumerate(fila):
        if n < 0:
            matriz[i][j] *= -1

print(matriz)