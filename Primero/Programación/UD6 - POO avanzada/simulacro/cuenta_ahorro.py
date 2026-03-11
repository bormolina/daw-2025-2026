from cuenta import Cuenta


class CuentaAhorro(Cuenta):
    def __init__(self, titular: str, numero_cuenta: str, saldo: float, interes_anual: float):
        super().__init__(titular, numero_cuenta, saldo)
        self.interes_anual = interes_anual

    def aplicar_intereses(self) -> None:
        intereses = self.saldo * (self.interes_anual / 100)
        self.saldo += intereses

    def retirar(self, cantidad: float) -> bool:
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False

    def __str__(self) -> str:
        base = super().__str__().replace("Cuenta", "Cuenta Ahorro")
        return f"{base} | Interés: {self.interes_anual}%"