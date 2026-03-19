from pathlib import Path

nombre_archivo = Path(__file__).parent / "quijote.txt"

# Versión 1 (sin usar readlines)
contador = 0
with open(nombre_archivo, "r", encoding="utf-8") as f:
    for linea in f:
        if linea[:4] == "Don ":
            contador += 1

print("Número de líneas que empiezan por 'Don':", contador)

# Versión 2 (usando readlines)
with open(nombre_archivo, "r", encoding="utf-8") as f:
    contador = len([linea for linea in f.readlines() if linea.startswith("Don")])
    print("Número de líneas que empiezan por 'Don':", contador)
