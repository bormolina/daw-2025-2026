from dataclasses import dataclass
from datetime import datetime

@dataclass
class Proveedor:
    id_proveedor: int
    nombre: str
    teléfono: str
    email: str
    localidad: str

@dataclass
class Pedido: 
    id_pedido: int
    fecha_pedido: datetime
    fecha_entrega: datetime
    precio_total: float
    direccion_envio: str
    peso_kg: float
    tipo_producto: int
    id_proveedor: int