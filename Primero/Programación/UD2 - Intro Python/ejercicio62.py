import random

def generarCuenta(inicial, final):
    a = random.randint(inicial, final)
    b = random.randint(inicial, final)
    operacion = random.randint(1, 3)

    if operacion == 1:
        operador = "+"
        resultado = a + b
    elif operacion == 2:
        operador = "-"
        resultado = a - b
    else:
        operador = "*"
        resultado = a * b

    print(f"{a} {operador} {b} = ?")
    return resultado


for i in range(10):
    resultado = generarCuenta(1, 10)
    try:    
        respuesta = int(input("Tu respuesta: "))
    except Exception as _:
        print("Incorrecto!")
    else:
        if resultado == respuesta:
            print("Correcto, has acertado!")
        else:
            print("Incorrecto!")
