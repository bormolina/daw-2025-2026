# Cómo abrir un fichero de texto con la función open y el bloque with

with open("quijote.txt", "r", encoding="utf-8") as f:
    # Dentro de este bloque podemos leer el fichero
    print("He abierto el fichero!!!")


print("Se cierra el fichero")
# Al salir del bloque with el fichero se cierra y por lo tanto ya no podemos leerlo
