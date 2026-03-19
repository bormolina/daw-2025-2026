import random
from pathlib import Path


def leer_configuracion(nombre_archivo: str) -> dict:
    config = {}

    with open(nombre_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            clave, valor = linea.strip().split("=")
            config[clave] = valor

    return config


def jugar(config: dict):

    intentos = int(config["intentos"])
    minimo = int(config["numero_minimo"])
    maximo = int(config["numero_maximo"])
    pistas = config["pistas_mayor_menor"] == "si"

    numero_secreto = random.randint(minimo, maximo)

    print(f"Adivina el número entre {minimo} y {maximo}")

    while intentos > 0:
        intento = int(input("Tu número: "))
        
        if intento == numero_secreto:
            print("¡Correcto!")
            return

        intentos -= 1

        if pistas:
            if intento < numero_secreto:
                print("El número secreto es mayor")
            else:
                print("El número secreto es menor")

        print(f"Intentos restantes: {intentos}")

    print(f"Has perdido. El número era {numero_secreto}")


if __name__ == "__main__":
    nombre_archivo = Path(__file__).parent / "config-ej6.txt"
    config = leer_configuracion(nombre_archivo)
    jugar(config)