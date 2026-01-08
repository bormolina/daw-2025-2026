def imprimir_menu():
    print("MENÚ")
    print("1) Ver mermeladas")
    print("2) Insertar mermelada")
    print("0) Salir")

def registrar_mermelada() -> list:
    nombre = input('Nombre de la mermelada: ')
    ingredientes = input('Ingredientes separados por comas: ').split(',')
    azucar = int(input('Cantidad de azúcar: '))
    eco = input('Es eco? (S/N): ')
    if eco == 'S':
        eco = True
    else:
        eco = False
    return [nombre, ingredientes, azucar, eco]

mermeladas = []

while True:
    imprimir_menu()
    opcion = int(input('Elige una opción: '))

    if opcion == 0:
        break
    elif opcion == 1:
        if len(mermeladas) == 0:
            print('No hay mermeladas registradas')
        else:
            for mermelada in mermeladas:
                print(mermelada)
    elif opcion == 2:
        mermeladas.append(registrar_mermelada())

