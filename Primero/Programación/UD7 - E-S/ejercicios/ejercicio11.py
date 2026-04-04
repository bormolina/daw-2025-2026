import json
from pathlib import Path


class Aportacion:

    def __init__(self, nombre: str, anio: int, importancia: str):
        self.nombre = nombre
        self.anio = anio
        self.importancia = importancia

    def __str__(self):
        return f"{self.nombre} ({self.anio}) - {self.importancia}"


class Matematico:

    def __init__(self, id: int, nombre: str, campo: str, aportacion: Aportacion):
        self.id = id
        self.nombre = nombre
        self.campo = campo
        self.aportacion = aportacion

    def __str__(self):
        return f"{self.nombre} [{self.campo}] -> {self.aportacion}"


if __name__ == "__main__":

    ruta = Path(__file__).parent.parent / "datos" / "gente-lista.json"

    matematicos = []

    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)
        
        for d in datos:
            datos_aportacion = d["aportacion"]
            aportacion = Aportacion(
                datos_aportacion["nombre"],
                datos_aportacion["anio"],
                datos_aportacion["importancia"]
            )

            m = Matematico(
                d["id"],
                d["nombre"],
                d["campo"],
                aportacion
            )

            matematicos.append(m)

    for m in matematicos:
        print(m)