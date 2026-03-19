from pathlib import Path

nombre_archivo = Path(__file__).parent / "quijote.txt"

# Versión 1 (sin usar readlines)
total_caracteres = 0
contador_lineas = 0

with open(nombre_archivo, "r", encoding="utf-8") as f:
    for linea in f:
        total_caracteres += len(linea)
        contador_lineas += 1

media = total_caracteres / contador_lineas

print("Longitud media de las líneas:", media)

# Versión 2 (usando readlines)
with open(nombre_archivo, "r", encoding="utf-8") as f:
    lineas = f.readlines()

media = sum(len(linea) for linea in lineas) / len(lineas)

print("Longitud media de las líneas:", media)