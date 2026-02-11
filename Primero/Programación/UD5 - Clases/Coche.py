class Coche:
    def __init__(self, marca: str, modelo: str, año_fabricación: int, peso: int, tipo_motor: str, potencia: int, automatico: bool, num_puertas: int, num_asientos: int, consumo: float, depósito: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.año_fabricación = año_fabricación
        self.peso = peso
        self.tipo_motor = tipo_motor
        self.potencia = potencia
        self.automatico = automatico
        self.num_puertas = num_puertas
        self.num_asientos = num_asientos
        self.consumo = consumo
        self.depósito = depósito

    def autonomia(self) -> float:
        return self.depósito / self.consumo * 100
    
    def __str__(self) -> str:
        return f"Marca: {self.marca}, modelo: {self.modelo}" # Lo completais vosotros

    
c = Coche('Seat', 'Ibiza', 2004, 1100, 'gasolina', 94, False, 4, 5, 5, 50)
print(c.autonomia())
