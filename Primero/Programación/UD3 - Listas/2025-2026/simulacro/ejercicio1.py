animales_domesticos = ["Perro", "Gato", "Conejo", "Hámster", "Loro", "Pez", "Tortuga", "Cobaya", "Hurón", "Canario"]

pesos_animales = [10, 4, 2, 0.1, 0.3, 0.2, 1.5, 1, 1.2, 0.05]  

# apartado a)
pos_min = pesos_animales.index(min(pesos_animales))
print(f"El animale que menos pesa es el {animales_domesticos[pos_min]}")

# apartado b)
media = sum(pesos_animales) / len(pesos_animales)
for i, peso in enumerate(pesos_animales):
    if peso > media:
        print(f"El animal {animales_domesticos[i]} pesa {pesos_animales[i]} más que la media {media}") 