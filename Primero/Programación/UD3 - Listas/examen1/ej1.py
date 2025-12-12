nombres = ["Cuarzo", "Pirita", "Hematita", "Galena", "Fluorita", "Calcita", "Magnetita", "Malaquita", "Obsidiana", "Apatito"]
pesos = [2.65, 5.02, 5.26, 7.6, 3.18, 2.71, 5.17, 3.9, 2.4, 3.2]
es_magnetico = [False, False, False, False, False, False, True, False, False, False]

apartadoA = [nombre for nombre in nombres if len(nombre) <= 7 and nombre[-1] != 'a']
print(apartadoA)

media = sum(pesos) / len(pesos)
apartadoB = []
for i, nombre in enumerate(nombres): 
    if not es_magnetico[i] and pesos[i] > media:
        apartadoB.append(nombre)

print(apartadoB)