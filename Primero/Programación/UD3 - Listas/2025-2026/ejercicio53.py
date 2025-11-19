alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

for alumno in alumnos:
    if not min(alumno[1:]) >= 5:
        print(f"{alumno[0]} tiene alguna suspensa")