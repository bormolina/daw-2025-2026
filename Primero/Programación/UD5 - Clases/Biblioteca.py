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

    def __str__(self) -> str:
        res = f"Biblioteca #{self.id_biblioteca}\n"
        res += f"Nombre: {self.nombre}\n"
        res += f"Dirección: {self.direccion}\n"
        res += f"Número de libros: {len(self.libros)}\n"
        res += "Catálogo:\n"
        for libro in self.libros:
            res += f"- {libro.titulo} ({libro.ISBN})\n"
        return res