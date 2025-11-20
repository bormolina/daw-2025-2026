from random import randint

def pedir_coordenada(mensaje: str, inicio: int, final: int) -> int:
    while True:
        coord = int(input(mensaje))
        if coord >= inicio and coord <= final:
            break
        else:
            print("Número fuera de rango")
    return coord

def generar_coordenada(pos: int) -> tuple[int]:
    return (pos // 3, pos % 3)

def imprimir_tablero(tablero: list[list[int]]):
    for fila in tablero:
        for casilla in fila:
            signo = "-"
            if casilla == 1:
                signo = "X"
            elif casilla == -1:
                signo = "O"
            print(signo, end=" ")
        print("")

def insertar_jugada(tablero: list[list[int]]):

    fila = pedir_coordenada("Inserta una fila: ", 0, 2)
    col = pedir_coordenada("Inserta una columna: ", 0, 2)
    
    while tablero[fila][col] != 0: # mientra la posición esté ocupada
        print("La posición ya está ocupada")
        fila = pedir_coordenada("Inserta una fila", 0, 2)
        col = pedir_coordenada("Inserta una columna", 0, 2)

    tablero[fila][col] = 1

def ia(tablero: list[list[int]]):
    fila, col = generar_coordenada(randint(0, 8))

    while tablero[fila][col] != 0: # mientra la posición esté ocupada
        fila, col = generar_coordenada(randint(0,8))
    
    tablero[fila][col] = -1

    