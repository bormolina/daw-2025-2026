from datetime import date, timedelta
from Mantecado import Mantecado
from Empleado import Empleado

def get_mantecados(n: int) -> list[Mantecado] | None:
    hoy = date.today()
    datos = [
        [
            Mantecado(
                1,
                "chocolate",
                hoy - timedelta(days=5),
                    hoy - timedelta(days=2),      
                    2.5,
                    ["harina", "azucar", "cacao", "manteca"]
                ),

                Mantecado(
                    2,
                    "almendra",
                    hoy - timedelta(days=4),
                    hoy + timedelta(days=3),
                    3.2,
                    ["harina", "azucar", "almendra", "manteca"]
                ),

                Mantecado(
                    3,
                    "limon",
                    hoy - timedelta(days=3),
                    hoy + timedelta(days=10),
                    1.9,
                    ["harina", "azucar", "limon", "manteca"]
                ),

                Mantecado(
                    4,
                    "canela",
                    hoy - timedelta(days=2),
                    hoy + timedelta(days=1),
                    2.1,
                    ["harina", "azucar", "canela", "manteca"]
                ),

                Mantecado(
                    5,
                    "chocolate",
                    hoy - timedelta(days=6),
                    hoy + timedelta(days=7),
                    2.8,
                    ["harina", "cacao", "manteca"]
                ),

                Mantecado(
                    6,
                    "coco",
                    hoy - timedelta(days=8),
                    hoy - timedelta(days=1),
                    2.3,
                    ["harina", "azucar", "coco", "manteca"]
                ),

                Mantecado(
                    7,
                    "almendra",
                    hoy - timedelta(days=1),
                    hoy + timedelta(days=15),
                    3.5,
                    ["harina", "almendra", "manteca"]
                ),

                Mantecado(
                    8,
                    "vainilla",
                    hoy - timedelta(days=2),
                    hoy + timedelta(days=4),
                    2.0,
                    ["harina", "azucar", "vainilla", "manteca"]
                ),

                Mantecado(
                    9,
                    "integral",
                    hoy - timedelta(days=3),
                    hoy + timedelta(days=2),
                    2.6,
                    ["harina integral", "azucar", "manteca"]
                ),

                Mantecado(
                    10,
                    "sin_azucar",
                    hoy - timedelta(days=1),
                    hoy + timedelta(days=6),
                    3.0,
                    ["harina", "edulcorante", "manteca"]
                )
        ]
    ]
    return datos[n] if 0 <= n < len(datos) else None



def get_empleados() -> list[Empleado]:
    hoy = date.today()

    return [
        Empleado(
            1,
            "Ana López",
            1850.0,
            hoy - timedelta(days=1200),
            ["IT"],
            [
                hoy - timedelta(days=1000),
                hoy - timedelta(days=800),
                hoy - timedelta(days=600),
                hoy - timedelta(days=300),
                hoy - timedelta(days=100),
            ]
        ),

        Empleado(
            2,
            "Carlos Ruiz",
            2100.0,
            hoy - timedelta(days=900),
            ["Ventas"],
            [
                hoy - timedelta(days=850),
                hoy - timedelta(days=500),
                hoy - timedelta(days=200),
            ]
        ),

        # SIN PREMIOS
        Empleado(
            3,
            "María Torres",
            1950.0,
            hoy - timedelta(days=600),
            ["RRHH", "Ventas"],  # trabaja en dos
            []
        ),

        Empleado(
            4,
            "Javier Martín",
            2300.0,
            hoy - timedelta(days=1500),
            ["Producción"],
            [
                hoy - timedelta(days=1400),
                hoy - timedelta(days=1200),
                hoy - timedelta(days=1000),
                hoy - timedelta(days=800),
                hoy - timedelta(days=400),
                hoy - timedelta(days=50),
            ]
        ),

        # SIN PREMIOS
        Empleado(
            5,
            "Lucía Fernández",
            1750.0,
            hoy - timedelta(days=300),
            ["Logística"],
            []
        ),

        Empleado(
            6,
            "Pedro Sánchez",
            2000.0,
            hoy - timedelta(days=1100),
            ["IT", "Producción"],  # trabaja en dos
            [
                hoy - timedelta(days=1000),
                hoy - timedelta(days=700),
                hoy - timedelta(days=600),
                hoy - timedelta(days=250),
            ]
        ),

        Empleado(
            7,
            "Elena Gómez",
            1900.0,
            hoy - timedelta(days=450),
            ["RRHH"],
            [
                hoy - timedelta(days=300),
                hoy - timedelta(days=120),
                hoy - timedelta(days=60),
            ]
        ),

        Empleado(
            8,
            "Raúl Navarro",
            2200.0,
            hoy - timedelta(days=1300),
            ["Producción"],
            [
                hoy - timedelta(days=1200),
                hoy - timedelta(days=1000),
                hoy - timedelta(days=900),
                hoy - timedelta(days=600),
                hoy - timedelta(days=350),
            ]
        ),

        Empleado(
            9,
            "Sofía Morales",
            2050.0,
            hoy - timedelta(days=750),
            ["Ventas", "Logística"],  # trabaja en dos
            [
                hoy - timedelta(days=600),
                hoy - timedelta(days=365),
                hoy - timedelta(days=180),
                hoy - timedelta(days=30),
            ]
        ),

        # SIN PREMIOS
        Empleado(
            10,
            "Diego Romero",
            1800.0,
            hoy - timedelta(days=200),
            ["IT"],
            []
        ),
    ]