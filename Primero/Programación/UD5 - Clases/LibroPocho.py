class LibroPocho:
  
    def __init__(self, ISBN: str, titulo: str, autores: list[str], generos: list[str], n_palabras: int, precio_base: float) -> None:
        self.ISBN = ISBN
        self.titulo = titulo
        self.autores = autores
        self.generos = generos
        self.precio_venta = precio_base

        if n_palabras >= 0:
           self.n_palabras = n_palabras
        else:
           self.n_palabras = 0

        if precio_base >= 0:
           self.precio_base = round(precio_base, 2)
        else:
           self.precio_base = 0

        self.precio_venta += round(self.precio_base * 0.21, 2)

    def __eq__(self, other) -> bool:
       if isinstance(other, LibroPocho):
           return self.ISBN == other.ISBN
       return False

    def longitud(self) -> str:
       longitudes = ["Corto", "Mediano", "Largo"]
       if self.n_palabras < 10000:
           longitud = longitudes[0]
       elif self.n_palabras >= 10000 and self.n_palabras <= 40000:
           longitud = longitudes[1]
       else:
           longitud = longitudes[2]
       return longitud
    
    def aplicar_descuento(self, descuento: float) -> None:
       self.precio_venta -= - self.precio_venta * descuento

    def __str__(self):
       return (
           f"Título: {self.titulo}\n"
           f"ISBN: {self.ISBN}, "
           f"Autores: {self.autores}, "
           f"Géneros: {self.generos}, "
           f"Número de palabras: {self.n_palabras}, "
           f"Precio: {self.precio_venta}"
       )
