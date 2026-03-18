import math

def area_rectangulo(base: float, altura: float) -> float:
    return base * altura

def area_circulo(radio: float) -> float:
    return math.pi * radio ** 2

def perimetro_rectangulo(base: float, altura: float) -> float:
    return 2 * (base + altura)

def perimetro_circulo(radio: float) -> float:
    return 2 * math.pi * radio