from datetime import datetime

class Jugador:
   def __init__(self, nombre: str, dorsal: int, posicion: str, partidos_jugados: int, goles: int,
                pos_capitan: int, n_tarjetas_amarillas: int, n_tarjetas_rojas: int,
                fecha_nacimiento: datetime, fecha_alta: datetime, titular: bool):
       self.nombre = nombre
       self.dorsal = dorsal
       self.posicion = posicion
       self.partidos_jugados = partidos_jugados
       self.goles = goles
       self.pos_capitan = pos_capitan
       self.n_tarjetas_amarillas = n_tarjetas_amarillas
       self.n_tarjetas_rojas = n_tarjetas_rojas
       self.fecha_nacimiento = fecha_nacimiento
       self.fecha_alta = fecha_alta
       self.titular = titular
  
   def ratio_goles(self):
       return self.goles / self.partidos_jugados if self.partidos_jugados > 0 else 0
  
   def __str__(self):
       return (f"Nombre: {self.nombre}, Dorsal: {self.dorsal}, Posición: {self.posicion}, "
               f"Partidos Jugados: {self.partidos_jugados}, Goles: {self.goles}, "
               f"Posición Capitán: {self.pos_capitan}, Tarjetas Amarillas: {self.n_tarjetas_amarillas}, "
               f"Tarjetas Rojas: {self.n_tarjetas_rojas}, Titular: {'Sí' if self.titular else 'No'}, "
               f"Fecha de Nacimiento: {self.fecha_nacimiento.strftime('%d-%m-%Y')}, "
               f"Fecha de Alta: {self.fecha_alta.strftime('%d-%m-%Y')}")