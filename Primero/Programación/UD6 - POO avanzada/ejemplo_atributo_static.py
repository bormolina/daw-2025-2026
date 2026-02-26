class Producto:
    IVA = 0.21  # atributo estático (común a todos los productos)

    def __init__(self, nombre: str, precio_base: float):
        self.nombre = nombre
        self.precio_base = precio_base

    def precio_final(self) -> float:
        return self.precio_base * (1 + Producto.IVA)


p1 = Producto("Teclado", 100)
p2 = Producto("Ratón", 50)

print(p1.precio_final())
print(p2.precio_final())

# Cambia el IVA global
Producto.IVA = 0.23

print(p1.precio_final())
print(p2.precio_final())