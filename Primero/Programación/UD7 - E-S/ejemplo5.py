import json
from pathlib import Path


class SerAntropomorficoQueSabeArtesMarciales:

    def __init__(self, id: int, nombre: str, especie: str, arma: str, color_antifaz: str):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.arma = arma
        self.color_antifaz = color_antifaz

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - arma: {self.arma}"


if __name__ == "__main__":

    ruta = Path(__file__).parent / "datos" / "tortugas-ninja.json"

    seres = []

    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)

        for d in datos:
            ser = SerAntropomorficoQueSabeArtesMarciales(
                d["id"],
                d["nombre"],
                d["especie"],
                d["arma"],
                d["color_antifaz"]
            )
            seres.append(ser)

    for s in seres:
        print(s)