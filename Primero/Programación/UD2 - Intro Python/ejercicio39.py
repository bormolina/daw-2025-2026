num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

if num1>num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

# No incluyendo el primer ni último número
for i in range(menor+1, mayor):
    print(i)