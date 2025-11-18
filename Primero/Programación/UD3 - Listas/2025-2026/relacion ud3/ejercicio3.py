import random

def emparejar(elementos: list[str]):
    while(len(elementos) > 0):
        aleatorio = random.randint(0, len(elementos)-1)
        elemento1 = elementos.pop(aleatorio)
        aleatorio = random.randint(0, len(elementos)-1)
        elemento2 = elementos.pop(aleatorio)
        print(f"{elemento1}\t vs \t{elemento2}")

tenistas_top_8 = [
    "Jannik Sinner",      # 11,330 puntos
    "Alexander Zverev",   # 8,135 puntos
    "Carlos Alcaraz",     # 7,410 puntos
    "Taylor Fritz",       # 4,900 puntos
    "Casper Ruud",        # 4,480 puntos
    "Daniil Medvedev",    # 3,930 puntos
    "Novak Djokovic",     # 3,900 puntos
    "Álex de Miñaur"      # 3,735 puntos
]

elementos = emparejar(tenistas_top_8.copy())