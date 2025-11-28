"""Ejercicio 6 (1 punto). Crea la función es_cuadrada(m: list) que recibe como parámetro de entrada una matriz. La función devuelve True si la matriz es cuadrada, False en otro caso. Una matriz es cuadrada si tiene el mismo número de filas que de columnas. Supón que la matriz que recibe como parámetro siempre es una matriz válida. 
"""

def es_cuadrada(m: list[list[int]]) -> bool:
    return len(m) == len(m[0])

matriz_cuadrada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matriz no cuadrada (2x3)
matriz_no_cuadrada = [
    [10, 11, 12],
    [13, 14, 15]
]

print(es_cuadrada(matriz_cuadrada))
print(es_cuadrada(matriz_no_cuadrada))