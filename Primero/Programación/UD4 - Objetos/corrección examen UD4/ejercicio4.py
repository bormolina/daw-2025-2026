from datetime import datetime
from Pedido import Pedido
from datos import get_datos

datos = get_datos()

def aplicar_sobrecoste(pedidos: list[Pedido]) -> None:
    fecha_limite = datetime(2024, 1, 10)

    for p in pedidos:
        if p.fecha_pedido >= fecha_limite:
            p.precio *= 1.10

aplicar_sobrecoste(datos)