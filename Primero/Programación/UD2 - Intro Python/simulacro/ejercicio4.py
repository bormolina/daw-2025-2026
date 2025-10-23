def convertirNota(nota: str) -> str:
    conversion = "Nota erronea"
    
    match nota:
        case "Do":
            conversion = "C"
        case "Re":
            conversion = "D"
        case "Mi":
            conversion = "E"
        case "Fa":
            conversion = "F"
        case "Sol":
            conversion = "G"
        case "La":
            conversion = "A"
        case "Si":
            conversion = "B"
    
    return conversion

while True:
    nota = input("Inserta una nota: ")

    if nota == "fin":
        break

    print(f"{nota} en notacion anglosajona es {convertirNota(nota)}")