"""
Crea una lista con 1000 números aleatorios entre 1 y 100. Encuentra el número que MÁS veces se repite
"""

import random

nums = []

for _ in range(0, 1000):
    nums.append(random.randint(1, 100))

# Partimos de la hipótesis de que el primero es el que más se repite
mas_repes = nums[0]

# Y ahora nuestro trabajo comprobar si es cierta
for n in nums:
    if nums.count(n) > nums.count(mas_repes):
        mas_repes = n

print(f"El númro que más veces se repite es: {n} que se repite {nums.count(n)} veces")

