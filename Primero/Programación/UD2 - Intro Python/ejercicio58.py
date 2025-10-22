def areaTriangulo(base: float, altura: float) -> float:
    area = base*altura/2
    return area

base = float(input("Inserta la base: "))
altura = float(input("Inserta la altura: "))
solucion = areaTriangulo(base, altura)
print(f"El área es {solucion}")