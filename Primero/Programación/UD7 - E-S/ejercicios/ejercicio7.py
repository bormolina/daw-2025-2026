import random
from pathlib import Path


def leer_configuracion(nombre_archivo: str) -> dict:
    config = {}
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            clave, valor = linea.strip().split("=")
            config[clave] = valor

    return config


def jugar(tablas: list[int], preguntas):
    contador = 0

    while preguntas == "infinito" or contador < preguntas:

        n = random.choice(tablas)
        m = random.randint(1, 10)

        respuesta = int(input(f"{n} x {m} = ? "))

        if respuesta == n * m:
            print("Correcto")
        else:
            print(f"Incorrecto. La respuesta era {n*m}")

        contador += 1


if __name__ == "__main__":
    nombre_archivo = Path(__file__).parent / "config-ej7.txt"
    config = leer_configuracion(nombre_archivo)
    tablas = [int(x) for x in config["tablas"].split(",")]
    preguntas_cfg = config["preguntas"]

    if preguntas_cfg != "infinito":
        preguntas = int(preguntas_cfg)
    else:
        preguntas = "infinito"

    jugar(tablas, preguntas)