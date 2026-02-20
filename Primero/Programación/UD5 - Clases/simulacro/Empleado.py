from datetime import date


class Empleado:
    def __init__(
        self,
        id: int,
        nombre: str,
        sueldo: float,
        fecha_ingreso: date,
        departamentos: list[str],
        empleado_del_mes: list[date] | None = None
    ):
        self.id = id
        self.nombre = nombre
        self.sueldo = sueldo
        self.fecha_ingreso = fecha_ingreso
        self.departamentos = departamentos
        self.empleado_del_mes = empleado_del_mes if empleado_del_mes is not None else []

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Empleado):
            return False
        return self.id == other.id

    def __str__(self) -> str:
        return f"{self.nombre} ({self.id})"