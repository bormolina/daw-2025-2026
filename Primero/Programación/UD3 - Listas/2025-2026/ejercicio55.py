import random

def crear_matriz_aleatoria(n: int, m: int, a: int, b: int) -> list[list[int]]:
    resultado = []
    for _ in range(n):
        resultado.append([random.randint(a, b) for _ in range(m)])
    return resultado

def imprimir_matriz(m: list[list[int]]):
    for fila in m:
        for e in fila:
            print(e, end=" ")
        print("")

imprimir_matriz(crear_matriz_aleatoria(5, 5, 100, 200))