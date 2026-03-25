import json
from pathlib import Path


class Producto:

    def __init__(self, id: int, nombre: str, precio: float, stock: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} | precio: {self.precio} | stock: {self.stock}"


if __name__ == "__main__":

    ruta = Path(__file__).parent.parent / "datos" / "productos.json"

    productos = []

    with open(ruta, "r", encoding="utf-8") as f:

        datos = json.load(f)

        for d in datos:
            p = Producto(
                d["id"],
                d["nombre"],
                d["precio"],
                d["stock"]
            )

            productos.append(p)

    for p in productos:
        print(p)