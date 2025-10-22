import geometria

def area(figura: str) -> float:
    area = -1
    match figura:
        case "Triángulo":
            base = float(input("Inserta la base: "))
            altura = float(input("Inserta la altura: "))
            area = geometria.areaTriangulo(base, altura)
        case "Rectángulo":
            base = float(input("Inserta la base: "))
            altura = float(input("Inserta la altura: "))
            area = geometria.areaRectangulo(base, altura)
        case "Círculo":
            radio = float(input("Inserta el radio: "))
            area = geometria.areaCirculo(radio)
        case _:
            print("Figuara geométrica no válida")
    return area


figura = input("Elige una figura (Triángulo, Rectángulo o Círculo): ")
areaFigura = area(figura)
print(f"El area es: {areaFigura}")