dineroTotal = int(input("Cuánto dinero quieres sacar?"))
dinero = dineroTotal

billetes50 = dinero // 50
dinero = dinero % 50
billetes20 = dinero // 20
dinero = dinero % 20
billetes10 = dinero // 10
dinero = dinero % 10
billetes5 = dinero // 5

print(f"{dineroTotal}€ son {billetes50} billetes de 50€, {billetes20} billetes de 20€, {billetes10} billetes de 10€ y {billetes5} billetes de 5€")