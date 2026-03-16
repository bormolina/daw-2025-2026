import json
from pathlib import Path


class Arma:

    def __init__(self, id: int, nombre: str, ataque: int, tipo: str):
        self.id = id
        self.nombre = nombre
        self.ataque = ataque
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} (ataque {self.ataque}, tipo {self.tipo})"


class Personaje:

    def __init__(self, id: int, nombre: str, especie: str, arma: Arma):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.arma = arma

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - arma: {self.arma}"


if __name__ == "__main__":

    ruta = Path(__file__).parent / "datos" / "tortugas-ninja3.json"

    personajes = []

    with open(ruta, "r", encoding="utf-8") as f:

        datos = json.load(f)

        for d in datos:

            arma_data = d["arma"]

            arma = Arma(
                arma_data["id"],
                arma_data["nombre"],
                arma_data["ataque"],
                arma_data["tipo"]
            )

            personaje = Personaje(
                d["id"],
                d["nombre"],
                d["especie"],
                arma
            )

            personajes.append(personaje)

    for p in personajes:
        print(p)