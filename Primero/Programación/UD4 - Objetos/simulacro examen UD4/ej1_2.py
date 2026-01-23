# Bibliotecas
from datetime import datetime
from Jugador import Jugador

# Funciones
def f2a(jugadores: list) -> Jugador:
    return max(jugadores, key = lambda j: j.partidos_jugados)

def f2b(jugadores: list) -> Jugador:
    return max(jugadores, key = lambda j: j.ratio_goles())

def f2c(jugadores: list) -> Jugador:
    return max([j for j in jugadores if j.posicion == 'Defensa'], key = lambda j: j.goles)

def f2d(jugadores: list) -> list:
    defensa = max([j for j in jugadores if j.posicion == 'Defensa'], key = lambda j: j.ratio_goles())
    centro = max([j for j in jugadores if j.posicion == 'Centrocampista'], key = lambda j: j.ratio_goles())
    delantero = max([j for j in jugadores if j.posicion == 'Delantero'], key = lambda j: j.ratio_goles())
    return [defensa, centro, delantero]

def f2e():
    pass

def f2f():
    pass

def f2g():
    pass

def f2h():
    pass


# Datos
atletico_madrid = [
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

atletico_madrid.append(Jugador("Ivo Grbić", 1, "Portero", 20, 0, 0, 1, 0, datetime(1996, 1, 18), datetime(2020, 8, 20), False))
atletico_madrid.append(Jugador("Reinaldo Mandanga", 23, "Defensa", 60, 2, 0, 15, 1, datetime(1994, 1, 21), datetime(2022, 1, 31), False))
atletico_madrid.append(Jugador("Pablo Motos", 24, "Centrocampista", 15, 0, 0, 5, 0, datetime(2003, 6, 15), datetime(2022, 12, 1), False))
atletico_madrid.append(Jugador("Menfis depeay", 19, "Delantero", 30, 10, 0, 6, 1, datetime(1994, 2, 13), datetime(2023, 1, 20), False))

# Lógica: Llamadas a las funciones

jugador_mas_partidos = f2a(atletico_madrid)
print(f'2a. El jugador con más partidos jugados es: {jugador_mas_partidos.nombre}')

mejor_ratio = f2b(atletico_madrid)
print(f'2b. El jugador con mejor ratio es: {mejor_ratio.nombre}')

defensa_pichichi = f2c(atletico_madrid)
print(f'2c. El defensa con más goles es {defensa_pichichi.nombre}')

mas_goleadores = f2d(atletico_madrid)
print('Los jugadores con mejor ratio goleador por posición son: ')
print(f'\tDefensa: {mas_goleadores[0].nombre}')
print(f'\tCentrocampista: {mas_goleadores[1].nombre}')
print(f'\tDelantero: {mas_goleadores[2].nombre}')



