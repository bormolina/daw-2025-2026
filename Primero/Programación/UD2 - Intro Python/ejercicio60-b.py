# Versión más larga con excepciones anidadas pero en la que sí detectamos en qué número de los dos se produce el error

try:
    a = float(input("Introduce el primer número: "))
except Exception as error:
    print(f"Error al introducir el primer número: {error}")
else:
    try:
        b = float(input("Introduce el segundo número: "))
    except Exception as error:
        print(f"Error al introducir el segundo número: {error}")
    else:
        suma = a + b
        print(f"La suma de {a} y {b} es {suma}")