import math


def areaCirculo(radio: float) -> float:
    return math.pi * radio * radio if radio > 0 else 0

def esPrimo(n: int) -> bool:
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False


def imc(peso: float, altura: float) -> str:
    resultado = peso / (altura * altura)
    if resultado < 18.5:
        return "Bajo peso"
    if resultado >= 18.5 and resultado < 24.9:
        return "Normal"
    if resultado >= 25 and resultado < 29.9:
        return "Sobrepeso"
    if resultado >= 29.9:
        return "Obesidad"
