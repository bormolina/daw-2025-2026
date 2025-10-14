nTerminos = int(input("¿Cuántos términos quieres?"))
i = 0

while i<=nTerminos:
    if i == 0:
        terminoAnterior = 0
        print(terminoAnterior)

    if i == 1:
        terminoActual = 1
        print(terminoActual)

    if i >= 2:
        nuevoTermino = terminoAnterior+terminoActual
        print(nuevoTermino)
        terminoAnterior = terminoActual
        terminoActual = nuevoTermino    

    i = i + 1