import json
from pathlib import Path


class Personaje:

    def __init__(self, id: int, nombre: str, arma: str, tecnicas: list[str]):
        self.id = id
        self.nombre = nombre
        self.arma = arma
        self.tecnicas = tecnicas

    def __str__(self):
        return f"{self.nombre} - arma: {self.arma} - tecnicas: {self.tecnicas}"


if __name__ == "__main__":

    ruta = Path(__file__).parent / "datos" / "tortugas-ninja2.json"

    tortugas = []

    with open(ruta, "r", encoding="utf-8") as f:

        datos = json.load(f)

        for d in datos:
            t = Personaje(
                d["id"],
                d["nombre"],
                d["arma"],
                d["tecnicas"]  # aquí ya es directamente una lista
            )
            tortugas.append(t)

    for t in tortugas:
        print(t)