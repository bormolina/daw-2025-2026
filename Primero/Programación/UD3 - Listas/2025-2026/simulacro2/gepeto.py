from random import randint

def matriz_aleatoria(n: int, m: int) -> list[list[int]]:
    matriz = []
    for _ in range(n):
        matriz.append([randint(0, 9) for _ in range(m)])
    return matriz

def imprimir_matriz(m: list[list[int]]) -> None:
    for fila in m:
        for n in fila:
            print(n, end=" ")
        print()


n_filas = int(input('Dime el número de filas: '))
n_cols = int(input('Dime el número de cols: '))

imprimir_matriz(matriz_aleatoria(n_filas, n_cols))