from dataclasses import dataclass
from datetime import datetime

@dataclass
class Comercial:
   id: int
   nombre: str
   apellido1: str
   apellido2: str
   ciudad: str = ''
   comision: float = 0

@dataclass
class Pedido: 
   id: int
   cantidad: float
   fecha: datetime
   id_cliente: int
   id_comercial: int

@dataclass
class Cliente:
   id: int 
   nombre: str
   apellido1: str
   apellido2: str
   ciudad: str
   categoria: int



c = Comercial(1, 'Borja', 'Molina', 'Zea', 'Monachil', 500)
c2 = Comercial(2, 'Alumo', 'Malvado', 'NO')
print(c.nombre)

# Trabajo para casa: cread objetos de las clases y provadlas