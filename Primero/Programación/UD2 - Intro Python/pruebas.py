import random

nDados = int(input("¿Cuántos dados quieres tirar?"))
for i in range(1, nDados+1):
    resultado = random.randint(1, 6)
    print(f"Tirada {i}, resultado: {resultado}")