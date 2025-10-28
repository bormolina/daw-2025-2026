def multiplos(n: int, inicio: int, final: int):
    print(f"Entre {inicio} y {final} el número {n} tiene los siguientes múltiplos: ")
    for i in range(inicio, final+1):
        if i % n == 0:
            print(i)

n = int(input("Introduce un número: "))
inicio = int(input("Introduce el inicio: "))
final = int(input("Introduce el final: "))

multiplos(n, inicio, final)
