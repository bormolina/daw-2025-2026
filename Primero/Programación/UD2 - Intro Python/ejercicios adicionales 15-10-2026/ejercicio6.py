texto = input("Inserta una frase: ")
palabra = input("Inserta una palabra: ")

if palabra in texto:
    print(f"La palabra {palabra} está en el texto: {texto}")