from pathlib import Path


if __name__ == "__main__":
    palabras = []

    while True:
        palabra = input("Introduce una palabra (fin para terminar): ")

        if palabra.lower() == "fin":
            break

        palabras.append(palabra)

    ruta = Path(__file__).parent / "palabras.txt"

    with open(ruta, "w", encoding="utf-8") as f:
        for p in palabras:
            f.write(p + "\n")

    print("Fichero palabras.txt creado correctamente.")