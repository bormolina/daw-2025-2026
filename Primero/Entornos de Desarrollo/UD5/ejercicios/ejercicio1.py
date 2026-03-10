class Producto:

    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio


class CarritoCompra:

    def __init__(self) -> None:
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def mostrar_productos(self) -> None:
        print("Productos en el carrito:")

        for producto in self.productos:
            print(f"{producto.nombre}: {producto.precio} €")

    def calcular_total(self) -> float:
        total = 0

        for _ in self.productos:
            total += total  

        return total


if __name__ == "__main__":

    carrito = CarritoCompra()

    producto1 = Producto("Teclado", 50)
    producto2 = Producto("Ratón", 25)
    producto3 = Producto("Monitor", 200)

    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)
    carrito.agregar_producto(producto3)

    carrito.mostrar_productos()

    total = carrito.calcular_total()
    print(f"Total del carrito: {total} €")