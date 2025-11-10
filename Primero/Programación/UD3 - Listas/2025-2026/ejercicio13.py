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

sumatoria = 0

for prec in precipitaciones_granada_2023:
    sumatoria += prec

media = sumatoria / len(precipitaciones_granada_2023)

for i, prec in enumerate(precipitaciones_granada_2023):
    if prec > media:
        print(f"En {meses[i]} llueve {prec} más que la media {media:.1f}")