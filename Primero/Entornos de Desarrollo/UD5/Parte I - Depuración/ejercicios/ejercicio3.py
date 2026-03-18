import random

"""
    HE VUELTO, ESTA VEZ EN FORMA DE EJERCICIO DE ENTORNOS DE DESARROLLO
    NO OS LIBRAREIS DE MI
"""
def jugar_partida(vidas: int) -> int:

    print("\nComienza la partida")

    while vidas > 0:

        a = random.randint(1, 10)
        b = random.randint(1, 10)

        print(f"\n¿Cuánto es {a} + {b}?")

        respuesta = int(input("Respuesta: "))

        if respuesta == a + b:
            print("Correcto")
        else:
            vidas -= 1
            print(f"Incorrecto. Te quedan {vidas} vidas")

    print("Has perdido todas las vidas")
    return vidas


if __name__ == "__main__":

    vidas = 3

    while True:

        print("\n--- MENÚ ---")
        print("1. Jugar")
        print("2. Configurar vidas")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":

            vidas = jugar_partida(vidas)

        elif opcion == "2":

            vidas = int(input("Introduce el número de vidas: "))
            print(f"Vidas configuradas: {vidas}")

        elif opcion == "3":

            print("Hasta luego")
            break

        else:
            print("Opción no válida")