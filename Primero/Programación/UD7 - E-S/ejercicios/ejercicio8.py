from pathlib import Path

class Producto:
    def __init__(self, id: int, nombre: str, precio: float, stock: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.id} - {self.nombre} | precio: {self.precio} | stock: {self.stock}"


if __name__ == "__main__":
    ruta = Path(__file__).parent.parent / "datos" / "productos.csv"
    productos = []

    with open(ruta, "r", encoding="utf-8") as f:
        next(f)  # saltar cabecera
        for linea in f:
            id, nombre, precio, stock = linea.strip().split(",")
            producto = Producto(int(id), nombre, float(precio), int(stock))
            productos.append(producto)

    for p in productos:
        print(p)