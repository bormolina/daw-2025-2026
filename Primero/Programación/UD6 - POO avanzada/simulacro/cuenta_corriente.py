from cuenta import Cuenta


class CuentaCorriente(Cuenta):
    def __init__(self, titular: str, numero_cuenta: str, saldo: float, limite_descubierto: float):
        super().__init__(titular, numero_cuenta, saldo)
        self.limite_descubierto = limite_descubierto

    def puede_retirar(self, cantidad: float) -> bool:
        return self.saldo - cantidad >= -self.limite_descubierto

    def retirar(self, cantidad: float) -> bool:
        if self.puede_retirar(cantidad):
            self.saldo -= cantidad
            return True
        return False

    def __str__(self) -> str:
        base = super().__str__().replace("Cuenta", "Cuenta Corriente")
        return f"{base} | Descubierto: {self.limite_descubierto:.2f}€"