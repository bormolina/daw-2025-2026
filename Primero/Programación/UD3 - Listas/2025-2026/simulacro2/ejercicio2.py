from random import randint

aleatorios = [randint(0, 100) for _ in range(20)]
nums_filtrados = [n for n in aleatorios if n % 5 == 0]