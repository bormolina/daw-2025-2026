from datetime import datetime
from Pedido import Pedido
from datos import get_datos


def f2a(pedidos: list[Pedido]) -> Pedido:
    return max([p for p in pedidos], key=lambda p: p.precio)


def f2b(pedidos: list[Pedido]) -> float:
    if len(pedidos) == 0:
        return 0
    else:
        return round(sum([p.precio for p in pedidos]) / len(pedidos), 2)


def f2c(pedidos: list[Pedido], transportista: str) -> list[Pedido]:
    return [p for p in pedidos if p.transportista == transportista]


def f2d(pedidos: list[Pedido]) -> Pedido:
    return max([p for p in pedidos], key=lambda p: p.fecha_pedido)


def f2e(pedidos: list[Pedido]) -> Pedido:
    return min([p for p in pedidos], key=lambda p:p.fecha_entrega-p.fecha_pedido)


def f2f(pedidos: list[Pedido]) -> Pedido:
    return max([p for p in pedidos], key=lambda p:p.precio_por_kg())


def f2g(pedidos: list[Pedido]) -> dict[str, float]:
    res = {}
    for p in pedidos:
        if p.tipo not in res:
            res[p.tipo] = 0
        res[p.tipo] += p.precio
    return res


def f2h(pedidos: list[Pedido]) -> dict[str, int]:
    res = {}
    for p in pedidos:
        localidad = p.direccion[2]
        if localidad not in res:
            res[localidad] = 0
        res[localidad] += 1
    return res


datos = get_datos()

p1 = Pedido(21, 'Cerezo', 450, ['Camino del Río', 3, 'Cájar'], datetime(2024, 2, 10), datetime(2024, 2, 17), 360, 'Raulito')
p2 = Pedido(22, 'Olivo', 600, ['Calle Real', 8, 'Monachil'], datetime(2024, 2, 5), datetime(2024, 2, 12), 420, 'Manolito')

datos.insert(0, p1)
datos.insert(0, p2)

r2a = f2a(datos)
print(f'2a. El id del pedido con mayor precio es {r2a.id_pedido} y su precio es {r2a.precio} €')
r2b = f2b(datos)
print(f'2b. El precio medio de los pedidos es {r2b} €')
r2c = f2c(datos, 'Manolito')
print(f'2c. Los pedidos realizados por manolito son {[p.id_pedido for p in r2c]}')
r2d = f2d(datos)
print(f'2d. El pedido más reciente es {r2d.id_pedido}')
r2e = f2e(datos)
print(f'2e. El pedido que menos tiempo ha tardado en realizarse es: {r2e.id_pedido} y el tiempo que tardo es {(r2e.fecha_entrega - r2e.fecha_pedido).days} días')
r2f = f2f(datos)
print(f'2f. El pedido de mayor precio por kilogramo es: {r2f.id_pedido} y su precio es {r2f.precio_por_kg()} €/kg')
r2g = f2g(datos)
print(f'2g. El precio total por tipo de leña es: {r2g}')
r2h = f2h(datos)
print(f'2h. El número de pedidos por localidad es: {r2h}')  
