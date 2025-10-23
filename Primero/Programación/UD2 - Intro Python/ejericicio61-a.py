# Sin funciones

while True:
    try:
        a = int(input("Inserta un número: "))
    except Exception as error:
        print(f"Número incorrecto")
    else:
        break

while True:
    try:
        b = int(input("Inserta un número: "))
    except Exception as error:
        print(f"Número incorrecto")
    else:
        break

resultado = a + b
print(f"La suma de {a} y {b} es {resultado}")