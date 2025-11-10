import random

lanzamientos = []
nVeces = 10

for _ in range(nVeces):
    n = random.random()
    if n > 0.5:
        lanzamientos.append("Cara")
    else:
        lanzamientos.append("Cruz")

print(lanzamientos)
    