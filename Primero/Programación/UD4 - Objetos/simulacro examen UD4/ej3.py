from datetime import datetime
from Jugador import Jugador
from datos import get_datos, get_datos_seleccion


atletico = [j for j in get_datos()] 
seleccion = [j for j in get_datos_seleccion()]


# Apartado A
atletico_nombres = [j.nombre for j in atletico]
seleccion_nombres = [j.nombre for j in seleccion]
atletico_seleccion = list(set(atletico_nombres) & set(seleccion_nombres))
print('Los jugadores del atlético que van a la selección son: ')
for j in atletico_seleccion:
    print(j)

# Apartado B
atletico_titulares_nombres = [j.nombre for j in atletico if j.titular]
seleccion_titulares_nombres = [j.nombre for j in seleccion if j.titular]
atletico_seleccion_titulares = list(set(atletico_titulares_nombres) & set(seleccion_titulares_nombres))
print('Los jugadores del atlético que van a la selección son: ')
for j in atletico_seleccion_titulares:
    print(j)
