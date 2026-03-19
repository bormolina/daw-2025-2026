from pathlib import Path

nombre_archivo = Path(__file__).parent / "quijote.txt"

# Versión 1 (sin usar readlines)
contador = 0
with open(nombre_archivo, "r", encoding="utf-8") as f:
    for linea in f:
        contador += 1

print("Número total de líneas:", contador)

# Versión 2 (usando readlines)
with open(nombre_archivo, "r", encoding="utf-8") as f:
    lineas = f.readlines()

print("Número total de líneas:", len(lineas))