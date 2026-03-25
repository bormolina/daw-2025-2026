from pathlib import Path


if __name__ == "__main__":

    carpeta_script = Path(__file__).parent

    ruta_quijote = carpeta_script.parent / "quijote.txt"
    ruta_salida = carpeta_script / "datos_quijote.txt"

    lineas = 0
    palabras = 0
    letras = 0

    with open(ruta_quijote, "r", encoding="utf-8") as f:

        for linea in f:
            lineas += 1
            palabras += len(linea.split())
            letras += sum(letra.isalpha() for letra in linea)

    with open(ruta_salida, "w", encoding="utf-8") as f:

        f.write(
            f"El Quijote tiene {lineas} líneas {palabras} palabras y {letras} letras"
        )