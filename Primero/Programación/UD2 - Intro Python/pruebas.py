suma = 0
while True:
    num = int(input("Inserta un número: "))
    if num == 0:
        break
    suma = suma + num
print(f"La suma de los números introducidos es: {suma}")