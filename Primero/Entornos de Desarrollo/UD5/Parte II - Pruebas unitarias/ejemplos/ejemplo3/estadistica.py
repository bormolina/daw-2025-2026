def media(datos: list[float]) -> float:
    return sum(datos) / len(datos)


def mediana(datos: list[float]) -> float:
    datos = sorted(datos)
    n = len(datos)

    if n % 2 == 1:
        return datos[n // 2]
    else:
        return (datos[n // 2 - 1] + datos[n // 2]) / 2


def rango_intercuartilico(datos: list[float]) -> float:
    datos = sorted(datos)
    n = len(datos)

    mitad = n // 2
    inferior = datos[:mitad]
    superior = datos[mitad:]

    q1 = mediana(inferior)
    q3 = mediana(superior)

    return q3 - q1


def dispersion(datos: list[float]) -> float:
    return max(datos) - min(datos)