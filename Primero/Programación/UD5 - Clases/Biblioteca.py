from Libro import Libro

class Biblioteca:
    def __init__(
        self,
        id_biblioteca: int,
        nombre: str,
        direccion: str,
        libros: list[Libro] | None = None
    ):
        self.id_biblioteca = id_biblioteca
        self.nombre = nombre
        self.direccion = direccion

        # Si no se pasa lista, se crea una vacía
        if libros is None:
            self.libros: list[Libro] = []
        else:
            self.libros = libros

    def añadir_libro(self, libro: Libro) -> None:
        self.libros.append(libro)

    def eliminar_libro_por_isbn(self, isbn: str) -> bool:
        for libro in self.libros:
            if libro.ISBN == isbn:
                self.libros.remove(libro)
                return True
        return False

    def buscar_por_isbn(self, isbn: str) -> Libro | None:
        for libro in self.libros:
            if libro.ISBN == isbn:
                return libro
        return None

    def contar_libros(self) -> int:
        return len(self.libros)
    
    def buscar_libros_por_palabra(self, palabra: str) -> list[Libro]:
        resultado = []
        for libro in self.libros:
            if palabra in libro:
                resultado.append(libro)
        return resultado

    def buscar_libros_por_autor(self, autor: str) -> list[Libro]:
        resultado = []
        for libro in self.libros:
            if autor in libro.autores:
                resultado.append(libro)
        return resultado

    def buscar_libros_por_precio_maximo(self, precio_max: float) -> list[Libro]:
        resultado = []
        for libro in self.libros:
            if libro.precio_venta <= precio_max:
                resultado.append(libro)
        return resultado
    
    def libro_mas_largo(self) -> Libro | None:
        if len(self.libros) == 0:
            return None
        return max(self.libros)

    def libro_mas_corto(self) -> Libro | None:
        if len(self.libros) == 0:
            return None
        return min(self.libros)

    def libros_ordenados_por_longitud(self) -> list[Libro]:
        return sorted(self.libros)

    def libro_mas_caro(self) -> Libro | None:
        if len(self.libros) == 0:
            return None
        return max(self.libros, key=lambda l: l.precio_venta)

    def libro_mas_barato(self) -> Libro | None:
        if len(self.libros) == 0:
            return None
        return min(self.libros, key=lambda l: l.precio_venta)

    def libros_ordenados_por_precio(self) -> list[Libro]:
        return sorted(self.libros, key=lambda l: l.precio_venta)

    def __str__(self) -> str:
        res = f"Biblioteca #{self.id_biblioteca}\n"
        res += f"Nombre: {self.nombre}\n"
        res += f"Dirección: {self.direccion}\n"
        res += f"Número de libros: {len(self.libros)}\n"
        res += "Catálogo:\n"
        for libro in self.libros:
            res += f"- {libro.titulo} ({libro.ISBN})\n"
        return res