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
with open(nombre_archivo, "r", encoding="utf-8") as f:
    texto = f.read().lower()

contador = texto.count("caballero")
print("Número de veces que aparece 'caballero':", contador)