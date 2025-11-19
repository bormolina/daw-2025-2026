matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, 5]
]


# versión sin index
# devolviendo el último 5
pos_fila = pos_columna = None

for i, fila in enumerate(matriz):
    for j, n in enumerate(fila):
        if n == 5:
            pos_fila = i
            pos_columna = j

print(f"La posición del último 5 es: {pos_fila} {pos_columna}")

# versión sin index
# devolviendo el primer 5
pos_fila = pos_columna = None
encontrado = False

for i, fila in enumerate(matriz):
    if encontrado:
        break
    for j, n in enumerate(fila):
        if n == 5:
            pos_fila = i
            pos_columna = j
            encontrado = True
            break

print(f"La posición del primer 5 es: {pos_fila} {pos_columna}")

# versión con index
pos_fila = pos_columna = None

for i, fila in enumerate(matriz):
    if fila.count(5) > 0:
        pos_fila = i
        pos_columna = fila.index(5)
        break

print(f"La posición del primer 5 es: {pos_fila} {pos_columna}")

