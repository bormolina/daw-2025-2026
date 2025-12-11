carrito = {
    "manzanas": "5",
    "platanos:": "3",
    "leche": "2"
}

while True:
    print(f"Carrito: {carrito}")
    print("1.Añadir un producto al carrito")
    print("2.Modificar cantidad de un producto existente")
    print("3.Quitar un producto del carrito")
    print("0.Salir")
    respuesta = int(input("Elige: "))

    match respuesta:
        case 0:
            break

        case 1:
            nombre = input("Introduce el nombre del producto: ")
            if nombre not in carrito:
                cantidad = input("Introduce la cantidad: ")
                carrito[nombre] = cantidad
            else:
                print("Ese producto ya esta en el carrito")

        case 2:
            nombre = input("Introduce el nombre del producto del que quieres cambiar su cantidad: ")
            if nombre in carrito:
                cantidad = input("Introduce la cantidad: ")
                carrito[nombre] = cantidad
            else:
                print("Ese producto no esta en el carrito")
        case 3:
            nombre = input("Introduce el nombre del producto que quieres borrar: ")
            if nombre in carrito:
                carrito.pop(nombre)
            else:
                print("Ese producto no esta en el carrito")
