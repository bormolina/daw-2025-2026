def areaTriangulo(base: float, altura: float) -> float:
    """Calcula el área de un triángulo
    :base: número real mayor a 0
    :base: float
    :altura: número real mayor a 0
    :altura: float


    :raises ValueError: si base o altura <= 0


    :return: el área del triángulo cuya base y altura son las pasada como parámetros
    """
    if base <= 0 or altura <= 0:
        raise ValueError("Tanto base como altura deben ser un número positivo")
    area = base * altura / 2
    return area