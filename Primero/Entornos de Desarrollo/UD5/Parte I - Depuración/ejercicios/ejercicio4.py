class EstacionMeteorologica:

    def __init__(self, ciudad: str):
        self.ciudad = ciudad
        self.temperaturas = []

    def registrar_temperatura(self, t: float) -> None:
        # Añade una nueva temperatura registrada a la lista
        self.temperaturas.append(t)

    def temperatura_media(self) -> float:
        # Devuelve la media aritmética de todas las temperaturas registradas

        total = 0

        for t in self.temperaturas:
            total += t

        return total / len(self.temperaturas)

    def temperatura_maxima(self) -> float:
        # Devuelve la temperatura más alta registrada

        maxima = 0

        for t in self.temperaturas:
            if t < maxima: 
                maxima = t

        return maxima


if __name__ == "__main__":

    estacion = EstacionMeteorologica("Granada")

    estacion.registrar_temperatura(18)
    estacion.registrar_temperatura(22)
    estacion.registrar_temperatura(16)
    estacion.registrar_temperatura(25)

    print("Temperatura media:")
    print(estacion.temperatura_media())

    print("\nTemperatura máxima:")
    print(estacion.temperatura_maxima())