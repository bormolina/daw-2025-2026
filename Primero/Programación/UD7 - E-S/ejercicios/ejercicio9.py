from pathlib import Path


class PersonajeSupernenas:

    def __init__(self, id: int, nombre: str, color: str, superpoder: str, caracteristica: str):
        self.id = id
        self.nombre = nombre
        self.color = color
        self.superpoder = superpoder
        self.caracteristica = caracteristica

    def __str__(self) -> str:
        return f"{self.nombre} ({self.color}) - poder: {self.superpoder} - {self.caracteristica}"


if __name__ == "__main__":

    ruta = Path(__file__).parent.parent / "datos" / "super-nenas.csv"
    personajes = []

    with open(ruta, "r", encoding="utf-8") as f:

        next(f)  # saltar cabecera

        for linea in f:
            id, nombre, color, superpoder, caracteristica = linea.strip().split(",")

            nombre, superpoder, caracteristica = [atributo.replace("_", " ") for atributo in [nombre, superpoder, caracteristica]]

            p = PersonajeSupernenas(
                int(id),
                nombre,
                color,
                superpoder,
                caracteristica
            )

            personajes.append(p)

    for p in personajes:
        print(p)