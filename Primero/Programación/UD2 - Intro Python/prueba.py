# Función que calcula el rango de peso en función del imc
# El peso se define en kg y la altura en metros
def imc(peso: float,  altura: float) -> str:
    imc = peso/(altura*altura)
    if imc < 18.5:
        resultado = "Peso bajo"
    elif imc >= 18.5 and imc< 24.9:
        resultado = "Peso óptimo"
    elif imc >= 24.9 and imc < 30:
        resultado = "Sobrepeso"
    else:
        resultado = "Obesidad"
   
    return resultado

altura = float(input("Inserta tu altura: "))
peso = float(input("Inserta tu peso: "))
rangoPeso = imc(altura, peso)
print(rangoPeso)