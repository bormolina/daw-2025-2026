texto = input("Introduce un texto: ")
palabrasTexto = texto.split()

diccionario = {}
for palabra in palabrasTexto:
    if not palabra in diccionario:
        diccionario[palabra] = 1
    else:
        diccionario[palabra] += 1

print("Frecuencia palabras: ")
for palabra, frecuencia in diccionario.items():
    print(f"{palabra}: {frecuencia}")