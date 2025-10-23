def kg2libras(peso: float) -> float:
    return peso / 0.453592

while True:
    peso = float(input("Inserta un peso en kilogramos: "))

    if peso <= 0:
        break

    pesoLibras = kg2libras(peso)
    print(f"{peso} kilos son {pesoLibras} libras")