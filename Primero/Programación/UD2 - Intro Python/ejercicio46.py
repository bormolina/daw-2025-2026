import math

while True:
    a = float(input("Inserta el término a: "))
    if a == 0:
        break
    b = float(input("Inserta el término b: "))
    c = float(input("Inserta el término c: "))

    discriminante = math.sqrt(b*b-4*a*c)
    denominador = 2*a
    solucion1 = (-b+ discriminante)/denominador
    solucion2 = (-b- discriminante)/denominador

    print(f"Para la ecuación: {a}*x² + {b}x + {c}, las soluciones son:")
    print(f"Solución 1 = {solucion1}")
    print(f"Solución 2 = {solucion2}")