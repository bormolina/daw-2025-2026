"""
Crea una función que reciba por parámetro una matriz. La función deberá devolver una lista de dos elementos: el primero de ellos con el número de filas de la matriz y el segundo con el número de columnas de la matriz. No hagas comprobaciones de que lo que le entra sea o no una matriz, supón que siempre recibirá por parámetro una matriz válida. 
"""

def dimension(m: list[list[int]]) -> list[int]:
    if len(m) == 0:
        return [0, 0]
    else:
        return [len(m), len(m[0])]


print(dimension([[1, 2, 3], [3, 4, 5]]))
