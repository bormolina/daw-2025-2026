class Producto:
    def __init__(self, nombre: str, precio: float, categoria: str) -> None:
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self) -> str:
        return f"{self.nombre} ({self.categoria}) - {self.precio:.2f} €"


class Tienda:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.catalogo: list[Producto] = []
        self.carrito: list[Producto] = []
        self.descuentos: dict[str, float] = {
            "informatica": 0.10,
            "hogar": 0.05,
            "libros": 0.15
        }

    def agregar_al_catalogo(self, producto: Producto) -> None:
        self.catalogo.append(producto)

    def mostrar_catalogo(self) -> None:
        print(f"\nCatálogo de {self.nombre}")
        print("-" * 40)
        for i, producto in enumerate(self.catalogo, start=1):
            print(f"{i}. {producto}")

    def buscar_por_categoria(self, categoria: str) -> list[Producto]:
        resultados: list[Producto] = []
        for producto in self.catalogo:
            if producto.categoria == categoria:
                resultados.append(producto)
        return resultados

    def anadir_al_carrito(self, nombre_producto: str) -> bool:
        for producto in self.catalogo:
            if producto.nombre.lower() == nombre_producto.lower():
                self.carrito.append(producto)
                return True
        return False

    def mostrar_carrito(self) -> None:
        print("\nCarrito actual")
        print("-" * 40)
        if not self.carrito:
            print("El carrito está vacío")
            return

        for producto in self.carrito:
            print(producto)

    def calcular_total_sin_descuento(self) -> float:
        total = 0.0
        for producto in self.carrito:
            total += producto.precio
        return total

    def calcular_total_con_descuento(self) -> float:
        total = 0.0
        for producto in self.carrito:
            descuento = self.descuentos.get(producto.categoria, 0.0)
            precio_final = producto.precio * (1 - descuento)
            total += precio_final
        return total

    def calcular_gasto_por_categoria(self) -> dict[str, float]:
        resumen: dict[str, float] = {}

        for producto in self.carrito:
            if producto.categoria not in resumen:
                resumen[producto.categoria] = 0.0

            descuento = self.descuentos.get(producto.categoria, 0.0)
            resumen[producto.categoria] += producto.precio * (1 - descuento)

        return resumen

    def imprimir_resumen(self) -> None:
        print("\nResumen del pedido")
        print("-" * 40)

        total_sin = self.calcular_total_sin_descuento()
        total_con = self.calcular_total_con_descuento()

        print(f"Total sin descuento: {total_sin:.2f} €")
        print(f"Total con descuento: {total_con:.2f} €")

        print("\nGasto por categoría:")
        resumen = self.calcular_gasto_por_categoria()
        for categoria, cantidad in resumen.items():
            print(f"- {categoria}: {cantidad:.2f} €")


if __name__ == "__main__":
    tienda = Tienda("Borjotienda")

    tienda.agregar_al_catalogo(Producto("Teclado mecánico", 80, "informatica"))
    tienda.agregar_al_catalogo(Producto("Ratón gaming", 35, "informatica"))
    tienda.agregar_al_catalogo(Producto("Lámpara", 22, "hogar"))
    tienda.agregar_al_catalogo(Producto("Sartén", 28, "hogar"))
    tienda.agregar_al_catalogo(Producto("Libro de Python", 30, "libros"))
    tienda.agregar_al_catalogo(Producto("Cuaderno", 6, "papeleria"))

    tienda.mostrar_catalogo()

    tienda.anadir_al_carrito("Teclado mecánico")
    tienda.anadir_al_carrito("Libro de Python")
    tienda.anadir_al_carrito("Lámpara")

    tienda.mostrar_carrito()
    tienda.imprimir_resumen()

    print("\nCálculo adicional")
    print("-" * 40)

    # Variable definida muy al principio del bloque final


    total = tienda.calcular_total_con_descuento()
    n_productos = len(tienda.carrito)

    print(f"Total actual del carrito: {total:.2f} €")
    print(f"Número de productos considerado: {n_productos}")
    promedio = total / n_productos
    print(f"Precio medio por producto: {promedio:.2f} €")