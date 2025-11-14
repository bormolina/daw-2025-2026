import random


# Ejemplo de filtrado
# Dada una lista de números quédate solo con los números pares
nums = [3, 4, 5, 6, 3, 11, 33, 44, 64]
nums_pares = []
for n in nums:
    if n % 2 == 0:
        nums_pares.append(n)
print(nums_pares)

nums_pares2 = [n for n in nums if n % 2 == 0]
print(nums_pares2)


# Otro ejemplo de filtrado
# Dada una lista de palabras quédate con aquellas cuya longitud sea mayor que 5
palabras = ["perro", "gato", "rinoceronte", "pez", "canario"]
palabras_largas = []
for palabra in palabras:
    if len(palabra) > 5:
        palabras_largas.append(palabra)
print(palabras_largas)

palabras_largas = [p.capitalize() for p in palabras if len(p)>5]


# Ejemplo de modificación de elementos de una lista
# Dada una lista de números, calcula el cuadrado de todos ellos
nums = [3, 4, 5, 6, 3, 11, 33, 44, 64]
nums_cuadrado = []
for n in nums:
    nums_cuadrado.append(n*n)
print(nums_cuadrado)

nums_cuadrado = [n*n for n in nums]


# Otro ejemplo de modificación
# Dada una lista de palabras poner en mayúscula la primera letra de todas
palabras = ["perro", "gato", "rinoceronte", "pez", "canario"]
palabras_capitalizadas = []
for palabra in palabras:
    palabras_capitalizadas.append(palabra.capitalize())
print(palabras_capitalizadas)

palabras_capitalizadas = [p.capitalize() for p in palabras]
