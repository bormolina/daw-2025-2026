import math


def area_cuadrado(lado: float) -> float:
    return lado * lado


def perimetro_rectangulo(base: float, altura: float) -> float:
    return 2 * (base + altura)


def area_circulo(radio: float) -> float:
    return math.pi * radio * radio


def area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2


def hipotenusa(cateto1: float, cateto2: float) -> float:
    return math.sqrt(cateto1 ** 2 + cateto2 ** 2)


def distancia_puntos(x1: float, y1: float, x2: float, y2: float) -> float:
    dx = x2 - x1
    dy = y2 - y1
    distancia = math.sqrt(dx ** 2 + dy ** 2)
    return distancia


def area_triangulo_lados(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def es_triangulo_valido(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True


def volumen_prisma_rectangular(ancho: float, fondo: float, altura: float) -> float:
    base = ancho * fondo
    volumen = base * altura
    return volumen


def area_corona_circular(radio_exterior: float, radio_interior: float) -> float:
    area_exterior = math.pi * radio_exterior ** 2
    area_interior = math.pi * radio_interior ** 2
    area = area_exterior - area_interior
    return area