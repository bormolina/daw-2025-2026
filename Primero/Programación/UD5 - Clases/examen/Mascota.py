from datetime import datetime


class Mascota:
    def __init__(self, id: int, nombre: str, tipo: str,
                 fecha_entrada: datetime, precio: float,
                 fecha_nacimiento: datetime,
                 fecha_venta: datetime | None = None,
                 vacunas: list[str] | None = None):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.fecha_entrada = fecha_entrada
        self.precio = precio
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_venta = fecha_venta
        self.vacunas = vacunas  # None = no necesita vacunas, [] = debería llevar pero no tiene

    def __eq__(self, other):
        if not isinstance(other, Mascota):
            return False
        return self.id == other.id

    def __str__(self):
        return f"{self.tipo} - {self.edad():.2f} días - {self.precio}€ [{self.id}]"

    def se_vacuna(self) -> bool:
        return self.vacunas is not None

    def edad(self) -> float:
        hoy = datetime.today()
        dias = (hoy - self.fecha_nacimiento).days
        return dias


if __name__ == "__main__":
    from datetime import timedelta  # Import solo para pruebas

    hoy = datetime.today()

    # Mascota 1: gato de 2.5 años, con vacunas
    fecha_nac_gato = hoy - timedelta(days=int(2.5 * 365.25))
    gato = Mascota(
        id=1,
        nombre="Misu",
        tipo="Gato",
        fecha_entrada=hoy - timedelta(days=10),
        precio=120.0,
        fecha_nacimiento=fecha_nac_gato,
        fecha_venta=None,
        vacunas=["Rabia", "Trivalente"]
    )

    # Mascota 2: tarántula de 1 año, sin vacunas necesarias
    fecha_nac_arana = hoy - timedelta(days=int(1 * 365.25))
    arana = Mascota(
        id=2,
        nombre="Venom",
        tipo="Tarántula",
        fecha_entrada=hoy - timedelta(days=3),
        precio=45.5,
        fecha_nacimiento=fecha_nac_arana,
        fecha_venta=None,
        vacunas=None
    )

    # Pruebas
    print("=== PRUEBAS DE MASCOTA ===")
    print("\nPruebas para el gato")
    print(gato)
    print("¿Se vacuna gato?", gato.se_vacuna())
    print()

    print("Pruebas para la araña")
    print(arana)
    print("¿Se vacuna araña?", arana.se_vacuna())
    print()

    print("¿Es el gato igual a la araña?", gato == arana)
    print("¿Es la araña igual a ella misma?", arana == arana)