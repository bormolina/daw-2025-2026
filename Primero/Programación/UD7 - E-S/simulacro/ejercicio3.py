from pathlib import Path


if __name__ == "__main__":
    ruta_entrada = Path(__file__).parent / "datos" / "lazarillo.txt"
    ruta_salida = Path(__file__).parent / "analisis_lazarillo.txt"

    # Variables dónde vamos a almacenar los resultados
    num_lineas = 0
    num_palabras = 0
    num_letras = 0
    linea_mas_larga = ""

    with open(ruta_entrada, "r", encoding="utf-8") as f:
        for linea in f:
            num_lineas += 1
            linea_limpia = linea.strip()
            palabras = linea_limpia.split()
            num_palabras += len(palabras)
            for c in linea_limpia:
                if c.isalpha(): #isalpha devuelve True si el carácter es una letra (mayúscula o minúscula) y False en caso contrario (espacios, signos de puntuación, números, etc)
                    num_letras += 1

            # Línea más larga
            # La clasificación de la línea más larga la primera, la comparo con la siguiente, si la siguiente es más larga, esa se convierte en la línea más larga, y así sucesivamente hasta el final del fichero
            if len(linea_limpia) > len(linea_mas_larga):
                linea_mas_larga = linea_limpia

    # Una vez tenemos los resultados en varibles es muy sencillo, tan solo tenemos que abrir el fichero de salida en modo escritura y escribir los resultados formateados como queramos (o bueno... como el profe te pida). 
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(f"Líneas: {num_lineas}\n")
        f.write(f"Palabras: {num_palabras}\n")
        f.write(f"Letras: {num_letras}\n")
        f.write("Línea más larga:\n")
        f.write(linea_mas_larga + "\n")