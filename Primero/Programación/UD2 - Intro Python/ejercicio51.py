import math

def longitudCircunferencia(radio: float) -> float:
    longitud = 2*math.pi*radio
    return longitud

longitud = longitudCircunferencia(2.5)
print(longitud)