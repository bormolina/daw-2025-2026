i = 1
palabraCorta = ""
palabraLarga = ""

while True:
    palabra = input("Inserta una palabra: ")
   
    if palabra == "fin":
        break
    
    if i == 1:
        palabraCorta = palabra
        palabraLarga = palabra
    else:
        if len(palabra) >= len(palabraLarga): 
            palabraLarga = palabra
        if len(palabra) <= len(palabraCorta): 
            palabraCorta = palabra
    
    i = i + 1

if palabraLarga != "" and palabraCorta != "":
    print(f"La palabra más corta es: {palabraCorta} y la más larga es {palabraLarga}")
else:
    print("No has insertado ninguna palabra")