mermeladas = [
    ["DulceSol Fresa", ["fresa", "limon"], 55, False],
    ["VerdeBosque Arandanos", ["arandanos", "manzana"], 60, True],
    ["CampoClaro Melocoton", ["melocoton", "limon"], 48, True],
    ["SolAndaluz Naranja", ["naranja"], 52, False],
    ["MonteMiel Mango", ["mango", "limon"], 58, False],
    ["EcoHuerta Higo", ["higo"], 45, True],
    ["RocaDulce Ciruela", ["ciruela"], 49, True],
    ["BosqueRojo Frambuesa", ["frambuesa", "manzana"], 62, False],
]


# Apartado A
apartado_a = [mermelada[0] for mermelada in mermeladas if mermelada[3]]
print(apartado_a)

apartado_a2 = [nombre for nombre, _, _, eco in mermeladas if eco]
print(apartado_a2)

# Apartado B
apartado_b = [nombre for nombre, ingredientes, _, eco in mermeladas if not eco and len(ingredientes) > 1]
print(apartado_b)

# Apartado C
media = sum([azucar for _,_,azucar,_ in mermeladas]) / len(mermeladas)
apartado_c = [nombre for nombre,_,azucar,_ in mermeladas if azucar > media]
print(apartado_c)

# Apartado D
apartado_d = [nombre for nombre, ingredientes, azucar, eco in mermeladas if not eco and 'limon' in ingredientes and azucar > media]
print(apartado_d)
