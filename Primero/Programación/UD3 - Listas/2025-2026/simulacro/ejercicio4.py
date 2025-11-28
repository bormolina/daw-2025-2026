""""
Crea la función sin_repetidos(l: list) que dada una lista de números devuelva otra lista que contenga los números de la primera lista pero sin repeticiones. La lista original NO debe ser cambiada. 
"""

def sin_repetidos(l: list[int]) -> list[int]:
    l2 = []
    for e in l:
        if l2.count(e) == 0:
            l2.append(e)

    return l2

l = [1, 1, 2, 2, 3, 4, 5, 5]
print(sin_repetidos(l))
print(l)
