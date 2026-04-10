from pathlib import Path

ruta = Path(__file__).parent / "datos" / "divina-comedia.txt"

# Como es un fichero pequeño lo leo del tirón y trabajo comodamente como si fuese una simple lista de strings, cada string es una línea del fichero. Si el fichero fuera muy grande, lo mejor sería ir leyendo línea a línea para no tener que cargar todo el fichero en memoria, pero como no se especifica nada al respecto, esta solución es perfectamente válida para el examen.
with open(ruta, "r", encoding="utf-8") as f:
    contenido = [linea.strip() for linea in f.readlines()] 

contenido_sin_lineas_vacias = [linea.strip() for linea in contenido if linea.strip()] 

# Resultados
apartado_a = contenido[6:27] 
apartado_b = sorted(contenido_sin_lineas_vacias, key=lambda linea: len(linea))[-1]
apartado_c = sorted(contenido_sin_lineas_vacias, key=lambda linea: linea.count("m"))[-1]

# Escribimos los resultados
ruta_salida = Path(__file__).parent / "ejercicio3-resultado.txt"

with open(ruta_salida, "w", encoding="utf-8") as f:
    f.write("### Apartado A:\n")
    for linea in apartado_a:
        f.write(f"{linea}\n")
    f.write("\n### Apartado B:\n")
    f.write(f"{apartado_b}\n")
    f.write("\n### Apartado C:\n")
    f.write(f"{apartado_c}\n")
