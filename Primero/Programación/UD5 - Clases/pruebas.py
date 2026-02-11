from dataclasses import dataclass

@dataclass
class Comercial:
   id: int
   nombre: str
   apellido1: str
   apellido2: str
   ciudad: str = ''
   comision: float = 0


c = Comercial(1, 'Borja', 'Molina', 'Zea', 'Monachil', 500)
c2 = Comercial(2, 'Alumo', 'Malvado', 'NO')
print(c.nombre)