def tablaMultiplicar(num: int):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

for i in range(1, 11):
    print(f"Tabla del {i} :")
    tablaMultiplicar(i)

# Además de escribir las tablas del 1 al 10 también le pido al usuario una
tabla = int(input("Inserta la tabla que quieres saber: "))
tablaMultiplicar(tabla)