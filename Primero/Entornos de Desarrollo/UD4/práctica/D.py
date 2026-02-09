from B import B
from C import C

b = C()

while True:
    if len(b.a1) < 5:
        print("Sin cartas suficientes. Fin.")
        break

    x = input("1 = robar | 0 = salir: ")
    if x == "0":
        break
    if x != "1":
        continue

    cartas = b.m2(5)
    if cartas is None:
        print("Sin cartas suficientes. Fin.")
        break

    m = B(cartas)
    print(m)
    print(m.m1())
    print(m.m2())