from datetime import datetime


class Cancion:
    
    def __init__(self, id: int, titulo: str, artistas: list[str], album: str, generos: list[str], duración: int, fecha_salida: datetime) -> None:
        self.id = id
        self.titulo = titulo
        self.artistas = artistas
        self.album = album
        self.generos = generos
        self.duracion = duración
        self.fecha_salida = fecha_salida

    
    def __eq__(self, other) -> bool:
        if isinstance(other, Cancion):
            return self.id == other.id
        return False
    
    def __str__(self) -> str:
        if len(self.artistas) > 1:
            str_artistas = ", ".join(self.artistas[:-1])
            str_artistas += f' y {self.artistas[-1]}'
        else:
            str_artistas = self.artistas[0]
        return f'{self.titulo} -- {str_artistas}'
    
# Hago las pruebas de que la clase funciona    
if __name__ == "__main__":
    c = Cancion(1, 'Monster', ['Skrillex', 'Julio Iglesias', 'Shakira'], 'Happy Unicorn',['Pop', 'K-pop'], 230, datetime(2026, 2, 11))

    print(c)
        