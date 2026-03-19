from pathlib import Path

nombre_archivo = Path(__file__).parent / "quijote.txt"

# Versión 1 (sin usar readlines)
contador = 0

with open(nombre_archivo, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.lower()
        contador += linea.count("caballero")

print("Número de veces que aparece 'caballero':", contador)


# Versión 2 (usando readlines)
# Para este problema la solución con readlines es menos eficiente
contador2 = 0
with open(nombre_archivo, "r", encoding="utf-8") as f:
    lineas = f.readlines()
    porLinea = [linea.lower().count("caballero") for linea in lineas]
    contador2 = sum(porLinea)

print("Número de veces que aparece 'caballero':", contador2)