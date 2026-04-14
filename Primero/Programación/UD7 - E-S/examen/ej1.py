from pathlib import Path


class Elemento:
    def __init__(self, nombre: str, simbolo: str, numero_atomico: int, masa_atomica: float, grupo: int) -> None:
        self.nombre = nombre
        self.simbolo = simbolo
        self.numero_atomico = numero_atomico
        self.masa_atomica = masa_atomica
        self.grupo = grupo



if __name__ == "__main__":
    ruta = Path(__file__).parent / "datos" / "elementos.csv"

    elementos_grupo1 = []

    suma_grupo1 = 0
    suma_resto = 0
    cont_resto = 0

    with open(ruta, "r", encoding="utf-8") as f:
        next(f)

        for linea in f:
            linea = linea.strip()

            if linea:
                partes = linea.split(",")

                nombre = partes[0]
                simbolo = partes[1]
                numero_atomico = int(partes[2])
                masa_atomica = float(partes[3])
                grupo = int(partes[4])

                if grupo == 1:
                    elemento = Elemento(nombre, simbolo, numero_atomico, masa_atomica, grupo)
                    elementos_grupo1.append(elemento)
                    suma_grupo1 += masa_atomica
                else:
                    suma_resto += masa_atomica
                    cont_resto += 1

    # Mostrar elementos del grupo 1
    print("Elementos del grupo 1:")
    for e in elementos_grupo1:
        print(e.nombre)

    # Medias
    if elementos_grupo1:
        media_grupo1 = suma_grupo1 / len(elementos_grupo1)
    else:
        media_grupo1 = 0

    if cont_resto > 0:
        media_resto = suma_resto / cont_resto
    else:
        media_resto = 0

    print(f"\nMedia grupo 1: {media_grupo1:.2f}")
    print(f"Media resto: {media_resto:.2f}")