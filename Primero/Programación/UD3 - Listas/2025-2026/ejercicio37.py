"""
Crea un programa que lea números hasta que insertes un cero. Al finalizar el programa deberá mostrar:
El mayor de los números introducidos
El menor de los números introducidos
La media de los números introducidos

"""

import statistics

nums = []

while True:
    n = int(input('Inserta un número: '))

    if n == 0:
        break
    
    nums.append(n)

print(f"El mayor es {max(nums)}")
print(f"El minimo es {min(nums)}")
print(f"La media es {sum(nums)/len(nums)}")
# También podemos calcular la media llamando a la biblioteca statistics
print(f"La media es {statistics.mean(nums)}")

