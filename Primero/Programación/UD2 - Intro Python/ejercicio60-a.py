# Versión más simple pero en la que no detectamos en qué número se produce el error

try:
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
except Exception as error:
    print(f"Se ha producido un error: {error}")
else:
    suma = a + b
    print(f"La suma de {a} y {b} es {suma}")
