print("¿Qué pista quieres alquilar?")
print("1. Tenis")
print("2. Futbol sala")
print("3. Futbol 11")
print("4. Rugby")

tipo = input("Elige el tipo de pista: ")
dia = input("Elige el día de la semana (L, M, X, J, V, S, D): ")
focas = input("¿Quieres focas? (S/N): ")
alumno = input("¿Eres alumno/a de la UGR? (S/N): ")

precio = 0

if dia == "S" or dia == "D":
    es_finde = True
elif dia == "L" or dia == "M" or dia == "X" or dia == "J" or dia == "V":
    es_finde = False

match tipo:
    case "1":
        precio = 10 if es_finde else 8 
        precio = precio + 5 if focas == "S" else precio
    case "2":
        precio = 30 if es_finde else 26
        precio = precio + 10 if focas == "S" else precio
    case "3":
        precio = 79 if es_finde else 64
        precio = precio + 20 if focas == "S" else precio
    case "4": 
        precio = 94 if es_finde else 80
        precio = precio + 25 if focas == "S" else precio

if alumno == "S":
    precio = precio - (precio*0.15)

print(f"Tienes que pagar {round(precio, 2)}€")