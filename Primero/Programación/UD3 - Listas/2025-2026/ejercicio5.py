import random

# Esto genera mil números aleatorios entre 0 y 10
# Confiad en mi que lo hace, al final del tema os explico
aleatorios = [random.randint(0, 10) for _ in range(1000)]

menor = aleatorios[0]

for n in aleatorios:
    if n < menor:
        menor = n

print(f"El menor es {menor}")

