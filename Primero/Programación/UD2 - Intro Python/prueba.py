import random

def lanzarDados(nDados: int):
    for i in range(1, nDados+1):
        tirada = random.randint(1, 6)
        print(f"Tirada {i} -- resultado: {tirada}")
   
lanzarDados(500)