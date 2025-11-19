matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

# Primera versión sin sum
sumatoria = 0

for fila in matriz:
    for n in fila:
        sumatoria += n

print(f"La suma total es: {sumatoria}")


# Segunda versión con sum
sumatoria = 0

for fila in matriz:
    sumatoria += sum(fila)

print(f"La suma total es: {sumatoria}")


