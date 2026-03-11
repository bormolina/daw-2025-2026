class Cuenta:
    COMISION_MANTENIMIENTO = 5.0

    def __init__(self, titular: str, numero_cuenta: str, saldo: float):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def ingresar(self, cantidad: float) -> None:
        self.saldo += cantidad

    def retirar(self, cantidad: float) -> bool:
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False

    def cobrar_comision(self) -> None:
        self.saldo -= Cuenta.COMISION_MANTENIMIENTO

    def __str__(self) -> str:
        return f"Cuenta | Titular: {self.titular} | Nº: {self.numero_cuenta} | Saldo: {self.saldo:.2f}€"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Cuenta):
            return False
        return self.numero_cuenta == other.numero_cuenta

    def __hash__(self) -> int:
        return hash(self.numero_cuenta)