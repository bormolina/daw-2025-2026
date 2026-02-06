from LibroPocho import LibroPocho

l1 = LibroPocho("978-958-481-533-0", "La divina comedia", ["Dante Alighieri"], ["Epopeya", "Aventura"], 12831, 15.00)
l2 = LibroPocho("978-958-481-533-0", "La divina comedia", ["Dante Alighieri"], ["Epopeya", "Aventura"], 12831, 15.00)
l3 = l2

print(l1 == l2) # Devuelve False
print(l2 == l3) # Devuelve True


def calcular_precio_final(precio, impuesto, descuento):
    if impuesto > 0:
        precio_con_impuesto = precio + (precio * impuesto / 100)
    else:
        precio_con_impuesto = precio
    if descuento > 0:
        precio_final = precio_con_impuesto - (precio_con_impuesto * descuento / 100)
    else:
        precio_final = precio_con_impuesto
    return precio_final

def calcular_precio_final(precio: float, impuesto: float=0, descuento: float=0) -> float:
    precio_con_impuesto = precio * (1 + impuesto / 100)
    precio_final = precio_con_impuesto * (1 - descuento / 100)
    return precio_final


calcular_precio_final(100, 21)
print(calcular_precio_final(100, 21, 21))
calcular_precio_final(100, 0, 21)
calcular_precio_final(100, descuento=21)
calcular_precio_final(100)