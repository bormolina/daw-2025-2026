from datos import get_empleados

datos = get_empleados()

anio = 2023

print(f"===== EMPLEADO DEL AÑO {anio} =====")

ganador = None
max_premios = 0

for e in datos:

    premios_este_anio = 0

    for fecha in e.empleado_del_mes:
        if fecha.year == anio:
            premios_este_anio += 1

    if premios_este_anio > max_premios:
        max_premios = premios_este_anio
        ganador = e


if ganador is not None:
    print("Empleado del año:", ganador)
else:
    print("No hubo premios ese año.")