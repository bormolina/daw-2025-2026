from datetime import datetime
from Jugador import Jugador

def get_datos() -> list[Jugador]:
    return [
   Jugador("Jan Oblak", 13, "Portero", 300, 0, 3, 10, 1, datetime(1993, 1, 7), datetime(2014, 7, 16), True),
   Jugador("José María Giménez", 2, "Defensa", 250, 10, 2, 40, 2, datetime(1995, 1, 20), datetime(2013, 4, 1), True),
   Jugador("Stefan Savic", 15, "Defensa", 230, 5, 0, 50, 3, datetime(1991, 1, 8), datetime(2015, 7, 20), True),
   Jugador("Mario Hermoso", 22, "Defensa", 150, 0, 0, 30, 1, datetime(1995, 6, 18), datetime(2019, 7, 18), True),
   Jugador("Nahuel Molina", 16, "Defensa", 50, 3, 0, 10, 0, datetime(1998, 4, 6), datetime(2022, 7, 28), True),
   Jugador("Koke Resurrección", 6, "Centrocampista", 550, 50, 1, 80, 2, datetime(1992, 1, 8), datetime(2009, 9, 19), True),
   Jugador("Marcos Llorente", 14, "Centrocampista", 200, 30, 0, 40, 1, datetime(1995, 1, 30), datetime(2019, 7, 1), True),
   Jugador("Rodrigo De Paul", 5, "Centrocampista", 70, 10, 0, 20, 0, datetime(1994, 5, 24), datetime(2021, 7, 12), True),
   Jugador("Saúl Ñíguez", 8, "Centrocampista", 350, 40, 0, 60, 3, datetime(1994, 11, 21), datetime(2012, 3, 8), True),
   Jugador("Antoine Griezmann", 7, "Delantero", 450, 180, 5, 40, 2, datetime(1991, 3, 21), datetime(2014, 7, 28), True),
   Jugador("Álvaro Morata", 9, "Delantero", 300, 110, 4, 50, 1, datetime(1992, 10, 23), datetime(2020, 7, 1), True)
]

def get_datos_seleccion() -> list[Jugador]:
    return [
   Jugador("Unai Simón", 23, "Portero", 40, 0, 1, 5, 0, datetime(1997, 6, 11), datetime(2020, 9, 1), True),
   Jugador("Dani Carvajal", 2, "Defensa", 80, 2, 1, 15, 1, datetime(1992, 1, 11), datetime(2014, 9, 4), True),
   Jugador("Aymeric Laporte", 14, "Defensa", 35, 3, 0, 5, 0, datetime(1994, 5, 27), datetime(2021, 5, 11), True),
   Jugador("Pau Torres", 4, "Defensa", 30, 2, 0, 3, 0, datetime(1997, 1, 16), datetime(2019, 11, 15), True),
   Jugador("Jordi Alba", 18, "Defensa", 90, 10, 1, 20, 2, datetime(1989, 3, 21), datetime(2012, 7, 5), True),
   Jugador("Carlos Soler", 19, "Centrocampista", 18, 3, 0, 2, 0, datetime(1997, 1, 2), datetime(2021, 9, 2), True),
   Jugador("Pedri", 16, "Centrocampista", 25, 5, 0, 2, 0, datetime(2002, 11, 25), datetime(2020, 9, 25), True),
   Jugador("Gavi", 9, "Centrocampista", 20, 4, 0, 3, 0, datetime(2004, 8, 5), datetime(2021, 10, 6), True),
   Jugador("Saúl Ñíguez", 8, "Centrocampista", 350, 40, 0, 60, 3, datetime(1994, 11, 21), datetime(2012, 3, 8), True),
   Jugador("Álvaro Morata", 9, "Delantero", 300, 120, 1, 50, 1, datetime(1992, 10, 23), datetime(2020, 7, 1), True),
   Jugador("Ferran Torres", 11, "Delantero", 45, 15, 0, 5, 0, datetime(2000, 2, 29), datetime(2020, 9, 3), True),
   Jugador("David Raya", 13, "Portero", 5, 0, 0, 1, 0, datetime(1995, 9, 15), datetime(2022, 3, 15), False),
   Jugador("Íñigo Martínez", 3, "Defensa", 35, 2, 0, 4, 0, datetime(1991, 5, 17), datetime(2013, 8, 14), False),
   Jugador("Koke Resurrección", 6, "Centrocampista", 550, 50, 1, 80, 2, datetime(1992, 1, 8), datetime(2009, 9, 19), False),
   Jugador("Borja Iglesias", 22, "Delantero", 10, 5, 0, 1, 0, datetime(1993, 1, 17), datetime(2022, 9, 24), False)
]
