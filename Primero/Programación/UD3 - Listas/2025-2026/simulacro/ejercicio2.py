animales_domesticos = ["Perro", "Gato", "Conejo", "Hámster", "Loro", "Pez", "Tortuga", "Cobaya", "Hurón", "Canario"]

pesos_animales = [
    [5, 40],   # Perro (depende de la raza)
    [2, 8],    # Gato
    [1, 3],    # Conejo
    [0.08, 0.25], # Hámster
    [0.2, 1.5],   # Loro
    [0.1, 2],  # Pez (varía mucho según la especie)
    [0.5, 2],  # Tortuga (pequeñas domésticas)
    [0.7, 1.5],  # Cobaya
    [0.5, 2],  # Hurón
    [0.02, 0.06] # Canario
]

diferencias = [p[1]-p[0] for p in pesos_animales]
mayor_diferencia = animales_domesticos[diferencias.index(max(diferencias))]
print(f"El animal de mayor diferencia es: {mayor_diferencia}")