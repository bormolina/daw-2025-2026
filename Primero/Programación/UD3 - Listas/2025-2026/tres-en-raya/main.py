from funcs import imprimir_tablero, insertar_jugada, ia, estado

tablero = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

imprimir_tablero(tablero)
turno = 0

while True:
    insertar_jugada(tablero)
    imprimir_tablero(tablero)
    
    estado_partida = estado(tablero)
    if estado_partida == 1:
        print("HAS GANADO!!!!")
        break

    if turno == 5:
        print("Has empatado")
    
    input("La IA juega...")
    ia(tablero)

    estado_partida = estado(tablero)
    imprimir_tablero(tablero)

    if estado_partida == -1:
        print("HAS PERDIDO!!!!")
        break

    turno += 1

