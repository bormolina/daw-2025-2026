import random


class PiedraPapelTijera:

    def __init__(self):
        self.opciones = ["piedra", "papel", "tijera"]

    def jugar_ronda(self, eleccion_jugador: str) -> str:
        # Determina el ganador de la ronda siguiendo las reglas:
        # piedra gana a tijera
        # tijera gana a papel
        # papel gana a piedra

        eleccion_cpu = random.choice(self.opciones)

        print(f"Jugador: {eleccion_jugador}")
        print(f"CPU: {eleccion_cpu}")

        if eleccion_jugador == "piedra" and eleccion_cpu == "tijera":
            return "Jugador gana"

        if eleccion_jugador == "tijera" and eleccion_cpu == "papel":
            return "Jugador gana"

        if eleccion_jugador == "papel" and eleccion_cpu == "piedra":
            return "Jugador gana"

        return "CPU gana"


if __name__ == "__main__":

    juego = PiedraPapelTijera()

    while True:

        print("\nElige una opción:")
        print("1. piedra")
        print("2. papel")
        print("3. tijera")
        print("4. salir")

        opcion = input("Opción: ")

        if opcion == "4":
            break

        if opcion not in ["1", "2", "3"]:
            print("Opción inválida")
            continue

        eleccion = juego.opciones[int(opcion) - 1]

        resultado = juego.jugar_ronda(eleccion)

        print("Resultado:", resultado)