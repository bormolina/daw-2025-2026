"""Crea una lista con palabras. Crea una segunda lista que contenga sólo las palabras que empiezan por d
"""

palabras = ["Hola", "perro", "abejorro", "Yoda", "Adios"]

# Primera versión, si la a es minúscula y solo minúscula
palabras2 = [p for p in palabras if p[0]=="a"]
print(palabras2)

# Segunda versión, si empieza por a o A
palabras3 = [p for p in palabras if p[0].lower()=="a"]