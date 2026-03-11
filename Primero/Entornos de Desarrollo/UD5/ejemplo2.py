class CuentaBancaria:

    def __init__(self, titular: str, saldo: float) -> None:
        self.titular: str = titular
        self.saldo: float = saldo
        self.movimientos: list[float] = []

    def ingresar(self, cantidad: float) -> None:
        self.saldo += cantidad
        self.movimientos.append(cantidad)  

    def retirar(self, cantidad: float) -> None:
        if cantidad > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= cantidad
            self.movimientos.append(-cantidad)

    def calcular_media_movimientos(self) -> float:
        total: float = 0

        for cantidad in self.movimientos:
            total += cantidad

        media = total / len(self.movimientos)
        return media


if __name__ == "__main__":

    cuenta = CuentaBancaria("Borjoso", 1000)

    cuenta.ingresar(200)
    cuenta.retirar(150)
    cuenta.ingresar(300)

    print(f"Saldo actual: {cuenta.saldo}")

    media = cuenta.calcular_media_movimientos()
    print(f"Media de movimientos: {media:.2f}")

