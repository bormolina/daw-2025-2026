from funcs import imprimir_tablero, insertar_jugada, ia

tablero = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

imprimir_tablero(tablero)

while True:
    insertar_jugada(tablero)
    imprimir_tablero(tablero)
    ia(tablero)
    input("La IA juega: ")
    imprimir_tablero(tablero)
