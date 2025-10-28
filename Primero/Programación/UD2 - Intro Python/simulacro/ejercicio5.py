import random

while True: 
    eleccion = input("¿Qué eliges (pares o nones)?: ")

    if eleccion == "pares" or eleccion == "nones":
        break
    else:
        print("Elección no válida. ")

while True:
    numDedos = int(input("¿Cuántos dedos sacas? "))

    if numDedos >= 0 and numDedos <=10:
        break
    else:
        print("Número de dedos erroneo")

dedosMaquina = random.randint(0, 10)
totalDedos = dedosMaquina + numDedos
print(f"Tu has sacado {numDedos} dedos y la máquina {dedosMaquina}")

if totalDedos % 2 == 0: #Si el total es par
    esPar = True
else:
    esPar = False

if (esPar and eleccion == "pares") or (not esPar and eleccion == "nones"):
    print("Has ganado") 
else:
    print("Has perdido")


