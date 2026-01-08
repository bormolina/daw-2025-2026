# PRIMERO DEFINIMOS LAS FUNCIONES
def diagonales(m: list[list[int]]) -> tuple[list[int], list[int]]:
    diagonal_principal = []
    diagonal_secundaria = []

    for i, fila in enumerate(m):
        tam = len(fila)
        diagonal_principal.append(fila[i])
        diagonal_secundaria.append(fila[tam-i-1])       
        
    return (diagonal_principal, diagonal_secundaria)

# DESPUÉS LOS DATOS
matriz = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15,16]
]

# FINALMENTE EL PROGRAMA
print(diagonales(matriz))

