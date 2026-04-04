from pathlib import Path


if __name__ == "__main__":
    ruta = Path(__file__).parent / "tablas_multiplicar.txt"

    with open(ruta, "w", encoding="utf-8") as f:
        for n in range(1, 11):
            f.write(f"Tabla del {n}\n")

            for i in range(1, 11):
                f.write(f"{n} x {i} = {n * i}\n")

            f.write("\n")

    print("Fichero tablas_multiplicar.txt generado correctamente.")