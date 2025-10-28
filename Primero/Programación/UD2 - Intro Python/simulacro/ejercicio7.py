import random

def generarCarta() -> str:
    num = random.randint(1, 13)
    palo = random.randint(1, 4)

    if palo == 1:
        paloCarta = "Corazones"
    elif palo == 2: 
        paloCarta = "Picas"
    elif palo == 3: 
        paloCarta = "Tréboles"
    elif palo == 4: 
        paloCarta = "Diamantes"

    valor = str(num)

    if valor == "11":
        valor = "J"
    elif valor == "12":
        valor = "Q"
    elif valor == "13":
        valor = "K"

    return f"{valor} de {paloCarta}"

tirada = 1
numRepeticiones = 0
primeraVez = 0
cartaUsuario = input("Elige una carta: ")

while numRepeticiones < 2:
    carta = generarCarta()
    print(f"Tirada {tirada}: {carta}")
   

    if cartaUsuario == carta:
        if numRepeticiones == 0:
            primeraVez = tirada
        numRepeticiones = numRepeticiones + 1

    tirada = tirada + 1

print(f"La primera vez que se saco la carta {cartaUsuario} fue en la tirada {primeraVez}")