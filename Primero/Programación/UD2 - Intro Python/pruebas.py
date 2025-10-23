while True:
    try:
        n = int(input("Inserta un número (0 para salir): "))
    except Exception as error:
        print(f"Se ha producido un error del tipo: {error}")
    else:
        if n == 0:
            print("Programa finalizado.")
            break
        elif n % 2 == 0:
            resultado = "par"
        else:
            resultado = "impar"
        print(f"{n} es {resultado}")
    finally:
        print("Fin de iteración\n")