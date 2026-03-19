from pathlib import Path

nombre_archivo = Path(__file__).parent / "quijote.txt"

# Versión 1 (sin usar readlines)
linea_mas_larga = ""
max_longitud = 0

with open(nombre_archivo, "r", encoding="utf-8") as f:
    for linea in f:
        longitud = len(linea)
        if longitud > max_longitud:
            max_longitud = longitud
            linea_mas_larga = linea

print("Versión 1 (sin usar readlines):")
print("Línea más larga:")
print(linea_mas_larga.strip())  # Usamos strip para eliminar el salto de línea al final
print("Número de caracteres:", max_longitud)


# Versión 2 (usando readlines)
with open(nombre_archivo, "r", encoding="utf-8") as f:
    lineas = f.readlines()

linea_mas_larga = max(lineas, key=lambda l: len(l))

print("\nVersión 2 (usando readlines):")
print("Línea más larga:")
print(linea_mas_larga.strip())
print("Número de caracteres:", len(linea_mas_larga))