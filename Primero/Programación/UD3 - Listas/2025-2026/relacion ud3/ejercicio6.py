"""
 Crea la función suma_matrices(m1:list, m2:list) que dadas dos matrices m1 y m2 devuelva su suma
"""

def sumar_matrices(m1: list[list[float]], m2: list[list[float]]) -> list[list[float]]:
    m3 = m1.copy()

    for i, fila in enumerate(m1):
        for j, _ in enumerate(fila):
            m3[i][j] = m1[i][j] +  m2[i][j]
        
    return m3

matriz_1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matriz_2 = [
    [4, 3, 2, 1],
    [8, 7, 6, 5],
    [12, 11, 10, 9],
    [16, 15, 14, 13]
]

print(sumar_matrices(matriz_1, matriz_2))