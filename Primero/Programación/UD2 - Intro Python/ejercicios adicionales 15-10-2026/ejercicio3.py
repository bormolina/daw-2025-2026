mes1 = int(input("Inserta un mes (1-12): "))
mes2 = int(input("Inserta otro mes (1-12): "))

# Os dejo a vosotros la gestión del nombre del mes y el número de dias

# Gestionamos cuando el primer mes es el que más días tiene
if (mes1 == 1 or mes1 == 3 or mes1 == 5 or mes1 == 7 or mes1 == 8 or mes1 == 10 or mes1 == 12) and (mes2 == 2 or mes2 == 4 or mes2 == 6 or mes2 == 9 or mes2 == 11):
    print(f"El primer mes es mayor que el segundo")
elif (mes2 == 1 or mes2 == 3 or mes2 == 5 or mes2 == 7 or mes2 == 8 or mes2 == 10 or mes2 == 12) and (mes1 == 2 or mes1 == 4 or mes1 == 6 or mes1 == 9 or mes1 == 11):
    print(f"El segundo mes es mayor que el primero")
else:
    print(f"Son iguales")