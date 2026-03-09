class Producto:
   IVA = 0.21  # atributo estático (común a todos los productos)


   def __init__(self, nombre: str, precio_base: float):
       self.nombre = nombre
       self.precio_base = precio_base


   def precio_final(self) -> float:
       return self.precio_base * (1 + Producto.IVA)
   

