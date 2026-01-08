clasicas = ["Fresa", "Melocoton", "Naranja", "Albaricoque", "Ciruela"]
ecologicas = ["Fresa", "Higo", "Ciruela", "Arandanos"]
gourmet = ["Frambuesa", "Arandanos", "Naranja", "Mango"]

'''
a) (0.5 puntos) Muestra por pantalla las mermeladas que aparecen tanto en el catálogo ecológico como en el gourmet.
b) (0.5 puntos) Muestra por pantalla las mermeladas que aparecen en el catálogo clásico o en el gourmet, pero que no aparecen en el catálogo ecológico.
'''

apartado_a = set(ecologicas) & set(gourmet)
print(apartado_a)

apartado_b = (set(clasicas) | set(gourmet)) - set(ecologicas)
print(apartado_b)

