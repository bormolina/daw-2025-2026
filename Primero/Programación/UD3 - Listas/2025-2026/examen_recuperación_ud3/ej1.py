sabores = ["Fresa", "Melocoton", "Naranja", "Arandanos", "Higo", "Albaricoque", "Mango", "Frambuesa", "Ciruela", "Limon"]
azucar = [55, 48, 52, 60, 45, 50, 58, 62, 49, 47]
es_light = [False, True, False, False, True, True, False, False, True, True]


# Apartado A
apartado_a = [sabor for i, sabor in enumerate(sabores) if len(sabor) <= 6 and not es_light[i]]
print(apartado_a)

# Apartado B
media = sum(azucar) / len(azucar)
apartado_b = [sabor for i, sabor in enumerate(sabores) if not es_light[i] and azucar[i] < media]
print(apartado_b)
