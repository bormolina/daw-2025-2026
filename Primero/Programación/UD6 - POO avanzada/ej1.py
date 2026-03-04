from datetime import datetime


class Vehiculo():
    def __init__(self, matricula: str, marca: str, fecha_matriculacion: datetime, fecha_ultima_itv: datetime):
        self.matricula = matricula
        self.marca = marca
        self.fecha_matriculacion = fecha_matriculacion
        self.fecha_ultima_itv = fecha_ultima_itv


class Coche(Vehiculo):
    def __init__(self, matricula: str, marca: str, fecha_matriculacion: datetime, fecha_ultima_itv: datetime, num_puertas: int, combustible: str):
        
        super().__init__(matricula, marca, fecha_matriculacion, fecha_ultima_itv)
        self.num_puertas = num_puertas
        self.combustible = combustible

    def proxima_itv(self) -> datetime:
        hoy = datetime.today()
        antiguedad = (hoy - self.fecha_matriculacion).days / 365.25

        if antiguedad <= 4:
            return datetime(self.fecha_ultima_itv.year + 4,
                            self.fecha_ultima_itv.month,
                            self.fecha_ultima_itv.day)
        
        elif 4 > antiguedad <= 10:
            return datetime(self.fecha_ultima_itv.year + 2,
                            self.fecha_ultima_itv.month,
                            self.fecha_ultima_itv.day)
        else:
            return datetime(self.fecha_ultima_itv.year + 1,
                            self.fecha_ultima_itv.month,
                            self.fecha_ultima_itv.day)


class Moto(Vehiculo):
    def __init__(self, matricula: str, marca: str, fecha_matriculacion: datetime, fecha_ultima_itv: datetime, cilindrada: int):
        
        super().__init__(matricula, marca, fecha_matriculacion, fecha_ultima_itv)
        self.cilindrada = cilindrada

    def proxima_itv(self):
        hoy = datetime(2026, 1, 1)  # fecha fija
        antiguedad = (hoy - self.fecha_matriculacion).days / 365.25

        if antiguedad >= 4:
            return datetime(self.fecha_ultima_itv.year + 2,
                            self.fecha_ultima_itv.month,
                            self.fecha_ultima_itv.day)
        else:
            return datetime(self.fecha_ultima_itv.year + 4,
                            self.fecha_ultima_itv.month,
                            self.fecha_ultima_itv.day)


if __name__ == "__main__":
    coche = Coche(
        "1234ABC",
        "Toyota",
        datetime(2012, 5, 10),   # fecha matriculación fija
        datetime(2025, 6, 1),    # última ITV fija
        5,
        "Gasolina"
    )

    moto = Moto(
        "5678XYZ",
        "Yamaha",
        datetime(2021, 3, 20),   # fecha matriculación fija
        datetime(2024, 4, 15),   # última ITV fija
        600
    )

    print("Próxima ITV coche:", coche.proxima_itv())
    print("Próxima ITV moto:", moto.proxima_itv())

    # Accesos correctos
    print(coche.num_puertas)
    print(moto.cilindrada)

    print(isinstance(moto, Moto))
    print(isinstance(moto, Vehiculo))
    print(isinstance(moto, Coche))
    print(isinstance(moto, object))
    print(issubclass(moto, object))
    print(issubclass(moto, Coche))
    print(issubclass(moto, Vehiculo))

    # Accesos incorrectos (comentados)
    # print(coche.cilindrada)  # Un coche no tiene cilindrada
    # print(moto.num_puertas)  # Una moto no tiene número de puertas