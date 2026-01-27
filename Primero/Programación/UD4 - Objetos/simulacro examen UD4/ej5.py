from datetime import datetime
from Jugador import Jugador
from datos import get_datos

def elegir_capitan(jugadores: list[Jugador])->Jugador:
    capitan = jugadores[0]
    for j in jugadores[1:]:
        capitan = mas_capitan(capitan, j)

    return capitan

def mas_capitan(j1: Jugador, j2: Jugador) -> Jugador:
    
    if j1.pos_capitan == j2.pos_capitan:
        return j1 if j1.fecha_nacimiento < j2.fecha_nacimiento else j2
    
    if j1.pos_capitan == 0:
        return j2
    
    if j2.pos_capitan == 0:
        return j1
    
    return j1 if j1.pos_capitan < j2.pos_capitan else j2

def mostrar_alineacion(plantilla: list[Jugador]) -> None:

    def formatea_jugador(j: Jugador, capitan: bool) -> str:
        resultado = f'({j.dorsal}) {j.nombre}'
        if capitan:
            resultado += ' [c]'
        return resultado

    titulares = [j for j in plantilla if j.titular]
    capitan = elegir_capitan(titulares)
    posiciones = ['Portero', 'Defensa', 'Centrocampista', 'Delantero']

    for p in posiciones:
        jugadores_pos = [formatea_jugador(j, j.nombre == capitan.nombre) for j in titulares if j.posicion == p]
        print(f'{p}: {' -- '.join(jugadores_pos)}')


plantilla = get_datos()
mostrar_alineacion(plantilla)