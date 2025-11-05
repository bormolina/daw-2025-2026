import math

def calcular_hipotenusa(a: float, b: float) -> float:
    assert a > 0 and b > 0, "Los catetos deben ser valores positivos"
    h = math.sqrt(a**2 + b**2)
    return h


print("Cálculo de la hipotenusa de un triángulo rectángulo\n")
cateto1 = int(input("Introduce el primer cateto: "))
# Pequeño fallo: añadimos un signo negativo por error humano
cateto2 = int(input("Introduce el segundo cateto: "))
h = calcular_hipotenusa(cateto1, cateto2)
print(h)
