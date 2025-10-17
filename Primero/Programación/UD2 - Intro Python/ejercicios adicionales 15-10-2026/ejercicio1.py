notaNumerica = int(input("Inserta una nota: "))

if notaNumerica >= 1 and notaNumerica <= 10:
    if notaNumerica>=1 and notaNumerica <= 4:
        print("Suspenso")
    elif notaNumerica == 5:
        print("Aprobado")
    elif notaNumerica == 6:
        print("Bien")
    elif notaNumerica == 7 or notaNumerica == 8:
        print("Notable")
    else:
        print("Sobresaliente")
else:
    print("Nota no válida")
