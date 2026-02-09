from datos import get_datos, get_datos_competencia

datos = get_datos()
datos_competencia = get_datos_competencia()

# Apartado A
print('\n### APARTADO A ###')
repes = []
for p in datos:
    for pc in datos_competencia:
        if p.direccion == pc.direccion:
            repes.append(f'{p.direccion[0]} {p.direccion[1]}, {p.direccion[2]}')

repes = list(set(repes))  # Eliminar duplicados
print('Las siguientes direcciones han pedido a ambas empresas:')
for r in repes:
    print(f'\t {r}')

# Apartado B
reporte = {}

# Contamos pedidos de nuestra empresa
for p in datos:
    localidad = p.direccion[2]
    if localidad not in reporte:
        reporte[localidad] = 0
    reporte[localidad] += 1

# Restamos pedidos de la competencia
for pc in datos_competencia:
    localidad = pc.direccion[2]
    if localidad not in reporte:
        reporte[localidad] = 0
    reporte[localidad] -= 1

print('\n### APARTADO B ###')
print("Diferencia de pedidos por localidad (nuestra empresa - competencia):")
for loc, diff in reporte.items():
    print(f"{loc}: {diff}")