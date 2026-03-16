from pathlib import Path


class Personaje:

    def __init__(self, id: int, nombre: str, especie: str, arma: str, color_antifaz: str):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.arma = arma
        self.color_antifaz = color_antifaz

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - arma: {self.arma}"


if __name__ == "__main__":

    ruta_csv = Path(__file__).parent / "datos" / "tortugas-ninja.csv"

    personajes = []

    with open(ruta_csv, "r", encoding="utf-8") as f:
        next(f)  # saltamos la cabecera
        for linea in f:
            id, nombre, especie, arma, color = linea.strip().split(",")
            personaje = Personaje(int(id), nombre, especie, arma, color)
            personajes.append(personaje)

    for p in personajes:
        print(p)