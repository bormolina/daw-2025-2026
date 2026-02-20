from datetime import date


class Mantecado:

    def __init__(
        self,
        id: int,
        tipo: str,
        fecha_creacion: date,
        fecha_caducidad: date,
        precio: float,
        ingredientes: list[str]
    ) -> None:
        self.id: int = id
        self.tipo: str = tipo
        self.fecha_creacion: date = fecha_creacion
        self.fecha_caducidad: date = fecha_caducidad
        self.precio: float = precio
        self.ingredientes: list[str] = ingredientes

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Mantecado):
            return False
        return self.id == other.id

    def __str__(self) -> str:
        return (
            f"{self.id} - {self.tipo} - "
            f"{self.fecha_creacion} - {self.fecha_caducidad} - "
            f"{self.precio} - {self.ingredientes}"
        )

    def dias_para_caducar(self) -> int:
        hoy: date = date.today()
        diferencia = self.fecha_caducidad - hoy
        return diferencia.days

    def esta_caducado(self) -> bool:
        return self.dias_para_caducar() < 0


# ===============================
# PRUEBAS
# ===============================
if __name__ == "__main__":

    m1 = Mantecado(
        id=1,
        tipo="Chocolate",
        fecha_creacion=date(2025, 12, 1),
        fecha_caducidad=date(2025, 12, 31),
        precio=3.5,
        ingredientes=["harina", "azúcar", "manteca", "cacao"]
    )

    m2 = Mantecado(
        id=1,
        tipo="Chocolate Especial",
        fecha_creacion=date(2025, 12, 5),
        fecha_caducidad=date(2026, 1, 5),
        precio=4.0,
        ingredientes=["harina", "azúcar", "manteca", "cacao", "almendra"]
    )

    print("Representación:")
    print(m1)

    print("\nDías para caducar:")
    print(m1.dias_para_caducar())

    print("\n¿Está caducado?")
    print(m1.esta_caducado())

    print("\nComparación por id (m1 == m2):")
    print(m1 == m2)