alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

medias = []

for fila in alumnos:
    notas = fila[1:]
    medias.append(sum(notas) / len(notas))

media_clase = sum(medias) / len(medias)
print(f"La media de la clase es {media_clase}")