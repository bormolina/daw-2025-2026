minimo = None
maximo = None

while True:
   n = int(input("Introduce un número (0 para salir): "))
   if n == 0:
       break
   # Si es el primer número, inicializamos
   if minimo is None or maximo is None:
       minimo = n
       maximo = n
   else:
       if n < minimo:
           minimo = n
       if n > maximo:
           maximo = n


if minimo is None:
   print("No se introdujo ningún número.")
else:
   print(f"El número mínimo es {minimo}")
   print(f"El número máximo es {maximo}")