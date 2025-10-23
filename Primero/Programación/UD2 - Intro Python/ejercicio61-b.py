# Versión con funciones. Más modular y escalable

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except:
            print("Número incorrecto")

a = pedir_entero("Inserta el primer número: ")
b = pedir_entero("Inserta el segundo número: ")

resultado = a + b
print(f"La suma de {a} y {b} es {resultado}")