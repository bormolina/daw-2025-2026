def mostrar_menu() -> None:
   print('''
--- ALMACEN DE ROPA ---
1. Añadir producto
2. Actualizar producto
3. Lista de productos
4. Salir
''')
   
def añadir_producto(almacen: dict[str, int]) -> dict[str, int]:
    producto = input('¿Cómo se llama el producto?: ')
    if producto in almacen:
        print('Este producto ya está registrado en el almacén')
    else:
        almacen[producto] = int(input('¿Cuántas unidades hay?: '))

    return almacen

almacen = {
    'camisetas': 3,
    'gorras': 5,
    'pantalones': 2
}

while True:
    mostrar_menu()
    opc = int(input('¿Qué quieres hacer?: '))
    match opc:
        case 1:
            almacen = añadir_producto(almacen)

        case 2:
            producto = input('¿Qué producto quieres actualizar?: ')
            if producto in almacen:
                act = int(input('Escribe un número positivo para sumar unidades y uno negativo para restar: '))
                almacen[producto] += act
            else:
                print('El producto nó está registrado en el almacén')
                opc = input('¿Quieres añadirlo? s/n: ')
                if opc == 's':
                    almacen = añadir_producto(almacen)

        case 3:
            print('Listado de productos:')
            for producto, unidades in almacen.items():
                print(f'{producto}: {unidades} unidades')

        case 4:
            print('Nos vemos :P')
            break