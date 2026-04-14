import json
from pathlib import Path


class Habitat:
    def __init__(self, tipo: str, zona: str, clima: str) -> None:
        self.tipo = tipo
        self.zona = zona
        self.clima = clima


class Dinosaurio:
    def __init__(self, nombre: str, periodo: str, habitat: Habitat) -> None:
        self.nombre = nombre
        self.periodo = periodo
        self.habitat = habitat

    def __str__(self) -> str:
        return f"{self.nombre} ({self.periodo}) - {self.habitat.zona}"


if __name__ == "__main__":
    ruta = Path(__file__).parent / "datos" / "dinos.json"

    dinosaurios = []

    # Leer JSON
    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)

        for d in datos:
            nombre = d["nombre"]
            periodo = d["periodo"]

            h = d["habitat"]
            tipo = h["tipo"]
            zona = h["zona"]
            clima = h["clima"]

            habitat = Habitat(tipo, zona, clima)
            dinosaurio = Dinosaurio(nombre, periodo, habitat)

            dinosaurios.append(dinosaurio)

    # Crear diccionario: zona -> lista de nombres
    dinos_por_zona = {}

    for d in dinosaurios:
        zona = d.habitat.zona

        if zona not in dinos_por_zona:
            dinos_por_zona[zona] = []

        dinos_por_zona[zona].append(d.nombre)

    # Mostrar resultado
    print("Dinosaurios por zona:")
    for zona in dinos_por_zona:
        print(f"{zona}: {dinos_por_zona[zona]}")