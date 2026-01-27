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


plantilla = get_datos()
capitan = elegir_capitan(plantilla)
print(capitan)