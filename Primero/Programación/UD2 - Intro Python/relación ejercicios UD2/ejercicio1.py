sumatoria = cantidad = media = 0
minimo = maximo = None

while sumatoria < 100:
    n = int(input("Inserta un número: "))

    sumatoria = sumatoria + n
    cantidad = cantidad + 1

    if minimo is None and maximo is None:
        minimo = n
        maximo = n
    else:
        if n > maximo:
            maximo = n
        
        if n < minimo: 
            minimo = n

media = sumatoria / cantidad

print(f"a) Cantidad de números = {cantidad}")
print(f"b) Suma total = {sumatoria}")
print(f"c) Media = {media}")
print(f"d) Mínimo = {minimo}")
print(f"d) Máximo = {maximo}")