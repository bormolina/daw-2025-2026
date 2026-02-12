from Cancion import Cancion
from random import shuffle

class Playlist:
    def __init__(self, id: int, nombre: str, canciones: list[Cancion] = []) -> None:
        self.id = id
        self.nombre = nombre
        if len(canciones) > 0:
            self.canciones = canciones

    def añadir_cancion(self, c: Cancion) -> None:
        self.canciones.append(c)
    
    def eliminar_cancion(self, id: int) -> bool:
        for c in self.canciones:
            if c.id == id:
                self.canciones.remove(c)
                return True
        return False
    
    def __str__(self) -> str:
        str_playlist = f"({self.id}) ## {self.nombre}\n"
        for c in self.canciones:
            str_playlist += f"{c}\n"
        return str_playlist
    

if __name__ == '__main__':
    from datetime import datetime

    c1 = Cancion(1, "Bohemian Rhapsody", ["Queen"], "A Night at the Opera",
                ["Rock"], 354, datetime(1975, 10, 31))

    c2 = Cancion(2, "Billie Jean", ["Michael Jackson"], "Thriller",
                ["Pop", "R&B"], 294, datetime(1983, 1, 2))

    c3 = Cancion(3, "Smells Like Teen Spirit", ["Nirvana"], "Nevermind",
                ["Grunge", "Rock"], 301, datetime(1991, 9, 10))

    c4 = Cancion(4, "Rolling in the Deep", ["Adele"], "21",
                ["Pop", "Soul"], 228, datetime(2010, 11, 29))

    c5 = Cancion(5, "Shape of You", ["Ed Sheeran"], "Divide",
                ["Pop"], 233, datetime(2017, 1, 6))

    c6 = Cancion(6, "Blinding Lights", ["The Weeknd"], "After Hours",
                ["Synthpop"], 200, datetime(2019, 11, 29))

    c7 = Cancion(7, "Despacito", ["Luis Fonsi", "Daddy Yankee"], "Vida",
                ["Reggaeton", "Pop latino"], 229, datetime(2017, 1, 13))

    c8 = Cancion(8, "Viva la Vida", ["Coldplay"], "Viva la Vida or Death and All His Friends",
                ["Alternative Rock"], 242, datetime(2008, 5, 25))

    c9 = Cancion(9, "Hotel California", ["Eagles"], "Hotel California",
                ["Rock"], 390, datetime(1976, 12, 8))

    c10 = Cancion(10, "Imagine", ["John Lennon"], "Imagine",
                ["Soft Rock"], 183, datetime(1971, 10, 11))
    
    p = Playlist(1, 'Prueba 1', [c1, c2, c3])
    print(p)
    p.añadir_cancion(c4)
    print(p)
    p.eliminar_cancion(2)
    print(p)

        