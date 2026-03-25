from pathlib import Path


if __name__ == "__main__":

    palabras = []

    while True:

        palabra = input("Introduce una palabra (fin para terminar): ")

        if palabra.lower() == "fin":
            break

        palabras.append(palabra)

    carpeta_script = Path(__file__).parent
    ruta = carpeta_script / "palabras.txt"

    with open(ruta, "w", encoding="utf-8") as f:

        for p in palabras:
            f.write(p + "\n")

    print("Fichero palabras.txt creado correctamente.")