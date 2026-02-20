from datetime import date
from datos import get_empleados


# f3a) Sueldo medio
def f3a(empleados: list) -> float:
    return sum(e.sueldo for e in empleados) / len(empleados)


# f3b) Empleado con sueldo más alto
def f3b(empleados: list):
    return max(empleados, key=lambda e: e.sueldo)


# f3c) Empleados que cobran más que n
def f3c(empleados: list, n: float) -> list:
    return [e for e in empleados if e.sueldo > n]


# f3d) Empleados que llevan más de n años en la empresa
def f3d(empleados: list, n: int) -> list:
    hoy = date.today()
    return [
        e for e in empleados
        if (hoy - e.fecha_ingreso).days > n * 365
    ]


# f3e) Empleado más antiguo
def f3e(empleados: list):
    return min(empleados, key=lambda e: e.fecha_ingreso)


# f3f) Todos los empleados ordenados por antigüedad (más antiguo primero)
def f3f(empleados: list) -> list:
    return sorted(empleados, key=lambda e: e.fecha_ingreso)


# f3g) Empleados contratados en un año concreto
def f3g(empleados: list, anio: int) -> list:
    return [e for e in empleados if e.fecha_ingreso.year == anio]


# f3h) Empleados que trabajan para un departamento dado
def f3h(empleados: list, departamento: str) -> list:
    return [e for e in empleados if departamento in e.departamentos]


# f3i) Reporte {departamento: número de empleados}
def f3i(empleados: list) -> dict:
    reporte = {}
    for e in empleados:
        for d in e.departamentos:
            reporte[d] = reporte.get(d, 0) + 1
    return reporte


# f3j) Reporte {departamento: sueldo medio}
def f3j(empleados: list) -> dict:
    acumulado = {}
    conteo = {}

    for e in empleados:
        for d in e.departamentos:
            acumulado[d] = acumulado.get(d, 0) + e.sueldo
            conteo[d] = conteo.get(d, 0) + 1

    return {d: acumulado[d] / conteo[d] for d in acumulado}


if __name__ == "__main__":

    datos = get_empleados()

    print("===== f3a Sueldo medio =====")
    print(f3a(datos))
    print()

    print("===== f3b Sueldo más alto =====")
    resultado = f3b(datos)
    print(f'{resultado.nombre} - {resultado.sueldo} €')
    print()

    print("===== f3c Sueldos > 2000 =====")
    for e in f3c(datos, 2000):
        print(f'{e.nombre} - {e.sueldo} €')
    print()

    print("===== f3d Más de 3 años en empresa =====")
    for e in f3d(datos, 3):
        print(f'{e.nombre} - {e.fecha_ingreso}')
    print()

    print("===== f3e Empleado más antiguo =====")
    print(f3e(datos))
    print()

    print("===== f3f Ordenados por antigüedad =====")
    for e in f3f(datos):
        print(f'{e.nombre} - {e.fecha_ingreso}')
    print()

    print("===== f3g Contratados en año concreto. (2022) =====")
    anio = 2022
    for e in f3g(datos, anio):
        print(f'{e.nombre} - {e.fecha_ingreso}')
    print()

    print("===== f3h Departamento IT =====")
    for e in f3h(datos, "IT"):
        print(e)
    print()

    print("===== f3i Reporte número empleados por departamento =====")
    print(f3i(datos))
    print()

    print("===== f3j Reporte sueldo medio por departamento =====")
    print(f3j(datos))

