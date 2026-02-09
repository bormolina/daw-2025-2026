from datetime import datetime   
from datos import get_datos
from Pedido import Pedido


# Sin diccionarios
def ranking_empleados(pedidos: list[Pedido]) -> None:

    nombres = set([p.transportista for p in pedidos])
    trabajadores = []
    for nombre in nombres:
        trabajadores.append([nombre, 0])


    for trabajador in trabajadores:
        pedidos_trabajador = [p for p in pedidos if p.transportista == trabajador[0]]
        for p in pedidos_trabajador:
            trabajador[1] += 1
            dias_entrega = (p.fecha_entrega - p.fecha_pedido).days
            if dias_entrega <= 1:
                trabajador[1] += 1
            elif dias_entrega > 3:
                trabajador[1] -= 0.25

    # Ranking mejores trabajadores
    sorted_trabajadores = sorted(trabajadores, key=lambda x: x[1], reverse=True)
    for trabajador in sorted_trabajadores:
        print(f"Trabajador: {trabajador[0]}, Puntos: {trabajador[1]}")

# Con diccionarios
def ranking_empleados2(pedidos: list[Pedido]) -> None:
    puntos_por_transportista = {}

    for p in pedidos:
        nombre = p.transportista

        # Inicializar si no existe
        if nombre not in puntos_por_transportista:
            puntos_por_transportista[nombre] = 0

        # Punto base por pedido
        puntos_por_transportista[nombre] += 1

        dias = (p.fecha_entrega - p.fecha_pedido).days

        # Bonificación / penalización
        if dias <= 1:
            puntos_por_transportista[nombre] += 1
        elif dias > 3:
            puntos_por_transportista[nombre] -= 0.25

    # Ordenar ranking por puntos
    ranking = sorted(
        puntos_por_transportista.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for nombre, puntos in ranking:
        print(f"Trabajador: {nombre}, Puntos: {puntos}")


print('\n\n### RANKING EMPLEADOS SIN DICCIONARIOS ###')
pedidos = get_datos()
ranking_empleados(pedidos)

print('\n\n### RANKING EMPLEADOS CON DICCIONARIOS ###')
pedidos = get_datos()
ranking_empleados2(pedidos)

