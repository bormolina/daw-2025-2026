from Videojuego2 import Videojuego2
from datetime import datetime


juegos = [
   Videojuego2("Final Fantasy VI", ["RPG"], datetime(1994, 4, 2), 9.5, 12, 49.99, 0.5),
   Videojuego2("The Legend of Zelda: Ocarina of Time", ["Aventura", "Acción"], datetime(1998, 11, 11), 9.9, 12, 39.99, 0.8),
   Videojuego2("Grand Theft Auto: San Andreas", ["Acción", "Mundo Abierto"], datetime(2004, 10, 3), 9.6, 18, 29.99, 4.7),
   Videojuego2("The Elder Scrolls V: Skyrim", ["RPG", "Mundo Abierto"], datetime(2011, 11, 3), 9.7, 18, 59.99, 12),
   Videojuego2("The Last of Us", ["Acción", "Aventura"], datetime(2013, 6, 14), 9.8, 18, 39.99, 45),
   Videojuego2("Bloodborne", ["Acción", "Souls-like"], datetime(2015, 3, 1), 9.7, 18, 19.99, 41),
   Videojuego2("The Legend of Zelda: Breath of the Wild", ["Aventura", "Mundo Abierto"], datetime(2017, 3, 3), 10, 12, 59.99, 13.4),
   Videojuego2("Red Dead Redemption 2", ["Acción", "Mundo Abierto"], datetime(2018, 10, 26), 9.9, 18, 59.99, 120),
   Videojuego2("Elden Ring", ["RPG", "Acción", "Souls-like"], datetime(2022, 2, 25), 9.8, 16, 59.99, 60),
   Videojuego2("Final Fantasy VII Rebirth", ["RPG", "Acción"], datetime(2025, 2, 10), 9.7, 16, 69.99, 100)
]

# Obtener el juego que más ocupa en disco
juego_peso_maximo = min(juegos, key=lambda juego: juego.precio_base)
print(f"El juego con mayor peso es '{juego_peso_maximo.nombre}' con {juego_peso_maximo.peso} GB.")
