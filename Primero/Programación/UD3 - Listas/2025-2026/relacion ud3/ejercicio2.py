'''
Crea una función que dadas una lista de números y un número n determine si todos los números de la lista son mayores o iguales a n. La función deberá devolver True o False.  
'''

def mayor_igual(lista: list[int], n: int)-> bool:
    return n <= min(lista)

lista = [4,7,5,10,12]
n = 2

print(mayor_igual(lista, n))