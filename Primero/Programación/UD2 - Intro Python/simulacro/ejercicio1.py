palabraCorta = ""
palabraLarga = ""
nPalabras = int(input("¿Cuántas palabras vas a insertar?"))

for i in range(nPalabras):
    palabra = input("Inserta palabra: ")

    if i == 0:
        palabraCorta = palabra
        palabraLarga = palabra

    if len(palabra) > len(palabraLarga):
        palabraLarga = palabra
    
    if len(palabra) < len(palabraCorta):
        palabraCorta = palabra

print(f"La palabra con menos letras es: {palabraCorta} y la que tiene más: {palabraLarga}")