from datetime import datetime

# Calcula la media de una lista de números
def media(nums: list[float]) -> float:
   sumatoria = 0
   for n in nums:
       sumatoria += n
   
   if len(nums) > 0:
       return sumatoria  / len(nums)
   else:
       return 0
   
# Dada una lista de números devuelve otra lista solo con los pares
def filtrar_pares(nums: list[int]) -> list[int]:
   pares = []
   for n in nums:
       if n % 2 == 0: # es par
           pares.append(n)
   return pares

# Devuelve el máximo de una lista
def maximo(l: list) -> object:
   elem_maximo = l[0]
   for e in l:
       if e > elem_maximo:
           elem_maximo = e
   return elem_maximo

# Funcion extremadamente ineficiente para ordenar
def ordenar(l: list) -> list:
   for i in range(len(l)):
       for j in range(len(l)):
           if l[i] < l[j]:
               temp = l[i]
               l[i] = l[j]
               l[j] = temp
   return l


datos = [12, 7, 4, 19, 2, 8, 3]


print("Datos:", datos)


r1 = media(datos)
print("Resultado 1:", r1)


r2 = filtrar_pares(datos)
print("Resultado 2:", r2)


r3 = maximo(datos)
print("Resultado 3:", r3)


r4 = ordenar(datos)
print("Resultado 4:", r4)


