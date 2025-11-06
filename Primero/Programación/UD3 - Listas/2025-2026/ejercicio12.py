precipitaciones_granada_2023 = [
   40.2,  # Enero
   35.6,  # Febrero
   45.8,  # Marzo
   50.1,  # Abril
   30.3,  # Mayo
   10.4,  # Junio
   1.2,   # Julio
   5.6,   # Agosto
   20.8,  # Septiembre
   60.5,  # Octubre
   55.3,  # Noviembre
   42.7   # Diciembre
]

meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

# A petición popular hacemos también el que menos llueve

i_max = i_min = 0
prec_max = prec_min = precipitaciones_granada_2023[0]


for i, prec in enumerate(precipitaciones_granada_2023):
    if prec > prec_max:
        prec_max = prec
        i_max = i
    
    if prec < prec_min:
        prec_min = prec
        i_min = i

print(f"El mes que más llueve es {meses[i_max]} --> {precipitaciones_granada_2023[i_max]}")
print(f"El mes que menos llueve es {meses[i_min]} --> {precipitaciones_granada_2023[i_min]}")