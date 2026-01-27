# Bibliotecas
from datetime import datetime
from Jugador import Jugador
from datos import get_datos

def tiempo_pasado(nacimiento: datetime) -> int:
   hoy = datetime.now()
   # Calcular la diferencia de años teniendo en cuenta si ya pasó el cumpleaños este año
   edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
   return edad


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

def f2e(jugadores: list[Jugador]) -> list:
    return [j for j in jugadores if tiempo_pasado(j.fecha_nacimiento) <= 28]

def f2f(jugadores: list[Jugador]) -> list[Jugador]:
    return [j for j in jugadores if j.goles == 0 and j.posicion != 'Portero']

def f2g(jugadores: list[Jugador]) -> list[Jugador]:
    return [j for j in jugadores if j.fecha_alta.year <= 2015]

def f2h(jugadores: list[Jugador]) -> list[Jugador]:
    menos_goles_delantero = min([j.goles for j in jugadores if j.posicion == 'Delantero'])
    return [j for j in jugadores if j.goles > menos_goles_delantero and j.posicion == 'Centrocampista']


# Datos
atletico_madrid = get_datos()

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

mas_jovenes_28 = f2e(atletico_madrid)
print(f'Los jugadores con 28 años o menos son: {[j.nombre for j in mas_jovenes_28]}')

mantas = f2f(atletico_madrid)
print(f'Los jugadores que nunca han marcado gol y no son porteros son: {[j.nombre for j in mantas]}')

antiguos = f2g(atletico_madrid)
print(f'Los jugadores que llevan desde el 2015 o antes en el equipo son: {[j.nombre for j in antiguos]}')

centros_goleadores = f2h(atletico_madrid)
print(f'Los centrocampistas que han metido más goles que algún delantero son: {[j.nombre for j in centros_goleadores]}')