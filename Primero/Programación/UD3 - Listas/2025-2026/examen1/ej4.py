def generar_matriz(filas: int, columnas: int, inicial: int) -> list[list[int]]:
    m = []
    v = inicial
    for i in range(filas):
        m.append([])
        for _ in range(columnas):
            m[i].append(v)
            v += 1
    return m


print(generar_matriz(4, 4, 5))

