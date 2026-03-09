from datetime import datetime


class Empleado:
    def __init__(self, nombre: str, fecha_inicio: datetime, sueldo: float):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.sueldo = sueldo


class EmpleadoFijo(Empleado):
    def __init__(self, nombre: str, fecha_inicio: datetime, sueldo: float):
        super().__init__(nombre, fecha_inicio, sueldo)

    def trienios(self) -> int:
        hoy = datetime.today()
        antiguedad_anos = (hoy - self.fecha_inicio).days // 365.25
        return antiguedad_anos // 3  # un trienio cada 3 años


class EmpleadoTemporal(Empleado):
    def __init__(self, nombre: str, fecha_inicio: datetime, sueldo: float, fecha_fin: datetime):
        super().__init__(nombre, fecha_inicio, sueldo)
        self.fecha_fin = fecha_fin

    def meses_restantes(self) -> int:
        hoy = datetime.today()
        diferencia = (self.fecha_fin.year - hoy.year) * 12 + (self.fecha_fin.month - hoy.month)
        return max(diferencia, 0)

    def ampliar_contrato(self, meses: int) -> None:
        nuevo_mes = self.fecha_fin.month + meses
        nuevo_anio = self.fecha_fin.year + (nuevo_mes - 1) // 12
        nuevo_mes = ((nuevo_mes - 1) % 12) + 1
        self.fecha_fin = datetime(nuevo_anio, nuevo_mes, self.fecha_fin.day)


if __name__ == "__main__":
    fijo = EmpleadoFijo("Ana", datetime(2015, 3, 10), 2000.0)
    temporal = EmpleadoTemporal("Luis", datetime(2024, 6, 1), 1500.0, datetime(2026, 9, 1))

    print("Trienios de Ana:", fijo.trienios())

    print("Meses restantes de Luis:", temporal.meses_restantes())
    temporal.ampliar_contrato(6)
    print("Meses restantes tras ampliar contrato:", temporal.meses_restantes())

    # Accesos correctos
    print(fijo.sueldo)
    print(temporal.fecha_fin)

    # Accesos incorrectos (comentados)
    # print(fijo.fecha_fin)       # Un fijo no tiene fecha_fin
    # print(temporal.trienios())  # Un temporal no tiene trienios